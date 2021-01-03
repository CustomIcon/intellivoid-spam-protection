from spamprotection.sync import SPBClient

# initializing the client
client = SPBClient()


def main():
    # calling for status
    user = input("Enter a Username or UserID: ")
    status = client.raw_output(user)
    # check if status got a successful response
    if status["success"]:
        print(status)
    else:
        print("Polish Cow did not Approve this!")


if __name__ == "__main__":
    main()
