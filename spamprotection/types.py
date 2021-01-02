from datetime import datetime
from attrdict import AttrDict

class SPB:
    def __str__(self) -> str:
        return f"<{self.__class__.__name__}: {self.__dict__}>"

    def __repr__(self) -> str:
        return self.__str__()


class Blacklist(SPB):
    def __init__(self, success: bool, response_code: int, results=dict, **kwargs):
        self.success = success
        self.response_code = response_code
        self.private_telegram_id = results["private_telegram_id"]
        self.entity_type = results["entity_type"]
        self.attributes = AttrDict(results["attributes"])
        self.language_prediction = AttrDict(results["language_prediction"])
        self.spam_prediction = AttrDict(results["spam_prediction"])
        self.last_updated = datetime.fromtimestamp(results["last_updated"])
