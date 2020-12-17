# Import libraries.
import cv2 as cv  # Computer vision library.
from time import sleep  # Time library.
import numpy as np  # Array library.

# Camera setup.
vc = cv.VideoCapture(0);
# Variable setup
samples = 1
name = input("ingrese nombre de la clase")
index = 'classes/' + name  # Path to save images.
counter = 0  # Number of image taken.
flag = 0  # Flag to take images.

# Image capture.

while True:
    ret, image = vc.read() #Reading.
    cv.imshow('Capture', image)
    # Image filtering.
    gray1 = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(np.uint8(gray1), 85, 70)  
    cv.imshow('Processed image', edges)            #show image preprocesada
    # Image saving flag.
    path = index + str(counter) + '.jpg'
    if cv.waitKey(1) & 0xFF == ord('s'):				#empezar a tomar fotos
        flag = 1
        print('Writing...')
        sleep(10)  # Idle time to setup.
    else:
        pass

    # Image saving.
    if flag == 1:
        cv.imwrite(path, edges)
        counter += 1
        print('{} images saved.'.format(counter))

        if counter == samples:
            break

    
# Destroy the window when finished.
cv.destroyAllWindows()
