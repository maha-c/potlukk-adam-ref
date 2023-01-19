from models.types import *
from models.inputs import *
from models.enums import *
from app_data import lukkers, potlukks, notification_queue


def potlukks_resolver() -> list[Potlukk]:
    return list(potlukks.values())

def notification_resolver() -> list[PotlukkNotification]:
    return notification_queue

def lukkers_resolver() -> list[LukkerUserInfo]:
    return [x.as_user_details() for x in lukkers.values()]