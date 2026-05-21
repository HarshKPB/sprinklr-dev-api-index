---
title: "Fetch Messages Headless Live Chat SDK"
slug: fetch-messages-headless-live-chat-sdk
url: https://dev.sprinklr.com/fetch-messages-headless-live-chat-sdk
---

# Fetch Messages Headless Live Chat SDK

# Fetch Messages


The `getMessages()` method retrieves the messages associated with a specific Live Chat conversation.

## SDK Method

`getMessages()`

## Example Usage




 Copy Code


try {
  const messages = await window.sprinklr.chat.getMessages({
    conversationId: '686f905211572236687a6e3a',
    size: 5,
  });
  console.log(messages);
} catch (error) {
  console.error("Failed to fetch messages:", error);
}



## Parameters





























| Parameter | Description | Type | Required/Optional | Default |
| --- | --- | --- | --- | --- |
| size | Number of conversations to fetch. Example: 5 | number | Optional | 20 |
| conversationId | Unique identifier for the conversation. Example: "686f905211572236687a6e3a" | string | Mandatory |  |

## Response Format - Message Object

The resolved `messages` object will look like this:




 Copy Code


{
  messages: Message[];
  hasMore: boolean;
}



## Response Format - Messages





















| Parameters | Description | Type |
| --- | --- | --- |
| messages | Array of message objects in the conversation. | Message[] |
| hasMore | Indicates if there are more messages to fetch. | boolean |

## Response Format - Message Object

The resolved `Message` object will look like this:




 Copy Code


Message: {
  id: string;
  conversationId: string;
  creationTime: number;
  deleted?: boolean;
  sender: string;
  additionalContext?: Record;
  messagePayload?: {
    messageType?: number;
    text?: string;
    textEntities?: TextEntity[]; // Highlights or links within the text
    quickReplies?: QuickReplies; // Options for quick user replies
    events?: MessageEvent[]; // Special events like agent assignment
    richText?: boolean; // If true, render message as raw HTML
    markdownText?: boolean; // If true, render message as Markdown
  };
}



## Response Parameters - Message
























































[messageType](https://dev.sprinklr.com/live-chat-object-type-reference#messageType)












[textEntities](https://dev.sprinklr.com/live-chat-object-type-reference#textEntities)






[quickReplies](https://dev.sprinklr.com/live-chat-object-type-reference#quickReplies)






[MessageEvent](https://dev.sprinklr.com/live-chat-object-type-reference#MessageEvent)






[richText](https://dev.sprinklr.com/live-chat-object-type-reference#richText)






[markdownText](https://dev.sprinklr.com/live-chat-object-type-reference#markdownText)




| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Unique identifier for the message. | string |
| conversationId |  | ID of the conversation the message belongs to. | string |
| creationTime |  | Timestamp when the message was created. | number |
| deleted |  | Indicates if the message has been deleted. | boolean |
| sender |  | The sender of the message. | string |
| additionalContext |  | Additional context or metadata related to the message. | Record<string, string[]> |
| messagePayload |  | Contains additional content and features of the message. | Object |
|  | messageType | Type of the message.For more information, see  object reference. | number |
|  | text | Plain text content of the message. | string |
|  | textEntities | Highlights or links within the text.For more information, see  object reference. | TextEntity[] |
|  | quickReplies | Options for quick user replies.For more information, see  object reference. | QuickReplies |
|  | events | Special events like agent assignment.For more information, see  object reference. | MessageEvent[] |
|  | richText | If true, render message as raw HTML.For more information, see  object reference. | boolean |
|  | markdownText | If true, render message as Markdown.For more information, see  object reference. | boolean |

  **Dev Notes: **


- Avoid making identical API calls simultaneously. If a request is made while an identical one is already being processed, the SDK will return the cached result.

- Pagination is handled automatically using an internal cursor. For example, if you fetch 5 conversations in one call, the next 5 will be fetched in the subsequent call. Use pagination via the `hasMore` flag.


## Error Types

**Dev Notes: **For robustness, always handle `UNEXPECTED_ERROR` as a catch-all in the UI or telemetry.









      ``



      ``



      ``



      ``
      ``````



| Error Type | When It Occurs |
| --- | --- |
| NOT_FOUND | Occurs when the requested conversation, message, or resource cannot be found. This typically happens when trying to access a conversation that has been deleted or when the conversation ID is invalid. |
| NOT_ACCEPTABLE | Occurs when the data format or content you're trying to send is invalid or cannot be processed. This includes malformed message content, invalid file types, or data that doesn't meet the system requirements. |
| UNEXPECTED_ERROR | Any unexpected or unclassified error. Used as a fallback for debugging purposes. |
| CHAT_NOT_INITIATED | Occurs when chat SDK methods (sendMessage, createConversation, etc.) are called before init(). |


  [](https://dev.sprinklr.com/fetch-messages-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/fetch-messages-headless-live-chat-sdk)
