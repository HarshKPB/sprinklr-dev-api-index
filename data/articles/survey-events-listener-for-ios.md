---
title: "Survey Events Listener for iOS"
slug: survey-events-listener-for-ios
url: https://dev.sprinklr.com/survey-events-listener-for-ios
---

# Survey Events Listener for iOS

# Survey Events Listener for iOS
 

The Sprinklr Survey Kit SDK supports a comprehensive set of events that your app can listen to. These events provide real-time visibility into the lifecycle of intercepts, surveys, and user sessions.

## Supported Events











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
| Initialization |  |  |  |
|  | INITIALIZATION_STARTING | {} | Indicates the SDK has started initialization |
|  | INITIALIZATION_FAILED | { "error": String } | Triggered when the SDK fails to initialize |
|  | INITIALIZATION_SUCCESS | { "intercepts": [ { "id": String, "name": String, "interceptId": String, "creativeId": String } ] } | Indicates the SDK initialization was successful and provides loaded intercept details |
| Register View Visit |  |  |  |
|  | PAGE_VISIT_STARTING | { "page": String } | Indicates that a page visit is starting |
|  | PAGE_VISIT_FAILED | { "page": String, "error": String } | Indicates a failure occurred while tracking a page visit |
|  | PAGE_VISIT_SUCCESS | { "page": String } | Confirms that a page visit was successfully tracked |
| Register Button Click |  |  |  |
|  | BUTTON_CLICK_FAILED | { "buttonId": String, "error": String } | Indicates a failure while handling a button click |
|  | BUTTON_CLICK_SUCCESS | { "buttonId": String } | Confirms that a button click was handled successfully |
| Evaluate Intercept |  |  |  |
|  | INTERCEPT_EVALUATION_STARTING | { "interceptId": String } | Begins evaluating a specific intercept |
|  | INTERCEPT_EVALUATION_SUCCESS | { "passed": Boolean, "message": String, "interceptId": String } | Evaluation completed successfully and includes result and message |
|  | INTERCEPT_EVALUATION_FAILED | { "passed": false, "error": String, "interceptId": String } | Indicates the evaluation failed and provides the error message |
| Evaluate All Intercepts |  |  |  |
|  | ALL_INTERCEPTS_EVALUATION_STARTING | {} | Begins evaluation of all intercepts |
|  | ALL_INTERCEPTS_EVALUATION_SUCCESS | { "evaluationResults": [ { "passed": Boolean, "message": String, "interceptId": String } ] } | All intercepts evaluated successfully with individual results |
|  | ALL_INTERCEPTS_EVALUATION_FAILED | { "error": String } | Evaluation of all intercepts failed |
| Display Intercept |  |  |  |
|  | DISPLAY_INTERCEPT_STARTING | { "interceptId": String } | Begins displaying the creative for a specific intercept |
|  | DISPLAY_INTERCEPT_IN_PROGRESS | { "interceptId": String, "creativeType": String, "creativeId": String } | Indicates that the intercept creative is currently being shown |
|  | DISPLAY_INTERCEPT_SUCCESS | { "interceptId": String, "creativeType": String, "creativeId": String } | Creative shown successfully for the given intercept |
|  | DISPLAY_INTERCEPT_FAILED | { "interceptId": String, "creativeType"?: String, "creativeId"?: String, "error": String } | Failed to show the creative for the intercept |
|  | SURVEY_FORM_DISPLAY_STARTING | { "interceptId": String, "creativeId": String } | A survey form is about to be shown |
|  | SURVEY_FORM_DISPLAY_IN_PROGRESS | { "interceptId": String, "creativeId": String } | Survey form is currently being shown |
|  | SURVEY_FORM_DISPLAY_SUCCESS | { "interceptId": String, "creativeId": String } | Survey form was shown successfully |
|  | SURVEY_FORM_DISPLAY_FAILED | { "interceptId": String, "creativeId": String, "error": String } | Survey form failed to display |
| Display All Intercepts |  |  |  |
|  | DISPLAY_ALL_INTERCEPTS_STARTING | {} | Begins showing all eligible intercept creatives |
|  | DISPLAY_ALL_INTERCEPTS_SUCCESS | {} | All eligible intercept creatives were shown successfully |
|  | DISPLAY_ALL_INTERCEPTS_FAILED | { "error": String } | Failed to show intercept creatives |
| Close Intercept |  |  |  |
|  | CLOSE_DISPLAYED_INTERCEPT | { "interceptId": String, "creativeType": String, "creativeId": String } | Triggered when an intercept creative is closed by the user or the app |
|  | SURVEY_FORM_CLOSED | { "interceptId": String, "creativeId": String } | User closed the displayed survey form |
| Cleanup |  |  |  |
|  | SURVEY_MANAGER_CLEANUP | {} | Indicates the SDK has completed cleanup operations |
| Start Session Tracking |  |  |  |
|  | SESSION_TRACKING_STARTED | {} | Indicates that session tracking has started |
| Stop Session Tracking |  |  |  |
|  | SESSION_TRACKING_STOPPED | {} | Indicates that session tracking has stopped |

## Listening to Events

Follow these steps to listen to the events:

### Swift

- Conform to the `SPREventsHandler` protocol:



 Copy Code


class ClassName: SPREventsHandler



- Assign the event handler before initializing the project:



 Copy Code


SPRSurveyManager.shared.eventHandler = self



- Implement the event listener method:

The `eventData` parameter contains event details in stringified JSON format.





 Copy Code



func onEvent(_ eventType: SPREventType, eventData: String) {
    // Handle event here
}




### Objective C

- Conform to the `SPREventsHandler` protocol:



 Copy Code


@interface ClassName ()
@end



- Assign the event handler before initializing the project:



 Copy Code


[SPRMessenger shared].eventHandler = self;



- Implement the event listener method:

The `eventData` parameter contains event details in stringified JSON format.





 Copy Code


- (void)onEvent:(SPREventType)eventType eventData:(NSString *)eventData {
    // Handle event here
}




## Related Resources

See [All Integrations Steps](https://dev.sprinklr.com/cfm-survey-kit-sdk-for-ios)

	 [](https://dev.sprinklr.com/survey-events-listener-for-ios)

[Back to top](https://dev.sprinklr.com/survey-events-listener-for-ios)
