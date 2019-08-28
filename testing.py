from empty_conll import clear_tree
from conllu import parse_tree_incr, parse_incr
import subprocess
import sys


def has3Nouns(tlist):
    past2 = False
    past1 = False
    for token in tlist:
        cur = False
        if token['upostag'] == 'N':
            cur = True
        if past2 and past1 and cur:
            return True
        past2 = past1
        past1 = cur
    return False


def compareTlist(tlist, tlist2, onlyThree=False):
    if onlyThree:
        nouns = [token['upostag'] == 'N' for token in tlist]
        shift1 = nouns[1:]+[False]
        shift2 = nouns[2:]+[False,False]
    equal = 0
    unequal = 0
    if len(tlist) != len(tlist2):
        print("your token lists are of length " +
              str(len(tlist)) + " and " + str(len(tlist2)))
    for (tok1, tok2) in zip(tlist, tlist2):
        if tok1['head'] == tok2['head']:
            equal += 1
        else:
            unequal += 1
    return equal, unequal

def getEvalData(devortest):
    if devortest:
        print("opening test data...")
        data = open("../PerDT/Data/test.conll",'r')
    else:
        print("opening development data...")
        data = open("../PerDT/Data/dev.conll", 'r')
    return data

def beforeTurbo(data):
    print('parsing data as trees...')
    trees = [tree for tree in parse_tree_incr(data)]
    cleared_trees = [clear_tree(tree) for tree in trees]
    texts = [tree.serialize() for tree in cleared_trees]
    file = open("tmp/cleared.conll", 'w')
    for text in texts:
        file.write(text)
        file.write(u"")
    print("ready for TurboTesting")


def afterTurbo(data,allorthree):
    sents = [sent for sent in parse_incr(data)]
    predicted = open("tmp/predicted.conll", 'r')
    predsents = [sent for sent in parse_incr(predicted)]
    sentidx3nouns = [i for i in range(len(sents)) if has3Nouns(sents[i])]
    #avg = sum([len(sents[i]) for i in sentidx3nouns])/len(sentidx3nouns)
    #print(sum([len(sent) for sent in sents])/len(sents))
    #print(avg)
    #sentidx3nouns = [i for i in range(len(sents)) if len(sents[i])>=17]

    if allorthree:
        sents = [sents[i] for i in sentidx3nouns]
        predsents = [predsents[i] for i in sentidx3nouns]
        #print(sum([len(sent) for sent in sents])/len(sents))

    if len(sents) != len(predsents):
        print("number of sentences is different from predicted sentences")
    toteq = 0
    totneq = 0
    for (tlist1, tlist2) in zip(sents, predsents):
        eq, neq = compareTlist(tlist1, tlist2)
        toteq += eq
        totneq += neq
    file = open("tmp/testresults.txt", 'w')
    file.write(str(toteq)+"\n")
    file.write(str(totneq))
    print(toteq/(totneq+toteq))


def main(devortest):
    beforeTurbo(getEvalData(devortest))
    subprocess.run(["../TurboParser-202/TurboParser", "--test", "--evaluate", "--file_model=models/unnorm_700_parser.model", "--file_test=tmp/cleared.conll", "--file_prediction=tmp/predicted.conll"])
    afterTurbo(getEvalData(devortest),False)
    afterTurbo(getEvalData(devortest),True)


if __name__ == "__main__":
    main(False)
    main(True)
