#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from PyPDF2 import PdfFileWriter, PdfFileReader

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, nargs='*', help='asdf')
args = parser.parse_args()

for infile in args.filename:
    inpdf = PdfFileReader(open(infile, 'rb'))

    for page in range(inpdf.numPages):
        out = PdfFileWriter()
        out.addPage(inpdf.getPage(page))
        infilename = infile.split('.')[0]
        with open(f'{infilename}-page{page}.pdf', 'wb') as outpdf:
            out.write(outpdf)
