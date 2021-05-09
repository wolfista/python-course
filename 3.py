import csv

with open('users-simple-five.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    for row in csv_reader:
        print(row)

field_names = ['Id', 'Reputation', 'Location', 'DisplayName']
with open('users-simple-five.csv') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file, fieldnames = field_names)
    for row in csv_dict_reader:
        print(row['Location'])