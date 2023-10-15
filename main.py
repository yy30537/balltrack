from ultralytics import YOLO
from pathlib import Path
import matplotlib.pyplot as plt

# Load trained model
model_path = Path("runs/detect/train11/weights/best.pt")
model = YOLO(str(model_path))

# Load test dataset
test_data_path = Path("data/test/images")
test_images = list(test_data_path.glob("*.jpg"))
#test_images = list(test_data_path.glob("*.jpg"))[:10]  # Get first 10 images

# Run model on test dataset
results = model.predict(source=test_images)

# Evaluate model
model.val() 

