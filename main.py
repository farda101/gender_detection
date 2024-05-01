from ultralytics import YOLO

model = YOLO('best.pt')

data = 'vid.mp4'
model.predict(source=data, show=True, conf=0.5)