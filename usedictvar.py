import createdict
from conllu import parse_tree_incr, parse_incr
import sys


def clear_sent(sent, mydict):
    for token in sent:
        token['feats'] = {'cluster': mydict[token['lemma']]
                          if token['lemma'] in mydict else -1}
        '''token['head'] = None
		token['deprel'] = '_'
		del token['deps']
		del token['misc']
		token['XPOSTAG'] = mydict[token['lemma']]'''


def main():
    if (len(sys.argv) != 3):
        print("need two arguments")
        exit(0)
    myfile = open(sys.argv[1], 'r')
    n = sys.argv[2]
    mydict = createdict.todict(myfile)

    print("opening training data...")
    data = open("../PerDT/Data/train.conll", 'r')
    print('parsing data as lists...')
    sents = [sent for sent in parse_incr(data)]
    print("clearing the sentences and inserting cluster markers...")
    for sent in sents:
        clear_sent(sent, mydict)
    print("serializing the sentences")
    texts = [sent.serialize() for sent in sents]
    file = open("tmp/updated-train-" + n + ".conll", 'w')
    for text in texts:
        file.write(text)
        file.write(u"")
    print("finished")


if __name__ == "__main__":
    main()
