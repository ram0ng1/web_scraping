import os
import requests
from bs4 import BeautifulSoup
import zipfile

# URL do site
url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
resposta = requests.get(url)

# Parse do HTML
soup = BeautifulSoup(resposta.text, 'html.parser')
pdf_links = soup.select('a[href$=".pdf"]')  # Seleciona apenas links que terminam com .pdf

# Pasta para salvar os PDFs
output_folder = 'downloads'
os.makedirs(output_folder, exist_ok=True)

# Baixar apenas os PDFs específicos
pdf_files = []
for link in pdf_links:
    pdf_url = link['href']
    if not pdf_url.startswith('http'):
        pdf_url = os.path.join(url, pdf_url)
    pdf_name = pdf_url.split('/')[-1]
    
    # Verifica se o nome do arquivo começa com Anexo_I_ ou Anexo_II_
    if pdf_name.startswith(('Anexo_I', 'Anexo_II')):
        pdf_path = os.path.join(output_folder, pdf_name)
        print(f'Baixando: {pdf_name}')
        pdf_response = requests.get(pdf_url)

        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
            print(f'PDF salvo: {pdf_name}')
        pdf_files.append(pdf_path)

# Compactar os PDFs em um arquivo ZIP
zip_path = 'Parsed_PDFs.zip'
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for pdf_file in pdf_files:
        zipf.write(pdf_file, os.path.basename(pdf_file))
        print(f'Adicionado ao ZIP: {os.path.basename(pdf_file)}')

print(f'Downloads concluídos na pasta "{output_folder}". Arquivo ZIP criado: "{zip_path}".')