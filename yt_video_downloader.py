import yt_dlp
import tkinter
from tkinter import filedialog
import os
import time

flag = 1

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window
root.tk.call('tk', 'scaling', 2.0)

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a Location')
    return tempdir

def download_video(url, output_dir):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'cookiefile': 'cookies.txt',
        'dump_single_json': True, # to get video details in JSON format
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=False)
            video_title = result['title']
            video_url = result['webpage_url']
            video_duration = result['duration']
            video_views = result['view_count']
            video_likes = result['like_count']
            video_upload_date = result['upload_date']
            print(f'Title: {video_title}\n'
                  f'URL: {video_url}\n'
                  f'Duration: {video_duration}\n'
                  f'Views: {video_views}\n'
                  f'Likes: {video_likes}\n'
                  f'Upload Date: {video_upload_date}')
            ydl.download([url])
    except Exception as e:
        print(f'[ERROR]: {e}')

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(f'[ERROR]: {msg}')

def my_hook(d):
    if d['status'] == 'finished':
        print('Download completed!')
    elif d['status'] == 'downloading':
        print(f'Downloading... {d["_percent_str"]} complete')

if __name__ == '__main__':
    while(flag == 1):
        video_link = str(input("Enter the link of the Video you want to Download: "))
        output_directory = f"{search_for_file_path()}"
        download_video(video_link, output_directory)

        choice = int(input("Do you want to download more Videos(Yes -> [Enter 1], No -> [Enter 0]): "))
        if(choice == 0):
            flag = 0

    print("\nThank you For Using Youtube Downloader\nA Product Developed by Ashwin Narayanan S")
    time.sleep(4)