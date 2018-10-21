#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import server
import parameters
import config
import os
import re
import sys

import rc


def id_info_get(text):
    ret_text = ''
    for i in text.split('\n'):
        if '@' in i:
            ret_text += i.lower() + '\n'
        else:
            ret_text += i + '\n'
    ret = []
    print(ret_text)
    for item in ret_text.split('@'):
        try:
            tmp = {}
            tmp['id'] = item.split(',')[0].split('{')[1]
            tmp['title'] = re.findall("title=\{(.+?)\}", item)[0]
            tmp['info'] = '@' + item.replace("'", "_")
            while '}\n' in tmp['info']:
                # print(tmp['info'])
                tmp['info'] = tmp['info'].replace('}\n', '}')
        except:
            tmp['id'] = "404"
            tmp['title'] = "404"
            tmp['info'] = '404'
        ret.append(tmp)
    print(ret)
    return ret


class PaperDB(QWidget):
    def __init__(self, parent=None):
        super(PaperDB, self).__init__(parent)

        self.db = server.PAPERDB()

        self.setWindowIcon(QIcon(':/icons/_128.ico'))
        r"""
        下拉菜单start
        """
        self.ComboBoxClass0 = QComboBox()
        self.ComboBoxClass0.addItem("全部")
        self.ComboBoxClass0.addItem("网络结构")
        self.ComboBoxClass0.addItem("半监督学习")

        self.analysisButton = QPushButton("查看")
        self.analysisButton.clicked.connect(self.InformationGet)
        r"""
        下拉菜单end
        """
        r"""
        目录设置start
        """
        current_config = config.config_get()
        self.pathLine = QLineEdit()
        self.pathLine.setText(parameters.client.path)
        self.pathLine.setReadOnly(True)

        self.browseButton = QPushButton("浏览")
        self.browseButton.clicked.connect(self.getPath)
        r"""
        目录设置end
        """
        r"""
        列表start
        """
        self.chapterGroupBox = QGroupBox("论文列表")
        self.chapterListView = QListWidget(self.chapterGroupBox)
        self.chapterListView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.chapterListView.setEnabled(False)

        self.table_test = QTableWidget(self.chapterGroupBox)
        self.table_test.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_test.setEnabled(True)

        groupBoxLayout = QHBoxLayout(self.chapterGroupBox)
        groupBoxLayout.addWidget(self.chapterListView)
        groupBoxLayout.addWidget(self.table_test)

        self.table_test.setColumnCount(4)
        self.table_test.setRowCount(3)
        self.table_test.setHorizontalHeaderLabels(["标题", '作者', 'c', 'd'])
        self.table_test.setSelectionBehavior(1)
        r"""
        列表end
        """
        r"""
        描述及其他选项start
        """
        self.statusLabel = QLabel("描述")
        self.downloadButton = QPushButton("详细")
        self.downloadButton.clicked.connect(self.download)

        self.Button0 = QPushButton("导出到bib")
        self.Button1 = QPushButton("插入记录")
        self.Button1.clicked.connect(self.insert0)
        self.Button2 = QPushButton("从bib导入")
        self.Button3 = QPushButton("打开")
        self.Button3.clicked.connect(self.openpdf)
        self.Button4 = QPushButton("插入文献")

        self.Button5 = QPushButton("保存并插入")
        self.Button5.clicked.connect(self.insert1)

        self.InfoEdit = QTextEdit()
        self.InfoEdit.setPlainText("Null")
        self.InfoEdit.setReadOnly(True)

        r"""
        描述及其他选项end
        """
        self.GridInit()

        self.IdList()

    def openpdf(self):
        selectedChapterList = self.chapterListView.selectedIndexes()
        if len(selectedChapterList) > 0:
            item = selectedChapterList[0].row()
            filename = parameters.client.path + "/" + self.contentNameList[item]['ID'] + ".pdf"
            if os.path.exists(filename):
                os.system(parameters.client.chrome + " " + filename)

    def item_insert(self, id, info):
        print(id)
        self.db.insert(id, info)

    def insert0(self):
        self.InfoEdit.setReadOnly(False)
        # self.InfoEdit.setPlainText("Edit...")
        self.Button1.setEnabled(False)
        self.Button5.setEnabled(True)

    def insert1(self):
        self.InfoEdit.setReadOnly(True)
        items = id_info_get(self.InfoEdit.toPlainText())
        for item in items:
            self.item_insert(item['id'], item['info'])
        self.Button1.setEnabled(True)
        self.Button5.setEnabled(False)

    def GridInit(self):
        r"""
        Grid start
        """
        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(QLabel("分类"), 0, 0)
        self.mainLayout.addWidget(self.ComboBoxClass0, 0, 1)
        self.mainLayout.addWidget(self.analysisButton, 0, 2)
        self.mainLayout.addWidget(QLabel("根目录:"), 1, 0)
        self.mainLayout.addWidget(self.pathLine, 1, 1)
        self.mainLayout.addWidget(self.browseButton, 1, 2)

        self.mainLayout.addWidget(self.statusLabel, 2, 0, 1, 2)
        self.mainLayout.addWidget(self.chapterGroupBox, 3, 0, 9, 2)

        self.mainLayout.addWidget(self.downloadButton, 2, 2)
        self.mainLayout.addWidget(self.Button0, 3, 2)
        self.mainLayout.addWidget(self.Button1, 4, 2)
        self.mainLayout.addWidget(self.Button2, 5, 2)
        self.mainLayout.addWidget(self.Button3, 6, 2)
        self.mainLayout.addWidget(self.Button4, 7, 2)

        self.mainLayout.addWidget(self.InfoEdit, 8, 2)

        self.mainLayout.addWidget(self.Button5, 9, 2)

        self.setLayout(self.mainLayout)
        self.setWindowTitle(parameters.client.title)
        self.setGeometry(400, 300, 800, 500)
        r"""
        Grid end 
        """

    def search_papers(self):
        self.chapterListView.clear()
        # print(self.ComboBoxClass0.currentIndex())
        # print(self.ComboBoxClass0.currentText())
        self.anaysisKeywords()

        self.chapterListView.setEnabled(True)
        self.downloadButton.setEnabled(True)
        self.chapterListView.setFocus()
        self.statusLabel.setText('选择后描述')
        self.downloadButton.setEnabled(True)

    def IdList(self):
        self.chapterListView.clear()
        # print(self.ComboBoxClass0.currentIndex())
        # print(self.ComboBoxClass0.currentText())
        self.anaysisKeywords()

        self.chapterListView.setEnabled(True)
        self.downloadButton.setEnabled(True)
        self.chapterListView.setFocus()
        self.statusLabel.setText('选择后描述')
        self.downloadButton.setEnabled(True)

    def getPath(self):
        path = str(QFileDialog.getExistingDirectory(self, "选择论文存储目录"))
        if path:
            self.pathLine.setText(path)

    def ButtonAdd(self, title, y, x, connect):
        tmpButton = QPushButton(title)
        tmpButton.clicked.connect(connect)
        self.mainLayout.addWidget(tmpButton, y, x)

    def setStatus(self, status):
        self.statusLabel.setText(status)

    def enableWidget(self, enable):
        widgets_list = [
            self.downloadButton,
            self.nameLine,
            self.pathLine,
            self.chapterListView,
            self.analysisButton,
            self.browseButton,
            self.one_folder_checkbox
        ]
        for widget in widgets_list:
            widget.setEnabled(enable)

        if enable:
            self.downloadButton.setText('下载选中')
            self.chapterListView.setFocus()

    def anaysisKeywords(self):

        self.contentNameList = self.db.select()
        for i in range(len(self.contentNameList)):
            self.chapterListView.addItem('№{0:0>3} | {1}'.format(i + 1, self.contentNameList[i]['ID']))
            self.table_test.insertRow(self.table_test.rowCount())
            newItem = QTableWidgetItem(self.contentNameList[i]['ID'])
            self.table_test.setItem(i,0,newItem)

            if os.path.exists(parameters.client.path + "/" + self.contentNameList[i]['ID'] + ".pdf"):
                self.chapterListView.item(i).setSelected(True)
            else:
                self.chapterListView.item(i).setSelected(False)
                self.chapterListView.item(i).setForeground(QColor(248, 168, 0))

    def download(self):
        selectedChapterList = [item.row() for item in self.chapterListView.selectedIndexes()]
        ret = ''
        for i in selectedChapterList:
            ret += self.contentNameList[i]['INFO']
        self.InfoEdit.setPlainText(ret)
        return 0

        self.downloadButton.setText("下载中...")
        one_folder = self.one_folder_checkbox.isChecked()

        self.enableWidget(False)

        selectedChapterList = [item.row() for item in self.chapterListView.selectedIndexes()]

        path = self.pathLine.text()
        comicName = self.comicName
        forbiddenRE = re.compile(r'[\\/":*?<>|]')  # windows下文件名非法字符\ / : * ? " < > |
        comicName = re.sub(forbiddenRE, '_', comicName)  # 将windows下的非法字符一律替换为_
        comicPath = os.path.join(path, comicName)

        if not os.path.isdir(comicPath):
            os.makedirs(comicPath)

        self.downloadThread = Downloader(selectedChapterList, comicPath, self.contentList, self.contentNameList,
                                         self.id, one_folder)
        self.downloadThread.output.connect(self.setStatus)
        self.downloadThread.finished.connect(lambda: self.enableWidget(True))
        self.downloadThread.start()

    def InformationGet(self):
        selectedChapterList = [item.row() for item in self.chapterListView.selectedIndexes()]
        ret = ''
        for i in selectedChapterList:
            ret += self.contentNameList[i]['INFO']
        self.InfoEdit.setPlainText(ret)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PaperDB()
    main.show()
    app.exec_()
