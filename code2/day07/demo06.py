import csv

csv_file = open('demo.csv', 'r', newline='', encoding='utf-8')
reader = csv.reader(csv_file)
for i in reader:
    print(i)
csv_file.close()
