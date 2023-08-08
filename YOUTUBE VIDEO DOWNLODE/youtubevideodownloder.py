from pytube import YouTube

def download_video(url, save_path='./'):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()

        print(f"Downloading: {yt.title}")
        video.download(output_path=save_path)
        print("Download completed!")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)