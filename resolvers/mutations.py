from app_data import get_details_by_user_id, lukkers, potlukks, notification_queue
from models.types import *
from models.inputs import *
from models.enums import *
from random import randint
from time import time
from app_data import lukkers, potlukks, notification_queue


def add_notification(input: PotlukkNotificationInput) -> PotlukkNotification:
    notification: PotlukkNotification = PotlukkNotification(
        eventId=randint(10000,99999),
        timestamp = int(time()),
        kind = input.kind,
        description = input.description,
        createdByUser = input.createdByUser,
        affectedPotlukkId = input.affectedPotlukkId
    )
    notification_queue.append(notification)
    return notification

def create_potlukk(input: PotlukkCreationInput) -> Potlukk | None:
    if host := get_details_by_user_id(input.hostId):
        potlukk: Potlukk  = Potlukk(
            potlukkId=randint(100000,999999),
            details= input.details.as_potluck_details(),
            host=host,
            invitations=[],
            dishes=[]
        )
        potlukks[potlukk.potlukkId] = potlukk
        return potlukk
    

def swap_potlukk_details(input: PotlukkDetailsSwapInput) -> Potlukk | None:
    if potluk := potlukks.get(input.potlukkId):
        fields = input.__dict__
        del fields["potlukkId"]
        potluk.details = PotlukkDetails(**fields)      
        return potluk
        
def swap_potlukk_dishes(input: DishesSwapInput) -> Potlukk | None:
    if potluk := potlukks.get(input.potlukkId):
        potluk.dishes = [d.as_dish() for d in input.dishes]
        return potluk

def send_invite(input: InvitationSendInput) -> Potlukk | None:
    if potluk := potlukks.get(input.potlukkId):
        for invite in potluk.invitations:
            if invite.potlukker.userId == input.potlukkerId:
                raise Exception("Person already invited")
        if lukker := get_details_by_user_id(input.potlukkerId):
            potluk.invitations.append(Invitation(status=InvitationStatus.PENDING, potlukker=lukker))
            return potluk


def update_invite(input: InvitationUpdateInput) -> Potlukk | None:
    if potluk := potlukks.get(input.potlukkId):
        for invite in potluk.invitations:
            if invite.potlukker.userId == input.potlukkerId:
                invite.status = input.status
                return potluk