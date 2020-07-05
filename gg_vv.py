import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('test_images/22.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')


l = []

color = ['Pink', 'Red', 'Brown', 'Black', 'White', 'Yellow', 'Blue', 'Green', 'Grey', 'Purple', 'Orange', 'Maroon']

for label in labels:
    print(label.description)
    l.append(label.description)

print(labels)
print(" ".join(l))

#
#
# for i in range(5):
#     print(i)
# print()
#
# a = [0,1,2,3,4,5,6,7,8,9,10]
#
# for i in range(len(a)):
#     print(i)
