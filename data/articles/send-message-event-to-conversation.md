---
title: "Send a Message or Event to an Ongoing Conversation"
slug: send-message-event-to-conversation
url: https://dev.sprinklr.com/send-message-event-to-conversation
---

# Send a Message or Event to an Ongoing Conversation

# Send a Message or Event to an Ongoing Conversation

This method is used to publish a message or an event in an ongoing open conversation.

An event is a special kind of message that Sprinklr bot understands and responds to. It is like giving a signal only to the bot and is not visible to the user in the conversation.

## Method

`sprChat(‘sendExternalEvent’);`

## Parameters







****
****

| Parameter | Type | Required/Optional | Description | Possible values |
| --- | --- | --- | --- | --- |
| clientExternalEvent | MessagePublishExternalEvent \| EventPublishClientExternalEvent   type MessagePublishExternalEvent = { type: 'MSG_PUBLISH'; payload: {     contextId?: string;     id: string;     message: {           text?: string;           textEntities?: App.Chat.TextEntity[];           attachment?: DeepPartial;           quickReplies?: DeepPartial;           disableManualResponse?: boolean;           maskingDetails?: StringTMap;         };     isSentByUser?: boolean;     messageContext?: StringTMap; }; } type EventPublishClientExternalEvent = {     type: 'EVENT_PUBLISH';     payload: {         contextId: string;         id: string;        event: {             type: string;             [key: string]: any;        };     }; } | Required | Defines the message or event that you want to publish in an ongoing conversation. | MSG_PUBLISH: Use this to publish a message in an ongoing conversation.  EVENT_PUBLISH: Use this to publish an event in an ongoing conversation. |

### Payload parameters

The following table describes the payload parameters that are passed within the `clientExternalEvent` parameter:







| Parameter | Type | Description |
| --- | --- | --- |
| contextId | String | The ID of the conversation in which you want to publish the message. The default value is the ID of the latest, active, and open conversation. |
| id | String | Unique identifier that you can send and expect back in updates on publish success/failure of this event. |
| message | message | The message you want to publish in the conversation. |
| isSentByUser | Boolean | Defines whether the message is sent by the customer or the brand. |
| messageContext | StringTMap<string[]> | Map of custom field ids and their values that should be updated on the conversation. |
| event | event: {         type: string;         [key: string]: any;       }; | The type describes the event. The key is any string you want to publish. |

## Examples

**Example 1**: Publishes a brand message, with the ID `123` on the latest active and open conversation and passes the message context  `_m_asfd12` with value `abc`.




  Copy Code



window.sprChat('sendExternalEvent', {
     type: 'MSG_PUBLISH',
     payload: {
         id: '123',
         message: {
           text: 'Hello world',
         },
         messageContext: {
           '_m_asfd12': [‘abc’],
         },
    },
 });





**Example 2**: Sends an event of type `MY_CUSTOM_EVENT` to the bot on the latest active and open conversation. This event must be already defined by the creator in Sprinklr Bot.




  Copy Code



window.sprChat('sendExternalEvent', {
     type: 'EVENT_PUBLISH',
     payload: {
         contextId: '6347db4b6b441a7a1eed68b8',
         id: '123',
         event: {
           type: 'MY_CUSTOM_EVENT',
         };
     };
});





[](https://dev.sprinklr.com/send-message-event-to-conversation)

[Back to top](https://dev.sprinklr.com/send-message-event-to-conversation)
