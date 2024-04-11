import random
import string


class Account:

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class AccountUtils:

    @staticmethod
    def generate_random_string(length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def generate_account() -> Account:
        first_name = AccountUtils.generate_random_string()
        last_name = AccountUtils.generate_random_string()
        email = f"{first_name}.{last_name}@example.com"
        password = AccountUtils.generate_random_string(10)
        return Account(first_name, last_name, email, password)
