from datetime import datetime


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
        # attributes
        self.is_blacklisted = results["attributes"]["is_blacklisted"]
        self.blacklist_flag = results["attributes"]["blacklist_flag"]
        self.blacklist_reason = results["attributes"]["blacklist_reason"]
        self.original_private_id = results["attributes"]["original_private_id"]
        self.is_potential_spammer = results["attributes"]["is_potential_spammer"]
        self.is_operator = results["attributes"]["is_operator"]
        self.is_agent = results["attributes"]["is_agent"]
        self.is_whitelisted = results["attributes"]["is_whitelisted"]
        self.intellivoid_accounts_verified = results["attributes"][
            "intellivoid_accounts_verified"
        ]
        self.is_official = results["attributes"]["is_official"]
        # language_prediction
        self.language = results["language_prediction"]["language"]
        self.probability = results["language_prediction"]["probability"]
        # spam_prediction
        self.ham_prediction = results["spam_prediction"]["ham_prediction"]
        self.spam_prediction = results["spam_prediction"]["spam_prediction"]
        # last_updated
        self.last_updated = datetime.fromtimestamp(results["last_updated"])
