import os
import io
import shutil
import PyPDF2

def compress_pdf(input_path, output_path):
    input_pdf = PyPDF2.PdfReader(open(input_path, 'rb'))
    output_pdf = PyPDF2.PdfWriter()
    for page_num in range(0,79):
        page = input_pdf.pages[page_num]
        page.compress_content_streams()
        output_pdf.add_page(page)
    # Write the output PDF to disk
    with open(output_path, 'wb') as output_file:
        output_pdf.write(output_file)

# Example usage
input_file = '0.pdf'
output_file = '0_compressed.pdf'
compress_pdf(input_file, output_file)
