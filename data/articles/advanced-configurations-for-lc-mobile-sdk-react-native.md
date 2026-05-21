---
title: "Advanced Configurations for LC Mobile SDK - React Native"
slug: advanced-configurations-for-lc-mobile-sdk-react-native
url: https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native
---

# Advanced Configurations for LC Mobile SDK - React Native

# Advanced Configuration - React Native


After integrating the Live Chat Mobile SDK into your application, you can configure advanced features to further improve the chat experience for your customers.

These options allow you to enable structured logging for better debugging, set up push notifications to keep users informed even when the app is closed, display in-app notifications for real-time updates, and extend functionality with authenticated user flows, co-browsing, and video calling.
Leveraging these advanced capabilities ensures a more reliable, secure, and engaging support experience tailored to your brand’s needs.

  The following are the steps for integrating Sprinklr Messenger.
  This page covers the **sixth step: Advanced Configuration**.
  Use the flow below to navigate through all steps of the integration process.

  [Install](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native) >
  [Setup](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native) >
  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native) >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-react-native) >
  **Advanced Configuration (Optional)**


**On this page:**



- [Live Chat Logger](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native#live-chat-logger)

- [Push Notifications](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native#push-notifications)

- [In-App Notifications](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native#in-app-notifications)

- [Enable Co-Browsing](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native#enable-co-browsing)

- [Set Up Video Calling](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native#video-calling-react-native)


## Live Chat Logger

The Live Chat Logger in the Live Chat SDK provides a structured mechanism for capturing and managing real-time SDK events and system logs.
It enables developers to monitor chat interactions, track user actions, and diagnose issues efficiently by logging critical events and system statuses.

### Add Events Logger to SDK Events

To track and manage various events efficiently, the SDK provides a logging system that can be configured according to your requirements.
The logging system supports different log levels to help debug issues effectively.

### Configure the Logger

Use the following snippet to enable logging and define custom log transports:


**Dev Notes: ** It is recommended to call `setLoggerConfig` before `takeOff` to avoid missing logs emitted during initialization.



import MessengerClient from '@sprinklrjs/chat-native-client';
MessengerClient.setLoggerConfig({
  enableLogs: true, // Required to enable logs
  logLevel: 4, // Optional, default is INFO (4)
  transports: [
    {
      write(level, ...logs) {
        // Implement your custom logger transport here
      },
    },
  ], // Optional, default transport is console
});



### setLoggerConfig Parameters

























      ``

``
****
****



| Parameter | Required/Optional | Value | Description |
| --- | --- | --- | --- |
| enableLogs | Required | Boolean (true/false) | Enable or disable logging. When set to true, logging is enabled. If false, logging is disabled. |
| logLevel | Optional | Integer (0 to 7) | Sets the level of logging detail. Default is 4 (INFO). See Log Levels table below. |
| transports | Optional | List of objects with a write method | Allows defining multiple transporters that get called in parallel.         write(level, …logs) {}         level: Level of the log         …logs: List of logs as strings |

### Available Log Levels



















| Log Level | Value | Description |
| --- | --- | --- |
| OFF | 0 | Disables all logging. No log messages will be recorded. |
| FATAL | 1 | Logs only the most severe error events that will presumably lead the application to abort. |
| ERROR | 2 | Logs things that went wrong so that either something failed or the system had to resort to a fallback that the user may have noticed. |
| WARN | 3 | Logs things that went wrong, but were recoverable so that a user should not have noticed. |
| INFO | 4 | Logs primarily large business-logic steps as the SDK connects, sends, and receives messages. |
| DEBUG | 5 | Logs details of the inner workings of the SDK logic and network stack. |
| TRACE | 6 | Logs high-traffic logs; tracks many objects as they move through the SDK. |
| ALL | 7 | Enables all logging levels, capturing every log message. |

As is standard with most logging systems, each of these settings also includes all levels below it.
Setting the SDK Logging Level to OFF disables SDK logging entirely.

## Add Messenger Events Listener to SDK Events

To track various SDK-related events, register an event listener using the `registerEventsListener` method.

### Register an Events Listener


**Dev Notes: ** It is recommended to call `registerEventsListener` before `takeOff` to avoid missing events during initialization.



import MessengerClient from '@sprinklrjs/chat-native-client';
MessengerClient.registerEventsListener(this.eventsListener);
eventsListener = (eventGroup, eventType, payload) => {
  // Handle events here
};



## Push Notifications

Push notifications allow users to receive real-time updates from the Live Chat Messenger, ensuring seamless communication even when the app is running in the background or closed.

### Prerequisites

Before configuring push notifications, ensure you have the following:

#### Android


- Google `service.json` file (specific to each environment - staging/production).

-
    Refer to the document below to know how to set up the `service.json` file:

    [Service.json file setup.pdf](https://prod2-sprcdn-assets.sprinklr.com/50400/10c76274-613c-4f90-a16b-d8a76a3808cf-1361481284/Service.json_file_setup.pdf)



**Dev Notes: ** The `service.json` file can or cannot be environment-specific depending on your organization.

#### iOS


- APNS certificate (`.p12` format) and its credentials (specific to each environment - staging/production)

- OR P8 Certificate with BundleId, Key, and Team Id.

### Important Notes


- The Google `service.json` file must match the respective environment (staging/production).

- The APNS certificate (`.p12` or P8 Key) and its credentials must be different for staging and production environments.

- If testing push notifications on a production iOS application, use TestFlight build.

- If the Google `service.json` file differs between sandbox/production and you are testing on a production mobile application, ensure to use an Android release build.

- If using a different Google `service.json` file for sandbox/production, ensure TestFlight is used when testing on production (Android).

### Configuration

To enable push notifications, raise a support ticket to [tickets@sprinklr.com](mailto:tickets@sprinklr.com) with the following information:


- Google `service.json` file (for Android).

- APNS certificate (`.p12`) and credentials (for iOS) OR P8 Certificate with Key, BundleId, TeamId.

- Live Chat App ID.

- Partner ID.

- Target Environment.

### Step 1: Register/Unregister for Push Notifications

You must register the Live Chat Messenger to send and receive push notifications. This requires updating the push token received from APNS (iOS) or FCM (Android).


**Dev Notes: ** Call this only after `takeOff` is completed or Live Chat is initialized.

#### Register for Push Notifications



import MessengerClient from '@sprinklrjs/chat-native-client';
MessengerClient.updatePushToken('f30c3b0835ecd378a134c74bce8cea866df8c5b6e12a8c219c9bb288f7270e22');



#### Unregister from Push Notifications

To stop receiving push notifications, unregister by sending an empty token:



import MessengerClient from '@sprinklrjs/chat-native-client';
MessengerClient.updatePushToken('');



### Step 3: Handle Messenger Push Notifications

Once registered, push notifications may be received from both the Messenger and from your application. It is important to distinguish and handle Messenger notifications correctly.

#### Identify Messenger Notifications



import MessengerClient from '@sprinklrjs/chat-native-client';
let isMessengerNotification = MessengerClient.canHandlePushNotification(notification);
// Returns true if it's a Messenger notification, otherwise false.



#### Displaying Messenger Notifications



import MessengerClient from '@sprinklrjs/chat-native-client';
// Handle incoming push notifications
function onNotificationReceived(notification) {
  if (MessengerClient.canHandlePushNotification(notification)) {
    if (!notification.foreground) {
      // If the app was in the background or killed, navigate to the corresponding conversation
      handleMessengerPushNotification(notification);
    }
    return;
  }
  // Handle other platform notifications
}



#### Open Messenger on Click of Push Notification



// Open Messenger conversation for the received Messenger push notification
function handleMessengerPushNotification(notification) {
  if (MessengerClient.isMessengerMounted()) {
    MessengerClient.handlePushNotification(notification);
  } else {
    // Open Messenger view with launch options
    const launchOptions = { type: 'NOTIFICATION', data: notification };
    presentMessengerView(launchOptions);
  }
}
// provide your configured presentMessengerView function to open conversation in messenger corresponding to the notification



By correctly registering for push notifications and distinguishing Messenger notifications, you can enhance the user experience within your mobile app.

### Sample Push Notification Payloads

#### Android



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




**Dev Notes: ** `notification` key and `badge` key inside `data` are DP controlled. Raise a support ticket at [tickets@sprinklr.com](mailto:tickets@sprinklr.com) to enable these.

#### iOS



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




**Dev Notes: ** `badge` key inside `aps` is DP controlled. Raise a support ticket at [tickets@sprinklr.com](mailto:tickets@sprinklr.com) to enable these.

## In-App Notifications

In-app notifications allow users to receive real-time updates when a message or reply is received from a support agent while the app is in the foreground.
These notifications appear as banners at the top of the app, ensuring users do not miss important updates.

You can either use the:


- Sprinklr-provided Messenger Notification Banner

- Customize the notification view to match your app's design.

### Step 1: Enable/Disable In-App Notifications

#### Using Sprinklr’s Default Notification Banner

To enable Sprinklr's in-app notification banner, add `MessengerNotificationBanner` parallel to the root view of your application.



import { MessengerNotificationBanner } from '@sprinklrjs/chat-native-client';
function onTapNotificationBanner(notification) {
 // open sprinklr messenger view with launch options
 const launchOptions = { type: 'NOTIFICATION', data: notification };
 presentMessengerView(launchOptions); // provide your presentMessengerView.. we need to open conversation in messenger corresponding to the notification
}
function MainApp () {
 return (
   <>



 )
}







#### Disabling In-App Notifications

If you want to disable in-app notifications, avoid adding `MessengerNotificationBanner` to your UI or handle notifications through custom logic (explained in the next section).

### Step 2: Customizing In-App Notifications as per Preference

If you prefer a custom notification banner instead of Sprinklr’s default banner, follow these additional steps:

#### Register a Custom Notification Handler

You need to register your own notification handler to process received notifications and display them in your custom banner.


**Dev Notes: ** The handler must be registered only after `takeOff` has been called.



import MessengerClient from '@sprinklrjs/chat-native-client'
// Custom notification handler
function notificationHandler(notification) {
     // Implement your custom logic to display notification in your custom banner
}
MessengerClient.registerNotificationHandler(notificationHandler)







#### Notification Object Structure

The notification object follows this format:



{
  "data": {
    "messageId": "",
    "title": "",          // live chat account display name
    "description": "", // notification message
    "cId": "",               // Conversation Id
    "imageURI": ""                 // Image to display inside the notification banner
  }
}







**Parameters**
















| Field | Type | Description |
| --- | --- | --- |
| messageId | String | Unique identifier of the message associated with the notification. |
| title | String | Title of the notification. Typically, this is the live chat account display name. |
| description | String | Main content or message of the notification. |
| cId | String | Unique identifier of the conversation related to the notification. |
| imageURI | String | URI of the image to be displayed in the notification banner. |

**Example**



import { useState, useEffect } from 'react';
import CustomBanner from './CustomBanner'; // Your custom component
function App() {
  const [notification, setNotification] = useState(null);
  useEffect(() => {
    // Register custom handler
    MessengerClient.registerNotificationHandler((notif) => {
      setNotification(notif); // Show your custom banner
    });
  }, []);
  const handleBannerTap = () => {
    // Navigate to messenger with notification
    navigate('Messenger', {
      launchOptions: { type: 'NOTIFICATION', data: notification },
    });
    setNotification(null); // Hide banner
  };
  return (
    <>
      {/* Your app UI */}
      {notification && (
         setNotification(null)}
        />
      )}

  );
}







## Enable Co-Browsing

Mobile co-browsing is a feature that enables customers to securely share their mobile app screens with service agents through the Sprinklr console.
This allows agents to guide users in real time through product purchases, complex form submissions, or any confusing areas within the mobile application interface.
For more details, see *Co-browsing on Mobile App*.

### Prerequisites

Before you begin, ensure the following prerequisites are met:

#### Support Request

To enable co-browsing, raise a support ticket at [tickets@sprinklr.com](mailto:tickets@sprinklr.com) with the following details:


- Partner Name

- Partner ID

- Concurrent co-browsing sessions expected

- Number of agents who will be using co-browsing (Concurrent sessions)

#### Install Dependency

Install `cobrowse-sdk-react-native` dependency:

For command to install the dependency, see *Install Peer Dependencies*.

### Enable Co-Browsing in Your App

To enable mobile co-browsing in your React Native application, configure the `MessengerClient.takeOff()` method with the `isCobrowsingEnabled` flag set to `true`:



import MessengerClient from '@sprinklrjs/chat-native-client';
MessengerClient.takeOff({
    ...restSettings,
    isCobrowsingEnabled: true,
});



### Full Device Screen Sharing Support

Full device screen sharing lets support agents view the entire device screen, including apps outside your own.
This helps them check system settings or guide users as they switch between different applications.


**Dev Notes: ** To enable this feature, refer to *Full device screen sharing documentation*.

### Redaction Support

When remotely viewing a user's screen, there may be certain sensitive data that should not be viewable by the agent.
For this purpose, Live Chat SDK supports redaction that automatically blocks out on device all sensitive data sources such as credit cards, social security numbers, etc.
When certain data is redacted, it will never leave the user's device.


**Dev Notes: ** To enable this feature, refer to *Redact sensitive data documentation*.

## Set Up Video Calling for React Native

Brands can integrate video calling into their mobile apps through Sprinklr Messenger. This guide explains how to integrate and configure video calling in Sprinklr Messenger for React Native using the Amazon Chime SDK.

### Prerequisites

To integrate AWS Chime, ensure the following prerequisites are met:


- AWS account with the Chime SDK enabled.

- If you want to enable video recording, you need an S3 bucket associated with your AWS account to store Chime-side recordings.

- AWS account number to process video call recordings.

- Permission to access Care Console in the Sprinklr platform.


**Dev Notes: ** You can enable AWS Chime account to make and receive video calls by reaching out to Sprinklr support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

### Installation


-

Install the AWS Chime SDK.


Add package dependency to your `package.json` file:




"@sprinklrjs/chime-video": "2.0.1"





-

Register the video call provider.


In your application entry point, register the video call provider with the Messenger SDK before calling the `takeOff` method:




MessengerClient.registerVideoCallProviderConfig({
  provider: 'AMAZON_CHIME',
});





### Configuring Push Notifications

You can configure push notification handling on Android and iOS, so that incoming calls and call notifications work properly.

**Android**

For Android, follow these steps:

**Step 1**: Create MessengerPushService

This service is responsible for handling incoming push notifications. The implementation differs based on the notification library being used.

If using `react-native-firebase`, extend `ReactNativeFirebaseMessagingService` in your `MessengerPushService`.

The following is an example code. A similar `Service` class can be created for any other push notifications library as well.



package com.messengerexample;
import android.util.Log;
import com.dieam.reactnativepushnotification.modules.RNPushNotificationListenerService;
import com.google.firebase.messaging.RemoteMessage;
import com.sprinklr.messenger.SPRMessengerController;
import java.util.Map;
public class MessengerPushService extends RNPushNotificationListenerService {
    private static final String TAG = "MessengerPushService";
    @Override
    public void onMessageReceived(RemoteMessage remoteMessage) {
        Map remoteData = remoteMessage.getData();
        Log.d(TAG, remoteData.toString());
        if (SPRMessengerController.shared().pusher().canHandlePushEvent(remoteData)) {
            SPRMessengerController.shared().pusher().handlePushEvent(this, remoteData, MainActivity.class);
        } else {
            super.onMessageReceived(remoteMessage);
        }
    }
    @Override
    public void onNewToken(String token) {
        super.onNewToken(token);
    }
}



**Step 2**: Register the Service in `AndroidManifest.xml`

Add the following to your `<application>` block:



<service
    android:name="<your.package.name>.MessengerPushService"
    android:exported="false">
    <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
    </intent-filter>
</service>



**Step 3**: Link sprinklr-messenger-notifications package

In the `settings.gradle` file, include the following project:



include ':sprinklr-messenger-notifications'
project(':sprinklr-messenger-notifications').projectDir = new File(rootProject.projectDir, '../node_modules/@sprinklrjs/chat-native-client/android/notifications')



**Step 4**: Update the MainApplication.java file

In the `app.gradle` or `build.gradle` file, add the following dependency under the dependencies block:



implementation project(':sprinklr-messenger-notifications')



**Step 5**: Update the `MainActivity.java` file

Import the following:



import com.sprinklr.messenger.SPRMessengerController;
import com.sprinklr.messenger.config.bean.SPRPusher;
import com.sprinklr.messenger.NotificationPreferences;



In the `onCreate()` method, initialize the `SPRMessengerController` and optionally configure notification icons:



SPRMessengerController.initialize(SPRPusher::new, this, mReactNativeHost);
// optional: to customize notification icons (should be done after SPRMessengerController.initialize)
NotificationPreferences notificationPreferences = new NotificationPreferences();
notificationPreferences.setSmallIcon(R.drawable.notification_icon); // for notification icon
notificationPreferences.setCallIcon(R.drawable.call_icon); // for call icon
SPRMessengerController.shared().pusher().setSPRNotificationPreferences(notificationPreferences);



**Step 6**: Update the `MainActivity.java` file



import android.content.Intent;
import com.sprinklr.messenger.SPRMessengerController;
public class MainActivity extends ReactActivity {
    // other methods
    @Override
    public void onResume() {
        SPRMessengerController.shared().removeCallNotification(this, this.getIntent());
        super.onResume();
    }
    @Override
    public void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        SPRMessengerController.shared().removeCallNotification(this, intent);
    }
}



#### iOS

For iOS, follow these steps:

Step 1: Add VOIP support

Add the following in your `Info.plist` file:



<key>UIBackgroundModes</key>
<array>
  <string>remote-notification</string>
  <string>voip</string>
</array>



**​Step 2**: Implement `PKPushRegistryDelegate` methods

Objective-C

Make the following changes in the `AppDelegate.m` file:



#import
#import
@interface AppDelegate ()
@end
@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    PKPushRegistry *voipRegistry = [[PKPushRegistry alloc] initWithQueue:dispatch_get_main_queue()];
    voipRegistry.delegate = (AppDelegate *)[UIApplication sharedApplication].delegate;
    voipRegistry.desiredPushTypes = [NSSet setWithObject:PKPushTypeVoIP];
    // other initializations
    return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
#pragma mark - PKPushRegistryDelegate methods
- (void)pushRegistry:(PKPushRegistry *)registry
didUpdatePushCredentials:(PKPushCredentials *)pushCredentials
             forType:(PKPushType)type {
    [[SPRVoipPushNotificationManager shared] didUpdatePushCredentials:pushCredentials
                                                              forType:(NSString *)type];
}
- (void)pushRegistry:(PKPushRegistry *)registry
didInvalidatePushTokenForType:(PKPushType)type {
    [[SPRVoipPushNotificationManager shared] didInvalidatePushTokenForType:(NSString *)type];
}
- (void)pushRegistry:(PKPushRegistry *)registry
didReceiveIncomingPushWithPayload:(PKPushPayload *)payload
             forType:(PKPushType)type
withCompletionHandler:(void (^)(void))completion {
    if ([[SPRVoipPushNotificationManager shared] canHandleVoipPushEvent:payload]) {
        [[SPRVoipPushNotificationManager shared] handleVoipPushEvent:payload
                                                             forType:type
                                                          completion:completion];
        return;
    }
}
@end



Swift

Make the following changes in the `AppDelegate.swift` file:



import PushKit
import SPRMessenger
@UIApplicationMain
class AppDelegate: PKPushRegistryDelegate {
    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
    ) -> Bool {
        let voipRegistry = PKPushRegistry(queue: DispatchQueue.main)
        voipRegistry.delegate = self
        voipRegistry.desiredPushTypes = [PKPushType.voIP]
        // other initializations
        return true
    }
    // MARK: - PKPushRegistryDelegate
    func pushRegistry(
        _ registry: PKPushRegistry,
        didUpdate pushCredentials: PKPushCredentials,
        for type: PKPushType
    ) {
        SPRVoipPushNotificationManager.shared()
            .didUpdatePushCredentials(pushCredentials, forType: type.rawValue)
    }
    func pushRegistry(
        _ registry: PKPushRegistry,
        didInvalidatePushTokenFor type: PKPushType
    ) {
        SPRVoipPushNotificationManager.shared()
            .didInvalidatePushToken(forType: type.rawValue)
    }
    func pushRegistry(
        _ registry: PKPushRegistry,
        didReceiveIncomingPushWith payload: PKPushPayload,
        for type: PKPushType,
        completionHandler completion: @escaping () -> Void
    ) {
        if SPRVoipPushNotificationManager.shared().canHandleVoipPushEvent(payload) {
            SPRVoipPushNotificationManager.shared()
                .handleVoipPushEvent(payload, forType: type.rawValue, completion: completion)
            return
        }
    }
}



### Support Video Continuity Outside Live Chat Interface

This feature allows users to continue a video or audio call even after they navigate away from the Live Chat interface and return to the host brand application.
Without continuity, the video call must be disconnected before leaving the Live Chat interface.
With continuity enabled, the call seamlessly continues outside the Live Chat interface.

Platform‑specific continuity behavior is as follows:


- **Android:** Continuity works at the device level, allowing calls to persist outside the parent app.

- **iOS:** Continuity works at the app level, so calls remain active only within the parent application.


**Dev Notes: ** To enable Video Call Continuity, contact Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

## Additional Resources

See **All Integration Steps**

  [Install](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native) >
  [Setup](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native) >
  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native) >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-react-native) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-react-native)

  [](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native)




[Back to top](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native)
