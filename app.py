from flask import Flask, render_template,request, jsonify, send_file
import numpy as np
import cv2
import base64
import os



def mix_magnitude_phase(modified_comp1, modified_comp2,ratio1, ratio2,c1,c2):
    mag = np.add(modified_comp1*((ratio1/100)),c2*(1-(ratio1/100)))
    phase = np.add(modified_comp2*(ratio2/100),c1*(1-(ratio2/100)))
    OutputImage = np.multiply(mag, np.exp(1j * phase))
    FinalImage = np.real(np.fft.ifft2((OutputImage)))
    FinalImage = (FinalImage - np.min(FinalImage)) / \
        (np.max(FinalImage) - np.min(FinalImage)) * 255
    FinalImage = FinalImage.astype(np.uint8)
    filename = Image.generate_image("hi.png", FinalImage)
    return send_file(filename, mimetype='image/png')


def mix_real_imag(real, imag, ratio1, ratio2):
    # Mix magnitude and imaginary components
    mixed_fft = np.add(real*ratio1/100, 1j * imag*ratio2/100)

    # Perform inverse FFT to get mixed image
    mixed_image = np.real(np.fft.ifft2(mixed_fft))

    # Normalize mixed image values to [0, 255]
    mixed_image = (mixed_image - np.min(mixed_image)) / (np.max(mixed_image) - np.min(mixed_image)) * 255

    # Convert mixed image to uint8 data type
    mixed_image = mixed_image.astype(np.uint8)
    filename = Image.generate_image("hi.png", mixed_image)
    return send_file(filename, mimetype='image/png')




class processimage:
    def __init__(self):
        self.components = []
        self.magnitude = None
        self.phase = None
        self.scaled_phase = None
        self.shifted_real = None
        self.shifted_imag = None
        self.fftMag = None

        f = None

    def get_components(self):
        return self.components
    
    def processimage(self,matrix):
        f = np.fft.fft2(matrix)
        fshift =  np.fft.fftshift(f)
        magnitude_spectrum = np.abs(f)
        scaled_mag = ((magnitude_spectrum - np.min(magnitude_spectrum)) / \
        (np.max(magnitude_spectrum) - np.min(magnitude_spectrum)) * 255).astype('float')
        phase = np.angle(f)

        phase_shift = np.angle(fshift)

        # Normalize phase values to [0, 1]
        phase_norm = (phase_shift + np.pi) / (2 * np.pi)
        
        # Scale phase values to [0, 255]
        phase_scaled = (phase_norm * 255).astype(np.uint8)


        realpart=np.real(f)
        imgpart=np.imag(f)

        shifted_mag = 20*np.log(np.abs(fshift))
        shifted_real = np.real(fshift)
        shifted_imag = np.imag(fshift)

        self.components = [scaled_mag, phase, realpart, imgpart]
        self.phase = phase
        self.magnitude = magnitude_spectrum
        self.scaled_phase = phase_scaled
        self.fftMag = shifted_mag
        self.shifted_real = shifted_real
        self.shifted_imag = shifted_imag

        return self.components
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
        cv2.imwrite(filen,matrix1)
        filename=filen
        return filename
    ###################################################################################################################################################################################    
    ################################################################################################## 
    def generate_component(self, filename,matrix, index_of_component):
        # remove any existing file with the same name
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass
        
        # process the matrix to extract the desired component
        if index_of_component == 0:  
            wanted_component = matrix.fftMag
        elif index_of_component == 1:
            wanted_component = matrix.scaled_phase
        elif index_of_component == 2:
            wanted_component = matrix.shifted_real
        elif index_of_component == 3:
            wanted_component = matrix.shifted_imag

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
    global Image2
    Image=processimage()
    Image2=processimage()
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    data_url1 = request.json['image_data']
    global image1
    image1 = cv2.imdecode(Image.decodefromjs(data_url1), cv2.IMREAD_GRAYSCALE)
    Image.processimage(image1)

    return 'Image saved!'

# @app.route('/image1')
# def image1():
#     filename=Image.generate_image("image1.png",image1)
#     return send_file(filename, mimetype='image/png')

    
@app.route('/real1')
def real():
    filename = Image.generate_component("component1.png", Image, 2)
    return send_file(filename, mimetype='image/png')

