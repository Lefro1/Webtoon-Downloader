import subprocess

import webtoon_downloader
import os
from subprocess import call
import cmd

series_name_to_url = [
    ('DeathRescheduled', 'https://www.webtoons.com/en/thriller/death-rescheduled/list?title_no=3515', 'E:/Manga/WebtoonDownloader'),
    ("LetsPlay", 'https://www.webtoons.com/en/romance/letsplay/list?title_no=1218', 'E:/Manga/WebtoonDownloader'),
    ('AnomalySoul', 'https://www.webtoons.com/en/challenge/anomaly-soul-season-1/list?title_no=526690', 'E:/Manga/WebtoonDownloader'),
    ('EverythingIsFine', 'https://www.webtoons.com/en/horror/everything-is-fine/list?title_no=2578', 'E:/Manga/WebtoonDownloader'),
    ('DownToEarth', 'https://www.webtoons.com/en/romance/down-to-earth/list?title_no=1817', 'E:/Manga/WebtoonDownloader'),
    ('HandJumper', 'https://www.webtoons.com/en/thriller/hand-jumper/list?title_no=2702', 'E:/Manga/WebtoonDownloader'),
    ('ImmortalWeakling', 'https://www.webtoons.com/en/super-hero/immortal-weakling/list?title_no=2733', 'E:/Manga/WebtoonDownloader'),
    ('MemeGirls', 'https://www.webtoons.com/en/challenge/meme-girls/list?title_no=304446', 'E:/Manga/WebtoonDownloader'),
    ('MaybeMeantToBe', 'https://www.webtoons.com/en/romance/maybe-meant-to-be/list?title_no=4208', 'E:/Manga/WebtoonDownloader'),
    ("ImTheGrimReaper", 'https://www.webtoons.com/en/supernatural/im-the-grim-reaper/list?title_no=1697', 'E:/Manga/WebtoonDownloader'),
    ('NotEvenBones', 'https://www.webtoons.com/en/thriller/not-even-bones/list?title_no=1756', 'E:/Manga/WebtoonDownloader'),
    ('Questism', 'https://www.webtoons.com/en/fantasy/questism/list?title_no=3767', 'E:/Manga/WebtoonDownloader'),
    ('I Was The Final Boss', 'https://www.webtoons.com/en/fantasy/i-was-the-final-boss/list?title_no=5170', 'E:/Manga/WebtoonDownloader'),
    ('Absolute Sword Sense', 'https://www.webtoons.com/en/action/absolute-sword-sense/list?title_no=5100', 'E:/Manga/WebtoonDownloader'),
    ('Bailin and Li Yun', 'https://www.webtoons.com/en/challenge/bailin-and-li-yun/list?title_no=781556', 'E:/Manga/WebtoonDownloader'),
    ('The Last Bloodline', 'https://www.webtoons.com/en/supernatural/the-last-bloodline/list?title_no=2722', 'E:/Manga/WebtoonDownloader'),
    ('Karsearin Adventures of a Red Dragon', 'https://www.webtoons.com/en/fantasy/karsearin-adventures-of-a-red-dragon/list?title_no=4447', 'E:/Manga/WebtoonDownloader'),
    ('Suitor Armor', 'https://www.webtoons.com/en/fantasy/suitor-armor/list?title_no=2159', 'E:/Manga/WebtoonDownloader'),
    ('Mage & Demon Queen', 'https://www.webtoons.com/en/comedy/mage-and-demon-queen/list?title_no=1438', 'E:/Manga/WebtoonDownloader'),
    ('The Ember Knight', 'https://www.webtoons.com/en/fantasy/the-ember-knight/list?title_no=2886', 'E:/Manga/WebtoonDownloader'),
    # ('Taming the Marquess', 'https://www.webtoons.com/en/romance/taming-the-marquess/list?title_no=4345') Does not work as it is pass-based
]

# Allows for downloading multiple entries in series as opposed to the standard CLI approach
def main():
    for(title, url, path) in series_name_to_url:
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
