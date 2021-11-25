WORD_LENGTH = 4


class Word(str):
    def __new__(cls, word):
        return str.__new__(cls, word.lower())

    def validate_word(self, word_list) -> None:
        if len(self) != WORD_LENGTH:
            raise ValueError(
                f"Words must be only {WORD_LENGTH} characters long - input word '{self}' is \
                {len(self)} characters")
        if self not in word_list:
            raise ValueError(f"The Word '{self}' is not in the dictionary - exiting")
