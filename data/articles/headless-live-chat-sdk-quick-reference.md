---
title: "Headless Live Chat SDK Quick Reference"
slug: headless-live-chat-sdk-quick-reference
url: https://dev.sprinklr.com/headless-live-chat-sdk-quick-reference
---

# Headless Live Chat SDK Quick Reference

# Headless Live Chat SDK Quick Reference


The Headless Live Chat SDK offers essential methods to initialize the SDK, create conversations, send messages, and subscribe to events.

Below is a table listing each method’s name and a brief description:

**Dev Notes: **Click the method name to view its complete documentation.









      [init()](https://dev.sprinklr.com/initialize-headless-live-chat-sdk)



      [createConversation()](https://dev.sprinklr.com/create-new-conversation-headless-live-chat-sdk)



      [sendMessage()](https://dev.sprinklr.com/send-message-headless-live-chat-sdk)



      [subscribeToEvents()](https://dev.sprinklr.com/subscribe-to-events-headless-live-chat-sdk)



      [getConversations()](https://dev.sprinklr.com/fetch-conversations-headless-live-chat-sdk)



      [getMessages()](https://dev.sprinklr.com/fetch-messages-headless-live-chat-sdk)



      [updateUser()](https://dev.sprinklr.com/update-user-headless-live-chat-sdk)



      [updateConversationContext()](https://dev.sprinklr.com/update-conversation-context-headless-live-chat-sdk)



      [closeConversation()](https://dev.sprinklr.com/close-conversations-headless-live-chat-sdk)



      [deleteConversation()](https://dev.sprinklr.com/delete-conversation-headless-live-chat-sdk)



      [readMessage()](https://dev.sprinklr.com/read-message-headless-live-chat-sdk)



  [updateLocale()](https://dev.sprinklr.com/update-locale-headless-live-chat-sdk)


  [sendMessageFeedback()](https://dev.sprinklr.com/send-message-feedback-headless-live-chat-sdk)


  [saveChatTranscript()](https://dev.sprinklr.com/save-chat-transcript-headless-live-chat-sdk)


  [downloadAttachment()](https://dev.sprinklr.com/download-attachment-headless-live-chat-sdk)




| SDK Method | Description |
| --- | --- |
|  | Initializes headless Live Chat SDK. |
|  | Starts a new conversation. |
|  | Publishes a message either in an ongoing open conversation or while creating a new conversation. |
|  | Subscribes to real-time updates like messages received, typing indicators, and conversation status changes. |
|  | Fetches a list of existing Live Chat conversations. |
|  | Fetches messages for a given Live Chat conversation. |
|  | Dynamically updates details of the currently logged-in user. With this method, you can update user profile information, custom user data, and user context metadata. |
|  | Dynamically updates the context metadata of a conversation. With this method, you can add or modify conversation-specific context data that can be used for filtering, categorization, and business logic. |
|  | Closes one or all conversations |
|  | Permanently deletes one or all conversations. This method removes conversations from the system. |
|  | Marks messages as read in a conversation. This method allows you to update the read status of messages. This helps track which messages have been viewed by the user and maintains proper unread count tracking. |
|  | Updates the locale (language) of the currently logged-in user dynamically. |
|  | Submits user feedback (like or dislike) for a given message in a conversation. |
|  | Saves the chat transcript for a specific conversation as a text file. |
|  | Downloads media attachments (images, videos, documents, audio files) from a specific message in a conversation. |


  [](https://dev.sprinklr.com/headless-live-chat-sdk-quick-reference)




[Back to top](https://dev.sprinklr.com/headless-live-chat-sdk-quick-reference)
