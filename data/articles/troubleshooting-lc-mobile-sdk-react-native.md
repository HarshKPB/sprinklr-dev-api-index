---
title: "Troubleshooting LC Mobile SDK - React Native"
slug: troubleshooting-lc-mobile-sdk-react-native
url: https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-react-native
---

# Troubleshooting LC Mobile SDK - React Native

# Troubleshooting Live Chat Mobile SDK - React Native


This document provides solutions to common issues you might encounter while integrating the Sprinklr Live Chat React Native SDK.

### 1. Live Chat Not Showing Up for Authenticated Users

If the Live Chat widget is not appearing after passing authenticated user details, follow these steps to verify the user hash:


- Navigate to your Live Chat Application in Sprinklr.

- Click the Options icon next to your application and select **Validate User Hash**.

- In the Validate User Hash window, enter the following details:


  - User ID

  - Profile Image URL

  - First Name

  - Last Name

  - Phone Number

  - Email



- Click **Copy Generated Hash** and compare it with the hash generated in your implementation.

- If the hashes don’t match, ensure your hash generation logic aligns with Sprinklr’s authentication mechanism.

### 2. App Crashes While Rendering MessengerView

If your app crashes due to `UIViewControllerBasedStatusBarAppearance` being set to false in Info.plist, wrap `MessengerView` inside `MessengerUIManagersProvider`.

*Placeholder: Example implementation wrapping MessengerView inside MessengerUIManagersProvider*

This ensures the MessengerView does not crash while preserving your app’s existing status bar settings.

### 3. Disabling Autolinking for Peer Dependencies (Android)

If your app faces compatibility issues due to autolinking, disable autolinking for `@sprinklrjs/chat-native-client` on Android.

*Placeholder: Example react-native.config.js configuration to disable autolinking*

After updating, run a clean installation and rebuild your app to prevent conflicts and ensure smooth integration.

### 4. Declaration File Not Found

You may encounter a TypeScript error when importing the `@sprinklr/chat-native-client` module:

*Placeholder: Example TypeScript error message*

Solution options:


- Install type definitions if available. *Placeholder: Example npm install command*

- Manually declare the module by creating a `.d.ts` file in your project root. *Placeholder: Example declaration file content*

### 5. Build Failed with an Exception

You may see a build failure during the Android build process with errors related to Gradle tasks.

*Placeholder: Example Gradle error message*

Solution: Explicitly disable the Android platform for the `@sprinklrjs/chat-native-client` module in your `react-native.config.js`.

*Placeholder: Example configuration disabling Android platform*

### 6. Android Build Failure When minifyEnabled is Set to True

You may encounter an Android build failure when `minifyEnabled` is set to true.

Solution: Add rules to your `proguard-rules.pro` file.

*Placeholder: Example ProGuard rules for React Native and co-browsing support*


  [](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-react-native)




[Back to top](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-react-native)
