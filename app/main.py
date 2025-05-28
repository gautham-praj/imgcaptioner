from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
from PIL import Image
from io import BytesIO

from app.utils.captioner import generate_caption  # your caption function

app = FastAPI()

class ImageUrl(BaseModel):
    url: str

@app.post("/caption")
async def caption_image(data: ImageUrl):
    try:
        # Download the image from the URL
        async with httpx.AsyncClient() as client:
            response = await client.get(data.url)
            response.raise_for_status()
        
        # Open image with PIL
        image = Image.open(BytesIO(response.content)).convert("RGB")

        # Generate caption
        caption = generate_caption(image)
        
        return {"caption": caption}

    except httpx.RequestError as e:
        raise HTTPException(status_code=400, detail=f"Error downloading image: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating caption: {e}")
