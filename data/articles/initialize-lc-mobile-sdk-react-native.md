---
title: "Initialize LC Mobile SDK - React Native"
slug: initialize-lc-mobile-sdk-react-native
url: https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native
---

# Initialize LC Mobile SDK - React Native

# Initialize Live Chat Mobile SDK - React Native


In the initialization steps, you prepare the Sprinklr Messenger Client SDK so that Live Chat can function correctly within your app by setting up the environment, user context, and configuration. The `takeOff` method is the entry point for this process, enabling you to initialize the SDK for different types of users such as anonymous, authenticated, or custom authenticated, depending on your app’s requirements.

  The following are the steps for integrating Sprinklr Messenger.
  This page covers the **third step: Initialize**.
  Use the flow below to navigate through all steps of the integration process.

  [Install](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native) >
  [Setup](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native) >
  **Initialize** >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-react-native) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native)


**On this page:**



- [Initialize for Anonymous Users](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native#initialize-anonymous-users)

- [Initialize for Authenticated Users](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native#initialize-authenticated-users)

- [Initialize for Custom Authenticated Users](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native#initialize-custom-users)


## Initialize for Anonymous Users

For anonymous users (unauthenticated users), you can initialize the messenger using the `takeOff` method without specifying any user details. Behind the scenes, an anonymous user is automatically created for the messenger and the flow for anonymous user is initialized.


**Dev Notes:**



- The `takeOff` method must be called only once in the application lifecycle.

- For optimal performance, call the `takeOff` method at the root of the application or as early as possible in your application flow.


### Syntax

To set up Sprinklr Messenger, you need to link the Sprinklr Messenger in your project and add the necessary permissions.



import MessengerClient from '@sprinklrjs/chat-native-client'
MessengerClient.takeOff({
  appId: '', // This will be provided by Sprinklr
  environment: '', // This will be provided by Sprinklr
  pushAppId: '', // Should be Unique id, if not sure pass same as device ID
  deviceId: '',
  skin: 'MODERN', // default value is MODERN, options: CLASSIC | MODERN
  locale: '', // default value is en
  themeMode: 'DEFAULT' // default value is DEFAULT, options DEFAULT | DARK
})





## Parameters





















      ``










****````
****``





****``





****````
****``




| Parameter | Description | Required/Optional |
| --- | --- | --- |
| appId | Unique identifier of the Live Chat app. This will be provided by Sprinklr. | Required |
| environment | This will be provided by Sprinklr. | Required |
| pushAppId | Unique identifier for push notifications. If unsure, use the same value as deviceId. | Optional |
| deviceId | Unique identifier for the device. | Optional |
| skin | Defines the messenger UI skin.         Supported Values: CLASSIC, MODERN         Default Value: MODERN | Optional |
| locale | Sets the language/locale for the messenger.         Default Value: en | Required |
| themeMode | Defines the theme mode.         Supported Values: DEFAULT, DARK         Default Value: DEFAULT | Optional |


**Dev Notes:**To update user information or implement custom authentication, see Configure Live Chat Messenger.

## Initialize for Authenticated Users

For authenticated users, initialize the messenger using the `takeOff` method with user details. The `takeOff` method will consider the provided user details for the messenger and initialize the flow accordingly.


**Dev Notes:**



- The `takeOff` method must be called only once in the application lifecycle.

- For updating the user details or other information in the messenger, you can use the dedicated methods explained in the Configure Live Chat section.

- For optimal performance, call the `takeOff` method at the root of the application or as early as possible in your application flow.


### Syntax

To set up Sprinklr Messenger, you need to link the Sprinklr Messenger in your project and add the necessary permissions.



import MessengerClient from '@sprinklrjs/chat-native-client'
MessengerClient.takeOff({
  appId: '', // This will be provided by Sprinklr
  environment: '', // This will be provided by Sprinklr
  pushAppId: '', // Should be Unique id, if not sure pass same as device ID
  deviceId: '',
  locale: '', // default value is en
  skin: 'MODERN', // default value is MODERN, options: CLASSIC | MODERN
  themeMode: 'DEFAULT', // default value is DEFAULT, options: DEFAULT | DARK
  user: {
    userId: '12345',
    firstName: 'John',
    lastName: 'Doe',
    phoneNo: '9876543210',
    email: 'John.Doe@example.com',
    profileImageUrl: 'https://example.com/profilePic.jpg',
    hash: 'f30c3b0835ecd378a134c74bce8cea866df8c5b6e12a8c219c9bb288f7270e22',
    hashCreationTime: 173888892 // in EPOCH and should be the same one that is used for generating the hash
  }
})





### Parameters





















      ``










****````
****``





****``





****````
****``









| Parameter | Description | Required/Optional |
| --- | --- | --- |
| appId | Unique identifier of the Live Chat app. This will be provided by Sprinklr. | Required |
| environment | This will be provided by Sprinklr. | Required |
| pushAppId | Unique identifier for push notifications. If unsure, use the same value as deviceId. | Optional |
| deviceId | Unique identifier for the device. | Optional |
| skin | Defines the messenger UI skin.         Supported Values: CLASSIC, MODERN         Default Value: MODERN | Optional |
| locale | Sets the language/locale for the messenger.         Default Value: en | Required |
| themeMode | Defines the theme mode.         Supported Values: DEFAULT, DARK         Default Value: DEFAULT | Optional |
| user | Specifies user details. For more details, see the User Object table. | Required (for authenticated chats) |

### User Object



















































| Parameter | Description | Required/Optional |
| --- | --- | --- |
| userId | Unique identifier of the user. | Required |
| firstName | First name of the user. | Optional |
| lastName | Last name of the user. | Optional |
| phoneNo | Phone number of the user. | Optional |
| email | Email ID of the user. | Optional |
| profileImageUrl | URL to the profile image of the user. | Optional |
| hash | To know the steps to generate a hash, see How to generate Hash? | Required |
| hashCreationTime | The timestamp indicating when the hash was generated. Use the same hash creation time that was applied during hash generation to ensure validation. For detailed steps, see How to Generate User Hash. | Required |

## Initialize for Custom Users

You can create a custom user with custom parameters and pass them to the `takeOff` method.


**Dev Notes:**



- The `takeOff` method must be called only once in the application lifecycle.

- For updating the user details or other information in the messenger, you can use the dedicated methods explained in other sections.

- For optimal performance, call the `takeOff` method at the root of the application or as early as possible in your application flow.

- If you want to implement a custom user authentication flow, contact the Sprinklr Support team at [tickets@sprinklr.com](mailto:tickets@sprinklr.com) to discuss the implementation process.


### Syntax

To set up Sprinklr Messenger, you need to link the Sprinklr Messenger in your project and add the necessary permissions.



import MessengerClient from '@sprinklrjs/chat-native-client'
MessengerClient.takeOff({
  appId: '', // This will be provided by Sprinklr
  environment: '', // This will be provided by Sprinklr
  pushAppId: '', // Should be Unique id, if not sure pass same as device ID
  deviceId: '',
  locale: '', // default value is en
  skin: 'MODERN', // default value is MODERN, options: CLASSIC | MODERN
  themeMode: 'DEFAULT', // default value is DEFAULT, options: DEFAULT | DARK
  customUser: {
    customAttribute1: 'value1', // Add your custom attribute
    customAttribute2: 'value2', // Add your custom attribute
    hash: 'f30c3b0835ecd378a134c74bce8cea866df8c5b6e12a8c219c9bb288f7270e22',
    hashCreationTime: 173888892 // in EPOCH and should be the same one that is used for generating the hash
  }
})





### Parameters





















      ``










****````
****``





****``





****````
****``









| Parameter | Description | Required/Optional |
| --- | --- | --- |
| appId | Unique identifier of the Live Chat app. This will be provided by Sprinklr. | Required |
| environment | This will be provided by Sprinklr. | Required |
| pushAppId | Unique identifier for push notifications. If unsure, use the same value as deviceId. | Optional |
| deviceId | Unique identifier for the device. | Optional |
| skin | Defines the messenger UI skin.         Supported Values: CLASSIC, MODERN         Default Value: MODERN | Optional |
| locale | Sets the language/locale for the messenger.         Default Value: en | Required |
| themeMode | Defines the theme mode.         Supported Values: DEFAULT, DARK         Default Value: DEFAULT | Optional |
| customUser | User details containing custom parameters and hash. For more details, see the Custom User Object table. | Required (for custom users) |

### Custom User Object


























| Parameter | Description | Required/Optional |
| --- | --- | --- |
| Custom Attribute | This is a custom attribute that could be defined by you. You can define multiple custom attributes. | Required |
| hash | To know the steps to generate a hash, see How to generate Hash? | Required |
| hashCreationTime | The timestamp indicating when the hash was generated. Use the same hash creation time that was applied during hash generation to ensure validation. For detailed steps, see How to Generate User Hash. | Required |

## Next Steps

[Launch Live Chat Mobile SDK](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native)

## Additional Resources

See **All Integration Steps**
 [Install](https://dev.sprinklr.com/../install-lc-mobile-sdk-react-native) > [Setup](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native) > [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-react-native) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-react-native)

  [](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native)




[Back to top](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native)
