from flask import Flask, render_template,request, jsonify, send_file
import numpy as np
import cv2
import base64
import os

def removefile(name):
    file_path = name
    if os.path.exists(file_path):
        os.remove(name)
    
def processimage(matrix):
    f = np.fft.fft2(matrix)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    phase = np.angle(fshift)
    realpart=np.real(fshift)
    imgpart=np.imag(fshift)
    return magnitude_spectrum,phase,realpart,imgpart
    

app = Flask(__name__)
@app.route('/')
def image_mixer():
    return render_template('index.html')



@app.route('/upload', methods=['POST'])
def upload():
    # Get the data URL from the request JSON
    data_url = request.json['image_data']
    image_data = data_url.split(',')[1]

# Decode the image data from base64
    decoded_data = base64.b64decode(image_data)
 
# Convert the decoded data to a NumPy array
    np_data = np.frombuffer(decoded_data, np.uint8)
    global image1
    image1 = cv2.imdecode(np_data, cv2.IMREAD_COLOR)

    # f = np.fft.fft2(image1)
    # global fshift
    # fshift = np.fft.fftshift(f)
    
    # # magnitude_spectrum = 20*np.log(np.abs(fshift))
    # # phase = np.angle(fshift)
    # # realpart=np.real(fshift)
    # # imgpart=np.imag(fshift)

    return 'Image saved!'

@app.route('/image1')
def image1():
    removefile("image1.png")
    cv2.imwrite("image1.png",image1)
    filename="image1.png"
    return send_file(filename, mimetype='image/png')

    
@app.route('/real1')
def real():
    removefile("real1.png")
    magnitude_spectrum,phase,realpart,imgpart=processimage(image1)
    cv2.imwrite('real1.png', realpart)
    filename="real1.png"
    return send_file(filename, mimetype='image/png')

@app.route('/imag1')
def imaginary():
    removefile("imag1.png")
    magnitude_spectrum,phase,realpart,imgpart=processimage(image1)
    cv2.imwrite('imag1.png', imgpart)
    filename="imag1.png"
    return send_file(filename, mimetype='image/png')
    
    


    
if __name__ == '__main__':
    app.run(debug=True)
    
    
    