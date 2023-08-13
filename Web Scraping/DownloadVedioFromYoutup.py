#Download Video from youtup

import requests

def download_video(url, file_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=200000):
                file.write(chunk)
        print("Video downloaded successfully.")
    else:
        print("An error occurred while downloading the video.")

# Use the URL of the video you want to download
video_url = "https://d3c33hcgiwev3.cloudfront.net/eRb40RXFEemYdRIT0BhLtg.processed/full/540p/index.webm?Expires=1692057600&Signature=OxF7zMSIrRIkKLLtaKGGy4aMqZZDHFVfRG4~A4BeyLiRIbPtBLvys03RP7GB5qkSuoqB5WRO9iLGG6H2xIhmfx9n~FVXzJ1LW1ycsqHjxV3pSbxf~yf0iI9tbZhfNO3gwQjHO~WxVuM5jKAQ0~dpuQiRQZYvuUNqnnDXGLvH-lo_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
# Specify the file path where the video will be saved
save_path = "video88.mp4"

# Execute the function to download the video
download_video(video_url, save_path)
#------------------------------------------------------------------------






# from logging import root
# import os
# #from os import link
# from tkinter import Label, messagebox
# from pytube import YouTube

# def download_yt_video(inp_command):
#     ytURL = str(input("Enter the URL of the YouTube video: "))
#     yt = YouTube(ytURL)
#     try:
#         print("Downloading...")
#         yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution")[-1].download()
#     except:
#         return "ERROR | Please try again later"
    
#     return f"Download Complete | Saved at {os.getcwd()}"

# download_yt_video("https://www.youtube.com/watch?v=tsYm7GBIU7Y&t=92s")
# # def download_youtube_clip(url, download_folder):
# #     return YouTube(url).streams.first().download(output_path=download_folder)





# # link=str(input("Enter the Url :"))
# # video=YouTube(link)
# # stream=video.streams.get_highest_resolution()
# # stream.download()
# # print("Download Sucsses !!")

# # def download(url_box):
# #     url = YouTube(str(url_box))
# #     video = url.streams.first()
# #     video.download()    
# #     messagebox.showinfo('', 'Download completed!')

# # def Download(links):
# #     Label(root, text='Downloading', font='arial 13').place(x=180, y=210)
    
# #     url = YouTube(str(links))

# #     video = url.streams.get_highest_resolution()

# #     video.download()

# #     Label(root, text='Downloaded', font='arial 15').place(x=180, y=210)
    

# # download_folder  ="C:\Users\Dell\Videos"
# # new_var = "https://www.youtube.com/28fd9ae0-a197-4b0d-90b7-e474779e2584"
# # download_yt_video(new_var)
# # download("https://www.youtube.com/28fd9ae0-a197-4b0d-90b7-e474779e2584")

# # download_youtube_clip(url="https://www.youtube.com/28fd9ae0-a197-4b0d-90b7-e474779e2584",download_folder="Users/")