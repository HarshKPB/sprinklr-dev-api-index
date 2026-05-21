---
title: "Initialize Sprinklr Survey Kit SDK for Android"
slug: initialize-sprinklr-survey-kit-sdk-for-android
url: https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-android
---

# Initialize Sprinklr Survey Kit SDK for Android

# Initialize Sprinklr Survey Kit SDK for Android

You must initialize the Sprinklr Survey Kit SDK before using its features. Initialization sets up the SDK environment and associates it with your Sprinklr project.

Call the `initializeProject()` method with the App ID, Environment, DeviceId provided by Sprinklr to complete the setup.

## Prerequisites

Before initializing the Sprinklr Survey Kit SDK, ensure that the following prerequisites are met:

- You have received the App ID and Environment details from Sprinklr. These are required parameters for initializing the SDK. You must have a Sprinklr account. If you do not have an account, please contact your admin to either create an account for you or provide the required IDs.

- Your app can generate or retrieve a unique device ID to pass during initialization.

## Initializing Sprinklr Survey Kit

Use this method to initialize the SDK for anonymous (unauthenticated) users, without requiring any user-specific details.

**Dev Note: **This initialization code should be added in your app’s `MainApplication`file to ensure that the SDK is initialized when the application starts.

### Java




 Copy Code



SPRSurveyProjectConfig config = new SPRSurveyProjectConfig()
        .setAppId("SPR_APP_ID") 
        .setEnvironment("SPR_ENVIRONMENT") 
        .setDeviceId("UNIQUE_DEVICE_ID") 
        .setAutoEvaluate(false); 
 
SPRSurveyManager.shared.initializeProject(this, config); 

## Parameters






****

-
- ****
-
-
- ****

- ****










****

****







****


| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| appId | Required | String |  |
| deviceId | Required | String | A unique ID for the user’s device. |
| environment | Required | String | The Sprinklr environment where the app is running. For example, PROD2.Determine the Environment:       The Environment is the name of the live production environment where your instance of Sprinklr is hosted, such as PROD, PROD2, PROD3.        Dev Notes: Reach out to the Sprinklr Team to obtain the name of your Production Environment. |
| autoEvaluate | Optional | Boolean | If true, intercepts are automatically evaluated after initialization. Supported Values: True (Default), False. |

## Next Steps

- [Integrate SDK Methods](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-android)

- [See All Integrations Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-android)

	 [](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-android)

[Back to top](https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-android)
