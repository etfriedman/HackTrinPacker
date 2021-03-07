import os.path
import numpy as np
from PIL import Image

fpath = "./images/ethan.jpg"
im = Image.open(fpath) #input image object
im = im.convert('RGB')
imRGB = np.asarray(im) #input image rgb matrix
blindness_type = '' #can be p, d, or t to select which type of colorblindness the user has

#conversions between rgb colorspace and lms colorspace
RGB_TO_LMS = np.array([[17.8824,43.5161,4.11935],
                      [3.45565,27.1554,3.86714],
                      [0.0299566,0.184309,1.46709]])
LMS_TO_RGB = np.linalg.inv(RGB_TO_LMS)

#conversions between lms and colorblind lms (protanopia, duteranopia, tritanopia)
p = np.array([[0,2.02344,-2.52581],
             [0,1,0],
             [0,0,1]])
d = np.array([[1,0,0],
             [0.494207,0,1.24827],
             [0,0,1]])
t = np.array([[1,0,0],
             [0,1,0],
             [-0.395913,0.801109,0]])

#shift matrices for each colorblindness type (protanopia, duteranopia, tritanopia)
pShift = np.array([[0,0,0],
                  [0.7,1,0],
                  [0.7,0,1]])
dShift = np.array([[1,0.7,0],
                  [0,0,0],
                  [0,0.7,1]])
tShift = np.array([[1,0,0.7],
                  [0,1,0.7],
                  [0,0,0]])

#simulate input image as seen by colorblindness in rgb space
sim = np.zeros(np.shape(imRGB))
out = sim
for i in range(np.shape(imRGB)[0]):
    for j in range(np.shape(imRGB)[1]):
        rgb = imRGB[i,j,:]
        lmb = RGB_TO_LMS @ np.transpose(rgb)

        #simulate colorblindness depending on value of blindness_type in lms colorspace
        if blindness_type == 'p':
            simLMS = p @ lmb
        elif blindness_type == 'd':
            simLMS = d @ lmb
        else:
            simLMS = t @ lmb

        #convert simulated image to rgb colorspace
        sim[i,j,:] = np.transpose(LMS_TO_RGB @ simLMS)

        #get differences in rgb values
        diff = rgb - sim[i,j,:]

        #get shift matrices
        if blindness_type == 'p':
            shifter = pShift @ np.transpose(diff)
        elif blindness_type == 'd':
            shifter = dShift @ np.transpose(diff)
        else:
            shifter = tShift @ np.transpose(diff)
        
        out[i,j,:] = rgb + np.transpose(shifter)

#create and save image object from shifted matrix
outIm = Image.fromarray(out, mode = 'RGB')
outIm.save("test.jpg", "JPEG")
outIm.show()