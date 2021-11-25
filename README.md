Note - code is currently functional but incomplete - there is additional testing, logging, tidyup etc. to complete. Structure will change and we might even give you a requirements file/package it up

How To Run
-----
Code can be run as python3 <word_list> <first_word> <end_word> <output_file>

e.g. python3 reference/words-english.txt hide sort /tmp/out.txt

Notes
-----

While we are told that we can assume that the words will both be found in the test pack, in the interests of defensive code we check anyway. As we are using sets this lookup is quick and cheap. In a similar vein we deal with all our words and word lists as lower case so that we don't have to sit and worry about whether we need to change case - and this conversion to lower case is handled when the words/word lists are created

The search is implemented as breadth first - by using a BFS we can be certain that the first correct result is the shortest (or joint shortest). Due to using unordered sets in the code, if there are multiple results then we cannot guarantee returning the same one each time. An improvement here could be to allow returning ALL correct results (i.e. when we find the depth which contains one correct result, continue iterating until that depth is complete)

The approach also takes advantage of sets and dictionaries having a cost to lookup of O(1). Given we will be reading from these lists (the word list and the graph) far more than writing to it (we will only write once) this will give a good performance benefit vs a list. We use this property to our advantage by taking a word, generating all it's possible word pairs, then looking to see if they exist. So for a 4 letter word we generate 25^4 possibilities and look them up in the word list to see if they exist.This is the worst case assuming all 4 letters change from start word to end word - if they don't such as in spin to spat then we only generate 25^2 possibilities

Reference materials:
- Python docs 
- Pytest docs (particularly for tmp_path - https://docs.pytest.org/en/6.2.x/tmpdir.html)
- Various helpful people on stackoverflow - e.g. https://stackoverflow.com/questions/7255655/how-to-subclass-str-in-python, 
