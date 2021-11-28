import argparse
import logging
from model.word import Word
from model.word_list import WordList
from word_ladder import WordLadder


logging.basicConfig(
    filename="word_ladder.log", format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.DEBUG)
logging.debug("Starting Word Ladder App")


def parse_args() -> tuple:
    parser = argparse.ArgumentParser(description="Blue Prism Word Ladder")
    parser.add_argument(
        "DictionaryFile",
        type=str,
        help="File containing dictionary words to move between",
    )
    parser.add_argument(
        "StartWord", type=str, help="Word to start search from"
    )
    parser.add_argument("EndWord", type=str, help="Target word to search for")
    parser.add_argument(
        "ResultFile", type=str, help="File name to save the results to"
    )
    parser.add_argument(
        "--word-length", type=int, help="Word Length to use - defaults to 4", default=4
    )
    args = parser.parse_args()
    return args.DictionaryFile, args.StartWord, args.EndWord, args.ResultFile, args.word_length


def main(word_list: WordList, start: str, end: str) -> list:
    start_word = Word(start)
    start_word.validate_word(word_list)
    end_word = Word(end)
    end_word.validate_word(word_list)
    word_ladder = WordLadder(start_word, end_word, word_list)
    result = word_ladder.calculate_route()
    return result


if __name__ == "__main__":
    dictionary_file, start_word, end_word, result_file, word_length = parse_args()
    wlist = WordList(word_length=word_length)
    wlist.load_from_file(dictionary_file)

    result_list = main(wlist, start_word, end_word)
    with open(result_file, "w", encoding='utf-8') as rf:
        rf.write(str(result_list))
    print(result_list)
