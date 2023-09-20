from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='./datasets/data.yaml', epochs=50, imgsz=640)

# Inference Code
image_path = 'shape.jpg'
model.predict(source=image_path, save=True, imgsz=640, show=True, conf=0.1)

