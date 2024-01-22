import pytube
import requests
import ssl



# Check if url is accesible
def check_url(url: str) -> None:
    
    request: requests.Response = requests.get(url = url)
    print(request.status_code)
    return request.status_code == 200



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
        print(resolution)
        pytube.YouTube = pytube.YouTube(url = url).streams.filter(resolution = resolution).first().download()

        print('Video was downloaded!')
    
    except Exception as exception:
        print(exception)