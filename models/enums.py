from enum import Enum
import strawberry
from pydantic import BaseModel

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