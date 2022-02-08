import os
import shutil

print("Starting directory is: {}".format(os.getcwd()))
os.chdir('FilesToSort2')
print("(Current working directory is: {})".format(os.getcwd()))

file_names = []
file_extensions = {}
for file in os.listdir("."):
    if os.path.isdir(file):
        continue
    file_names.append(file)
    extension = file.split('.')[-1]
    if extension not in file_extensions:
        category = input("what category do you want to sort {} files into? ".format(extension))
        file_extensions[extension] = category

folder_names = []
for extension in file_extensions:
    folder_name = file_extensions[extension]
    if folder_name not in folder_names:
        folder_names.append(folder_name)

for names in folder_names:
    try:
        os.mkdir(names)
    except FileExistsError:
        pass

for files in file_names:
    for extension in file_extensions.items():
        try:
            if extension[0] == files.split('.')[-1]:
                shutil.move(files, file_extensions[extension[0]] + "/" + files)
        except FileNotFoundError:
            pass
