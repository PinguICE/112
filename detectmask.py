import cv2
import numpy as np
import tensorflow as tf
model = tf.keras.models.load_model("keras_model.h5")

catnap = cv2.VideoCapture(0)

while True:
    check, frame = catnap.read()
    img = cv2.resize(frame,(224,224))
    testimg = np.array(img,dtype = np.float32)
    testimg = np.expand_dims(testimg,axis=0)
    normalimg = testimg / 255.0
    predicion = model.predict(normalimg)
    print("Predicción",predicion)
    cv2.imshow("Resultado",frame)
    key = cv2.waitKey(1)
    if key == 32:
        break
cv2.destroyAllWindows()

# para copiar python3 detectmask.py