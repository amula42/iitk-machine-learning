import csv
filename = open('indians-diabetes.data.csv')

reader = csv.reader(filename, delimiter=',')

lines = list(reader)

print('No of Rows: ', len(lines), '\n\n')

print("List of Data \n", lines )