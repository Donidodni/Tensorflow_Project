from ultralytics import YOLO
import cv2


model = YOLO(r"C:\KMS\Tensorflow_project\best.pt")
results = model(
    r"C:\KMS\Tensorflow_project\dog_pic.jpg",
    show=True,
)
cv2.waitKey(0)
