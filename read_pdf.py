import PyPDF2
import re
import os

from emission_source import EmissionSource
from records import Records

# a function to read the data from a pdf file
def read_pdf(pdf_file):
    # the path of file you want to read
    pdf_file = input("Insira o caminho do arquivo: ")
    try:
        # this line ensure the program will read correctly the path
        # we're given to him
        pdf_file = os.path.expanduser(pdf_file)

        # opening the pdf file in 'rb' (reading binary)
        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ''
            # concatenates all the pages in a single string
            for page in pdf_reader.pages:
                text += page.extract_text()

            # extract the data from the page
            data = page.extract_text()

            print(data)

    except Exception as e:
        print("An error ocurred while reading the PDF:", str(e))


def extract_duedate_and_consumotion(pdf_file_path):
    try:
        pdf_file_path = os.path.expanduser(pdf_file_path)
        # the pattern of the due date and total consumption
        duedate_pattern = r'VENCIMENTO (\d{2}/\d{2}/\d{4})'
        consumption_pattern = r'CONSUMO TOTAL FATURADO (\d{1,}) kWh'
        # open the pdf file in read binary mode
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_text = ''

            # here, I'm assuming the pdf has a single page since it's an energy bill
            page = pdf_reader.pages[0]
            # extract the text from the entire page
            pdf_text += page.extract_text().replace('\n', ' ')
            # search for the due date pattern
            duedate_match = re.search(duedate_pattern, pdf_text)
            duedate_value = duedate_match.group(1) if duedate_match else None
            # if find the pattern, stores the value in duedate_value
            if duedate_match:
                duedate_value = pdf_text[:duedate_match.end()].split()[-1]
            # search for the total consumption pattern
            consumption_match = re.search(consumption_pattern, pdf_text) 
            consumption_value = consumption_match.group(1) if consumption_match else None
            # if find the pattern, stores the value in consumption_match
            if consumption_match:
                consumption_value = pdf_text[:consumption_match.end()].split()[-2]

            if duedate_value and consumption_value:
                try:
                    default_state = 'SC'
                    source_name = input("Insert the name of the source: ")
                    new_emission_source = EmissionSource(consumption_value, duedate_value[-4:], duedate_value[3:5], default_state, source_name)

                    records = Records()
                    records.add_emission_source(new_emission_source)

                    print(str(new_emission_source))

                    print(f"Registration sucessful, the emission id is {new_emission_source.id}")
                
                except Exception as e:
                    print("Error", str(e))

                

            return duedate_value, consumption_value


    # if something goes wrong
    except Exception as e:
        print("An error ocurred while extracting the data: ", str(e))

    return 0