from flask import Flask, render_template,request, jsonify, send_file
import numpy as np
import cv2
import base64
import os

class processimage:
    
    def processimage(self,matrix):
        f = np.fft.fft2(matrix)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20*np.log(np.abs(fshift))
        phase = np.angle(fshift)

        phase = np.angle(fshift)
        
        # Normalize phase values to [0, 1]
        phase_norm = (phase + np.pi) / (2 * np.pi)
        
        # Scale phase values to [0, 255]
        phase_scaled = (phase_norm * 255).astype(np.uint8)


        realpart=np.real(fshift)
        imgpart=np.imag(fshift)
        components=[]
        components.append(magnitude_spectrum)
        components.append(phase_scaled)
        components.append(realpart)
        components.append(imgpart)
        return components
    ################################################################################################################################
    ################################################################################################################################
    def decodefromjs(self,data_url):
        image_data = data_url.split(',')[1]

    # Decode the image data from base64
        decoded_data = base64.b64decode(image_data)
    
    # Convert the decoded data to a NumPy array
        np_data = np.frombuffer(decoded_data, np.uint8)
        return np_data
    ################################################################################################################################
    ################################################################################################################################    
    def generate_image(self,filen,matrix1):
        self.removefiles(filen)
        print(type(matrix1))
        cv2.imwrite(filen,matrix1)
        filename=filen
        print('AAAAAAAAAh')
        return filename
    ###################################################################################################################################################################################    
    ################################################################################################## 
    def generate_component(self, filename, matrix, index_of_component):
        # remove any existing file with the same name
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass
        
        # process the matrix to extract the desired component
        wanted_component = Image.processimage(matrix)[index_of_component]

        # save the component as a JPEG file
        cv2.imwrite(filename, wanted_component)

        # return the filename of the saved file
        return filename

    def removefiles(self,name):
        file_path = name
        if os.path.exists(file_path):
            os.remove(name)
    

###################################################################################################################################################################################
 ###################################################################################################################################################################################
app = Flask(__name__)
@app.route('/')
def image_mixer():
    global Image
    Image=processimage()

    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    data_url1 = request.json['image_data']
    global image1
    image1 = cv2.imdecode(Image.decodefromjs(data_url1), cv2.IMREAD_GRAYSCALE)

    return 'Image saved!'

# @app.route('/image1')
# def image1():
#     filename=Image.generate_image("image1.png",image1)
#     return send_file(filename, mimetype='image/png')

    
@app.route('/real1')
def real():
    global image1
    filename = Image.generate_component("component1.jpeg", image1, 2)
    print(filename)
    return send_file(filename, mimetype='image/jpeg')

@app.route('/imag1')
def imaginary():
    filename=Image.generate_component("component1.png",image1,3)
    return send_file(filename, mimetype='image/png')
    
@app.route('/phase1')
def phase():
    filename=Image.generate_component("component1.png",image1,1)
    return send_file(filename, mimetype='image/png')    

@app.route('/magnitude1')
def mag1():
    filename=Image.generate_component("component1.png",image1,0)
    return send_file(filename, mimetype='image/jpeg') 

################################################################################################################
################################################################################################################
@app.route('/upload2', methods=['POST'])
def upload2():
    data_url = request.json['image_data']
    global image2
    image2 = cv2.imdecode(Image.decodefromjs(data_url), cv2.IMREAD_GRAYSCALE)
    return 'Image saved!'
    
@app.route('/image2')
def image2():
    filename=Image.generate_image("image2.png",image2)
    return send_file(filename, mimetype='image/png')    

@app.route('/real2')
def real1():
    filename=Image.generate_component("component2.png",image2,2)
    return send_file(filename, mimetype='image/png')

@app.route('/imag2')
def imaginary1():
    filename=Image.generate_component("component2.png",image2,3)
    return send_file(filename, mimetype='image/png')
    
@app.route('/phase2')
def phase1():
    filename=Image.generate_component("component2.png",image2,1)
    return send_file(filename, mimetype='image/png')    

@app.route('/magnitude2')
def mag2():
    filename=Image.generate_component("component2.png",image2,0)
    return send_file(filename, mimetype='image/png')



if __name__ == '__main__':
    app.run(debug=True)
    
    
    