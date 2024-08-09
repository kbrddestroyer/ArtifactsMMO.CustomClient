import time
import asyncio
from src.API.ArtifactsMMO import Action, ActifactsAPI
from src.API.Actions.CommonActions import *
from src.custom_types.coordinates import Vector2


class Character(object):
    def __init__(self, nickname: str, api: ActifactsAPI):
        self.__name = nickname
        self.__freeze_time: float = 0
        self.__unfreeze_timestamp: int = 0
        self.__api: ActifactsAPI = api

    def __perform_freeze(self, freeze_time: float):
        freeze_ms: int = int(freeze_time * 1000)
        self.__freeze_time = freeze_time
        self.__unfreeze_timestamp = time.time() + freeze_ms

    async def __perform_delayed_action(self, action):
        print(f'Waiting {self.__freeze_time} and performing {action}')
        await asyncio.sleep(self.__freeze_time)
        self.__freeze_time = 0
        self.__unfreeze_timestamp = 0
        await self.__perform_action(action)

    async def __perform_action(self, action: Action):
        print(f'Action: {action}')
        if self.__freeze_time == 0:
            code, json = self.__api.send_request(action)
            if code != 200:
                if code == 499:
                    # Freeze
                    err: str = json['error']['message']
                    cooldown = float(err[len("Character in cooldown: "):-len(' seconds left.')])
                    self.__perform_freeze(cooldown)
                    await self.__perform_delayed_action(action)
                return

            cooldown: float = float(json['data']['cooldown']['total_seconds'])
            self.__perform_freeze(cooldown)
        else:
            await self.__perform_delayed_action(action)

    async def move(self, position: Vector2):
        await self.__perform_action(MoveAction(position))

    async def move(self, x: int, y: int):
        await self.__perform_action(MoveAction(Vector2(x, y)))

    async def fight(self):
        await self.__perform_action(FightAction())
