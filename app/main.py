
from fastapi import FastAPI
from app.routes import nft

app = FastAPI(title="ArtMintFlow - NFT Tokenization Agent")

app.include_router(nft.router, prefix="/nft", tags=["NFT"])
