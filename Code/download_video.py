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

        video_resolutions = []
        videos = []

        for stream in video.streams.filter(progressive = True, file_extension = 'mp4').order_by(attribute_name = 'resolution'):
            video_resolutions.append(stream.resolution)
            videos.append(stream)
        
        video_resolutions = list(dict.fromkeys(video_resolutions))

        return videos, video_resolutions

    except Exception as exception:
        return exception, None



def download_video(url: str, resolution: str) -> None:

    ssl._create_default_https_context = ssl._create_stdlib_context

    try:
        video: pytube.YouTube = pytube.YouTube(url = url).streams.filter(resolution = resolution, progressive = True)

        print('Video was downloaded!')
    
    except Exception:
        print(Exception)