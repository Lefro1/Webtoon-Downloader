import subprocess

import webtoon_downloader
import os
from subprocess import call
import cmd

"""
This function reads data from subscriptions.txt and generates a list of tuples containing series names, URLs, and a common file path.

Returns:
    list: A list of tuples, where each tuple contains (series_name, url, file_path).
"""
def get_subscription_map():
    subscriptions_file = "helpers/subscriptions.txt"
    file_path = 'E:/Manga/WebtoonDownloader'

    # Initialize an empty list to store the generated series_name_to_url list
    series_name_to_url = []

    # Read the data from subscriptions.txt and generate the list
    with open(subscriptions_file, 'r') as file:
        for line in file:
            series_name, url = line.strip().split('|')
            series_name_to_url.append((series_name.strip(), url.strip(), file_path))

    return series_name_to_url



# Allows for downloading multiple entries in series as opposed to the standard CLI approach
def main():
    for(title, url, path) in get_subscription_map():
        print(title, url, path)

        fullPath = f"E:/Manga/WebtoonDownloader/{title}"
        if not os.path.exists(fullPath):
            os.makedirs(fullPath)

        finalChapter = 0
        for dirName in os.listdir(fullPath):
            currChapter = dirName.split("Chapter ",1)[1].split()[0]
            finalChapter = max(finalChapter, int(currChapter))

        command_args = f' {url} --images-format png --separate --dest "{fullPath}" --start {finalChapter}'

        script_call_start = "python webtoon_downloader.py"
        script_call = script_call_start + command_args

        print(script_call)
        subprocess.call(script_call, shell=True)

if(__name__ == '__main__'):
    main()
