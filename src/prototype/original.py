import numpy
from ultralytics import YOLO
from PIL import Image, ImageDraw
import cv2
import time




model1 = YOLO('yolov8n.pt')
counter = 9 
cap = cv2.VideoCapture(r"images/test-python.jpg")
#cap = cv2.VideoCapture(0)
while cap.isOpened():
    #counter+=1
    # Read a frame from the video
    success, frame = cap.read()
    predictions = {}
    if success:

        # Run YOLOv8 inference on the frame
        car_confidence_threshold = 0.15
        results1 = model1(frame, conf=0.25)
        for pred in results1: # if it is only an image and not a stream this for only runs 1 time
            boxes = pred.boxes
            for box in boxes:
                class_name = model1.names[int(box.cls)]
                
                if not predictions.get(class_name): predictions[class_name] = [[box.xyxy[0]]] 
                else: predictions[class_name] += [box.xyxy[0]]
        
        cv2.imshow("prediction", results1[0].plot())
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        #time.sleep(10)
cap.release()
cv2.destroyAllWindows()