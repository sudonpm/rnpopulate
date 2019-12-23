# React Native Populate

### This python script is for new React Native Projects.

It will read from the directory of where it is being run and populate that directory with the folder src and some subfolders.

It will copy the assets folder to src/assets and then delete the assets folder.

It will modify app.json so it reads from src/assets.

I've added a Navigator component to be implemented/read from App.js with a MainScreen.js as well. Very blank for now but sets a good foundation for navigation with a new app.

## Dependencies required:

```react-native-gesture-handler```

```react-navigation```

```react-navigation-stack```

# Installation/Use:

I've modified my **.bash_profile** and added:

```export PYTHONPATH=$PYTHONPATH:/My/Scripts/Folder/That/Has/rnpopulate.py```

So when I start a new project in Code's terminal window I can just type:

```python```

```import rnpopulate```
