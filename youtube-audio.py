from pytube import YouTube
from pytube.helpers import safe_filename
import os
import getpass
import subprocess
import colorama
from colorama import Fore, Back, Style
colorama.init()
if not os.path.exists('Music'):
    os.makedirs('Music')
print(Fore.YELLOW+"Welcome "+getpass.getuser()+" to YouMP3"+ Style.RESET_ALL)
link=input("Enter the video URL: ")
dwl_path="Music/"
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
	subprocess.call("ffmpeg -loglevel panic -i \""+dwl_path+fname+".webm\" -acodec libmp3lame -b:a 320k -vn \""+dwl_path+fname+".mp3\"",shell=True) #convert to mp3
except:
	print ("Error Converting file!. Make sure ffmpeg is installed.")
print("Removing old file...")
try:
	os.remove(dwl_path+fname+".webm") # remove old webm file
except:
	print ("Error accessing directory")
print ("File(s) stored at : ",dwl_path)
print("Complete !") # test url: https://youtu.be/69yShAberPE
