# React Native Populate

### This python script is for new React Native Projects.

# What exactly does it do?

## Folders created:

```
/src/assets
/src/components
/src/config
/src/constants
/src/db
/src/screens
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

# Dependencies required:

```
react-native-gesture-handler
react-navigation
react-navigation-stack
```

# Installation/Use:

I've modified my **.bash_profile** and added:

```export PYTHONPATH=$PYTHONPATH:/My/Scripts/Folder/That/Has/rnpopulate.py```

So when I start a new project in Code's terminal window I can just type:

```
python
import rnpopulate
```