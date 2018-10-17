import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("team2.jpg")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# faces is an array of multi list
faces = face_cascade.detectMultiScale(gray_img,
# 1.05 -> 1.1 detect 2 face thanh chi 1 face nguoi
scaleFactor=1.1,
minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

print(type(faces))
print(faces)

resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

#cv2.imshow("Gray",gray_img)
#cv2.imshow("Gray",img)
cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
