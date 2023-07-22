import pandas as pd
import json
import os

# function to convert a .csv file to a json file.
def excel_to_json_convert(excel_file):
    try:
        # read the Excel file into the pandas dataframe
        data_frame = pd.read_csv(excel_file)
        # convert the dataframe to a .json
        json_data = json.loads(data_frame.to_json(orient='columns'))
        json_data = json.dumps(json_data, indent=4)

        # create the output JSON filename based on the input filename
        input_filename = os.path.splitext(os.path.basename(excel_file))[0]
        json_file = f"{input_filename}.json"
        
        # write 'json_data' to a file
        with open(json_file, 'w') as file:
            file.write(json_data)
        # print a sucess message, if the conversion is sucessful
        print("Conversion sucessful. JSON file created:", json_file)
    # if it fails, print a error message and give a detailed description
    # of the error
    except Exception as e:
        print("An error occurred in the conversion of the file:", str(e))

excel_file = input("Insert the path of the excel file: ")
excel_to_json_convert(excel_file)