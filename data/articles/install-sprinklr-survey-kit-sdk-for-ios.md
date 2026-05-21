---
title: "Install Sprinklr Survey Kit SDK for iOS"
slug: install-sprinklr-survey-kit-sdk-for-ios
url: https://dev.sprinklr.com/install-sprinklr-survey-kit-sdk-for-ios
---

# Install Sprinklr Survey Kit SDK for iOS

# Install Sprinklr Survey Kit SDK for iOS
 

This guide shows how to install the Sprinklr Survey Kit SDK for iOS.

## Prerequisites

Before you begin with the installation, ensure the following prerequisites are met:


- Customer Feedback Management (CFM) is enabled for your account.

- Obtain the credentials required to access the Sprinklr Survey Kit SDK. To get the credentials, reach out to Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

**Dev Notes: **You can use the same username and password you obtained from Sprinklr Support for both Android SDK and iOS SDK integration.

Once you have the credentials, in the root `.netrc` file, add the following lines:




 Copy Code


machine clients-external-cocoapods-cfm.sprinklr.com
login userName
password password



## Install Survey Kit iOS Dependency

Add `SPRSurveyKit` to your Podfile and run the following code:




 Copy Code


pod install
target :YourTargetName do
 pod 'SPRSurveyKit', :podspec => 'https://clients-external-cocoapods-cfm.sprinklr.com/SPRSurveyKit/0.1.0/SPRSurveyKit.podspec'
end



## Next Steps


- [Initialize Sprinklr Survey Kit SDK for iOS](https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-ios)

- [See All iOS Integration Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-ios)

	 [](https://dev.sprinklr.com/install-sprinklr-survey-kit-sdk-for-ios)

[Back to top](https://dev.sprinklr.com/install-sprinklr-survey-kit-sdk-for-ios)