@app.route('/imag1')
def imaginary():
    filename=Image.generate_component("component1.png",Image,3)
    return send_file(filename, mimetype='image/png')
    
@app.route('/phase1')
def phase():
    filename=Image.generate_component("component1.png",Image,1)
    return send_file(filename, mimetype='image/png')    

@app.route('/magnitude1')
def mag1():
    filename=Image.generate_component("component1.png",Image,0)
    return send_file(filename, mimetype='image/png') 

################################################################################################################
################################################################################################################
@app.route('/upload2', methods=['POST'])
def upload2():
    data_url = request.json['image_data']
    global image2
    image2 = cv2.imdecode(Image2.decodefromjs(data_url), cv2.IMREAD_GRAYSCALE)
    global c2
    c2=Image2.processimage(image2)
    return 'Image saved!'
    
@app.route('/image2')
def image2():
    filename=Image2.generate_image("image2.png",image2)
    return send_file(filename, mimetype='image/png')    

@app.route('/real2')
def real1():
    filename=Image2.generate_component("component2.png",Image2,2)
    return send_file(filename, mimetype='image/png')

@app.route('/imag2')
def imaginary1():
    filename=Image2.generate_component("component2.png",Image2,3)
    return send_file(filename, mimetype='image/png')
    
@app.route('/phase2')
def phase1():
    filename=Image2.generate_component("component2.png",Image2,1)
    return send_file(filename, mimetype='image/png')    

@app.route('/magnitude2')
def mag2():
    filename=Image2.generate_component("component2.png",Image2,0)
    return send_file(filename, mimetype='image/png')

@app.route('/mixer', methods=['POST'])
def mix_signals():
    global type1, type2, ratio_1, ratio_2, index1, index2,compliment2,compliment

    index1 = request.json['index1']
    index2 = request.json['index2']
    ratio_1 = int(request.json['slider1_val'])
    ratio_2 = int(request.json['slider2_val'])
    img1 = int(request.json['Im1'])
    img2 = int(request.json['Im2'])
    type1 = request.json['type1']
    type2 = request.json['type2']
    print(index1)
    global modified_comp1, modified_comp2
    if img1 == 0:
        modified_comp1 = Image.components[index1]
        if (index1==0): #get the phase
            compliment=Image.components[1]
        elif (index1==1): #get the mag
            compliment=Image.components[0]   

                

    elif img1 == 1:
        modified_comp1 = Image2.components[index1]
        if (index1==0): #get the phase
            compliment=Image2.components[1]
        elif (index1==1): #get the mag
            compliment=Image2.components[0]
    
    
    if img2 == 0:
        modified_comp2 = Image.components[index2]
        if (index2==0): #get the phase
            compliment2=Image.components[1]
        elif (index2==1): #get the mag
            compliment2=Image.components[0]
    elif img2 == 1:
        modified_comp2 = Image2.components[index2]
        if (index2==0): #get the phase
            compliment2=Image2.components[1]
        elif (index2==1): #get the mag
            compliment2=Image2.components[0]
        
    
        

    return 'Indices updated successfully!'

@app.route('/final_image')
def final_im():
    print(type1)

    

    if(type1 == 'magnitude' and type2 == 'phase'):  
        return mix_magnitude_phase(modified_comp1, modified_comp2,ratio_1,ratio_2,compliment,compliment2)
    
    elif(type1 == 'phase' and type2 == 'magnitude'):
        return mix_magnitude_phase(modified_comp2, modified_comp1,ratio_1,ratio_2,compliment2,compliment)
    
    elif(type1 == 'real' and type2 == 'imag'):
        return mix_real_imag(modified_comp1, modified_comp2,ratio_1/100,ratio_2/100)
    
    elif(type1 == 'imag' and type2 == 'real'):
        return mix_real_imag(modified_comp2, modified_comp1,ratio_1/100,ratio_2/100)
    

        
            

##########################################################################################################


if __name__ == '__main__':
    app.run(debug=True)
    
    
    