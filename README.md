## Shape-Detection
# Introduction
This report provides an overview and analysis of a Python script that utilizes the Ultralytics library to work with a YOLOv8 object detection model. The script performs two primary tasks: training the YOLOv8 model on a custom dataset and conducting inference on a sample image. The script's functionality, including model loading, training, and inference, is examined in detail.

# Script Overview
The Python script leverages the Ultralytics library to work with a YOLOv8 model. YOLO (You Only Look Once) is a popular object detection algorithm known for its speed and accuracy.

# Dataset classes
names: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'circle', 'cross', 'g', 'hexagon', 'pentagon', 'plus', 'rectangle', 'star', 'trapezium', 'triangle']
![labels_correlogram](https://github.com/MaramWael02/Shape-Detection/assets/95209939/dd5f5d6d-c59a-46ab-b5be-71ad1f522aa1)
![labels](https://github.com/MaramWael02/Shape-Detection/assets/95209939/d0ff43e1-cada-4f27-82e4-dffa89e9f66c)


# Model Loading
The script starts by loading a pre-trained YOLOv8 model using the following code:

![Screenshot 2023-09-20 201925](https://github.com/MaramWael02/Shape-Detection/assets/95209939/e0ab0cb7-c32b-4260-83e5-5b3cdc3600a7)

The 'yolov8n.pt' file contains pre-trained weights for the YOLOv8 model. This pre-trained model serves as the starting point for further training or inference.

# Model Training

The next part of the script is dedicated to training the YOLOv8 model on a custom dataset. The training process is initiated with the following code:

Here is a link to the dataset used in this code : https://universe.roboflow.com/vidhi6khosla-gmail-com/suas-final

![Screenshot 2023-09-20 202218](https://github.com/MaramWael02/Shape-Detection/assets/95209939/20e05779-fb9f-4c3d-81fa-966e657fd9fd)

# Testing Results
![val_batch2_pred](https://github.com/MaramWael02/Shape-Detection/assets/95209939/e9d91788-b543-4bc0-b1b1-7703ad2e5925)
![val_batch2_labels](https://github.com/MaramWael02/Shape-Detection/assets/95209939/f84fe637-41df-4258-8740-d6a06f2a0d41)
![val_batch1_pred](https://github.com/MaramWael02/Shape-Detection/assets/95209939/639e4a94-7855-472a-8aeb-fda9797b5e18)
![val_batch1_labels](https://github.com/MaramWael02/Shape-Detection/assets/95209939/d1c85327-4101-4412-b024-bcaf74115e8a)
![val_batch0_pred](https://github.com/MaramWael02/Shape-Detection/assets/95209939/3eeee82e-be20-4cc6-8145-e21ce9552535)
![val_batch0_labels](https://github.com/MaramWael02/Shape-Detection/assets/95209939/7333bac7-737d-4a5e-9a6c-521332b998dd)


# Model Evaluation 

![results](https://github.com/MaramWael02/Shape-Detection/assets/95209939/a74bf1f5-acf0-4b8b-bb9e-993760b97bb1)
![R_curve](https://github.com/MaramWael02/Shape-Detection/assets/95209939/cdc9d0f1-77fc-4a54-8663-b57cef558f84)
![PR_curve](https://github.com/MaramWael02/Shape-Detection/assets/95209939/d4b7fea7-8bd1-470b-8855-fc8625236d8e)
![P_curve](https://github.com/MaramWael02/Shape-Detection/assets/95209939/75595059-dbf1-47c6-9bbf-07ff28b72b45)
![F1_curve](https://github.com/MaramWael02/Shape-Detection/assets/95209939/df6bf781-a377-4947-8503-32b0a9c4c576)
![confusion_matrix_normalized](https://github.com/MaramWael02/Shape-Detection/assets/95209939/1db23863-ebd7-4499-b18c-c28fe6cfc78f)
![confusion_matrix](https://github.com/MaramWael02/Shape-Detection/assets/95209939/1923ef20-5c90-45f2-9055-f5677cc3e7bd)


# Inference Code 

Following model training, the script proceeds to perform inference on a sample image using the trained YOLOv8 model. The inference code is as follows:

![Screenshot 2023-09-20 202335](https://github.com/MaramWael02/Shape-Detection/assets/95209939/af638fb3-2835-4967-9160-17f12744a6a6)

The inference code performs the following actions:

* image_path = 'shape.jpg': Specifies the path to the input image ('shape.jpg') on which object detection will be performed.
* model.predict(...): Initiates the inference process, where the model processes the input image and detects objects. The detected objects are annotated with bounding boxes, and the annotated image can be saved and displayed.
* The resulting image after feeding it into the model
  
![shape](https://github.com/MaramWael02/Shape-Detection/assets/95209939/9671e1af-337f-4f10-bf56-2048a7e7c47f)


