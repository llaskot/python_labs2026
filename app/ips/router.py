from fastapi import Response, Request, HTTPException, APIRouter, Depends
from pymongo.errors import PyMongoError

from .schemas import IpCheck, IpResponse
from .service import IpService
from app.auth import check_token
from app.users import UserPermissionsDto

router = APIRouter(prefix="/ips", tags=["IPs"])


@router.post("/",
             response_model=IpResponse
             )
async def find_by_ip(data: IpCheck,
                     user: UserPermissionsDto = Depends(check_token)):
    auth_service = IpService()
    try:
        ip_info = await auth_service.find_by_ip(data, user)
        return ip_info

    except HTTPException as e:
        raise e from e
    except  PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error:\n {str(e)}") from e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: \n{str(e)}") from e
