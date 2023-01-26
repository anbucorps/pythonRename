import os, pathlib

def rename_files(root):
    
    """Function to rename files in a directory"""
    os.chdir(root)
    counter = 1
    folder_name = os.path.basename(root)

    for subdir, dirs, files in os.walk(root):
        dirs.sort()
        files.sort()
        for file in files:
            # remove .db files
            if file.endswith(".db"):
                os.remove(os.path.join(subdir, file))
            folder_name = os.path.basename(subdir)
            if folder_name != os.path.basename(root):
                counter = 1
                os.chdir(subdir)
            # split filename and extension into two variables
            file_name, file_ext = os.path.splitext(file)
            new_name = folder_name + '-' + '{ind:04d}'.format(ind=counter) + file_ext
            if file != new_name and os.path.isfile(file):
                if os.path.isfile(new_name):
                    while os.path.isfile(new_name):
                        counter += 1
                        new_name = folder_name + '-' +'{ind:04d}'.format(ind=counter) + file_ext
                os.replace(file, new_name)
            counter += 1

def main():
    root = pathlib.Path(__file__).parent.absolute()
    rename_files(root)

if os.name == 'nt' or os.name == 'posix':
    main()
