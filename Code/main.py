import flet

from download_video import download_video
from gui import window

# url test: https://www.youtube.com/watch?v=_TtFTSv42bY


def main():
    
    #flet.app(target = window)

    # Get url

    url: str = input('Please enter the video url: ')

    download_video(url = url)



if __name__ == '__main__':
    main()