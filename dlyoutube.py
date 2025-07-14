# pip install yt_dlp ติตตั้ง library yt_dlp ก่อน

import yt_dlp  #เรียกใช้ library สำหรับดาวโหลดวิดีโอ
def download_youtube_video(url, save_path="."): #ฟังก์ชันที่ดาวน์โหลดวิดีโอ 1.ลิงก์วิดีโอที่ต้องการดาวน์โหลด 2.ที่เก็บไฟล์วิดีโอ
    ydl_opts = {
          # กำหนดรูปแบบชื่อไฟล์ที่บันทึก
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
         # เลือกรูปแบบไฟล์วิดีโอที่มีคุณภาพดีที่สุด
        'format': 'best' 
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl: # ใช้งาน yt_dlp โดยกำหนด options จาก ydl_opts
        ydl.download([url])  # ดาวน์โหลดวิดีโอจากลิงก์ URL
video_url = input("Enter the YouTube video URL: ") # รับลิงก์วิดีโอจากผู้ใช้
download_youtube_video(video_url, save_path=".") # เรียกใช้ฟังก์ชันเพื่อดาวน์โหลดวิดีโอและบันทึกไว้ที่โฟลเดอร์