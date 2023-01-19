from enum import Enum
import strawberry
from pydantic import BaseModel
from models.dtos import LukkerUserInfoOut

from models.enums import Allergen, InvitationStatus, NotificationKind, PotlukkStatus

@strawberry.type
class LukkerUserInfo:
    userId: int
    username: str
    fname: str 
    lname: str
    allergies: list[Allergen]


@strawberry.type
class Lukker:
    userId: int
    username: str
    password: str 
    fname: str 
    lname: str 
    allergies: list[Allergen]

    def as_user_details(self) -> LukkerUserInfo:
        return LukkerUserInfo(
            userId=self.userId,
            username=self.username,
            fname= self.fname,
            lname= self.lname,
            allergies= self.allergies
        )
    
    def as_lukker_info_out(self) -> LukkerUserInfoOut:
        return LukkerUserInfoOut(
            userId= self.userId,
            username=self.username,
            fname=self.fname,
            lname=self.lname,
            allergies=self.allergies
        )




@strawberry.type
class Invitation:
    status: InvitationStatus
    potlukker: LukkerUserInfo

@strawberry.type
class Dish:
    name: str 
    description: str
    broughtBy: int = 0
    serves: int 
    allergens : list[Allergen]

@strawberry.type
class PotlukkDetails:
    title: str
    location: str
    status: PotlukkStatus 
    description: str 
    isPublic: bool
    time: int
    tags: list[str]


@strawberry.type
class Potlukk:
    potlukkId: int 
    details: PotlukkDetails
    host: LukkerUserInfo
    invitations: list[Invitation]
    dishes: list[Dish]


@strawberry.type
class PotlukkNotification:
    eventId: int
    timestamp: int
    kind: NotificationKind
    description: str
    affectedPotlukkId: int
    createdByUser: int