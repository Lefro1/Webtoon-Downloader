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


def combine_files(file_1, file_2, destination):
    with open(file_1, 'r') as file1, open(file_2, 'r') as file2:
        contents1 = file1.read()
        contents2 = file2.read()

    combined_contents = contents1 + contents2

    with open(destination, 'w') as dest_file:
        dest_file.write(combined_contents)


def main():
    subscriptions = "subscriptions.txt"
    additional = "additional_downloads.txt"
    all_downloads = "all_downloads.txt"

    organize_file(read_and_sort_file(subscriptions), subscriptions)
    organize_file(read_and_sort_file(additional), additional)
    combine_files(subscriptions, additional, all_downloads)


if __name__ == '__main__':
    main()
