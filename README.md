# Text Extractor

## Description
This is a simple yet powerful text extractor designed to pull text from various file formats. It streamlines the process of digitizing content from images and PDFs, making it an indispensable tool for content management systems, document digitization efforts, and automated text processing workflows. Supported input types include:
- Image
- PDF

This tool aims to provide a hassle-free way to convert your files into editable text formats, enhancing accessibility and efficiency in handling digital documents.

## Installation

You have two options for running the Text Extractor: using Docker for CPU environments or Docker for GPU environments for enhanced performance. Please choose the one that best fits your setup.

### Docker for CPU

To install and run the text extractor in a CPU environment, use the following Docker command:

```bash
docker run -p 58337:58337 -d --name text-extractor cyfeng/text-extractor-core-cpu:latest
```

### Docker for GPU

If you have a GPU and wish to leverage it for better performance, use this Docker command instead:

```bash
docker run -p 58337:58337 -d --name text-extractor cyfeng/text-extractor-core-gpu:latest
```

## Usage

### Via Python Script
To call the text extraction API from a Python script, you can use the requests library as shown in the example below. This method is suitable for integrating text extraction capabilities into your Python applications or scripts.

```python
import requests

def call_extract_text_api(image_file_path):
    url = 'http://127.0.0.1:58337/extract_text'
    files = {'file': open(image_file_path, 'rb')}
    response = requests.post(url, files=files)
    return response.json()

if __name__ == '__main__':
    image_file_path = 'path/to/your/image.jpg'
    result = call_extract_text_api(image_file_path)
    print(result)
```

### Via Curl
Alternatively, you can use the `curl` command to interact with the text extraction API. This method is suitable for quick testing and one-off extractions.

```bash
curl -X 'POST' \
  'http://127.0.0.1:58337/extract_text' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@path/to/your/image.jpg;type=image/jpeg'
```