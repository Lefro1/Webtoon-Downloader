import os


def main():
    directory = r'E:\Manga\CustomDownloads - Copy'

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.cbz'):
                old_path = os.path.join(root, file)
                new_name = file.split('(')[0].strip() + '.cbz'
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)


if(__name__ == '__main__'):
    main()
