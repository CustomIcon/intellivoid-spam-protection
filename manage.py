from spamprotection import SPBClient as AsyncClient
from spamprotection.sync import SPBClient as SyncClient
from spamprotection.types import Blacklist
import asyncio
import logging
logging.basicConfig(level=logging.INFO)


async def async_types_check():
    return AsyncClient()
    

async def async_raw_check():
    return AsyncClient()


def sync_types_check():
    return SyncClient()


def sync_raw_check():
    return SyncClient()


def types_check():
    return Blacklist


if __name__ == "__main__":
    asyncio.run(async_types_check())
    asyncio.run(async_raw_check())
    sync_types_check()
    sync_raw_check()