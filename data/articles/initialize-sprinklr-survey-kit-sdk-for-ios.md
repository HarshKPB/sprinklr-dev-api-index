---
title: "Initialize Sprinklr Survey Kit SDK for iOS"
slug: initialize-sprinklr-survey-kit-sdk-for-ios
url: https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-ios
---

# Initialize Sprinklr Survey Kit SDK for iOS

# Initialize Sprinklr Survey Kit SDK for iOS

After installation, the next step is to initialize the Sprinklr Survey Kit SDK by calling the `initializeProject` method.

In this step, the `SPRSurveyManager` class is initialized with the App ID, environment, and device ID. To confirm whether the initialization was successful, you can listen to the `INITIALIZATION_SUCCESS` event. The initialization can be done in the app delegate (`didFinishLaunchingWithOptions`).

## Prerequisites

Before you begin, ensure that the following prerequisite is met:


- You must have a Sprinklr account. If you do not have an account, please contact your admin to either create an account for you or provide the required IDs.

## Initializing Sprinklr Survey Kit

Use this method to initialize the SDK for anonymous (unauthenticated) users, without requiring any user-specific details.

### Swift




 Copy Code


import SPRSurveyKit
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        let config = SPRSurveyProjectConfig()
        config.appId = "SPR_APP_ID" // This will be provided by sprinklr
        config.deviceId = "UNIQUE_DEVICE_ID";
        config.environment = "SPR_ENVIRONMENT"; // This will be provided by sprinklr (eg. PROD2)
        config.autoEvaluate = false; // true or false, default value is true
               SPRSurveyManager.shared.initializeProject(from: config)
}



### Objective C




 Copy Code


#import
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  SPRSurveyProjectConfig *config = [SPRSurveyProjectConfig new];
  config.appId = @"SPR_APP_ID"; // This will be provided by sprinklr
  config.deviceId = @"UNIQUE_DEVICE_ID";
  config.environment = @"SPR_ENVIRONMENT"; // This will be provided by sprinklr (eg. PROD2)
  config.autoEvaluate = NO; // YES or NO, default value is YES
SPRSurveyManager *surveyManager = [SPRSurveyManager shared];
[surveyManager initializeProjectFrom:config];
}



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
| autoEvaluate | Optional | Boolean | If true, intercepts are automatically evaluated after initialization. Supported Values: YES (Default), NO. |

## Next Steps

- [Integrate SDK Methods](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-ios)

- [See All Integrations Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-ios)

	 [](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-ios)

[Back to top](https://dev.sprinklr.com/business-hours-and-holiday-lists)
