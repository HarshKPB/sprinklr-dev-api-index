---
title: "Live Chat Object Type Reference"
slug: live-chat-object-type-reference
url: https://dev.sprinklr.com/live-chat-object-type-reference
---

# Live Chat Object Type Reference

# Live Chat Object Type Reference


This document outlines the various Live Chat object types, including chat messages, message events, user metadata, and message formatting options. These specifications are designed to help you understand the structure and purpose of each object type.

Below are the key object types:


- [chatMessages](https://dev.sprinklr.com/live-chat-object-type-reference#chatMessages)

- [MessageEvent](https://dev.sprinklr.com/live-chat-object-type-reference#MessageEvent)

- [messageType](https://dev.sprinklr.com/live-chat-object-type-reference#messageType)

- [textEntities](https://dev.sprinklr.com/live-chat-object-type-reference#textEntities)

- [quickReplies](https://dev.sprinklr.com/live-chat-object-type-reference#quickReplies)

- [richText](https://dev.sprinklr.com/live-chat-object-type-reference#richText)

- [markdownText](https://dev.sprinklr.com/live-chat-object-type-reference#markdownText)

- [users](https://dev.sprinklr.com/live-chat-object-type-reference#users)

## chatMessages

An array of chat message objects exchanged within conversations.




 Copy Code


chatMessages: Array<{
  id: string;
  messagePayload?: {
    messageType?: number;
    text?: string;
    textEntities?: TextEntity[]; // Highlights or links within the text
    quickReplies?: QuickReplies; // Options for quick user replies
    events?: MessageEvent[]; // Special events like agent assignment
    richText?: boolean; // If true, render message as raw HTML
    markdownText?: boolean; // If true, render message as Markdown
  };
  conversationId: string;
  creationTime: number; // Timestamp in ms
  deleted?: boolean; // Flag if message was deleted
  sender: string; // User ID of the sender
  additionalContext?: StringTMap; // Only present when sending messages via SDK
  inReplyToChatMessageId?: string; // Only present when sending messages via SDK (reply reference)
}>



### Parameters






















































































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| id |  | Required | Unique identifier for the message. | string |
| messagePayload |  | Optional | Object containing details of the message content. | object |
|  | messageType | Optional | Indicates the message type. | number |
|  | text | Optional | The message text | string |
|  | textEntities | Optional | Highlights or links within the text |  |
|  | quickReplies | Optional | Options for quick user replies |  |
|  | events | Optional | Special events like agent assignment |  |
|  | richText | Optional | If true, render message as raw HTML |  |
|  | markdownText | Optional | If true, render message as Markdown |  |
| conversationId |  | Required | ID of the conversation this message belongs to | string |
| creationTime |  | Required | Epoch timestamp (ms) when the message was created | number |
| deleted |  | Optional | Flag if message was deleted | boolean |
| sender |  | Required | User ID of the sender | string |
| additionalContext |  | Optional | Only present when sending messages via SDK | StringTMap<string[]> |
| inReplyToChatMessageId |  | Optional | Only present when sending messages via SDK (reply reference) | string |

## MessageEvent

Events related to agent and queue assignment within a conversation message.

### Structure




 Copy Code


MessageEvent: {
    type: 'AGENT_ASSIGNED' | 'AGENT_UNASSIGNED' | 'AGENT_ASSIGNMENT_CHANGED' | 'WORK_QUEUE_ASSIGNED';
    newAgentId?: string; // For new agent assigned
    oldAgentId?: string; // For old agent unassigned
    queueId?: string; // For work queue assignment
}



### Parameters















- ``
- ``
- ``
- ``






















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | The type of event.         It can be of the following types:                    AGENT_ASSIGNED: newAgentId is provided.           AGENT_UNASSIGNED: oldAgentId is provided.           AGENT_ASSIGNMENT_CHANGED: Both newAgentId and oldAgentId are provided.           WORK_QUEUE_ASSIGNED: queueId is provided. | string |
| newAgentId | Optional | The ID of the new agent assigned to the chat. | string |
| oldAgentId | Optional | The ID of the agent who was unassigned or replaced. | string |
| queueId | Optional | The ID of the work queue the chat was assigned to. | string |

## messageType

Indicates the type/category of the message.

### Common Values

Some common values include:


























| Value | Message Type |
| --- | --- |
| 313 | LIVE_CHAT_POST |
| 314 | LIVE_CHAT_POST_BACK |
| 340 | LIVE_CHAT_EVENT |
| 394 | LIVE_STREAM_MESSAGE |

## textEntities

Used to convert parts of the message text into clickable links based on their position.

### Structure




 Copy Code


TextEntity {
    indices: [number, number]; // Start and end positions in text
    url?: string; // Link URL to convert the text into
    phoneNumber?: string; // Phone number to convert the text into a clickable phone link
}



### Parameters






























| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| indices | Required | Start and end positions in text | [number, number] |
| url | Optional | Link URL to convert the text into | string |
| phoneNumber | Optional | Phone number to convert the text into a clickable phone link | string |

### Example




 Copy Code


[
{ indices: [0, 5], url: 'https://www.google.co.in/' }
]



This means the characters from position 0 to 5 in the message text become a clickable link pointing to Google.

## quickReplies

Quick reply options shown to the user as buttons or selectable items.

### Structure




 Copy Code


quickReplies?: {
  quickReplies: [{
    id: string;
    type: 'TEXT';
    title: string;
    imageUrl?: string;
    payload?: string;
  }];
  disableManualResponse?: boolean; // If true, disables manual typing response by user
}



### Parameters






















































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| quickReplies | Optional | An array of quick reply options to present to the user. Each object represents one quick reply button. | object |
| id | Required | ID for the quick reply option. | string |
| type | Required | The type of quick reply. Currently supports only the value 'TEXT'. | string |
| title | Required | Title of the quick reply. | string |
| imageUrl | Optional | URL of the image. | string |
| payload | Optional | Payload of the quick reply. | string |
| disableManualResponse | Optional | Indicates whether to disable manual response. | boolean |

### Example




 Copy Code


quickReplies: {
  disableManualResponse: true,
  quickReplies: [
    {
      id: '12313',
      type: 'TEXT',
      title: 'my title',
      imageUrl: 'https://myurl.com',
    }
  ],
}



## richText

A boolean flag indicating that the message content should be rendered as raw HTML (dangerouslySetInnerHTML in React).

## markdownText

A boolean flag indicating the message content should be parsed and rendered as Markdown.

## users

An array representing all users involved in a conversation.

### Structure




 Copy Code


users: Array<{
    userId: string;
    userType: string; // 'PARTNER' or 'ANONYMOUS'
    userName?: string;
    firstName: string;
    lastName?: string;
    fullName?: string;
    profileImageUrl: string;
    email: string;
    phoneNo: string;
    locale: string;
}>



### Parameters















- ``
- ``
- ``
- ``
- ``
****[getMessages()](https://dev.sprinklr.com/fetch-messages-headless-live-chat-sdk)



























































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| userId | Required | Unique identifier for the user. Special values include:    C_: Represents authenticated customer (prefix would be 'C_')   A_: Represents the anonymous customer (prefix would be 'A_')  Unique identifier for brand messages. Some special values include:    P_-200: Represents bot messages sent from the brand's Live Chat widget (for example, welcome messages).   P_0: The system user.   P_-100: The system moderation user.  Any other value typically indicates an agent user.  Dev Notes: The participant list does not follow the same sequence as the messages. Use the  method to retrieve the sender along with the associated message. | string |
| userType | Required | Indicates the type of user: 'PARTNER' means a known user or agent, while 'ANONYMOUS' refers to a visitor whose identity is not known. | string |
| userName | Optional | Username of the user. | string |
| firstName | Required | First name of the user. | string |
| lastName | Optional | Last name of the user. | string |
| fullName | Optional | Full name of the user. | string |
| profileImageUrl | Required | URL to the user's profile image. | string |
| email | Required | Email ID of the user. | string |
| phoneNo | Required | Phone number of the user. | string |
| locale | Required | Locale or language preference of the user. | string |


  [](https://dev.sprinklr.com/live-chat-object-type-reference)




[Back to top](https://dev.sprinklr.com/live-chat-object-type-reference)
