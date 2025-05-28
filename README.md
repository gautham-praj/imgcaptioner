# Image Captioning API

This project provides a REST API for generating descriptive captions of images using a pretrained Vision Transformer (ViT) encoder and GPT-2 decoder model from Hugging Face. Users can send an image URL to the API and receive a caption describing the content of the image.

---

## Table of Contents

- [Features](#features)  
- [Technology Stack](#technology-stack)    
- [How It Works](#how-it-works)  

---

## Features

- Generates captions for images using a state-of-the-art pretrained VisionEncoderDecoder model from Hugging Face.
- Supports image input via URL.
- Asynchronous image fetching with `httpx`.
- Easy to extend and integrate.

---

## Technology Stack

- Python 3.9+  
- FastAPI - Web framework  
- Hugging Face Transformers - VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer  
- PyTorch - Model inference  
- Pillow (PIL) - Image processing  
- HTTPX - Async HTTP client  

---

## How It Works
- The API receives a POST request with an image URL.
- The server downloads the image asynchronously using HTTPX.
- The image is processed with Pillow.
- The image is passed to a pretrained VisionEncoderDecoder model to generate a caption.
- The caption is returned in the JSON response.
