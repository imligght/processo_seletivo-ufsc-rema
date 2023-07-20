import pandas as pd
import json
import os

# function to convert a .csv file to a json file.
def csv_to_json_convert(csv_file):
    try:
        # read the Excel file into the pandas dataframe
        data_frame = pd.read_csv(csv_file )

        # newIndex = [None] * len(data_frame.columns)
        # for i, index in enumerate(data_frame.columns):
        #     if "Unnamed" in index[1]:
        #         indexTuple = tuple(index[0])

        #     else:
        #         indexTuple[i] = index

        #     newIndex = indexTuple

        # data_frame.columns = pd.MultiIndex.from_tuples(newIndex)
        # print(data_frame.columns)
        # print(data_frame)

        # convert the dataframe to a .json
        json_data = json.loads(data_frame.to_json(orient='columns'))
        json_data = json.dumps(json_data, indent=4)

        # create the output JSON filename based on the input filename
        input_filename = os.path.splitext(os.path.basename(csv_file))[0]
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

csv_file = "anexos/Dados_Sazonais_Para_o_Brasil.csv"
csv_to_json_convert(csv_file)