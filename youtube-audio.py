from pytube import YouTube
import os
import subprocess

print("Welcome "+os.getlogin())
link=input("Enter the video URL: ")
dwl_path="C:/Users/"+os.getlogin()+"/Music/"
yt=YouTube(link)
print("Title: "+yt.title)
print ("Searching for audio streams..")
audio=yt.streams.filter(only_audio=True).all() #filter audio streams only
print ("Downloading audio stream...")
audio[1].download(dwl_path) #download
print ("Coverting ....")
subprocess.call("ffmpeg.exe -loglevel panic -i \""+dwl_path+yt.title+".webm\" -acodec libmp3lame -b:a 320k -vn \""+dwl_path+yt.title+".mp3\"",shell=True) #convert to mp3
print("Removing old file...")
os.remove(dwl_path+yt.title+".webm") # remove old webm file
print("Complete.") #https://youtu.be/69yShAberPE