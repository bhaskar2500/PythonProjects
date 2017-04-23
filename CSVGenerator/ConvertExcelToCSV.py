import csv
import xlrd
import sys

def Excel2CSV(excelFile,sheetName,CSVFile="LibraryBookList.csv"):
    
     workbook = xlrd.open_workbook(excelFile)
     worksheet = workbook.sheet_by_name(sheetName)
     csvfile = open(CSVFile, 'w',newline='')
     wr = csv.writer(csvfile)
     for rownum in range(worksheet.nrows):
         wr.writerow([x for x in worksheet.row_values(rownum)])
     csvfile.close()

try :
    excelFile=sys.argv[1]
    workbook = xlrd.open_workbook(excelFile)
    for sheet in workbook.sheet_names():
        Excel2CSV(excelFile,sheet,CSVFile=sys.argv[2]+'.csv')
except  Exception as ex :
    excelFile="BookListExcelColumn.xlsx"
    Excel2CSV(excelFile,"Sheet1")