# useful_system_scripts
System Scripts that I use

**DISCLAIMER:** None of these scripts are robust right now, with no input validation or test cases done yet. Therefore, use at your own risk.

## best_webm.py

A script that prompts the user for the number of videos they want to download, then 
asks for the corresponding number of URLs and downloads those videos in the best 
possible video and audio quality available in 'webm' format. Useful for downloading a series of videos that aren't 
in a playlist without needing to execute the youtube-dl command each time.

## youtu-dl.py

*Will be renamed*

**Requires FFMPEG to be installed**

A script that asks for a YouTube URL and downloads the best quality audio version and transcodes it to MP3. I use it to download audio versions of video podcasts that will work on all my portable audio devices, where other file formats might not always be supported. 
