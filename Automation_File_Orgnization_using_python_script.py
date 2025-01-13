#Import Python modules.
import os #for interact with operating system (files,folders.. manage)
import shutil #for move and save files folders.
source_folder = "C:/Users/vci/Desktop/Experiment"
categories = {
    "Images": [".jpg",".png",".gif",".webp"],
    "Videos": [".mp4",".mkv",".avi"],
    "Music": [".mp3",".wav"],
    "Documents": [".pdf",".docx",".txt"],
    "Archives": [".zip",".rar"],
}

for category in categories.keys():
    folder_path = os.path.join(source_folder,category)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder,file_name)
    if os.path.isfile(file_path):
        file_extenstion = os.path.splitext(file_name)[1]
        moved = False
        for category,extentions in categories.items():
            if file_extenstion in extentions:
                shutil.move(file_path,os.path.join(source_folder,category))
                moved = True
                print(f"Moved: {file_name} -> {category}")
        if not moved:
            other_folder = os.path.join(source_folder,"Others")
            if not os.path.exists(other_folder):
                os.mkdir(other_folder)
            shutil.move(file_path,os.path.join(other_folder,file_name))
            print(f"Moved: {file_name} -> {category}")
