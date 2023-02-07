from models.types import *
from models.inputs import *
from models.enums import *
from app_data import lukkers, potlukks, notification_queue


def potlukks_resolver(potlukkId: int | None = None) -> list[Potlukk]:

    if potlukkId:
        if potlukk := potlukks.get(potlukkId):
            return [potlukk]
        else:
            return []

    return list(potlukks.values())

def notification_resolver() -> list[PotlukkNotification]:
    return notification_queue

def lukkers_resolver() -> list[LukkerUserInfo]:
    return [x.as_user_details() for x in lukkers.values()]