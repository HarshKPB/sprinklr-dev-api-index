---
title: "Live Chat Application APIs"
slug: live-chat-application-apis
url: https://dev.sprinklr.com/live-chat-application-apis
---

# Live Chat Application APIs

# Live Chat APIs

	Live chat is the capability that allows end customers to interact with brands via a messaging interface in real time. Live chat is often deployed on websites and is also referred to as Website chat. However, its usage is not limited to websites, it can be installed on mobile applications, blogs, forums, etc. Sprinklr live chat is powered by bots to answer the simple queries of customers; while the complex ones can be routed to an agent. Customers can also exchange images, videos, and documents with agents.

Live chat APIs are introduced for customers having their own live chat application UI, but aim to communicate through Sprinklr's backend. The Live Chat APIs allow using Sprinklr's backend to manage interaction elements such as handling existing conversations, initiate new conversations, continuing existing conversations, fetching new messages in real time, and chat user persona handling.

**Related Knowledge Base Article: ** **[Configure Sprinklr Live Chat Application](https://www.sprinklr.com/help/articles/create-live-chat-application/sprinklr-live-chat-builder/656d9b83a4191a67114d7adb)**

## Live Chat APIs Workflow

### 1. Initial Connection

- **[Handshake API](https://dev.sprinklr.com/handshake-api-fetch-application-details)** - To fetch Live Chat application details

- **[App Handshake API](https://dev.sprinklr.com/app-handshake-api)** - To authenticate the user

### 2. Existing Conversation Handling

- **[Fetch Latest Conversations](https://dev.sprinklr.com/fetch-conversations-api)**: To fetch the conversations that have been initiated so far within the live chat application

- **[Fetch Single Conversation](https://dev.sprinklr.com/fetch-single-conversation-api)** - To fetch a single conversation for the given conversation Id

- **[Fetch Messages](https://dev.sprinklr.com/fetch-messages-api)** - Fetch the messages within a live chat conversation

- **[Fetch Single Message](https://dev.sprinklr.com/fetch-single-message-api)** - fetch the a single message within a live chat conversation using the unique identifier for the conversation and message

- **[User LookUp API](https://dev.sprinklr.com/user-lookup-api)** -For searching profile information about end users who sent the messages on the live chat application

### 3. Initiating New Chats

- **[Create New Conversation](https://dev.sprinklr.com/create-new-conversation)** - to create a new conversation once the user has been authenticated

- **[Conversation Send](https://dev.sprinklr.com/conversation-send-api)** - to send messages to the live chat application

- **[Start Typing API](https://dev.sprinklr.com/start-typing-api)** - Helps indicate that the customer is typing and replying to a case

- **[Stop Typing](https://dev.sprinklr.com/stop-typing-api)** - Helps indicate that the customer has stopped typing

- **[Message Read Validation](https://dev.sprinklr.com/message-read-validation)** - Helps indicate that the message has been read by the end user

### 4. Continuing Existing Chats

- **[Conversation Send - Post Back API](https://dev.sprinklr.com/post-back-message)** - when user click on an old message and replies on the chat

- **[Start Typing API](https://dev.sprinklr.com/start-typing-api)** - Helps indicate that the customer is typing and replying to a case

- **[Stop Typing](https://dev.sprinklr.com/stop-typing-api)** - Helps indicate that the customer has stopped typing

- **[Message Read Validation](https://dev.sprinklr.com/message-read-validation)** - Helps indicate that the message has been read by the end user

### 5. Fetching New Messages in Real-Time (When Bot or Agent Responds)

- **[Message.Created Webhook](https://dev.sprinklr.com/message-webhooks)** - for fetching message Id and conversation Id

- **[Fetch Messages API](https://dev.sprinklr.com/fetch-messages-api)** - Fetch the messages within a live chat conversation using the conversation Id received in the webhook response

### 6. Chat User Persona Handling

- **[Message.Created Webhook](https://dev.sprinklr.com/message-webhooks)** - For fetching conversation and sender Id

- **[User LookUp API](https://dev.sprinklr.com/user-lookup-api)** - For searching profile information for a anonymous (unrecognized) sender
	[](https://dev.sprinklr.com/live-chat-application-apis)




[Back to top](https://dev.sprinklr.com/live-chat-application-apis)
