---
title: "Survey Events Listener for Flutter"
slug: survey-events-listener-for-flutter
url: https://dev.sprinklr.com/survey-events-listener-for-flutter
---

# Survey Events Listener for Flutter

# Survey Events Listener for Flutter

The Sprinklr Survey Kit SDK supports a comprehensive set of events that your app can listen to. These events provide real-time visibility into the lifecycle of intercepts, surveys, and user sessions.

## Supported Events

#### Events Emitted









    ****


















    ****

















    ****












    ****

















    ****

















    ****












    ****
























    ****






























    ****


















    ****





    ****





| Related SDK Method or Purpose | Event Type | Payload | Description |
| --- | --- | --- | --- |
| Initialization | INITIALIZATION_STARTING | {} | Indicates the SDK has started initialization. |
|  | INITIALIZATION_FAILED | { "error": String } | Triggered when the SDK fails to initialize. |
|  | INITIALIZATION_SUCCESS | { "intercepts": [ { "id": String, "name": String, "interceptId": String, "creativeId": String } ] } | Indicates the SDK initialization was successful and provides loaded intercept details. |
| Register Screen View Visit | SCREEN_VIEW_VISIT_STARTING | { "page": String } | Indicates that a screen view visit is starting. |
|  | SCREEN_VIEW_VISIT_FAILED | { "page": String, "error": String } | Indicates a failure occurred while tracking a screen view visit. |
|  | SCREEN_VIEW_VISIT_SUCCESS | { "page": String } | Confirms that a screen view visit was successfully tracked. |
| Register Button Click | BUTTON_CLICK_FAILED | { "buttonId": String, "error": String } | Indicates a failure while handling a button click. |
|  | BUTTON_CLICK_SUCCESS | { "buttonId": String } | Confirms that a button click was handled successfully. |
| Evaluate Intercept | INTERCEPT_EVALUATION_STARTING | { "interceptId": String } | Begins evaluating a specific intercept. |
|  | INTERCEPT_EVALUATION_SUCCESS | { "passed": Boolean, "message": String, "interceptId": String } | Evaluation completed successfully and includes result and message. |
|  | INTERCEPT_EVALUATION_FAILED | { "passed": false, "error": String, "interceptId": String } | Indicates the evaluation failed and provides the error message. |
| Evaluate All Intercepts | ALL_INTERCEPTS_EVALUATION_STARTING | {} | Begins evaluation of all intercepts. |
|  | ALL_INTERCEPTS_EVALUATION_SUCCESS | { "evaluationResults": [ { "passed": Boolean, "message": String, "interceptId": String } ] } | All intercepts evaluated successfully with individual results. |
|  | ALL_INTERCEPTS_EVALUATION_FAILED | { "error": String } | Evaluation of all intercepts failed. |
| Session Tracking | SESSION_TRACKING_STARTED | {} | Indicates that session tracking has started. |
|  | SESSION_TRACKING_STOPPED | {} | Indicates that session tracking has stopped. |
| Display Intercept | DISPLAY_INTERCEPT_STARTING | { "interceptId": String } | Begins displaying the creative for a specific intercept. |
|  | DISPLAY_INTERCEPT_IN_PROGRESS | { "interceptId": String, "creativeType": String, "creativeId": String } | Indicates that the intercept creative is currently being shown. |
|  | DISPLAY_INTERCEPT_SUCCESS | { "interceptId": String, "creativeType": String, "creativeId": String } | Creative shown successfully for the given intercept. |
|  | DISPLAY_INTERCEPT_FAILED | { "interceptId": String, "creativeType"?: String, "creativeId"?: String, "error": String } | Failed to show the creative for the intercept. |
| Survey Form | SURVEY_FORM_DISPLAY_STARTING | { "interceptId": String, "creativeId": String } | A survey form is about to be shown. |
|  | SURVEY_FORM_DISPLAY_IN_PROGRESS | { "interceptId": String, "creativeId": String } | Survey form is currently being shown. |
|  | SURVEY_FORM_DISPLAY_SUCCESS | { "interceptId": String, "creativeId": String } | Survey form was shown successfully. |
|  | SURVEY_FORM_DISPLAY_FAILED | { "interceptId": String, "creativeId": String, "error": String } | Survey form failed to display. |
|  | SURVEY_FORM_CLOSED | { "interceptId": String, "creativeId": String } | User closed the displayed survey form. |
| Display All Intercepts | DISPLAY_ALL_INTERCEPTS_STARTING | {} | Begins showing all eligible intercept creatives. |
|  | DISPLAY_ALL_INTERCEPTS_SUCCESS | {} | All eligible intercept creatives were shown successfully. |
|  | DISPLAY_ALL_INTERCEPTS_FAILED | { "error": String } | Failed to show intercept creatives. |
| Close Intercept | CLOSE_DISPLAYED_INTERCEPT | { "interceptId": String, "creativeType": String, "creativeId": String } | Triggered when an intercept creative is closed by the user or the app. |
| Cleanup | SURVEY_MANAGER_CLEANUP | {} | Indicates the SDK has completed cleanup operations. |

## Register Event Handler

You can register an event handler to listen for SDK events and respond to them in your application. In Flutter, events are delivered via a stream:

### Method



import 'dart:async';
import 'package:spr_survey_kit/spr_survey_kit.dart';
StreamSubscription? eventSub;
Future registerEventHandler() async {
  eventSub = await surveyKit.onEvent((EventData event) {
    final EventType type = event.eventType;
    final String data = event.eventData;
    // Handle specific events
    switch (type) {
      case EventType.INITIALIZATION_SUCCESS:
        // SDK ready to use
        break;
      case EventType.SURVEY_FORM_DISPLAY_SUCCESS:
        // Survey displayed to user
        break;
      case EventType.SURVEY_FORM_CLOSED:
        // User closed the survey
        break;
      default:
        break;
    }
  });
}



### Parameters


























| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| callback | Required | Function | The function called when events occur. |
| eventType | Required | EventType | The type of event emitted by the SDK. |
| eventData | Required | string | JSON string containing the event payload. |

## Related Resources

See [All Integrations Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-flutter)

[](https://dev.sprinklr.com/survey-events-listener-for-flutter)

[Back to top](https://dev.sprinklr.com/survey-events-listener-for-flutter)
