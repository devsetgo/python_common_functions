# -*- coding: utf-8 -*-
""" An example of functions in the common library"""


from com_lib.logging_config import config_logging
from com_lib.pass_lib import encrypt_pass
from com_lib.pass_lib import verify_pass

config_logging()


def hash_pass(pwd: str):

    hashed_pwd = encrypt_pass(pwd)
    return hashed_pwd


def hash_pass_verify(pwd: str, crypt_pwd: str) -> bool:

    check = verify_pass(pwd, crypt_pwd)
    return check


def main():
    pwd = "toast"
    crypt_pwd = hash_pass(pwd)
    print(crypt_pwd)

    result = hash_pass_verify(pwd, crypt_pwd)

    if result == True:
        print("first check of password is valid")
    else:
        print("first check of password is invalid")

    pwd_2 = "toasT"
    result2 = hash_pass_verify(pwd_2, crypt_pwd)

    if result2 == True:
        print("second check of password is valid")
    else:
        print("second check of password is invalid")


if __name__ == "__main__":

    main()
