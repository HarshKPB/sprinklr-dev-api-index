---
title: "Sprinklr Survey Kit SDK"
slug: sprinklr-survey-kit-sdk
url: https://dev.sprinklr.com/sprinklr-survey-kit-sdk
---

# Sprinklr Survey Kit SDK

# Customer Feedback Management (CFM) Survey Kit SDK
 

The Sprinklr Survey Kit SDK allows you to seamlessly integrate Sprinklr's Customer Feedback Management (CFM) module into your app. It allows you to display surveys within users’ mobile app based on targeting rules such as pages they’ve viewed or buttons they’ve clicked.


## Supported Platforms


The Sprinklr Survey Kit SDK is supported on the following platforms:




      ****
      ****




      ****
      [Android Integration Documentation](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-android)


      ****
      [iOS Integration Documentation](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-ios)


      ****
      [React Native Integration Documentation](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-react-native)


      ****
      [Flutter Integration Documentation](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-flutter)



| Platform | Documentation |
| --- | --- |
| Android | Refer to |
| iOS | Refer to |
| React Native | Refer to |
| Flutter | Refer to |

## Key Concepts

The following are the key concepts you must understand before you begin with the integration:

### SPRSurveyManager

The `SPRSurveyManager` class enables your app to interact with Sprinklr Surveys. You can initialize `SPRSurveyManager` with the App ID, environment name, and device ID. For more information, see [Initialize Sprinklr Survey Kit for Android](https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-android) or [Initialize Sprinklr Survey Kit for iOS](https://dev.sprinklr.com/initialize-sprinklr-survey-kit-sdk-for-ios).

### Intercepts

Intercepts are rules or conditions set within an app that determine when a survey or creative (pop-up) should be shown to a user.

In Sprinklr, for In-App survey distributions, you can configure **Intercept Conditions**, which may include factors such as the user’s OS version, session duration, number of screen views, whether a survey has already been shown, geographic location, and more. These conditions can be combined using logical operators.

When a user's session matches the defined conditions, the intercept is triggered, and the survey or creative is displayed accordingly.

**Related Knowledge Base Article: **[Setting Up the In-App distribution with Trigger Conditions](https://www.sprinklr.com/help/articles/setting-up-the-inapp-distribution/setting-up-the-inapp-distribution-with-trigger-conditions/68d127d4c8792738a6f8f282).

### Intercept Evaluation

You can control how intercepts are evaluated using the **autoEvaluate** flag.


- **Automatic Evaluation**: To have the Survey Kit automatically evaluate intercepts and display creatives when the evaluation is successful, set the `autoEvaluate` flag to **true** in the `SPRSurveyProjectConfig`.

- **Manual Evaluation**: If you prefer more control over when intercepts are evaluated and displayed, set the `autoEvaluate` flag to **false** and manually call the `evaluateIntercept` or `evaluateAllIntercepts` method.

These methods asynchronously check the server for intercept display logic. After evaluating the intercept, the SDK emits an event containing a **TargetingResult** object, which indicates whether the creative should be displayed. You can also display the creative at any time without checking if the evaluation is successful.

### Intercept Display Logic

The Mobile App intercept supports the following display logic condition types:


- **App Session: View Count**: This setting evaluates the intercept based on a specific number of pages viewed.


  - **Total Views**: Logic based on the total number of views in the app.

  - **Unique Views**: Logic based on the unique views encountered by the app user.



Refer to the **Register View Visit** section in the documentation to ensure that views are properly recorded via the SDK.


- **App Session: Button Clicks**: This setting evaluates the intercept based on the total number of clicks of a particular button within a specific screen.

Refer to the **Register Button Click** section in the documentation to ensure that button clicks are properly recorded via the SDK.


- **App Usage**: This setting evaluates the intercept based on the duration of app usage. If the app usage duration exceeds the specified threshold, the intercept is evaluated as true.

Additionally, some other intercepts are evaluated on the server side. Please refer to the knowledge base article for details on all In-App Conditions.

**Related Knowledge Base Article: **[CFM Surveys](https://www.sprinklr.com/help/articles/creating-programs-subprograms-and-surveys/creating-programs-subprograms-and-surveys/67fe70d9c14a394d14c58d5e#_336bd979-b80b-438a-bbd6-4e75bc15eb9d).

## Next Steps


- Refer to [Android Integration Documentation](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-android)

- Refer to [iOS Integration Documentation](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-ios)

- Refer to [React Native Integration Documentation](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-react-native)

- Refer to [Flutter Integration Documentation](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-flutter)

	 [](https://dev.sprinklr.com/sprinklr-survey-kit-sdk)

[Back to top](https://dev.sprinklr.com/sprinklr-survey-kit-sdk)
