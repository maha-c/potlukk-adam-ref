from fastapi import APIRouter, HTTPException
from random import randint
from app_data import get_details_by_user_id, lukkers, potlukks, notification_queue
from models.dtos import LukkerIn, LukkerUserInfoOut, PotLukkerRegistrationDetails
from models.types import Lukker

def lukker_in_to_lukker(lukker: LukkerIn):
    return Lukker(
        userId=lukker.userId,
        username=lukker.username,
        password=lukker.password,
        fname=lukker.fname,
        lname=lukker.lname,
        allergies=lukker.allergies
    )

router = APIRouter()

@router.post("/lukkers", response_model = LukkerUserInfoOut)
def create_user(user: PotLukkerRegistrationDetails) -> LukkerUserInfoOut:
    lukker = Lukker(
        userId = randint(10000,99999),
        username= user.username,
        password= user.password,
        fname= user.fname,
        lname= user.lname,
        allergies= user.allergies
    )
    lukkers[lukker.userId] = lukker
    return lukker.as_lukker_info_out()
    

@router.get("/lukkers", response_model=list[LukkerUserInfoOut])
def get_all_users() -> list[LukkerUserInfoOut]:
    return [u.as_lukker_info_out() for u in lukkers.values()]


@router.get("/lukkers/{id}", response_model=LukkerUserInfoOut)
def get_user_by_id(id: int) ->LukkerUserInfoOut:

    if lukker := lukkers.get(id):
        return lukker.as_lukker_info_out()

    raise HTTPException(status_code=404)


@router.put("/lukkers/{id}", response_model=LukkerUserInfoOut)
def update_user(id: int, lukker: LukkerIn) -> LukkerUserInfoOut:
    try:
        lukkers[id] = lukker_in_to_lukker(lukker)
        for potlukk in potlukks.values():

            if potlukk.host.userId == id:
                potlukk.host = lukker_in_to_lukker(lukker).as_user_details()
            
            for invite in potlukk.invitations:
                if invite.potlukker.userId == id:
                    invite.potlukker = lukker_in_to_lukker(lukker).as_user_details()
        
        return lukker_in_to_lukker(lukker).as_lukker_info_out()
            
    except Exception as e:
        raise HTTPException(status_code=404)
    
