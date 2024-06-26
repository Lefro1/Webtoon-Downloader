import os


def remove_duplicate_files(root_dir):
    counter = 0

    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            counter += 1
            if counter % 100000 == 0:
                print(f"-------------Checking: {root}/{filename}")
            if filename.endswith('.png'):
                basename, ext = os.path.splitext(filename)
                chapter_number, sub_number = basename.split('_')
                if chapter_number.startswith('0'):
                    chapter_number = chapter_number.lstrip('0')
                    if f"{chapter_number}_{sub_number}.png" in files:
                        os.remove(os.path.join(root, filename))
                        print(f"Deleted: {root}/{filename}")


# Replace 'root_directory' with the path to your root directory containing all the folders with images
root_directory = 'E:\Manga\WebtoonDownloader'
remove_duplicate_files(root_directory)
