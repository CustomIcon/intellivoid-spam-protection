# 🎉 Welcome to the unofficial intellivoid-spam-protection wiki!

This library handles All Requests done to https://api.intellivoid.net/spamprotection/v1/lookup. To understand how this is meant to be used, please see read the following Documentation

## ✨ Getting Started
- Installing the library:
 
    `pip install Intellivoid-SPB`

- For those who wants to try out Development Builds:

    `pip install git+https://github.com/OpenRestfulAPI/intellivoid-spam-protection@dev`

## Methods
Currently there are 2 methods that can be called from `SPBClient()`


- `check_blacklist()`
    - `user_id`: a `username` or `user_id`
    
    `Returns`: [spamprotection.types.Blacklist](https://github.com/OpenRestfulAPI/intellivoid-spam-protection/blob/fa299feab04ab1a9e11480b6af25279ef395f020/spamprotection/types.py#L13)

    _example_:
    ```
    from spamprotection.sync import SPBClient()

    client = SPBClient()
    status = client.check_blacklist("DeprecatedUser")
    print(status)

    # OUTPUT: <Blacklist: {'success': True, 'response_code': 200, 'private_telegram_id': 'TEL-9e44b25d996fefdad8bd458599a5d7aa10e47b6108d873e74ac7701a8ae546b0-24ecd995', 'entity_type': 'user', 'attributes': {'is_blacklisted': False, 'blacklist_flag': None, 'blacklist_reason': None, 'original_private_id': None, 'is_potential_spammer': False, 'is_operator': False, 'is_agent': False, 'is_whitelisted': False, 'intellivoid_accounts_verified': False, 'is_official': False}, 'language_prediction': {'language': 'en', 'probability': 0.38992445568412987}, 'spam_prediction': {'ham_prediction': 0.9904256536, 'spam_prediction': 0.009672318329241}, 'last_updated': datetime.datetime(2021, 1, 2, 11, 23, 8)}>
    ```

- `raw_output()`
    - `user_id`: a `username` or `user_id`

    `Returns`: `[dict()]`

    _example__:
    ```
    from spamprotection.sync import SPBClient()

    client = SPBClient()
    status = client.raw_output("DeprecatedUser")
    print(status)

    # OUTPUT: {'success': True, 'response_code': 200, 'results': {'private_telegram_id': 'TEL-9e44b25d996fefdad8bd458599a5d7aa10e47b6108d873e74ac7701a8ae546b0-24ecd995', 'entity_type': 'user', 'attributes': {'is_blacklisted': False, 'blacklist_flag': None, 'blacklist_reason': None, 'original_private_id': None, 'is_potential_spammer': False, 'is_operator': False, 'is_agent': False, 'is_whitelisted': False, 'intellivoid_accounts_verified': False, 'is_official': False}, 'language_prediction': {'language': 'en', 'probability': 0.38992445568412987}, 'spam_prediction': {'ham_prediction': 0.9904256536, 'spam_prediction': 0.009672318329241}, 'last_updated': 1609568588}}
    ```

## Detailed Examples

All Detailed Examples are listed inside [Examples Directory](https://github.com/OpenRestfulAPI/intellivoid-spam-protection/tree/master/examples)


## Development

For those who wants to contribute or Develop the wrapper follow the instructions below:

### Requirements

- Installation of `python3.6` or `python3.8`
- Installation of `make`: `sudo apt install make`
- clone the github repository and switch to dev branch: `git clone https://github.com/OpenRestfulAPI/intellivoid-spam-protection && cd intellivoid-spam-protection && git checkout dev`
- setup a virtualenv and install requirements: `pip install requirements_dev.txt`
- 🎉 Finally you can test the changes in examples folder :D


## Note
This is an Unofficial wrapper made by an individual on Telegram. The person who owns and created this library has nothing to do with Intellivoid Company.
