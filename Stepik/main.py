import csv

names_dict = []

with open('salary_data.csv', 'r', encoding='utf-8') as file_csv
    reader = csv.DictReader(file_csv, delimiter=';')
    for rowDict in reader:
        name, salary = rowDict['company_name'], int(rowDict['salary'])

