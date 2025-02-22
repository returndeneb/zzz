import cv2

def extract_final_drawing(video_path):
    cap = cv2.VideoCapture(video_path)
    prev_frame = None
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) > 0:
            prev_frame = frame
        else:
            if prev_frame is not None:
                cv2.imwrite("final_drawing.png", prev_frame)
                break
    cap.release()

if __name__ == "__main__":
    video_path = "input_video.mp4"
    extract_final_drawing(video_path)
