import PyPDF2

decr = input("Fichier:")

pdf_file = open(decr, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
pdf_reader.decrypt('')
pdf_writer = PyPDF2.PdfWriter()


for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])

with open('0_decrypt.pdf', 'wb') as new_file:
    pdf_writer.write(new_file)
pdf_file.close()
