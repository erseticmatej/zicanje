import csv
import pygame.mixer as pgm
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
    pgm.init()
    pgm.music.load('Jane jesi kratak.mp3')
    pgm.music.play()
    print("Jane, jesi kratak")
elif predictions[0] == 1:
    print("Pusio je svoje pljuge")
else:
    pgm.init()
    pgm.music.load('Nije pusio.mp3')
    pgm.music.play()
    print("Nije pusio")

import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("karlo")

#install sklearn, scipy, numpy , graphviz, pygame
#dan, sat, jel ima para, jel ima pljugi, jel zapalio
#https://github.com/machine-learning-projects/machine-learning-recipes
#http://scikit-learn.org/stable/modules/tree.html#tree-classification
#https://en.wikipedia.org/wiki/Decision_tree_learning
#https://www.google.hr/search?ei=5S7FWtuGKszMwALPibPACQ&q=google+machine+learning+recipes&oq=google+machine+learning+rec&gs_l=psy-ab.3.0.35i39k1j0i22i30k1.1895.2516.0.3580.4.4.0.0.0.0.238.560.0j2j1.3.0....0...1c.1.64.psy-ab..1.3.559...0j0i67k1.0.a3lB8JmyQ0M