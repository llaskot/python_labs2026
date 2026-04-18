from typing import Any, Mapping

from pymongo.results import UpdateResult

from app.abstracts import AbstractRepository
from app.database import db
from .ip_model import Ip
from .schemas import IpCreate, IpUpdate


class IpRepository(AbstractRepository[Ip, IpCreate, IpUpdate]):
    def __init__(self, db):
        self.collect = db["ips"]
        super().__init__(Ip, self.collect)

    # async def get_by_ip(self, item_ip: str) -> Ip:
    #     return await self.collection.find_one({'ip': str(item_ip)})

    async def add_to_lists(self, item_ip: str, update_dto: IpUpdate) -> Ip| None :

        res = await self.collection.update_one(
            {"ip": item_ip},
            {
                "$push": update_dto.model_dump()
            }
        )
        if res.modified_count == 0:
            return None
        else:
            return await self.collection.find_one({'ip': item_ip})


ip_repo = IpRepository(db)
