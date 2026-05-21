---
title: "Initialize LC Mobile SDK - Android"
slug: initialize-lc-mobile-sdk-android
url: https://dev.sprinklr.com/initialize-lc-mobile-sdk-android
---

# Initialize LC Mobile SDK - Android

# Initialize Live Chat Mobile SDK - Android


The initialization step starts Sprinklr Messenger within your application by calling the `takeOff` method. This step defines the starting state of the messenger, determining whether the user begins as anonymous, authenticated, or custom.

  The following are the steps for integrating Sprinklr Messenger.
  This page covers the **second step: Initialize**.
  Use the flow below to navigate through all steps of the integration process.

  [Install and Setup](https://dev.sprinklr.com/install-lc-mobile-sdk-android) >
  **Initialize** >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-android) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-android) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android)


**On this page:**



- [Initialize for Anonymous Users](https://dev.sprinklr.com/initialize-lc-mobile-sdk-android#initialize-anonymous-users)

- [Initialize for Authenticated Users](https://dev.sprinklr.com/initialize-lc-mobile-sdk-android#initialize-authenticated-users)

- [Initialize for Custom Authenticated Users](https://dev.sprinklr.com/initialize-lc-mobile-sdk-android#initialize-custom-users)


## Initialize for Anonymous Users

For anonymous users (unauthenticated users), you can initialize the messenger using the `takeOff` method without specifying any user details. Behind the scenes, an anonymous user is automatically created for the messenger and the flow for anonymous user is initialized.


**Dev Notes:**



- The `takeOff` method must be called only once in the application lifecycle.

- For optimal performance, call the `takeOff` method at the root of the application or as early as possible in your application flow.


### Syntax



SPRMessenger sprMessenger = SPRMessenger.shared();
SPRMessengerConfig config = new SPRMessengerConfig();
config.setAppId("SPR_APP_ID"); // This will be provided by sprinklr
config.setDeviceId("UNIQUE_DEVICE_ID");
config.setPushAppId("SPR_PUSH_ID"); //Unique id, if not sure pass same as device ID
config.setEnvironment("SPR_ENVIRONMENT"); // This will be provided by sprinklr (eg PROD2)
config.setLocale("SPR_LOCALE"); // default value is en
config.setSkin("MODERN"); // default value is CLASSIC, options: CLASSIC | MODERN
config.setThemeMode("DEFAULT"); // default value is DEFAULT, options: DEFAULT | DARK
sprMessenger.takeOff(this, config);




### Parameters
























``










****
****





****





****
****




| Parameter | Description | Required/Optional |
| --- | --- | --- |
| appId | Unique identifier of the Live Chat app.         This will be provided by Sprinklr. | Required |
| environment | Environment identifier.         This will be provided by Sprinklr (e.g., PROD2). | Required |
| pushAppId | Unique identifier for push notifications.         If unsure, use the same value as deviceId. | Optional |
| deviceId | Unique identifier for the device. | Optional |
| skin | Defines the messenger UI skin.         Supported Values: CLASSIC, MODERN         Default Value: MODERN | Optional |
| locale | Sets the language/locale for the messenger.         Default Value: en | Required |
| themeMode | Defines the theme mode.         Supported Values: DEFAULT, DARK         Default Value: DEFAULT | Optional |

## Initialize for Authenticated Users

For authenticated users, initialize the messenger using the `takeOff` method with user details. The `takeOff` method will consider the provided user details and initialize the flow accordingly.

Initialization for authenticated users should be performed after the user has successfully logged in and completed the authentication process within your application. After authentication, your application should pass the user object, app ID, and messenger activity details to Sprinklr Messenger so it can begin initialization in the background.  If the user has never logged in before, the system can instead create an anonymous user to allow access to the messenger features.


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










****
****





****





****
****









| Parameter | Description | Required/Optional |
| --- | --- | --- |
| appId | Unique identifier of the Live Chat app.         This will be provided by Sprinklr. | Required |
| environment | Environment identifier.         This will be provided by Sprinklr (e.g., PROD2). | Required |
| pushAppId | Unique identifier for push notifications.         If unsure, use the same value as deviceId. | Optional |
| deviceId | Unique identifier for the device. | Optional |
| skin | Defines the messenger UI skin.         Supported Values: CLASSIC, MODERN         Default Value: MODERN | Optional |
| locale | Sets the language/locale for the messenger.         Default Value: en | Required |
| themeMode | Defines the theme mode.         Supported Values: DEFAULT, DARK         Default Value: DEFAULT | Optional |
| user | Associates the authenticated user object with the messenger configuration. | Required |

**User Object Parameters**





















































| Parameter | Description | Required/Optional |
| --- | --- | --- |
| userId | Unique identifier for the user. | Required |
| firstName | User’s first name. | Required |
| lastName | User’s last name. | Required |
| phoneNumber | User’s phone number. | Optional |
| email | User’s email address. | Optional |
| profileImageUrl | URL of the user’s profile image. | Optional |
| hash | Secure hash generated for the user.         Used for authentication validation. | Required |
| hashCreationTime | Timestamp used during hash generation.         Must match the time used when creating the hash. | Required |

## Initialize for Custom Users

You can define a custom user with custom attributes and pass them to the `takeOff` method. This approach lets you initialize the messenger with personalized attributes or non‑standard user details, giving you flexibility to support custom authentication flows or unique user profiles.


**Dev Notes:**



- The `takeOff` method must be called only once in the application lifecycle.

- For updating the user details or other information in the messenger, you can use the dedicated methods explained in other sections.

- For optimal performance, call the `takeOff` method at the root of the application or as early as possible in your application flow.

- If you want to implement a custom user authentication flow, contact the Sprinklr Support team at [tickets@sprinklr.com](mailto:tickets@sprinklr.com) to discuss the implementation process.


### Syntax



SPRMessenger sprMessenger = SPRMessenger.shared();
SPRMessengerConfig config = new SPRMessengerConfig();
config.setAppId("SPR_APP_ID"); // This will be provided by sprinklr
config.setDeviceId("UNIQUE_DEVICE_ID");
config.setPushAppId("SPR_PUSH_ID");  //Unique id, if not sure pass same as device ID
config.setEnvironment("SPR_ENVIRONMENT"); // This will be provided by sprinklr (eg. PROD2)
config.setSkin("MODERN"); // default value is CLASSIC, options: CLASSIC | MODERN
config.setLocale("SPR_LOCALE"); // default value is en
config.setThemeMode("DEFAULT"); // default value is DEFAULT, options: DEFAULT | DARK
Map customUser = new HashMap<>();
customUser.put("customAttribute1", "value1"); //Add your custom attribute
customUser.put("customAttribute2", "value2"); //Add your custom attribute
customUser.put("hash","8cf5a3815eedc5305b53f2cb8c1785d46a94abe39cfb15bd26d1e1f75e66056a");
customUser.put("hashCreationTime", 1734156789); // should be same that is used in hash generation
config.setCustomUser(customUser);
sprMessenger.takeOff(this, config);




### Parameters
























``










****
****





****





****
****









| Parameter | Description | Required/Optional |
| --- | --- | --- |
| appId | Unique identifier of the Live Chat app.         This will be provided by Sprinklr. | Required |
| environment | Environment identifier.         This will be provided by Sprinklr (e.g., PROD2). | Required |
| pushAppId | Unique identifier for push notifications.         If unsure, use the same value as deviceId. | Optional |
| deviceId | Unique identifier for the device. | Optional |
| skin | Defines the messenger UI skin.         Supported Values: CLASSIC, MODERN         Default Value: MODERN | Optional |
| locale | Sets the language/locale for the messenger.         Default Value: en | Required |
| themeMode | Defines the theme mode.         Supported Values: DEFAULT, DARK         Default Value: DEFAULT | Optional |
| customUser | Map object containing custom user attributes and authentication details. | Required (for authenticated users) |

**Custom User Object**

































| Attribute | Description | Required/Optional |
| --- | --- | --- |
| customAttribute1 | Example of a custom attribute you can define for the user. | Optional |
| customAttribute2 | Example of a custom attribute you can define for the user. | Optional |
| hash | Secure hash generated for the user.         Used for authentication validation. | Required |
| hashCreationTime | Timestamp used during hash generation.         Must match the time used when creating the hash. | Required |

## Next Steps

[Launch Live Chat Mobile SDK](https://dev.sprinklr.com/launch-lc-mobile-sdk-android)

## Additional Resources

See **All Integration Steps**

  [Install and Setup](https://dev.sprinklr.com/install-lc-mobile-sdk-android) >
  **Initialize** >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-android) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-android) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-android)

  [](https://dev.sprinklr.com/initialize-lc-mobile-sdk-android)




[Back to top](https://dev.sprinklr.com/initialize-lc-mobile-sdk-android)
