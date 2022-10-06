import sendMail as sm


def ask(question):
    return input(question)


def getDetails():
    details = {}
    details.update({"To": ask("Enter mail id to spam: ")})
    details.update({"Subject": ask("Enter text for subject: ")})
    details.update({"Body": ask("Enter text for body: ")})
    details.update({"Times": ask("Enter number of times to spam: ")})
    return details


def main():
    details = getDetails()
    sm.sendMail(
        "yash.yasodhan.123@gmail.com",
        details["To"],
        details["Subject"],
        details["Body"],
        int(details["Times"])
    )
    print("Executed Program Successfully")


if __name__ == '__main__':
    main()
