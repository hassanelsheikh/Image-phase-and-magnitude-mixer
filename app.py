from flask import Flask, render_template,request, jsonify, send_file
import numpy as np
import cv2
import base64



app = Flask(__name__)
@app.route('/')
def image_mixer():
    return render_template('index.html')

@app.route('/send_image1', methods=['POST'])
def get_signal():
    global image1
    array= request.get_json()
    image1=array[0]
    img=np.array(image1)
    cv2.imwrite('image.png', img)

    # cv2.imshow('tamam ?', np.array(image1))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return jsonify({'img': img.size})

@app.route('/upload', methods=['POST'])
def upload():
    # Get the data URL from the request JSON
    data_url = request.json['image_data']

    # Decode the data URL and save the image to a file
    with open('image.jpg', 'wb') as f:
        f.write(base64.b64decode(data_url.split(',')[1]))

    return 'Image saved!'


if __name__ == '__main__':
    app.run(debug=True)