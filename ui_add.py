import sys
import os
import json
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
import ui_base
import bibtexJson


class UIAdd(ui_base.UIBase):
    def __init__(self, parent=None):
        super(UIAdd, self).__init__(parent)
        self.windowTitle = 'References'
        if os.path.exists('xhq.json'):
            print('load json')
            with open('xhq.json', 'r', encoding='UTF-8') as f:
                self.papers = json.load(f)
        else:
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

        keys_show = ['title', 'author', 'year', 'type']
        if os.path.exists('xhq.json'):
            with open('xhq.json', 'r', encoding='UTF-8') as f:
                bib = json.load(f)
        else:
            bib = bibtexJson.loadBibtexAsJson('xhq.bib')

        item_num = len(bib)
        keys_num = len(keys_show)
        self.paperTable.setRowCount(item_num)
        self.paperTable.setColumnCount(keys_num)
        self.paperTable.setHorizontalHeaderLabels(keys_show)

        for i in range(item_num):
            for j in range(keys_num):
                self.paperTable.setItem(i, j, QTableWidgetItem(bib[i][keys_show[j]]))

    def buttons_init(self):
        button_names = ["确定修改笔记", "Save Json"]
        button_num = min(len(self.btns), len(button_names))
        for i in range(button_num):
            self.btns[i].setText(button_names[i])

    def button_clicked(self):
        sender = self.sender()
        if sender.text() == self.btns[0].text():
            self.refresh_editbox()
        elif sender.text() == self.btns[1].text():
            self.save_json2file()
        else:
            pass

    def save_json2file(self):
        with open('xhq.json', 'w', encoding='UTF-8') as f:
            json.dump(self.papers, f, ensure_ascii=False)
        self.setWindowTitle(self.windowTitle)

    def refresh_editbox(self):
        row = self.paperTable.currentIndex().row()
        self.papers[row]['note'] = self.editbox.toPlainText()
        self.setWindowTitle(self.windowTitle + '*')

    def table_clicked(self):
        row = self.paperTable.currentIndex().row()
        info = self.papers[row]
        if 'note' in info.keys():
            note = info['note']
            self.editbox.setText(note)
        else:
            self.editbox.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    testui = UIAdd()
    testui.show()
    sys.exit(app.exec_())
