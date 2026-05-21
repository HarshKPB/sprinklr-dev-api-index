---
title: "Install and Setup LC Mobile SDK - iOS"
slug: install-and-setup-lc-mobile-sdk-ios
url: https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-ios
---

# Install and Setup LC Mobile SDK - iOS

# Install and Setup Live Chat SDK - iOS


To integrate Sprinklr Live Chat Messenger into your project, you must install and setup the Live Chat SDK into your project. This article provides a step-by-step guide to install Live Chat Messenger.


The following are the steps for integrating Sprinklr Messenger. This page covers the **first step: Install and Setup**. Use the flow below to navigate through all steps of the integration process.

 **Install and Setup** >  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios)

**On this page:**



- [Install](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-ios#install)

- [Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-ios#setup)


## Install Live Chat SDK

You can install the Live Chat SDK in iOS using one of two methods:


- CocoaPods

- Swift Package Manager (SPM)

### Using CocoaPods

You can integrate the Live Chat SDK package in your iOS project using CocoaPods.

#### Prerequisites

Before you begin, ensure the following prerequisites are met:


- To access the Sprinklr Messenger framework, you need a username and password. Reach out to Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com) to get the username and password created for your account.

**Dev Notes: **This username and password will be the same for both Android SDK and iOS SDK integration.


- Once you have the username and password, add the required entries to the root `.netrc` file.




machine clients-external-cocoapods.sprinklr.com
login userName
password password




#### Install Messenger iOS Dependency

Follow these steps:


- Add `SPRMessengerClient` to your Podfile.




pod install
target :YourTargetName do
 pod 'SPRMessengerClient', :podspec => 'https://clients-external-cocoapods.sprinklr.com/SPRMessengerClient/15.0.0/SPRMessengerClient.podspec'
 pod 'hermes', :podspec => 'https://clients-external-cocoapods.sprinklr.com/hermes/15.0.0/hermes.podspec'
end






- If your app has enabled bitcode, add this pod installer script in your Podfile to enable bitcode.




post_install do |installer|
 installer.pods_project.targets.each do |target|
   target.build_configurations.each do |config|
     config.build_settings['ENABLE_BITCODE'] = 'YES'
   end
 end
end



### Using Swift Package Manager (SPM)

You can install the Sprinklr Live Chat SDK into your Xcode project using the Swift Package Manager.

**Dev Notes: **To access the SPM framework file, reach out to Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

#### Supported Version

SPM integration is supported from Sprinklr Live Chat SDK version 10.0.0 and above.

#### Installation Steps


- Download and unzip the provided ZIP file containing the Sprinklr Live Chat Swift package.

- Open your project in Xcode, then go to **File > Add Package Dependencies**.

- In the **Add Swift Packages** dialog, click **Add Local**.

- Browse to the unzipped folder and select the Sprinklr Messenger Swift Package.

- Xcode will validate the package and add it to your project.

- Confirm the package is successfully integrated by checking the Package Dependencies section in your Xcode project settings.

## Set Up Live Chat SDK

To enable full functionality of the Sprinklr Live Chat SDK on iOS, your project must include specific permissions in the `info.plist` file. These permissions allow the app to access the camera, microphone, photo library, and optionally the user’s location for features such as media upload, video recording, and location sharing.

### Example



NSCameraUsageDescription
Messenger app requires access to the camera to capture the photos.
NSMicrophoneUsageDescription
Messenger app requires access to the microphone to record video.
NSPhotoLibraryUsageDescription
Messenger app requires access to the photos library.
NSLocationWhenInUseUsageDescription
We need your location to display it on the map.



### Permissions




































| Permission (Info.plist Key) | Description | Required/Optional | Scope |
| --- | --- | --- | --- |
| NSCameraUsageDescription | Messenger app requires access to the camera to capture photos. | Required | Media Upload |
| NSMicrophoneUsageDescription | Messenger app requires access to the microphone to record video. | Required | Media Upload / Video |
| NSPhotoLibraryUsageDescription | Messenger app requires access to the photos library. | Required | Media Upload |
| NSLocationWhenInUseUsageDescription | Messenger app requires access to the user’s location to display it on the map. This permission is optional and should be included only if you want to support location sharing. | Optional | Location Sharing |

## Next Steps

[Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios)

## Additional Resources

See **All Integration Steps**
 [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-ios) > [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-ios)

  [](https://dev.sprinklr.com/install-lc-mobile-sdk-ios)




[Back to top](https://dev.sprinklr.com/install-lc-mobile-sdk-ios)
