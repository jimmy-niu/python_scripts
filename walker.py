import os, sys, shutil

mypath = os.getcwd()

def get_file_names(root, files):
	file_names = []
	for name in files:
		file_names.append(os.path.join(root, name))
	return file_names

def move_files(dest, origin, files, extensions, keep_structure=True):
	for f in files:
		_, extension = os.path.splitext(f)
		if extension in extensions or not extensions:
			
			new_path = str(f).split(origin)[1]
			if keep_structure:
				new_path = dest + new_path
			else:
				new_path = dest + "\\" + os.path.basename(f)

			os.makedirs(os.path.dirname(new_path), exist_ok=True)
			try:			
				shutil.move(f, new_path)
			except:
				print("Failed file move: ", f)
		elif extension == ".json":
			os.remove(f)


file_structures = []
file_extensions = {}
sorted_files = {}

# Src, Dest, Keep_Structure
file_structures.append(("Takeout\Drive", "..\Drive", True))
file_extensions[("Takeout\Drive", "..\Drive", True)] = []

file_structures.append(("Takeout\Google Photos", "..\Photos", False))
file_extensions[("Takeout\Google Photos", "..\Photos", False)] = [".jpg", ".JPG", ".png", ".PNG", ".mp4", ".MP4", ".mov", ".MOV", ".jpeg", ".JPEG", ".mpg", ".mpeg", ".gif", ".GIF", ".m4v", ".M4V"]

file_structures.append(("Takeout\Contacts", "..\Contacts", False))
file_extensions[("Takeout\Contacts", "..\Contacts", False)] = [".jpg", ".JPG", ".png", ".PNG", ".mp4", ".MP4", ".mov", ".MOV", ".jpeg", ".JPEG", ".mpg", ".mpeg", ".gif", ".GIF", ".m4v", ".M4V"]

for root, dirs, files in os.walk(".", topdown=False):
	found = False
	for fs in file_structures:
		if ("Autodesk_Inventor_2014_Eng_64bit_dlm" in root or "Takeout\Drive\Trash" in root):
			found = True
			continue
		elif(fs[0] in root):
			if(fs in sorted_files):
				sorted_files[fs] += get_file_names(root, files)
			else:
				sorted_files[fs] = get_file_names(root, files)
			found = True
			continue
	if not found:
		print(root)


for fs in sorted_files:
	files = sorted_files[fs]
	move_files(fs[1], fs[0], files, file_extensions[fs], fs[2])



'''
Module to remove empty folders recursively. Can be used as standalone script or be imported into existing script.
https://jacobtomlinson.dev/posts/2014/python-script-recursively-remove-empty-folders/directories/
'''

def removeEmptyFolders(path, removeRoot=True):
  'Function to remove empty folders'
  if not os.path.isdir(path):
    return

  # remove empty subfolders
  try:
	  files = os.listdir(path)
	  if len(files):
	    for f in files:
	      fullpath = os.path.join(path, f)
	      if os.path.isdir(fullpath):
	        removeEmptyFolders(fullpath)

	  # if folder empty, delete it
	  files = os.listdir(path)
	  if len(files) == 0 and removeRoot:
	    print("Removing empty folder:", path)
	    os.rmdir(path)
  except:
	  print("bungus")

removeEmptyFolders(mypath)

