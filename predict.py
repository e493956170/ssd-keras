from ssd import SSD
from PIL import Image
import numpy as np
ssd = SSD()

import cv2





# img = 'img/test.jpg'
# try:
#     image = Image.open(img)
# except:
#     print('Open Error! Try again!')
# else:
#     r_image = ssd.detect_image(image)
#     r_image = cv2.cvtColor(np.asarray(r_image),cv2.COLOR_RGB2BGR)  
#     cv2.imshow("ObjectDection",r_image)
#     cv2.waitKey(0)

cap = cv2.VideoCapture(0)
while True:
    ret ,frame = cap.read()
    # img = input('Input image filename:')
    try:
        # image = Image.open(img)
        image = frame
    except:
        print('Open Error! Try again!')
    else:
        r_image = ssd.detect_image(image)
        r_image = cv2.cvtColor(np.asarray(r_image),cv2.COLOR_RGB2BGR)  
        cv2.imshow("ObjectDection",r_image)
        cv2.waitKey(1)

# ssd.close_session()
    