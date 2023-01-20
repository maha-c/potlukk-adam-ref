from typing import AsyncGenerator
from models.types import *
from models.inputs import *
from models.enums import *
from app_data import lukkers, potlukks, notification_queue
import asyncio



async def notifcation_subscription() -> AsyncGenerator[list[PotlukkNotification],None]:

    previous_size = len(notification_queue)

    while True:
        await asyncio.sleep(5)

        if previous_size != len(notification_queue):
            yield notification_queue[-len(notification_queue)-previous_size:]
            previous_size = len(notification_queue)