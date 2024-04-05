from bytetrack_ultralytics import run_tracking
#from botSORT_ultralytics import run_tracking
import cv2

def save_tracked_video(results, input_video_path, output_video_path):
    cap = cv2.VideoCapture(input_video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

  #if result is a list and contains elements
    if isinstance(results, list) and len(results) > 0:
        for result in results:
            frame = result.imgs[0] if hasattr(result, 'imgs') else None 
            
            if frame is not None:
                out.write(frame)
                
    else:
        print("A 'results' object is not a list or empty.")

    cap.release()
    out.release()

video_path = 'park_people.mp4'
output_video_path = 'tracked_park_people.mp4'

results = run_tracking(video_path)
save_tracked_video(results, video_path, output_video_path)
