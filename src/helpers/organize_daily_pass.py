def organize_file(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        titles = file.readlines()

    # Remove leading/trailing whitespaces and sort the titles
    sorted_titles = sorted([title.strip() for title in titles])

    # Write the sorted titles back to the file
    with open(file_path, 'w') as file:
        file.write("\n".join(sorted_titles))

if __name__ == "__main__":
    file_path = "daily_pass.txt"
    organize_file(file_path)
