
import aiohttp
import os
from dotenv import load_dotenv
load_dotenv()

NFT_STORAGE_API = os.getenv("NFT_STORAGE_API")

async def upload_to_ipfs(file):
    url = "https://api.nft.storage/upload"
    headers = {"Authorization": f"Bearer {NFT_STORAGE_API}"}
    async with aiohttp.ClientSession() as session:
        data = await file.read()
        async with session.post(url, data=data, headers=headers) as res:
            result = await res.json()
            return f"https://ipfs.io/ipfs/{result['value']['cid']}"
