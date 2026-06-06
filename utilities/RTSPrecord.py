import cv2
import time
import os
from datetime import datetime

# ==== CONFIGURATION ====
USERNAME = "root"
PASSWORD = "axisroot"
IP = "192.168.0.90"

RTSP_URL = f"rtsp://{USERNAME}:{PASSWORD}@{IP}:554/axis-media/media.amp"

# Unique timestamp for this recording session
session_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Outputs with unique names
RAW_FILE = f"raw_output_{session_time}.avi"
DISPLAY_FILE = f"annotated_output_{session_time}.avi"

# =======================

cap = cv2.VideoCapture(RTSP_URL)

if not cap.isOpened():
    print("Cannot open stream")
    exit()

width = int(cap.get(3))
height = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 25

fourcc = cv2.VideoWriter_fourcc(*'XVID')

raw_out = cv2.VideoWriter(RAW_FILE, fourcc, fps, (width, height))
annotated_out = cv2.VideoWriter(DISPLAY_FILE, fourcc, fps, (width, height))

start_time = time.time()

def get_size_mb(path):
    if os.path.exists(path):
        return os.path.getsize(path) / (1024 * 1024)
    return 0

print("Recording started... Press 'q' to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # ===== RAW VIDEO (no overlay) =====
    raw_out.write(frame)

    # ===== ANNOTATED VIDEO =====
    annotated_frame = frame.copy()

    # Timer
    elapsed = int(time.time() - start_time)
    h = elapsed // 3600
    m = (elapsed % 3600) // 60
    s = elapsed % 60

    rec_text = f"REC {h:02}:{m:02}:{s:02}"

    # Timestamp
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # File size (annotated file)
    size_mb = get_size_mb(DISPLAY_FILE)

    # Draw timestamp
    cv2.putText(annotated_frame, now, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255), 2)

    # Draw recording timer
    cv2.putText(annotated_frame, rec_text, (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 0, 255), 2)

    # Draw file size (top-right)
    size_text = f"{size_mb:.2f} MB"
    text_size = cv2.getTextSize(size_text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
    x_pos = width - text_size[0] - 10

    cv2.putText(annotated_frame, size_text, (x_pos, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 255, 255), 2)

    # Write outputs
    raw_out.write(frame)
    annotated_out.write(annotated_frame)

    # Show live view
    cv2.imshow("Live Annotated Stream", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
raw_out.release()
annotated_out.release()
cv2.destroyAllWindows()

print("Recording stopped.")