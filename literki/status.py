from enum import Enum


class Status(Enum):
    (DEFAULT, WRONG, ON_PLACE,
     IN_WORD, USED, FAILED) = range(6)
