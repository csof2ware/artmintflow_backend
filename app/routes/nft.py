
from fastapi import APIRouter, File, UploadFile, Form
from app.services.ipfs import upload_to_ipfs
from app.services.metadata import generate_metadata

router = APIRouter()

@router.post("/tokenize")
async def tokenize_artwork(
    file: UploadFile = File(...),
    title: str = Form(...),
    description: str = Form(...),
    artist: str = Form(...),
    year: str = Form(...),
    wallet_address: str = Form(...)
):
    image_url = await upload_to_ipfs(file)
    metadata = generate_metadata(
        title, description, artist, year, image_url
    )
    return {"metadata": metadata, "image_url": image_url}
