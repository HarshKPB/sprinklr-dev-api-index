---
title: "Download Attachment Headless Live Chat SDK"
slug: download-attachment-headless-live-chat-sdk
url: https://dev.sprinklr.com/download-attachment-headless-live-chat-sdk
---

# Download Attachment Headless Live Chat SDK

# Download Message Attachments


The `downloadAttachment()` method downloads media attachments (images, videos, documents, audio files) from a specific message in a conversation.

## SDK Method

`downloadAttachment()`

## Example Usage




 Copy Code


// Download a specific attachment
try {
  const result = await window.sprinklr.chat.downloadAttachment({
    conversationId: '627b7d2cb1628c58860f962c',
    messageId: '68e7bfbce7c5f52dbc9c22a0',
    attachmentId: 'att-123', // Optional: specific attachment ID
  });
  console.log('Attachment downloaded:', result); // 'SUCCESS'
} catch (error) {
  console.error("Failed to download attachment:", error);
}
// Download all attachments from a message (when attachmentId is not provided)
try {
  const result = await window.sprinklr.chat.downloadAttachment({
    conversationId: '627b7d2cb1628c58860f962c',
    messageId: '68e7bfbce7c5f52dbc9c22a0',
  });
  console.log('All attachments downloaded:', result); // 'SUCCESS'
} catch (error) {
  console.error("Failed to download attachments:", error);
}



## Parameters












      ``

      ``

      ``


      ``

      ``

      ``


      ``

      ``

      ``



| Parameter | Description | Type | Required/Optional | Sample |
| --- | --- | --- | --- | --- |
| conversationId | Unique identifier of the conversation where the message exists | string | Required | "627b7d2cb1628c58860f962c" |
| messageId | Unique identifier of the message within the conversation | string | Required | "68e7bfbce7c5f52dbc9c22a0" |
| attachmentId | Identifier of the attachment if the operation targets a specific attachment within the message | string | Optional | "att-123" |


**Dev Notes:**



- The attachment file(s) will be automatically downloaded by the browser. Ensure that browser pop-up blockers are not preventing the download.

- When calling the SDK without specifying an `attachmentId`, the first attachment from the message will be downloaded.


## Response Format



'SUCCESS'



## Error Types









      ``
      ``````


      ``
      ``````


      ``



      ``
      ``````



| Error Type | When It Occurs |
| --- | --- |
| NOT_FOUND | When the requested conversation, message, or resource cannot be found.          This typically happens when trying to access a conversation that has been deleted or when the          conversationId is invalid. |
| NOT_ACCEPTABLE | When the data format or content is invalid. This includes: the message doesn't contain any media attachments,          invalid attachmentId (if provided), or the messageId/conversationId values are invalid. |
| UNEXPECTED_ERROR | Any unexpected or unclassified error. Used as a fallback for debugging purposes. |
| CHAT_NOT_INITIATED | Thrown when chat SDK methods (sendMessage, createConversation, etc.)          are called before init(). |


  [](https://dev.sprinklr.com/download-attachment-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/download-attachment-headless-live-chat-sdk)
