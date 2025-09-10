# Drone-Detection-fasterrcnn_resnet50_fpn

Drone detection with a simple program obtained by typing the question "python detection box with model resnet50" into the Internet Explorer address bar.

Download the files, unzip the archive containing the test images (Test1), and run the program:

python Drone-Detection-fasterrcnn_resnet50_fpn.py

Changing line 69 of the program can test any folder with images.

If you get "module not found" errors, it would be a good idea to create a new environment,to avoid incompatibilities with programs running in the current environment, and install the following list of modules:

pip install torch

pip install torchvision

pip install packaging

pip install pyparsing

pip install cycler

pip install python-dateutil (the module and package names differ here)

pip Install kiwisolver

pip install importlib_resources

Although as of 09/10/2025 in the list of classes of the COCO dataset, with which most of the models are pre-trained, class 5 appears as "airplane", by running this simple program it can be verified that drones are detected that do not have any appearance of airplanes.

You can make comparisons with other projects; the ones I've found to be the most accurate are:

https://universe.roboflow.com/drone-detection-pexej/drone-detection-data-set-yolov7/dataset/1 (you may need a Roboflow API key, which is free and easily obtained).

https://github.com/ablanco1950/Drone-Detection_Yolov10

https://app.roboflow.com/a-stx8a/drone_detection_rf_detr-9ghzn/models/drone_detection_rf_detr-9ghzn/1

https://github.com/ablanco1950/Drone_Detection_RFDETRBase

It is observed that these projects are complementary, some objects are detected by some, but not by others, so a solution could be a project that uses several modules in cascade as occurs in the project https://github.com/ablanco1950/Drone-Detection_Yolov10

