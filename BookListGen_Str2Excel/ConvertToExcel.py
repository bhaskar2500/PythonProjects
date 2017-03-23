from BookList import bookListstring
import xlsxwriter

# Extracts Data from string for a particular feature
def createUsingDictkeys(eachDictFeature,eachFeature,dictFeatures):
    if eachDictFeature in eachFeature:
        dictFeatures[eachDictFeature].append(eachFeature.split(":")[1])   

#converts to excel after processing the data
def convertTextToExcel(bookListstring):    
    dictFeatures={"ISBN-10":[],"ISBN-13":[],"ISBN-10":[],"Publisher":[],"Published":[],"Edition":[],"Binding":[],"Author":[],"Title":[]}
    for eachBook in bookListstring.split("\n\n"):
        for eachFeature in eachBook.split("\n"):
            for eachDictFeature in dictFeatures.keys():
                createUsingDictkeys(eachDictFeature,eachFeature,dictFeatures)
    createExcelSheet(dictFeatures)

#Puts the data in the excelSheet
def createExcelSheet(dictFeatures):
    workbook = xlsxwriter.Workbook('BookListExcelColumn.xlsx')
    worksheet = workbook.add_worksheet()
    col = 0
    for key in dictFeatures.keys():
        worksheet.write(0, col, key)
        worksheet.write_column(1,col,dictFeatures[key])
        #worksheet.write_row(row, 1, dictFeatures[key])
        col += 1
    workbook.close()


convertTextToExcel(bookListstring)