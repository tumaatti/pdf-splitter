#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog

from PyPDF2 import PdfFileWriter, PdfFileReader


class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Choose file..'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.openFileNameDialog()
        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        global file_name
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            'QFileDialog.getOpenFileName()',
            '',
            'All files (*);;PDF Files (*.pdf)',
            options=options
        )


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PDF Splitter 2000')
        self.choose_button = QPushButton('Choose file..')
        self.choose_button.clicked.connect(self.find_file)
        self.split_button = QPushButton('Split PDF')
        self.split_button.clicked.connect(self.split_pdf)

        wid = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.choose_button)
        layout.addWidget(self.split_button)
        wid.setLayout(layout)
        self.setCentralWidget(wid)

    def find_file(self, checked):
        FileExplorer()

    def split_pdf(self):
        global file_name
        inpdf = PdfFileReader(open(file_name, 'rb'))

        for page in range(inpdf.numPages):
            out = PdfFileWriter()
            out.addPage(inpdf.getPage(page))
            infilename = file_name.split('.')[0]
            with open(f'{infilename}-page{page + 1}.pdf', 'wb') as outpdf:
                out.write(outpdf)


app = QApplication(sys.argv)
app.setStyleSheet('QPushButton { padding: 10px; width: 300px }')
w = MainWindow()
w.show()
app.exec_()
