---
title: "Install Live Chat Web SDKs"
slug: install-live-chat-web-sdks
url: https://dev.sprinklr.com/install-live-chat-web-sdks
---

# Install Live Chat Web SDKs

# Install Live Chat Web SDKs

You can create a Live Chat application from your Sprinklr Service account and embed the application to your website. After the application is embedded on your website, you can use the SDK methods to define the behavior of the Live Chat support according to your requirements.

## Prerequisites

Before you begin, complete the following prerequisites:

- You have a Sprinklr Service account and have the necessary permissions to manage Live Chat applications. For details about what permissions you need, see [Creating a Live Chat Application](https://www.sprinklr.com/help/articles/create-live-chat-application/creating-a-live-chat-application/63bc490c3fece76798a38d99).

- Create a Live Chat app on the Live Chat builder. For steps, see [Sprinklr Live Chat builder](https://www.sprinklr.com/help/articles/create-live-chat-application/sprinklr-live-chat-builder/656d9b83a4191a67114d7adb).

- Install the Live Chat app on your website by embedding the generated Live Chat code by the builder. For details about where to embed the code, see [Installing on web](https://www.sprinklr.com/help/articles/website-installation/installing-on-web/63bc490bf7c92723b10e6eed).

- Configure Live Chat app settings such as locale, user, device type, and more. To view the list of settings, see [Configure Live Chat app settings](https://dev.sprinklr.com/configure-live-chat-app-settings).

## SDK methods

After you install the Live Chat app on your website, you can use the Live Chat SDK methods to customize the application according to your brand’s requirements. You can define how users can open and close the Live Chat app, what information is shown when the chat window opens, and more.

The following table lists the use cases and corresponding SDK methods that you can use to implement them:

**Dev Notes: **For detailed documentation, click the method name in the SDK method column.



**** **** **** ****



[sprChat(‘open’)](https://dev.sprinklr.com/open-or-close-the-live-chat-window)

[sprChat('close')](https://dev.sprinklr.com/open-or-close-the-live-chat-window)

[sprChat(‘openNewConversation’)](https://dev.sprinklr.com/open-a-new-or-existing-conversation)

[sprChat(‘openExistingConversation’)](https://dev.sprinklr.com/open-a-new-or-existing-conversation)

[sprChat(‘updateConversationContext’)](https://dev.sprinklr.com/update-conversation-custom-fields-or-context)

[sprChat(‘updateClientContext’)](https://dev.sprinklr.com/update-client-custom-fields-or-context)

[sprChat(‘updateUserSettings’)](https://dev.sprinklr.com/update-user-details)

[sprChat(‘sendExternalEvent’)](https://dev.sprinklr.com/send-message-event-to-conversation)

[sprChat(‘subscribeToUpdate’)](https://dev.sprinklr.com/subscribe-to-live-chat-updates)

[sprChat(‘unsubscribeToUpdate’)](https://dev.sprinklr.com/unsubscribe-to-live-chat-updates)

[sprChat('updatelocale','locale')](https://dev.sprinklr.com/change-language-of-live-chat)

[sprChat(‘addFilterToEvaluate’)](https://dev.sprinklr.com/add-filter-to-evaluate-live-chat-state)

[sprChat(‘removeFilterToEvaluate’)](https://dev.sprinklr.com/remove-filter)

[sprChat(‘disable’)](https://dev.sprinklr.com/disable-or-enable-live-chat)

[sprChat(‘enable’)](https://dev.sprinklr.com/disable-or-enable-live-chat)

| Action | SDK method | Description | Example usage |
| --- | --- | --- | --- |
| Open the Live Chat window |  | This method opens the chat window. | You can use this method to open the chat window when customer clicks Contact Us on your website. |
| Close the Live Chat window |  | This method closes the chat window. |  |
| Open a new conversation |  | This method opens the chat window and starts a new conversation on behalf of the customer. | When a first-time visitor seeks assistance, you can automatically open a new chat with a personalized welcome message. |
| Open an existing conversation |  | This method opens the latest active and open conversation. You can also use this method to open a particular conversation, if you have the ID captured. | You can use this method to reopen an existing conversation for a returning user to the website. |
| Update Custom Fields of a conversation |  | This method is used to update custom fields/context during or after a conversation. | After a purchase is made on the website, you might want to set the transaction amount or ID on the case for reporting. After doing this, you can attribute sales to each conversation/case. |
| Update client Custom Fields |  | This method is used to update custom fields/context for all the subsequent conversations that will be started after this update. | When a user updates their profile information, you can use this method to ensure that this updated information is reflected in all future chat interactions. |
| Update user details |  | This method is used to update user details. | If a user logs in, you can authenticate their details and personalize the chat experience, such as by addressing them by name or recalling their previous issues, fostering a more tailored interaction. |
| Send a message or event to an ongoing conversation |  | This method is used to publish a message or send an event to a conversation. | Send notifications or alerts to users in an ongoing conversation. For instance, notifying users about promotional offers. |
| Subscribe to Live Chat updates |  | This method is used to either receive proactive updates from the Live Chat application about the current state or listen to the status of the previously fired SDK requests. | You can use event subscriptions to enhance customer support by monitoring chat availability, tracking unread messages for agents, responding to external events triggered by a bot or rule, and gathering analytics on user interactions. |
| Unsubscribe to Live Chat updates |  | This method is used to unsubscribe from Live Chat events that you subscribed to earlier. | This allows you to unsubscribe from the previously subscribed notification updates. |
| Change language of Live Chat |  | This method is used to change the language of Live Chat at any time. | During a chat, if a user switches their preferred language, you can use the SDK to instantly update the chat language. |
| Add filter to evaluate Live Chat state |  | This method is used to query the state of Live Chat using filters. |  |
| Remove filter |  | This method is used to remove the filters that were previously set using the addFilterToEvaluate method. |  |
| Disable Live Chat |  | This method disables the Live Chat app completely on the website. | If there are technical issues with the chat system or if all support agents are unavailable, you can disable Live Chat. This prevents users from attempting to reach support when it can't be provided. |
| Enable Live Chat |  | This method enables the Live Chat app. | After the technical issues are resolved or agents become available again, you can enable Live Chat so that users can start reaching out to support for assistance. |

[](https://dev.sprinklr.com/install-live-chat-web-sdks)

[Back to top](https://dev.sprinklr.com/install-live-chat-web-sdks)
