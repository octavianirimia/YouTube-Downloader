import flet

from download_video import get_video_resolutions, download_video



def window(page: flet.Page):

    # Useful functions

    def reset_submit_url_button(event) -> None:
        
        submit_url_button.disabled = False
        submit_url_button.update()

        if exception_text_field in page.controls:
            page.remove(exception_text_field)
        
        if available_resolutions_dropdown in page.controls:
            available_resolutions_dropdown.value = None
            available_resolutions_dropdown.options = None
            page.remove(available_resolutions_dropdown)
        
        if select_download_directory_button in page.controls:
            page.remove(select_download_directory_button)
        
        if directory_path_text_field in page.controls:
            page.remove(directory_path_text_field)
        
        if download_button in page.controls:
            page.remove(download_button)


    def list_video_available_resolutions(event) -> None:

        submit_url_progress_ring.opacity = 1
        submit_url_progress_ring.update()
        
        stream_resolutions: list | Exception = get_video_resolutions(url_text_field.value)

        if isinstance(stream_resolutions, Exception):
            submit_url_button.disabled = True
            exception_text_field.value = stream_resolutions
            page.add(exception_text_field)

            if available_resolutions_dropdown in page.controls:
                page.remove(available_resolutions_dropdown)
            
            submit_url_progress_ring.opacity = 0
            submit_url_progress_ring.update()
        
        else:
            submit_url_progress_ring.opacity = 0
            submit_url_progress_ring.update()

            for stream_resolution in stream_resolutions:

                available_resolutions_dropdown.options.append(flet.dropdown.Option(key = stream_resolution))

            page.add(available_resolutions_dropdown)
    

    def add_select_download_directory_button(event) -> None:
        page.add(select_download_directory_button)


    def get_directory_path(event: flet.FilePickerResultEvent):

        if event.path:
            directory_path_text_field.value = event.path
            page.add(directory_path_text_field, download_button)
        
        else:
            directory_path_text_field.value = "Cancelled!"

        directory_path_text_field.update()


    # Window settings
    page.title = "YouTube Downloader"
    page.window_width, page.window_height = 600, 400
    page.window_resizable = False
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER

    # Interface widgets
    url_text_field: flet.TextField = flet.TextField(
        label = "Video URL",
        autofocus = True,
        on_change = reset_submit_url_button
    )

    submit_url_button : flet.ElevatedButton = flet.ElevatedButton(
        text = 'Submit URL',
        on_click = list_video_available_resolutions
    )

    submit_url_progress_ring = flet.ProgressRing(width = 16, height = 16, stroke_width = 2, opacity = 0)

    submit_row: flet.Row = flet.Row([submit_url_button, submit_url_progress_ring], alignment=flet.MainAxisAlignment.CENTER)

    page.add(url_text_field, submit_row)

    exception_text_field: flet.Text = flet.Text(color = 'red')

    available_resolutions_dropdown = flet.Dropdown(on_change = add_select_download_directory_button)

    directory_path_text_field: flet.Text = flet.Text()
    directory_dialog = flet.FilePicker(on_result = get_directory_path)
    page.overlay.extend([directory_dialog])

    select_download_directory_button: flet.ElevatedButton = flet.ElevatedButton(
        text = "Select download directory",
        icon = flet.icons.FOLDER_OPEN,
        on_click = lambda _: directory_dialog.get_directory_path(),
    )

    download_button: flet.ElevatedButton = flet.ElevatedButton(
        text = 'Download',
        on_click = lambda _: download_video(
            url = url_text_field.value,
            resolution = available_resolutions_dropdown.value,
            path = directory_path_text_field.value
        )
    )