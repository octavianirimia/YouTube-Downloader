import flet

from download_video import get_video_resolutions, download_video



class Resolutions:
    def __init__(self):
        self.result: list | Exception = None



def list_available_resolutions(
        page: flet.Page, url: str, stream_resolutions: Resolutions, submit_url_button: flet.ElevatedButton, exception_text_field: flet.Text,
        available_resolutions_dropdown: flet.Dropdown, download_button: flet.ElevatedButton) -> None:

    stream_resolutions.result = get_video_resolutions(url = url)

    if isinstance(stream_resolutions.result, Exception):
        submit_url_button.disabled = True
        exception_text_field.value = stream_resolutions.result
        page.add(exception_text_field)

        if available_resolutions_dropdown in page.controls:
            page.remove(available_resolutions_dropdown)
    
    else:
        for stream_resolution in stream_resolutions.result:
            available_resolutions_dropdown.options.append(flet.dropdown.Option(key = stream_resolution))

        page.add(available_resolutions_dropdown)#, download_button)



def reset_submit_url_button(page: flet.Page, submit_url_button: flet.ElevatedButton, exception_text_field: flet.Text) -> None:

    submit_url_button.disabled = False

    if exception_text_field in page.controls:
        page.remove(exception_text_field)



def download(page: flet.Page, download_button: flet.ElevatedButton) -> None:
    page.add(download_button)
    


def window(page: flet.Page):

    stream_resolutions: Resolutions = Resolutions()

    # Window settings
    page.title = "YouTube Downloader"
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER

    # Interface widgets
    url_field: flet.TextField = flet.TextField(
        label = "Video URL",
        autofocus = True,
        on_change = lambda _:reset_submit_url_button(page = page, submit_url_button = submit_url_button,exception_text_field = exception_text_field)
    )

    submit_url_button : flet.ElevatedButton = flet.ElevatedButton(
        text = 'Submit URL',
        on_click = lambda _: list_available_resolutions(
            url = url_field.value, stream_resolutions = stream_resolutions, page = page, submit_url_button = submit_url_button,
            exception_text_field = exception_text_field, available_resolutions_dropdown = available_resolutions_dropdown,
            download_button = download_button
        )
    )

    exception_text_field: flet.Text = flet.Text(color = 'red')

    available_resolutions_dropdown = flet.Dropdown(on_change = lambda _: download(page, download_button))

    download_button: flet.ElevatedButton = flet.ElevatedButton(
        text = 'Download',
        on_click = lambda _: download_video(url = url_field.value, resolution = available_resolutions_dropdown.value)
    )


    page.add(url_field, submit_url_button)