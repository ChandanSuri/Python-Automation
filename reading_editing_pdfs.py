import PyPDF2
import os

os.chdir('')

pdfFile = open('file1.pdf', 'rb')

# create PDF reader object
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

page = reader.getPage(0) # page object
page.extractText()

# for getting all the data in whole PDF
for pageNum in range(reader.numPages):
	print(reader.getPage(pageNum).extractText())

# for merging 2 PDFs accordingly, acc to requirements

pdf1File = open('example1.pdf', 'rb')
pdf2File = open('example2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
	page = reader1.getPage(pageNum)
	writer.addPage(page)

for pageNum in range(reader2.numPages):
	page = reader2.getPage(pageNum)
	writer.addPage(page)

outputFile = open('combined.pdf', 'wb')
writer.write(outputFile)

outputFile.close()
pdf1File.close()
pdf2File.close()

# End----