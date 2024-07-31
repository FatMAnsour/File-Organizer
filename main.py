import os
import shutil

def organize_files(direcory):
    if not os.path.exists(direcory):
     print(f"the Directory {direcory} not found")
     return

    # Create a dictionary to map file extensions to folder names
    file_types={
     'Documents':['.pdf','.docx','.txt','.xlsx','.pptx'],
     'Image':['.png','.jpg','.jpeg','.gif','.bmp','.tiff'],
     'Audio': ['.mp3', '.wav', '.aac'],
     'Video': ['.mp4', '.mov', '.avi'],
     'Archives': ['.zip', '.tar', '.rar', '.gz']
    }
    for folder in file_types:
      folder_path=os.path.join(directory,folder)
      if not os.path.exists(folder_path):
            os.mkdir(folder_path)
            print(f"Created folder: {folder_path}")
    
    for file in os.listdir(direcory):
        file_path=os.path.join(direcory,file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()

            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    # Move the file to the corresponding folder
                    shutil.move(file_path, os.path.join(directory, folder, file))
                    print(f"Moved: {file} -> {folder}")
                    break

if __name__ == "__main__":
    # Define the path to the directory you want to organize
    directory = 'Enter-Your-Directory'
    
    # Call the function to organize files in the specified directory
    organize_files(directory)


