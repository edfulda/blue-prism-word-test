import logging


class WordList(set):

    def __init__(self, word_length: int, iterable=None) -> None:
        self.word_length = word_length
        if not iterable:
            iterable = set()
        else:
            for i in iterable:
                self.__check_and_add(i)

    def load_from_file(self, dictionary_file: str) -> set:
        """Pulls the correct words from a dictionary file into a set

        Adds those of the correct length to a set of words, with whitespace stripped and in lower
        case"""
        logging.debug("Loading Word Lists from file %s", dictionary_file)
        with open(dictionary_file, encoding='utf-8') as f:
            for line in f:
                self.__check_and_add(line)
        logging.debug("Word list loaded. Length %s", len(self))
        # TODO - improve error handling. Left Strip text as well as right.
        # TODO - Maybe also check for non-alphabetic characters?

    def __check_and_add(self, line: str) -> None:
        mod_line = line.rstrip().lstrip().lower()
        if len(mod_line) == self.word_length:
            self.add(mod_line)
