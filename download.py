import yt_dlp

url = "https://chzzk.naver.com/live/59f26a2bf81ef15e21ae6c78526bb608"

ydl_opts = {
    "outtmpl": "%(title)s.%(ext)s",  # 파일명을 방송 제목으로 설정
    "format": "best",  # 가장 높은 화질로 다운로드
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
