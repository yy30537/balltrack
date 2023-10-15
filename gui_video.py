import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO
import cv2
from pathlib import Path
from PIL import Image, ImageTk

# Load trained model
model_path = Path("runs/detect/train11/weights/best.pt")
model = YOLO(str(model_path))

def process_frame(frame):
    # Process frame
    results = model.predict(source=frame)
    pred = results[0]
    
    # If basketball is detected, draw bounding boxes
    if pred.boxes is not None and pred.boxes.xyxy.shape[0] > 0:
        x1, y1, x2, y2 = map(int, pred.boxes.xyxy[0].tolist())
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    return frame

def update_frame(cap, label):
    _, frame = cap.read()
    if frame is not None:
        frame = process_frame(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)
        label.config(image=photo)
        label.image = photo
        label.after(10, update_frame, cap, label)  # Call again after 10ms

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        cap = cv2.VideoCapture(file_path)
        update_frame(cap, label_image)

root = tk.Tk()
root.title("Basketball Detection")

btn_open = tk.Button(root, text="Open Video", command=open_file)
btn_open.pack()

label_image = tk.Label(root)
label_image.pack()

root.mainloop()
