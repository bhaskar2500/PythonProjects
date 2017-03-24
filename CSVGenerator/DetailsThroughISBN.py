import isbnlib
import csv
import pandas as pd
from ConvertToExcel import createExcelSheet,librarikaData
import xlsxwriter
from collections import defaultdict
from ConvertExcelToCSV import Excel2CSV

df = pd.read_csv('ISBNNumbers.csv')
saved_column = df.ISBN
listOfBookDicts=[]
dd = defaultdict(list)
listAuthors=[]

def CreateBookByISBN():
    try:
        i=0
        for isbn in saved_column.values.tolist()[:4]:   
            if type(isbn) is str:        
                book = isbnlib.meta(isbn)
                listOfBookDicts.append(book)        
        
        for d in listOfBookDicts: # you can list as many input dicts as you want here
            if d is not None:
                for key, value in d.items():
                    dd[key].append(value)              
             
        for k,v in dd.items():
            for each in v:                
                if(len(each)>1) and type(each)==list:      
                    dd[k].remove(each)         
                    dd[k].insert(i,';'.join(each) )
                    i=i+1 
                elif type(each)==list:
                    dd[k].remove(each)
                    dd[k].insert(i,''.join(each))
                    i=i+1
    
        for  specs in librarikaData :
            if specs not in dd.keys():
                
                dd[specs]=[] 
        createExcelSheet(dd)
        Excel2CSV("BookListExcelColumn.xlsx","Sheet1")
    except Exception as ex:
        print(ex)
        pass

CreateBookByISBN()