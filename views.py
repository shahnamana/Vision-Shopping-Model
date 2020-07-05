import os
from flask import Flask, flash, request, redirect, url_for
from flask import render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.getcwd()+'\\image'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request

def webscrapfn(query_add):
    my_url = 'https://www.google.com/search?tbm=shop&q='+query_add
    print(my_url)
    hdr = {'User-Agent': 'Mozilla/5.0'}
    request = Request(my_url, headers=hdr)
    uClient = uReq(request)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html,'html.parser')

    '''
    the following line provides proper output for img, pricelist, name_prod

    '''
    containers = page_soup.findAll('div' , {'class' :'u30d4'})

    price_lst = []

    img_url = []

    name_prod = []

    for container in containers[:10]:
        for j in container.findAll('span', {'class':"HRLxBb"}):
            price_lst.append(j.text)
        for a in container.find_all('a'):
            name_prod.append(a.text)
        for a in container.findAll('img'):
            img_url.append(a.get('src'))

    '''
    The next line removes the blank entries got from a tag of images as they don't have any text
    '''

    prodlist = dict()
    main_list_all_items = []

    print(len(img_url))
    for i in range(9):
        prodlist = dict()
        prodlist['name_prod'] = name_prod[i]
        prodlist['img_url'] = img_url[i]
        prodlist['price_lst'] = price_lst[i]
        main_list_all_items.append(prodlist)

    return main_list_all_items



def google_vision_api(img_path):

    import io
    import os

    # Imports the Google Cloud client library
    from google.cloud import vision
    from google.cloud.vision import types

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    # file_name = os.path.abspath('test_images/22.jpg')
    file_name = img_path

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')


    l = []

    for label in labels:
        print(label.description)
        l.append(label.description)
    temp_lab = l
    l = ['t+shirt' if x=='Tshirt' else x for x in l]
    l = [l[i].replace(' ' ,'+') for i in range(len(l))]

    query = "+".join(l[:6])

    return query


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            img_path = UPLOAD_FOLDER+'\\'+filename

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            q = google_vision_api(img_path)
            list1 = webscrapfn(q)
            return render_template('display.html', main_list_all_items = list1)
    return render_template("index.html")




if __name__ == '__main__':
    app.run()
