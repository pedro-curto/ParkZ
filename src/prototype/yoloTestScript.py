import numpy
from ultralytics import YOLO
from PIL import Image, ImageDraw
import cv2
import time
import numpy as np

def draw_bounding_box(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    """
    Draws bounding boxes on the input image based on the provided arguments.

    Args:
        img (numpy.ndarray): The input image to draw the bounding box on.
        class_id (int): Class ID of the detected object.
        confidence (float): Confidence score of the detected object.
        x (int): X-coordinate of the top-left corner of the bounding box.
        y (int): Y-coordinate of the top-left corner of the bounding box.
        x_plus_w (int): X-coordinate of the bottom-right corner of the bounding box.
        y_plus_h (int): Y-coordinate of the bottom-right corner of the bounding box.
    """
    label = f"{class_id} ({confidence:.2f})"
    color = "red"
    cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 2)
    cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Load the YOLO model
model = YOLO('yolov8n.pt')  # Confirm the model file path and name

# Load the image
image_path = 'img1.jpg'
original_image: np.ndarray = cv2.imread(image_path)
frame = cv2.imread(image_path)
pred = {}
if frame is not None:
    # Run YOLOv8 inference on the frame
    results = model(frame, conf=0.05, iou=0.85)
    
    for det in results[0]:  # Assuming results.xyxy[0] contains the detections for the first image
        #x_min, y_min, x_max, y_max, confidence, class_idx = int(det[0]), int(det[1]), int(det[2]), int(det[3]), det[4], results.cls
        #print(x_min, y_min, x_max, y_max, confidence, class_idx)
        class_number = results.cls


        if class_number == 2:  # Check if detected class is 'car'
            draw_bounding_box(original_image, class_number, confidence, x_centre - w, y_centre - h, x_centre + w, y_centre + h)
                    
                #if not predictions.get(class_name): predictions[class_name] = [[box.xyxy[0]]] 
                #else: predictions[class_name] += [box.xyxy[0]]
     

cv2.imshow("image", original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

