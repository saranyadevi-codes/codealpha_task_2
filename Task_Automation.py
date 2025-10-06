import os
import shutil

# Ask the user for folder paths (works for everyone)
source_folder = input("Enter the source folder path: ")
destination_folder = input("Enter the destination folder path: ")

# Check if destination folder exists; if not, create it
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through all files in the source folder
for file_name in os.listdir(source_folder):

    # Move only .jpg and .jpeg files
    if file_name.lower().endswith((".jpg", ".jpeg")):
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # Move the file and print its name
        shutil.move(source_path, destination_path)
        print(f"Moved: {file_name}")

print("All JPG files have been moved!")