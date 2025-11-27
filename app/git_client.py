import requests
from typing import Final, Any
from http import HTTPMethod 

class GitClient:
    _URL: Final[str] = "https://api.github.com/users/{username}/events"


    def __init__(self):
        pass

    def __fetch(self, url: str, body: dict, head: dict) -> Any:
        response = requests.request(
            method=HTTPMethod.GET, 
            data=body,
            url=url
        )
        response.raise_for_status()
        return response.json()

    def fetch_events(self, username: str = None) -> list[dict]:
        if not username:
            raise ValueError("Username can't be a Null.")

        url: str = self._URL.format(username=username)        
        body: dict = {''}
        head = {''}

        resp: list[dict] = self.__fetch(url, body, head)

        return resp