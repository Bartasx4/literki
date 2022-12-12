

class LiterkiError(Exception):
    """ Base exception. """


class DictionaryNotFountError(LiterkiError):
    """ Not found file with dictionary. """


class MaximumAttemptsReachedError(LiterkiError):
    """ The maximum number of attempts has been reached. """


class WrongLanguageError(LiterkiError):
    """ Wrong Language. """


class WrongKeyError(LiterkiError):
    """ Not found key on keyboard -_- """


class WrongStatusError(LiterkiError):
    """ Wrong status """


class WrongWordError(LiterkiError):
    """  """
