import os
import zipfile
import concurrent.futures
from concurrent.futures import as_completed

MAX_WORKERS = 8
ROOT_DIR = r'E:/Manga/WebtoonDownloader'
OUTPUT_DIR = r'E:/Manga/WebtoonDownloader_Zipped'

def truncate_folder_name(folder_name: str) -> str:
    idx = folder_name.find('(')
    return folder_name[:idx].strip() if idx != -1 else folder_name

def zip_folder(subdir_path: str, output_file: str) -> str:
    # Return a status string so we can print from the main thread
    try:
        # Make sure parent dir exists (in case call site races on creation)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with zipfile.ZipFile(output_file, mode='w', compression=zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(subdir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, subdir_path)
                    zipf.write(file_path, arcname)
        return f"OK  | {subdir_path} -> {output_file}"
    except Exception as e:
        # If something failed, try to remove a partial file
        try:
            if os.path.exists(output_file):
                os.remove(output_file)
        except Exception:
            pass
        return f"ERR | {subdir_path}: {e!r}"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    futures = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for series_name in os.listdir(ROOT_DIR):
            series_path = os.path.join(ROOT_DIR, series_name)
            if not os.path.isdir(series_path):
                continue

            # Each series has its own output subdir
            series_out = os.path.join(OUTPUT_DIR, series_name)
            os.makedirs(series_out, exist_ok=True)

            for chapter_name in os.listdir(series_path):
                chapter_path = os.path.join(series_path, chapter_name)
                if not os.path.isdir(chapter_path):
                    continue

                truncated = truncate_folder_name(chapter_name)
                output_file = os.path.join(series_out, f"{truncated}.cbz")

                if os.path.exists(output_file):
                    continue

                # Submit this chapter to the shared pool
                futures.append(executor.submit(zip_folder, chapter_path, output_file))

        # Report results as they complete
        for fut in as_completed(futures):
            print(fut.result())

    print(f"Done. Submitted {len(futures)} chapter(s).")

if __name__ == '__main__':
    main()
