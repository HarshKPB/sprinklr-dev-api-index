---
title: "Launch LC Mobile SDK - React Native"
slug: launch-lc-mobile-sdk-react-native
url: https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native
---

# Launch LC Mobile SDK - React Native

# Launch Live Chat Mobile SDK - React Native


The Sprinklr Messenger can be launched and customized to fit your application’s needs. By default, the messenger opens with both the home screen and conversation view, but you can configure it to start in different modes such as a new conversation, the last active conversation, or even a specific conversation by ID.

This flexibility allows you to tailor the chat experience for your users, whether they need quick access to ongoing conversations, knowledge base articles, or predefined brand messages.

The following are the steps for integrating Sprinklr Messenger. This page covers the **fourth step: Launch**. Use the flow below to navigate through all steps of the integration process.

  [Install](https://dev.sprinklr.com/install-lc-mobile-sdk-react-native) >
  [Setup](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native) >
  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native) >
  **Launch** >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-react-native) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native)


**On this page:**



- [Launch Messenger](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#launch-messenger)

- [Customize Messenger View](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#customize-messenger-view)


## Launch Messenger


The messenger view can be displayed using any of the UI controls such as **Floating Action Button (FAB)**, **Messenger Icon**, or **Tab Bar Icon**, depending on your application requirements.


To present the messenger view, create a full‑page messenger view as shown in the following example. You can define the full‑page messenger view as a scene in your navigator and present it according to your use case.



import MessengerClient from '@sprinklrjs/chat-native-client'
MessengerClient.takeOff({
  appId: '', // This will be provided by Sprinklr
  environment: '', // This will be provided by Sprinklr
  pushAppId: '', // Should be Unique id, if not sure pass same as device ID
  deviceId: '',
  skin: 'MODERN', // default value is MODERN, options: CLASSIC | MODERN
  locale: '', // default value is en
  themeMode: 'DEFAULT' // default value is DEFAULT, options DEFAULT | DARK
})





### Parameters














   ``



| Parameter | Description |
| --- | --- |
| onDismiss | A callback function that handles closing of the messenger. |
| launchOptions | Defines how the messenger should be launched. You can use launchOptions to open the messenger in response to events such as notifications. |

## Customize Live Chat Messenger View

By default, the messenger opens with a home screen displaying all conversations. You can customize this behavior to launch Messenger with either the **default view** (home + conversation screens) or a **single conversation view**.

### See the relevant section:

- [Default View](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#default-view-main)
- [Single Conversation View](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#single-conversation-main)

### Default View

The default view shows both home and conversation screens.

#### Default View Options Quick Reference









      [Default View](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#default-view)



      [Default View with New Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#default-view-new-conversation)



      [Default View with Last Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#default-view-last-conversation)



      [Default View with Knowledge Base List](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#default-view-kb-list)



      [Default View with Custom Brand/User Messages](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#default-view-custom-message)



      [Default View with Particular Conversation ID](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#default-view-conversation-id)




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



import { MessengerView } from '@sprinklrjs/chat-native-client';
function SPRMessenger(launchOptions = {}, onDismiss) {
    return (

    );
}





### Parameters











    ``


| Parameter | Description |
| --- | --- |
| onDismiss | A callback function that handles closing of the messenger. |
| launchOptions | Defines how the messenger should be launched. You can also use launchOptions to open the messenger in response to events like notifications. |

## Default View with New Conversation

Use the following code to open the default view with a new conversation. This configuration will initiate a new conversation
on behalf of the user that starts with the welcome messages set in the application builder. To continue any existing conversations,users must return to the home screen.


**Dev Notes: **This configuration will open a new conversation every time, irrespective of whether the previous conversation was closed or not.

### Syntax



import { MessengerView } from '@sprinklrjs/chat-native-client';
function SPRMessenger(launchOptions = {}, onDismiss) {
  const chatInitialisationContext = {
    landingScreen: 'NEW_CONVERSATION',
  };
  return (

  );
}





### Parameters














    ``




    ``


| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| onDismiss | — | A callback function that handles the closing of the messenger. |
| launchOptions | — | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to NEW_CONVERSATION to start a new conversation when the messenger is launched. |

## Default View with Last Conversation

Use the following code to open the default view with the last conversation. This configuration will open the last conversation
that is still active. If there are no open conversations, Live Chat will initiate a new conversation on behalf of the user,
starting with the welcome messages set in the application builder.


**Dev Notes: **This configuration ensures that users return to their most recent active conversation. If none exist, a new conversation is automatically started.

### Syntax



import { MessengerView } from '@sprinklrjs/chat-native-client';
function SPRMessenger(launchOptions = {}, onDismiss) {
  const chatInitialisationContext = {
    landingScreen: 'LAST_CONVERSATION',
  };
  return (

  );
}





### Parameters














    ``




    ``


| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| onDismiss | — | A callback function that handles closing the messenger. |
| launchOptions | — | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to LAST_CONVERSATION to open the last active conversation when the messenger is launched. |

## Default View with Knowledge Base List

Use the following code to open the Knowledge Base list view in the Sprinklr Live Chat widget.
This will launch Live Chat with the Knowledge Base list view, enabling users to browse relevant articles before starting a conversation.


**Dev Notes: **This configuration is useful when you want users to explore knowledge base articles before initiating a chat conversation.

### Syntax



import { MessengerView } from '@sprinklrjs/chat-native-client';
function SPRMessenger(launchOptions = {}, onDismiss) {
  const chatInitialisationContext = {
    landingScreen: 'KNOWLEDGE_BASE_LIST',
  };
  return (

  );
}





### Parameters














    ``




    ``


| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| onDismiss | — | A callback function that handles closing the messenger. |
| launchOptions | — | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to KNOWLEDGE_BASE_LIST to open the knowledge base articles list when the messenger is launched. |

## Default View with Custom Brand/User Message

Use the following code to open the default view with a new conversation that starts with custom brand/user messages.
To continue any existing conversations, users must return to the home screen.


**Dev Notes: **This configuration allows you to predefine brand and user messages that appear when the chat starts,
  ensuring a customized conversation experience.

### Syntax



import { MessengerView } from '@sprinklrjs/chat-native-client';
function SPRMessenger(launchOptions = {}, onDismiss) {
  const chatInitialisationContext = {
    landingScreen: 'NEW_CONVERSATION',
    initialMessages: [
      {
        message: 'This is a brand message',
        isSentByUser: false,
      },
      'This is another brand message',
      {
        message: 'This is a user message',
        isSentByUser: true,
      },
    ],
  };
  return (

  );
}





### Parameters














    ``




    ``







| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| onDismiss | — | A callback function that handles closing the messenger. |
| launchOptions | — | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to NEW_CONVERSATION to start a new conversation when the messenger is launched. |
| chatInitialisationContext | initialMessages | Contains a list of predefined messages that appear when the chat starts. For more information, see the Initial Messages table. |

#### Initial Messages














    ````
****
****


| Parameter | Description | Possible Values |
| --- | --- | --- |
| message | The text of the message. | Any string value |
| isSentByUser | Defines whether the message was sent by the user or by the brand. | true, false         true: Indicates that the message is sent by the user.         false: Indicates that the message is sent by the brand. |

## Default View with Particular Conversation ID

Use the following code to open a specific conversation using its conversation ID. Ensure that the conversation you want to open
is not deleted and has the most recently published message.

To open a specific conversation, you need its conversation ID. You can capture the conversation ID by listening to events
indicating the ongoing conversation.


**Dev Notes: **This configuration is useful when you want to resume a specific conversation by its unique ID.
  Make sure the conversation is active and not deleted.

### Syntax



import { MessengerView } from '@sprinklrjs/chat-native-client';
function SPRMessenger(launchOptions = {}, onDismiss) {
  const chatInitialisationContext = {
    landingScreen: 'EXISTING_CONVERSATION',
    params: {
      conversationId: 'id_of_conversation',
    },
  };
  return (

  );
}





### Parameters














    ``




    ``







| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| onDismiss | — | A callback function that handles closing the messenger. |
| launchOptions | — | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to EXISTING_CONVERSATION to open an existing conversation. |
| chatInitialisationContext | params | Contains the parameters required for initializing the chat. For more information, see the params table. |

#### `params` Object










| Parameter | Description |
| --- | --- |
| conversationId | The unique ID of the conversation that you want to open. |

## Single Conversation View

You can choose to display only the conversation screen and hide the home screen completely.










      [Single Conversation View with New Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#single-new-conversation)



      [Single Conversation View with Last Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#single-last-conversation)



      [Single Conversation View with Custom Brand/User Messages](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#single-custom-message)



      [Single Conversation View with Conversation ID](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native#single-conversation-id)




| Option | Description |
| --- | --- |
|  | Always starts a new conversation with welcome messages. Previous conversations are not shown. |
|  | Opens the last active conversation. If none exist, starts a new one with welcome messages. |
|  | Starts a new conversation with predefined brand and/or user messages. Overrides welcome message. |
|  | Opens a specific existing conversation by its ID, bypassing the home screen. Must be active and not deleted. |

## Single Conversation View with New Conversation

When Live Chat is set to a single conversation view with `NEW_CONVERSATION`, it initiates a new conversation on behalf of the user.
This conversation starts with the welcome messages set in the application builder.

This configuration will always open a conversation view by initiating a new conversation and will not show any previous conversations that are currently open.


**Dev Notes: **Use this configuration when you want the messenger to operate strictly in single conversation mode,
  ensuring that only new conversations are initiated and no previous conversations are displayed.

### Syntax



import { MessengerView } from '@sprinklrjs/chat-native-client';
function SPRMessenger(launchOptions = {}, onDismiss) {
  const chatInitialisationContext = {
    scope: 'CONVERSATION',
    landingScreen: 'NEW_CONVERSATION',
  };
  return (

  );
}





### Parameters














    ``




    ``




    ``


| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| onDismiss | — | A callback function that handles closing the messenger. |
| launchOptions | — | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to NEW_CONVERSATION to open a new conversation. |
| chatInitialisationContext | scope | Defines the scope of the chat. Value CONVERSATION indicates the messenger operates within the conversation scope. |

## Single Conversation View with Last Conversation

When Live Chat is set to single conversation view with `LAST_CONVERSATION`, it opens the last conversation of the user that is still open.
If there are no open conversations, it initiates a new conversation on behalf of the user that starts with the welcome messages set in the application builder.


**Dev Notes: **This configuration ensures that users return to their most recent active conversation.
  If no active conversation exists, a new one is automatically started.

### Syntax



import { MessengerView } from '@sprinklrjs/chat-native-client';
function SPRMessenger(launchOptions = {}, onDismiss) {
  const chatInitialisationContext = {
    scope: 'CONVERSATION',
    landingScreen: 'LAST_CONVERSATION',
  };
  return (

  );
}





### Parameters














    ``




    ``




    ``


| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| onDismiss | — | A callback function that handles closing the messenger. |
| launchOptions | — | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to LAST_CONVERSATION to open the last active conversation when the messenger is launched. |
| chatInitialisationContext | scope | Defines the scope of the chat. Value CONVERSATION indicates the messenger operates within the conversation scope. |

## Single Conversation View with Custom Brand Message

Use the following code to open a single conversation view with a new conversation that starts with a custom message from your brand or user.


**Dev Notes: **If a welcome message is enabled in Live Chat with this view, the welcome message will not be displayed.
  Instead, the custom brand message is displayed.

### Syntax



import { MessengerView } from '@sprinklrjs/chat-native-client';
function SPRMessenger(launchOptions = {}, onDismiss) {
  const chatInitialisationContext = {
    scope: 'CONVERSATION',
    landingScreen: 'NEW_CONVERSATION',
    initialMessages: [
      {
        message: 'This is a brand message',
        isSentByUser: false,
      },
      'This is another brand message',
      {
        message: 'This is a user message',
        isSentByUser: true,
      },
    ],
  };
  return (

  );
}





### Parameters














    ``




    ``




    ``







| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| onDismiss | — | A callback function that handles closing the messenger. |
| launchOptions | — | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to NEW_CONVERSATION to start a new conversation when the messenger is launched. |
| chatInitialisationContext | scope | Defines the scope of the chat. Value CONVERSATION indicates the messenger operates within the conversation scope. |
| chatInitialisationContext | initialMessages | Contains a list of predefined messages that appear when the chat starts. For more information, see the Initial Messages table. |

#### Initial Messages














    ````
****
****


| Parameter | Description | Possible Values |
| --- | --- | --- |
| message | The text of the message. | Any string value |
| isSentByUser | Defines whether the message was sent by the user or by the brand. | true \| false         true: Indicates that the message is sent by the user.         false: Indicates that the message is sent by the brand. |

## Single Conversation View with Conversation ID

Use the following code to open a specific conversation without the home page. Ensure that the conversation you want to open
is not deleted and has the most recently published message.

To open a specific conversation, you need its conversation ID. You can capture the conversation ID by listening to events
indicating the ongoing conversation.


**Dev Notes: **This configuration is useful when you want to resume a specific conversation directly, bypassing the home screen.
  Make sure the conversation is active and not deleted.

### Syntax



import { MessengerView } from '@sprinklrjs/chat-native-client';
function SPRMessenger(launchOptions = {}, onDismiss) {
  const chatInitialisationContext = {
    scope: 'CONVERSATION',
    landingScreen: 'EXISTING_CONVERSATION',
    params: {
      conversationId: 'id_of_conversation',
    },
  };
  return (

  );
}





### Parameters














    ``




    ``




    ``







| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| onDismiss | — | A callback function that handles closing the messenger. |
| launchOptions | — | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to EXISTING_CONVERSATION to open an existing conversation. |
| chatInitialisationContext | scope | Defines the scope of the chat. Value CONVERSATION indicates the messenger operates within the conversation scope. |
| chatInitialisationContext | params | Contains the parameters required for initializing the chat. For more information, see the Params table. |

#### Params










| Parameter | Description |
| --- | --- |
| conversationId | The unique ID of the conversation that you want to open. |

## Next Steps

[Configure Live Chat Mobile SDK](https://dev.sprinklr.com/configure-lc-mobile-sdk-react-native)

## Additional Resources

See **All Integration Steps**
 [Install](https://dev.sprinklr.com/../install-lc-mobile-sdk-react-native) > [Setup](https://dev.sprinklr.com/setup-lc-mobile-sdk-react-native) > [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-react-native) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-react-native) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-react-native)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-react-native)

  [](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native)




[Back to top](https://dev.sprinklr.com/launch-lc-mobile-sdk-react-native)
