import random
from pathlib import Path
from .errors import DictionaryNotFountError
from .errors import MaximumAttemptsReachedError
from .errors import WrongWordError
from .status import Status
from .keyboard import Keyboard


class Literki:

    def __init__(self, language: str = 'pl'):
        random.seed()
        self._length: int = 5
        self._word: str = ''
        self._language: str = language
        self._max_tries: int = 9
        self._tries: int = 0
        self._only_one: bool = True
        self._used_alert: bool = True
        self._keyboard = Keyboard(self._language)

    @property
    def keyboard(self):
        return self._keyboard

    @property
    def keyboard_layout(self):
        return self._keyboard.layout

    @property
    def length(self):
        return self._length

    @property
    def max_tries(self):
        return self._max_tries

    def new_word(self):
        self.__reset()
        words_list = self.__load_words()
        new_list = []
        for word in words_list:
            if len(word) == self._length:
                new_list.append(word)
        self._word = random.choice(new_list)
        return self._word

    def guess(self, word_guess: str, force: bool = False):
        assert self.__can_guess(word_guess)
        keys_status = self._keyboard.keys_status(word_guess)
        if not force and self._used_alert and Status.USED in keys_status:
            return Status.FAILED
        result = []
        for index, char in enumerate(word_guess):
            status = None
            if char == self._word[index]:
                status = Status.ON_PLACE
            elif char in self._word:
                status = Status.IN_WORD
            else:
                status = Status.WRONG
            self._keyboard.set(char, status)
            result.append(status)
        self._tries -= 1
        if all([Status.ON_PLACE == char_status] for char_status in result):
            self.__end(win=True)
        elif self._tries == self._max_tries:
            self.__end(win=False)
        return result

    def set(self, default_length: int = 5,
            max_tries: int = 9,
            only_one: bool = True,
            used_alert: bool = True):
        self._length = default_length
        self._max_tries = max_tries
        self._only_one = only_one
        self._used_alert = used_alert

    def __can_guess(self, word_guess: str):
        if self._tries >= self._max_tries:
            raise MaximumAttemptsReachedError
        if len(word_guess) != self._length:
            raise WrongWordError
        return True

    def __end(self, win: bool):
        exit()

    def __load_words(self):
        current = Path().absolute()
        path = Path(f'{current}/literki/dicts/{self._language}.txt')
        words_list = []
        if not path.is_file():
            raise DictionaryNotFountError('Not found dictionary file', path.absolute())
        with open(path.absolute(), 'r') as file:
            for word in file:
                new_word = word.replace('\n', '').strip().lower()
                if end := new_word.find('/') != -1:
                    new_word = new_word[:end]
                words_list.append(new_word)
        return words_list

    def __reset(self):
        self._word: str = ''
        self._tries: int = 0
        self._keyboard.reset()

    def __repr__(self):
        return self._word
