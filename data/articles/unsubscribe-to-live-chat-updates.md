---
title: "Unsubscribe to Live Chat Updates"
slug: unsubscribe-to-live-chat-updates
url: https://dev.sprinklr.com/unsubscribe-to-live-chat-updates
---

# Unsubscribe to Live Chat Updates

# Unsubscribe to Live Chat Updates

This method is used to unsubscribe from getting updates about the Live Chat events that you previously subscribed to.

## Method

`sprChat(‘unsubscribeToUpdate’);`

## Parameters







| Parameter | Type | Required/Optional | Description | Possible values |
| --- | --- | --- | --- | --- |
| topic | String | Required | The update you subscribed to earlier. | availabilityChanged, unreadCountChanged, externalEventTriggered, loadCompleted, eventTriggered, openNewConversation, sendExternalEvent |
| subscriber | (params: {        request: StringAnyMap;        response: {          data: StringAnyMap;          error: StringAnyMap;        };    }) => void; | Required | The callback function that is invoked when a matching update is available. | None |

### Topics







| Topic | Description |
| --- | --- |
| availabilityChanged | Live Chat’s availability event. |
| unreadCountChanged | Notifies the count of all the conversations. |
| externalEventTriggered | The external event triggered by bot/rule flow. |
| loadCompleted | Notifies whether Live Chat is loaded successfully or not. |
| eventTriggered | Different analytics events of Live Chat. |
| openNewConversation | Indicates whether a new conversation is created or not. |
| sendExternalEvent | Indicates whether an external event is sent to the conversation or not. |

## Examples

**Example 1**: The following example unsubscribes to Live Chat’s availability event:




  Copy Code



window.sprChat('unsubscribeToUpdate', {
     topic: 'availabilityChanged',
     subscriber: onAvailabilityChange, // pass the same subscriber fn to unsubscribe
 });





**Example 2**: The following example unsubscribes to notification count of all the conversation:




  Copy Code



window.sprChat('unsubscribeToUpdate', {
     topic: 'unreadCountChanged',
     subscriber: onUnreadCountChanged, // pass the same subscriber fn to unsubscribe
 });





**Example 3**: The following example unsubscribes to external events trigged by bot/rule flow:




  Copy Code



window.sprChat('unsubscribeToUpdate', {
     topic: 'externalEventTriggered',
     subscriber: onExternalEvent, // pass the same subscriber fn to unsubscribe
 });





**Example 4**: The following example unsubscribes to the topic that indicates whether Live Chat is loaded successfully or not:




  Copy Code



window.sprChat('unsubscribeToUpdate', {
     topic: 'loadCompleted',
     subscriber: onLoadCompleted, // pass the same subscriber fn to unsubscribe
 });





**Example 5**: The following example unsubscribes to different analytics events of Live Chat:




  Copy Code



window.sprChat('unsubscribeToUpdate', {
     topic: 'eventTriggered',
     subscriber: onEventTriggered, // pass the same subscriber fn to unsubscribe
 });





**Example 6**: The following example unsubscribes to the topic that indicates whether a new conversation is created or not:




  Copy Code



window.sprChat('unsubscribeToUpdate', {
    topic: 'openNewConversation',
    subscriber: onNewConversation, // pass the same subscriber fn to unsubscribe
 });





**Example 7**: The following example unsubscribes to send external event:




  Copy Code



window.sprChat('unsubscribeToUpdate', {
     topic: 'sendExternalEvent',
     subscriber: onSendExternalEvent, // pass the same subscriber fn to unsubscribe
 });





[](https://dev.sprinklr.com/unsubscribe-to-live-chat-updates)

[Back to top](https://dev.sprinklr.com/unsubscribe-to-live-chat-updates)
