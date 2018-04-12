import csv, sys
from pydub import AudioSegment
from pydub.playback import play
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QDialog, QMessageBox)
from PyQt5.QtCore import pyqtSlot, Qt
from sklearn import tree

class App(QDialog):
    def __init__(self):
        super().__init__()
        self.top = 50
        self.left = 50
        self.height = 350
        self.width = 500
        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)

        self.label1 = QLabel("Koji dan? (1 za ponedjeljak - 7 za nedjelju)", self)
        self.label2 = QLabel("Koji sat? (1 - 7)", self)
        self.label3 = QLabel("Je li imao para? (Da/Ne)", self)
        self.label4 = QLabel("Je li imao pljugi? (Da/Ne)", self)

        self.label1.move(75, 50)
        self.label2.move(75, 100)
        self.label3.move(75, 150)
        self.label4.move(75, 200)

        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        self.input3 = QLineEdit(self)
        self.input4 = QLineEdit(self)

        self.input1.move(330, 50)
        self.input2.move(330, 100)
        self.input3.move(330, 150)
        self.input4.move(330, 200)

        self.input1.resize(40, 25)
        self.input2.resize(40, 25)
        self.input3.resize(40, 25)
        self.input4.resize(40, 25)

        self.button = QPushButton('Click', self)
        self.button.move(220, 300)
        self.button.clicked.connect(self.main)

        self.show()

    def main(self):
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

        print("Koji dan? (1 za ponedjeljak - 7 za nedjelju)")
        x1 = self.input1.text()
        if x1 == 6:
            x1 = 5

        print("Koji sat? (1 - 7)")
        x2 = self.input2.text()

        print("Je li imao para? (Da/Ne)")
        x3 = self.input3.text()

        print("Je li imao pljugi? (Da/Ne)")
        x4 = self.input4.text()

        test = (x1, x2, x3, x4)

        predictions = clf.predict([test])
        if test[3] == 0 and predictions[0] == 1:
            jesi = AudioSegment.from_mp3('./Jane_jesi_kratak.mp3')
            play(jesi)
            QMessageBox.about(self, "Kratak", "Jane, jesi kratak?")
        elif predictions[0] == 1:
            QMessageBox.about(self, "Svoje", "Pusio je svoje pljuge.")
        else:
            nije = AudioSegment.from_mp3('./Nije_pusio.mp3')
            play(nije)
            QMessageBox.about(self, "Nema nema", "Nije pusio.")

#import graphviz
#dot_data = tree.export_graphviz(clf, out_file=None)
#graph = graphviz.Source(dot_data)
#graph.render("karlo")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = App()
    sys.exit(app.exec_())

#pip3 install sklearn scipy numpy graphviz pygame pydub PyQt5
#dan, sat, jel ima para, jel ima pljugi, jel zapalio
#https://github.com/machine-learning-projects/machine-learning-recipes
#http://scikit-learn.org/stable/modules/tree.html#tree-classification
#https://en.wikipedia.org/wiki/Decision_tree_learning
#sudo apt-get install graphviz
#sudo apt-get install ffmpeg
#https://www.google.hr/search?ei=5S7FWtuGKszMwALPibPACQ&q=google+machine+learning+recipes&oq=google+machine+learning+rec&gs_l=psy-ab.3.0.35i39k1j0i22i30k1.1895.2516.0.3580.4.4.0.0.0.0.238.560.0j2j1.3.0....0...1c.1.64.psy-ab..1.3.559...0j0i67k1.0.a3lB8JmyQ0M