import os
import shutil

def copy_dir_content(source, destination):
    if not os.path.exists(source):
        raise ValueError("Source does not exist")   
    
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
        
    for path in os.listdir(source):
        fullPath = os.path.join(source, path)
        if os.path.isfile(fullPath):
            shutil.copy(fullPath, destination)
        else:
            new_dest = os.path.join(destination, path)
            copy_dir_content(fullPath, new_dest)

def read_file(path):
    with open(path) as f:
        return f.read()
    
def get_all_files_paths(directory, extension = None):
    ans = []
    for path in os.listdir(directory):
        fullPath = os.path.join(directory, path)
        if os.path.isfile(fullPath):
            if extension != None:
                if fullPath.split(".")[-1] != extension:
                    continue
            ans.append(fullPath)
        else:
            ans.extend(get_all_files_paths(fullPath, extension))
    return ans
    
def save_file(path, content, create_dir = False):
    if not os.path.exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            if create_dir:
                os.makedirs(dir)
            else:
                raise Exception(f"Destination directory {dir} does not exist")
              
    with open(path, "w") as f:
        f.write(content)