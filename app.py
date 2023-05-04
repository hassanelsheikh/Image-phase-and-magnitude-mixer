from flask import Flask, render_template,request, jsonify, send_file
import numpy as np
import cv2
import base64



app = Flask(__name__)
@app.route('/')
def image_mixer():
    return render_template('index.html')



@app.route('/upload', methods=['POST'])
def upload():
    # Get the data URL from the request JSON
    data_url = request.json['image_data']
    global image1
    image_data = data_url.split(',')[1]

# Decode the image data from base64
    decoded_data = base64.b64decode(image_data)
 
# Convert the decoded data to a NumPy array
    np_data = np.frombuffer(decoded_data, np.uint8)
    image1 = cv2.imdecode(np_data, cv2.IMREAD_COLOR)

    # img1=cv2.imread(data_url,cv2.IMREAD_COLOR)
    # # Decode the data URL and save the image to a file
    # with open('image.jpg', 'wb') as f:
    #     f.write(base64.b64decode(data_url.split(',')[1]))
    f = np.fft.fft2(image1)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))


    phase = np.angle(fshift)
    cv2.imshow('hmm', image1)

    cv2.imshow('Magnitude', magnitude_spectrum)
    cv2.imshow('Phase', phase)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return 'Image saved!'


if __name__ == '__main__':
    app.run(debug=True)