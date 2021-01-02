# Welcome to the unofficial intellivoid-spam-protection wiki!

This library handles All Requests done to https://api.intellivoid.net/spamprotection/v1/lookup. To understand how this is meant to be used, please see read the following [Documentation](https://github.com/pokurt/intellivoid-spam-protection/wiki)

## Getting Started
- Installing the library:
 
    `pip install git+https://github.com/pokurt/intellivoid-spam-protection`

- For those who wants to try out Development Builds:

    `pip install git+https://github.com/pokurt/intellivoid-spam-protection@dev`

## Usage

```
from spamprotection import SPBClient
import asyncio

client = SPBClient()

async def main():
    user = input("Enter a Username or UserID to check Spam Prediction on SPB: ")
    status = await client.check_blacklist(user)
    if status.success:
        print((await text_parser(status.private_telegram_id)))
    else:
        print("Polish Cow did not Approve this!")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
```