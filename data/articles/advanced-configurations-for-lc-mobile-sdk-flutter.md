---
title: "Advanced Configurations for LC Mobile SDK - Flutter"
slug: advanced-configurations-for-lc-mobile-sdk-flutter
url: https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter
---

# Advanced Configurations for LC Mobile SDK - Flutter

# Advanced Configuration - Flutter


After integrating the Live Chat Mobile SDK into your application, you can configure advanced features to further enhance the customer experience, including enabling logging for better debugging, setting up notifications, and activating capabilities such as co-browsing and video calling.

  The following are the steps for integrating Sprinklr Messenger.
  This page covers the **fifth step: Advanced Configuration**.
  Use the flow below to navigate through all steps of the integration process.

  [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-flutter) >
  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-flutter) >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-flutter) >
  **Advanced Configuration (Optional)**


**On this page:**



- [Live Chat Logger](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter#live-chat-logger)

- [Add Messenger Events Listener](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter#events-listener)

- [Push Notifications](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter#push-notifications)

- [Enable Co-Browsing](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter#enable-co-browsing)


## Live Chat Logger

The Live Chat Logger provides a structured mechanism for capturing and managing real-time SDK events and system logs. It enables developers to monitor chat interactions, track user actions, and diagnose issues efficiently by logging critical events and system statuses. The logging system supports different log levels to help debug issues effectively.

### Configure the Logger

You can enable logging in the Flutter Live Chat SDK using the `SPRLoggerConfig` object.

Use the following snippet to enable logging and define custom log transports:


**Dev Notes: ** It is recommended to call `setLoggerConfig` before `takeOff` to avoid missing logs emitted during initialization.



void _write(SPRLogLevel level, List logs) {
  // your custom logger transport
}
SPRLoggerTransport _loggerTransport = SPRLoggerTransport(
  write: _write,
);
SPRLoggerConfig _loggerConfig = SPRLoggerConfig(
  enableLogs: true, // required to enable logs
  level: SPRLogLevel.SPR_INFO, // optional, default level is SPRLogLevel.SPR_INFO
  loggerTransport: _loggerTransport, // required to set flutter logger transport
);
SPRMessengerConfig messengerConfig = SPRMessengerConfig(
  // other config
  loggerConfig: _loggerConfig,
);



### Parameters














      ********





      ****





      ****
**
**




| Parameter | Required/Optional | Value | Description |
| --- | --- | --- | --- |
| enableLogs | Required | Boolean (true/false) | This parameter is required to enable or disable logging.          When set to true, logging is enabled, allowing the application to record log messages.          If set to false, logging is disabled. |
| logLevel | Optional | Integer (0 to 7) | This parameter sets the level of logging detail.          The default value is 4, which corresponds to the INFO level.          Refer to the table below for more details on Log Level. |
| transports | Optional | List of objects with a write method | write(level, …logs){}         level: Level of the log         …logs: List of logs as strings         This parameter allows defining multiple transporters that get called in parallel. |

**Dev Notes: **Each logging level automatically includes all levels beneath it. Additionally, setting the SDK Logging Level to OFF disables logging entirely.

## Add Messenger Events Listener to SDK Events

Register a custom event listener to capture and handle SDK messenger events.

### Register an Events Listener


**Dev Notes: ** It is recommended to call `registerEventsListener` before `takeOff` to avoid missing events during initialization.



void onEvent(String eventGroup, String eventType, String payload) {
  // Your function body
}
SPRMessengerEventsListener eventsListener = SPRMessengerEventsListener(
  onEvent: onEvent,
);
SPRMessenger().setMessengerEventsListener(
  eventsListener: eventsListener,
);



### Parameters



























      ``




      ````




      ``````



| Parameter | Required/Optional | Description |
| --- | --- | --- |
| eventGroup | Required | Identifies the group or category of the event. |
| eventType | Required | Specifies the type of event within the group. |
| payload | Required | Contains the event data or details in serialized form (commonly JSON with event-specific information). |
| onEvent | Required | Callback function that handles events triggered by SPRMessengerEventsListener. |
| eventsListener | Required | Listener object created with SPRMessengerEventsListener that binds the onEvent callback. |
| setMessengerEventsListener | Required | Registers the eventsListener with SPRMessenger so that events are captured and passed to onEvent. |

For supported events, see Common Resources.

## Push Notifications

Push notifications allow users to receive real-time updates from the Live Chat Messenger, ensuring seamless communication even when the app is running in the background or closed.

**Dev Notes: **If you are using push notifications for Android, ensure that `app/res/drawable` has `notification_icon.png` before the `takeOff` method is called.

### Prerequisites

Before configuring push notifications, ensure you have the following:

#### Android


- Google `service.json` file (specific to each environment - staging/production).

-
    Refer to the document below to know how to set up the `service.json` file:

    [Service.json file setup.pdf](https://prod2-sprcdn-assets.sprinklr.com/50400/10c76274-613c-4f90-a16b-d8a76a3808cf-1361481284/Service.json_file_setup.pdf)



**Dev Notes: ** The `service.json` file may or may not be environment‑specific, depending on your organization’s setup.

#### iOS


- APNS certificate (`.p12` format) and its credentials (specific to each environment - staging/production)


**Dev Notes:**



- The Google `service.json` file must match the respective environment (staging/production).

- The APNS certificate (`.p12` or P8 Key) and its credentials must be different for staging and production environments.

- If testing push notifications on a production iOS application, use a TestFlight build.

- If the Google `service.json` file differs between sandbox/production and you are testing on a production mobile application, ensure you use an Android release build.

- If using a different Google `service.json` file for sandbox/production, ensure TestFlight is used when testing on production (Android).


### Configuration

To enable push notifications, raise a support ticket to [tickets@sprinklr.com](mailto:tickets@sprinklr.com) with the following information:


- Google `service.json` file (for Android)

- APNS certificate (`.p12`) and credentials (for iOS) OR P8 Certificate with Key, BundleId, TeamId

- Live Chat App ID

- Partner ID

- Environment

### Step 1: Register/Unregister for Push Notifications

You must register the Live Chat Messenger to send and receive push notifications. This requires updating the push token received from APNS (iOS) or FCM (Android).


**Dev Notes: ** Call this only after `takeOff` is completed or Live Chat is initialized.

#### Register for Push Notifications

**Android**



SPRMessenger().setPushRegistrationToken(token: token);



**iOS**

In your `ios/AppDelegate.swift` file, add the following code to register for push notifications:



import SPRMessengerClient
@main
@objc class AppDelegate: FlutterAppDelegate {
  // other methods
  override func application(
    _ application: UIApplication,
    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
  ) {
    // Convert token to string
    let token = deviceToken.map { String(format: "%02.2hhX", $0) }.joined()
    // Pass to push manager
    SPRMessenger.pushManager().registrationToken = token
  }
}



#### Unregister from Push Notifications

To stop receiving push notifications, unregister by sending an empty token:

**Android**



SPRMessenger().setPushRegistrationToken(token: "");



**iOS**

In your `ios/AppDelegate.swift` file, add the following code to register for push notifications:



SPRMessenger.pushManager().registrationToken = ""



### Step 2: Handle Messenger Notifications

**Android**

Once you have registered for messenger push notifications, you might receive notifications from both your platform and the messenger. To check if a notification is from the messenger, use the following:




bool isMessengerNotification = await SPRMessenger().canHandlePushEvent(
  message: remoteData
);
// remoteData is FCM RemoteMessage received in onBackgroundMessage of Firebase messaging service






If the notification is a messenger notification, follow the step below to handle the push notification:




SPRMessenger().handlePushEvent(message: remoteData);






You can now open the conversation screen directly from a push notification when the app is in the background and the Messenger SDK is mounted:




SPRMessenger().handlePushNotification(message: remoteMessage);






**iOS**

Make sure that appropriate notification permissions are granted for the application:




import SPRMessengerClient
@main
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didReceiveRemoteNotification userInfo: [AnyHashable : Any],
    fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
  ) {
    if SPRMessenger.pushManager().canHandlePushEvent(userInfo) {
      SPRMessenger.pushManager().handlePushEvent(userInfo)
    }
    completionHandler(.noData)
  }
  override func userNotificationCenter(
    _ center: UNUserNotificationCenter,
    didReceive response: UNNotificationResponse,
    withCompletionHandler completionHandler: @escaping () -> Void
  ) {
    let userInfo = response.notification.request.content.userInfo
    if SPRMessenger.pushManager().canHandlePushEvent(userInfo) {
      SPRMessenger.pushManager().handlePushEvent(userInfo)
    }
    completionHandler()
  }
}






  Here is an example file with push notifications setup to better understand the complete flow:



      import UIKit
import Flutter
import SPRMessengerClient
@main
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    GeneratedPluginRegistrant.register(with: self)
    SPRMessenger.pushManager().autoRequestNotificationPermissions = false
    self.requestPushNotificationPermissions()
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
  override func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    // Convert token to string
    let token = deviceToken.map { String(format: "%02.2hhX", $0) }.joined()
    // Pass to push manager
    SPRMessenger.pushManager().registrationToken = token
  }
  override func application(
    _ application: UIApplication,
    didReceiveRemoteNotification userInfo: [AnyHashable : Any],
    fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
  ) {
    if SPRMessenger.pushManager().canHandlePushEvent(userInfo) {
      SPRMessenger.pushManager().handlePushEvent(userInfo)
    }
    completionHandler(.noData)
  }
  override func userNotificationCenter(
    _ center: UNUserNotificationCenter,
    didReceive response: UNNotificationResponse,
    withCompletionHandler completionHandler: @escaping () -> Void
  ) {
    let userInfo = response.notification.request.content.userInfo
    if SPRMessenger.pushManager().canHandlePushEvent(userInfo) {
      SPRMessenger.pushManager().handlePushEvent(userInfo)
    }
    completionHandler()
  }
  func requestPushNotificationPermissions() {
    let center = UNUserNotificationCenter.current()
    center.getNotificationSettings { settings in
      switch settings.authorizationStatus {
      case .notDetermined:
        DispatchQueue.main.async {
          center.delegate = self
          center.requestAuthorization(options: [.sound, .alert, .badge]) { granted, error in
            if granted {
              self.registerForPushNotifications()
            } else {
              // Notify user to enable push notifications in Settings
            }
          }
        }
      case .denied:
        // Notify user to enable push notifications in Settings
        break
      case .authorized, .provisional, .ephemeral:
        self.registerForPushNotifications()
      @unknown default:
        break
      }
    }
  }
  func registerForPushNotifications() {
    DispatchQueue.main.async {
      UIApplication.shared.registerForRemoteNotifications()
    }
  }
}






### Step 3: Open Live Chat Messenger

Open the Live Chat view with an initial notification: The Messenger view can be launched directly from a push notification or from in‑app notification banners.



      Map launchOptions = {
 "type": "NOTIFICATION",
 "data": notificationData
};
SPRMessenger().startApplication(launchOptions: launchOptions);






### Step 4: Controlling Notification Permissions

**Note:** Step 1 and Step 2 should be completed before calling `takeOff()`.

Prior to initializing the Messenger, you can manage push notifications based on the user's app settings and permission status, provided your app has already obtained notification permission from the user.


-


      To deactivate push notifications according to the user’s application settings, or if the user has not granted notification permission:





      SPRMessenger().setPushEnabled(pushEnabled:false); // Disable if app settings are disabled








-


      The Live Chat application will not request notification permission again if it has already been granted.
      If your application has not obtained notification permissions and you also wish to prevent the Live Chat application from requesting notification permission when `takeOff()` is called, set the `autoRequestPermission` parameter to `false`:





      SPRMessenger().setAutoRequestNotificationPermissions(
   autoRequestNotificationPermissions: false,
  ); // App will not ask the permission for push notifications








-


      Whenever the user has granted notification permission to your application, ensure that push notifications for the Live Chat application are enabled:





      SPRMessenger().setPushEnabled(pushEnabled: true);








### Sample Push Notification Payloads

Push notification payloads define the JSON data delivered to Android and iOS apps when a notification is triggered. They include both display information (title, body, sound, badge) and metadata (sender, message ID, conversation ID, event type). The following examples show typical payload structures for each platform along with parameter details.

### Android



      {
  "notification": {
    "title":"NOTIFICATION_TITLE",
    "body":"NOTIFICATION_BODY"
  },
  "data": {
    "sender": "SENDER_ID",
    "nid": "N_ID",
    "mId": "M_ID",
    "type": "NEW_MESSAGE",
    "et": "LIVE_CHAT_MOBILE_NOTIFICATION",
    "cId": "C_ID",
    "badge": 1,
    "sound": "default",
    "title": "NOTIFICATION_TITLE",
    "message": "NOTIFICATION_BODY"
  }
}



**Note:** `notification` key and `badge` key inside `data` are DP controlled. Kindly raise a support ticket at [tickets@sprinklr.com](mailto:tickets@sprinklr.com) to enable these.


























| Parameter | Sub-parameter | Type | Description |
| --- | --- | --- | --- |
| notification |  | Object | Object containing notification details. |
|  | title | String | Title of the notification (displayed in the system tray). |
|  | body | String | Body/message of the notification. |
| data |  | Object | Object containing other details. |
|  | sender | String | Unique identifier of the message sender. |
|  | nid | String | Notification ID used to uniquely identify the notification. |
|  | mId | String | Message ID associated with the notification. |
|  | type | String | Type of the event, e.g., NEW_MESSAGE. |
|  | et | String | Event type source, e.g., LIVE_CHAT_MOBILE_NOTIFICATION. |
|  | cId | String | Conversation ID the message is associated with. |
|  | badge | Integer | Badge count to display on the app icon. |
|  | sound | String | Notification sound setting (e.g., default). |
|  | title | String | Title displayed in the app-specific notification context. |
|  | message | String | Message body shown in the app-specific notification view. |

### iOS



      {
  "aps": {
    "alert": {
      "title": "NOTIFICATION_TITLE",
      "body": "NOTIFICATION_BODY"
    },
    "sound": "default",
    "badge": 1
  },
  "sender": "SENDER_ID",
  "nid": "N_ID",
  "mId": "M_ID",
  "type": "NEW_MESSAGE",
  "et": "LIVE_CHAT_MOBILE_NOTIFICATION",
  "cId": "C_ID"
}



**Note:** `badge` key inside `aps` is DP controlled. Kindly raise a support ticket at [tickets@sprinklr.com](mailto:tickets@sprinklr.com) to enable these.






















| Parameter | Sub-parameter | Type | Description |
| --- | --- | --- | --- |
| aps | alert.title | String | Title of the notification (displayed in system tray). |
|  | alert.body | String | Body of the notification message. |
|  | sound | String | Sound to play for the notification (e.g., default). |
|  | badge | Integer | Badge count to be displayed on the app icon. |
| sender |  | String | Unique identifier of the sender. |
| nid |  | String | Notification ID used to uniquely identify the notification. |
| mId |  | String | Message ID associated with the notification. |
| type |  | String | Type of the event (e.g., NEW_MESSAGE). |
| et |  | String | Event type source (e.g., LIVE_CHAT_MOBILE_NOTIFICATION). |
| cId |  | String | Conversation ID the message is associated with. |

## Enable Co-Browsing

Mobile co-browsing is a feature that enables customers to securely share their mobile app screens with service agents through the Sprinklr console.
This allows agents to guide users in real time through product purchases, complex form submissions, or any confusing areas within the mobile application interface.
For more details, see [Co-Browsing on Mobile App](https://www.sprinklr.com/help/articles/useragent-journey/cobrowsing-on-mobile-app/65a8cdf5ab59de79d2a0574c).

### Prerequisites

Before you begin, ensure the following prerequisites are met:

#### Support Request

To enable co-browsing, raise a support ticket at
[tickets@sprinklr.com](mailto:tickets@sprinklr.com) with the following details:


- Partner Name

- Partner ID

- Concurrent co-browsing sessions expected

- Number of agents who will be using co-browsing (Concurrent sessions)

#### Add Co-Browse Dependency

Add the co-browse dependency in your project.

**a. Android**

To add support for co-browsing in Android, add the following flag to the project’s root-level `build.gradle` file:




buildscript {
   ext {
       is_cobrowsing_enabled = true
   }
}



**b. iOS**

To add support for co-browsing in iOS, add the following pod in the project’s `ios/Podfile`:




pod 'SPRMessengerClientCobrowseSDK',
    :podspec => 'https://clients-external-cocoapods.sprinklr.com/SPRMessengerClientCobrowseSDK/15.0.0/SPRMessengerClientCobrowseSDK.podspec'



Then run:



      pod install



#### Enable Co-Browse

To enable co-browsing, set `isCobrowsingEnabled: true` in the `takeOff` method:




SPRMessengerConfig messengerConfig = SPRMessengerConfig(
  // rest config,
  isCobrowsingEnabled: true,
);
SPRMessenger().takeOff(config: messengerConfig);



#### Full Device Screen Sharing Support

Full device screen sharing lets support agents view the entire device screen, including apps outside your own.
This helps them check system settings or guide users as they switch between different applications.

To enable this feature, refer to
[Full Device Screen Sharing | Cobrowse.io documentation](https://docs.cobrowse.io/sdk-features/full-device-capabilities/full-device-screen-sharing#flutter).

#### Redaction Support

Redaction ensures that sensitive information is hidden or masked during co-browsing or screen-sharing sessions.
This prevents private data, such as personal details, payment information, or confidential text, from being visible to support agents
while still allowing the rest of the application to be shared seamlessly.

To redact sensitive information, wrap your widget with the `SPRRedacted` widget:




import 'package:sprinklr_plugin/widgets/SPRRedacted.dart';
SPRRedacted(
  child: Text("Sensitive Text"),
);



## Additional Resources

See **All Integration Steps**

  [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-flutter) >
  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-flutter) >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-flutter) >
  **Advanced Configuration (Optional)**

See [Troubleshooting](https://dev.sprinklr.com/)

  [](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter)




[Back to top](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter)
