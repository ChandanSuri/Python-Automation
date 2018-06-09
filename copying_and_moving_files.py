import shutil

#file name variables
file_name_from = 'C:\\spam.txt'
file_name_to = 'C:\\delicious'

file_name_to_rename = 'C:\\delicious\\spam123.txt'

dir_name_from = 'C:\\delicious'
dir_name_to = 'C:\\delicious_backup'

# copy the file
shutil.copy(file_name_from, file_name_to)
#copy and rename the file
shutil.copy(file_name_from, file_name_to_rename)
#copy whole directory to another directory
shutil.copytree(dir_name_from, dir_name_to)
#move a file to another directory
shutil.move(file_name_from, dir_name_to)
#move function can also be used to rename,when used different name...

import os

current_dir = os.getcwd()
file_path_to_delete = 'C:\\folder1\\folder2\\sp.txt'
dir_to_delete = 'C:\\folder1'
#delete a file
os.unlink(file_path_to_delete)
# gives error when not empty directory
os.rmdir(dir_to_delete)
#this deletes the directries with all files and directories inside it...
shutil.rmtree(dir_to_delete)

import send2trash

#sends the files to recycle bin... so when you dont want to delete the file permanently...
send2trash.send2trash(dir_to_delete)
# you can also send files to recycle bin...


# Walking a Directory Tree

import os

for folder_name, subfolders, filenames in os.walk(dir_name_to):
	print('The folder is ' + folder_name)
	print('The subfolders in ' + str(folder_name) + ' are: ' + str(subfolders))
	print('The filenames in  ' + str(folder_name + ' are: ' + str(filenames)))

# you can also iterate for sub folders with in the the subfolders in the directory...
