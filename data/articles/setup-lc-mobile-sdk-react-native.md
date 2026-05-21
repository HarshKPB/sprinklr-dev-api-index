---
title: "Setup LC Mobile SDK - React Native"
slug: setup-lc-mobile-sdk-react-native
url: https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native
---

# Setup LC Mobile SDK - React Native

# Set Up Live Chat Mobile SDK - React Native

To set up Sprinklr Messenger, you need to link the Sprinklr Messenger in your project and add the necessary permissions.

The following are the steps for integrating Sprinklr Messenger. This page covers the **second step: Setup**. Use the flow below to navigate through all steps of the integration process.

 [Install](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native) > **Setup** > [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-react-native) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native)


**On this page:**



- [Setup for Android](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native#setup-android)

- [Setup for iOS](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native#setup-ios)


## Setup for Android

To setup Sprinklr Messenger, follow these steps:

### Link Sprinklr Messenger in Your Project

You can link Sprinklr Messenger in your project with autolinking or without autolinking. Autolinking automatically links the peer dependencies in your project with Sprinklr Messenger.


**Dev Notes:**
    Sprinklr Messenger supports the React Native New Architecture.
    If you are using the new architecture, it is recommended to use `autolinking` to link Sprinklr Messenger in your project.


See the relevant section for steps:


- Autolinking is enabled (recommended)

- Autolinking is disabled

#### Autolinking Enabled


-
    In `android/settings.gradle`, add the required lines.

    This will add Sprinklr Messenger and related dependencies to your app.




include ':spr-native-kit'
project(':spr-native-kit').projectDir = new File(rootProject.projectDir, '../node_modules/@sprinklrjs/native-kit/android')






-
    In `MainApplication.java`, add the necessary lines to make Sprinklr Messenger packages part of the React Native package.

To enable autolinking, pass `true` as the value to the `getPackages` method.


**Java**




import com.sprinklr.messenger.SPRMessengerPackagesProvider;
@Override
protected List getPackages() {
    List packages = new ArrayList<>(Arrays.asList(
        ...{YOUR_NATIVE_PACKAGES}
    ));
    packages.addAll(
        SPRMessengerPackagesProvider.getPackages(
            isAutolinkingEnabled,
            ActivityClass,
            R.drawable.notification_icon
        )
    );
    return packages;
}
// isAutolinkingEnabled: send false to disable automatic linking, send true to enable autolinking
// ActivityClass: Class of activity (like MainActivity.class). This is optional and required only if you are using video calls
// NotificationIcon: Icon used to display notification. This is optional and required only if you are using video calls





**Kotlin**




import com.sprinklr.messenger.SPRMessengerPackagesProvider
override fun getPackages(): List =
    PackageList(this).packages.apply {
        // ---- Sprinklr Messenger configuration ----
    // Enable / disable autolinking for Sprinklr packages
    val isAutolinkingEnabled = true

    // Required only if using video calls
    val activityClass = MainActivity::class.java

    // Required only if using video calls
    val notificationIcon = R.drawable.notification_icon

    addAll(
        SPRMessengerPackagesProvider.getPackages(
            isAutolinkingEnabled,
            activityClass,
            notificationIcon
        )
    )
}





**Parameters**













      ````





      ````





      ``




| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| isAutolinkingEnabled | Required | Send false to disable automatic linking, send true to enable autolinking. | Boolean |
| ActivityClass / activityClass | Optional | Class of the activity (e.g., MainActivity.class or MainActivity::class.java). Required only if you are using video calls. | Class<?> / Class<*> |
| NotificationIcon / notificationIcon | Optional | Resource ID of the icon used to display notifications (e.g., R.drawable.notification_icon). Required only if you are using video calls. | int / Int |

#### Autolinking Disabled


-
    In `android/settings.gradle`, add the required lines.

    This will add Sprinklr Messenger and related dependencies to your app.



include ':@sprinklr-chat-native-client'
​
project(':@sprinklr-chat-native-client').projectDir = new File(rootProject.projectDir, '../node_modules/@sprinklrjs/chat-native-client/android')
​
include ':spr-native-kit'
​
project(':spr-native-kit').projectDir = new File(rootProject.projectDir, '../node_modules/@sprinklrjs/native-kit/android')






-
    In `android/app/build.gradle`, add the dependency line to include Sprinklr Messenger.



dependencies {
  implementation project(':@sprinklr-chat-native-client')
}






-
    Add the necessary lines to `MainApplication.java`.
    This will make Sprinklr Messenger packages part of the React Native package.



import com.sprinklr.messenger.SPRMessengerPackagesProvider
.
.
     @Override
     protected List getPackages() {
       List packages = new ArrayList<>(Arrays.asList(
          ...{YOUR_NATIVE_PACKAGES}
       ));
       packages.addAll(SPRMessengerPackagesProvider.getPackages());
       return packages;
     }






### Add Permissions to Your Project

If you are supporting media upload/download and location sharing features in messenger, include the following permissions in `AndroidManifest.xml`:



















































































| Permission | Description | Required/Optional | Android API Level | Scope |
| --- | --- | --- | --- | --- |
| android.permission.READ_EXTERNAL_STORAGE | Allows an app to read from external storage. | Required | API Level < 29 | Media Download |
| android.permission.WRITE_EXTERNAL_STORAGE | Allows an app to write to external storage. | Required | API Level < 29 | Media Download |
| android.permission.CAMERA | Allows an app to access the device camera. | Optional | All supported API Level | Video Calling (only required if video call feature is used) |
| android.permission.RECORD_AUDIO | Allows an app to record audio. | Optional | All supported API Level | Video Calling (only required if video call feature is used) |
| android.permission.POST_NOTIFICATIONS | Allows an app to send notifications to the user. | Optional | All supported API Level | Push Notifications (only required if messenger push notifications are shown) |
| android.permission.ACCESS_FINE_LOCATION | Allows an app to access the location of the user. | Optional | All supported API Level | Location Sharing (only required if Live Chat location sharing is used) |
| android.permission.ACCESS_COARSE_LOCATION | Allows an app to access the approximate location of the user. | Optional | All supported API Level | Location Sharing (only required if Live Chat location sharing is used) |
| android.permission.FOREGROUND_SERVICE | Allows an app to start a foreground service. | Optional | All supported API Level | Video Calling (only required if audio calls should continue in background) |
| android.permission.FOREGROUND_SERVICE_MICROPHONE | Allows an app to start a foreground service of type “microphone”. | Optional | All supported API Level | Video Calling (only required if audio calls should continue in background) |

### Example



<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.DOWNLOAD_WITHOUT_NOTIFICATION" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>





## Setup for iOS

To setup Sprinklr Messenger in iOS, follow these steps:

### Link Sprinklr Messenger in Your Project

In Podfile, add the following lines. This will add Sprinklr Messenger and related dependencies to your app.

#### Autolinking is Enabled



pod 'SPRNativeKit', :path => '../node_modules/@sprinklrjs/native-kit/SPRNativeKit.podspec'





#### Autolinking is Disabled



pod 'SPRMessenger', :path => '../node_modules/@sprinklrjs/chat-native-client/SPRMessenger.podspec'
​
pod 'SPRNativeKit', :path => '../node_modules/@sprinklrjs/native-kit/SPRNativeKit.podspec'





### Add Permissions to Your Project

If you are supporting upload and download media functionality in messenger, include the following permissions in the info.plist file:

**Note:** These permissions are required by Apple for all apps that access the photo library or use the camera/microphone.









































| Permission | Description | Required/Optional | iOS version | Scope |
| --- | --- | --- | --- | --- |
| NSCameraUsageDescription | Allows an app to access the device camera. | Optional (only required if video call or media (videos/images) sharing feature is being used in Live Chat) | All iOS versions | Video Call, Media Upload |
| NSMicrophoneUsageDescription | Allows an app to access the microphone. | Optional (only required if video call or video sharing feature is being used in Live Chat) | All iOS versions | Video Call, Media Upload |
| NSPhotoLibraryUsageDescription | Allows an app to access the photo library. | Optional (only required if media from gallery sharing feature is being used in Live Chat) | All iOS versions | Media Upload |
| NSLocationWhenInUseUsageDescription | Allows an app to access location of the user. | Optional (only required if location sharing is being used in Live Chat) | All iOS versions | Location Sharing |

#### Example



<key>NSCameraUsageDescription</key>
<string>Messenger app requires access to the camera to capture the photos.</string>
<key>NSMicrophoneUsageDescription</key>
<string>Messenger app requires access to the microphone to record video.</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>Messenger app requires access to the photos library.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>We need your location to display it on the map.</string>





## Next Steps

[Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native)

## Additional Resources

See **All Integration Steps**
 [Install](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native) > [Setup](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native) > [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-react-native) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-react-native)

  [](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native)




[Back to top](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native)
