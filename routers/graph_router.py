from random import randint
from time import time
from typing import AsyncGenerator
import strawberry
from strawberry.fastapi import GraphQLRouter
from models.types import *
from models.inputs import *
from models.enums import *
from resolvers.queries import lukkers_resolver, notification_resolver, potlukks_resolver
from resolvers.mutations import add_notification, create_potlukk, swap_potlukk_dishes, swap_potlukk_details, send_invite, update_invite
from resolvers.subscriptions import notifcation_subscription


@strawberry.type
class Query:
    potlukks: list[Potlukk] = strawberry.field(resolver=potlukks_resolver)
    notifications: list[PotlukkNotification] = strawberry.field(resolver=notification_resolver)
    lukkers: list[LukkerUserInfo] = strawberry.field(resolver=lukkers_resolver)


@strawberry.type
class Mutation:
    add_notification: PotlukkNotification = strawberry.mutation(resolver=add_notification)
    create_potlukk: Potlukk | None = strawberry.mutation(resolver=create_potlukk)
    swap_potlukk_details: Potlukk | None = strawberry.mutation(resolver=swap_potlukk_details)
    swap_potlukk_dishes: Potlukk | None = strawberry.mutation(resolver=swap_potlukk_dishes)
    send_invite: Potlukk | None = strawberry.mutation(resolver=send_invite)
    update_invite: Potlukk | None = strawberry.mutation(resolver=update_invite)


@strawberry.type
class Subscription:
    notifcation_subscription: AsyncGenerator[list[PotlukkNotification],None] = strawberry.subscription(resolver=notifcation_subscription)

schema = strawberry.Schema(Query,Mutation,Subscription)


graphql_app = GraphQLRouter(schema)

