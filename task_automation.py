import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f" Created destination folder: {destination_folder}")

    moved_count = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.jpg'):
            src_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(destination_folder, filename)
            shutil.move(src_path, dest_path)
            moved_count += 1
            print(f"Moved: {filename}")

    if moved_count == 0:
        print(" No .jpg files found to move.")
    else:
        print(f"Successfully moved {moved_count} .jpg file(s).")

if __name__ == "__main__":
    src = input("Enter source folder path: ")
    dest = input("Enter destination folder path: ")
    move_jpg_files(src, dest)
