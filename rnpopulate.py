#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import os
import shutil
from os import path

# get the path of where the project/script is being run
currentPath = os.getcwd()

# define the name of the directories to be created
path1 = "%s/src/constants" % currentPath
path2 = "%s/src/screens" % currentPath
path3 = "%s/src/assets" % currentPath
path4 = "%s/src/components" % currentPath
path5 = "%s/src/db" % currentPath
path6 = "%s/src/config" % currentPath

# make directories
if (str(path.exists(path1)) == "False"):
    os.makedirs(path1)
    print("created: %s folder" % path1)
else: print("%s already exists" % path1)

if str(path.exists(path2)) == "False":
    os.makedirs(path2)
    print("created: %s folder" % path2)
else: print("%s already exists" % path2)

if str(path.exists(path3)) == "False":
    os.makedirs(path3)
    print("created: %s folder" % path3)
else: print("%s already exists" % path3)

if str(path.exists(path4)) == "False":
    os.makedirs(path4)
    print("created: %s folder" % path4)
else: print("%s already exists" % path4)

if str(path.exists(path5)) == "False":
    os.makedirs(path5)
    print("created: %s folder" % path5)
else: print("%s already exists" % path5)

if str(path.exists(path6)) == "False":
    os.makedirs(path6)
    print("created: %s folder" % path6)
else: print("%s already exists" % path6)

# copy assets files to new directory

if str(path.isfile("%s/splash.png" % path3)) == "False":
    shutil.copy('%s/assets/splash.png' % currentPath, '%s/' % path3)
    print("copied splash.png successfully")
else: print("splash.png file already exists")

if str(path.isfile("%s/icon.png" % path3)) == "False":
    shutil.copy('%s/assets/icon.png' % currentPath, '%s/' % path3)
    print("copied icon.png successfully")
else: print("icon.png file already exists")


# Replace variables in file
if str(path.isfile("%s/app.json" % currentPath)) == "True":
    with open('%s/app.json' % currentPath, 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace('"icon": "./assets/icon.png"', '"icon": "./src/assets/icon.png"'))
        print("done app.json replacement from ./assets/icon to ./src/assets/icon")
else: print("%s/app.json does not exist to be modified" % currentPath)


if str(path.isfile("%s/app.json" % currentPath)) == "True":
    with open('%s/app.json' % currentPath, 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace('"image": "./assets/splash.png"', '"image": "./src/assets/splash.png"'))
        print("done app.json replacement from ./assets/splash to ./src/assets/splash")
else: print("%s/app.json does not exist to be modified" % currentPath)

# delete project/assets folder now that we are using /src/assets
if str(path.exists('%s/assets' % currentPath)) == "True":
    shutil.rmtree('%s/assets' % currentPath)
    print("done deleting project/assets folder now that we are using project/src/assets")
else: print("%s/assets doesn't exist to be deleted." % currentPath)