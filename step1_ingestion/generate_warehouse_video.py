import cv2
import os

input_path = "step1_ingestion/videos/new_video.MOV"
output_path = "step1_ingestion/videos/warehouse_1.mp4"

# Ստուգում ենք՝ մուտքային ֆայլը գոյություն ունի՞
if not os.path.exists(input_path):
    print(f"❌ Ֆայլը չի գտնվել՝ {input_path}")
    exit()

# Բացում ենք վիդեոն
cap = cv2.VideoCapture(input_path)

# Ստուգում ենք՝ արդյոք վիդեոն բացվեց
if not cap.isOpened():
    print("❌ Չհաջողվեց բացել մուտքային վիդեոն")
    exit()

# Ստանում ենք վիդեոյի չափերը
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Պատրաստում ենք գրանցող օբյեկտ
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    frame_count += 1

cap.release()
out.release()

print(f"✅ Վիդեոն հաջողությամբ պահպանվեց որպես {output_path} ({frame_count} կադր)")
