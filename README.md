Environment setup
-----

This has been tested with Python 3.7.11 and 3.9.7. Due to the use of type hinting, earlier versions will not work.

The environment should only need two packages - and indeed these are only for the tests, the core code uses only built in libraries

How To Run
-----
Code should be run from this root directory (blue-prism-word-test) and can be run as:
```bash
python3 <word_list> <first_word> <end_word> <output_file>
```
e.g.
```bash
python3 reference/words-english.txt hide sort /tmp/out.txt
```
Note that the output file uses unix-style ("\n") line endings. 

Tests can be run as 
```bash
python3 -m pytest
```
Development Notes
-----

While we are told that we can assume that the words will both be found in the test pack, in the interests of defensive code we check anyway. As we are using sets this lookup is quick and cheap. In a similar vein we deal with all our words and word lists as lower case so that we don't have to sit and worry about whether we need to change case - and this conversion to lower case is handled when the words/word lists are created

The search is implemented as breadth first - by using a BFS we can be certain that the first correct result is the shortest (or joint shortest). Due to using unordered sets in the code, if there are multiple results then we cannot guarantee returning the same one each time. An improvement here could be to allow returning ALL correct results (i.e. when we find the depth which contains one correct result, continue iterating until that depth is complete)

The approach also takes advantage of sets and dictionaries having a cost to lookup of O(1). Given we will be reading from these lists (the word list and the graph) far more than writing to it (we will only write once) this will give a good performance benefit vs a list. We use this property to our advantage by taking a word, generating all it's possible word pairs, then looking to see if they exist. So for a 4 letter word we generate 25^4 possibilities and look them up in the word list to see if they exist.This is the worst case assuming all 4 letters change from start word to end word - if they don't such as in spin to spat then we only generate 25^2 possibilities

Test Notes
-----
Testing is with pytest and hypothesis - pytest to hit some of the simple cases, hypothesis to test the weird edge cases. Note that some of the hypothesis tests are somewhat restrictive around what types of test data they generate - this is by running the hypothesis tests we bypass some of the earlier validation (E.g. that words are the same length)

Reference materials
-----
- Python docs 
- Pytest docs (particularly for tmp_path - https://docs.pytest.org/en/6.2.x/tmpdir.html)
- Various helpful people on stackoverflow - e.g. https://stackoverflow.com/questions/7255655/how-to-subclass-str-in-python, https://stackoverflow.com/questions/14117415/in-python-using-argparse-allow-only-positive-integers
- Some examples of other word ladder apps - e.g. https://www.programcreek.com/2012/12/leetcode-word-ladder/
- Hypothesis documentation https://hypothesis.readthedocs.io/en/latest/quickstart.html 