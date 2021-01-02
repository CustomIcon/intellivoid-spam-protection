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
    if status.attributes.is_blacklisted:
        text += "Blacklist Flag: {}\n".format(status.attributes.blacklist_flag)
        text += "Blacklist Reason: {}\n".format(status.attributes.blacklist_reason)
    text += "Original PrivateID: {}\n".format(status.attributes.original_private_id)
    if status.attributes.is_potential_spammer:
        text += "This user is a Spammer\n"
    if status.attributes.is_operator:
        text += "This user is an Operator\n"
    if status.attributes.is_agent:
        text += "This user is an Agent\n"
    if status.attributes.is_whitelisted:
        text += "This user is Whitelisted\n"
    if status.attributes.intellivoid_accounts_verified:
        text += "This user is an Intellivoid Verified Account\n"
    if status.attributes.is_official:
        text += "This is an Official Account\n"
    text += "Language: {}\n".format(status.language_prediction.language)
    text += "Language Probability: {}\n".format(status.language_prediction.probability)
    text += "Ham Prediction: {}\n".format(status.spam_prediction.ham_prediction)
    text += "Spam Prediction: {}\n".format(status.spam_prediction.spam_prediction)
    text += "Last Updated On: {}\n".format(status.last_updated)
    return text


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
