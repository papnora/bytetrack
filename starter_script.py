from bytetrack_ultralytics import run_tracking
#from botSORT_ultralytics import run_tracking
import cv2

def save_tracked_video(results, input_video_path, output_video_path):
    cap = cv2.VideoCapture(input_video_path)
    ret, frame = cap.read()
    frame_id = 0 
    #fps = cap.get(cv2.CAP_PROP_FPS)     
    width = frame.shape[1]
    height = frame.shape[0]
    print(frame.shape)
    out = cv2.VideoWriter(str(output_video_path), cv2.VideoWriter_fourcc(*'DIVX'), 20.0, (width, height))

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
output_video_path = 'tracked_park_people.avi'

results = run_tracking(video_path)
save_tracked_video(results, video_path, output_video_path)
