WORD_LENGTH = 4


class WordList(set):
    def load_from_file(self, dictionary_file: str) -> set:
        """Pulls the correct words from a dictionary file into a set

        Adds those of the correct length to a set of words, with whitespace stripped and in lower 
        case"""
        with open(dictionary_file) as f:
            for line in f:
                if len(line.rstrip()) == WORD_LENGTH:
                    self.add(line.rstrip().lower())
        # TODO - improve error handling. Left Strip text as well as right.
        # TODO - Maybe also check for non-alphabetic characters?
