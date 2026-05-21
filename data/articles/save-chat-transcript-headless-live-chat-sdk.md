---
title: "Save Chat Transcript Headless Live Chat SDK"
slug: save-chat-transcript-headless-live-chat-sdk
url: https://dev.sprinklr.com/save-chat-transcript-headless-live-chat-sdk
---

# Save Chat Transcript Headless Live Chat SDK

# Save Chat Transcript


The `saveChatTranscript()` method downloads the chat transcript for a specific conversation. This method allows users to save a complete record of their conversation as a text file.

## SDK Method

`saveChatTranscript()`

## Example Usage




 Copy Code


try {
  const result = await window.sprinklr.chat.saveChatTranscript({
    conversationId: '627b7d2cb1628c58860f962c',
  });
  console.log('Transcript saved:', result); // 'SUCCESS'
} catch (error) {
  console.error("Failed to save transcript:", error);
}



## Parameters












      ``

      ``

      ``



| Parameter | Description | Type | Required/Optional | Sample |
| --- | --- | --- | --- | --- |
| conversationId | Unique identifier of the conversation where the message exists | string | Required | "627b7d2cb1628c58860f962c" |

**Dev Notes: **The transcript file will be automatically downloaded by the browser. Ensure that browser pop-up blockers are not preventing the download.

## Response Format

The resolved `message` object will look like this:



'SUCCESS'



## Error Types









      ``
      ``````


      ``



      ``



      ``
      ``````



| Error Type | When It Occurs |
| --- | --- |
| NOT_FOUND | When the requested conversation, message, or resource cannot be found.          This typically happens when trying to access a conversation that has been deleted or when the          conversationId is invalid. |
| NOT_ACCEPTABLE | When the data format or content you're trying to send is invalid or cannot be processed. |
| UNEXPECTED_ERROR | Any unexpected or unclassified error. Used as a fallback for debugging purposes. |
| CHAT_NOT_INITIATED | Thrown when chat SDK methods (sendMessage, createConversation, etc.)          are called before init(). |


  [](https://dev.sprinklr.com/save-chat-transcript-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/save-chat-transcript-headless-live-chat-sdk)
