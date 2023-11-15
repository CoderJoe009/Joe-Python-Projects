from tabulate import tabulate
import sys
if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
file_name = sys.argv[1]
if '.csv' not in file_name:
    sys.exit('Not a CSV file')
try:
    with open(file_name, 'r') as file:
        table = table = [line.strip().split(',') for line in file.readlines()]
        headers1 = ['Sicilian Pizza','Small','Large']
        headers2 = ['Regular Pizza','Small','Large']
        if file_name == 'sicilian.csv' :
            print(tabulate(table, headers1, tablefmt="grid"))
        elif file_name == 'regular.csv' :
            print(tabulate(table, headers2, tablefmt="grid"))

except FileNotFoundError:
    sys.exit('File does not exist')






