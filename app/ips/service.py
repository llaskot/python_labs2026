import bcrypt
import httpx
from fastapi import HTTPException
from sentry_sdk.utils import json_dumps

from app.abstracts import AbstractService
from .repository import ip_repo
from .schemas import IpCreate, IpUpdate, IpCheck

URL = 'http://ip-api.com/json'

class IpService(AbstractService[IpCreate, IpUpdate]):
    def __init__(self):
        super().__init__(ip_repo)

    async def find_by_ip(self, data: IpCheck):
        res = None
        try:
            res = await self.repo.get_by_ip(data.ip)
        except Exception as e:
            print(e)
        if res :
            res['source'] = 'db'
            return res
        else:
            async with httpx.AsyncClient() as client:
                resp = await client.get(f'{URL}/{str(data.ip)}')
                resp.raise_for_status()
                res = resp.json()
                if res['status'] != "success":
                    raise HTTPException(status_code=400, detail=res)
            res['ip'] = res.pop('query')
            create_dto = IpCreate(**res)
            new_item  = await self.repo.create(create_dto)
            new_item.source = 'outside API'
            return new_item.model_dump(by_alias=True)

