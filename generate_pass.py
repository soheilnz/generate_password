import random
import string


def paswd(lenght, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special_charr = string.punctuation

    char = letters
    if numbers:
        char += digits
    if special_char:
        char += special_charr

    pwd = ""
    while len(pwd) < lenght:
        pwd += random.choice(char)

    return pwd

print(paswd(10))