from ultralytics import YOLO

def run_tracking(video_path, model_path='yolov8n.pt', tracker_config='botsort.yaml'):
    model = YOLO(model_path)
    results = model.track(source=video_path, show=True, tracker=tracker_config)
    print("*********************")
    print("BotSORT || Results type:")
    print("*********************")
    print(type(results)) 
    print(results[0]) 
    return results