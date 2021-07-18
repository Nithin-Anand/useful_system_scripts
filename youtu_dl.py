import argparse
import os

        


yt_url = input("Enter URL: ")

yt_command = 'youtube-dl -f 140 ' + yt_url + ' --audio-format mp3 -x'

os.system(yt_command)