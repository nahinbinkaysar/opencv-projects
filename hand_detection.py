import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import urllib.request
import os

def download_model():
    """Download the hand landmarker model if not present"""
    model_path = "hand_landmarker.task"
    if not os.path.exists(model_path):
        print("Downloading hand landmarker model...")
        url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
        urllib.request.urlretrieve(url, model_path)
        print("Model downloaded!")
    return model_path

def draw_landmarks_on_image(rgb_image, detection_result):
    """Draw hand landmarks and connections on the image"""
    HAND_CONNECTIONS = [
        (0, 1), (1, 2), (2, 3), (3, 4),      # Thumb
        (0, 5), (5, 6), (6, 7), (7, 8),      # Index
        (0, 9), (9, 10), (10, 11), (11, 12), # Middle
        (0, 13), (13, 14), (14, 15), (15, 16), # Ring
        (0, 17), (17, 18), (18, 19), (19, 20), # Pinky
        (5, 9), (9, 13), (13, 17)            # Palm
    ]
    
    FINGERTIP_IDS = [4, 8, 12, 16, 20]
    
    annotated_image = rgb_image.copy()
    height, width, _ = annotated_image.shape
    
    for hand_landmarks in detection_result.hand_landmarks:
        # Draw connections (skeleton/rig)
        for connection in HAND_CONNECTIONS:
            start = hand_landmarks[connection[0]]
            end = hand_landmarks[connection[1]]
            start_point = (int(start.x * width), int(start.y * height))
            end_point = (int(end.x * width), int(end.y * height))
            cv2.line(annotated_image, start_point, end_point, (0, 255, 0), 2)
        
        # Draw landmarks
        for idx, landmark in enumerate(hand_landmarks):
            cx, cy = int(landmark.x * width), int(landmark.y * height)
            
            if idx in FINGERTIP_IDS:
                cv2.circle(annotated_image, (cx, cy), 10, (0, 255, 255), cv2.FILLED)
            else:
                cv2.circle(annotated_image, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    
    return annotated_image

def main():
    model_path = download_model()
    
    # Create HandLandmarker
    base_options = python.BaseOptions(model_asset_path=model_path)
    options = vision.HandLandmarkerOptions(
        base_options=base_options,
        num_hands=2
    )
    detector = vision.HandLandmarker.create_from_options(options)
    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    print("Hand Detection Started! Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        detection_result = detector.detect(mp_image)
        
        annotated_frame = draw_landmarks_on_image(rgb_frame, detection_result)
        bgr_annotated = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)
        
        cv2.imshow('Hand Detection - Press Q to Quit', bgr_annotated)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()