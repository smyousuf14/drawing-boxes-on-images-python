import csv
import json

with open('sample.csv') as csvDataFile:
    data=list(csv.reader(csvDataFile))

print(data[1][0])
x_value = json.loads(data[1][0])
print(x_value.get('x'))
