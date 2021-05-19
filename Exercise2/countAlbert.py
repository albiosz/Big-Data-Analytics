#output task 1: Building DAG of jobs...
#Nothing to be done.
#coursesTaken-A.csv
#coursesTaken-B.csv
import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

result = set()

with open(input_file, mode = 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter = '\t')
    
    for row in reader:
        result.add(row[0])

    csv_file.close()

unique_item_count = len(result)
print(unique_item_count)

try:
    file = open(output_file, 'w+')
    file.write(str(unique_item_count))
    file.close()
except:
    print("Writing to file not possible.")