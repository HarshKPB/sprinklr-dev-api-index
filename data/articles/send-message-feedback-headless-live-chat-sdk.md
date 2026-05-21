---
title: "Send Message Feedback Headless Live Chat SDK"
slug: send-message-feedback-headless-live-chat-sdk
url: https://dev.sprinklr.com/send-message-feedback-headless-live-chat-sdk
---

# Send Message Feedback Headless Live Chat SDK

# Send Message Feedback


The `sendMessageFeedback()` method submits user feedback (like or dislike) for a given message in a conversation.

## SDK Method

`sendMessageFeedback()`

## Example Usage




 Copy Code


// Send positive feedback (like)
try {
  const updatedMessage = await window.sprinklr.chat.sendMessageFeedback({
    conversationId: '627b7d2cb1628c58860f962c',
    messageId: '68e7bfbce7c5f52dbc9c22a0',
    feedbackRating: 1, // 1 for positive, 0 for negative
  });
  console.log('Feedback sent:', updatedMessage);
} catch (error) {
  console.error("Failed to send feedback:", error);
}
// Send negative feedback (dislike) with filledForm
// Note: filledForm is only used for negative feedback (rating: 0)
try {
  const updatedMessage = await window.sprinklr.chat.sendMessageFeedback({
    conversationId: '627b7d2cb1628c58860f962c',
    messageId: '68e7bfbce7c5f52dbc9c22a0',
    feedbackRating: 0,
    filledForm: {
      helpful: false,
      comment: 'This did not help me.',
    },
  });
  console.log('Feedback sent:', updatedMessage);
} catch (error) {
  console.error("Failed to send feedback:", error);
}



## Parameters





























``

``````








``````






| Parameter | Description | Type | Required/Optional | Sample |
| --- | --- | --- | --- | --- |
| messageId | Unique identifier of the message to provide feedback for | string | Required | 'msg_123456789' |
| conversationId | Unique identifier of the conversation containing the message | string | Required | 'conv_987654321' |
| feedbackRating | Feedback rating: 1 for positive, 0 for negativeEach message can only receive a feedbackRating once.Once a feedbackRating is submitted, it cannot be changed. Attempting to send feedback on a message that already has a feedbackRating will result in a NOT_ACCEPTABLE error. | Integer | Required | 1 (positive) or 0 (negative) |
| filledForm | Provides additional form data for detailed feedback. It allows users to provide additional context, comments, or form data when submitting negative feedback.   Only used for negative feedback (feedbackRating: 0). For positive feedback (feedbackRating: 1), filledForm should not be provided. | StringAnyMap | Optional | { "helpful": false, "comment": "This did not help me." } |

### Feedback Submission Requirements



    Feedback can only be sent on messages that have feedback enabled. A message must meet all of the following conditions:




- Feedback must be enabled in the application configuration (`messageFeedbackConfig.enabled` must be `true`)

- The message must be an auto-response/bot-generated message (`messagePayload.additional.IS_AUTO_RESPONSE` must be `true`)

- The message must not have `disableUserFeedback` set to `true` (either on the message payload or on the attachment)


## Response Format

The resolved `message` object will look like this:



{
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
    feedbackRating?: 0 | 1; // The feedback rating that was submitted
  };
}



## Error Types









      ``
      ``````


      ``

- ````
- ``````````
- ````
- ``````
- ``


      ``



      ``
      ``````



| Error Type | When It Occurs |
| --- | --- |
| NOT_FOUND | When the requested conversation, message, or resource cannot be found.          This typically happens when trying to access a conversation that has been deleted or when the          conversationId is invalid |
| NOT_ACCEPTABLE | Thrown in any of the following cases:                    Feedback configuration is not enabled (messageFeedbackConfig.enabled is false)           disableUserFeedback is enabled for the message (messagePayload.disableUserFeedback is true) or for the attachment (messagePayload.attachment.disableUserFeedback is true)           Message is not bot-generated (auto-response) – messagePayload.additional.IS_AUTO_RESPONSE is not true           feedbackRating is not 0 or 1           Feedback has already been submitted (message already has a feedbackRating value) |
| UNEXPECTED_ERROR | Any unexpected or unclassified error. Used as a fallback for debugging purposes |
| CHAT_NOT_INITIATED | Thrown when chat SDK methods (sendMessage, createConversation, etc.) are called before init() |


  [](https://dev.sprinklr.com/send-message-feedback-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/send-message-feedback-headless-live-chat-sdk)
