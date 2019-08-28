import sys

#takes in a single argument

def extractTuple(line):
	firstpart = line.partition("\t")
	secondpart = firstpart[2].partition("-")
	return firstpart[0], secondpart[0]

def todict(mapfile):
	lines = mapfile.readlines()
	mytuples = [extractTuple(line) for line in lines]
	return dict(mytuples)

def main():
	if (len(sys.argv) < 2):
		print ("need an argument")
	myfile = open(sys.argv[1],'r')
	mydict = todict(myfile)
	print(mydict[';'])

if __name__ == "__main__":
	main()