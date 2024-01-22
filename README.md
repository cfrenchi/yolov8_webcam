# yolov8_webcam
Repo to showcase using yolov8 with your webcam in python

## cv2-yolov8.py

This Python script uses OpenCV and YOLO (You Only Look Once) for real-time object detection. The script captures video from the webcam, applies the YOLO model for object detection, and saves the output video with detected objects.

## Dependencies

- OpenCV
- Ultralytics YOLO
```
pip install opencv-python ultralytics
```

## Directory Structure

The script uses two directories:

- `outputs`: This directory is used to store the output videos. If the directory does not exist, the script will create it.
- `models`: This directory is used to store the YOLO models. If the directory does not exist, the script will create it.

## Usage

You can specify the type of YOLO model to use with the `-model_type` argument. The options are:

- `seg`: for segmentation models
- `pose`: for pose estimation models
- `obb`: for oriented bounding box models
- `cls`: for classification models

If no model type is specified, the script will use the default YOLO model.

## Example

`python cv2-yolov8.py -model_type seg`

## Models

Models will automatically be downloaded if you do not have the specific model installed locally

## Output

The script saves the output video in the `outputs` directory. The filename is in the format `{model_type}_{timestamp}.mp4`, where:

- `model_type` is the type of YOLO model used
- `timestamp` is the current date and time in the format `YYYYMMDD_HHMMSS`