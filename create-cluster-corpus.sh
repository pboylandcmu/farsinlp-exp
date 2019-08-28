python conll-to-text.py
#python empty-conlll.py I think this is only needed to
../brown-cluster/wcluster --text tmp/raw-lemmas.txt --c $1
python usedictvar.py raw-lemmas-c$1-p1.out/map $1
../TurboParser-202/TurboParser --train --file_train=tmp/updated-train-$1.conll --file_model=models/unnorm_$1_parser.model --logtostderr
