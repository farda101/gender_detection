from pymongo import MongoClient
from ultralytics import YOLO
import csv


client = MongoClient('mongodb://localhost:27017/')
db = client['object-detection']
collection = db['gender']

def save_to_csv(predictions, csv_file):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if predictions.boxes is not None and len(predictions.boxes) > 0:
            for pred in predictions.boxes[0]:
                class_index = int(pred.cls[0])
                class_name = model.names[class_index]
                writer.writerow([class_name])

def save_to_mongodb(predictions):
    if predictions.boxes is not None and len(predictions.boxes) > 0:
        for pred in predictions.boxes[0]:
            class_index = int(pred.cls[0])
            class_name = model.names[class_index]
            
            collection.insert_one({'label': class_name})
            
csv_file = 'object-detection.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['label'])

model = YOLO('best.pt')

for frame in model.predict(source=0, show=True, conf=0.5, stream=True):
    save_to_mongodb(frame)
    save_to_csv(frame, csv_file)