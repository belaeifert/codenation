import re

def valid_email(email):
    return bool(re.fullmatch(r'^[\w\-\.]+@[a-zA-Z\d]+(\.[a-zA-Z]{1,3})+$', email))


def filter_email(emails):
    return [email for email in emails if valid_email(email)]

