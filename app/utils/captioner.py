from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import requests
import torch

# Load model and processor
model = VisionEncoderDecoderModel.from_pretrained("ydshieh/vit-gpt2-coco-en")
processor = ViTImageProcessor.from_pretrained("ydshieh/vit-gpt2-coco-en")
tokenizer = AutoTokenizer.from_pretrained("ydshieh/vit-gpt2-coco-en")

# Move model to device (GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_caption(image: Image.Image) -> str:
    try:
        pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)

        output_ids = model.generate(pixel_values, max_length=16)

        caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        return f"Error generating caption: {str(e)}"
