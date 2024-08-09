import requests
from src.config import TOKEN
from abc import abstractmethod


class Action(object):
    def __init__(self, action: str):
        self._action: str = action

    @abstractmethod
    def data(self) -> str:
        pass

    def __str__(self):
        return self._action


class ActifactsAPI(object):
    def __init__(self):
        self.token: str = ''
        self.username: str = ''

    def __headers(self):
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def start(self, username: str, token: str) -> None:
        self.username = username
        self.token = token

    def formulate_link(self, action: str) -> str:
        return f"https://api.artifactsmmo.com/my/{self.username}/action/{action}"

    def send_request(self, action: Action) -> (int, dict):
        headers = self.__headers()
        payload = action.data()

        result = requests.post(self.formulate_link(str(action)), headers=headers, data=payload)
        if result.status_code != 200:
            print(f'Error in request: {result.text}')
        print(result.json())
        return result.status_code, result.json()
