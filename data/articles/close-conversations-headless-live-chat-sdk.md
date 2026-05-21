---
title: "Close Conversations Headless Live Chat SDK"
slug: close-conversations-headless-live-chat-sdk
url: https://dev.sprinklr.com/close-conversations-headless-live-chat-sdk
---

# Close Conversations Headless Live Chat SDK

# Close Conversations


The `closeConversation()` method closes one or all conversations.

## SDK Method

`closeConversation()`

## Example Usage




 Copy Code


// Close a specific conversation
try {
  const result = await window.sprinklr.chat.closeConversation({
    conversationId: '627b7d2cb1628c58860f962c'
  });
  console.log('Conversation closed:', result); // 'SUCCESS'
} catch (error) {
  console.error("Failed to close conversation:", error);
}
// Close all conversations
try {
  const result = await window.sprinklr.chat.closeConversation({
    conversationId: 'ALL'
  });
  console.log('All conversations closed:', result); // 'SUCCESS'
} catch (error) {
  console.error("Failed to close all conversations:", error);
}



## Parameters















****

****
- ****
- ****
- ****``






| Parameter | Description | Type | Required/Optional | Sample |
| --- | --- | --- | --- | --- |
| conversationId | Specifies the conversation to be closed.          Supported Values: conversationId, 'ALL'          Closing Logic:                    With a specific conversationId: Closes the specified conversation identified by the provided ID.           With 'ALL': Closes all conversations associated with the current user.           Without conversationId: This will result in an error as the conversationId is a required parameter. | string \| 'ALL' | Required | '627b7d2cb1628c58860f962c' or 'ALL' |

## Response Format

The resolved value will look like this:




 Copy Code


'SUCCESS'



  **Dev Notes: **


- **Initialization Required:** Always call `init()` before using `closeConversation()`. The method will throw `CHAT_NOT_INITIATED` error if called before initialization.

- **Repeated Request Handling:** The system handles repeated closing requests gracefully to prevent duplicate operations.

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
| UNEXPECTED_ERROR | Occurs for any unexpected or unclassified error. Used as a fallback for debugging purposes. |
| CHAT_NOT_INITIATED | Occurs when chat SDK methods (sendMessage, createConversation, etc.) are called before init(). |


  [](https://dev.sprinklr.com/close-conversations-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/close-conversations-headless-live-chat-sdk)
