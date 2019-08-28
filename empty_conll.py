from io import open
from conllu import parse_tree_incr, parse_incr
from keras.utils.np_utils import to_categorical


def clear_tree(tree):
	tree.token['feats'] = None
	tree.token['head'] = None
	tree.token['deprel'] = '_'
	del tree.token['deps']
	del tree.token['misc']
	for child in tree.children:
		clear_tree(child)
	return tree

def main():
	print("opening training data...")
	data = open("../PerDT/Data/train.conll",'r')
	print('parsing data as trees...')
	trees = [tree for tree in parse_tree_incr(data)]
	print("clearing the trees of data")
	for tree in trees:
		clear_tree(tree)
	print("serializing the trees")
	texts = [tree.serialize() for tree in trees]
	file = open("tmp/cleared-train.conll",'w')
	for text in texts:
		file.write(text)
		file.write(u"")
	print("finished")

if __name__ == "__main__":
	main()