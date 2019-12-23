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

# What exactly happens?

## Folders created:

```
/src/constants
/src/screens
/src/assets
/src/components
/src/db
/src/config
```

## Files changed:

### App.js to:

```
//sudonpm's Navigator Main App file

import { createAppContainer } from 'react-navigation';
import Navigator from './src/components/Navigator';

export default createAppContainer(Navigator);
```

### app.json changed:

```assets/icon.png```  to ```src/assets/icon.png```

```assets/splash.png``` to ```src/assets/splash.png```

## Deleted assets folder after copying it's contents to src/assets folder.

## Files Created:

### src/components/Navigator.js:

```
//sudonpm's Navigator Component

import { createStackNavigator } from 'react-navigation-stack';

import MainScreen from '../screens/MainScreen';

const Navigator = createStackNavigator(
    {
        Main: MainScreen
      },
      {
        initialRouteName: 'Main',
        defaultNavigationOptions: {
          title: 'Accountable 0.1'
        }
      }
);

export default Navigator;
```

### src/screens/MainScreen.js:

```
//sudonpm's Navigator's Main Screen

import React from 'react';
import { Text, View } from 'react-native';

const MainScreen = ({ navigation }) => {
  //instead of using props.navigation.navigate we
  //can just call navigation as seen above to use
  //navigation.navigate
  //EX: onPress={() => navigation.navigate('Main')}
  return ( 
    <View>
      <Text>
        Accountable
      </Text>
    </View>
  );
};

export default MainScreen;
```