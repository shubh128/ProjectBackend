import flask 
import werkzeug
import time	
import cv2
import os
import time

import numpy as np
from matplotlib import pyplot as plt



app = flask.Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    files_ids = list(flask.request.files)
    print("\nNumber of Received Images : ", len(files_ids))
    image_num = 1
    for file_id in files_ids:
        print("\nSaving Image ", str(image_num), "/", len(files_ids))
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        timestr  =  time.strftime("%Y%m%d-%H%M%S")
        #Filename1 = timestr+'_'+filename
        #global Filename
       # Filename = "WTF"
        imagefile.save("test")
        image_num = image_num + 1
    print("\n")
    return "Image(s) Uploaded Successfully. Come Back Soon."

# @app.route('/Binary', methods=['GET', 'POST'])
# def Binary():
#     print("Its working canny Binary")
#     image = cv2.imread('/home/jathin/Desktop/Projects/Boils FInal/test')
#     # scale_percent = 20 # percent of original size
#     # width = int(image.shape[1] * scale_percent / 100)
#     # height = int(image.shape[0] * scale_percent / 100)
#     # dim = (width, height)
#     # img = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
#     ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
#     cv2.imshow('Original image',image)
#     cv2.imshow('Gray image', thresh1)
#     # ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
#     # ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#     # ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
#     # ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
#     # titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
#     # images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
#     # for i in range(6):
#     #     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     #     plt.title(titles[i])
#     #     plt.xticks([]),plt.yticks([])

#     return "Success"

    image_num = 1
    for file_id in files_ids:
        print("\nSaving Image ", str(image_num), "/", len(files_ids))
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        timestr  =  time.strftime("%Y%m%d-%H%M%S")
        #Filename1 = timestr+'_'+filename
        #global Filename
       # Filename = "WTF"
        imagefile.save("test")
        image_num = image_num + 1
        image = cv2.imread('/home/jathin/Desktop/Projects/Boils FInal/test')
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('Original image',image)
#     cv2.imshow('Gray image', gray)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     print("Working")
#     return "Success"


@app.route('/Sobel', methods=['GET', 'POST'])
def Sobel():
    print("Its working Sobel")
    os.system('python3 Final.py')
    time.sleep(5)
    return "Success"



@app.route('/Canny', methods=['GET', 'POST'])
def Canny():
    print("Its working canny")
    image = cv2.imread('./test')
    scale_percent = 20 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img,100,200)
    # cv2.imshow('Original image',img)
    # cv2.imshow('Canny image', edges)
    cv2.imwrite( "./Final/Canny.jpg", edges)
    # cv2.imshow('Gray image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Working")
    return "Success"



app.run(host="0.0.0.0", port=5000, debug=True)