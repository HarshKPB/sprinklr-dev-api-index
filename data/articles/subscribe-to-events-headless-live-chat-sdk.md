---
title: "Subscribe to Events Headless Live Chat SDK"
slug: subscribe-to-events-headless-live-chat-sdk
url: https://dev.sprinklr.com/subscribe-to-events-headless-live-chat-sdk
---

# Subscribe to Events Headless Live Chat SDK

# Subscribe to Real-Time Events


The `subscribeToEvents()` method enables you to subscribe to real-time updates like messages received, typing indicators, and conversation status changes.

You can subscribe to specific events by providing:


- A topic (either a single string or an array of strings)

- A custom subscriber function that will be executed whenever an event is received on the specified topic(s)

This allows you to handle topic-specific events in a flexible and modular way, enabling custom logic to be triggered based on the content or context of the incoming event.

## SDK Method

`subscribeToEvents()`

## Syntax




 Copy Code


const unsubscribe = await window.sprinklr.chat.subscribeToEvents({
  topics: string | string[],
  subscriber: fn,
});



## Example




 Copy Code


function ChatComponent() {
  useEffect(() => {
    let unsubscribeFn;
    const subscribe = async () => {
      unsubscribeFn = await window.sprinklr.chat.subscribeToEvents({
        topics: ['@chat/MESSAGE_RECEIVED'],
        subscriber: (payload) => {
          console.log('New message received:', payload);
        },
      });
    };
    subscribe();
    return () => {
      if (typeof unsubscribeFn === 'function') {
        unsubscribeFn(); // Clean up the subscription
      }
    };
  }, []);
  return Chat UI goes here;
}



## Supported Topics and Payload Structures

  These topics allow your application to respond to real-time events in the chat system.
  Each topic corresponds to a specific type of event and includes a well-defined payload structure.

### Supported Topics

The following topic types are supported:


