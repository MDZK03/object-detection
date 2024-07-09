from ultralytics import YOLO
from tkinter import Tk, filedialog
import cv2

def image():
    def select_image():
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        if file_path:
            image = cv2.imread(file_path)
            return image
        else:
            return None

    # load a pretrained YOLOv8n model
    model = YOLO("model/yolov8n.pt", "v8")

    #choose the image want to detect
    img_source = select_image()

    detection_output = model.predict(source=img_source, conf=0.25, save=True, show=True)
    
    cv2.imshow("ORIGINAL", img_source)