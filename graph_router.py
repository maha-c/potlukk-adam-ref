import asyncio
from random import randint
from time import time
from typing import AsyncGenerator
import strawberry


from strawberry.fastapi import GraphQLRouter

from models import  Dish, Invitation, InvitationStatus, MergePotlukkDetailsInput, PotLukkerUserInfo, Potlukk, PotlukkCreationInput, PotlukkNotification, PotlukkNotificationInput, SendInvitationInput, UpdateDishesInput, UpdateInvitationInput, potlukks, potlukkNotifications, potlukkers, Potlukk, PotlukkDetails

def get_details_by_user_id(id: int) -> PotLukkerUserInfo | None:
    
    if lukker := potlukkers.get(id):
        return PotLukkerUserInfo(
            userId= lukker.userId,
            username= lukker.username,
            allergies= lukker.allergies,
            fname= lukker.fname,
            lname= lukker.lname
        )


def potlukks_resolver() -> list[Potlukk]:
    return list(potlukks.values())

def notification_resolver() -> list[PotlukkNotification]:
    return potlukkNotifications

def lukkers_resolver() -> list[PotLukkerUserInfo]:
    return [x.as_user_details() for x in potlukkers.values()]


@strawberry.type
class Mutation:

    @strawberry.mutation
    def add_notification(self, input: PotlukkNotificationInput) -> PotlukkNotification:
        notification: PotlukkNotification = PotlukkNotification(
            eventId=randint(10000,99999),
            timestamp = int(time()),
            kind = input.kind,
            description = input.description,
            createdByUser = input.createdByUser,
            affectedPotlukkId = input.affectedPotlukkId
        )
        potlukkNotifications.append(notification)
        return notification

    @strawberry.mutation
    def create_potlukk(self, input: PotlukkCreationInput) -> Potlukk | None:

        if host := get_details_by_user_id(input.hostId):
            potlukk: Potlukk  = Potlukk(
                potlukkId=randint(100000,999999),
                details= input.details,
                host=host,
                invitations=[],
                dishes=[]
            )
            potlukks[potlukk.potlukkId] = potlukk
            return potlukk
    
    @strawberry.mutation
    def swap_potlukk_details(self, input: MergePotlukkDetailsInput) -> Potlukk | None:
        if potluk := potlukks.get(input.potlukkId):
   
            return potluk
        
    @strawberry.mutation
    def swap_potlukk_dishes(self, input: UpdateDishesInput) -> Potlukk | None:
        if potluk := potlukks.get(input.potlukkId):
            potluk.dishes = [x for x in input.dishes]
            return potluk

    @strawberry.mutation
    def send_invite(self, input: SendInvitationInput) -> Potlukk | None:
        if potluk := potlukks.get(input.potlukkId):
            for invite in potluk.invitations:
                if invite.potlukker.userId:
                    raise Exception("Person already invited")
            if lukker := get_details_by_user_id(input.pottlukkerId):
                potluk.invitations.append(Invitation(status=InvitationStatus.PENDING, potlukker=lukker))
                return potluk

    @strawberry.mutation
    def update_invite(self, input: UpdateInvitationInput) -> Potlukk | None:
        if potluk := potlukks.get(input.potlukkId):
            for invite in potluk.invitations:
                if invite.potlukker.userId == input.potlukkerId:
                    invite.status = input.status
                    return potluk


@strawberry.type
class Subscription:

    @strawberry.subscription
    async def notifcation_subscription(self) -> AsyncGenerator[list[PotlukkNotification],None]:

        previous_size = len(potlukkNotifications)

        while True:
            await asyncio.sleep(5)

            if previous_size != len(potlukkNotifications):
                yield potlukkNotifications[-len(potlukkNotifications)-previous_size:]
                previous_size = len(potlukkNotifications)
      

@strawberry.type
class Query:
    potlukks: list[Potlukk] = strawberry.field(resolver=potlukks_resolver)
    notifications: list[PotlukkNotification] = strawberry.field(resolver=notification_resolver)
    lukkers: list[PotLukkerUserInfo] = strawberry.field(resolver=lukkers_resolver)


schema = strawberry.Schema(Query,Mutation, Subscription)


graphql_app = GraphQLRouter(schema)

