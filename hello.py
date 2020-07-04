from flask import Flask, redirect, render_template, request
import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    # client = vision.ImageAnnotatorClient()
    #
    # # The name of the image file to annotate
    # file_name = os.path.abspath('test_images/niketshirt.jpg')
    #
    # # Loads the image into memory
    # with io.open(file_name, 'rb') as image_file:
    #     content = image_file.read()
    #
    # image = types.Image(content=content)
    #
    # # Performs label detection on the image file
    # response = client.label_detection(image=image)
    # labels = response.label_annotations
    # l = []
    #
    # color = ['Pink', 'Red', 'Brown', 'Black', 'White', 'Yellow', 'Blue', 'Green', 'Grey', 'Purple', 'Orange', 'Maroon']
    #
    # for label in labels:
    #     # print(label.description)
    #     l.append(label.description)
    print(request.method)
    if request.method == 'GET':
        print('hello')

        if request.form.get('redirect')=='Redirect':
            print('helllsnckasnkmascnasoidkasdlknawdjknwdniwjd')
            return redirect("/redirect")

    return render_template("first_page.html")


@app.route('/redirect', methods = ['GET', 'POST'])
def red():
    if request.method == 'GET':
        return redirect("https://www.google.com/", code=302)
    else:
        pass

if __name__ == "__main__":
    app.run()
