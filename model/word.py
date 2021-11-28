from model.word_list import WordList


class Word(str):
    def __new__(cls, word):
        return str.__new__(cls, word.lower())

    def validate_word(self, word_list: WordList) -> None:
        if len(self) != word_list.word_length:
            raise ValueError(
                f"Words must be only {word_list.word_length} characters long - \
                input word '{self}' is {len(self)} characters")
        if self not in word_list:
            raise ValueError(f"The Word '{self}' is not in the dictionary - exiting")
