import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import PyQt5


class UIBase(QWidget):
    def __init__(self):
        super(UIBase, self).__init__()
        self.ui_init()

    def ui_init(self):
        self.mainLayout = QHBoxLayout()
        self.paperTable = QTableView()
        self.controlLayout = QVBoxLayout()

        self.InitPaperTable()
        self.InitControlLayout()

        self.mainLayout.addWidget(self.paperTable)
        self.mainLayout.addLayout(self.controlLayout)
        self.setWindowTitle("Input Dialog")

        self.setLayout(self.mainLayout)

    def InitPaperTable(self):
        pass

    def InitControlLayout(self):
        self.buttonLayout = QGridLayout()
        self.InitButtonLayout()

        self.editbox = QTextEdit()

        self.controlLayout.addLayout(self.buttonLayout)
        self.controlLayout.addWidget(self.editbox)

    def InitButtonLayout(self):
        buttons_namelist = ['ok'] + ['x' for i in range(9)]
        self.btns = [QPushButton(buttons_namelist[i], self) for i in range(9)]
        for i in range(9):
            self.buttonLayout.addWidget(self.btns[i], i // 3, i % 3, 1, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    testui = UIBase()
    testui.show()
    sys.exit(app.exec_())
