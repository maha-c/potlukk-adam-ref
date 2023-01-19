from fastapi import APIRouter, HTTPException
from graph_router import get_details_by_user_id
from pydantic import BaseModel
from models import Allergen, PotLukker, PotLukkerRegistrationDetails, PotLukkerUserInfo, PotlukkerCredentials, potlukkers, potlukks

router = APIRouter()


class PotLukkerUserInfoOut(BaseModel):
    userId: int
    username: str
    fname: str 
    lname: str
    allergies: list[Allergen]

@router.post("/verify", response_model=PotLukkerUserInfoOut)
def signin(credentials: PotlukkerCredentials) -> PotLukkerUserInfo:

    for lukker in list(potlukkers.values()):
        if lukker.username == credentials.username and lukker.password:
            if details := get_details_by_user_id(lukker.userId):
                return details

    raise HTTPException(status_code=404)

