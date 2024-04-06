from collections import defaultdict
import cv2
import numpy as np
from pathlib import Path
from ultralytics import YOLO

video_path = 'park_people.mp4'
output_video_path = Path('/notebooks/Tracking_PN/videos/bytetrack_out.avi')



def run_and_save_tracking(video_path, output_video_path, model_path='yolov8n.pt', tracker_config='bytetrack.yaml'):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)
    
    track_history = defaultdict(lambda: [])
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(str(output_video_path), cv2.VideoWriter_fourcc(*'DIVX'), 20.0, (width, height))
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        results = model.track(frame, show=False, tracker=tracker_config)
        
       # boxes = results[0].boxes.xywh.cpu()
       # track_ids = results[0].boxes.id.int().cpu().tolist()
        # annotációk: bounding boxok, azonosítók (ID-k), osztálynevek
        annotated_frame = results[0].plot()
        out.write(annotated_frame)
        
    
    cap.release()
    out.release()
   # cv2.destroyAllWindows()


run_and_save_tracking(video_path, output_video_path) 