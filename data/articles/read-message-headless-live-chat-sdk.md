---
title: "Read Message Headless Live Chat SDK"
slug: read-message-headless-live-chat-sdk
url: https://dev.sprinklr.com/read-message-headless-live-chat-sdk
---

# Read Message Headless Live Chat SDK

# Read Message


The `readMessage()` method marks messages as read in a conversation. This method allows you to update the read status of messages. This helps track which messages have been viewed by the user and maintains proper unread count tracking.

**Dev Notes: ** This action is final and cannot be undone, so it is advised to use it with caution.

## SDK Method

`readMessage()`

## Example Usage




 Copy Code


// Mark a specific message as read
try {
  const result = await window.sprinklr.chat.readMessage({
    conversationId: '627b7d2cb1628c58860f962c',
    messageId: '68e7bfbce7c5f52dbc9c22a0'
  });
  console.log('Message marked as read:', result); // 'SUCCESS'
} catch (error) {
  console.error("Failed to mark message as read:", error);
}
// Mark the last sent message as read (when messageId is not provided)
try {
  const result = await window.sprinklr.chat.readMessage({
    conversationId: '627b7d2cb1628c58860f962c'
  });
  console.log('Last message marked as read:', result); // 'SUCCESS'
} catch (error) {
  console.error("Failed to mark last message as read:", error);
}



## Parameters



























| Parameters | Description | Type | Required/Optional | Sample |
| --- | --- | --- | --- | --- |
| conversationId | The unique identifier of the conversation containing the message to mark as read. | string | Required | '627b7d2cb1628c58860f962c' |
| messageId | The unique identifier of the specific message to mark as read. If not provided, the last sent message in the conversation will be used. | string | Optional | '68e7bfbce7c5f52dbc9c22a0' |

**Dev Notes: **


- **With `messageId`:** Mark up to the specified messages as read in the given conversation.

- **Without `messageId`:** Mark all messages as read in the given conversation.

- **Validation:** The method validates that both the conversation and message are fetched before processing.

## Response Format

The resolved value will look like this:




 Copy Code


'SUCCESS'



  **Dev Notes: **


- **Initialization Required:** Always call `init()` before using `readMessage()`. The method will throw `CHAT_NOT_INITIATED` error if called before initialization.

- **Call SDK Sequence:** Call this SDK only after the `getConversations` and `getMessages` SDKs; otherwise, it will fail.

- **Unread Count Management:** This method helps maintain accurate unread message counts across the conversation system.

- **Promise Based:** The method returns a Promise that resolves with `'SUCCESS'` on completion or rejects with an error if the operation fails.

## Error Types

**Dev Notes: **For robustness, always handle `UNEXPECTED_ERROR` as a catch-all in the UI or telemetry.









      ``



      ``



      ``



      ``




| Error Type | When It Occurs |
| --- | --- |
| NOT_FOUND | When the requested conversation, message, or resource cannot be found. This typically happens when trying to access a conversation that has been deleted. |
| NOT_ACCEPTABLE | When the data format or content you're trying to send is invalid or cannot be processed. This includes malformed message content, invalid file types, or data that doesn't meet the system requirements or when the conversation ID or message ID are invalid. |
| UNEXPECTED_ERROR | Any unexpected or unclassified error. Used as a fallback for debugging purposes. |
| CHAT_NOT_INITIATED | Thrown when chat SDK methods (sendMessage, createConversation, etc.) are called before init(). |


  [](https://dev.sprinklr.com/read-message-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/read-message-headless-live-chat-sdk)
