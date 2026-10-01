import csv

with open('IBGE.csv', 'r', encoding='utf-8-sig', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=';')
    for linha in leitor_csv:
        print(linha)