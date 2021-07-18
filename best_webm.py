import os
from termcolor import cprint


def get_urls():
    # Takes in x number of YouTube URLs, wtih x input by the user
    in_url_list = []


    num_urls = int(input('Enter the number of videos you want to download: '))
    cprint('Now the system will prompt you to enter each URL in turn', 'magenta')
    for i in range(num_urls):
        input_msg = 'Enter YouTube URL ' + str(i + 1) + ': '
        in_url_list.append(input(input_msg))

    return in_url_list

def download_best_webms(url_list):
    # Takes a URL list and downloads the best quality webm for each URL
    for i in range(len(url_list)):
        vid_msg = 'Downloading video ' + str(i + 1)
        cprint(vid_msg, 'blue')
        cmd = 'youtube-dl -f bestvideo[ext=webm]+bestaudio[ext=webm] ' + url_list[i]
        os.system(cmd)

    cprint('All videos downloaded!', 'green')


if __name__ == '__main__':
    # Combines the two previous functions to download the videos
    urls = get_urls()
    download_best_webms(url_list=urls)