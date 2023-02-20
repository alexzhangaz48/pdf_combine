import PyPDF4

# Open the first PDF file
pdf1 = open('merged_file.pdf', 'rb')

# Open the second PDF file
pdf2 = open('merged_file2.pdf', 'rb')

# Create a PDF reader object for both the files
pdf1_reader = PyPDF4.PdfFileReader(pdf1)
pdf2_reader = PyPDF4.PdfFileReader(pdf2)

# Create a new PDF writer object
pdf_writer = PyPDF4.PdfFileWriter()

# Loop through the first PDF and add all pages to the new writer
for page_num in range(pdf1_reader.getNumPages()):
    page = pdf1_reader.getPage(page_num)
    pdf_writer.addPage(page)

# Loop through the second PDF and add all pages to the new writer
for page_num in range(pdf2_reader.getNumPages()):
    page = pdf2_reader.getPage(page_num)
    pdf_writer.addPage(page)

# Create a new PDF file and write the merged PDF to it
merged_pdf = open('bankingStatement.pdf', 'wb')
pdf_writer.write(merged_pdf)

# Close all files
pdf1.close()
pdf2.close()
merged_pdf.close()
