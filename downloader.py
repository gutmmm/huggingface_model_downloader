import os
import argparse
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import validators

class HuggingFaceDownloader():
    @classmethod
    def run(cls, url, download_dir):
        cls.download_dir, cls.url = download_dir, url

        cls.check_url()
        cls.check_dir()
        cls.get_webpage_source()
    
    @classmethod
    def check_url(cls):
        if not validators.url(cls.url):
            raise Exception ("Invalid URL")

    @classmethod
    def check_dir(cls):
        if not os.path.isdir(cls.download_dir):
            print(f"Directory {cls.download_dir} does not exist. Creating it now...")
            os.makedirs(cls.download_dir)

    @classmethod
    def get_webpage_source(cls):
        response = requests.get(cls.url)
        webpage_source = BeautifulSoup(response.content, 'html.parser')
        cls.process_webpage_source(webpage_source)

    @classmethod
    def process_webpage_source(cls, webpage_source):
        links = webpage_source.find_all('a', href=lambda href: href and href.endswith("download=true"))
        links = [link['href'] for link in links]
        cls.queue_and_download(links)
   
    @classmethod
    def queue_and_download(cls, download_links):
        for link in download_links:
            filename = os.path.split(link)[-1][:-14]
            url = 'https://huggingface.co' + link
            response = requests.get(url, stream=True)
            total_size_in_bytes = int(response.headers.get('content-length', 0))
            block_size = 1024  # 1 Kibibyte
            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
            with open(os.path.join(cls.download_dir, filename), 'wb') as f:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    f.write(data)
            progress_bar.close()
            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                print("Failed to download: ", filename)
            else:
                print(f"Downloaded: {filename}")


if __name__ == '__main__':
    url = input('Paste here a link to HF model -> ')
    HuggingFaceDownloader.run(url, download_dir='./downloaded_models')
