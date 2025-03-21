1  # 📦 FFmpeg Setup for Live Environment (Production)

2  ## ✅ Why FFmpeg is needed
3  FFmpeg is required to compress warehouse video files into smaller sizes for efficient processing and storage.

4  ---

5  ## 🛠 How to Install FFmpeg on Live Server

6  ### Option 1: Ubuntu / Debian (e.g. AWS EC2, VPS)
7  ```bash
8  sudo apt update
9  sudo apt install ffmpeg
10 ```
   
11 ### Option 2: MacOS Server (rare)
12 ```bash
13 brew install ffmpeg
14 ```

15 ### Option 3: Docker (recommended)
16 In your Dockerfile:
17 ```dockerfile
18 RUN apt-get update && apt-get install -y ffmpeg
19 ```

