import isbnlib
import csv
import pandas as pd
from ConvertToExcel import createExcelSheet,librarikaData
import xlsxwriter
from collections import defaultdict,OrderedDict
from ConvertExcelToCSV import Excel2CSV
import sys
import traceback

isbnFileName = str(sys.argv[1] if '.csv' in str(sys.argv[1]) else sys.argv[1]+'.csv' )
listOfBookDicts=[]
dd = defaultdict(list)
listAuthors=[]
notFoundIsbn=[]
column={}
finalFeatureDict=OrderedDict()
notString=[]


def isbnVerfication(key):    
    global listOfBookDicts
    global notFoundIsbn
    for isbn in column[key]:
        if isbnlib.is_isbn10(isbn) or isbnlib.is_isbn13(isbn):   
            if type(isbn) is str:        
                book = isbnlib.meta(isbn)
                if book is None:
                    notFoundIsbn.append(isbn)
                listOfBookDicts.append(book)        
            else:
                notFoundIsbn.append(isbn)
        else:
            notFoundIsbn.append(isbn)
    #return notFoundIsbn,listOfBookDicts
def CreateBookByISBN():

    i=0
    with open(isbnFileName,"r") as f:
        global column
        reader=csv.reader(f)
        headers=reader.__next__()
        
        for h in headers:
            column[h]=[]
        for row in reader:
            for h,v in zip(headers,row):                    
                column[h].append(v)
                
    isbnVerfication("ISBN13")
    isbnVerfication("ISBN")

    print(len(column["ISBN13"]) ,'-------------------------------====--->',len(list(filter(None,listOfBookDicts))),'++++++++',len(list(filter(None,notFoundIsbn))))

    with open('LogRemainingISBN.txt','wt') as f:
        f.write("\n".join(list(filter(None,notFoundIsbn))))    
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

    createOrderDict(dd,librarikaData)                
    createExcelSheet(finalFeatureDict)
    Excel2CSV("BookListExcelColumn.xlsx","Sheet1", sys.argv[2] if '.csv' in str(sys.argv[2]) else sys.argv[2]+'.csv')


def createOrderDict(dd,librarikaData):
     for  specs in librarikaData :            
            if specs not in dd.keys():                
                finalFeatureDict[specs]=[]
            else:
                finalFeatureDict[specs]=dd[specs]

     for key in list(dd.keys()):
         if key=='ISBN-13':
            finalFeatureDict['ISBN13']=dd[key]   
         if  key not in librarikaData :
            finalFeatureDict.pop(key, None)

CreateBookByISBN()
print('-----******----- Successfully Completed -----******-----')

