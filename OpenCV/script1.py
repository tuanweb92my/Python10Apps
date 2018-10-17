import cv2
import os
import glob

path = '/Users/nguyeant/Documents/GitHub/Python10Apps/OpenCV/sample-images'
i = 10
for filename in glob.glob(os.path.join(path,'*.jpg')):
    i = i + 1
    # print(filename)
    img=cv2.imread(filename,0)

    #print(type(img))
    #print(img)
    #print(img.shape)
    #print(img.ndim)

# resized_image = cv2.resize(img,(1000,500))
    resized_image = cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))
    #cv2.imshow(filename,resized_image)
    cv2.imwrite('/Users/nguyeant/Documents/GitHub/Python10Apps/OpenCV/hinh'+ str(i) + '.jpg',resized_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
