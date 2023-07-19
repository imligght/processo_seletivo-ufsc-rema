import PyPDF2
import os
# a function to read the data from a pdf file
def read_pdf(pdf_file):
    try:
        # this line ensure the program will read correctly the path
        # we're given to him
        pdf_file = os.path.expanduser(pdf_file)

        # opening the pdf file in 'rb' (reading binary)
        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            # here, i'm assuming the pdf has a single page
            page = pdf_reader.pages[0]

            # extract the data from the page
            data = page.extract_text()

            print(data)

    except Exception as e:
        print("An error ocurred while reading the PDF:", str(e))
# the path of file you want to read
pdf_file = "~/Documents/it_desafio/anexos/ContaCELESCExemplo1.pdf"

read_pdf(pdf_file=pdf_file)