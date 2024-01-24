import pytube
import ssl



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



def download_video(url: str, resolution: str, path: str):

    ssl._create_default_https_context = ssl._create_stdlib_context

    try:
        pytube.YouTube = pytube.YouTube(url = url).streams.filter(resolution = resolution).first().download(output_path = path)
    
    except Exception as exception:
        return exception
