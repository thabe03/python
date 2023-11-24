from PyPDF2 import PdfMerger
debut = int(input("Debut:"))
fin = int(input("Fin:"))
pdfs = [str(i)+'.pdf' for i in range(debut,fin+1)]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()

