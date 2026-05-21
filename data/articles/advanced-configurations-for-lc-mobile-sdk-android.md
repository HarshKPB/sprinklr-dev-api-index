---
title: "Advanced Configurations for LC Mobile SDK - Android"
slug: advanced-configurations-for-lc-mobile-sdk-android
url: https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android
---

# Advanced Configurations for LC Mobile SDK - Android

# Advanced Configuration - Android


After integrating the Live Chat Mobile SDK into your application, you can configure advanced features to further improve the chat experience for your customers.

These options allow you to enable structured logging for better debugging, set up push notifications to keep users informed even when the app is closed, display in-app notifications for real-time updates, and extend functionality with authenticated user flows, co-browsing, and video calling.
Leveraging these advanced capabilities ensures a more reliable, secure, and engaging support experience tailored to your brand’s needs.

  The following are the steps for integrating Sprinklr Messenger.
  This page covers the **sixth step: Advanced Configuration**.
  Use the flow below to navigate through all steps of the integration process.

  [Install and Setup](https://dev.sprinklr.com/install-lc-mobile-sdk-android) >
  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-android) >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-android) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-android) >
  **Advanced Configuration (Optional)**


**On this page:**



- [Live Chat Logger](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#live-chat-logger)

- [Messenger Events Listener](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#events-listener)

- [Push Notifications](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#push-notifications)

- [In‑App Notifications](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#in-app-notification)

- [Video Calling (AWS Chime)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#video-calls)

- [Enable SSL Pinning](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#ssl-pinning)

- [Co‑Browsing](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#co-browsing)


## Advanced Configuration Options









      [Logger Configuration](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#live-chat-logger)



      [Messenger Events Listener](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#events-listener)



      [Push Notifications](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#push-notifications)



      [In‑App Notifications](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#in-app-notification)



      [Video Calling (AWS Chime)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#video-calls)



      [SSL Pinning](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#ssl-pinning)



      [Co‑Browsing](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android#co-browsing)




| Option | Description |
| --- | --- |
|  | Capture and manage real‑time SDK events and system logs for debugging. |
|  | Listen to chat events such as message sent/received and user actions. |
|  | Deliver real‑time updates even when the app is backgrounded or closed. |
|  | Display alerts and messages inside the app UI. |
|  | Enable video calls between agents and customers. |
|  | Enhance security by validating server identity with public key. |
|  | Allow agents to view and guide customers through app screens. |

## Live Chat Logger

The Live Chat Logger in the Live Chat SDK provides a structured mechanism for capturing and managing real-time SDK events and system logs.
It enables developers to monitor chat interactions, track user actions, and diagnose issues efficiently by logging critical events and system statuses.

### Add Events Logger to SDK Events

To track and manage various events efficiently, the SDK provides a logging system that can be configured according to your requirements.
The logging system supports different log levels to help debug issues effectively.



 SPRLoggerConfig sprLoggerConfig = new
  SPRLoggerConfig()
  .setLevel(SPRLoggerConfig.SPRLogLevel.SPR_INFO) // optional, default
  level is SPRLogLevel.SPR_INFO
  .setEnableLogs(true) // required to enable logs
  .setLoggerTransport((level, logs) -> {
  // your custom logger transport
   }); // required to set native logger transport
SPRMessengerConfig config = new SPRMessengerConfig();
// set other config
config.setLoggerConfig(sprLoggerConfig);




### Parameters














      ````





      ``




      ``
      ``



| Parameter | Required/Optional | Value | Description |
| --- | --- | --- | --- |
| enableLogs | Required | Boolean (true / false) | Enables or disables logging. Must be set to true to record log messages. If false, logging is disabled. |
| level | Optional | Enum (SPRLogLevel) | Sets the logging detail level. Default is SPRLogLevel.INFO. Other levels can be used to control verbosity. For complete list, see Supported Log Levels. |
| loggerTransport | Required | Object implementing write(level, …logs) | Defines a custom transport for logs. The object must implement a write method that receives the log level and log messages. Multiple transports can be defined to handle logs in parallel. |

As is standard with most logging systems, each of these settings also includes all levels below it.
Setting the SDK Logging Level to OFF disables SDK logging entirely.

## Add Messenger Events Listener to SDK Events

Add messenger delegate where you have defined your takeOff method:



SPRMessenger.shared().setMessengerEventsListener(new
SPRMessengerEventsListener() {
  @Override
  public void onEvent(String eventGroup, String
eventType, String eventPayload) {}
});



### Parameters
















































| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| eventGroup | Required | String | Identifies the group or category of the event (e.g., messaging events, connection events). |
| eventType | Required | String | Specifies the type of event within the group (e.g., message received, chat started). |
| payload | Required | String | Contains the event data or details in serialized form (commonly JSON with event-specific information). |
| onEvent | Required | Function | Callback function that handles events triggered by SPRMessengerEventsListener. |
| eventsListener | Required | SPRMessengerEventsListener | Listener object created with SPRMessengerEventsListener that binds the onEvent callback. |
| setMessengerEventsListener | Required | Method | Registers the eventsListener with SPRMessenger so that events are captured and passed to onEvent. |

For supported events, see Common Resources.

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

### Step 1: Register/Unregister for Push Notifications

You must register the Live Chat Messenger to send and receive push notifications. This requires updating the push token received from APNS (iOS) or FCM (Android).



SPRMessenger.shared().pusher().setRegistrationToken(token);



#### Unregister from Push Notifications

To stop receiving push notifications, unregister by sending an empty token:



SPRMessenger.shared().pusher().setRegistrationToken("");




### Step 3: Handle Messenger Push Notifications

Once registered, push notifications may be received from both the Messenger and from your application. It is important to distinguish and handle Messenger notifications correctly.

#### Identify Messenger Notifications

Once you’ve registered for Messenger push notifications, your app may receive notifications from both your platform and Messenger. To determine whether a notification originates from Messenger, use the following check:



Boolean isMessengerNotification = SPRMessenger.shared().pusher().canHandlePushEvent(remoteData); // remote data is fcm RemoteMessage received in onMessageReceived of firebase service




### Displaying Messenger Notifications

Once you have identified if the notification is a Messenger notification, you need to follow the below step to handle push notification.



SPRMessenger.shared().pusher().handlePushEvent(this, remoteData);




### Open Live Chat Messenger

Open Live Chat view with initial notification: Messenger view can be presented with initial notification as the result of opening from notifications or in-app notification banners:



Bundle notificationBundle = new Bundle();
notificationBundle.putString("type", "NOTIFICATION");
notificationBundle.putBundle("data", notificationData);
Bundle appLaunchBundle = new Bundle();
appLaunchBundle.putBundle("launchOptions", notificationBundle);
SPRMessenger.shared().startApplication(appLaunchBundle);




### Controlling Push Notification Permissions

Prior to initializing the Messenger, you have the option to contol push notifications based on the user's app settings and permission request, provided your app has already obtained permission from the user.

- To deactivate the push notifications according to the user’s application setting or if the user has not granted notification permission to your application:



SPRMessenger.shared().pusher().setNotificationEnabled(false); // Disable if app settings are disabled




- The Live Chat application will not request for notification permission again if it has already been granted. When your application has not obtained notification permissions and if you also wish to prevent the Live Chat application from requesting notification permission when `takeOff` is called, you can set the `autoRequestPermission` parameter to `false`.



SPRMessenger.shared().pusher().setAutoRequestNotificationPermissions(false);
// App will not ask the permission for push notifications




- Whenever the user has granted notification permission to your application, ensure that the push notifications for Live Chat application are also enabled. To do this:



SPRMessenger.shared().pusher().setNotificationEnabled(true);​




### Customizing Notification Preferences

Brands have the option to customize sound notifications for push notifications. This allows brands to personalize the notification experience by choosing specific sounds that align with their brand identity or user preferences.

- **Customize push notifications icons according to your preference**: Brands have the flexibility to customize the small, large, and call icons for Push notifications based on their preferences.



SPRNotificationPreferences notificationPreference = new SPRNotificationPreferences();
notificationPreference.setSmallIcon(R.drawable.notification_icon);
notificationPreference.setLargeIcon(R.drawable.notification_icon);
notificationPreference.setCallIcon(R.drawable.call_icon);
SPRMessenger.shared().pusher().setNotificationPreferences(notificationPreference);




- **Customize Sound for Push Notifications**: Brands have the option to enable a custom sound for their Push notifications.



SPRNotificationPreferences notificationPreference = new SPRNotificationPreferences();
Uri soundUri = Uri.parse("android.resource://" + this.getPackageName() + "/"+ R.raw.notification_sound);
notificationPreference.setSound(soundUri);
SPRMessenger.shared().pusher().setNotificationPreferences(notificationPreference);




- **Disable Sound**: Brands have the option to disable sound for Push notifications based on their preferences.



SPRNotificationPreferences notificationPreference = new SPRNotificationPreferences();
notificationPreference.setSoundDisabled(true); default value is false
SPRMessenger.shared().pusher().setNotificationPreferences(notificationPreference);




## In-App Notification

In-app notifications are messages or alerts displayed within a mobile application itself, rather than on the device's main notification tray or lock screen. These notifications are specifically tailored to communicate information directly to the user while they are actively engaged with the app.

You can either use the:


- Sprinklr-provided Messenger Notification Banner

- Customize the notification view to match your app's design.

### Enable/Disable In-App Notifications

By default, in-app notifications are enabled. To disable or enable in-app notifications again for Sprinklr Live Chat, contact Sprinklr Support at
  [tickets@sprinklr.com](mailto:tickets@sprinklr.com). Be sure to raise separate support tickets for sandbox and production environments.

### Customizing Notification Preferences

For in-app notifications, you can provide a custom notification sound or choose to disable the sound entirely. To set this up, refer to the following steps:

- **Customize push notifications icons according to your preference**: Brands have the flexibility to customize the small, large, and call icons for Push notifications based on their preferences.



SPRNotificationPreferences notificationPreference = new SPRNotificationPreferences();
notificationPreference.setSmallIcon(R.drawable.notification_icon);
notificationPreference.setLargeIcon(R.drawable.notification_icon);
notificationPreference.setCallIcon(R.drawable.call_icon);
SPRMessenger.shared().pusher().setNotificationPreferences(notificationPreference);




- **Customize Sound for Push Notifications**: Brands have the option to enable a custom sound for their Push notifications.



SPRNotificationPreferences notificationPreference = new SPRNotificationPreferences();
Uri soundUri = Uri.parse("android.resource://" + this.getPackageName() + "/"+ R.raw.notification_sound);
notificationPreference.setSound(soundUri);
SPRMessenger.shared().pusher().setNotificationPreferences(notificationPreference);




- **Disable Sound**: Brands have the option to disable sound for Push notifications based on their preferences.



SPRNotificationPreferences notificationPreference = new SPRNotificationPreferences();
notificationPreference.setSoundDisabled(true); default value is false
SPRMessenger.shared().pusher().setNotificationPreferences(notificationPreference);




## Taking Video Calls on Messenger

The video calling feature enables brands to connect with customers through video calls directly within the mobile application. These calls can be initiated by agents, providing a more personalized support experience. Sprinklr Live Chat integrates with the AWS Chime service to provide video calling functionality.

Brands can integrate video calling into their mobile apps through Sprinklr Messenger. This guide explains how to integrate and configure video calling in Sprinklr Messenger for React Native using the Amazon Chime SDK.

### Prerequisites

To integrate AWS Chime, ensure the following prerequisites are met:


- AWS account with the Chime SDK enabled

- If you want to enable video recording, you need an S3 bucket associated with your AWS account to store Chime-side recordings.

- AWS account number to process video call recordings

- Permission to access Care Console in the Sprinklr platform

- You can enable AWS Chime account to make and receive video calls by reaching out to Sprinklr support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com)

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


-
    Install AWS Chime SDK and React Native:






implementation 'com.spr:messengerclientchimevideosdk:14.0.2'
implementation 'com.facebook.react:react-android'






-
    Add video package to the messenger config:






import com.spr.messengerchimevideoclient.SPRAmazonChimeManager;






-
    Create config for takeOff:






SPRMessenger sprMessenger = SPRMessenger.shared();
SPRMessengerConfig config = new SPRMessengerConfig();
config.setAppId("SPR_APP_ID"); // Provided by Sprinklr
config.setDeviceId("UNIQUE_DEVICE_ID");
config.setPushAppId("SPR_PUSH_ID"); // Unique id, can be same as device ID
config.setEnvironment("SPR_ENVIRONMENT"); // Provided by Sprinklr (e.g., PROD2)
config.setLocale("SPR_LOCALE"); // Default is en
config.setThemeMode("DEFAULT"); // Options: DEFAULT | DARK
sprMessenger.takeOff(this, config);






-
    Pass SPRAmazonChimeManager:






config.setExtraPackages(new ArrayList<>(Arrays.asList(
    new SPRAmazonChimeManager()
)));






-
    Pass video call provider to SPRMessengerConfig:






config.setVideoCallProvider(SPRVideoCallProviders.AMAZON_CHIME);






-
  Set theme color for call view:






SPRThemeConfig themeConfig = new SPRThemeConfig();
themeConfig.setPrimaryColor(Color.parseColor("#0828cc")); // Default black
themeConfig.setSecondaryColor(Color.parseColor("#0828cc")); // Default white or black depending on primary
config.setThemeConfig(themeConfig);






-
  Call takeOff with all configs:






sprMessenger.takeOff(this, config);






-
  Start the application:






SPRMessenger.shared().startApplication();






### Video Call Continuity Outside Live Chat Interface

Live Chat allows users to continue a video or audio call even after they navigate away from the Live Chat interface and return to the host brand application.


- **Without continuity:** The video call must be disconnected before leaving the Live Chat interface.

- **With continuity enabled:** The call seamlessly continues outside the Live Chat interface.

On **Android**, this functionality operates at the device level, meaning the call will continue even after the user leaves the parent application.


**Dev Notes: **To enable this feature, contact Sprinklr Support at `tickets@sprinklr.com`.

### Integration Steps

To support video call continuity outside Live Chat, you must provide an `ActivityContext` when invoking the `startApplication` methods. This context is required to launch the `VideoCallActivity` intent.

### With Video Call Continuity




SPRMessenger.shared().startApplication(ActivityContext);
SPRMessenger.shared().startApplication(applicationLaunchBundle, ActivityContext);
SPRMessenger.shared().startApplication(appLaunchBundle, ActivityContext);




### Without Video Call Continuity




SPRMessenger.shared().startApplication();
SPRMessenger.shared().startApplication(applicationLaunchBundle);
SPRMessenger.shared().startApplication(appLaunchBundle);




## Enable SSL Pinning

Enable SSL Pinning and Public Key provided by Sprinklr by creating SPRSSLPinning object and pass it to SPRMessengerConfig.

**Dev Notes: **To get the Public Key, contact Sprinklr Support at tickets@sprinklr.com.



SPRMessenger sprMessenger = SPRMessenger.shared();
SPRMessengerConfig config = new SPRMessengerConfig();
config.setAppId("SPR_APP_ID"); // This will be provided by sprinklr
config.setDeviceId("UNIQUE_DEVICE_ID");
config.setPushAppId("SPR_PUSH_ID");   //Unique id, if not sure pass same as device ID
config.setEnvironment("SPR_ENVIRONMENT"); // This will be provided by sprinklr (eg. PROD2)
config.setSkin("MODERN"); // default value is CLASSIC, options: CLASSIC | MODERN
config.setLocale("SPR_LOCALE"); // default value is en
config.setThemeMode("DEFAULT"); // default value is DEFAULT, options: DEFAULT | DARK
SPRSSLPinningConfig sprsslPinningConfig = new SPRSSLPinningConfig();
sprsslPinningConfig.setEnabled(true);
sprsslPinningConfig.setPublicKey("SPR_PUBLIC_KEY"); // This will be provided by sprinklr
config.setSslPinningConfig(sprsslPinningConfig);
sprMessenger.takeOff(this, config);




### Parameters












































      ````





      ````

















      ``



| Parameter | Type | Default Value | Description |
| --- | --- | --- | --- |
| appId | String |  | Application ID provided by Sprinklr. |
| pushAppId | String |  | Unique Push ID. If not sure, use the same as device ID. |
| deviceId | String |  | Unique identifier for the device. |
| environment | String |  | Environment provided by Sprinklr (for example, PROD2). |
| locale | String | en | Locale setting for Messenger (default is English). |
| skin | Enum | CLASSIC | UI skin mode. Options: CLASSIC \| MODERN. |
| themeMode | Enum | DEFAULT | Theme mode. Options: DEFAULT \| DARK. |
| sslPinningConfig.enabled | Boolean | false | Enables SSL pinning for secure communication. |
| sslPinningConfig.publicKey | String | — | Public key provided by Sprinklr for SSL pinning. |
| videoCallProvider | Enum | — | Specifies the video call provider (e.g., SPRAmazonChimeProvider). |

## Enable Co-Browsing

Co-browsing will allow agents to get full visibility into the customer’s screen, enabling them to guide customers through product purchases, complex form filling, or confusing information on mobile application. For more details, please refer here.

### Prerequisites

To enable co-browsing, raise a support ticket at [tickets@sprinklr.com](mailto:tickets@sprinklr.com) with the following details:


- Partner Name

- Partner ID

- Concurrent co-browsing sessions expected

- Number of agents who will be using co-browsing

### Install Co-Browsing SDK and React Native




implementation 'com.facebook.react:react-android'
implementation 'com.sprinklr.externals:cobrowse-sdk-react-native:2.18.2'
implementation 'io.cobrowse:cobrowse-sdk-android:2.30.3'




### Add Co-Browsing Package to Messenger Config




import io.cobrowse.reactnative.CobrowseIOPackage; // import statement for co-browsing sdk package




### Create Config for takeOff




SPRMessenger sprMessenger = SPRMessenger.shared();
SPRMessengerConfig config = new SPRMessengerConfig();
config.setAppId("SPR_APP_ID");  // Provided by Sprinklr
config.setDeviceId("UNIQUE_DEVICE_ID");
config.setPushAppId("SPR_PUSH_ID"); // Unique id, can be same as device ID
config.setEnvironment("SPR_ENVIRONMENT"); // Provided by Sprinklr (e.g., PROD2)
config.setLocale("SPR_LOCALE"); // Default value is en
config.setSkin("MODERN"); // Default CLASSIC, options: CLASSIC | MODERN
config.setThemeMode("DEFAULT"); // Default DEFAULT, options: DEFAULT | DARK
sprMessenger.takeOff(this, config);




### Pass Co-Browsing Package and Enable Flag




config.setExtraPackages(new ArrayList<>(Arrays.asList(
    new CobrowseIOPackage()
)));
config.setCobrowsingEnabled(true);




### Full Device Screen Sharing Support

Full device screen sharing lets support agents view the entire device screen, including apps outside your own. This helps them check system settings or guide users as they switch between different applications.

To enable this feature, refer to [Full Device Screen Sharing](https://docs.cobrowse.io/sdk-features/full-device-capabilities/full-device-screen-sharing#android) documentation.

### Redaction Support

When remotely viewing a user's screen, certain sensitive data should not be viewable by the agent. Live Chat SDK supports redaction that automatically blocks sensitive data sources such as credit cards or social security numbers. Redacted data never leaves the user's device.

To enable this feature, refer to [Redact Sensitive Data](https://docs.cobrowse.io/sdk-features/redact-sensitive-data#android) documentation.


  [](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android)




[Back to top](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android)
