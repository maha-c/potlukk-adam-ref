from pydantic import BaseModel
from models.enums import Allergen, InvitationStatus, NotificationKind, PotlukkStatus


class LukkerUserInfoOut(BaseModel):
    userId: int
    username: str
    fname: str 
    lname: str
    allergies: list[Allergen]


class PotlukkerCredentials(BaseModel):
    username: str 
    password: str


class PotLukkerRegistrationDetails(BaseModel):
    username: str
    password: str 
    fname: str 
    lname: str 
    allergies: list[Allergen]

class LukkerIn(BaseModel):
    userId: int
    username: str
    password: str 
    fname: str 
    lname: str 
    allergies: list[Allergen]

