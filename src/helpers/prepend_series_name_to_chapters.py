import os

# Set the base directory
base_dir = r'U:\Books\Webtoon_Manhwa'

# Iterate over each series directory
for series_name in os.listdir(base_dir):
    series_path = os.path.join(base_dir, series_name)

    if os.path.isdir(series_path):
        # Iterate over each file in the series directory
        for filename in os.listdir(series_path):
            # Only target files with the .cbz extension
            if filename.endswith('.cbz'):
                # Check if the series name is already in the filename
                if not filename.startswith(series_name):
                    # Create the new filename
                    new_filename = f"{series_name} {filename}"

                    # Define the full path for the old and new filenames
                    old_file_path = os.path.join(series_path, filename)
                    new_file_path = os.path.join(series_path, new_filename)

                    # Rename the file
                    os.rename(old_file_path, new_file_path)
                    print(f'Renamed "{old_file_path}" to "{new_file_path}"')
                else:
                    print(f'Skipped renaming "{filename}" as it already contains the series name.')

print("Renaming completed.")
