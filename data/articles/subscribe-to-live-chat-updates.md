---
title: "Subscribe to Live Chat Updates"
slug: subscribe-to-live-chat-updates
url: https://dev.sprinklr.com/subscribe-to-live-chat-updates
---

# Subscribe to Live Chat Updates

# Subscribe to Live Chat Updates


This method is used to either receive updates from Live Chat about the current state or listen to the status of the SDK requests made previously. For example, it can be used to listen to the success or failure notification of a [sendExternalEvent](https://spr-apigee-prod-apiprodportal.apigee.io/send-message-event-to-conversation) SDK request.

This method can also notify when the chat changes its availability status (if availability conditions are specified in Live Chat builder causing the chat to change state dynamically).

## Method

`sprChat(‘subscribeToUpdate’);`

## Parameters







| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| topic | String | Required | The topic that you want to subscribe to. For the list of topics and their definition, see the Topics table. |
| subscriber | (params: {     request: StringAnyMap;     response: {     data: StringAnyMap;     error: StringAnyMap;       };   }) => void; | Required | The callback function that is invoked when a matching update is available. For the definitions of request and response, see the Subscriber table. |

###

### Topics

Topics are the events that you can subscribe to. The following table describes the events that you can subscribe to:







| Topic | Description |
| --- | --- |
| availabilityChanged | Live Chat’s availability event. |
| unreadCountChanged | Notifies the count of all the conversations. |
| externalEventTriggered | The external event triggered by bot/rule flow. |
| loadCompleted | Notifies whether Live Chat is loaded successfully or not. |
| eventTriggered | Different analytics events of Live Chat. |
| openNewConversation | Indicates whether a new conversation is created or not. |
| sendExternalEvent | Indicates whether an external event is sent to the conversation or not. |

### Subscriber

This function is a callback that is invoked when a matching update is available. The following table explains the additional parameters that were sent with the SDK request where the SDK is the one for which this subscriber is notifying:

These parameters are passed in the `params` section of the `subscriber` function.





| Parameter | Description |
| --- | --- |
| request | The callback function receives a request object only when this notifier is for the response of an SDK invocation. It contains all the parameters that were passed when the SDK request was made. |
| response | The callback function also receives a response object containing data. The structure of data depends on the topic. You can find the structure for each topic in the Examples section. The response object can also carry error which are pre-defined set of errors. You can find the error list in the Examples section. |
| data | Any data to be shared after the SDK invocation was successful or data to be shared for chat application state. |
| error | Error that occurred while executing the SDK. |

## Examples

**Example 1**: The following example listens to Live Chat service availability (which can change based on conditions defined in the Live Chat builder):




  Copy Code



function onAvailabilityChange({response: {data: { isChatVisible } } } ) {
  // isChatVisible: true/false means live chat is available/unavailable
}
window.sprChat('subscribeToUpdate', {
    topic: 'availabilityChanged',
    subscriber: onAvailabilityChange,
});





**Example 2**: The following example listens to the unread notification count across all the conversations:




  Copy Code



function onUnreadCountChanged({ response: { data: { count } } }) {
  // count: number
}
window.sprChat('subscribeToUpdate', {
    topic: 'unreadCountChanged',
    subscriber: onUnreadCountChanged,
});





**Example 3**: The following example listens to the external events triggered by bot/rule for the brand to handle where the type and externalParams have been defined in the bot/rule itself.




  Copy Code



function onExternalEvent({ response: { data } } ) {
  // data contains the different externalEvent depending on configuration.
  // data: { type: string; payload: { externalParams: any, contextId: string }},
}
window.sprChat('subscribeToUpdate', {
    topic: 'externalEventTriggered',
    subscriber: onExternalEvent,
});





**Example 4**: The following example listens to the load signal of Live Chat:




  Copy Code



function onLoadCompleted({ response: { error } } ) {
  //error can be true/false  if (error) {
    // live chat could not be loaded
  } else {
     // live chat is loaded
  }
}
window.sprChat('subscribeToUpdate', {
    topic: 'loadCompleted',
    subscriber: onLoadCompleted,
});





**Example 5**: The following example listens to the telemetry/analytics events:




  Copy Code