- [MESSAGE_RECEIVED](https://dev.sprinklr.com/subscribe-to-events-headless-live-chat-sdk#message-received)

- [MESSAGE_UPDATED](https://dev.sprinklr.com/subscribe-to-events-headless-live-chat-sdk#message-updated)

- [CONVERSATIONS_UPDATED](https://dev.sprinklr.com/subscribe-to-events-headless-live-chat-sdk#conversations-updated)

- [USER_RESOLVED](https://dev.sprinklr.com/subscribe-to-events-headless-live-chat-sdk#user-resolved)

- [AGENT_START_TYPING](https://dev.sprinklr.com/subscribe-to-events-headless-live-chat-sdk#agent-start-typing)

- [AGENT_STOP_TYPING](https://dev.sprinklr.com/subscribe-to-events-headless-live-chat-sdk#agent-stop-typing)

- [EXTERNAL_EVENT_SEND](https://dev.sprinklr.com/subscribe-to-events-headless-live-chat-sdk#external-event-send)

### MESSAGE_RECEIVED

**Topic:** `@chat/MESSAGE_RECEIVED`

**Description:** This event is triggered whenever a new message is received from an agent through the events real-time service. It lets your application know that a new chat message has arrived in a conversation.

**Payload Structure:**










      ``




      ``





| Key | Type | Description |
| --- | --- | --- |
| chatMessage | object | Contains the details of the received message (text, attachments, metadata, among others) |
| conversationId | string | The unique ID of the conversation this message belongs to |

### MESSAGE_UPDATED

**Topic:** `@chat/MESSAGE_UPDATED`

**Description:** This event is triggered when an existing message is updated, such as edits to the text or changes to attachments. It helps keep the chat UI in sync with the latest message content.

**Payload Structure:**










      ``




      ``





| Key | Type | Description |
| --- | --- | --- |
| chatMessage | object | Contains the details of the received message (text, attachments, metadata, etc.) |
| conversationId | string | The unique ID of the conversation this message belongs to |

### CONVERSATIONS_UPDATED

**Topic:** `@conversation/CONVERSATIONS_UPDATED`

**Description:** This event is used to notify updates at the conversation level, such as changes in status, participants, or case details.

**Payload Structure:**









    ``
    ``
    ``
    ``
    ``
    ``
    ``
    ``
    ``
    ``
    ``
    ``


| Key | Type | Description |
| --- | --- | --- |
| conversationId | string | ID of the updated conversation |
| includeAll | boolean | Indicates if all conversations are included |
| deleted | boolean | Whether the conversation is marked as deleted |
| closed | boolean | Whether the conversation has been closed |
| surveyUrl | string | URL for any post-conversation survey |
| sender | string | ID of the sender of the update |
| workQueueAssigned | boolean | If the conversation is assigned to a work queue |
| caseNumber | number | Human-readable case number |
| expireAssetUntilLastMessageId | string | Expiry setting based on the last message ID |
| agentAssigned | boolean | If an agent is assigned to the conversation |
| caseId | string | Internal case ID associated with the conversation |
| participants | string[] | List of user IDs participating in the conversation |

### USER_RESOLVED

**Topic:** `@user/RESOLVED`

**Description:** This event provides a complete list of all users involved in a particular conversation, useful for user management or UI display.

**Payload Structure:**










      ``





| Key | Type | Description |
| --- | --- | --- |
| users | Array<object> | List of user objects in the conversation |

### AGENT_START_TYPING

**Topic:** `@user/AGENT_START_TYPING`

**Description:** This event indicates when an agent starts typing a message in a conversation, useful for displaying “agent is typing...” indicators in the UI.

**Payload Structure:**









    ``
    ``
    ``


| Key | Type | Description |
| --- | --- | --- |
| userId | string | ID of the agent who started typing |
| actionTime | number | Timestamp (in milliseconds) when typing began |
| conversationId | string | ID of the conversation |

### AGENT_STOP_TYPING

**Topic:** `@user/AGENT_STOP_TYPING`

**Description:** This event indicates when an agent stops typing in a conversation, signaling the end of the typing indicator.

**Payload Structure:**









    ``
    ``


| Key | Type | Description |
| --- | --- | --- |
| userId | string | ID of the agent who stopped typing |
| conversationId | string | ID of the conversation |

### EXTERNAL_EVENT_SEND

**Topic:** `@conversation/EXTERNAL_EVENT_SEND`

**Description:** Listens to the external events triggered by bot/rule for the brand to handle where the type and externalParams have been defined in the bot/rule itself.

**Payload:**




 Copy Code



{
  type: '@conversation/EXTERNAL_EVENT_SEND',
  payload: {
    data: {
      type: string,        // The type/category of the external event
      payload: object      // The actual data payload of the external event
    }
  }
}



**Payload Structure:**











      ``





      ``






| Field | Type | Description | Example |
| --- | --- | --- | --- |
| payload.data.type | string | The type or category identifier of the external event being sent | 'test', 'notification', 'custom_event' |
| payload.data.payload | object | The actual payload data containing the event-specific information | { caseNumber: "12233496", contextId: "68e66287efc2833e4730a2f4" } |

**Example Usage:**




 Copy Code



{
  type: '@conversation/EXTERNAL_EVENT_SEND',
  payload: {
    data: {
      type: 'test',
      payload: {
        caseNumber: '12233496',
        contextId: '68e66287efc2833e4730a2f4',
        externalParams: '[""]\n\n[""]',
        transcript: '[{"Sender":"Anonymous User","CreationTime":1759928967702,...}]'
      }
    }
  }
}



## Errors









      ``



      ``



      ``




| Error Type | When It Occurs |
| --- | --- |
| NOT_FOUND | Thrown when the specified conversation or resource cannot be found. |
| NOT_ACCEPTABLE | Indicates invalid input format or unreadable data. |
| UNEXPECTED_ERROR | Any unexpected or unclassified error. |


  [](https://dev.sprinklr.com/subscribe-to-events-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/subscribe-to-events-headless-live-chat-sdk)
