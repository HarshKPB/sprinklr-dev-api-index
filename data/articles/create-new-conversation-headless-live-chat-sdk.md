---
title: "Create New Conversation Headless Live Chat SDK"
slug: create-new-conversation-headless-live-chat-sdk
url: https://dev.sprinklr.com/create-new-conversation-headless-live-chat-sdk
---

# Create New Conversation Headless Live Chat SDK

# Create New Conversation Headless Live Chat SDK


The `createConversation()` method is used to start a new conversation, optionally with initial messages and context like assigning a case or agent.

This method does the following:


- **Initiates a new conversation with optional initial messages:** When called, it creates a new conversation. You can also pass an array of messages to pre-populate the conversation. These messages are sent on behalf of the user/brand/bot depending on the `isSentByUser` flag.

- **Initiates conversation with context:** You can pass custom metadata (via `conversationContext`) that helps categorize or label the conversation. This context can be used later for analytics, routing, or personalization.

## SDK Method

`createConversation()`

## Example Usage




 Copy Code


try {
  const conversation = await window.sprinklr.chat.createConversation({
    initialMessages: [{ message: "Hi", isSentByUser: true }],
    createCase: true,
    requestId: "req-123",
    conversationContext: { userTier: ["gold"] }
  });
  // Access conversation object
  console.log(conversation);
} catch (error) {
  // Handle any errors (e.g., not initialized, invalid payload)
  console.error("Failed to create conversation:", error);
}



## Parameters






















































































| Parameter | Sub-Parameter | Required/Optional | Description | Type | Default |
| --- | --- | --- | --- | --- | --- |
| requestId |  | Optional | A unique request identifier to trace this API call.Example: "req-91xyz10" | string |  |
| externalCaseId |  | Optional | An external case reference to link the new conversation.Example: "123" | string |  |
| initialMessages |  | Optional | Array of initial messages to seed the conversation with.Example: [{ message: "Hi, I need help", isSentByUser: true }] | Array<{ isSentByUser?: boolean; message: string \| Partial<MessagePayload> }> |  |
|  | isSentByUser | Optional | Flag indicating if the message was sent by the user.Supported Values: true, false | boolean | false |
|  | message | Required | The message content (string or partial MessagePayload).Example: "Hi, I need help" | string or Partial<MessagePayload> |  |
| createCase |  | Optional | Whether a new case should be created with the conversation.Supported Values: true, falseIf false, conversation is temporary. | boolean |  |
| assignToAgent |  | Optional | ID of the agent to assign the conversation to.Example: "123" | string |  |
| conversationContext |  | Optional | Custom field map to store additional metadata on the conversation.Example: { "userTier": [] } | StringTMap<string[]> |  |

## Response Format

The resolved `conversation` object will look like this:




 Copy Code


conversation: {
  id: string;                   // Unique ID for the conversation
  creationTime: number;         // Epoch timestamp (ms) when the conversation was created
  caseId: string;               // Internal case ID linked with the conversation
  caseNumber: number;           // Human-readable case number (for display/logging)
  chatMessages: object;         // Contains the initial message(s) if provided
  participants: string[];       // Array of user IDs involved in the conversation
}



## Response Parameters





























[chatMessages type doc](https://dev.sprinklr.com/live-chat-object-type-reference#chatMessages)








| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique ID for the conversation | string |
| creationTime | Epoch timestamp (ms) when the conversation was created | number |
| caseId | The case ID linked with the conversation | string |
| caseNumber | The case number associated with the case | number |
| chatMessages | An array of chat message objects exchanged within conversations.       Refer to the  for object structure. | object |
| participants | Array of user IDs involved in the conversation | string[] |

## Error Types









      ``



      ``



      ``



      ``
      ``````



| Error Type | When it Occurs |
| --- | --- |
| NOT_FOUND | Thrown when the specified conversation or resource cannot be found. |
| NOT_ACCEPTABLE | Indicates invalid input format or unreadable data. |
| UNEXPECTED_ERROR | Any unexpected or unclassified error. |
| CHAT_NOT_INITIATED | Thrown when chat SDK methods          sendMessage, createConversation, and others          are called before init(). |


  [](https://dev.sprinklr.com/create-new-conversation-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/create-new-conversation-headless-live-chat-sdk)
