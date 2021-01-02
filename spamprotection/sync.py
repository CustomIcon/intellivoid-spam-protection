import requests

from .errors import UnknownError
from .types import Blacklist

from json import JSONDecodeError
from typing import Union


class SPBClient:
    def __init__(
        self, *, host: str = "https://api.intellivoid.net/spamprotection/v1/lookup"
    ) -> None:
        self._host = host

    def do_request(self, user_id: str, method: str = "get"):
        request = requests.get(f"{self._host}?query={user_id}")
        try:
            return request.json(), request
        except JSONDecodeError:
            return request.text(), request

    def raw_output(self, user_id: Union[int, str]) -> Union[Blacklist, bool]:
        try:
            data, _ = self.do_request(user_id)
            return data
        except UnknownError:
            return False

    def check_blacklist(self, user_id: Union[int, str]) -> Union[Blacklist, bool]:
        try:
            data, _ = self.do_request(user_id)
            return Blacklist(**data)
        except UnknownError:
            return False
