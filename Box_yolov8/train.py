from ultralytics import YOLO

# YOLO 모델 인스턴스화
model = YOLO("yolov8s.pt")

results = model.train(
    data="C:/KMS/Tensorflow_project/Box_yolov8/data.yaml", epochs=30, imgsz=640
)
