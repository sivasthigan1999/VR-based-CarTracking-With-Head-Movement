from cvzone.FaceDetectionModule import FaceDetector
import cv2
import socket

cap=cv2.VideoCapture(0)
cap.set(3, 640) #width
cap.set(4 ,480) #height

##For find the X , Y co-ordinates of the faces
detector = FaceDetector()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ('127.0.0.1', 5052)

while True:
    success, img =cap.read()
    # For find the Faces
    img, bboxs = detector.findFaces(img) #bounding box and images
    if bboxs:
        center = bboxs[0]['center'] #Gives the X and Y values of the center of the bounding box
        print(center)
        data = str.encode(str(center))
        sock.sendto(data, serverAddressPort)
    cv2.imshow('image', img)
    cv2.waitKey(1)
