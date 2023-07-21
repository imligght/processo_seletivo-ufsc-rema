import pandas as pd

def find_yearly_factor(xlsx_file):
    #try:
        data_frame = pd.read_excel(xlsx_file)

        for i in data_frame:
                for j in data_frame:
                        if i % 3 == 0

        print(data_frame)

find_yearly_factor('/home/light/Documents/it_desafio/anexos/Dados_Sazonais_Para_o_Brasil.xlsx')