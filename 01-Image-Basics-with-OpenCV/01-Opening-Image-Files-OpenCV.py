import os

import cv2

path = os.curdir
path = os.path.join(path, '../')
path = os.path.join(path, 'DATA/00-puppy.jpg')
print(path)
img = cv2.imread(path)


while True:

    cv2.imshow('Puppy',img)

    # EXPLANATION FOR THIS LINE OF CODE:
    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163
    
    # IF we've waited at least 1 ms AND we've pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
