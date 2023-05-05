import string
from random import Random

def generate_password():
    characters = string.ascii_letters + string.digits
    password = ''
    random = Random()
    for _ in range(8):
        password += characters[random.randint(0, len(characters) - 1)]
    return password

