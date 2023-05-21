import os
import zipfile



def main():
    root_dir = r'E:/Manga/WebtoonDownloader'
    output_dir = r'E:/Manga/WebtoonDownloaderZipped'

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over the first level subdirectories
    for dir_name in os.listdir(root_dir):
        dir_path = os.path.join(root_dir, dir_name)
        if os.path.isdir(dir_path):
            # Create a separate folder for each first level subdirectory within the output directory
            output_subdir = os.path.join(output_dir, dir_name)
            os.makedirs(output_subdir, exist_ok=True)

            # Iterate over the second level subdirectories
            for subdir_name in os.listdir(dir_path):
                subdir_path = os.path.join(dir_path, subdir_name)
                if os.path.isdir(subdir_path):
                    # Create a zip file for each second level subdirectory within the corresponding output folder
                    output_file = os.path.join(output_subdir, f'{subdir_name}.cbz')
                    if not os.path.exists(output_file):
                        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                            # Add all files in the current second level subdirectory to the ZIP
                            for root, _, files in os.walk(subdir_path):
                                print(f"Zipping {subdir_path}")
                                for file in files:
                                    file_path = os.path.join(root, file)
                                    zipf.write(file_path, os.path.relpath(file_path, subdir_path))


if __name__ == '__main__':
    main()
