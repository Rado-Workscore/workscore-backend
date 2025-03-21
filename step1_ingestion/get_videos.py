import json  # Config ֆայլը կարդալու համար
import os    # Ֆայլերի կառավարում
import time  # Պահանջվող դադարներ տալու համար
import cv2   # OpenCV-ն պետք է տեսախցիկի հոսքը ստանալու համար
from pathlib import Path  # Ֆայլերի ուղիներ կառավարելու համար

# Բացում ենք config.json-ը, որ ստանանք պահեստի տվյալները
with open(os.path.join(os.path.dirname(__file__), "config.json"), "r") as file:

    config = json.load(file)

# Ստանում ենք պահեստների ցանկը
warehouses = config["warehouses"]

# Ստուգում ենք պահեստների կարգավորումները
for warehouse in warehouses:
    warehouse_id = warehouse["id"]  # Պահեստի ID
    method = warehouse["method"]  # RTSP կամ FTP
    
    if method == "RTSP":
        print(f"📡 Պահեստ {warehouse_id}: RTSP live stream")

        # Սահմանում ենք տեսախցիկի RTSP հոսքի URL-ը
        rtsp_url = "videos/new_video.MOV"


        # Բացում ենք հոսքը
        cap = cv2.VideoCapture(rtsp_url)

        # Ստուգում ենք՝ արդյոք հոսքը ճիշտ բացվեց
        if not cap.isOpened():
            print(f"❌ Չհաջողվեց բացել RTSP հոսքը պահեստ {warehouse_id}-ի համար")
        else:
            print(f"✅ RTSP հոսքը հաջող բացվեց պահեստ {warehouse_id}-ի համար")

            # Ստեղծում ենք տեսանյութի ֆայլ՝ պահելու համար
            video_path = f"videos/warehouse_{warehouse_id}.mp4"
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))

            # Սկսում ենք տեսախցիկից ստանալ ֆրեյմեր (կադրեր)
            frame_count = 0
            while frame_count < 300:  # 300 կադր (~15 վայրկյան)
                ret, frame = cap.read()
                if not ret:
                    print(f"⚠️ Կադրը չի ստացվում պահեստ {warehouse_id}-ի համար")
                    break
                else:
                    print(f"✅ Ստացվեց կադր պահեստ {warehouse_id}-ից")
    


                # Գրանցում ենք կադրը ֆայլում
                out.write(frame)
                frame_count += 1

                cv2.imshow("Frame", frame)  # ✅ Ցույց ենք տալիս վիդեոն
                cv2.waitKey(1)  # ✅ Պատուհանը թարմացվում է ամեն կադրից հետո


            # Աշխատանքը ավարտվել է, փակում ենք ֆայլերը
            cap.release()
            out.release()
            print(f"🎥 Տեսանյութը պահպանվեց՝ {video_path}")

    elif method == "FTP":
        print(f"📂 Պահեստ {warehouse_id}: FTP/SFTP ֆայլեր")
        from ftplib import FTP

        ftp_server = warehouse["ftp_server"]
        ftp_user = warehouse["ftp_user"]
        ftp_password = warehouse["ftp_password"]
        video_path = warehouse["video_path"]  # Ֆայլի ուղին սերվերում

        try:
           ftp = FTP(ftp_server)
           ftp.login(user=ftp_user, passwd=ftp_password)
           print(f"✅ Մուտք գործեցինք FTP սերվեր՝ {ftp_server}")

           # Ստեղծում ենք տեղային ֆայլ, ուր կպահենք ներբեռնված վիդեոն
           local_filename = f"step1_ingestion/videos/warehouse_{warehouse_id}_ftp_video.mp4"
           with open(local_filename, "wb") as f:
               ftp.retrbinary(f"RETR {video_path}", f.write)
           print(f"📥 Վիդեոն ներբեռնվեց և պահպանվեց՝ {local_filename}")

           ftp.quit()

        except Exception as e:
            print(f"❌ Սխալ FTP-ից ներբեռնելիս պահեստ {warehouse_id}-ի համար:", e)

        # Այստեղ կգրենք ֆայլերի ներբեռնելու կոդը
        
    else:
        print(f"⚠️ Պահեստ {warehouse_id}: Անհայտ մեթոդ '{method}' ❌")
