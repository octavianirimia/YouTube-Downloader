import pytube
import ssl



def download_video(url: str) -> None:

    ssl._create_default_https_context = ssl._create_stdlib_context

    try:
        video: pytube.YouTube = pytube.YouTube(url = url)

        video.streams.get_highest_resolution().download()

        print('Video was downloaded!')
    
    except Exception:
        print(Exception)