import cv2
import numpy as np
catnap = cv2.VideoCapture(0)

while True:
    success, image = catnap.read()
    image = cv2.flip(image,1)
    cv2.imshow("Leyendo img",image)
    key = cv2.waitKey(1)
    if key == 32:
        break
cv2.destroyAllWindows()




# para copiar python3 abrircam.py