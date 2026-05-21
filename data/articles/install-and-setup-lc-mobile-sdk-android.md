---
title: "Install and Setup LC Mobile SDK - Android"
slug: install-and-setup-lc-mobile-sdk-android
url: https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-android
---

# Install and Setup LC Mobile SDK - Android

# Install and Setup Live Chat SDK - Android


To integrate Sprinklr Live Chat Messenger into your project, you must install the Live Chat SDK along with its necessary peer dependencies. This section provides a step-by-step guide to install Live Chat Messenger and its necessary dependencies.


  The following are the steps for integrating Sprinklr Messenger.
  This page covers the **first step: Install and Setup**.
  Use the flow below to navigate through all steps of the integration process.

  **Install and Setup** >
  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-android) >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-android) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-android) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android)

**On this page:**


- [Prerequisites](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-android#prerequisites)

- [Install](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-android#install)

- [Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-android#setup)


## Prerequisites

Before you begin installing Sprinklr Messenger, ensure you have a valid username and password. To obtain these credentials, contact Sprinklr Support by raising a ticket at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

## Install

To begin integrating Sprinklr Messenger into your Android project, you’ll need to configure Gradle with the required properties, repositories, and plugins.

To Install Sprinklr Messenger, follow these steps:

- In `gradle.properties`, add the following properties:



sprMessengerClientVersion = 14.0.2
sprNexusRepositoryUrl = https://prod-nexus-external.sprinklr.com/nexus/repository/maven-clients/



- In `settings.gradle`, modify the `pluginManagement` block to include the custom Nexus repository and plugin:

**Dev Notes: **To access the Sprinklr Messenger framework, you need a username and password. Reach out to Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com) to get the username and password created for your account.

This username and password would be same for both Android SDK and iOS SDK integration.



pluginManagement {
    maven {
        url sprNexusRepositoryUrl
        credentials {
            username = $username
            password = $password
        }
    }
}
plugins {
    id "com.spr.messengerclient.spr-gradle-plugin" version sprMessengerClientVersion
}



- In the root `build.gradle`, add the Nexus repository and apply the `spr-gradle-plugin` for enforcing React Native version:



repositories {
    maven {
        url sprNexusRepositoryUrl
        credentials {
            username = $username
            password = $password
        }
    }
}
plugins {
    id "com.spr.messengerclient.spr-gradle-plugin"
}



- In the app module's `build.gradle`, add the following dependency:




implementation "com.spr:messengerclient:$sprMessengerClientVersion"



## Setup

Live Chat Messenger requires certain Android permissions to enable full functionality. The `INTERNET` permission is always needed for network requests, while additional permissions may be required if you enable features such as attachments, audio/video calls, or location sharing.



<uses-permission android:name="android.permission.INTERNET"/>



### Add Permissions to Your Project

If you are supporting media upload/download and location sharing features in messenger, include the following permissions in `AndroidManifest.xml`:












































































| Permission | Description | Required/Optional | Android API Level | Scope |
| --- | --- | --- | --- | --- |
| android.permission.READ_EXTERNAL_STORAGE | Allows reading files from external storage for attachments. | Required (if attachments enabled) | All | Attachments |
| android.permission.WRITE_EXTERNAL_STORAGE | Allows writing files to external storage for attachments. | Required (if attachments enabled) | All | Attachments |
| android.permission.CAMERA | Allows capturing photos or videos. | Required (if camera usage enabled) | All | Attachments / Video Calls |
| android.permission.RECORD_AUDIO | Allows recording audio for calls or attachments. | Required (if audio calls enabled) | All | Audio/Video Calls |
| android.permission.ACCESS_FINE_LOCATION | Provides precise location data. | Optional | All | Location Sharing |
| android.permission.ACCESS_COARSE_LOCATION | Provides approximate location data. | Optional | All | Location Sharing |
| android.permission.FOREGROUND_SERVICE | Allows starting a foreground service to keep audio calls active in background. | Optional | All | Audio/Video Calls |
| android.permission.FOREGROUND_SERVICE_MICROPHONE | Allows starting a foreground service of type “microphone” to keep audio calls active in background. | Optional | All | Audio/Video Calls |
| android.permission.POST_NOTIFICATIONS | Allows posting notifications to the user. | Required (Android 13+) | API 33+ | Notifications |

## Next Steps

[Initialize Live Chat SDK](https://dev.sprinklr.com/initialize-lc-mobile-sdk-android)

## Additional Resources

See **All Integration Steps**

  **Install and Setup** >
  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-android) >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-android) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-android) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-android)

  [](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-android)




[Back to top](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-android)
