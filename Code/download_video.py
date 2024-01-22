import pytube
import requests
import ssl



# Get all resolutions of the video
def get_video_resolutions(url: str):

    ssl._create_default_https_context = ssl._create_stdlib_context

    try:
        video = pytube.YouTube(url = url)

        stream_resolutions = []

        for stream in video.streams.order_by(attribute_name = 'resolution'):
            stream_resolutions.append(stream.resolution)
        
        stream_resolutions = list(dict.fromkeys(stream_resolutions))

        return stream_resolutions

    except Exception as exception:
        return exception



def download_video(url: str, resolution: str) -> None:

    ssl._create_default_https_context = ssl._create_stdlib_context

    try:
        pytube.YouTube = pytube.YouTube(url = url).streams.filter(resolution = resolution).first().download()
    
    except Exception:
        pass
    #