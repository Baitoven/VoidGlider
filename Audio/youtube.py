import logging
import vlc
import yt_dlp
import os
import asyncio

mediaPlayer = vlc.MediaPlayer()

def parse_url(url):
    return url.split('=')[1]

async def load_from_url(url):
    isDownloadedEvent = asyncio.Event()

    def progress_hook(event):
        filename = os.path.basename(event['filename'])
        if event['status'] == 'error':
            logging.error(f'[youtube-dl] error occured downloading: {filename}')
        elif event['status'] == 'finished':
            total_size_str = event.get('_total_bytes_str', '?').strip()
            elapsed_str = event.get('_elapsed_str', '?').strip()
            logging.info(f'[youtube-dl] finished downloading: {filename} - '
                     f'{total_size_str} in {elapsed_str}')
            isDownloadedEvent.set()
        #else:
            #logging.warning(f'[youtube-dl] unknown event: {str(event)}')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': './Audio/AudioCache/' + parse_url(url), #%(title)s.%(ext)s
        'quiet': True,
        'progress_hooks': [progress_hook],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    await isDownloadedEvent.wait()
