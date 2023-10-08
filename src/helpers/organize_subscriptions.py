import re


def sanitize_filename(filename):
    # Define a regex pattern to match any illegal characters in filenames
    illegal_chars = r'[<>:"/\\|?*]'
    replacement_chars = {'’': '\'',
                         'â€™': '\''
                         }

    for illegal_char in replacement_chars:
        filename = re.sub(illegal_char, replacement_chars[illegal_char], filename)

    # Remove any illegal characters from the filename
    return re.sub(illegal_chars, '', filename)


def read_and_sort_file(file_name):
    # Initialize an empty list to store the subscriptions
    subscriptions = []

    # Read the data from subscriptions.txt
    with open(file_name, 'r') as file:
        for line in file:
            # Split the line by '|' to get the series name and URL
            series_name, url = line.strip().split('|')

            # Remove any illegal characters from series_name and url
            series_name = sanitize_filename(series_name.strip())

            subscriptions.append((series_name, url))

    # Sort the subscriptions alphabetically by series name
    sorted_subscriptions = sorted(subscriptions, key=lambda x: x[0])

    return sorted_subscriptions


def organize_file(sorted_subscriptions, file_name):
    # Write the sorted subscriptions back to the target file
    with open(file_name, 'w') as file:
        for series_name, url in sorted_subscriptions:
            file.write(f"{series_name}|{url}\n")

def organize_daily_pass(file_path):
    """
    Daily pass definition is different because it does not user the | delimiter.
    """
    # Read the content of the file
    with open(file_path, 'r') as file:
        titles = file.readlines()

    # Remove leading/trailing whitespaces and sort the titles
    sorted_titles = sorted([title.strip() for title in titles])

    # Write the sorted titles back to the file
    with open(file_path, 'w') as file:
        file.write("\n".join(sorted_titles))


def combine_files(file_1, file_2, destination):
    with open(file_1, 'r') as file1, open(file_2, 'r') as file2:
        contents1 = file1.read()
        contents2 = file2.read()

    combined_contents = contents1 + contents2

    with open(destination, 'w') as dest_file:
        dest_file.write(combined_contents)


def create_series_dict(main_file):
    # Create a dictionary to store series names as keys and URLs as values
    series_dict = {}
    with open(main_file, 'r') as file1:
        for line in file1:
            series_name, url = line.strip().split('|')
            series_dict[series_name] = url
    return series_dict


def remove_entries(main_file, removal_file):
    # Create a dictionary from the main file
    series_dict = create_series_dict(main_file)

    # Read the lines from the removal file
    with open(removal_file, 'r') as file2:
        lines_removal = {line.strip() for line in file2}

    # Find the series names to keep (those not in removal file)
    series_to_keep = {series_name: url for series_name, url in series_dict.items() if series_name not in lines_removal}

    # Rewrite the filtered lines back to the main file
    with open(main_file, 'w') as file1:
        for series_name, url in series_to_keep.items():
            file1.write(f"{series_name}|{url}\n")


def main():
    subscriptions = "subscriptions.txt"
    additional = "additional_downloads.txt"
    all_downloads = "all_downloads.txt"
    daily_pass = "daily_pass.txt"

    organize_file(read_and_sort_file(subscriptions), subscriptions)
    organize_file(read_and_sort_file(additional), additional)
    organize_daily_pass(daily_pass)
    combine_files(subscriptions, additional, all_downloads)
    remove_entries(all_downloads, daily_pass)


if __name__ == '__main__':
    main()
