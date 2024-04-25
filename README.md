# 🤗 HuggingFace Model Downloader

This Python script allows you to download models from Hugging Face's model hub. It takes a URL of a model page on the Hugging Face website, identifies the download links for the model files, and downloads them to a specified directory. 
### ⚠️ IMPORTANT NOTE
The link must me the tab of the `Files and versions` in the HF model page. 
(Example: [https://huggingface.co/TheBloke/Llama-2-7B-AWQ/tree/main])


### 🚀 Usage

This project is built with the Poetry framework, ensuring smooth dependency management. Follow these steps to get started:

1. Installation: First, make sure you have Poetry installed. Navigate to the project directory containing the `pyproject.toml` file and run:

```bash
poetry install
```

This command will automatically install all required dependencies.

2. Activate Poetry Shell: To activate the Poetry shell, run:

```bash
poetry shell
```

3. Run the Script: Finally, execute the script using the following command:

```bash
python downloader.py
```

### ℹ️ Notes

* This script assumes that the model files are available for download directly from the provided URL.
* It's recommended to ensure that you have sufficient disk space before downloading large models.
* Depending on your internet connection and the size of the model files, the download process may take some time.


### 📜 Disclaimer
This script is provided as-is without any warranties. Use it responsibly and respect the terms of use of the Hugging Face model hub.

For more information, visit [Hugging Face](https://huggingface.co/).