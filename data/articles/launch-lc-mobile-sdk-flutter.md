---
title: "Launch LC Mobile SDK - Flutter"
slug: launch-lc-mobile-sdk-flutter
url: https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter
---

# Launch LC Mobile SDK - Flutter

# Launch Live Chat Mobile SDK - Flutter


The Sprinklr Messenger can be launched and customized to fit your application’s needs. By default, the messenger opens with both the home screen and conversation view, but you can configure it to start in different modes such as a new conversation, the last active conversation, or even a specific conversation by ID.

This flexibility allows you to tailor the chat experience for your users, whether they need quick access to ongoing conversations, knowledge base articles, or predefined brand messages.

The following are the steps for integrating Sprinklr Messenger. This page covers the **third step: Launch**. Use the flow below to navigate through all steps of the integration process.

  [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-flutter) >
  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-flutter) >
  **Launch** >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-flutter) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter)


**On this page:**



- [Launch Messenger](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#launch-messenger)

- [Customize Messenger View](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#customize-messenger-view)


## Launch Messenger


To launch the application, add the following code with the button present inside your application:



SPRMessenger().startApplication();




## Customize Live Chat Messenger View

By default, the messenger opens with a home screen displaying all conversations. You can customize this behavior to launch Messenger with either the **default view** (home + conversation screens) or a **single conversation view**.

### See the relevant section:

- [Default View](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#default-view-main-heading)
- [Single Conversation View](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#single-conversation-view-main-heading)

### Default View

The default view shows both home and conversation screens.









      [Default View](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#default-view)



      [Default View with New Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#default-view-with-new-conversation)



      [Default View with Last Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#default-view-with-last-conversation)



      [Default View with Knowledge Base List](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#default-view-with-knowledge-base-list)



      [Default View with Custom Brand/User Message](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#default-view-with-custom-branduser-message)



      [Default View with Particular Conversation ID](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#default-view-with-particular-conversation-id)




| Option | Description |
| --- | --- |
|  | Opens with both the home screen and the conversation screen. |
|  | Always starts a new conversation with welcome messages. Previous conversations are not continued. |
|  | Opens the last active conversation. If none exist, starts a new one with welcome messages. |
|  | Launches with the Knowledge Base list view, allowing users to browse articles before starting a chat. |
|  | Starts a new conversation with predefined brand and/or user messages. |
|  | Opens a specific existing conversation by its ID (must be active and not deleted). |

## Default View

By default, Live Chat opens with both the home screen and the conversation screen. This configuration provides the standard entry point for users, showing the messenger’s home and any active conversations.

### Syntax



SPRMessenger().startApplication();




## Default View with New Conversation

Use the following code to open the default view with a new conversation. This configuration will initiate a new conversation on behalf of the user that starts with the welcome messages set in the application builder. To continue any existing conversations,users must return to the home screen.

**Dev Notes: **This configuration will open a new conversation every time, irrespective of whether the previous conversation was closed or not.

### Syntax



SPRMessenger().startApplication(chatInitialisationContext: {
     "landingScreen": "NEW_CONVERSATION",
   });




### Parameters




















      ``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| chatInitialisationContext | Required | Object | Context object used to configure the initial state of the chat application when starting. |
| landingScreen | Optional | String | Defines which screen should be displayed when the chat application starts.           Example: "NEW_CONVERSATION" launches directly into a new conversation screen. |

## Default View with Last Conversation

Use the following code to open the default view with the last conversation. This configuration will open the last conversation
that is still active. If there are no open conversations, Live Chat will initiate a new conversation on behalf of the user,
starting with the welcome messages set in the application builder.


**Dev Notes: **This configuration ensures that users return to their most recent active conversation. If none exist, a new conversation is automatically started.

### Syntax



SPRMessenger().startApplication(chatInitialisationContext: {
     "landingScreen": "LAST_CONVERSATION",
   });




### Parameters




















      ``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| chatInitialisationContext | Required | Object | Context object used to configure the initial state of the chat application when starting. |
| landingScreen | Optional | String | Defines which screen should be displayed when the chat application starts.           Example: "LAST_CONVERSATION" launches directly into the most recent conversation screen. |

## Default View with Knowledge Base List

Use the following code to open the Knowledge Base list view in the Sprinklr Live Chat widget. This will launch Live Chat with the Knowledge Base list view, enabling users to browse relevant articles before starting a conversation.


**Dev Notes: **This configuration is useful when you want users to explore knowledge base articles before initiating a chat conversation.

### Method



SPRMessenger().startApplication(chatInitialisationContext: {
     "landingScreen": "KNOWLEDGE_BASE_LIST",
   });




### Parameters




















      ``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| chatInitialisationContext | Required | Object | Context object used to configure the initial state of the chat application when starting. |
| landingScreen | Optional | String | Defines which screen should be displayed when the chat application starts.           Example: "KNOWLEDGE_BASE_LIST" launches directly into the knowledge base list screen, allowing users to browse available articles or FAQs. |

## Default View with Custom Brand/User Message

Use the following code to open the default view with a new conversation that starts with custom brand/user messages.
To continue any existing conversations, users must return to the home screen.


**Dev Notes: **This configuration allows you to predefine brand and user messages that appear when the chat starts,
  ensuring a customized conversation experience.

### Syntax



SPRMessenger().startApplication(chatInitialisationContext: {
    'landingScreen': 'NEW_CONVERSATION',
    'initialMessages': [
        'This is a brand message',
        'This is another brand message',
    ],
});



### Parameters




















      ``





      ``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| chatInitialisationContext | Required | Object | Context object used to configure the initial state of the chat application when starting. |
| landingScreen | Optional | String | Defines which screen should be displayed when the chat application starts.           Example: "NEW_CONVERSATION" launches directly into a new conversation screen. |
| initialMessages | Optional | Array<String> | Pre-populates the chat with one or more initial messages when the conversation starts.           Example: ["This is a brand message", "This is another brand message"]. |

## Default View with Particular Conversation ID

Use the following code to open a specific conversation using its conversation ID. Ensure that the conversation you want to open
is not deleted and has the most recently published message.

To open a specific conversation, you need its conversation ID. You can capture the conversation ID by listening to events
indicating the ongoing conversation.


**Dev Notes: **This configuration is useful when you want to resume a specific conversation by its unique ID.
  Make sure the conversation is active and not deleted.

### Syntax



SPRMessenger().startApplication(chatInitialisationContext: {
     "landingScreen": "EXISTING_CONVERSATION",
     "params": {
       "conversationId": "id_of_conversation",
     }
   });



### Parameters




















      ``









      ``

      ``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| chatInitialisationContext | Required | Object | Context object used to configure the initial state of the chat application when starting. |
| landingScreen | Optional | String | Defines which screen should be displayed when the chat application starts.           Example: "EXISTING_CONVERSATION" launches directly into a specific existing conversation. |
| params | Optional | Object | Additional configuration parameters required when launching into an existing conversation. |
| conversationId | Required (when landingScreen = "EXISTING_CONVERSATION") | String | Unique identifier of the conversation to be opened.           Example: "id_of_conversation". |

## Single Conversation View

You can choose to display only the conversation screen and hide the home screen completely.










      [Single Conversation View](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#single-conversation-view)



      [Single Conversation View with New Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#single-conversation-view-with-new-conversation)



      [Single Conversation View with Last Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#single-conversation-view-with-last-conversation)



      [Single Conversation View with Custom Brand/User Messages](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#single-conversation-view-with-custom-branduser-messages)



      [Single Conversation View with Conversation ID](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter#single-conversation-view-with-conversation-id)




| Option | Description |
| --- | --- |
|  | Directly opens the conversation screen in Live Chat and hides the home screen. |
|  | Always starts a new conversation with welcome messages. Previous conversations are not shown. |
|  | Opens the last active conversation. If none exist, starts a new one with welcome messages. |
|  | Starts a new conversation with predefined brand and/or user messages. Overrides the welcome message. |
|  | Opens a specific existing conversation by its ID, bypassing the home screen. Must be active and not deleted. |

## Single Conversation View


Use the following code to directly open the conversation screen in Live Chat and hide the home screen.

### Syntax



SPRMessenger().startApplication(chatInitialisationContext: {
     "scope": "CONVERSATION",
   });



### Parameters





















      ``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| chatInitialisationContext | Required | Object | Context object used to configure the initial state of the chat application when starting. |
| scope | Optional | String | Defines the scope of the chat session.           Example: "CONVERSATION" launches the application with the scope limited to a specific conversation context. |

## Single Conversation View with New Conversation

When Live Chat is set to a single conversation view with `NEW_CONVERSATION`, it initiates a new conversation on behalf of the user.
This conversation starts with the welcome messages set in the application builder.

This configuration will always open a conversation view by initiating a new conversation and will not show any previous conversations that are currently open.


**Dev Notes: **Use this configuration when you want the messenger to operate strictly in single conversation mode,
  ensuring that only new conversations are initiated and no previous conversations are displayed.

### Syntax



SPRMessenger().startApplication(chatInitialisationContext: {
     "scope": "CONVERSATION",
     "landingScreen": "NEW_CONVERSATION",
   });



### Parameters




















      ``





      ``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| chatInitialisationContext | Required | Object | Context object used to configure the initial state of the chat application when starting. |
| scope | Optional | String | Defines the scope of the chat session.           Example: "CONVERSATION" launches the application with the scope limited to a specific conversation context. |
| landingScreen | Optional | String | Defines which screen should be displayed when the chat application starts.           Example: "NEW_CONVERSATION" launches directly into a new conversation screen. |

## Single Conversation View with Last Conversation

When Live Chat is set to single conversation view with `LAST_CONVERSATION`, it opens the last conversation of the user that is still open.
If there are no open conversations, it initiates a new conversation on behalf of the user that starts with the welcome messages set in the application builder.


**Dev Notes: **This configuration ensures that users return to their most recent active conversation.
  If no active conversation exists, a new one is automatically started.

### Syntax



SPRMessenger().startApplication(chatInitialisationContext: {
     "scope": "CONVERSATION",
     "landingScreen": "LAST_CONVERSATION",
   });



### Parameters




















      ``





      ``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| chatInitialisationContext | Required | Object | Context object used to configure the initial state of the chat application when starting. |
| scope | Optional | String | Defines the scope of the chat session.           Example: "CONVERSATION" launches the application with the scope limited to a specific conversation context. |
| landingScreen | Optional | String | Defines which screen should be displayed when the chat application starts.           Example: "LAST_CONVERSATION" launches directly into the most recent conversation screen. |

## Single Conversation View with Custom Brand Message

Use the following code to open a single conversation view with a new conversation that starts with a custom message from your brand or user.


**Dev Notes: **If a welcome message is enabled in Live Chat with this view, the welcome message will not be displayed.
  Instead, the custom brand message is displayed.

### Syntax



SPRMessenger().startApplication(chatInitialisationContext: {
     "scope": "CONVERSATION",
     "landingScreen": "EXISTING_CONVERSATION",
     "params": {
       "conversationId": "id_of_conversation",
     }
   });



### Parameters




















      ``





      ``









      ``

      ``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| chatInitialisationContext | Required | Object | Context object used to configure the initial state of the chat application when starting. |
| scope | Optional | String | Defines the scope of the chat session.           Example: "CONVERSATION" launches the application with the scope limited to a specific conversation context. |
| landingScreen | Optional | String | Defines which screen should be displayed when the chat application starts.           Example: "EXISTING_CONVERSATION" launches directly into a specific existing conversation. |
| params | Optional | Object | Additional configuration parameters required when launching into an existing conversation. |
| conversationId | Required (when landingScreen = "EXISTING_CONVERSATION") | String | Unique identifier of the conversation to be opened.           Example: "id_of_conversation". |

## Single Conversation View with Conversation ID

Use the following code to open a specific conversation without the home page. Ensure that the conversation you want to open
is not deleted and has the most recently published message.

To open a specific conversation, you need its conversation ID. You can capture the conversation ID by listening to events
indicating the ongoing conversation.


**Dev Notes: **This configuration is useful when you want to resume a specific conversation directly, bypassing the home screen.
  Make sure the conversation is active and not deleted.

### Syntax



SPRMessenger().startApplication(chatInitialisationContext: {
  "scope": "CONVERSATION",
  "landingScreen": "EXISTING_CONVERSATION",
  "params": {
    "conversationId": "id_of_conversation",
  }
});



### Parameters




















      ``





      ``









      ``

      ``



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| chatInitialisationContext | Required | Object | Context object used to configure the initial state of the chat application when starting. |
| scope | Optional | String | Defines the scope of the chat session.           Example: "CONVERSATION" launches the application with the scope limited to a specific conversation context. |
| landingScreen | Optional | String | Defines which screen should be displayed when the chat application starts.           Example: "EXISTING_CONVERSATION" launches directly into a specific existing conversation. |
| params | Optional | Object | Additional configuration parameters required when launching into an existing conversation. |
| conversationId | Required (when landingScreen = "EXISTING_CONVERSATION") | String | Unique identifier of the conversation to be opened.           Example: "id_of_conversation". |

## Next Steps

[Configure Live Chat Mobile SDK](https://dev.sprinklr.com/configure-lc-mobile-sdk-flutter)

## Additional Resources

See **All Integration Steps**

  [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-flutter) >
  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-flutter) >
  [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter) >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-flutter) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-flutter)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-flutter)

  [](https://dev.sprinklr.com/launch-lc-mobile-sdk-fluttere)




[Back to top](https://dev.sprinklr.com/launch-lc-mobile-sdk-flutter)
