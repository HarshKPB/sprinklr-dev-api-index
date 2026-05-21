---
title: "Fetch Conversations Headless Live Chat SDK"
slug: fetch-conversations-headless-live-chat-sdk
url: https://dev.sprinklr.com/fetch-conversations-headless-live-chat-sdk
---

# Fetch Conversations Headless Live Chat SDK

# Fetch Conversations


The `getConversations()` method fetches a list of existing Live Chat conversations.

## SDK Method

`getConversations()`

## Example Usage




 Copy Code


try {
  const conversations = await window.sprinklr.chat.getConversations({
    size: 5, // Optional: number of conversations to fetch
  });
  console.log(conversations);
} catch (error) {
  console.error("Failed to fetch conversations:", error);
}



## Parameters




















| Parameter | Description | Type | Required/Optional | Default |
| --- | --- | --- | --- | --- |
| size | Number of conversations to fetch. Example: 5 | number | Optional | By default, a size of 20 is used if no size is specified. |

## Response Format - Conversations Object

The resolved `conversations` object will look like this:




 Copy Code


{
  conversations: [
    {
      id: string;
      participants: string[];
      creationTime?: number;
      lastMessageId?: string;
      caseId?: string;
      closed?: boolean;
      deleted?: boolean;
      unreadCount?: number;
      caseNumber?: number;
      chatMessages: Message[];
      lastMessage?: Message;
    }
  ],
  hasMore: boolean;
}



## Response Format - Conversations


















- ``
- ``
- ``
- ``
- ``
****[getMessages()](https://dev.sprinklr.com/fetch-messages-headless-live-chat-sdk)























































| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the conversation. | string |
| participants | Unique identifier for the user. Special values include:    C_: Represents authenticated customer (prefix would be 'C_')   A_: Represents the anonymous customer (prefix would be 'A_')  Unique identifier for brand messages. Some special values include:    P_-200: Represents bot messages sent from the brand's Live Chat widget (for example, welcome messages).   P_0: The system user.   P_-100: The system moderation user.  Any other value typically indicates an agent user.  Dev Notes: The participant list does not follow the same sequence as the messages. Use the  method to retrieve the sender along with the associated message. | string[] |
| creationTime | Timestamp when the conversation was created. | number |
| lastMessageId | ID of the last message sent in the conversation. | string |
| caseId | Identifier for the case related to this conversation. | string |
| closed | Indicates if the conversation is marked as closed. | boolean |
| deleted | Indicates if the conversation has been deleted. | boolean |
| unreadCount | Number of unread messages in the conversation. | number |
| caseNumber | Case number associated with the conversation. | number |
| chatMessages | Array of messages in the conversation. | Message[] |
| lastMessage | The most recent message object in the conversation. | Message |
| hasMore | Indicates if there are more conversations to fetch. | boolean |

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


  [](https://dev.sprinklr.com/fetch-conversations-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/fetch-conversations-headless-live-chat-sdk)
