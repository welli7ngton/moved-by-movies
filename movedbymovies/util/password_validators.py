import string as s

from .my_exceptions import (
    HasNoPunctuation, HasNotEnoughLength, HasNoUppercase, HasNoNumbers
)


class ValidatePassword:
    def __init__(self, password: str) -> None:
        self.validate(password)

    @classmethod
    def validate(cls, password: str) -> None:
        cls.has_punctuation(password)
        cls.has_uppercase(password)
        cls.has_numbers(password)
        cls.has_enough_length(password)

    @staticmethod
    def has_punctuation(password: str) -> None:
        if not any(char in s.punctuation for char in password):
            raise HasNoPunctuation

    @staticmethod
    def has_uppercase(password: str) -> None:
        if not any(char.isupper() for char in password):
            raise HasNoUppercase

    @staticmethod
    def has_numbers(password: str) -> None:
        if not any(char.isdigit() for char in password):
            raise HasNoNumbers

    @staticmethod
    def has_enough_length(password: str) -> None:
        if len(password) < 8:
            raise HasNotEnoughLength
