import string as s
from my_exceptions import (
    HasNoPunctuation, HasNotEnoughLength, HasNoUppercase, HasNoNumbers
)


class ValidatePassword():
    def __init__(self, password: str) -> None:
        __class__.has_punctuation(password)
        __class__.has_uppercase(password)
        __class__.has_numbers(password)
        __class__.has_enought_length(password)

    @classmethod
    def has_punctuation(cls, password: str) -> bool:
        for i in password:
            if i in s.punctuation:
                return True
        raise HasNoPunctuation

    @classmethod
    def has_uppercase(cls, password: str) -> bool:
        for i in password:
            if i in s.ascii_uppercase:
                return True
        raise HasNoUppercase

    @classmethod
    def has_numbers(cls, password: str) -> bool:
        for i in password:
            if i in s.digits:
                return True
        raise HasNoNumbers

    @classmethod
    def has_enought_length(cls, password: str) -> bool:
        if len(password) >= 8:
            return True
        raise HasNotEnoughLength
