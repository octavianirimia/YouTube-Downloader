# YouTube-Downloader

## About the project

This application can help you download a video from YouTube at the desired quality.

It is an application written in Python with the help of pytube and flet packages.


### Built with

- Python
- Pytube
- Flet

## Getting started

If you want to work on this project locally on your computer you should follow the instructions below.


### Windows

#### Prerequisites

* A code editor (I used Visual Studio Code installed from Microsoft Store)
* Python installed (I used Python 3.12.1 installed from Microsoft Store)
* Git (Download it from the official website)

1. Open Git Bash go to the desired location and clone the repo

   ```sh
   git clone https://github.com/octavianirimia/YouTube-Downloader.git
   ```

2. Open your code editor and navigate to your cloned folder (In visual studio code go to File and click Open folder)

3. Create a Python virtual environment from the code editor terminal

   ```sh
   python -m venv .YouTube_Downloader
   ```

4. Activate Python virtual environment from the code editor terminal

   ```sh
   .YouTube_Downloader\Scripts\activate
   ```

5. Install the necessary packages

   ```sh
   pip install flet pytube
   ```

Now you can run the program from the main.py file


### Mac

#### Prerequisites

* A code editor (I used Visual Studio Code installed from the official website)
* Python installed (I used Python 3.12.1 installed from the official website. Macs already have Python installed but it's an older version)

1. Open your terminal and install command line tools

   ```sh
   xcode-select --install
   ```

2. Open your code editor and navigate to your cloned folder (In visual studio code go to File and click Open folder)

3. Create a Python virtual environment from the code editor terminal

   If you want to use the python version you have installed type "python3.xy -m venv .YouTube_Downloader". If you only type only "python3 -m venv .YouTube_Downloader" you are using the default installation of Python.

   ```sh
   python3.12 -m venv .YouTube_Downloader
   ```

5. Activate Python virtual environment from the code editor terminal

   ```sh
   source ".YouTube_Downloader/bin/activate"
   ```

6. Install the necessary packages from the code editor terminal

   ```sh
   pip install flet pytube
   ```

Now you can run the program from the main.py file
