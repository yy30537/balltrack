from ultralytics import YOLO

# Load a model
model = YOLO('yolov8-custom.yaml')

# Train the model
model.train(data='data/data.yaml', epochs=10)
