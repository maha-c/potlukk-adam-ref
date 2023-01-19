from models.types import Lukker, LukkerUserInfo, Potlukk, PotlukkNotification


lukkers: dict[int, Lukker] = {}
potlukks: dict[int, Potlukk] = {}
notification_queue: list[PotlukkNotification] = []

def get_details_by_user_id(id: int) -> LukkerUserInfo | None:
    
    if lukker := lukkers.get(id):
        return LukkerUserInfo(
            userId= lukker.userId,
            username= lukker.username,
            allergies= lukker.allergies,
            fname= lukker.fname,
            lname= lukker.lname
        )
