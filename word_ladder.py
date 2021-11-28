import logging
import string
from collections import defaultdict, deque

from model.word_list import WordList


class WordLadder(object):
    def __init__(self, start: str, target: str, word_list: WordList) -> None:
        self.graph = defaultdict(set)
        self.start = start
        self.target = target
        self.word_list = word_list

    def get_next_words(self, word: string):
        next_words = set()
        for i in range(self.word_list.word_length):
            if word[i] == self.target[i]:
                # Short circuit the loop when the letters already match target
                # (i.e. if we have spin and spot, no point checking the path spin->shin)
                continue
            for letter in string.ascii_lowercase.replace(word[i], ""):
                # Iterate over the alphabet except original letter
                new_string = (word[:i] + letter + word[i + 1:])  # Construct our new string
                if new_string in self.word_list:
                    next_words.add(new_string)
        return next_words

    def calculate_route(self) -> list[str]:
        # to start we only need to generate routes from 1st word
        self.graph[self.start] = self.get_next_words(self.start)
        q = deque([(self.start, [self.start])])
        # Visited will prevent us following a route twice - the second visit to a word is
        # guaranteed to be as long or longer than the shortest route
        visited = (set())
        while q:
            word, journey = q.popleft()
            logging.debug("Calculating route from %s", word)
            if word not in visited:
                visited.add(word)
                self.graph[word] = self.get_next_words(word)
                logging.debug("Got next words for %s", word)
                for nxt in self.graph[word]:
                    if nxt not in visited:
                        q.append((nxt, journey + [nxt]))
                        if nxt == self.target:
                            logging.info(
                                "At target - exiting loop. Number of steps = %s. Number of Visits %r",
                                len(journey) + 1, len(visited))
                            return(journey + [nxt])
        return []  # no results found
