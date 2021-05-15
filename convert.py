import csv
import json
from PIL import Image, ImageDraw

with open('sample.csv') as csvDataFile:
    data=list(csv.reader(csvDataFile))

#initialize the sample jpg image
image = Image.open("sample.jpg")

for index in range(1, len(data)): 
    box_values = json.loads(data[index][0])
    x1_value = box_values.get('x1')
    y1_value = box_values.get('y1')
    x2_value = box_values.get('x2')
    y2_value = box_values.get('y2')
    # Draw a box over the specified coordinates
    draw = ImageDraw.Draw(image)
    draw.rectangle((x1_value, y1_value, x2_value, y2_value), fill=None, outline="yellow",width=3)

image.save("test.jpg")