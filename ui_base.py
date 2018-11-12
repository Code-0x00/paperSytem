import sys
from PyQt5.QtWidgets import *


class UIBase(QWidget):
    def __init__(self, parent=None):
        super(UIBase, self).__init__(parent)
        self.ui_init()
        self.info_init()
        self.buttons_init()

    def ui_init(self):
        self.main_layout = QHBoxLayout()
        self.paperTable = QTableWidget()
        self.control_widget = QWidget()

        self.paper_table_init()
        self.control_widget_init()

        self.main_layout.addWidget(self.paperTable)
        self.main_layout.addWidget(self.control_widget)
        self.setWindowTitle("Input Dialog")

        self.setLayout(self.main_layout)

    def paper_table_init(self):
        pass

    def control_widget_init(self):
        self.control_widget.setMaximumWidth(300)
        self.controlLayout = QVBoxLayout()
        self.control_widget.setLayout(self.controlLayout)

        self.buttonLayout = QGridLayout()
        self.button_layout_init()

        self.editbox = QTextEdit()

        self.controlLayout.addLayout(self.buttonLayout)
        self.controlLayout.addWidget(self.editbox)

    def button_layout_init(self):
        buttons_namelist = ['ok'] + ['x' for i in range(9)]
        self.btns = [QPushButton(buttons_namelist[i], self) for i in range(9)]
        for i in range(9):
            self.buttonLayout.addWidget(self.btns[i], i // 3, i % 3, 1, 1)
            self.btns[i].clicked.connect(self.button_clicked)

    def info_init(self):
        pass

    def buttons_init(self):
        pass

    def button_clicked(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    testui = UIBase()
    testui.show()
    sys.exit(app.exec_())
