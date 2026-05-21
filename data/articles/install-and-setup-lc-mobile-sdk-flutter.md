---
title: "Install and Setup LC Mobile SDK - Flutter"
slug: install-and-setup-lc-mobile-sdk-flutter
url: https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-flutter
---

# Install and Setup LC Mobile SDK - Flutter

# Install and Setup Live Chat SDK - Flutter


To integrate Sprinklr Live Chat Messenger into your project, you must install and set up the Live Chat SDK along with its necessary peer dependencies. This section provides a step-by-step guide to install and set up Live Chat Messenger and its necessary dependencies.


The following are the steps for integrating Sprinklr Messenger. This page covers the **first step: Install and Setup**. Use the flow below to navigate through all steps of the integration process.

 **Install and Setup** > [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-flutter) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-flutter) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter)

**On this page:**

- [Install](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-flutter#install)

- [Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-flutter#setup)


## Install Sprinklr Messenger



- Download the Sprinklr Messenger plugin shared with you and save it to your preferred location.
For example, you can place the plugin outside the main directory of your project.


- In your project’s `pubspec.yaml`, add the Sprinklr Messenger dependency in the `dependencies` section:



dependencies:
 sprinklr_plugin:
   path: PATH_HERE



Replace `PATH_HERE` with the actual path where the Sprinklr Messenger plugin is located.

- To get the Sprinklr Messenger dependency into your project, run the following command:



flutter pub get





**iOS**




pod install
target :YourTargetName do
 pod 'SPRMessengerClient', :podspec => 'https://clients-external-cocoapods.sprinklr.com/SPRMessengerClient/15.0.0/SPRMessengerClient.podspec'
 pod 'hermesvm’, :podspec => 'https://clients-external-cocoapods.sprinklr.com/hermesvm/15.0.0/hermesvm.podspec'​
end




**Android**

In the root project’s `build.gradle` file, add the nexus repository to the `repositories` block inside `allProjects` to resolve Sprinklr dependencies.




allprojects {
    repositories {
        // other repos
        maven {
            url "https://prod-nexus-external.sprinklr.com/nexus/repository/maven-clients/"
            credentials {
                username =
                password =
            }
        }
    }
}




In the app module's `build.gradle`, apply the `spr-react-gradle-plugin` to configure the native code:




plugins {
    id "com.spr.messengerclient.spr-gradle-plugin.spr-react-gradle-plugin"
}




Also, add the following configure block to run the native build properly.




sprConfig {
    configureNdk = true
}




**(Optional)** If your project already uses CMake for native builds, additional changes will be required. To make sure you are using CMake already, look for the following snippet in your `app/build.gradle`:

**Dev Notes: **The minimum required CMake version is 3.13.




externalNativeBuild {
   cmake {
       path "path/to/CMakeLists.txt"
   }
}




Once it is confirmed that your project uses native builds with CMake, add the following code in the `CMakeLists.txt` file specified above:




# Define the library name here if not already defined
project(appmodules)
# PATH_TO_APP_BUILD_DIR should point to the build directory inside app.
include(${PATH_TO_APP_BUILD_DIR}/spr-react-gradle-plugin/resources/modules/react-native/ReactAndroid/cmake-utils/ReactNative-application.cmake)




Parallel to the `CMakeLists.txt` file, create a file `OnLoad.cpp`, and add the following code in it:




#include
#include
#include
#include
#include
#include
#ifdef REACT_NATIVE_APP_CODEGEN_HEADER
#include REACT_NATIVE_APP_CODEGEN_HEADER
#endif
#ifdef REACT_NATIVE_APP_COMPONENT_DESCRIPTORS_HEADER
#include REACT_NATIVE_APP_COMPONENT_DESCRIPTORS_HEADER
#endif
namespace facebook::react {
    void registerComponents(
            std::shared_ptr registry) {
        // Custom Fabric Components go here. You can register custom
        // components coming from your App or from 3rd party libraries here.
        //
        // providerRegistry->add(concreteComponentDescriptorProvider<
        //        MyComponentDescriptor>());
        // We link app local components if available
#ifdef REACT_NATIVE_APP_COMPONENT_REGISTRATION
        REACT_NATIVE_APP_COMPONENT_REGISTRATION(registry);
#endif
        // And we fallback to the components autolinked
        autolinking_registerProviders(registry);
    }
    std::shared_ptr cxxModuleProvider(
            const std::string& name,
            const std::shared_ptr& jsInvoker) {
        // Here you can provide your CXX Turbo Modules coming from
        // either your application or from external libraries. The approach to follow
        // is similar to the following (for a module called `NativeCxxModuleExample`):
        //
        // if (name == NativeCxxModuleExample::kModuleName) {
        //   return std::make_shared(jsInvoker);
        // }
        // And we fallback to the CXX module providers autolinked
        return autolinking_cxxModuleProvider(name, jsInvoker);
        return nullptr;
    }
    std::shared_ptr javaModuleProvider(
            const std::string& name,
            const JavaTurboModule::InitParams& params) {
        // Here you can provide your own module provider for TurboModules coming from
        // either your application or from external libraries. The approach to follow
        // is similar to the following (for a library called `samplelibrary`):
        //
        // auto module = samplelibrary_ModuleProvider(name, params);
        // if (module != nullptr) {
        //    return module;
        // }
        // return rncore_ModuleProvider(name, params);
        // We link app local modules if available
#ifdef REACT_NATIVE_APP_MODULE_PROVIDER
        auto module = REACT_NATIVE_APP_MODULE_PROVIDER(name, params);
  if (module != nullptr) {
    return module;
  }
#endif
        // We first try to look up core modules
        if (auto module = FBReactNativeSpec_ModuleProvider(name, params)) {
            return module;
        }
        // And we fallback to the module providers autolinked
        if (auto module = autolinking_ModuleProvider(name, params)) {
            return module;
        }
        return nullptr;
    }
} // namespace facebook::react
JNIEXPORT jint JNICALL JNI_OnLoad(JavaVM* vm, void*) {
    return facebook::jni::initialize(vm, [] {
        facebook::react::DefaultTurboModuleManagerDelegate::cxxModuleProvider =
                &facebook::react::cxxModuleProvider;
        facebook::react::DefaultTurboModuleManagerDelegate::javaModuleProvider =
                &facebook::react::javaModuleProvider;
        facebook::react::DefaultComponentsRegistry::
        registerComponentDescriptorsFromEntryPoint =
                &facebook::react::registerComponents;
    });
}




## Setup


The **Setup** section includes the platform-specific configurations required to successfully integrate the Sprinklr Messenger Plugin into your Flutter project.


Depending on your platform, see the relevant section:



- [Setup for Android](https://dev.sprinklr.com/)

- [Setup for iOS](https://dev.sprinklr.com/)

### Setup for Android


The Android setup includes the necessary configurations to enable key features such as video player support, required permissions in the Android manifest, ProGuard rules for release builds, and compatibility with the minimum supported API level.

#### Prerequisites

Before you begin, ensure the following prerequisites are met:


- Contact Sprinklr Support at `tickets@sprinklr.com` to obtain your Maven credentials.

- The username and password will be the same for both Android and iOS.

- In your Android project folder, create a file named `signing.properties` and add the Maven credentials to this file as shown below.


**Note:** It is recommended to add `signing.properties` to your `.gitignore` file for better security.




MAVEN_USERNAME =
MAVEN_PASSWORD =




### Video Player Support

To add support for video player in Android, add the following flag to the project’s root-level `build.gradle` file:



buildscript {
   ext {
       use_spr_video_player = true
   }
}



### Add Permissions to Your Project

This step includes adding the necessary permissions to your Android project to enable Sprinklr Messenger features.

The `android.permission.INTERNET` permission is included in the `AndroidManifest.xml` by default as it is required to make network requests:



<uses-permission android:name="android.permission.INTERNET" />



  If you are supporting media upload/download and location sharing features in messenger, include the following permissions in `AndroidManifest.xml`:

### Permissions






























































| Permission | Description | Required/Optional | Android API Level | Scope |
| --- | --- | --- | --- | --- |
| android.permission.READ_EXTERNAL_STORAGE | Allows an app to read from external storage. | Required | API Level < 29 | Media Download |
| android.permission.WRITE_EXTERNAL_STORAGE | Allows an app to write to external storage. | Required | API Level < 29 | Media Download |
| android.permission.CAMERA | Allows an app to access the device camera. | Optional - Only required if video call feature is being used. | All supported API Level | Video Calling |
| android.permission.RECORD_AUDIO | Allows an app to record audio. | Optional - Only required if video call feature is being used. | All supported API Level | Video Calling |
| android.permission.POST_NOTIFICATIONS | Allows an app to send notifications to the user. | Optional - Only required if messenger push notifications are to be shown. | All supported API Level | Push Notifications |
| android.permission.ACCESS_FINE_LOCATION | Allows an app to access the location of the user. | Optional - Only required if location sharing feature of Live Chat is used. | All supported API Level | Location Sharing |
| android.permission.ACCESS_COARSE_LOCATION | Allows an app to access the approximate location of the user. | Optional - Only required if location sharing feature of Live Chat is used. | All supported API Level | Location Sharing |

### ProGuard Configuration (Code Minification)

If you're using code minification in your Android release build, ensure you update your project's `proguard-rules.pro` file to include the following rule:



-keep class com.facebook.react.devsupport.** { *; }



Confirm your ProGuard file is referenced correctly in the `app/build.gradle` file:



buildTypes {
    release {
        minifyEnabled true
        proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
    }
}



## Setup for iOS


You can integrate the Live Chat SDK package in your iOS project using CocoaPods.

### Prerequisites

Before you begin with the setup, ensure the following prerequisites are met:


- To access the Sprinklr Messenger framework, you need a username and password. Contact Sprinklr Support at `tickets@sprinklr.com` to get the credentials created for your account.

- The username and password will be the same for both Android and iOS.

- You can use the same credentials that you used for `clients-cocoapods.sprinklr.com`.

- Once you have the username and password, add the following lines to the root `.netrc` file:


**Note:** Ensure your `.netrc` file is secured and excluded from version control for better security.




machine clients-external-cocoapods.sprinklr.com
login userName
password password




### Install Messenger iOS Dependency

Add **SPRMessengerClient** to your Podfile and run the following code:



pod install
​
target :YourTargetName do
​
 pod 'SPRMessengerClient', :podspec => 'https://clients-cocoapods.sprinklr.com/SPRMessengerClient/12.0.1/SPRMessengerClient.podspec'
​
end



  If your app has bitcode enabled, add this pod installer script in your Podfile:



post_install do |installer|
 installer.pods_project.targets.each do |target|
   target.build_configurations.each do |config|
     config.build_settings['ENABLE_BITCODE'] = 'YES'
   end
 end
end



### Add Permissions

Include the following permissions in `info.plist` if you are supporting upload and download media functionality in messenger:









































| Permission | Description | Required/Optional | iOS Version | Scope |
| --- | --- | --- | --- | --- |
| NSCameraUsageDescription | Allows an app to access the device camera. | Optional - Only required if video call or media (videos/images) sharing feature is being used in Live Chat. | All iOS versions | Video Call, Media Upload |
| NSMicrophoneUsageDescription | Allows an app to access the microphone. | Optional - Only required if video call or video sharing feature is being used in Live Chat. | All iOS versions | Video Call, Media Upload |
| NSPhotoLibraryUsageDescription | Allows an app to access the photo library. | Optional - Only required if media from gallery sharing feature is being used in Live Chat. | All iOS versions | Media Upload |
| NSLocationWhenInUseUsageDescription | Allows an app to access location of the user. | Optional - Only required if location sharing is being used in Live Chat. | All iOS versions | Location Sharing |

### Example



<key>NSCameraUsageDescription</key>
<string>Messenger app requires access to the camera to capture the photos.</string>
<key>NSMicrophoneUsageDescription</key>
<string>Messenger app requires access to the microphone to record video.</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>Messenger app requires access to the photos library.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>We need your location to display it on the map.</string>



## Next Steps

[Initialize Live Chat SDK](https://dev.sprinklr.com/initalize-lc-mobile-sdk-flutter)

## Additional Resources

See **All Integration Steps**
 **Install and Setup** > [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-flutter) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-flutter) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-flutter)

  [](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-flutter)




[Back to top](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-flutter)
