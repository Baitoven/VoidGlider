import vlc
import yt_dlp

url = 'https://www.youtube.com/watch?v=hgfJoV5Lmbw'
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': './Audio/1.%(ext)s', #%(title)s
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

vlc.MediaPlayer('./Audio/1.mp3')