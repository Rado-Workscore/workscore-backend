import subprocess
import os

def compress_video(input_path, output_path, crf=28):
    """
    Կոմպրեսավորում է վիդեոն՝ օգտագործելով FFmpeg։
    input_path – սկզբնական վիդեոյի ուղին
    output_path – կոմպրեսված վիդեոյի ուղին
    crf – որակի կարգավորիչ (ավելի բարձր = ավելի փոքր ֆայլ, ավելի ցածր որակ)
    """
    command = [
        "ffmpeg",
        "-i", input_path,
        "-vcodec", "libx264",
        "-crf", str(crf),
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        print(f"✅ Կոմպրեսիան ավարտվեց: Պահպանվեց {output_path}")
    except subprocess.CalledProcessError as e:
        print("❌ Կոմպրեսիայի սխալ:", e)


# Օրինակ օգտագործում (փոխիր այս ուղիները ըստ քեզ մոտ եղած տեսանյութերի)
if __name__ == "__main__":
    input_video = "step1_ingestion/videos/warehouse_1.mp4"
    output_video = "step1_ingestion/videos/warehouse_1_compressed.mp4"
    compress_video(input_video, output_video)
