from enum import Enum
import strawberry
from pydantic import BaseModel

################################################### Enums ####################################################################

@strawberry.enum
class PotlukkStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"

@strawberry.enum
class InvitationStatus(Enum):
    ACCEPTED = "ACCEPTED"
    MAYBE = "MAYBE"
    DECLINED = "DECLINED"
    PENDING = "PENDING"

@strawberry.enum
class NotificationKind(Enum):
    DISH_ADDED = "DISH_ADDED"
    DISH_REMOVED = "DISH_REMOVED"
    POTLUKK_ALTERED = "POTLUKK_ALTERED"
    POTLUKK_CANCELED = "POTLUKK_CANCELLED"
    INVITE_ACCEPTED = "INVITE_ACCEPTED"
    INVITE_DECLINE = "INVITE_DECLINED"
    INVITE_SENT = "INVITE_SENT"

@strawberry.enum
class Allergen(Enum):
    MILK = "MILK"
    EGG = "EGG"
    FISH = "FISH"
    SHELLFISH = "SHELLFISH"
    SOY = "SOY"
    WHEAT = "WHEAT"
    TREENUT = "TREE_NUT"
    PEANUT = "PEANUT"


################################################### Types ####################################################################

@strawberry.type
class PotLukkerUserInfo:
    userId: int
    username: str
    fname: str 
    lname: str
    allergies: list[Allergen]


@strawberry.type
class PotLukker:
    userId: int
    username: str
    password: str 
    fname: str 
    lname: str 
    allergies: list[Allergen]

    def as_user_details(self) -> PotLukkerUserInfo:
        return PotLukkerUserInfo(
            userId=self.userId,
            username=self.username,
            fname= self.fname,
            lname= self.lname,
            allergies= self.allergies
        )

@strawberry.type
class PotLukkerRegistrationDetails:
    username: str
    password: str 
    fname: str 
    lname: str 
    allergies: list[Allergen]



@strawberry.type
class PotlukkerCredentials:
    username: str 
    password: str

@strawberry.type
class Invitation:
    status: InvitationStatus
    potlukker: PotLukkerUserInfo

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
    host: PotLukkerUserInfo
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

################################################### Inputs ####################################################################

@strawberry.input
class PotlukkNotificationInput:
    kind: NotificationKind
    description: str
    affectedPotlukkId: int
    createdByUser: int



@strawberry.input
class PotlukkDetailsInput(PotlukkDetails):
    title: str
    location: str
    status: PotlukkStatus 
    description: str 
    isPublic: bool
    time: int
    tags: list[str]

@strawberry.input
class PotlukkDetailsMergeInput:
    title: str | None = strawberry.UNSET
    location: str | None = strawberry.UNSET
    status: PotlukkStatus | None = strawberry.UNSET
    description: str | None = strawberry.UNSET
    isPublic: bool | None = strawberry.UNSET
    time: int | None = strawberry.UNSET
    tags: list[str] | None = strawberry.UNSET

@strawberry.input
class DishInput(Dish):
    pass

@strawberry.input
class PotlukkCreationInput:
    details: PotlukkDetailsInput
    hostId: int

@strawberry.input
class UpdateDishesInput:
    potlukkId: int 
    dishes: list[DishInput]

@strawberry.input
class MergePotlukkDetailsInput:
    potlukkId: int 
    details: PotlukkDetailsMergeInput  

@strawberry.input
class SendInvitationInput:
    potlukkId: int 
    pottlukkerId: int

@strawberry.input
class UpdateInvitationInput:
    potlukkId: int 
    potlukkerId: int 
    status: InvitationStatus


# App Data
potlukkers: dict[int, PotLukker] = {}
potlukks: dict[int, Potlukk] = {}
potlukkNotifications: list[PotlukkNotification] = []

