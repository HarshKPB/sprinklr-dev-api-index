---
title: "Sprinklr Survey Kit SDK Methods for Flutter"
slug: sprinklr-survey-kit-sdk-methods-for-flutter
url: https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter
---

# Sprinklr Survey Kit SDK Methods for Flutter

# Sprinklr Survey Kit SDK Methods for Flutter

This page list the supported SDK methods for Flutter.

## SDK Methods Quick Reference









    ****
    [Start Session Tracking](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter#start-session-tracking)






    [Stop Session Tracking](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter#stop-session-tracking)





    ****
    [Register View Visit](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter#register-view-visit)






    [Register Button Click](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter#register-button-click)





    ****
    [Evaluate Intercept](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter#evaluate-intercept)






    [Evaluate All Intercepts](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter#evaluate-all-intercepts)






    [Display Intercept](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter#display-intercept)






    [Display All Intercepts](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter#display-all-intercepts)





    ****
    [Cleanup](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter#cleanup)





| Category | Method Name | Signature | Purpose | Events Emitted |
| --- | --- | --- | --- | --- |
| Session Tracking |  | void startSessionTracking() | Starts automatic session tracking to monitor user sessions and activity. | SESSION_TRACKING_STARTED |
|  |  | void stopSessionTracking() | Stops automatic session tracking. | SESSION_TRACKING_STOPPED |
| User Actions |  | void registerViewVisit(String viewName) | Logs a user’s visit to a specific view or screen. | SCREEN_VIEW_VISIT_STARTING, SCREEN_VIEW_VISIT_SUCCESS, SCREEN_VIEW_VISIT_FAILED |
|  |  | void registerButtonClick(String buttonId) | Logs a button click within a specified view. | BUTTON_CLICK_SUCCESS, BUTTON_CLICK_FAILED |
| Intercept Management |  | void evaluateIntercept(String interceptId) | Evaluates a specific intercept to determine if it should be displayed. | INTERCEPT_EVALUATION_STARTING, INTERCEPT_EVALUATION_SUCCESS, INTERCEPT_EVALUATION_FAILED |
|  |  | void evaluateAllIntercepts() | Evaluates all configured intercepts for the current user context. | ALL_INTERCEPTS_EVALUATION_STARTING, ALL_INTERCEPTS_EVALUATION_SUCCESS, ALL_INTERCEPTS_EVALUATION_FAILED |
|  |  | void displayIntercept(String interceptId) | Displays a specific intercept (survey) to the user. | DISPLAY_INTERCEPT_STARTING, DISPLAY_INTERCEPT_IN_PROGRESS, DISPLAY_INTERCEPT_SUCCESS, DISPLAY_INTERCEPT_FAILED |
|  |  | void displayAllIntercepts() | Displays all eligible intercepts based on evaluation results. | DISPLAY_ALL_INTERCEPTS_STARTING, DISPLAY_ALL_INTERCEPTS_SUCCESS, DISPLAY_ALL_INTERCEPTS_FAILED |
| Cleanup |  | void cleanup() | You can call cleanup to clean associated data from the application. Call this when you no longer need the SDK or before re-initializing. | SURVEY_MANAGER_CLEANUP |

## Start Session Tracking

 The `startSessionTracking()` method enables automatic monitoring of user sessions within your app. By starting session tracking, the SDK records user sessions and activity.

### Method



void startSessionTracking()



### Example



surveyKit.startSessionTracking();



### Events Emitted










| Event | Description |
| --- | --- |
| SESSION_TRACKING_STARTED | Session tracking has been successfully initiated. |

## Stop Session Tracking

 The `stopSessionTracking()` method stops automatic monitoring of user sessions within your app.

### Method



void stopSessionTracking()



### Example



surveyKit.stopSessionTracking();



### Events Emitted










| Event | Description |
| --- | --- |
| SESSION_TRACKING_STOPPED | Session tracking has been successfully stopped. |

## Register View Visit

The `registerViewVisit(String viewName)` method logs a user’s visit to a specific view or screen within your app. This tracking helps the SDK evaluate intercepts and trigger surveys based on navigation behavior, providing contextually relevant feedback opportunities.

### Method



void registerViewVisit(String viewName)



### Parameters













****
****

[Setting up the In-App distribution with Trigger Conditions](https://www.sprinklr.com/help/articles/setting-up-the-inapp-distribution/setting-up-the-inapp-distribution-with-trigger-conditions/68d127d4c8792738a6f8f282)


| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| viewName | Required | String | The unique name or identifier of the view (screen/page) being visited.       Ensure that a variant (intercept) is created using this viewName in the Sprinklr UI.       In the CFM Persona App, open the required survey and create an In-App distribution. Then, create a Variant for this distribution with the following configuration:       Condition: Screen Views       Field: App Screen Id (specify this viewName value)       For detailed steps, see . |

### Example



surveyKit.registerViewVisit('HomePage');
surveyKit.registerViewVisit('ProductPage');
surveyKit.registerViewVisit('CheckoutPage');



### Events Emitted


















| Event | Description |
| --- | --- |
| SCREEN_VIEW_VISIT_STARTING | View visit registration has started. |
| SCREEN_VIEW_VISIT_SUCCESS | View visit was successfully registered. |
| SCREEN_VIEW_VISIT_FAILED | View visit registration failed. |

## Register Button Click

 The `registerButtonClick(String buttonId)` method registers a button click event within your app. It is used for tracking user interactions, allowing the SDK to evaluate intercepts and deliver surveys based on specific user actions such as clicks on purchase or navigation buttons.

### Method



registerButtonClick(String buttonId)



### Parameters















| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| buttonId | Required | string | The ID or name of the button clicked. |

### Example



surveyKit.registerButtonClick('buy_now_button');



### Events Emitted














| Event | Description |
| --- | --- |
| BUTTON_CLICK_SUCCESS | Button click was successfully registered. |
| BUTTON_CLICK_FAILED | Button click registration failed. |

## Evaluate Intercept

 The `evaluateIntercept(String interceptId)` method evaluates a specific intercept to determine whether it should be displayed based on targeting rules. It emits the `INTERCEPT_EVALUATION_SUCCESS` event when the evaluation completes successfully.

### Method



void evaluateIntercept(String interceptId)



### Parameters


















| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| interceptId | Required | string | The unique identifier of the intercept to be evaluated. |

### Example



surveyKit.evaluateIntercept('intercept_12345');



### Events Emitted






















| Event | Description |
| --- | --- |
| INTERCEPT_EVALUATION_STARTING | Intercept evaluation has started. |
| INTERCEPT_EVALUATION_SUCCESS | Intercept evaluation completed successfully. |
| INTERCEPT_EVALUATION_FAILED | Intercept evaluation failed. |

## Evaluate All Intercepts

 The `evaluateAllIntercepts()` method evaluates all configured intercepts for the current user context.

### Method



void evaluateAllIntercepts()



### Parameters


















| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| interceptId | Required | string | The unique identifier of the intercept to be evaluated. |

### Example



surveyKit.evaluateAllIntercepts();



### Events Emitted


















| Event | Description |
| --- | --- |
| ALL_INTERCEPTS_EVALUATION_STARTING | All intercepts evaluation has started. |
| ALL_INTERCEPTS_EVALUATION_SUCCESS | All intercepts evaluation completed successfully. |
| ALL_INTERCEPTS_EVALUATION_FAILED | All intercepts evaluation failed. |

## Display Intercept

 The `displayIntercept(String interceptId)` displays a specific intercept (survey) to the user.

### Method



void displayIntercept(String interceptId)



### Parameters














| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| interceptId | Required | string | The unique identifier of the intercept to be evaluated. |

### Example



surveyKit.displayIntercept('intercept_12345');



### Events Emitted






















| Event | Description |
| --- | --- |
| DISPLAY_INTERCEPT_STARTING | Display intercept process has started. |
| DISPLAY_INTERCEPT_IN_PROGRESS | Display intercept is currently in progress. |
| DISPLAY_INTERCEPT_SUCCESS | Display intercept completed successfully. |
| DISPLAY_INTERCEPT_FAILED | Display intercept failed. |

## Display All Intercepts

  The `displayAllIntercepts()` method displays all eligible intercepts (surveys) to the user based on evaluation results.

### Method



void displayAllIntercepts()




### Example



surveyKit.displayAllIntercepts();




### Events Emitted


















| Event | Description |
| --- | --- |
| DISPLAY_ALL_INTERCEPTS_STARTING | Display all intercepts process has started. |
| DISPLAY_ALL_INTERCEPTS_SUCCESS | Display all intercepts completed successfully. |
| DISPLAY_ALL_INTERCEPTS_FAILED | Display all intercepts failed. |

## Cleanup

You can call cleanup to clean associated data from the application. Call this when you no longer need the SDK or before re-initializing.

**Dev Notes: **In addition to calling `cleanup`, ensure that you cancel your `eventSub` and `logSub` stream subscriptions in the widget’s `dispose()` method (or equivalent teardown logic).

### Method



void cleanup()



### Example



@override
void dispose() {
  surveyKit.cleanup();
  super.dispose();
}



### Events Emitted














| Event | Description |
| --- | --- |
| SURVEY_MANAGER_CLEANUP | Indicates that the SDK has completed cleanup operations. |

## Next Steps

- Perform Advanced Configurations such as [Listen to SDK Events](https://dev.sprinklr.com/survey-events-listener-for-flutter) or [Enable Survey Events Logging](https://dev.sprinklr.com/enable-survey-events-logging-for-flutter)

- See [All Integrations Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-flutter)

	 [](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter)

[Back to top](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-flutter)
