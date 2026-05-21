---
title: "Advanced Configurations for LC Mobile SDK - iOS"
slug: advanced-configurations-for-lc-mobile-sdk-ios
url: https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios
---

# Advanced Configurations for LC Mobile SDK - iOS

# Advanced Configuration - iOS


After integrating the Live Chat Mobile SDK into your application, you can configure advanced features to further improve the chat experience for your customers.

These options allow you to enable structured logging for better debugging, set up push notifications to keep users informed even when the app is closed, display in-app notifications for real-time updates, and extend functionality with authenticated user flows, co-browsing, and video calling.
Leveraging these advanced capabilities ensures a more reliable, secure, and engaging support experience tailored to your brand’s needs.

  The following are the steps for integrating Sprinklr Messenger.
  This page covers the **fifth step: Advanced Configuration**.
  Use the flow below to navigate through all steps of the integration process.

 [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-ios) >  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios) > **Advanced Configuration (Optional)**


**On this page:**



- [Live Chat Logger](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios#live-chat-logger)

- [Messenger Events Listener](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios#events-listener)

- [Push Notifications](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios#push-notifications)

- [In-App Notifications](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios#in-app-notifications)

- [Taking Video Calls on Messenger](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios#taking-video-calls)

- [Enable SSL Pinning](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios#enable-ssl-pinning)

- [Enable Co-Browsing](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios#enable-co-browsing)


## Live Chat Logger

The Live Chat Logger provides a structured mechanism for capturing and managing real-time SDK events and system logs.
It enables developers to monitor chat interactions, track user actions, and diagnose issues efficiently by logging critical events and system statuses.

### Add Events Logger to SDK Events

To track and manage various events efficiently, the SDK provides a logging system that can be configured according to your requirements.
The logging system supports different log levels to help debug issues effectively.

### Configure the Logger

You can enable logging using the `SPRLoggerConfig` object.

Use the following snippet to enable logging and define custom log transports:


**Dev Notes: ** It is recommended to call `setLoggerConfig` before `takeOff` to avoid missing logs emitted during initialization.

**Swift**

Add logger transport where you have defined your `takeOff` method:



          class ClassName: SPRLoggerTransport



Before calling the `takeOff` method, add `loggerConfig`:



          let loggerConfig = SPRLoggerConfig()
loggerConfig.enableLogs = true // required to enable logs
loggerConfig.level = SPRLogLevel.INFO // optional, default level is SPRLogLevel.INFO
loggerConfig.loggerTransport = self
config.loggerConfig  = loggerConfig



Add a custom logger transport function:



          public func write(_ level: UnsafeMutablePointer, withLogs logs: [Any]) {
  // your custom logger transport
}



**Objective C**

Add logger transport where you have defined your take off method:



          @interface ClassName ()
  >SPRLoggerTransport<
@end



Before calling `takeOff`, add `loggerConfig`: 



          SPRLoggerConfig *loggerConfig =  [[SPRLoggerConfig alloc] init];
loggerConfig.level = SPR_INFO;
loggerConfig.enableLogs = YES;
loggerConfig.loggerTransport = self;
config.loggerConfig = loggerConfig;



Add a custom logger transport function:



          - (void) write:(nonnull SPRLogLevel*)level withLogs:(nonnull NSArray *)logs {
// your custom logger transport
}



### Parameters














      ````





      ````````




      ``
      ``



| Parameter | Required/Optional | Value | Description |
| --- | --- | --- | --- |
| enableLogs | Required | Boolean (true / false) | Enables or disables logging. Must be set to true to record log messages. If false, logging is disabled. |
| level | Optional | Enum (SPRLogLevel) | Sets the logging detail level. Default is SPRLogLevel.INFO. Other levels (e.g., DEBUG, WARN, ERROR) can be used to control verbosity. |
| loggerTransport | Optional | Object implementing write(level, …logs) | Defines a custom transport for logs. The object must implement a write method that receives the log level and log messages. Multiple transports can be defined to handle logs in parallel. |

As is standard with most logging systems, each of these settings also includes all levels below it.
Setting the SDK Logging Level to OFF disables SDK logging entirely.

## Add Messenger Events Listener to SDK Events

The SDK generates a variety of events during its lifecycle, covering areas such as boot process, user sessions, network status, push notifications, conversations, video calls, and more.
By adding an events listener, your application can monitor these events and take appropriate actions whenever they occur.

**Swift**


-
    Add the Messenger delegate in the class where you initialize the SDK with `takeOff`:





class ClassName: SPRMessengerEventsListener






-
    In the class initializer, add the following code after `takeOff`:





let sprMessenger = SPRMessenger.shared()
sprMessenger.eventsListener = self






-
    Add the function to listen for events:





func onEvent(_ eventGroup: String, withEventType eventType: String, andPayload payload: String) {}






**Objective‑C**


-
    At the top of the class, add:





@interface ClassName ()
@end






-
    In the class initializer, add the following code after `takeOff`:





SPRMessenger* sprMessenger = [SPRMessenger shared];
sprMessenger.eventsListener = self;






-
    Add the function to listen for events:





- (void)onEvent:(nonnull NSString *)eventGroup
   withEventType:(nonnull NSString *)eventType
      andPayload:(nonnull NSString *)payload {}






### Parameters













      ``





      ``





      ``





      ``
      ``




      ``
      ````




      ``
      ``````



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| eventGroup | Required | String | Identifies the group or category of the event (e.g., messaging events, connection events). |
| eventType | Required | String | Specifies the type of event within the group (e.g., message received, chat started). |
| payload | Required | String | Contains the event data or details in serialized form (commonly JSON with event-specific information). |
| onEvent | Required | Function | Callback function that handles events triggered by SPRMessengerEventsListener. |
| eventsListener | Required | SPRMessengerEventsListener | Listener object created with SPRMessengerEventsListener that binds the onEvent callback. |
| setMessengerEventsListener | Required | Method | Registers the eventsListener with SPRMessenger so that events are captured and passed to onEvent. |

For supported events, see Supported Events by iOS SDK.

## Push Notifications

Push notifications allow users to receive real-time updates from the Live Chat Messenger, ensuring seamless communication even when the app is running in the background or closed.

### Prerequisites

Before configuring push notifications, ensure you have the APNS (Apple Push Notification Service) certificate (P12) along with its credentials.


**Dev Notes: ** APNS certificate (P12) and its credentials must be different for staging/prod environments. If you are testing the push notification setup on prod mobile application (iOS), ensure to use Android release build.

### Configuration

To enable push notifications, raise a support ticket to [tickets@sprinklr.com](mailto:tickets@sprinklr.com) with the following information:



- APNS certificate (P12) along with its credentials

- Live Chat AppID

- Partner ID

- Env

### Register/Unregister for Push Notifications

You must register the Live Chat Messenger to send and receive push notifications. This requires updating the push token received from APNS (iOS) or FCM (Android).


-
    **Register for Push Notifications**


  -
        **Swift**




SPRMessenger.pushManager().registrationToken = token






  -
        **Objective-C**




[[SPRMessenger pushManager] setRegistrationToken: token];








-
    **Unregister from Push Notifications**

To stop receiving push notifications, unregister by sending an empty token:



  -
        **Swift**




SPRMessenger.pushManager().registrationToken = ""






  -
        **Objective-C**




[[SPRMessenger pushManager] setRegistrationToken: @""];








### Handle Messenger Push Notifications

Once registered, your app may receive push notifications from both messenger and your application. It is essential to correctly identify and handle messenger notifications.


-
    **Identify Messenger Notifications**

Once you’ve registered for Messenger push notifications, your app may receive notifications from both your platform and Messenger. To determine whether a notification originates from Messenger, use the following check:



  -
        **Swift**




let isMessengerNotification = SPRMessenger.pushManager().canHandlePushEvent(userInfo)






  -
        **Objective-C**




BOOL isMessengerNotification = [[SPRMessenger pushManager] canHandlePushEvent: userInfo]








-
    **Displaying Messenger Notifications**

Once you have identified if the notification is a Messenger notification, you need to follow the below step to handle push notification.



  -
        **Swift**




SPRMessenger.pushManager().handlePushEvent(userInfo)






  -
        **Objective-C**




[[SPRMessenger pushManager] handlePushEvent: userInfo]








-
    **Open Messenger on Click of Push Notification**

You can now open the conversation screen directly from a push notification when the app is in the background and the Messenger SDK is mounted.



  -
        **Swift**




SPRMessenger.pushManager().handlePushNotification(userInfo)






  -
        **Objective-C**




[[SPRMessenger pushManager] handlePushNotification: userInfo]








### Open Messenger View with Initial Notification

The Messenger view can be launched directly with an initial notification, either when the app is opened from a push notification or from an in‑app notification banner.

**Swift**



let launchOptions = ["type": "NOTIFICATION", "data": notificationData]
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions);



**Objective-C**



NSDictionary *launchOptions = @{
   @"type": @"NOTIFICATION", @"data":notificationData
};
SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions];



### Controlling Notification Permissions

Before initializing the messenger, you can control whether push notifications are enabled based on the user’s app settings and permission status, provided your app has already obtained notification permission from the user.


**Dev Notes:** Ensure that you complete Step 1 (Disable Push Notifications) and Step 2 (Prevent Auto‑Request for Notification Permissions) before calling `takeOff()`.


-
    **Disable Push Notifications**

To deactivate push notifications according to the user’s application settings, or if the user has not granted notification permission:



  -
        **Swift**




SPRMessenger.pushManager().pushEnabled = false // Disable if app settings are disabled






  -
        **Objective-C**




[[SPRMessenger pushManager] setPushEnabled:NO]; // Disable if app settings are disabled








-
    **Prevent Auto‑Request for Notification Permissions**

The Live Chat application will not request notification permission again once it has already been granted. If your application has not obtained notification permissions, and you also want to prevent the Live Chat application from requesting permission when `takeOff()` is called, set the `autoRequestPermission` parameter to false.



  -
        **Swift**




SPRMessenger.pushManager().autoRequestNotificationPermissions = false // App will not ask the permission for push notifications






  -
        **Objective-C**




[[SPRMessenger pushManager] setAutoRequestNotificationPermissions:NO]; // App will not ask the permission for push notifications








-
    **Enable Push Notifications**

After the user grants notification permission, you must enable push notifications for the Live Chat application by setting `pushEnabled = true`.



  -
        **Swift**




SPRMessenger.pushManager().pushEnabled = true






  -
        **Objective-C**




[[SPRMessenger pushManager] setPushEnabled:YES];








### Customizing Notification Preferences

Brands have the option to customize sound notifications for push notifications. This allows brands to personalize the notification experience by choosing specific sounds that align with their brand identity or user preferences.


**Dev Notes:** To customize push notification sounds, raise a support ticket at
    [tickets@sprinklr.com](mailto:tickets@sprinklr.com) and include the name of the sound file you’ve added to your app assets.


### Notification Grouping and Inline Reply

Live Chat supports a conversation‑aware push notification experience with grouped messages and inline reply support. Users can preview grouped messages, reply directly from the notification bar, or take quick actions such as like, all without opening the app.


-
    **AppDelegate Setup**

To enable inline reply on notifications, register the notification category:





[[SPRNotificationReplyHandler shared] registerNotificationCategory];






-
    **Handle Notification Response**


**Dev Notes: **Ensure `takeOff()` is called before passing notification responses to `SPRNotificationReplyHandler`.





- (void)userNotificationCenter:(UNUserNotificationCenter *)center
 didReceiveNotificationResponse:(UNNotificationResponse *)response
          withCompletionHandler:(void (^)(void))completionHandler {
    [[SPRNotificationReplyHandler shared] handleNotificationResponse:response completionHandler:^{
        if (completionHandler) {
            completionHandler();
        }
    }];
}






-
    **Customize Inline Reply UI**




[[SPRNotificationReplyHandler shared]
    configureReplyTextsWithActionTitle:@""
                       inputPlaceholder:@""
                       inputButtonTitle:@""];







**Dev Notes:**



- Default inline reply labels are localized automatically. For custom labels, localization must be handled by the client application.

- iOS supports notification grouping by default. If you need to disable grouping, this can be configured through a Dynamic Property (DP) setting. To request this change, contact Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).


## In-App Notifications

In‑app notifications are alerts displayed within the mobile application itself, rather than in the device’s main notification tray or lock screen. They are designed to deliver information directly to users while they are actively using the application.

You can either use the:


- Sprinklr-provided Messenger Notification Banner

- Customize the notification view to match your app's design.

### Enable/Disable In-App Notifications

By default, in-app notifications are enabled. To disable or enable in-app notifications again for Sprinklr Live Chat, contact Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com). Be sure to raise separate support tickets for sandbox and production environments.

### Customizing Notification Preferences

For in-app notifications, you can provide a custom notification sound or choose to disable the sound entirely. Follow these steps:


-
    **Customize Sound for Push Notifications**

Brands have the option to enable a custom sound for their In-App notifications.

    **Swift**




let notificationPreferences = SPRNotificationPreferences()
if let soundUri = Bundle.main.path(forResource: "notification_sound", ofType: "mp3"),
   !soundUri.isEmpty {
    notificationPreferences.soundUri = soundUri
}
SPRMessenger.pushManager().setNotificationPreference(notificationPreferences)




    **Objective-C**



          SPRNotificationPreferences *notificationPreferences = [SPRNotificationPreferences new];
NSString *soundUri = [[NSBundle mainBundle] pathForResource:@"notification_sound" ofType:@"mp3"];
if (soundUri != nil && soundUri.length > 0) {
    notificationPreferences.soundUri = soundUri;
}
SPRMessengerPushManager *sprMessengerPushManager = [SPRMessenger pushManager];
[sprMessengerPushManager setNotificationPreference:notificationPreferences];






-
    **Disable Sound**

Brands have the option to disable sound for In-App notifications based on their preferences.

    **Swift**




let notificationPreferences = SPRNotificationPreferences()
notificationPreferences.soundDisabled = true // default value is false
SPRMessenger.pushManager().setNotificationPreference(notificationPreferences)




    **Objective-C**




SPRNotificationPreferences *notificationPreferences = [SPRNotificationPreferences new];
notificationPreferences.soundDisabled = YES; // default value NO
SPRMessengerPushManager* sprMessengerPushManager = [SPRMessenger pushManager];
[sprMessengerPushManager setNotificationPreference:notificationPreferences];






## Taking Video Calls on Messenger

The video calling feature enables brands to connect with customers through video calls directly within the mobile application. These calls can be initiated by agents, providing a more personalized support experience. Sprinklr Live Chat integrates with the AWS Chime service to provide video calling functionality.

Brands can integrate video calling into their mobile apps through Sprinklr Messenger. This guide explains how to integrate and configure video calling in Sprinklr Messenger for React Native using the Amazon Chime SDK.

### Prerequisites

To integrate AWS Chime, ensure the following prerequisites are met:


- AWS account with the Chime SDK enabled.

- If you want to enable video recording, you need an S3 bucket associated with your AWS account to store Chime-side recordings.

- AWS account number to process video call recordings.

- Permission to access Care Console in the Sprinklr platform.

- You can enable AWS Chime account to make and receive video calls by reaching out to Sprinklr support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

### Pricing

The following are the pricing details:


- AWS has usage-based pricing, with costs calculated per minute per participant. For example, a call between an agent and a customer counts as 2 participants.

- AWS charges $0.0017 per minute per attendee (one attendee is an agent and the other is a customer).

- If you choose to enable video call recording, AWS will add separate pricing for recording using the media capture pipeline which is around $0.0034 per minute (irrespective of number of attendees).

For more details, you can refer to [Amazon Chime SDK pricing](https://aws.amazon.com/chime/chime-sdk/pricing/).

### Video Call Recording

You can choose whether or not to record video calls. If you decide to enable video call recording, note the following clarifications:


- Video call recordings are stored on your AWS Chime account S3 bucket.

- Video call recordings are also stored on Sprinklr AWS S3, which allows you to view them in the Sprinklr platform.


**Dev Notes:** For the integration, Step 6 is mandatory.

### Integration Steps

**Install Chime-related dependencies**

**Dev Notes: **If you installed the Live Chat SDK using Swift Package Manager, all Chime-related dependencies are automatically installed. You can therefore skip this step and proceed directly to the next steps.

Add `SPRMessengerClientChimeVideoSDK` to your Podfile. Then, run the following code:



          pod install
target :YourTargetName do
  pod 'SPRMessengerClientChimeVideoSDK',
      :podspec => 'https://clients-external-cocoapods.sprinklr.com/SPRMessengerClientChimeVideoSDK/15.0.0/SPRMessengerClientChimeVideoSDK.podspec'
end



### Setup VoIP Push Notifications

To display incoming video calls, Sprinklr relies on the call kit infrastructure provided by iOS that offers an experience of a real call. This also gives users access to control actions such as end call, mute call and other call kit actions from both the video call UI as well as the call kit UI. To leverage this, Sprinklr uses VoIP push notifications which helps users to receive calls on their devices.

To setup VoIP push notifications, follow these steps:


-
    **Add PushKit into your app**

Implement Apple's [PushKit API](https://developer.apple.com/documentation/pushkit) directly into your app to obtain a VoIP token. For more detailed guidance on setting this up, see [Apple's VoIP Best Practices](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/OptimizeVoIP.html).



-
    **Generate VoIP Certificate**

The certificate generated must be a VoIP Services Certificate. You must use the same bundle ID for the VoIP certificate as you do for your main app. For more information, see [Creating VoIP Certificates](https://developer.apple.com/help/account/certificates/create-voip-services-certificates/).



-
    **Share Certificate with Sprinklr**

Share the generated VoIP Certificate in `.p12` format with Sprinklr along with its password.



### Register/Unregister for VoIP Push Notifications


-
    **Register VoIP Token**

Inside `didUpdatePushCredentials`, add the following code:

    **Swift**




func pushRegistry(_ registry: PKPushRegistry, didUpdate pushCredentials: PKPushCredentials, for type: PKPushType) {
    SPRMessenger.voipPushManager().didUpdate(pushCredentials, forType: type.rawValue)
}




    **Objective-C**




- (void)pushRegistry:(PKPushRegistry *)registry didUpdatePushCredentials:(PKPushCredentials *)pushCredentials forType:(PKPushType)type {
    [[SPRMessenger voipPushManager] didUpdatePushCredentials:pushCredentials forType:(NSString *)type];
}






-
    **Unregister VoIP Token**

Inside `didInvalidatePushTokenForType`, add the following code:

    **Swift**




func pushRegistry(_ registry: PKPushRegistry, didInvalidatePushTokenFor type: PKPushType) {
    SPRMessenger.voipPushManager().didInvalidatePushToken(forType: type.rawValue)
}




    **Objective-C**




- (void)pushRegistry:(PKPushRegistry *)registry didInvalidatePushTokenForType:(PKPushType)type {
    [[SPRMessenger voipPushManager] didInvalidatePushTokenForType:(NSString *)type];
}






### Handle VoIP Notifications

Send VoIP Notification to Messenger SDK if its type belongs to messenger.

Inside `didReceiveIncomingPushWithPayload`, add following code:

**Swift**



          func pushRegistry(_ registry: PKPushRegistry,
                  didReceiveIncomingPushWith payload: PKPushPayload,
                  for type: PKPushType,
                  completion: @escaping () -> Void) {
    if SPRMessenger.voipPushManager().canHandleVoipPushEvent(payload) {
        SPRMessenger.voipPushManager().handleVoipPushEvent(payload,
                                                           forType: type,
                                                           completion: completion)
    }
}



**Objective-C**



          - (void)pushRegistry:(PKPushRegistry *)registry
didReceiveIncomingPushWithPayload:(PKPushPayload *)payload
             forType:(PKPushType)type
withCompletionHandler:(void (^)(void))completion {
    if ([[SPRMessenger voipPushManager] canHandleVoipPushEvent:payload]) {
        [[SPRMessenger voipPushManager] handleVoipPushEvent:payload
                                                   forType:type
                                                completion:completion];
        return;
    }
    // Add your custom code
}



### Pass Video Call Provider to SPRMessengerConfig

Create config for `takeOff` as done in the Initialization step and pass `videoCallProvider` in the config.

**Swift**



          import SPRMessengerClient
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
    let config = SPRMessengerConfig()
    config.appId = "SPR_APP_ID" // This will be provided by Sprinklr
    config.pushAppId = "SPR_PUSH_ID" // Should be unique, if not sure pass same as device ID
    config.deviceId = "UNIQUE_DEVICE_ID"
    config.environment = "SPR_ENVIRONMENT" // Provided by Sprinklr (e.g., PROD2)
    config.locale = "SPR_LOCALE" // Default value is en
    config.themeMode = "DEFAULT" // Default value is DEFAULT, options: DEFAULT | DARK
    config.videoCallProvider = SPRAmazonChimeProvider
    SPRMessenger.takeOff(config)
}



**Objective-C**



          #import
#import
#import
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    SPRMessengerConfig *config = [SPRMessengerConfig new];
    config.appId = @"SPR_APP_ID"; // This will be provided by Sprinklr
    config.pushAppId = @"SPR_PUSH_ID"; // Should be unique, if not sure pass same as device ID
    config.deviceId = @"UNIQUE_DEVICE_ID";
    config.environment = @"SPR_ENVIRONMENT"; // Provided by Sprinklr (e.g., PROD2)
    config.locale = @"SPR_LOCALE"; // Default value is en
    config.themeMode = @"DEFAULT"; // Default value is DEFAULT, options: DEFAULT | DARK
    config.videoCallProvider = SPRAmazonChimeProvider;
    [SPRMessenger takeOff:config];
}



**Parameters**





































      ``






****````
****``




      ``




| Parameter | Required/Optional | Description | Type (Swift / Objective‑C) |
| --- | --- | --- | --- |
| appId | Required | Application ID provided by Sprinklr. | String / NSString |
| pushAppId | Required | Unique Push ID. If unsure, use the same as the device ID. | String / NSString |
| deviceId | Required | Unique identifier for the device. | String / NSString |
| environment | Required | Environment provided by Sprinklr. For example, PROD2. | String / NSString |
| locale | Optional | Language/locale setting. Default is en. | String / NSString |
| themeMode | Optional | String / NSString |  |
| videoCallProvider | Optional | Video call provider integration. For example, SPRAmazonChimeProvider. | Constant / Constant |

## Enable SSL Pinning

To enhance security, you can enable SSL Pinning in your application. Sprinklr provides the Public Key, which must be configured by creating an `SPRSSLPinningConfig` object and attaching it to your `SPRMessengerConfig`. This ensures that all communication between the app and Sprinklr servers is validated against the pinned key.


**Dev Notes:** To generate or obtain the Public Key, contact Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

### Syntax

**Swift**



          import SPRMessengerClient
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
    let config = SPRMessengerConfig()
    config.appId = "SPR_APP_ID" // This will be provided by Sprinklr
    config.pushAppId = "SPR_PUSH_ID" // Should be unique, if not sure pass same as device ID
    config.deviceId = "UNIQUE_DEVICE_ID"
    config.environment = "SPR_ENVIRONMENT" // Provided by Sprinklr (e.g., PROD2)
    config.locale = "SPR_LOCALE" // Default value is en
    config.skin = "MODERN" // Default value is CLASSIC, options: CLASSIC | MODERN
    config.themeMode = "DEFAULT" // Default value is DEFAULT, options: DEFAULT | DARK
    let sslPinningConfig = SPRSSLPinningConfig()
    sslPinningConfig.enabled = true
    sslPinningConfig.publicKey = "SPR_PUBLIC_KEY" // This will be provided by Sprinklr
    config.sslPinningConfig = sslPinningConfig
    SPRMessenger.takeOff(config)
} 



**Objective-C**



          #import
#import
#import
- (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    SPRMessengerConfig *config = [SPRMessengerConfig new];
    config.appId = @"SPR_APP_ID"; // This will be provided by Sprinklr
    config.pushAppId = @"SPR_PUSH_ID"; // Should be unique, if not sure pass same as device ID
    config.deviceId = @"UNIQUE_DEVICE_ID";
    config.environment = @"SPR_ENVIRONMENT"; // Provided by Sprinklr (e.g., PROD2)
    config.locale = @"SPR_LOCALE"; // Default value is en
    config.skin = @"MODERN"; // Default value is CLASSIC, options: CLASSIC | MODERN
    config.themeMode = @"DEFAULT"; // Default value is DEFAULT, options: DEFAULT | DARK
    SPRSSLPinningConfig *sslPinningConfig = [[SPRSSLPinningConfig alloc] init];
    sslPinningConfig.enabled = YES;
    sslPinningConfig.publicKey = @"SPR_PUBLIC_KEY"; // This will be provided by Sprinklr
    config.sslPinningConfig = sslPinningConfig;
    [SPRMessenger takeOff:config];
} 



### Parameters





































      ``






****````
****``






****````
****``





      ````





      ``




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| appId | Required | Application ID provided by Sprinklr. | String / NSString |
| pushAppId | Required | Unique Push ID. If unsure, use the same as the device ID. | String / NSString |
| deviceId | Required | Unique identifier for the device. | String / NSString |
| environment | Required | Environment provided by Sprinklr. For example, PROD2. | String / NSString |
| locale | Optional | Language/locale setting. Default is en. | String / NSString |
| skin | Optional | UI skin mode.Supported Values: CLASSIC \| MODERNDefault Value: CLASSIC. | String / NSString |
| themeMode | Optional | UI theme mode.Supported Values: DEFAULT \| DARKDefault Value: DEFAULT | String / NSString |
| sslPinningConfig | Optional | SSL Pinning configuration object. Contains enabled (Boolean/BOOL) and publicKey (String/NSString). | Object |
| videoCallProvider | Optional | Video call provider integration. For example, SPRAmazonChimeProvider. | Constant |

## Enable Co-Browsing

Co-browsing will allow agents to get full visibility into the customer’s screen, enabling them to guide customers through product purchases, complex form filling, or confusing information on mobile application. For more details, please refer here.

### Prerequisites

To enable co-browsing, raise a support ticket at [tickets@sprinklr.com](mailto:tickets@sprinklr.com) with the following details:


- Partner Name

- Partner ID

- Concurrent co-browsing sessions expected

- Number of agents who will be using co-browsing

### Install Co-Browsing Related Dependencies

To install co-browsing related dependencies, follow these steps:


-

Add `SPRMessengerClientCobrowseSDK` to your Podfile and run the following code:




          pod install
target :YourTargetName do
pod 'SPRMessengerClientCobrowseSDK', :podspec => 'https://clients-external-cocoapods.sprinklr.com/SPRMessengerClientCobrowseSDK/15.0.0/SPRMessengerClientCobrowseSDK.podspec'
end








- Create config for `takeOff` and pass co-browsing flag:

**Swift**



          import SPRMessengerClient
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
    let config = SPRMessengerConfig()
    config.appId = "SPR_APP_ID" // Provided by Sprinklr
    config.pushAppId = "SPR_PUSH_ID" // Unique ID, if unsure use device ID
    config.deviceId = "UNIQUE_DEVICE_ID"
    config.environment = "SPR_ENVIRONMENT" // Provided by Sprinklr (e.g., PROD2)
    config.locale = "SPR_LOCALE" // Default value is en
    config.skin = "MODERN" // Default value is CLASSIC, options: CLASSIC | MODERN
    config.themeMode = "DEFAULT" // Default value is DEFAULT, options: DEFAULT | DARK
    config.isCobrowsingEnabled = true
    SPRMessenger.takeOff(config)
}







