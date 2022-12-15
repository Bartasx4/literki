from .errors import WrongLanguageError
from .errors import WrongKeyError
from .errors import WrongStatusError
from .status import Status


class Keyboard:
    DEFAULT = ['QWERTYUIOP',
               'ASDFGHJKL',
               'ZXCVBNM']
    PL = 'ĄĆĘŁŃÓŚŹŻ'
    SE = 'ÅÖÄ'
    LANGUAGES = {'en': DEFAULT,
                 'pl': [PL] + DEFAULT,
                 'se': [SE] + DEFAULT
                 }

    def __init__(self, language: str = 'en'):
        self._layout = self.__set_language(language)
        self._keyboard = self.__create_keyboard()

    def keys_status(self, keys: str):
        status = []
        for char in keys:
            status.append(self._keyboard[char])
        return status

    @property
    def status(self):
        return self._keyboard

    @property
    def layout(self):
        return self._layout

    def reset(self):
        self.__create_keyboard()

    def set(self, key: str, status: Status):
        self.__set_key(key, status)

    def __create_keyboard(self):
        keyboard = {}
        for row in self._layout:
            for char in row:
                keyboard[char.lower()] = Status.DEFAULT
        return keyboard

    def __set_language(self, language: str):
        language = language.lower()
        if language not in self.LANGUAGES:
            raise WrongLanguageError
        return self.LANGUAGES[language]

    def __set_key(self, char, status: Status):
        if char not in self._keyboard:
            raise WrongKeyError
        if not isinstance(status, Status):
            raise WrongStatusError
        current_status = self._keyboard[char]
        if status == Status.WRONG:
            self._keyboard[char] = Status.USED
        elif current_status == Status.DEFAULT or current_status == Status.IN_WORD:
            self._keyboard[char] = status

    def __repr__(self):
        return str(self._keyboard)

    def __iter__(self):
        return self._keyboard.__iter__()
