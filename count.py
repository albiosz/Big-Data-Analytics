#output task 1: Building DAG of jobs...
#Nothing to be done.
#coursesTaken-A.csv
#coursesTaken-B.csv
import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]
print(input_file)
print(output_file)

counter = 0
columns = []
with open(input_file, mode = 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter = '\t')
    for row in reader:
        for r in row:
            counter += 1
        break
    print(counter)
    for i in range(0, counter):
        new_column = []
        columns.append(new_column)
    print(columns)
    for row_ in reader:
        #print(row_)
        idx = 0
        for r_ in row_:
            columns[idx].append(r_)
            idx += 1
    csv_file.close()
unique_item_count = len(set(columns[0]))
print(unique_item_count)
try:
    file = open(output_file, 'w+')
    file.write(str(unique_item_count))
    file.close()
except:
    print("Writing to file not possible.")
