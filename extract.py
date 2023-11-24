from PyPDF2 import PdfReader, PdfWriter

pdf_file_path = input("Nom:")
file_base_name = pdf_file_path.replace('.pdf', '')

pdf = PdfReader(pdf_file_path)
start = input("Go : ")
while start != "Stop":
    start = input("Go")
    debut = int(input("Debut:"))
    fin = int(input("Fin:"))
    pages = range(debut-1,fin)
    pdfWriter = PdfWriter()

    for page_num in pages:
        pdfWriter.add_page(pdf.pages[page_num])

    with open(start+".pdf", 'wb') as f:
        pdfWriter.write(f)
        f.close()