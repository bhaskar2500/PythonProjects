import csv
import xlrd
import sys

def Excel2CSV(excelFile,sheetName,CSVFile="LibraryBookList.csv"):
    
     workbook = xlrd.open_workbook(excelFile)
     worksheet = workbook.sheet_by_name(sheetName)
     csvfile = open(CSVFile, 'w',newline='',encoding="utf-8")
     wr = csv.writer(csvfile)
     for rownum in range(worksheet.nrows):
         wr.writerow([x for x in worksheet.row_values(rownum)])
     csvfile.close()
