---
title: "Sprinklr Survey Kit SDK Methods for React Native"
slug: sprinklr-survey-kit-sdk-methods-for-react-native
url: https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native
---

# Sprinklr Survey Kit SDK Methods for React Native

# Sprinklr Survey Kit SDK Methods for React Native

This page list the supported SDK methods for React Native.

## SDK Methods Quick Reference









    ****
    [Start Session Tracking](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native#start-session-tracking)






    [Stop Session Tracking](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native#stop-session-tracking)





    ****
    [Register View Visit](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native#register-view-visit)






    [Register Button Click](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native#register-button-click)





    ****
    [Evaluate Intercept](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native#evaluate-intercept)






    [Evaluate All Intercepts](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native#evaluate-all-intercepts)






    [Display Intercept](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native#display-intercept)






    [Display All Intercepts](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native#display-all-intercepts)





    ****
    [Cleanup](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native#cleanup)





| Category | Method Name | Signature | Purpose | Events Emitted |
| --- | --- | --- | --- | --- |
| Session Tracking |  | startSessionTracking(): void | Starts automatic session tracking to monitor user sessions and activity. | SESSION_TRACKING_STARTED |
|  |  | stopSessionTracking(): void | Stops automatic session tracking. | SESSION_TRACKING_STOPPED |
| User Actions |  | registerViewVisit(viewName: string): void | Logs a user’s visit to a specific view or screen. | SCREEN_VIEW_VISIT_STARTING, SCREEN_VIEW_VISIT_SUCCESS, SCREEN_VIEW_VISIT_FAILED |
|  |  | registerButtonClick(buttonId: string): void | Logs a button click within a specified view. | BUTTON_CLICK_SUCCESS, BUTTON_CLICK_FAILED |
| Intercept Management |  | evaluateIntercept(interceptId: string): void | Evaluates a specific intercept to determine if it should be displayed. | INTERCEPT_EVALUATION_STARTING, INTERCEPT_EVALUATION_SUCCESS, INTERCEPT_EVALUATION_FAILED |
|  |  | evaluateAllIntercepts(): void | Evaluates all configured intercepts for the current user context. | ALL_INTERCEPTS_EVALUATION_STARTING, ALL_INTERCEPTS_EVALUATION_SUCCESS, ALL_INTERCEPTS_EVALUATION_FAILED |
|  |  | displayIntercept(interceptId: string): void | Displays a specific intercept (survey) to the user. | DISPLAY_INTERCEPT_STARTING, DISPLAY_INTERCEPT_IN_PROGRESS, DISPLAY_INTERCEPT_SUCCESS, DISPLAY_INTERCEPT_FAILED |
|  |  | displayAllIntercepts(): void | Displays all eligible intercepts based on evaluation results. | DISPLAY_ALL_INTERCEPTS_STARTING, DISPLAY_ALL_INTERCEPTS_SUCCESS, DISPLAY_ALL_INTERCEPTS_FAILED |
| Cleanup |  | cleanup(): void | You can call cleanup to clean associated data from the application. Call this when you no longer need the SDK or before re-initializing. | SURVEY_MANAGER_CLEANUP |

## Start Session Tracking

 The `startSessionTracking()` method enables automatic monitoring of user sessions within your app. By starting session tracking, the SDK records session duration and activity.

### Method



startSessionTracking(): void



### Example



import { startSessionTracking } from '@sprinklrjs/survey-kit';
startSessionTracking();



### Events Emitted

| Event | Description |
| --- | --- |
| SESSION_TRACKING_STARTED | Session tracking has been successfully initiated. |

## Stop Session Tracking

 The `stopSessionTracking()` method stops automatic monitoring of user sessions within your app.

### Method



stopSessionTracking(): void



### Example



import { stopSessionTracking } from '@sprinklrjs/survey-kit';
stopSessionTracking();



### Events Emitted

| Event | Description |
| --- | --- |
| SESSION_TRACKING_STOPPED | Session tracking has been successfully stopped. |

## Register View Visit

The `registerViewVisit(viewName: string)` method logs a user’s visit to a specific view or screen within your app. This tracking helps the SDK evaluate intercepts and trigger surveys based on navigation behavior, providing contextually relevant feedback opportunities.

### Method



registerViewVisit(viewName: string): void



### Parameters













****
****

[Setting up the In-App distribution with Trigger Conditions](https://www.sprinklr.com/help/articles/setting-up-the-inapp-distribution/setting-up-the-inapp-distribution-with-trigger-conditions/68d127d4c8792738a6f8f282)


| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| viewName | Required | String | The unique name or identifier of the view (screen/page) being visited.       Ensure that a variant (intercept) is created using this viewName in the Sprinklr UI.       In the CFM Persona App, open the required survey and create an In-App distribution. Then, create a Variant for this distribution with the following configuration:       Condition: Screen Views       Field: App Screen Id (specify this viewName value)       For detailed steps, see . |

### Example



import { registerViewVisit } from '@sprinklrjs/survey-kit';
// Register page visit
registerViewVisit('HomePage');
registerViewVisit('ProductPage');
registerViewVisit('CheckoutPage');



### Events Emitted

| Event | Description |
| --- | --- |
| SCREEN_VIEW_VISIT_STARTING | View visit registration has started. |
| SCREEN_VIEW_VISIT_SUCCESS | View visit was successfully registered. |
| SCREEN_VIEW_VISIT_FAILED | View visit registration failed. |

## Register Button Click

 The `registerButtonClick(buttonId: string)` method registers a button click event within your app. It is used for tracking user interactions, allowing the SDK to evaluate intercepts and deliver surveys based on specific user actions such as clicks on purchase or navigation buttons.

### Method



registerButtonClick(buttonId: string)



### Parameters















| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| buttonId | Required | string | The ID or name of the button clicked. |

### Example



import { registerButtonClick } from '@sprinklrjs/survey-kit';
// In your component
 {
    registerButtonClick('buy_now_button');
    // ... handle purchase
  }}
/>



### Events Emitted

| Event | Description |
| --- | --- |
| BUTTON_CLICK_SUCCESS | Button click was successfully registered. |
| BUTTON_CLICK_FAILED | Button click registration failed. |

## Evaluate Intercept

 The `evaluateIntercept(interceptId: string)` method evaluates a specific intercept to determine whether it should be displayed based on targeting rules. It emits the `INTERCEPT_EVALUATION_SUCCESS` event when the evaluation completes successfully.

### Method



evaluateIntercept(interceptId: string)



### Parameters

| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| interceptId | Required | string | The unique identifier of the intercept to be evaluated. |

### Example



import { evaluateIntercept } from '@sprinklrjs/survey-kit';
evaluateIntercept('intercept_12345');



### Events Emitted

| Event | Description |
| --- | --- |
| INTERCEPT_EVALUATION_STARTING | Intercept evaluation has started. |
| INTERCEPT_EVALUATION_SUCCESS | Intercept evaluation completed successfully. |
| INTERCEPT_EVALUATION_FAILED | Intercept evaluation failed. |

## Evaluate All Intercepts

 The `evaluateAllIntercepts()` method evaluates all configured intercepts for the current user context.

### Method



evaluateAllIntercepts();



### Parameters

| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| interceptId | Required | string | The unique identifier of the intercept to be evaluated. |

### Example



import { evaluateAllIntercepts } from '@sprinklrjs/survey-kit';
evaluateAllIntercepts();



### Events Emitted


















| Event | Description |
| --- | --- |
| ALL_INTERCEPTS_EVALUATION_STARTING | All intercepts evaluation has started. |
| ALL_INTERCEPTS_EVALUATION_SUCCESS | All intercepts evaluation completed successfully. |
| ALL_INTERCEPTS_EVALUATION_FAILED | All intercepts evaluation failed. |

## Display Intercept

 The `displayIntercept(interceptId: string): void
` displays a specific intercept (survey) to the user.

### Method



displayIntercept('intercept_12345');



### Parameters














| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| interceptId | Required | string | The unique identifier of the intercept to be evaluated. |

### Example



import { displayIntercept } from '@sprinklrjs/survey-kit';
// Display specific intercept
displayIntercept('intercept_12345');



### Events Emitted






















| Event | Description |
| --- | --- |
| DISPLAY_INTERCEPT_STARTING | Display intercept process has started. |
| DISPLAY_INTERCEPT_IN_PROGRESS | Display intercept is currently in progress. |
| DISPLAY_INTERCEPT_SUCCESS | Display intercept completed successfully. |
| DISPLAY_INTERCEPT_FAILED | Display intercept failed. |

## Display All Intercepts

  The `displayAllIntercepts(): void` method displays all eligible intercepts (surveys) to the user based on evaluation results.

### Method



displayAllIntercepts();




### Example



import { displayAllIntercepts } from '@sprinklrjs/survey-kit';
// Show all eligible surveys
displayAllIntercepts();




### Events Emitted


















| Event | Description |
| --- | --- |
| DISPLAY_ALL_INTERCEPTS_STARTING | Display all intercepts process has started. |
| DISPLAY_ALL_INTERCEPTS_SUCCESS | Display all intercepts completed successfully. |
| DISPLAY_ALL_INTERCEPTS_FAILED | Display all intercepts failed. |

## Cleanup

You can call cleanup to clean associated data from the application. Call this when you no longer need the SDK or before re-initializing.

### Method



cleanup(): void



### Example



import { cleanup } from '@sprinklrjs/survey-kit';
// In your component cleanup
useEffect(() => {
  return () => {
    cleanup();
  };
}, []);



### Events Emitted














| Event | Description |
| --- | --- |
| SURVEY_MANAGER_CLEANUP | Indicates that the SDK has completed cleanup operations. |

## Next Steps

- Perform Advanced Configurations such as [Listen to SDK Events](https://dev.sprinklr.com/survey-events-listener-for-react-native) or [Enable Survey Events Logging](https://dev.sprinklr.com/enable-survey-events-logging-for-react-native)

- See [All Integrations Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-react-native)

	 [](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native)

[Back to top](https://dev.sprinklr.com/sprinklr-survey-kit-sdk-methods-for-react-native)
