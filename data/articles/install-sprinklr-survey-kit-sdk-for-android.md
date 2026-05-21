---
title: "Install Sprinklr Survey Kit SDK for Android"
slug: install-sprinklr-survey-kit-sdk-for-android
url: https://dev.sprinklr.com/install-sprinklr-survey-kit-sdk-for-android
---

# Install Sprinklr Survey Kit SDK for Android

# Install Sprinklr Survey Kit SDK for Android
 

This guide shows how to install the Sprinklr Survey Kit SDK for Android.

## Prerequisites

Before you begin with the installation, ensure the following prerequisites are met:


- Customer Feedback Management (CFM) is enabled for your account.

- Obtain the credentials required to access the Sprinklr Survey Kit SDK. To get the credentials, reach out to Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

Once you have the credentials, follow the steps below to install the SDK in your Android project.

### Step A: Define the Repository URL

In your `gradle.properties` file, add the repository URL:




 Copy Code


sprNexusRepositoryUrl = https://prod-nexus-external.sprinklr.com/nexus/repository/maven-clients-cfm/

###  Step B: Add the Maven Repository

Add the Maven repository URL to your root-level `build.gradle` file using the shared credentials.




 Copy Code



allprojects {
    repositories {
       repositories{
          maven {
              url sprNexusRepositoryUrl
              credentials {
                    username = $username
                    password = $password
              }
          }
        }
    }
}

**Dev Note: **To access the Sprinklr Survey Kit SDK, you need a username and password. Reach out to Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com) to get the username and password created for your account.

Additionally, this username and password would be same for both Android SDK and iOS SDK integration

### Step C: Add the SDK dependency

Add the SDK dependency to your app-level `build.gradle` file.




 Copy Code



dependencies { 
    implementation 'com.spr:surveykit:0.1.0' 
} 

**Dev Note: **Since the Gradle file has been edited. Android Studio will ask you whether to sync the files or not. Select Yes, and sync the Gradle files for successful installation of the SDK.

## Next Steps


- [Initialize Sprinklr Survey Kit SDK for Android](https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-android)

- [See All Android Integration Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-android)

	 [](https://dev.sprinklr.com/install-sprinklr-survey-kit-sdk-for-android)

[Back to top](https://dev.sprinklr.com/install-sprinklr-survey-kit-sdk-for-android)