function onEventTriggered({ response: { data } } ) {
   // data: {
       eventType: "CONVERSATION_WINDOW_OPENED"|
                  "CONVERSATION_WINDOW_CLOSED"|
                  "CONVERSATION_EXPORTED"|
                  "CONVERSATION_DELETED"|
                  "CONVERSATION_CLOSED"|
                  "CONVERSATIONS_DELETED"|
                  "CONVERSATIONS_CLOSED"|
                  "NEW_CONVERSATION_CREATED"|
                  "EXISTING_CONVERSATION_OPENED"|
                  "TRIGGER_VISIBLE"|
                  "BUTTON_CLICKED"|
                  "AGENT_ASSIGNED"|
                  "VIDEO_CALL_OUTGOING_STARTING"|
                  "AUDIO_CALL_OUTGOING_STARTING"|
                  "VIDEO_CALL_CARD_CTA_CLICKED"|
                  "AUDIO_CALL_CARD_CTA_CLICKED"|
                  "VIDEO_CALL_LAUNCH_CLICKED"|
                  "AUDIO_CALL_LAUNCH_CLICKED"|
                  "VIDEO_CALL_LAUNCHED"|
                  "AUDIO_CALL_LAUNCHED"|
                  "CONVERSATION_BACK_PRESSED"|
                  "CONVERSATION_LIST_BACK_PRESSED"|
                  "SURVEY_BACK_PRESSED"|
                  "VIDEO_CALL_JOIN_CTA_CLICKED"|
                  "VIDEO_CALL_JOIN_BACK_CTA_CLICKED"|
                  "AUDIO_CALL_JOIN_CTA_CLICKED"|
                  "AUDIO_CALL_JOIN_BACK_CTA_CLICKED"|
                  "VIDEO_CALL_END_CLICKED"|
                  "AUDIO_CALL_END_CLICKED"|
                  "INFO_CARD_OPENED"|
                  "INFO_CARD_CLOSED"|
                  "USER_PROFILE_UPDATED"|
                  "WIDGET_MAXIMIZED"|
                  "WIDGET_MINIMIZED"|
                  "PROACTIVE_PROMPT_TRIGGERED"|
                  "PROACTIVE_PROMPT_ENGAGED"|
                  "PROACTIVE_PROMPT_CLOSED"|
                  "PAGE_OPENED",
       additional?: {
         appId: string;
         conversationId: string;
         page: string;    // website URL on which live chat is embedded
         // other details depending on the type of analytics event
       }
     }
}
window.sprChat('subscribeToUpdate', {
    topic: 'eventTriggered',
    subscriber: onEventTriggered,
} );





**Example 6**: The following example checks whether the requested new conversation was created or not when window.sprChat(‘openNewConversation’) was called:




  Copy Code



const sdkPayload = {
conversationContext: {
    '_c_abcdef123': ['123']
}
};
window.sprChat('openNewConversation', sdkPayload);
function onNewConversation( { request, data?: { conversationId }, error?: 'LIMIT_REACHED' } ) {
      // request is same as sdkPayload
   if (error) {
      // open new conversation limit reached
   } else {
      // conversation is created successfully
   }
}
window.sprChat('subscribeToUpdate', {
    topic: 'openNewConversation',
    subscriber: onNewConversation,
} );





**Example 7**: The following example checks whether the message was published or not when window.sprChat(‘sendExternalEvent’) was called:




  Copy Code



const sdkPayload = {
    type: 'MSG_PUBLISH',
    payload: {
        id: '123',
        message: {
          text: 'Hello world',
        },
        messageContext: {
          '_m_asfd12': ['abc'],
        },
   },
};
window.sprChat('sendExternalEvent', sdkPayload);
function onSendExternalEvent( { request, data?: any; error?: 'INCORRECT_PAYLOAD' } ) {
      // request is same as sdkPayload
   if (error) {
      // sdk was called with incorrect payload
   } else {
   // data: {
       type: 'MSG_PUBLISHED',
       payload: {
          id: string;  // same as sdk.payload.id
          contextId: string;
          sprMsgId?: string;
      }
}
}
window.sprChat('subscribeToUpdate', {
    topic: 'sendExternalEvent',
    subscriber: onSendExternalEvent,
} );





[](https://dev.sprinklr.com/subscribe-to-live-chat-updates)

[Back to top](https://dev.sprinklr.com/subscribe-to-live-chat-updates)
