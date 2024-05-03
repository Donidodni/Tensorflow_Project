from ultralytics import YOLO
import cv2

model = YOLO("yolov8s.pt")

result = model(source="./detect2.mp4", show=True, conf=0.5, save=True)
