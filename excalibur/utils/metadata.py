import uuid
import string
import secrets


def generate_uuid():
    return str(uuid.uuid4())


def random_string(length):
    ret = ""
    while length:
        ret += secrets.choice(string.digits + string.ascii_lowercase + string.ascii_uppercase
        )
        length -= 1
    return ret
