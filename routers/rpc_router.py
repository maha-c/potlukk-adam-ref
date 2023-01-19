from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app_data import get_details_by_user_id, lukkers, potlukks, notification_queue
from models.dtos import LukkerUserInfoOut, PotlukkerCredentials

router = APIRouter()


@router.post("/verify", response_model = LukkerUserInfoOut)
def signin(credentials: PotlukkerCredentials) -> LukkerUserInfoOut:

    for lukker in list(lukkers.values()):
        if lukker.username == credentials.username and lukker.password:
            return lukker.as_lukker_info_out()
            
    raise HTTPException(status_code=404)

