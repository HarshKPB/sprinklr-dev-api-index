---
title: "Initialize Sprinklr Survey Kit SDK for Flutter"
slug: initialize-sprinklr-survey-kit-sdk-for-flutter
url: https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-flutter
---

# Initialize Sprinklr Survey Kit SDK for Flutter

# Initialize Sprinklr Survey Kit SDK for Flutter

Initialize the Sprinklr Survey Kit SDK. In this step, the SDK is initialized with the App ID, environment, and device ID. To confirm whether the initialization was successful, you can listen to the `INITIALIZATION_SUCCESS` event.


## Method



Future initializeProject({required String appId, required String environment, required String deviceId, bool autoEvaluate = true})

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
| deviceId | Optional | String | A unique ID for the user’s device. |
| environment | Required | String | The Sprinklr environment where the app is running. For example, PROD2.Determine the Environment:       The Environment is the name of the live production environment where your instance of Sprinklr is hosted, such as PROD, PROD2, PROD3.        Dev Notes: Reach out to the Sprinklr Team to obtain the name of your Production Environment. |
| autoEvaluate | Optional | Boolean | If true, intercepts are automatically evaluated after initialization. Supported Values: true (Default), false. |

## Response












      ````



| Return Type | Values | Description |
| --- | --- | --- |
| Future<bool> | true, false | Resolves to true if initialization succeeds, false otherwise. |

### Example



final SPRSurveyKit surveyKit = SPRSurveyKit();
Future initialize() async {
  try {
    final success = await surveyKit.initializeProject(
      appId: '68776f7cd1db742044c49639_app_1000528027',
      environment: 'PROD2',
      deviceId: '12345',
      autoEvaluate: true,
    );
    if (success) {
      // SDK initialized
      surveyKit.startSessionTracking();
    }
  } catch (error) {
    // Initialization failed
  }
}

### Events Emitted

This SDK emits specific events during its lifecycle. You can listen to these events to monitor initialization progress, handle success or failure states, and trigger custom logic in your application.


















| Event | Description |
| --- | --- |
| INITIALIZATION_STARTING | Initialization process has started |
| INITIALIZATION_SUCCESS | Initialization completed successfully |
| INITIALIZATION_FAILED | Initialization failed |

## Next Steps

- [Integrate SDK Methods](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter)

- [See All Integrations Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-flutter)

	 [](https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-flutter)

[Back to top](https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-flutter)
