import string
from random import Random

def generate_password():
    characters = string.ascii_letters + string.digits
    password = ''
    for _ in range(8):
        password += characters[Random.randint()]
    return password

