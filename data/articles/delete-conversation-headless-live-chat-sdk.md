---
title: "Delete Conversation Headless Live Chat SDK"
slug: delete-conversation-headless-live-chat-sdk
url: https://dev.sprinklr.com/delete-conversation-headless-live-chat-sdk
---

# Delete Conversation Headless Live Chat SDK

# Delete Conversation


The `deleteConversation()` method permanently deletes one or more conversations from the system.

**Dev Notes: ** This action is final and cannot be undone, so it is advised to use it with caution.

## SDK Method

`deleteConversation()`

## Example Usage




 Copy Code


// Delete a specific conversation
try {
  const result = await window.sprinklr.chat.deleteConversation({
    conversationId: '627b7d2cb1628c58860f962c'
  });
  console.log('Conversation deleted:', result); // 'SUCCESS'
} catch (error) {
  console.error("Failed to delete conversation:", error);
}
// Delete all conversations
try {
  const result = await window.sprinklr.chat.deleteConversation({
    conversationId: 'ALL'
  });
  console.log('All conversations deleted:', result); // 'SUCCESS'
} catch (error) {
  console.error("Failed to delete all conversations:", error);
}



## Parameters















****

****
- ****
- ****
- ****






| Parameter | Description | Type | Required/Optional | Sample |
| --- | --- | --- | --- | --- |
| conversationId | Specifies the conversation to be deleted.          Supported Values: conversationId, 'ALL'          Deletion Logic:                    With specific conversationId: Deletes the specified conversation.           With 'ALL': Deletes all conversations for the current user.           Without conversationId: This will result in an error as the method requires a conversationId. | string \| 'ALL' | Required | '627b7d2cb1628c58860f962c' or 'ALL' |

## Response Format

The resolved value will look like this:




 Copy Code


'SUCCESS'



  **Dev Notes: **


- **Initialization Required:** Always call `init()` before using `deleteConversation()`. The method will throw `CHAT_NOT_INITIATED` error if called before initialization.

- **Repeated Request Handling:** The system handles repeated deletion requests gracefully to prevent duplicate operations.

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


  [](https://dev.sprinklr.com/delete-conversation-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/delete-conversation-headless-live-chat-sdk)
