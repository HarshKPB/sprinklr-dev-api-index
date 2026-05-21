---
title: "Sprinklr Survey Kit SDK Methods for iOS"
slug: sprinklr-survey-kit-sdk-methods-for-ios
url: https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-ios
---

# Sprinklr Survey Kit SDK Methods for iOS

# Sprinklr Survey Kit SDK Methods for iOS

The `SPRSurveyManager` class provides a suite of methods that allow developers to manage and display in-app surveys, track user interactions, and control when and how these surveys appear.


These methods enable dynamic survey delivery based on user behavior, app navigation, or predefined targeting logic. By evaluating intercepts, displaying creatives, and logging user actions like view visits and button clicks, you can deliver highly contextual and personalized survey experiences within your app.

## SDK Methods Quick Reference







    [Evaluate Intercept](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-ios#evaluate-intercept)
    ``



    [Evaluate All Intercepts](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-ios#evaluate-all-intercepts)
    ``



    [Display Intercept](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-ios#display-intercept)
    ``



    [Display All Intercepts](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-ios#display-all-intercepts)
    ``



    [Register View Visit](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-ios#register-view-visit)
    ``



    [Register Button Click](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-ios#register-button-click)
    ``



    [Start Session Tracking](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-ios#start-session-tracking)
    ``



    [Stop Session Tracking](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-ios#stop-session-tracking)
    ``



| SDK Method Name | Method | Purpose |
| --- | --- | --- |
|  | evaluateIntercept | Evaluates a specific intercept to determine if it should be shown. |
|  | evaluateAllIntercepts | Evaluates all intercepts asynchronously. |
|  | displayIntercept | Displays the creative for a specific, evaluated intercept. |
|  | displayAllIntercepts | Displays all passing intercepts not yet shown in the current session. |
|  | registerViewVisit | Logs a user’s visit to a specific view or screen in the app. |
|  | registerButtonClick | Logs a button click within a specified view for tracking or targeting. |
|  | startSessionTracking | Starts tracking the time a user spends in the app for evaluating intercepts based on session duration. |
|  | stopSessionTracking | Stops tracking the time a user spends in the app. |

## Evaluate Intercept

This method asynchronously evaluates the given intercept and emits the `INTERCEPT_EVALUATION_SUCCESS` event with a result object. The result object indicates the outcome of the evaluation for the given intercept. It contains a Boolean value with the key `passed` and a string with the key `id`, which represents the `interceptId`.

**Dev Notes: **The method also emits starting and failure events that you can listen to for tracking the evaluation lifecycle. For more details, see the [INTERCEPT_EVALUATION](https://dev.sprinklr.com/survey-events-listener-for-ios#evaluate-intercept) events documentation.

### Method

#### Swift




 Copy Code


SPRSurveyManager.shared.evaluateIntercept(interceptId: "INTERCEPT_ID")



#### Objective C




 Copy Code


SPRSurveyManager.shared.evaluateIntercept(interceptId: "INTERCEPT_ID")



### Parameters












****


| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| interceptId | Required | String | The unique identifier of the intercept to be evaluated.See Steps to Retrieve Intercept ID given below. |

#### Steps to Retrieve Intercept ID


You can obtain the Intercept ID from the Sprinklr UI. Make sure you have created an In-App distribution and defined its variants for your survey.


To copy the Intercept ID:


- Open the CFM Persona App.

- In the side navigation panel, click **Programs**.

- Locate the survey you want to use.

- Hover over the survey and click **View**.

- Go to the **Distribution** tab.

- Find the distribution of type **In App**.

- Click the three-dot icon next to the distribution name.

- Select **Copy Variant ID**.

- In the pop-up window, choose the intercept variant for which you need the ID, and click **Copy ID**.

## Evaluate All Intercepts

This method asynchronously evaluates all intercepts and emits the **ALL_INTERCEPTS_EVALUATION_SUCCESS** event with a result object.

The result object is an array of all intercepts, indicating the outcome of the evaluation for each intercept.Each result object contains a Boolean value with the key `passed` and a string with the key `id`, which is the `interceptId`.

**Dev Notes: **The method also emits starting and failure events that you can listen to for tracking the evaluation lifecycle. For more details, see the [ALL_INTERCEPTS_EVALUATION](https://dev.sprinklr.com/survey-events-listener-for-ios#evaluate-all-intercepts) events documentation.

### Method

#### Swift




 Copy Code


SPRSurveyManager.shared.evaluateAllIntercepts()



#### Objective C




 Copy Code


[[SPRSurveyManager shared] evaluateAllIntercepts];



## Display Intercept

This method displays the creative associated with the passing action set for the given intercept and emits the **DISPLAY_INTERCEPT_SUCCESS** event.

Before using this method, use the `evaluateIntercept` methods to determine whether the creative should be displayed by evaluating an intercept logic.

**Dev Notes: **The method also emits starting and failure events that you can listen to for tracking the evaluation lifecycle. For more details, see the [DISPLAY_INTERCEPT](https://dev.sprinklr.com/survey-events-listener-for-ios#display-intercept) events documentation.

### Method

#### Swift




 Copy Code


SPRSurveyManager.shared.displayIntercept(interceptId: "INTERCEPT_ID")



#### Objective C




 Copy Code


[[SPRSurveyManager shared] displayInterceptWithInterceptId:@"INTERCEPT_ID"];



#### Steps to Retrieve Intercept ID


You can obtain the Intercept ID from the Sprinklr UI. Make sure you have created an In-App distribution and defined its variants for your survey.


To copy the Intercept ID:


- Open the CFM Persona App.

- In the side navigation panel, click **Programs**.

- Locate the survey you want to use.

- Hover over the survey and click **View**.

- Go to the **Distribution** tab.

- Find the distribution of type **In App**.

- Click the three-dot icon next to the distribution name.

- Select **Copy Variant ID**.

- In the pop-up window, choose the intercept variant for which you need the ID, and click **Copy ID**.

## Display All Intercepts

This method displays all the creatives which have been evaluated and have not been displayed in the current session and emits the **DISPLAY_ALL_INTERCEPTS_SUCCESS** event.

**Dev Notes: **The method also emits starting and failure events that you can listen to for tracking the evaluation lifecycle. For more details, see the [DISPLAY_ALL_INTERCEPTS](https://dev.sprinklr.com/survey-events-listener-for-ios#display-all-intercepts) events documentation.

### Method

#### Swift




 Copy Code


SPRSurveyManager.shared.displayAllIntercepts()



#### Objective C




 Copy Code


[[SPRSurveyManager shared] displayAllIntercepts];



## Register View Visit

You can use this method to record visits to a particular view.

**Dev Notes: **The method emits starting, success and failure events that you can listen to for tracking the evaluation lifecycle. For more details, see the [PAGE_VISIT](https://dev.sprinklr.com/survey-events-listener-for-ios#register-view-visit) events documentation.

### Method

#### Swift




 Copy Code


SPRSurveyManager.shared.registerViewVisit(viewName: "VIEW_NAME")



#### Objective C




 Copy Code


[[SPRSurveyManager shared] registerViewVisitWithViewName:@"VIEW_NAME"];



### Parameters













****
****

[Setting up the In-App distribution with Trigger Conditions](https://www.sprinklr.com/help/articles/setting-up-the-inapp-distribution/setting-up-the-inapp-distribution-with-trigger-conditions/68d127d4c8792738a6f8f282)


| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| viewName | Required | String | The unique name or identifier of the view (screen/page) being visited.       Ensure that a variant (intercept) is created using this viewName in the Sprinklr UI.       In the CFM Persona App, open the required survey and create an In-App distribution. Then, create a Variant for this distribution with the following configuration:       Condition: Screen Views       Field: App Screen Id (specify this viewName value)       For detailed steps, see . |

## Register Button Click

You can use this method to record a particular button click inside a view.

**Dev Notes: **The method emits success and failure events that you can listen to for tracking the evaluation lifecycle. For more details, see the [BUTTON_CLICK](https://dev.sprinklr.com/survey-events-listener-for-ios#register-button-click) events documentation.

### Method

#### Swift




 Copy Code


SPRSurveyManager.shared.registerButtonClick(buttonId: "BUTTON_ID"))



#### Objective C




 Copy Code


[[SPRSurveyManager shared] registerButtonClickWithButtonId:@"BUTTON_ID"];



### Parameters













****
****

[Setting up the In-App distribution with Trigger Conditions](https://www.sprinklr.com/help/articles/setting-up-the-inapp-distribution/setting-up-the-inapp-distribution-with-trigger-conditions/68d127d4c8792738a6f8f282)


| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| viewName | Required | String | The unique name or identifier of the view (screen/page) being visited.       Ensure that a variant (intercept) is created using this viewName in the Sprinklr UI.       In the CFM Persona App, open the required survey and create an In-App distribution. Then, create a Variant for this distribution with the following configuration:       Condition: Screen Views       Field: App Screen Id (specify this viewName value)       For detailed steps, see . |

## Start Session Tracking

This method starts tracking time spent by user on application for tracking and evaluating intercepts based on session duration.

**Dev Notes: **The method emits the SESSION_TRACKING_STARTED event that you can listen to. For more details, see the [SESSION_TRACKING_STARTED](https://dev.sprinklr.com/survey-events-listener-for-ios#start-session-tracking) events documentation.

### Method

#### Swift




 Copy Code


SPRSurveyManager.shared.startSessionTracking()



#### Objective C




 Copy Code


[[SPRSurveyManager shared] startSessionTracking];



## Stop Session Tracking

This method stops tracking time spent by user on the application.

**Dev Notes: **The method emits the SESSION_TRACKING_STOPPED event that you can listen to. For more details, see the [SESSION_TRACKING_STOPPED](https://dev.sprinklr.com/survey-events-listener-for-ios#stop-session-tracking) events documentation.

### Method

#### Swift




 Copy Code


SPRSurveyManager.shared.stopSessionTracking()



#### Objective C




 Copy Code


[[SPRSurveyManager shared] stopSessionTracking];



## Cleanup

You can call cleanup to clean associated data from the application.

**Dev Notes: **The method emits the SURVEY_MANAGER_CLEANUP event that you can listen to that indicates the SDK has completed cleanup operations. For more details, see the [SURVEY_MANAGER_CLEANUP](https://dev.sprinklr.com/survey-events-listener-for-ios#cleanup) event documentation.

### Method

#### Swift




 Copy Code


SPRSurveyManager.shared.cleanup()



#### Objective C




 Copy Code


[[SPRSurveyManager shared] cleanup];



## Next Steps

- Perform Advanced Configurations such as [Listen to SDK Events](https://dev.sprinklr.com/survey-events-listener-for-ios) or [Enable Survey Events Logging](https://dev.sprinklr.com/enable-survey-events-logging-for-ios)

- See [All Integrations Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-ios)

	 [](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-ios)

[Back to top](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-ios)
