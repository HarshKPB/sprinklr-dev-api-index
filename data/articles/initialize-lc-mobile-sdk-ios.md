---
title: "Initialize LC Mobile SDK - iOS"
slug: initialize-lc-mobile-sdk-ios
url: https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios
---

# Initialize LC Mobile SDK - iOS

# Initialize Live Chat Mobile SDK - iOS


Initialization sets up the app environment and establishes the user context (anonymous, authenticated, or custom). The takeOff method is the entry point for this process, enabling you to initialize the SDK for different types of users such as anonymous, authenticated, or custom authenticated, depending on your app’s requirements.

  The following are the steps for integrating Sprinklr Messenger.
  This page covers the **second step: Initialize**.
  Use the flow below to navigate through all steps of the integration process.

 [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-ios) >  **Initialize** > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios)


**On this page:**



- [Initialize for Anonymous Users](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios#initialize-anonymous-users)

- [Initialize for Authenticated Users](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios#initialize-authenticated-users)

- [Initialize for Custom Authenticated Users](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios#initialize-custom-users)


## Initialize for Anonymous Users

For anonymous users (unauthenticated users), you can initialize the messenger using the `takeOff` method without specifying any user details. Behind the scenes, an anonymous user is automatically created for the messenger and the flow for anonymous user is initialized.


**Dev Notes: **The `takeOff` method must be called only once in the application lifecycle. For optimal performance, call the `takeOff` method at the root of the application or as early as possible in your application flow.

You can use separate methods for updating the user or other information in the messenger, which are explained in other sections.

### Syntax

**Swift**



import SPRMessengerClient
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        let config = SPRMessengerConfig();
        config.appId = "SPR_APP_ID" // This will be provided by sprinklr
        config.pushAppId = "SPR_PUSH_ID"; // Should be Unique id, if not sure pass same as device ID
        config.deviceId = "UNIQUE_DEVICE_ID"; // unique key
        config.environment = "SPR_ENVIRONMENT"; // This will be provided by sprinklr (eg. PROD2)
        config.locale = "SPR_LOCALE"; // default value is en
        config.skin = "MODERN"; // default value is MODERN, options: CLASSIC | MODERN
         config.themeMode = "DEFAULT"; // default value is DEFAULT, options: DEFAULT | DARK
        SPRMessenger.takeOff(config)
}




**Objective-C**



#import
#import
#import
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  SPRMessengerConfig *config = [SPRMessengerConfig new];
  config.appId = @"SPR_APP_ID"; // This will be provided by sprinklr
  config.pushAppId = @"SPR_PUSH_ID"; // Should be Unique id, if not sure pass same as device ID
  config.deviceId = @"UNIQUE_DEVICE_ID";
  config.environment = @"SPR_ENVIRONMENT"; // This will be provided by sprinklr (eg. PROD2)
  config.locale = @"SPR_LOCALE"; // default value is en
  config.skin = @"MODERN"; // default value is MODERN, options: CLASSIC | MODERN
  config.themeMode = @"DEFAULT";  // default value is DEFAULT, options: DEFAULT | DARK
  [SPRMessenger takeOff:config];
}




### Parameters















****````
****``

****````
****``


| Parameter | Description | Required/Optional |
| --- | --- | --- |
| appId | Unique identifier of the Live Chat app. Provided by Sprinklr. | Required |
| environment | Environment provided by Sprinklr (e.g., PROD2). | Required |
| locale | Language/locale for the messenger. Default: en. | Required |
| pushAppId | Unique identifier for push notifications. If unsure, use same as deviceId. | Optional |
| deviceId | Unique identifier for the device. | Optional |
| skin | Messenger UI skin.Supported Values: CLASSIC, MODERN. Default: MODERN. | Optional |
| themeMode | Theme mode.Supported Values: DEFAULT, DARK. Default: DEFAULT. | Optional |

## Initialize for Authenticated Users

After a user successfully logs in and completes authentication, you must initialize the Sprinklr Messenger SDK with the authenticated user’s details. This includes passing the application ID along with a user object containing information such as id, firstName, lastName, profileImageUrl, phoneNo, email.


**Dev Notes: **The `takeOff` method must be called only once in the application lifecycle. For optimal performance, call it at the root of the application or as early as possible in your application flow.

### Syntax

**Swift**



import SPRMessengerClient
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        let config = SPRMessengerConfig();
        config.appId = "SPR_APP_ID" // This will be provided by sprinklr
        config.pushAppId = "SPR_PUSH_ID"; // Should be Unique id, if not sure pass same as device ID
        config.deviceId = "UNIQUE_DEVICE_ID";
        config.environment = "SPR_ENVIRONMENT"; // This will be provided by sprinklr (eg. PROD2)
        config.locale = "SPR_LOCALE"; // default value is en
        config.skin = "MODERN"; // default value is MODERN, options: CLASSIC | MODERN
         config.themeMode = "DEFAULT"; // default value is DEFAULT, options: DEFAULT | DARK
        let user = SPRMessengerUser();
        user.id = "12345";
        user.firstName = "John";
        user.lastName = "Doe";
        user.phoneNo = "9876543210";
        user.email = "John.Doe@example.com";
        user.profileImageUrl = "https://example.com/profilePic.jpg";
        user.hashValue = "f30c3b0835ecd378a134c74bce8cea866df8c5b6e12a8c219c9bb288f7270e22";
        user.hashCreationTime = 1734156789; // should be the same one that is used for generating the hash
        config.user = user;
        SPRMessenger.takeOff(config)
}




