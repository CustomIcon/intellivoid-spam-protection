from json import JSONDecodeError
from typing import Union

import aiohttp
from .errors import UnknownError
from .types import Blacklist


class SPBClient:
    def __init__(
        self, *, host: str = "https://api.intellivoid.net/spamprotection/v1/lookup"
    ) -> None:
        self._host = host

    async def do_request(self, user_id: str, method: str = "get"):
        async with aiohttp.ClientSession() as ses:
            request = await ses.get(f"{self._host}?query={user_id}")
        try:
            return await request.json(), request
        except JSONDecodeError:
            return await request.text(), request

    async def raw_output(self, user_id: Union[int, str]) -> Union[Blacklist, bool]:
        try:
            data, _ = await self.do_request(user_id)
            return data
        except UnknownError:
            return False

    async def check_blacklist(self, user_id: Union[int, str]) -> Union[Blacklist, bool]:
        try:
            data, _ = await self.do_request(user_id)
            return Blacklist(**data)
        except UnknownError:
            return False
        except aiohttp.client_exceptions.ClientConnectorError:
            return "Api is down at the moment"
