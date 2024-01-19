import flet

from download_video import get_video_resolutions



def window(page: flet.Page):
    

    def list_available_resolutions(url: str):

        streams_or_exception, streams_resolution = get_video_resolutions(url = url)

        if isinstance(streams_or_exception, Exception):
            submit_url_button.disabled = True
            exception_text_field.value = streams_or_exception
            page.add(exception_text_field)
            
            if available_resolutions_dropdown in page.controls:
                page.remove(available_resolutions_dropdown)
        
        else:
            for stream_resolution in streams_resolution:
                available_resolutions_dropdown.options.append(flet.dropdown.Option(key = stream_resolution))

            page.add(available_resolutions_dropdown)
    

    def reset_submit_url_button(event) -> None:
        submit_url_button.disabled = False

        if exception_text_field in page.controls:
            page.remove(exception_text_field)


    # Window settings
    page.title = "YouTube Downloader"
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER

    # Interface widgets
    url_field: flet.TextField = flet.TextField(
        label = "Video URL",
        autofocus = True,
        on_change = reset_submit_url_button
    )

    submit_url_button : flet.ElevatedButton = flet.ElevatedButton(
        text = 'Submit URL',
        on_click = lambda _: list_available_resolutions(url = url_field.value)
    )
    
    exception_text_field: flet.Text = flet.Text(color = 'red')

    available_resolutions_dropdown = flet.Dropdown()


    page.add(url_field, submit_url_button)