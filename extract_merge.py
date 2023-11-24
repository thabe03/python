from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import os

def extract(file, no, new_name):
    pdf = PdfReader(file)
    pages = range(no-1,no)
    pdfWriter = PdfWriter()

    for page_num in pages:
        pdfWriter.add_page(pdf.pages[page_num])

    with open(str(new_name)+".pdf", 'wb') as f:
        pdfWriter.write(f)
        f.close()

file = input("File name>>")
if not os.path.isfile("0.pdf"):
    list = []
    no = input(">>")
    while no != "88":
        list.append(int(no))
        if no == "88":
            break
        no = input(">>")
    print(list)

    for key, value in enumerate(list):
        extract(file, value, key)

end = len(list)
pdfs = [str(i)+'.pdf' for i in range(0,end)]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()