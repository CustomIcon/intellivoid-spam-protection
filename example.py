from spamprotection import SPBClient
from spamprotection.types import Blacklist
import asyncio

# initializing the client
client = SPBClient()


async def main():
    # calling for status
    user = input("Enter a Username or UserID to check Spam Prediction on SPB: ")
    status = await client.check_blacklist(user)
    # check if status got a successful response
    if status.success:
        print((await text_parser(status)))
    else:
        print("Polish Cow did not Approve this!")


async def text_parser(status: Blacklist):
    text = "Private TelegramID: {}\n".format(status.private_telegram_id)
    text += "Entity Type: {}\n".format(status.entity_type)
    if status.is_blacklisted:
        text += "Blacklist Flag: {}\n".format(status.blacklist_flag)
        text += "Blacklist Reason: {}\n".format(status.blacklist_reason)
    text += "Original PrivateID: {}\n".format(status.original_private_id)
    if status.is_potential_spammer:
        text += "This user is a Spammer\n"
    if status.is_operator:
        text += "This user is an Operator\n"
    if status.is_agent:
        text += "This user is an Agent\n"
    if status.is_whitelisted:
        text += "This user is Whitelisted\n"
    if status.intellivoid_accounts_verified:
        text += "This user is an Intellivoid Verified Account\n"
    if status.is_official:
        text += "This is an Official Account\n"
    text += "Language: {}\n".format(status.language)
    text += "Language Probability: {}\n".format(status.probability)
    text += "Ham Prediction: {}\n".format(status.ham_prediction)
    text += "Spam Prediction: {}\n".format(status.spam_prediction)
    text += "Last Updated On: {}\n".format(status.last_updated)
    return text


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
