# Web Scraping

Este repositório contém um script de Web Scraping desenvolvido em Python para baixar arquivos PDF do site GOV.BR e compactá-los em um único arquivo ZIP.

## Descrição

O objetivo deste projeto é acessar uma página específica do site GOV.BR, baixar os anexos I e II em formato PDF e compactá-los em um arquivo ZIP.

## Funcionalidades

1. Acesso ao site: [GOV.BR - ANS](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
2. Download dos Anexos I e II em formato PDF
3. Compactação de todos os anexos em um único arquivo ZIP

## Requisitos

- Python >=3.8
- Bibliotecas: requests, BeautifulSoup, zipfile

Você pode instalar as bibliotecas necessárias executando:

```bash

pip install -r requirements.txt

```

## Como executar

1. Clone este repositório:

```bash
git clone https://github.com/ram0ng1/web_scraping.git
cd web_scraping
```

2. Execute o script Python:

```bash
python web_scraping.py
```
