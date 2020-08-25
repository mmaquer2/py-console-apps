import pandas as pd
import openpyxl as openpyxl

from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference

#name of workbook
#name of rows
#import data from where?
# create a filename?

wbName = input('what is the name of this workbook? ')
wbPath = input('what is the desired path of this wb?')
startRow = input('what row would you like to start on? ')
dataIn = input('would you like to enter data? y/n')

createRow = input()
createCol = input()


if dataIn == 'y':
    dataSrc = ""
else:
    pass



df =pd.read(dataSrc)
wbName.to_excel(wbPath,startRow)

