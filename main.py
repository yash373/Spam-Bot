import sendMail as sm


def getDetails():
    details = {}
    details.update({"To": input("Enter mail id to spam: ")})
    details.update({"Subject": input("Enter text for subject: ")})
    details.update({"Body": input("Enter text for body: ")})
    details.update({"Times": input("Enter number of times to spam: ")})
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
