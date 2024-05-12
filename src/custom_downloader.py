import subprocess

import webtoon_downloader
import os
from subprocess import call
import cmd

"""
This function reads data from all_downloads.txt and generates a list of tuples containing series names, URLs, and a common file path.

Returns:
    list: A list of tuples, where each tuple contains (series_name, url, file_path).
"""
def get_subscription_map():
    subscriptions_file = "helpers/all_downloads.txt"
    file_path = 'E:/Manga/WebtoonDownloader'

    # Initialize an empty list to store the generated series_name_to_url list
    series_name_to_url = []

    # Read the data from all_downloads.txt and generate the list
    with open(subscriptions_file, 'r') as file:
        for line in file:
            series_name, url = line.strip().split('|')
            series_name_to_url.append((series_name.strip(), url.strip(), file_path))

    return series_name_to_url

def series_name_exists_in_daily_pass(series_name, daily_pass_file):
    # Read the data from skip.txt
    with open(daily_pass_file, 'r') as file:
        for line in file:
            if series_name.lower() == line.strip().lower():
                return True
    return False


def find_starting_chapter(fullPath):
    chapter_numbers = []

    for dirName in os.listdir(fullPath):
        try:
            chapter_num = int(dirName.split("Chapter ", 1)[1].split()[0])
            chapter_numbers.append(chapter_num)
        except (IndexError, ValueError):
            # Skip if chapter number extraction fails
            pass

    chapter_numbers.sort()

    missing_chapter = None
    for i in range(len(chapter_numbers) - 1):
        if chapter_numbers[i + 1] - chapter_numbers[i] != 1:
            missing_chapter = chapter_numbers[i] + 1
            break

    if missing_chapter is None:
        return chapter_numbers[-1] if chapter_numbers else 0
    else:
        return missing_chapter

# Allows for downloading multiple entries in series as opposed to the standard CLI approach
def main():
    for(title, url, path) in get_subscription_map():
        if series_name_exists_in_daily_pass(title, 'helpers/skip.txt'):
            continue

        print(title, url, path)
        full_path = f"E:/Manga/WebtoonDownloader/{title}"
        if not os.path.exists(full_path):
            os.makedirs(full_path)

        download_starting_chapter = find_starting_chapter(full_path)

        command_args = f' {url} --images-format png --separate --dest "{full_path}" --start {download_starting_chapter}'

        script_call_start = "python webtoon_downloader.py"
        script_call = script_call_start + command_args

        print(script_call)
        subprocess.call(script_call, shell=True)

if(__name__ == '__main__'):
    main()