**Objective-C**



#import
#import
#import
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  SPRMessengerConfig *config = [SPRMessengerConfig new];
  config.appId = @"SPR_APP_ID"; // This will be provided by sprinklr
  config.pushAppId = @"SPR_PUSH_ID"; // Should be Unique id, if not sure pass same as device ID
  config.deviceId = @"UNIQUE_DEVICE_ID";
  config.environment = @"SPR_ENVIRONMENT"; // This will be provided by sprinklr (eg. PROD2)
  config.locale = @"SPR_LOCALE"; // default value is en
  config.skin = @"MODERN"; // default value is MODERN, options: CLASSIC | MODERN
  config.themeMode = @"DEFAULT"; // default value is DEFAULT, options: DEFAULT | DARK
  SPRMessengerUser *user = [SPRMessengerUser new];
  user.id = @"12345";
  user.firstName = @"John";
  user.lastName = @"Doe";
  user.phoneNo = @"9876543210";
  user.email = @"John.Doe@example.com";
  user.profileImageUrl = @"https://example.com/profilePic.jpg";
  user.hashValue = @"f30c3b0835ecd378a134c74bce8cea866df8c5b6e12a8c219c9bb288f7270e22";
  user.hashCreationTime = @(1734156789); // should be the same one that is used for generating the hash
  config.user = user;
  [SPRMessenger takeOff:config];
}




### Parameters















****````
****``


****````
****``


| Parameter | Description | Required/Optional |
| --- | --- | --- |
| appId | Unique identifier of the Live Chat app. Provided by Sprinklr. | Required |
| environment | Environment provided by Sprinklr. | Required |
| user | User details object. | Required (for authenticated chats) |
| pushAppId | Unique identifier for push notifications. | Optional |
| deviceId | Unique identifier for the device. | Optional |
| skin | Messenger UI skin.Supported Values: CLASSIC, MODERN. Default: MODERN. | Optional |
| locale | Language/locale. Default: en. | Required |
| themeMode | Theme mode.Supported Values: DEFAULT, DARK. Default: DEFAULT. | Optional |

### User Object



















| Parameter | Description | Required/Optional |
| --- | --- | --- |
| userId | Unique identifier of the user. | Required |
| firstName | First name of the user. | Optional |
| lastName | Last name of the user. | Optional |
| phoneNo | Phone number of the user. | Optional |
| email | Email ID of the user. | Optional |
| profileImageUrl | URL to profile image. | Optional |
| hash | Generated hash for validation. | Required |
| hashCreationTime | Timestamp of hash generation. Must match the time used for generating the hash. | Required |

