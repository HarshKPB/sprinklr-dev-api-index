---
title: "Install Sprinklr Survey Kit SDK for React Native"
slug: install-sprinklr-survey-kit-sdk-for-react-native
url: https://dev.sprinklr.com/install-sprinklr-survey-kit-sdk-for-react-native
---

# Install Sprinklr Survey Kit SDK for React Native

# Install Sprinklr Survey Kit SDK for React Native
 

This guide shows how to install the Sprinklr Survey Kit SDK for React Native.

## Configure .npmrc

Sprinklr Survey Kit is a restricted package. Therefore, you need to configure the following registry in `.npmrc` for Sprinklr scoped packages:



@sprinklrjs:registry=https://prod-nexus-external.sprinklr.com/nexus/repository/npm-cfm/
always-auth=true
_auth=



**Dev Notes: **`<SPR_REGISTRY_AUTH_TOKEN>` is the registry token provided by Sprinklr. To get the registry token, raise a support ticket at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

## Install Survey Kit Package

Install the Sprinklr Survey Kit in your project using your preferred package manager, as shown in the following commands:


### Using npm



npm install @sprinklrjs/survey-kit

### Using npm



yarn add @sprinklrjs/survey-kit

## iOS Setup




cd ios
pod install
cd ..

## Next Steps


- [Initialize Sprinklr Survey Kit SDK for React Native](https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-react-native)

- [See All Android Integration Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-react-native)

	 [](https://dev.sprinklr.com/install-sprinklr-survey-kit-sdk-for-react-native)

[Back to top](https://dev.sprinklr.com/install-sprinklr-survey-kit-sdk-for-react-native)
