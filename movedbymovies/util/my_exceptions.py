from string import punctuation, ascii_uppercase, digits


class HasNoPunctuation(BaseException):
    def __str__(self) -> str:
        return f'Password has no punctuation({punctuation})'


class HasNoUppercase(BaseException):
    def __str__(self) -> str:
        return f'Password has no uppercase({ascii_uppercase})'


class HasNotEnoughLength(BaseException):
    def __str__(self) -> str:
        return 'Password has no enough length(8)'


class HasNoNumbers(BaseException):
    def __str__(self) -> str:
        return f'Password has no numbers ({digits})'
