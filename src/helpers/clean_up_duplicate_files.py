import os


def remove_duplicate_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith('.png'):
                basename, ext = os.path.splitext(filename)
                chapter_number, sub_number = basename.split('_')
                if chapter_number.startswith('0'):
                    chapter_number = chapter_number.lstrip('0')
                    if f"{chapter_number}_{sub_number}.png" in files:
                        os.remove(os.path.join(root, filename))
                        print(f"Deleted: {filename}")


# Replace 'root_directory' with the path to your root directory containing all the folders with images
root_directory = 'E:\Manga\WebtoonDownloader\The Lone Necromancer'
remove_duplicate_files(root_directory)
