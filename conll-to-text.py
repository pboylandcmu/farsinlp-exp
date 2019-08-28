from io import open
from conllu import parse_tree_incr, parse_incr
from keras.utils.np_utils import to_categorical

def toText(sent):
	justlemmas = [token['lemma'] for token in sent]
	return ' '.join(justlemmas)

def main():
	print("opening training data...")
	data = open("../PerDT/Data/train.conll",'r')
	print('parsing data as lists...')
	sents = [sent for sent in parse_incr(data)]
	print("extracting raw lemmas...")
	senttexts = [toText(sent) for sent in sents]
	print("writing to file")
	file = open("tmp/raw-lemmas.txt",'w')
	for text in senttexts:
		file.write(text)
		file.write(u"\n\n")
	print("finished")

if __name__ == "__main__":
	main()