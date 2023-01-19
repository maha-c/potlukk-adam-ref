from fastapi import APIRouter, HTTPException
from random import randint
from rpc_router import PotLukkerUserInfoOut
from graph_router import get_details_by_user_id
from models import PotLukker, PotLukkerRegistrationDetails, PotLukkerUserInfo, PotlukkerCredentials, potlukkers, potlukks

router = APIRouter()

@router.post("/lukkers", response_model=PotLukkerUserInfoOut)
def create_user(user: PotLukkerRegistrationDetails) -> PotLukkerUserInfo:
    lukker = PotLukker(
        userId = randint(10000,99999),
        username= user.username,
        password= user.password,
        fname= user.fname,
        lname= user.lname,
        allergies= user.allergies
    )
    potlukkers[lukker.userId] = lukker
    return lukker.as_user_details()
    
@router.get("/lukkers", response_model=list[PotLukkerUserInfoOut])
def get_all_users() -> list[PotLukkerUserInfo]:
    return [u.as_user_details() for u in potlukkers.values()]

@router.get("/lukkers/{id}", response_model=PotLukkerUserInfoOut)
def get_user_by_id(id: int) ->PotLukkerUserInfo:
    if lukker := get_details_by_user_id(id):
        return lukker
    raise HTTPException(status_code=404)

@router.put("/lukkers/{id}", response_model=PotLukkerUserInfoOut)
def update_user(id: int, lukker: PotLukker) -> PotLukkerUserInfo:
    try:
        potlukkers[id] = lukker
        for potlukk in potlukks.values():

            if potlukk.host.userId == id:
                potlukk.host = lukker.as_user_details()
            
            for invite in potlukk.invitations:
                if invite.potlukker.userId == id:
                    invite.potlukker = lukker.as_user_details()
        
        return lukker.as_user_details()
            
    except Exception as e:
        raise HTTPException(status_code=404)
    
