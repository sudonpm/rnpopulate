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

# writing and implementing Navigator Component
# open file
file1 = open("%s/App.js" % currentPath, "w")
# set strings in the array L
L = ["import { createAppContainer } from 'react-navigation'; \n",
     "import Navigator from './src/components/Navigator'; \n\n",
     "export default createAppContainer(Navigator); \n"]


# write to file with header first then strings defined in L
file1.write("//sudonpm's Navigator Main App file \n\n")
file1.writelines(L)
# close file
file1.close()

# open file
file2 = open("%s/Navigator.js" % path4, "w")
# set strings in the array S
S = ["import { createStackNavigator } from 'react-navigation-stack'; \n\n",
     "import MainScreen from '../screens/MainScreen'; \n\n",
     "const Navigator = createStackNavigator( \n",
     "    { \n",
     "        Main: MainScreen, \n",
     "      }, \n",
     "      { \n",
     "        initialRouteName: 'Main', \n",
     "        defaultNavigationOptions: { \n",
     "          title: 'App Title' \n",
     "        } \n",
     "      } \n",
     "); \n\n",
     "export default Navigator;"]


# write to file with header first then strings defined in S
file2.write("//sudonpm's Navigator Component \n\n")
file2.writelines(S)
# close file
file2.close()

# open file
file3 = open("%s/MainScreen.js" % path2, "w")
# set strings in the array K
K = ["import React from 'react'; \n",
     "import { Text, View } from 'react-native'; \n\n",
     "const MainScreen = ({ navigation }) => { \n",
     "  return ( \n",
     "    <View> \n",
     "      <Text> \n",
     "        App Main Screen \n",
     "      </Text> \n",
     "    </View> \n",
     "  ); \n",
     "}; \n\n",
     "export default MainScreen;"]


# write to file with header first then strings defined in K
file3.write("//sudonpm's Navigator's Main Screen \n\n")
file3.writelines(K)
# close file
file3.close()