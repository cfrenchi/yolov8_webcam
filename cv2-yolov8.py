import cv2
from datetime import datetime
import argparse
import os
from ultralytics import YOLO

# Define directories and check if they exist, create them if they don't
output_dir = "outputs"
models_dir = "models"
for directory in [output_dir, models_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Argument parsing
parser = argparse.ArgumentParser(description='YOLO model type')
parser.add_argument('-model_type', type=str, choices=['', 'seg', 'pose', 'obb', 'cls'], default='',
                    help='The type of YOLO model to use')
args = parser.parse_args()

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
if not cap.isOpened():
    print("Could not open webcam")
    exit()

# Timestamp for output file
now = datetime.now()
timestamp_str = now.strftime("%Y%m%d_%H%M%S")

# VideoWriter setup
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(os.path.join(output_dir, f'{args.model_type}_{timestamp_str}.mp4'), fourcc, 20.0, (640, 480))

# Model setup
model_name = "yolov8n.pt" if args.model_type == '' else f"yolov8n-{args.model_type}.pt"
model_path = os.path.join(models_dir, model_name)
model = YOLO(model_path)

# Window setup
cv2.namedWindow(f'{args.model_type} Estimation', cv2.WINDOW_NORMAL)

try:
    # Main loop for pose overlay on webcam
    while True:
        success, img = cap.read()
        results = model(img, stream=True)

        for r in results:
            im_array = r.plot()
            cv2.imshow(f'{args.model_type} Estimation', im_array)
            out.write(im_array)

        if cv2.waitKey(1) == ord('q'):
            break
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cap.release()
    out.release()  # Save the video file
    cv2.destroyAllWindows()