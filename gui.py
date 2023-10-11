import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO
import cv2
from pathlib import Path
from PIL import Image, ImageTk

# Load trained model
model_path = Path("runs/detect/train8/weights/best.pt")
model = YOLO(str(model_path))

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Load image and run prediction
        image = cv2.imread(file_path)
        results = model.predict(source=image)
        
        # Extracting the first prediction result
        pred = results[0]
        
        # Rendering and displaying the image
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)
        image_tk = ImageTk.PhotoImage(image_pil)
        label_image.config(image=image_tk)
        label_image.image = image_tk
        
        # Displaying detection result
        pred_label = "Basketball Detected" if len(pred) > 0 else "No Basketball Detected"
        label_result.config(text=pred_label)

root = tk.Tk()
root.title("Basketball Detection")

btn_open = tk.Button(root, text="Open Image", command=open_file)
btn_open.pack()

label_image = tk.Label(root)
label_image.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
