#!/usr/bin/env python3

# importing os and pathlib modules
import os, pathlib

# Function to rename multiple files 
def main(): 
	root = pathlib.Path(__file__).parent.absolute()
	os.chdir(pathlib.Path(__file__).parent.absolute())

	i = 1
	dircheck = os.path.basename(root)
	folder_name = dircheck
	# run twice to get numbering of files correctly, sloppy but too tired to think of a better way
	for x in range(2):
		for subdir, dirs, files in os.walk(root):
			# sort directories in alphabetical order (not necessary, but nice congreguity between posix and windows in behavior)
			dirs.sort()
			# sort files in order (necessary for posix, works without this in windows)
			files.sort()
			for file in files:
				if file.endswith(".db"):
					os.remove(os.path.join(subdir, file))
				#set foldername to parent directory of file
				folder_name = os.path.basename(subdir)
				# reset count to 1 when iterating in new folder, change dircheck to new folders name
				if dircheck != folder_name:
					i=1
					dircheck = folder_name
					os.chdir(subdir)
				# split filename and extension into two variables
				file_name, file_ext = os.path.splitext(file)
				# name new file with foldername0001.example styled naming
				new_name = folder_name + '-' + '{ind:04d}'.format(ind=i) + file_ext
				# check for filename being duplicated
				if file != new_name:
					# check for new filename overwriting another file
					if os.path.isfile(new_name):
						while os.path.isfile(new_name):
							i += 1
							new_name = folder_name + '-' +'{ind:04d}'.format(ind=i) + file_ext
					os.replace(file, new_name)
				i += 1				
# tested on both windows and linux based OS
if os.name == 'nt' or os.name == 'posix':
	# call function
	main()
