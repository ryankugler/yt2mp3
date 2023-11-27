import os
import shutil
import time

source_folder = '.'
destination_folder = './mp3s'

print(".\n.\n.")
url = input("Paste the URL to the Youtube video: ")

def download_mp3(youtube_url, output_folder='.'):
    # Construct the yt-dlp command with the filename
    command = f'yt-dlp --ffmpeg-location /opt/homebrew/bin/ffmpeg --extract-audio --audio-format mp3 -o "{output_folder}/%(title)s.%(ext)s" {youtube_url}'
    os.system(command)

def move_mp3_files(source_folder, destination_folder):
    # Check if destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List all files in the source folder
    for file in os.listdir(source_folder):
        if file.endswith(".mp3"):
            source_file = os.path.join(source_folder, file)
            destination_file = os.path.join(destination_folder, file)

            # Move each MP3 file to the destination folder
            shutil.move(source_file, destination_file)
            print(f"Moved: {file}")

print("\t======== MP3 Downloading ======== ")
download_mp3(url)
time.sleep(5)
print("\t======== Moving MP3 ======== ")
move_mp3_files(source_folder,destination_folder)
