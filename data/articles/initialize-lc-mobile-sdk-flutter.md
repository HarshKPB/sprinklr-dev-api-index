---
title: "Initialize LC Mobile SDK - Flutter"
slug: initialize-lc-mobile-sdk-flutter
url: https://dev.sprinklr.com/initialize-lc-mobile-sdk-flutter
---

# Initialize LC Mobile SDK - Flutter

# Initialize Live Chat Mobile SDK - Flutter


Initialization sets up the app environment and establishes the user context (anonymous, authenticated, or custom). The `takeOff` method is the entry point for this process, enabling you to initialize the SDK for different types of users such as anonymous, authenticated, or custom authenticated, depending on your app’s requirements.

  The following are the steps for integrating Sprinklr Messenger.
  This page covers the **second step: Initialize**.
  Use the flow below to navigate through all steps of the integration process.

  [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-flutter) >
  **Initialize** >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-flutter) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter)


**On this page:**



- [Initialize for Anonymous Users](https://dev.sprinklr.com/initialize-lc-mobile-sdk-flutter#initialize-anonymous-users)

- [Initialize for Authenticated Users](https://dev.sprinklr.com/initialize-lc-mobile-sdk-flutter#initialize-authenticated-users)

- [Initialize for Custom Authenticated Users](https://dev.sprinklr.com/initialize-lc-mobile-sdk-flutter#initialize-custom-users)


## Initialization Key Steps

The initialization process involves the following steps:

- Create a `SPRMessengerConfig` object with the parameters provided by Sprinklr.

- Call the `SPRMessenger().takeOff()` function with the SPRMessengerConfig object as an argument.

## Initialize for Anonymous Users

For anonymous users (unauthenticated users), you can initialize the messenger using the `takeOff` method without specifying any user details. Behind the scenes, an anonymous user is automatically created for the messenger and the flow for anonymous user is initialized.


**Dev Notes:**



- The `takeOff` method must be called only once in the application lifecycle.

- For optimal performance, call the `takeOff` method at the root of the application or as early as possible in your application flow.


### Syntax



SPRMessengerConfig messengerConfig = SPRMessengerConfig(
 appId: "SPR_APP_ID", // This will be provided by Sprinklr
 environment: " SPR_ENVIRONMENT ", // This will be provided by Sprinklr (eg-PROD)
 skin: "MODERN", // This can be either “CLASSIC” or “MODERN”
 locale: "en", // default value is en
 deviceId: "UNIQUE_DEVICE_ID",
 pushAppId: "SPR_PUSH_ID", // Should be Unique id, if not sure pass same as device ID
 themeMode: "DEFAULT", // default value is DEFAULT, options: DEFAULT | DARK "
 appKey: "com.sprinklr.messenger.release", // Should be "com.sprinklr.messenger.adhoc" for staging/dev builds.
);
SPRMessenger().takeOff(config: messengerConfig);




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


**Dev Notes:** To update user information or implement custom authentication, see Configure Live Chat Messenger.

## Initialize for Authenticated Users

For authenticated users, initialize the messenger using the `takeOff` method with user details. The `takeOff` method will consider the provided user details for the messenger and initialize the flow accordingly.


**Dev Notes:**



- The `takeOff` method must be called only once in the application lifecycle.

- For updating the user details or other information in the messenger, you can use the dedicated methods explained in the Configure Live Chat section.

- For optimal performance, call the `takeOff` method at the root of the application or as early as possible in your application flow.


### Syntax



SPRMessengerUser messengerUser = SPRMessengerUser(
 userId: "12345",
 firstName: "John",
 lastName: "Doe",
 phoneNumber: "999999999",
 email: "xyz@example.com",
 profileImageUrl: "https://images.com.1.png",
 hash: HmacHashCalculation.generateHash(
    data: "12345_John_Doe_https//images.com.1.png_999999999_xyz@example.com",
    key: "API_KEY", // This will be provided by Sprinklr
 ),
);
SPRMessengerConfig messengerConfig = SPRMessengerConfig(
 appId: "SPR_APP_ID", // This will be provided by Sprinklr
 environment: " SPR_ENVIRONMENT ", // This will be provided by Sprinklr (eg-PROD)
 skin: "MODERN", // This can be either “CLASSIC” or “MODERN”
 locale: "en", // default value is en
 deviceId: "UNIQUE_DEVICE_ID",
 pushAppId: "SPR_PUSH_ID", // Should be Unique id, if not sure pass same as device ID
 appKey: "com.sprinklr.messenger.release", // Should be "com.sprinklr.messenger.adhoc" for staging/dev builds.
 themeMode: "DEFAULT", // default value is DEFAULT, options: DEFAULT | DARK
 user: messengerUser,
);
SPRMessenger().takeOff(config: messengerConfig);




### Parameters





















      ``










****````
****``





****``





****````
****``




      ****




| Parameter | Description | Required/Optional |
| --- | --- | --- |
| appId | Unique identifier of the Live Chat app. This will be provided by Sprinklr. | Required |
| environment | This will be provided by Sprinklr. | Required |
| pushAppId | Unique identifier for push notifications. If unsure, use the same value as deviceId. | Optional |
| deviceId | Unique identifier for the device. | Optional |
| skin | Defines the messenger UI skin.         Supported Values: CLASSIC, MODERN         Default Value: MODERN | Optional |
| locale | Sets the language/locale for the messenger.         Default Value: en | Required |
| themeMode | Defines the theme mode.         Supported Values: DEFAULT, DARK         Default Value: DEFAULT | Optional |
| user | Specifies user details. For more details, see the User Object table below. | Required (for authenticated chats) |

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



Map customUser = {
 “customAttribute1”: "value1", //Add your own attribute
 “customAttribute2”: "value2", //Add your own attribute
 “hash”: HmacHashCalculation.generateHash(
    data: "value1_value2", //String
    key: "API_KEY", // This will be provided by Sprinklr
 ),
};
SPRMessengerConfig messengerConfig = SPRMessengerConfig(
 appId: "SPR_APP_ID", // This will be provided by Sprinklr
 environment: "SPR_ENVIRONMENT", // This will be provided by Sprinklr (eg-PROD)
 skin: “MODERN”, // This can be either “CLASSIC” or “MODERN”
 locale: "en", // default value is en
 deviceId: "UNIQUE_DEVICE_ID",
 pushAppId: "SPR_PUSH_ID", // Should be Unique id, if not sure pass same as device ID
 appKey: "com.sprinklr.messenger.release", // Should be "com.sprinklr.messenger.adhoc" for staging/dev builds.
 themeMode: "DEFAULT", // default value is DEFAULT, options: DEFAULT | DARK
 customUser: customUser,
);
SPRMessenger().takeOff(config: messengerConfig);




### Parameters





















      ``










****````
****``





****``





****````
****``




      ****




| Parameter | Description | Required/Optional |
| --- | --- | --- |
| appId | Unique identifier of the Live Chat app. This will be provided by Sprinklr. | Required |
| environment | This will be provided by Sprinklr. | Required |
| pushAppId | Unique identifier for push notifications. If unsure, use the same value as deviceId. | Optional |
| deviceId | Unique identifier for the device. | Optional |
| skin | Defines the messenger UI skin.         Supported Values: CLASSIC, MODERN         Default Value: MODERN | Optional |
| locale | Sets the language/locale for the messenger.         Default Value: en | Required |
| themeMode | Defines the theme mode.         Supported Values: DEFAULT, DARK         Default Value: DEFAULT | Optional |
| customUser | User details containing custom parameters and hash. For more details, see the Custom User Object table below. | Required (for custom users) |

### Custom User Object


























| Parameter | Description | Required/Optional |
| --- | --- | --- |
| Custom Attribute | This is a custom attribute that could be defined by you. You can define multiple custom attributes. | Required |
| hash | To know the steps to generate a hash, see How to generate Hash? | Required |
| hashCreationTime | The timestamp indicating when the hash was generated. Use the same hash creation time that was applied during hash generation to ensure validation. For detailed steps, see How to Generate User Hash. | Required |

## Next Steps

[Launch Live Chat Mobile SDK](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter)

## Additional Resources

See **All Integration Steps**

  [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-flutter) >
  **Initialize** >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-flutter) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-flutter)

  [](https://dev.sprinklr.com/initialize-lc-mobile-sdk-flutter)




[Back to top](https://dev.sprinklr.com/initialize-lc-mobile-sdk-flutter)
