from bnb import *
import sys
from PySide6 import (QtCore, QtWidgets, QtGui)

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.path = []
        self.isSolvable = False
        self.arrSimpulTime = []
        self.initState = ()

        self.button = QtWidgets.QPushButton("Start!")
        self.text = QtWidgets.QLabel("Masukkan kondisi awal pada tabel. Cell kosong direpresentasikan dengan angka 16. Asumsi input benar. Apabila solvable, pencet button start lagi untuk menunjukkan step")
        self.table = QtWidgets.QTableWidget()
        self.status = QtWidgets.QLabel("Status: Not Started")
        self.result = QtWidgets.QTextEdit("")

        self.table.setRowCount(4)
        self.table.setColumnCount(4)
        self.result.setReadOnly(True)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.text)
        layout.addWidget(self.button)
        layout.addWidget(self.status)
        layout.addWidget(self.result)
        layout.addWidget(self.table)

        self.button.clicked.connect(self.magic)

    def getTable(self):
        matrix = []
        matrix.append(int(self.table.item(0,0).text()))
        matrix.append(int(self.table.item(0,1).text()))
        matrix.append(int(self.table.item(0,2).text()))
        matrix.append(int(self.table.item(0,3).text()))
        matrix.append(int(self.table.item(1,0).text()))
        matrix.append(int(self.table.item(1,1).text()))
        matrix.append(int(self.table.item(1,2).text()))
        matrix.append(int(self.table.item(1,3).text()))
        matrix.append(int(self.table.item(2,0).text()))
        matrix.append(int(self.table.item(2,1).text()))
        matrix.append(int(self.table.item(2,2).text()))
        matrix.append(int(self.table.item(2,3).text()))
        matrix.append(int(self.table.item(3,0).text()))
        matrix.append(int(self.table.item(3,1).text()))
        matrix.append(int(self.table.item(3,2).text()))
        matrix.append(int(self.table.item(3,3).text()))
        return matrix
    
    def setTable(self, matrix):
        print(matrix)
        self.table.item(0,0).setText(str(matrix[0]))
        self.table.item(0,1).setText(str(matrix[1]))
        self.table.item(0,2).setText(str(matrix[2]))
        self.table.item(0,3).setText(str(matrix[3]))
        self.table.item(1,0).setText(str(matrix[4]))
        self.table.item(1,1).setText(str(matrix[5]))
        self.table.item(1,2).setText(str(matrix[6]))
        self.table.item(1,3).setText(str(matrix[7]))
        self.table.item(2,0).setText(str(matrix[8]))
        self.table.item(2,1).setText(str(matrix[9]))
        self.table.item(2,2).setText(str(matrix[10]))
        self.table.item(2,3).setText(str(matrix[11]))
        self.table.item(3,0).setText(str(matrix[12]))
        self.table.item(3,1).setText(str(matrix[13]))
        self.table.item(3,2).setText(str(matrix[14]))
        self.table.item(3,3).setText(str(matrix[15]))
    
    def setTextBox(self):
        for i in range(1,17):
            self.result.append("Kurang "+str(i)+ " = " +str(kurang(i, self.initState)))
        
        self.result.append("sumKurang(i)+X = "+ str(kurangPlusX(self.initState)))

    @QtCore.Slot()
    def magic(self):
        if self.isSolvable==False:
            matrix = self.getTable()
            self.status.setText("Status: Processing")
            self.initState = (matrix, 0, 0+costFuncG(matrix), -1)

            self.setTextBox()
            self.isSolvable = solve(self.initState, self.path, self.arrSimpulTime)
            self.status.setText("Status: " + ("Solvable with time "+"{:.5f}".format(self.arrSimpulTime[1]) + " seconds and simpul count " + str(self.arrSimpulTime[0])) if self.isSolvable==True else "Unsolvable" )
            if self.isSolvable==True:
                del self.path[0]
        elif len(self.path)>0:
            self.setTable(self.path[0][0])
            del self.path[0]

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
