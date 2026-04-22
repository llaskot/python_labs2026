from typing import Any

from bson import ObjectId

from app.abstracts import AbstractService
from .outsude_servise import get_ip_info
from .repository import ip_repo
from .schemas import IpCreate, IpUpdate, IpCheck
from app.users import UserPermissionsDto


class IpService(AbstractService[IpCreate, IpUpdate]):
    def __init__(self):
        super().__init__(ip_repo)

    async def find_by_ip(self, data: IpCheck, user: UserPermissionsDto) -> dict:
        res = None
        try:
            update_dto = IpUpdate(
                requested_by=ObjectId(user.id),
            )
            res = await self.repo.add_to_lists(str(data.ip), update_dto)
        except Exception as e:
            print(e)
        if res :
            res['source'] = 'db'
            return res

        res = await get_ip_info(str(data.ip))
        res['ip'] = res.pop('query')
        res['requested_by'] = [ObjectId(user.id)]
        create_dto = IpCreate(**res)
        new_item  = await self.repo.create(create_dto)
        new_item.source = 'outside API'
        return new_item.model_dump(by_alias=True)

