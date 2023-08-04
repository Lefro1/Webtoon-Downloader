import re

def sanitize_filename(filename):
    # Define a regex pattern to match any illegal characters in filenames
    illegal_chars = r'[<>:"/\\|?*]'

    # Remove any illegal characters from the filename
    return re.sub(illegal_chars, '', filename)

def read_subscriptions():
    subscriptions_file = "subscriptions.txt"

    # Initialize an empty list to store the subscriptions
    subscriptions = []

    # Read the data from subscriptions.txt
    with open(subscriptions_file, 'r') as file:
        for line in file:
            # Split the line by '|' to get the series name and URL
            series_name, url = line.strip().split('|')

            # Remove any illegal characters from series_name and url
            series_name = sanitize_filename(series_name.strip())
            url = sanitize_filename(url.strip())

            subscriptions.append((series_name, url))

    # Sort the subscriptions alphabetically by series name
    sorted_subscriptions = sorted(subscriptions, key=lambda x: x[0])

    return sorted_subscriptions


def write_subscriptions(sorted_subscriptions):
    subscriptions_file = "subscriptions.txt"

    # Write the sorted subscriptions back to subscriptions.txt
    with open(subscriptions_file, 'w') as file:
        for series_name, url in sorted_subscriptions:
            file.write(f"{series_name}|{url}\n")


# Read the subscriptions, sort them, and write back to the file
sorted_subscriptions = read_subscriptions()
write_subscriptions(sorted_subscriptions)


def main():
    write_subscriptions(read_subscriptions())


if __name__ == '__main__':
    main()
