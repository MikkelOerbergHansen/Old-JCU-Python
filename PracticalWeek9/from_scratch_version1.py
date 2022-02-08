import os
import shutil

print("Starting directory is: {}".format(os.getcwd()))
os.chdir('FilesToSort')
print("(Current working directory is: {})".format(os.getcwd()))
path = os.getcwd()
file_names = []
for filename in os.listdir('.'):
    # Ignore directories, just process files
    if os.path.isdir(filename):
        continue
    file_names.append(filename)
folder_name = ['xlsx', 'docx', 'png', 'doc', 'txt', 'xls', 'jpg', 'gif']
for names in folder_name:
    try:
        os.mkdir(names)
    except FileExistsError:
        pass

for files in file_names:
    if ".xlsx" in files:
        shutil.move(files, 'xlsx/' + files)
    elif ".docx" in files:
        shutil.move(files, 'docx/' + files)
    elif ".png" in files:
        shutil.move(files, 'png/' + files)
    elif ".doc" in files:
        shutil.move(files, 'doc/' + files)
    elif "txt" in files:
        shutil.move(files, 'txt/' + files)
    elif "xls" in files:
        shutil.move(files, 'xls/' + files)
    elif "jpg" in files:
        shutil.move(files, 'jpg/' + files)
    elif "gif" in files:
        shutil.move(files, 'gif/' + files)