## Initialize for Authenticated Custom Users

To create a custom authenticated user account, you can pass custom attributes to the Sprinklr Messenger SDK. This allows you to define user accounts with personalized details beyond the standard fields.


**Dev Notes: **Provide the custom attributes along with a hash and its creation time in the configuration object. The `takeOff` method must be called only once in the application lifecycle. For custom authentication flows, contact Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

### Syntax

**Swift**



let config = SPRMessengerConfig();
config.appId = "SPR_APP_ID" // This will be provided by sprinklr
config.pushAppId = "SPR_PUSH_ID"; // Should be Unique id, if not sure pass same as device ID
config.deviceId = "UNIQUE_DEVICE_ID";
config.environment = "SPR_ENVIRONMENT"; // This will be provided by sprinklr (eg. PROD2)
config.locale = "SPR_LOCALE"; // default value is en
config.skin = "MODERN"; // default value is MODERN, options: CLASSIC | MODERN
config.themeMode = "DEFAULT"; // default value is DEFAULT, options: DEFAULT | DARK
config.customUser = ["customAttribute1": "value1", "customAttribute2": "value2", "hash": "8cf5a3815eedc5305b53f2cb8c1785d46a94abe39cfb15bd26d1e1f75e66056a", "hashCreationTime":1734156789]  // Add your custom attributes and hashCreationTime should be the same one that is used for generating the hash
SPRMessenger.takeOff(config);




**Objective-C**



SPRMessengerConfig *config = [[SPRMessengerConfig alloc] init];
  config.appId = @"SPR_APP_ID"; // This will be provided by sprinklr
  config.pushAppId = @"SPR_PUSH_ID"; // Should be Unique id, if not sure pass same as device ID
  config.deviceId = @"UNIQUE_DEVICE_ID";
  config.environment = @"SPR_ENVIRONMENT"; // This will be provided by sprinklr (eg. PROD2)
  config.locale = @"SPR_LOCALE"; // default value is en
  config.skin = @"MODERN"; // default value is MODERN, options: CLASSIC | MODERN
  config.themeMode = @"DEFAULT";  // default value is DEFAULT, options: DEFAULT | DARK
config.customUser = @{@"customAttribute1": @"value1", @"customAttribute2": @"value2", @"hash": @"8cf5a3815eedc5305b53f2cb8c1785d46a94abe39cfb15bd26d1e1f75e66056a", @"hashCreationTime": @(1734156789)}  // Add your custom attributes and hashCreationTime should be the same one that is used for generating the hash
[SPRMessenger takeOff:config];




### Parameters














****````
****``


****````
****``
    ****


| Parameter | Description | Required/Optional |
| --- | --- | --- |
| appId | Unique identifier of the Live Chat app. | Required |
| environment | Environment provided by Sprinklr. | Required |
| pushAppId | Unique identifier for push notifications. | Optional |
| deviceId | Unique identifier for the device. | Optional |
| skin | Messenger UI skin.Supported Values: CLASSIC, MODERN. Default: MODERN. | Optional |
| locale | Language/locale. Default: en. | Required |
| themeMode | Theme mode.Supported Values: DEFAULT, DARK. Default: DEFAULT. | Optional |
| customUser | Object containing custom parameters and hash. See the Custom User Object table below. | Required (for custom users) |

### Custom User Object














| Parameter | Description | Required/Optional |
| --- | --- | --- |
| Custom Attribute | Custom attributes defined by you. Multiple attributes can be added. | Required |
| hash | Generated hash for validation. | Required |
| hashCreationTime | Timestamp of hash generation. Must match the time used for generating the hash. | Required |

## Next Steps

[Launch Live Chat Mobile SDK](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios)

## Additional Resources

See **All Integration Steps**
 [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-ios) >  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-react-native)

  [](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native)




[Back to top](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native)
