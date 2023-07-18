import pandas as pd
import os

# function to convert a .xlsx file to a json file.
def xlsx_to_json_convert(xlsx_file):
    try:
        # read the Excel file into the pandas dataframe
        data_frame = pd.read_excel(xlsx_file)

        # convert the dataframe to a .json
        json_data = data_frame.to_json(orient='records')

        # create the output JSON filename based on the input filename
        input_filename = os.path.splitext(os.path.basename(xlsx_file))[0]
        json_file = f"{input_filename}.json"
        
        # write 'json_data' to a file
        with open(json_file, 'w') as file:
            file.write(json_data)
        # print a sucess mensage, if the conversion is sucessful
        print("Conversion sucessful. JSON file created: ", json_file)
    # if it fails, print a error mensage and give a detailed description
    # of the error
    except Exception as e:
        print("An error occurred in the conversion of the file:", str(e))

xlsx_file = "~/Documents/it_desafio/anexos/Dados Sazonais Para o Brasil.xlsx"
xlsx_to_json_convert(xlsx_file)