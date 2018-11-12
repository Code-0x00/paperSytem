import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
import ui_base
import bibtexJson


class UIAdd(ui_base.UIBase):
    def __init__(self, parent=None):
        super(UIAdd, self).__init__(parent)
        # self.papers = []

        self.papers = bibtexJson.loadBibtexAsJson('xhq.bib')
        self.paperTable.clicked.connect(self.table_clicked)

    def keyPressEvent(self, QKeyEvent):
        print('ssss')
        if QKeyEvent.key() == Qt.Key_Escape:
            print('esc')
            return

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print('left')

    def info_init(self):
        self.paperTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.paperTable.setSelectionMode(QAbstractItemView.SingleSelection)

        keys_show = ['title', 'author', 'year']
        bib = bibtexJson.loadBibtexAsJson('xhq.bib')

        # print(self.papers)

        item_num = len(bib)
        keys_num = len(keys_show)
        self.paperTable.setRowCount(item_num)
        self.paperTable.setColumnCount(keys_num)
        self.paperTable.setHorizontalHeaderLabels(keys_show)

        for i in range(item_num):
            for j in range(keys_num):
                self.paperTable.setItem(i, j, QTableWidgetItem(bib[i][keys_show[j]]))

    def buttons_init(self):
        button_names = ["确定修改笔记", ""]
        button_num = min(len(self.btns), len(button_names))
        for i in range(button_num):
            self.btns[i].setText(button_names[i])

    def button_clicked(self):
        sender = self.sender()
        if sender.text() == self.btns[0].text():
            row=self.paperTable.currentIndex().row()
            self.papers[row]['note']=self.editbox.toPlainText()

    def table_clicked(self):
        row = self.paperTable.currentIndex().row()
        info = self.papers[row]
        note = ''
        if 'note' not in info.keys():
            pass
        else:
            note = info['note']
        self.editbox.setText(note)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    testui = UIAdd()
    testui.show()
    sys.exit(app.exec_())
