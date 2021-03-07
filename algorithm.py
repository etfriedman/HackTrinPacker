import numpy as np

im = np.array[]

#convert rgb colorspace to lms
RGB_TO_LMS = np.array[[17.8824,43.5161,4.11935],
                      [3.45565,27.1554,3.86714],
                      [0.0299566,0.184309,1.46709]]

#convert regular lms to lms as seen by protanopia
p = np.array[[0,2.02344,-2.52581],
             [0,1,0],
             [0,0,1]]
#convert regular lms to lms as seen by duteranopia
d = np.array[[1,0,0],
             [0.494207,0,1.24827],
             [0,0,1]]
#convert regular lms to lms as seen by tritanopia
t = np.array[[1,0,0],
             [0,1,0],
             [-0.395913,0.801109,0]]

for i in np.nditer(im):
    rgb = np.array[i[0],i[1],i[2]]
    lmb = RGB_TO_LMS @ rgb



print(a @ b)