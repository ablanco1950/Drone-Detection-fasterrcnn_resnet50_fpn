#preguntando a la IA de Bing
#python detection box with model resnet50
# with slight modifications by Alfonso Blanco

THRESHOLD=0.5
CLASS=5
LABEL_CLASS="Drone"

import re
import os
import cv2

def loadimages(dirname):
 
     imgpath = dirname + "\\"
      
     
     imagesPath = []
     TabFileName=[]
   
    
     print("Reading images from ",imgpath)
     NumImage=-2
     
     Cont=0
     for root, dirnames, filenames in os.walk(imgpath):
        
         NumImage=NumImage+1
         
         for filename in filenames:
             
             if re.search("\.(jpg|jpeg|png|bmp|tiff|JPEG)$", filename):
                 
                 
                 filepath = os.path.join(root, filename)
                
                 
                 #image = cv2.imread(filepath)
                 #image = cv2.resize(image, (640,640), interpolation = cv2.INTER_AREA) # adapting any size image
                 #print(filepath)
                 #print(image.shape)
                 #image=image/255.0
                 imagesPath.append(filepath)
                 TabFileName.append(filename)
                 
                 Cont+=1
                 #if Cont > 1:break
     print("Readed " + str(len(imagesPath)))
     #cv2.imshow('True', images[0])
     #cv2.waitKey(0)
   
     return imagesPath, TabFileName


import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.transforms import functional as F
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load the pre-trained Faster R-CNN model
model = fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()  # Set the model to evaluation mode


# Test the function on a test image
dirnameImages="test\\images"
dirnameImages="Test1"
TabImagesPath, TabfileName = loadimages(dirnameImages)
for i in range(len(TabImagesPath)):
    
    image = Image.open(TabImagesPath[i]).convert("RGB")


    # Transform the image
    image_tensor = F.to_tensor(image).unsqueeze(0)  # Add batch dimension

    # Perform detection
    with torch.no_grad():
        predictions = model(image_tensor)

    # Extract boxes, labels, and scores
    boxes = predictions[0]['boxes']
    labels = predictions[0]['labels']
    scores = predictions[0]['scores']

    # Visualize the results
    fig, ax = plt.subplots(1, figsize=(12, 9))
    ax.imshow(image)

    ContDrone=0

    # Draw detection boxes
    for box, label, score in zip(boxes, labels, scores):
        #if label !=5 : continue 
        if score > THRESHOLD and (label==CLASS):  # Confidence threshold and label selected
            label=LABEL_CLASS
            ContDrone=ContDrone+1
            x_min, y_min, x_max, y_max = box
            rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                                      linewidth=2, edgecolor='red', facecolor='none')
            ax.add_patch(rect)
            ax.text(x_min, y_min, f"{label}, Score: {score:.2f}",
                    color='white', fontsize=10, bbox=dict(facecolor='red', alpha=0.5))
    print(" Drones detected = " + str(ContDrone))
    plt.axis('off')
    plt.show()
