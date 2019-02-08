import os

from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

def vision():
    import requests
    # If you are using a Jupyter notebook, uncomment the following line.
    #%matplotlib inline
    import matplotlib.pyplot as plt
    from PIL import Image
    from io import BytesIO


    subscription_key = "3ce370692850429d98d3bfb773bc37c2"
    assert subscription_key

    vision_base_url = "https://centralindia.api.cognitive.microsoft.com/vision/v2.0/"

    analyze_url = vision_base_url + "analyze"

    image_path = "/home/jaskeerat/Projects/ShivNadar/img"


    image_data = open(image_path, "rb").read()
    headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
                  'Content-Type': 'application/octet-stream'}
    params     = {'visualFeatures': 'Description'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    analysis = response.json()
    
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()

    image = Image.open(BytesIO(image_data))
    plt.imshow(image)
    plt.axis("off")
    _ = plt.title(image_caption, size="x-large", y=-0.1)
    return(analysis)

def result():
    # os.system("rm -rf result.txt")
    f = open('result.txt', 'r')
    message = f.read()
    return message
def check():
    
     
    tags=vision()['description']['tags']
    print(tags)
    if('flower' in tags or 'water' in tags or 'green' in tags or 'table' in tags):
        print("True")
    else:
        print("Flase")


@app.route("/")
def home():
    return "WELCOME "


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/pepper")
def pepper():

    os.chdir(
        "/home/jaskeerat/Projects/ShivNadar/ShivNadar_pepper/tensorflow-for-poets-2")
    os.system("python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=/home/jaskeerat/Projects/ShivNadar/img")
    os.chdir("/home/jaskeerat/Projects/ShivNadar/")
    os.system("rm -rf img")
    return result()

    # return render_template('upload.html')


@app.route("/potato")
def potato():
    os.chdir("/home/jaskeerat/Projects/ShivNadar/ShivNadar_potato/tensorflow-for-poets-2")
    os.system("python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=/home/jaskeerat/Projects/ShivNadar/img")
    os.chdir("/home/jaskeerat/Projects/ShivNadar/")
    os.system("rm -rf img")
    return result()


@app.route("/tomato")
def tomato():
    os.chdir("/home/jaskeerat/Projects/ShivNadar/ShivNadar_tomato/tensorflow-for-poets-2")
    os.system("python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=/home/jaskeerat/Projects/ShivNadar/img")
    os.chdir("/home/jaskeerat/Projects/ShivNadar/")
    os.system("rm -rf img")
    return result()


@app.route("/soya")
def soya():
    os.chdir("/home/jaskeerat/Projects/ShivNadar/ShivNadar_soya_bean/tensorflow-for-poets-2")
    os.system("python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=/home/jaskeerat/Projects/ShivNadar/img")
    os.chdir("/home/jaskeerat/Projects/ShivNadar/")
    os.system("rm -rf img")
    return result()

@app.route("/apple")
def apple():
    os.chdir("/home/jaskeerat/Projects/ShivNadar/tensorflow-apple")
    os.system("python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=/home/jaskeerat/Projects/ShivNadar/img")
    os.chdir("/home/jaskeerat/Projects/ShivNadar/")
    os.system("rm -rf img")
    return result()

@app.route("/cherry")
def cherry():
    os.chdir("/home/jaskeerat/Projects/ShivNadar/tensorflow-cherry")
    os.system("python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=/home/jaskeerat/Projects/ShivNadar/img")
    os.chdir("/home/jaskeerat/Projects/ShivNadar/")
    os.system("rm -rf img")
    return result()

@app.route("/corn")
def corn():
    os.chdir("/home/jaskeerat/Projects/ShivNadar/tensorflow-corn")
    os.system("python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=/home/jaskeerat/Projects/ShivNadar/img")
    os.chdir("/home/jaskeerat/Projects/ShivNadar/")
    os.system("rm -rf img")
    return result()

@app.route("/grape")
def grape():
    os.chdir("/home/jaskeerat/Projects/ShivNadar/tensorflow-grape")
    os.system("python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=/home/jaskeerat/Projects/ShivNadar/img")
    os.chdir("/home/jaskeerat/Projects/ShivNadar/")
    os.system("rm -rf img")
    return result()

@app.route("/peach")
def peach():
    os.chdir("/home/jaskeerat/Projects/ShivNadar/tensorflow-peach")
    os.system("python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=/home/jaskeerat/Projects/ShivNadar/img")
    os.chdir("/home/jaskeerat/Projects/ShivNadar/")
    os.system("rm -rf img")
    return result()
@app.route('/upload')
def uploadfile():
    
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':

        f = request.files['file']
        f.save(secure_filename('img'))
        check()
        return render_template('choice.html')
