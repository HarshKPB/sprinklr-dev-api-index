---
title: "Initialize Sprinklr Survey Kit SDK for React Native"
slug: initialize-sprinklr-survey-kit-sdk-for-react-native
url: https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-react-native
---

# Initialize Sprinklr Survey Kit SDK for React Native

# Initialize Sprinklr Survey Kit SDK for React Native

Initialize the Sprinklr Survey Kit SDK. In this step, the SDK is initialized with the App ID, environment, and device ID. To confirm whether the initialization was successful, you can listen to the `INITIALIZATION_SUCCESS` event.


## Method



initializeProject(config: SurveyProjectConfig): Promise

## Syntax




interface SurveyProjectConfig {
  appId: string;           // Your Sprinklr app ID (required)
  environment: string;     // Environment (e.g., 'PROD2', 'PROD3') (required)
  deviceId?: string;       // Unique device identifier (optional)
  autoEvaluate?: boolean;  // Auto-evaluate intercepts (optional, default: true)
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
| deviceId | Optional | String | A unique ID for the user’s device. |
| environment | Required | String | The Sprinklr environment where the app is running. For example, PROD2.Determine the Environment:       The Environment is the name of the live production environment where your instance of Sprinklr is hosted, such as PROD, PROD2, PROD3.        Dev Notes: Reach out to the Sprinklr Team to obtain the name of your Production Environment. |
| autoEvaluate | Optional | Boolean | If true, intercepts are automatically evaluated after initialization. Supported Values: true (Default), false. |

## Response












      ````



| Return Type | Values | Description |
| --- | --- | --- |
| Promise<boolean> | true, false | Resolves to true if initialization succeeds, false otherwise. |

### Example



import { initializeProject } from '@sprinklrjs/survey-kit';
const initialize = async () => {
  try {
    const success = await initializeProject({
      appId: '68776f7cd1db742044c49639_app_1000528027',
      environment: 'PROD2',
      deviceId: '12345',
      autoEvaluate: true,
    });
    if (success) {
      console.log('SDK initialized');
    }
  } catch (error) {
    console.error('Initialization failed:', error);
  }
};

### Events Emitted

This SDK emits specific events during its lifecycle. You can listen to these events to monitor initialization progress, handle success or failure states, and trigger custom logic in your application.


















| Event | Description |
| --- | --- |
| INITIALIZATION_STARTING | Initialization process has started |
| INITIALIZATION_SUCCESS | Initialization completed successfully |
| INITIALIZATION_FAILED | Initialization failed |

## Next Steps

- [Integrate SDK Methods](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native)

- [See All Integrations Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-react-native)

	 [](https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-react-native)

[Back to top](https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-react-native)
