import sys
from PyQt5.QtWidgets import *
import ui_base
import bibtexJson


class UIAdd(ui_base.UIBase):
    def __init__(self, parent=None):
        super(UIAdd, self).__init__(parent)

    def info_init(self):
        self.paperTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        keys_show = ['title', 'author', 'year']
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
        button_names = ["确定"]
        button_num = len(button_names)
        for i in range(button_num):
            self.btns[i].setText(button_names[i])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    testui = UIAdd()
    testui.show()
    sys.exit(app.exec_())
