import fitz
import os
import re

def extract_duedate_and_consumption(pdf_file_path):
    try:
        # Expandir o caminho do arquivo fornecido pelo usuário
        pdf_file_path = os.path.expanduser(pdf_file_path)
        
        # O padrão da data de vencimento e do consumo total
        duedate_pattern = r'\bVENCIMENTO\s+(\d{2}/\d{2}/\d{4})\b'
        consumption_pattern = r'\b(\d+\s+kWh)\b'
        
        # Abrir o arquivo PDF
        pdf_document = fitz.open(pdf_file_path)
        pdf_text = ''
        
        # Extrair o texto de todas as páginas
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            pdf_text += page.get_text()
        
        # Procurar pelo padrão de data de vencimento
        duedate_match = re.search(duedate_pattern, pdf_text)
        duedate_value = duedate_match.group(1) if duedate_match else None
        
        # Se encontrar o padrão, armazenar o valor em duedate_value
        if duedate_match:
            duedate_value = pdf_text[duedate_match.end():].split()[0]
        
        # Procurar pelo padrão de consumo total faturado
        consumption_match = re.search(consumption_pattern, pdf_text) 
        consumption_value = consumption_match.group(1) if consumption_match else None
        
        # Se encontrar o padrão, armazenar o valor em consumption_value
        if consumption_match:
            consumption_value = pdf_text[consumption_match.end():].split()[0]
        
        # Retornar um dicionário com as informações extraídas
        return {
            'duedate_value': duedate_value,
            'consumption_value': consumption_value
        }

    # Em caso de erro, imprimir a mensagem de erro e retornar None
    except Exception as e:
        print("An error occurred while extracting the data:", str(e))
        return None
    finally:
        # Fechar o documento PDF
        pdf_document.close()

# Chamada da função com o caminho do arquivo PDF
result = extract_duedate_and_consumption("~/Documents/it_desafio/anexos/ContaCELESCExemplo1.pdf")
print(result)