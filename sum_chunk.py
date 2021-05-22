import sys
import csv
import os

input_file = sys.argv[1]
name = os.path.basename(input_file)
output_file = os.path.splitext(name)[0]+'.sum'
#print(input_file)
print(output_file)

counter = 0
columns = []
student_courses = []
with open(input_file, mode = 'r') as csv_file:
    reader = list(csv.reader(csv_file, delimiter = '\t'))#iterator gets exhausted -> conversion to list
    courses = []
    for row in reader:
        student = row[0]
        found = False
        if len(courses)>0:
            for c in courses:
                if student in c:
                    found == True
        if found == False:
            counter = 0
            grade_sum = 0
            for row1 in reader:
                compare_student = row1[0]
                if compare_student == student:
                    counter = counter + 1
                    grade_sum = grade_sum + float(row1[2])
            summed_student = [student, counter, grade_sum]
            courses.append(summed_student)
    csv_file.close()

try:
    path = "chunks/summed/"+output_file
    file = open( path, 'w+')
    for c in courses:
        file.write(str(c))
    file.close()
except:
    print("Writing to file not possible.")
