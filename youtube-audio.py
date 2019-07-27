from pytube import YouTube
from pytube.helpers import safe_filename
import os
import subprocess
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.YELLOW+"Welcome "+os.getlogin()+" to YouMP3"+ Style.RESET_ALL)
link=input("Enter the video URL: ")
dwl_path="C:/Users/"+os.getlogin()+"/Music/"
try:
	yt=YouTube(link)
except:
	print (Fore.RED+"Connection Error!")
print(Fore.BLUE+"Title: "+yt.title+Style.RESET_ALL)
print ("Searching for audio streams..")
audio=yt.streams.filter(only_audio=True).all() #filter audio streams only
print ("Downloading audio stream...")
try:
	audio[1].download(dwl_path) #download
except:
	print (Fore.RED+"Error!")
fname=(safe_filename(yt.title)) #downloaded file name
print ("Coverting ....")
try:
	subprocess.call("ffmpeg.exe -loglevel panic -i \""+dwl_path+fname+".webm\" -acodec libmp3lame -b:a 320k -vn \""+dwl_path+fname+".mp3\"",shell=True) #convert to mp3
except:
	print ("Error Converting file!. Make sure ffmpeg is installed.")
print("Removing old file...")
try:
	os.remove(dwl_path+fname+".webm") # remove old webm file
except:
	print ("Error accessing directory")
print("Complete !") # test url: https://youtu.be/69yShAberPE
print ("File(s) stored at : ",dwl_path)