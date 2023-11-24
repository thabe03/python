import fitz

# Example usage
input_file = input("Input file: ")
output_file = input_file.replace(".pdf", "_clean.pdf")

doc = fitz.open(input_file)
for page in doc:
    for annot in page.annots():
        if annot.type[0] == 8:
            page.delete_annot(annot)

doc.save(output_file)
doc.close()
print("Tous les surlignages ont été supprimés.")




