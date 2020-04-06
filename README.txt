1.
gen.py generates random examples of a random conjunction formula and outputs
them to a file (./data/train.txt) the last char in the line is the tag of the example (1-true, 0-flase)

run:
python gen.py dimension_number example_number

example:
python gen.py 5 50

2.
Run the model to learn what the correct conjunction formula is (reads the file from ./data/train.txt)

run:
python bool_conj.py