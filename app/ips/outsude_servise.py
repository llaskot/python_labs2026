import httpx
from fastapi import HTTPException

URL = 'http://ip-api.com/json'

async def get_ip_info(ip_address: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f'{URL}/{ip_address}')
        resp.raise_for_status()
        res = resp.json()
        if res['status'] != "success":
            raise HTTPException(status_code=400, detail=res)
        return res