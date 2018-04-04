import csv
from sklearn import tree

X = []
y = []
with open('pusenje.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        row = list(map(int, row))
        X.append(row[0:4])
        y.append(row[4])

clf = tree.DecisionTreeClassifier()

clf.fit(X, y)

test = list(map(int, input().split()))

predictions = clf.predict([test])
if test[3] == 0 and predictions[0] == 1:
    print("Jane, jesi kratak")
elif predictions[0] == 1:
    print("Pusio je svoje pljuge")
else:
    print("Nije pusio")

import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("karlo")

#install sklearn, scipy, numpy and graphviz
#dan, sat, jel ima para, jel ima pljugi, jel zapalio