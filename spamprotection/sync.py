import requests

from .errors import UnknownError
from .types import Blacklist

from json import JSONDecodeError
from typing import Union


class SPBClient:
    def __init__(
        self,
        *,
        host: str = "https://api.intellivoid.net/spamprotection/v1/lookup"
    ) -> None:
        """
        [SPBClient]
        
        Args:
            host (str): [current spam protection lookup endpoint].
        """
        self._host = host

    def do_request(
        self,
        user_id: str,
    ):
        """[Requests to the url]

        Args:
            user_id (str): [username or user_id can be passed into the arg]

        Returns:
            [json]: [json response of the output]
        """
        request = requests.get(f"{self._host}?query={user_id}")
        try:
            return request.json(), request
        except JSONDecodeError:
            return request.text(), request

    def raw_output(
        self,
        user_id: Union[int, str]
    ):
        """[raw json output]

        Args:
            user_id (Union[int, str]): [can pass user_id or username]

        Returns:
            [json]: [returns json response]
        """
        try:
            data, _ = self.do_request(user_id)
            return data
        except UnknownError:
            return False

    def check_blacklist(
        self,
        user_id: Union[int, str]
    ) -> Union[Blacklist, bool]:
        """[checks spb for blacklist]

        Args:
            user_id (Union[int, str]): [can pass user_id or username]

        Returns:
            Union[Blacklist, bool]: [Blacklist type]
        """
        try:
            data, _ = self.do_request(user_id)
            return Blacklist(**data)
        except UnknownError:
            return False
