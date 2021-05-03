import csv
import pandas as pd

with open('sample.csv') as csvDataFile:
    data=list(csv.reader(csvDataFile))
print(data)
