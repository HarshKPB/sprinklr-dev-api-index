---
title: "Setup Sprinklr Messenger for React Native"
slug: setup-sprinklr-messenger-for-react-native
url: https://dev.sprinklr.com/setup-sprinklr-messenger-for-react-native
---

# Setup Sprinklr Messenger for React Native

# Setup Sprinklr Messenger for React Native

To set up Sprinklr Messenger, you need to link the Sprinklr Messenger in your project and add the necessary permissions.


## Setup for Android


To setup Sprinklr Messenger, follow these steps:



- Link Sprinklr Messenger in your project. To do that, in `android/settings.gradle`, add the following lines. This will add Sprinklr Messenger and related dependencies to your app.
		  
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
include ':@sprinklr-chat-native-client'
project(':@sprinklr-chat-native-client').projectDir = new File(rootProject.projectDir, '../node_modules/@sprinklrjs/chat-native-client/android')
include ':spr-native-kit'
project(':spr-native-kit').projectDir = new File(rootProject.projectDir, '../node_modules/@sprinklrjs/native-kit/android')
 

     
     
 

In `android/app/build.gradle`, add the following line:

			  
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
dependencies {
  implementation project(':@sprinklr-chat-native-client')
}
 

     
     
 

Add these lines to `MainApplication.java`. This will make Sprinklr Messenger’s related packages a part of the React Native package:

			   
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
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
 

     
     
 


- Add the relevant permissions to project:

If you are supporting upload and download media functionality in messenger, include the following permissions in `AndroidManifest.xml`:













      ``






      ``






      ``






      ``






      ``






      ``







| Permission | Description | Required/Optional | Android API Level | Scope |
| --- | --- | --- | --- | --- |
| android.permission.READ_EXTERNAL_STORAGE | Allows an app to read from external storage. |  |  |  |
| android.permission.WRITE_EXTERNAL_STORAGE | Allows an app to write to external storage. |  |  |  |
| android.permission.DOWNLOAD_WITHOUT_NOTIFICATION | Allows an app to download without showing a notification to the user. |  |  |  |
| android.permission.CAMERA | Allows an app to access the device camera. |  |  |  |
| android.permission.RECORD_AUDIO | Allows an app to record audio. |  |  |  |
| android.permission.POST_NOTIFICATIONS | Allows an app to send notifications to the user. |  |  |  |


**Example**:

		 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.DOWNLOAD_WITHOUT_NOTIFICATION" />
<uses-permission android:name="android.permission.CAMERA" />
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
 

     
     
 



## Setup for iOS


To setup Sprinklr Messenger in iOS, follow these steps:



- Link Sprinklr Messenger in your project:

In the Podfile of your project, add the following lines. This will add Sprinklr Messenger and related dependencies to your app:

				 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
pod 'SPRMessenger', :path => '../node_modules/@sprinklrjs/chat-native-client/SPRMessenger.podspec'
pod 'SPRNativeKit', :path => '../node_modules/@sprinklrjs/native-kit/SPRNativeKit.podspec' # Add this pod manually if not linked automatically via react native auto linking
 

     
     
 

- Add the relevant permissions to your project:

If you are supporting upload and download media functionality in messenger, include the following permissions in the `Info.plist` file:













      ``






      ``






      ``







| Permission | Description | Required/Optional | iOS Version | Scope |
| --- | --- | --- | --- | --- |
| NSCameraUsageDescription | Allows an app to access the device camera. |  |  |  |
| NSMicrophoneUsageDescription | Allows an app to access the microphone. |  |  |  |
| NSPhotoLibraryUsageDescription | Allows an app to access the photo library. |  |  |  |


**Example:**

				 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
<key>NSCameraUsageDescription</key>
<string>Messenger app requires access to the camera to capture the photos.</string>
<key>NSMicrophoneUsageDescription</key>
<string>Messenger app requires access to the microphone to record video.</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>Messenger app requires access to the photos library.</string>
 

     
     
 



## App SDK Flow


## Next Steps

[](https://dev.sprinklr.com/install-live-chat-web-sdks)

[Back to top](https://dev.sprinklr.com/install-live-chat-web-sdks)
