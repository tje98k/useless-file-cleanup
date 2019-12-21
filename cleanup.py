import os
import hashlib

trashlist = [] 
print('enter path to search for files')
path = input()

print('scanning for probable trash files in ' + path)

for root, dirs, files in os.walk(path):
    if '.' in root:
        pass
    elif 'AppData' in root: 
        pass
    elif 'Windows' in root:
        pass
    elif 'Program Files' in root:
        pass
    elif 'AMD' in root:
        pass
    elif 'ProgramData' in root:
        pass
    else:
        for file in files:
            if '.rar' in file:
                trashlist.append(os.path.join(root, file))
            elif '.msi' in file:
                trashlist.append(os.path.join(root, file))
            elif '.7z' in file:
                trashlist.append(os.path.join(root, file))
            elif 'install' in file:
                trashlist.append(os.path.join(root, file))
            elif 'installer' in file:
                trashlist.append(os.path.join(root, file))
            elif '.zip' in file:
                trashlist.append(os.path.join(root, file))
            
print('these files were found in ' + path + ' and may be useless')
for trashfile in trashlist:
    print(trashfile)
print('do you wish to delete the aforementioned files? type "y" or "n"')
trashanswer = input()
if trashanswer == 'n':
    pass
elif trashanswer == 'y':
    for trashfile in trashlist:
            os.remove(trashfile)
            print('Deleted file ' + trashfile)
else:
    print('please either type "y" or "n"')
        
print('now checking on ' + path + ' for duplicate files')

uniquelist = dict()
duplicatelist = []
for root, dirs, files in os.walk(path):
    if '.' in root:
        pass
    elif 'AppData' in root: 
        pass
    elif 'Windows' in root:
        pass
    elif 'Program Files' in root:
        pass
    elif 'AMD' in root:
        pass
    elif 'ProgramData' in root:
        pass
    else:
        try:
            for file in files:
               filehash = hashlib.md5(open(os.path.join(root, file), 'rb').read()).hexdigest()
               if filehash not in uniquelist:
                        uniquelist[filehash] = os.path.join(root, file)
               else:
                   if os.path.join(root, file) not in uniquelist:
                       if os.path.join(root, file) not in duplicatelist:
                           duplicatelist.append(os.path.join(root, file))
                           print(os.path.join(root, file) + ' is a duplicate of ' + uniquelist[filehash])
        except:
            pass

print('Do you wish to delete these duplicates? type "y" or "n"')
dupanswer = input()
if dupanswer == 'n':
    print('okay. closing program.')
elif dupanswer == 'y':
    for duplicatefile in duplicatelist:
            os.remove(duplicatefile)
            print('Deleted file ' + duplicatefile)
else:
    print('please either type "y" or "n"')

