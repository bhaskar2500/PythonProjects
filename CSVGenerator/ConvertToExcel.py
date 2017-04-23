import xlsxwriter
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

librarikaData=["Title"
,"Authors" 
,"Co-authors" 
,"Edition"
,"Year"
,"Publisher"
,"Category"
,"ISBN"
,"ISBN13"
,"Call No"
,"Accession No" 
,"Subject"
,"Copy No"
,"Remarks"
,"Binding"
,"Condition"
,"Description"
,"Tags"]