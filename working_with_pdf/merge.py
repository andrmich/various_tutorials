'''From: https://realpython.com/pdf-python/'''
from PyPDF2 import PdfFileReader, PdfFileWriter


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    paths = ['reportlab-sample.pdf', 'rotated_pages.pdf']
    merge_pdfs(paths, output='merged.pdf')
