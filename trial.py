from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def download_youtube_video(url,path):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        print('Downloading the video now...')
        video_stream.download(output_path=path)
        print('Sucess')
    except Exception as e:
        print(f'an error occured: {e}')

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=NI9LXzo0UY0"
    save_path = "./"
    download_youtube_video(video_url, save_path)