**Objective-C**



          #import
#import
#import
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    SPRMessengerConfig *config = [SPRMessengerConfig new];
    config.appId = @"SPR_APP_ID"; // Provided by Sprinklr
    config.pushAppId = @"SPR_PUSH_ID"; // Unique ID, if unsure use device ID
    config.deviceId = @"UNIQUE_DEVICE_ID";
    config.environment = @"SPR_ENVIRONMENT"; // Provided by Sprinklr (e.g., PROD2)
    config.locale = @"SPR_LOCALE"; // Default value is en
    config.skin = @"MODERN"; // Default value is CLASSIC, options: CLASSIC | MODERN
    config.themeMode = @"DEFAULT"; // Default value is DEFAULT, options: DEFAULT | DARK
    config.isCobrowsingEnabled = YES;
    [SPRMessenger takeOff:config];
}








### Parameters





































      ``





      ``````





      ``````





      ``




| Parameter | Required/Optional | Description | Type (Swift / Objective‑C) |
| --- | --- | --- | --- |
| appId | Required | Application ID provided by Sprinklr. | String / NSString |
| pushAppId | Required | Unique Push ID. If unsure, use the same as the device ID. | String / NSString |
| deviceId | Required | Unique identifier for the device. | String / NSString |
| environment | Required | Environment provided by Sprinklr. For example, PROD2. | String / NSString |
| locale | Optional | Language/locale setting. Default is en. | String / NSString |
| skin | Optional | UI skin mode. Supported Values: CLASSIC \| MODERN. Default Value: CLASSIC. | String / NSString |
| themeMode | Optional | UI theme mode. Supported Values: DEFAULT \| DARK. Default Value: DEFAULT. | String / NSString |
| isCobrowsingEnabled | Optional | Flag to enable co‑browsing functionality. Default is false. | Boolean / BOOL |

### Full Device Screen Sharing Support

Full device screen sharing lets support agents view the entire device screen, including apps outside your own. This helps them check system settings or guide users as they switch between different applications.

To enable this feature, refer to [Full device screen sharing](https://docs.cobrowse.io/sdk-features/full-device-capabilities/full-device-screen-sharing#ios) documentation.

### Redaction Support

When remotely viewing a user's screen, there may be certain sensitive data that should not be viewable by the agent. For this purpose, Live Chat SDK supports redaction that automatically blocks out on device all sensitive data sources such as credit cards, social security numbers, etc. When certain data is redacted, it will never leave the user's device.

To enable this feature, refer to [Redact sensitive data](https://docs.cobrowse.io/sdk-features/redact-sensitive-data#ios) documentation.

## Additional Resources

See **All Integration Steps**
 [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-ios) > [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-ios)

  [](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios)




[Back to top](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios)
