from enum import Enum
import strawberry
from pydantic import BaseModel

from models.enums import Allergen, InvitationStatus, NotificationKind, PotlukkStatus
from models.types import Dish, PotlukkDetails

@strawberry.input
class PotlukkNotificationInput:
    kind: NotificationKind
    description: str
    affectedPotlukkId: int
    createdByUser: int


@strawberry.input
class PotlukkDetailsCreationInput:
    title: str
    location: str
    status: PotlukkStatus 
    description: str 
    isPublic: bool
    time: int
    tags: list[str]

    def as_potluck_details(self,) -> PotlukkDetails:
        return PotlukkDetails(
            title=self.title,
            location=self.location,
            status=self.status,
            description=self.description,
            isPublic=self.isPublic,
            time=self.time,
            tags=self.tags
        )

@strawberry.input
class PotlukkCreationInput:
    details: PotlukkDetailsCreationInput
    hostId: int

@strawberry.input
class PotlukkDetailsSwapInput:
    potlukkId: int
    title: str 
    location: str 
    status: PotlukkStatus 
    description: str 
    isPublic: bool 
    time: int 
    tags: list[str] 

@strawberry.input
class DishInput:
    name: str 
    description: str
    broughtBy: int = 0
    serves: int 
    allergens : list[Allergen]

    def as_dish(self)-> Dish:
        return Dish(
            name=self.name,
            description=self.description,
            broughtBy=self.broughtBy,
            serves= self.serves,
            allergens=self.allergens
        )

@strawberry.input
class DishesSwapInput:
    potlukkId: int 
    dishes: list[DishInput]

@strawberry.input
class InvitationSendInput:
    potlukkId: int 
    potlukkerId: int

@strawberry.input
class InvitationUpdateInput:
    potlukkId: int 
    potlukkerId: int 
    status: InvitationStatus
