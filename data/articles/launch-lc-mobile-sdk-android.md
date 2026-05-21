---
title: "Launch LC Mobile SDK - Android"
slug: launch-lc-mobile-sdk-android
url: https://dev.sprinklr.com/launch-lc-mobile-sdk-android
---

# Launch LC Mobile SDK - Android

# Launch Live Chat Mobile SDK - Android


Sprinklr Messenger can be launched in different modes to fit your application’s needs. By default, it opens with both the home screen and conversation view, but you can set it to start in other modes such as a new conversation, the last active conversation, or a specific conversation by ID. This flexibility lets you shape the chat experience for your users, whether they need quick access to ongoing conversations, knowledge base articles, or predefined brand messages.

The following are the steps for integrating Sprinklr Messenger. This page covers the **third step: Launch**. Use the flow below to navigate through all steps of the integration process.

  [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-android) >
  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-android) >
  **Launch** >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-android) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android)


**On this page:**



- [Launch Messenger](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#launch-messenger)

- [Default View Options](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#default-view)

- [Single Conversation View Options](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#single-conversation-view-main)


## Launch Messenger


Add the following code inside the `onClick` event of the messenger button in your application:



SPRMessenger.shared().startApplication();




## Customize Messenger Launch View

By default, the messenger opens with a home screen displaying all conversations. You can customize this behavior to launch Messenger with either the **default view** (home + conversation screens) or a **single conversation view**.

### See the relevant section:



- [Default View](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#default-view)

- [Single Conversation View](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#single-conversation-view-main)

### Default View

The default view shows both home and conversation screens.






    [Default View](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#default-view)



    [Default View with New Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#default-view-new-conversation)



    [Default View with Last Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#default-view-last-conversation)



    [Default View with Knowledge Base List](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#default-view-knowledge-base)



    [Default View with Custom Brand/User Messages](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#default-view-custom-messages)



    [Default View with Conversation ID](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#default-view-conversation-id)



    [Default View with Video Call](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#default-view-video-call)



    [Default View with Audio Call](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#default-view-audio-call)



| Option | Description |
| --- | --- |
|  | Opens with both the home screen and the conversation screen. |
|  | Always starts a new conversation with welcome messages. Previous conversations are not continued. |
|  | Opens the last active conversation. If none exist, starts a new one with welcome messages. |
|  | Launches with the Knowledge Base list view, allowing users to browse articles before starting a chat. |
|  | Starts a new conversation with predefined brand and/or user messages. |
|  | Opens a specific existing conversation by its ID (must be active and not deleted). |
|  | Starts a new conversation and configures the messenger to initiate a video call. |
|  | Starts a new conversation and configures the messenger to initiate an audio call. |

## Default View

By default, Live Chat opens with both the home screen and the conversation screen. This configuration provides the standard entry point for users, showing the messenger’s home and any active conversations.

### Syntax



SPRMessenger.shared().startApplication();




## Default View with New Conversation

Use the following code to launch the messenger in its default view with a new conversation. This starts a fresh chat for the user, beginning with the welcome messages defined in the application builder. To continue any existing conversations, users need to navigate back to the home screen.


**Dev Notes: **This configuration will open a new conversation every time, irrespective of whether the previous conversation was closed or not.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("landingScreen", "NEW_CONVERSATION");
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);




### Parameters








    ``



| Parameter | Description | Type |
| --- | --- | --- |
| landingScreen | Defines the screen shown when the messenger launches. In this example, it is set to NEW_CONVERSATION. | String |

## Default View with Last Conversation

Use the following code to open the default view with the last conversation. This configuration will open the last conversation that is still active. If there are no open conversations, Live Chat will initiate a new conversation on behalf of the user, starting with the welcome messages set in the application builder.


**Dev Notes: **This configuration ensures that users return to their most recent active conversation. If none exist, a new conversation is automatically started.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("landingScreen", "LAST_CONVERSATION");
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);




### Parameters








    ``



| Parameter | Description | Type |
| --- | --- | --- |
| landingScreen | Defines the screen shown when the messenger launches. In this example, it is set to LAST_CONVERSATION. | String |

## Default View with Knowledge Base List

Use the following code to open the Knowledge Base list view in the Sprinklr Live Chat widget. This will launch Live Chat with the Knowledge Base list view, enabling users to browse relevant articles before starting a conversation.


**Dev Notes: **This configuration is useful when you want users to explore knowledge base articles before initiating a chat conversation.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("landingScreen", "KNOWLEDGE_BASE_LIST");
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);




### Parameters









    ``


| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| chatInitialisationContext | landingScreen | Defines the screen shown when the messenger launches. In this example, it is set to KNOWLEDGE_BASE_LIST to open the knowledge base articles list when the messenger is launched. |

## Default View with Custom Brand/User Message

Use the following code to open the default view with a new conversation that starts with custom brand/user messages.To continue any existing conversations, users must return to the home screen.


**Dev Notes: **This configuration allows you to predefine brand and user messages that appear when the chat starts,
  ensuring a customized conversation experience.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("landingScreen", "NEW_CONVERSATION");
Bundle brandMessage = new Bundle();
  brandMessage.putString("message", "This is a brand message");
  brandMessage.putBoolean("isSentByUser", false);
Bundle userMessage = new Bundle();
  userMessage.putString("message", "This is a user message");
  userMessage.putBoolean("isSentByUser", true);
  bundle.putParcelableArray("initialMessages", new Bundle[]{brandMessage, userMessage});
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);



### Parameters








    ``








| Parameter | Description | Type |
| --- | --- | --- |
| landingScreen | Defines the screen shown when the messenger launches. In this example, it is set to NEW_CONVERSATION. | String |
| initalMessages | Contains a list of predefined messages that appear when the chat starts. For more information, see the initialMessages table. | String |

#### initalMessages Parameters














    ````
****
****


| Parameter | Description | Possible Values |
| --- | --- | --- |
| message | The text of the message. | Any string value |
| isSentByUser | Defines whether the message was sent by the user or by the brand. | true, false         true: Indicates that the message is sent by the user.         false: Indicates that the message is sent by the brand. |

## Default View with Conversation ID

Use the following code to open a specific conversation using its conversation ID. Ensure that the conversation you want to open is not deleted and has the most recently published message.

To open a specific conversation, you need its conversation ID. You can capture the conversation ID by listening to events indicating the ongoing conversation.


**Dev Notes: **This configuration is useful when you want to resume a specific conversation by its unique ID. Make sure the conversation is active and not deleted.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("landingScreen", "EXISTING_CONVERSATION");
Bundle params = new Bundle();
  params.putString("conversationId", "id_of_conversation");
​  bundle.putBundle("params", params);
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);



### Parameters








    ``









    ``



| Parameter | Description | Type |
| --- | --- | --- |
| landingScreen | Specifies the screen shown when the messenger launches. In this example, it is set to EXISTING_CONVERSATION. | String |
| chatInitialisationContext | Contains all launch parameters for the messenger. Developers must place their configuration bundle inside this key so the application starts with the correct context. | Bundle |
| params | Holds additional parameters required by the chosen landing screen. For EXISTING_CONVERSATION, this includes the conversation identifier. | Bundle |

### `params` Parameters












| Parameter | Description | Type |
| --- | --- | --- |
| conversationId | The unique identifier of the conversation to open when the messenger launches. | String |

## Default View with Video Call

Use the following code to open a new conversation and configure the messenger to initiate a video call.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("landingScreen", "NEW_CONVERSATION");
  bundle.putStringArray("initialMessages", new String[]{});
Bundle additional = new Bundle();
  additional.putString("callType", "VIDEO");
  bundle.putBundle("additional", additional);
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);



### Parameters








    ``


















| Parameter | Description | Type |
| --- | --- | --- |
| landingScreen | Specifies the screen shown when the messenger launches. In this example, it is set to NEW_CONVERSATION. | String |
| initialMessages | An array of messages that can be preloaded into the new conversation. This can be empty if no messages are required. | String[] |
| chatInitialisationContext | Contains all launch parameters for the messenger. Developers must place their configuration bundle inside this key so the application starts with the correct context. | Bundle |
| additional | Holds extra parameters for the conversation, such as call type. | Bundle |

### `additional` Parameters








    ``



| Parameter | Description | Type |
| --- | --- | --- |
| callType | Specifies the type of call to initiate within the conversation. In this example, it is set to VIDEO. | String |

## Default View with Audio Call

Use the following code to open a new conversation and configure the messenger to initiate an audio call.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("landingScreen", "NEW_CONVERSATION");
  bundle.putStringArray("initialMessages", new String[]{});
Bundle additional = new Bundle();
  additional.putString("callType", "AUDIO");
  bundle.putBundle("additional", additional);
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);



### Parameters








    ``


















| Parameter | Description | Type |
| --- | --- | --- |
| landingScreen | Specifies the screen shown when the messenger launches. In this example, it is set to NEW_CONVERSATION. | String |
| initialMessages | An array of messages that can be preloaded into the new conversation. This can be empty if no messages are required. | String[] |
| chatInitialisationContext | A required key that contains all launch parameters for the messenger. Developers must place their configuration bundle inside this key so the application starts with the correct context. | Bundle |
| additional | A nested bundle that holds extra parameters for the conversation, such as call type. | Bundle |

### `additional` Parameters








    ``



| Parameter | Description | Type |
| --- | --- | --- |
| callType | Specifies the type of call to initiate within the conversation. In this example, it is set to AUDIO. | String |

## Single Conversation View

You can choose to display only the conversation screen and hide the home screen completely.







    [Single Conversation View](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#single-conversation-view)



    [Single Conversation View with New Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#single-conversation-new)



    [Single Conversation View with Last Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#single-conversation-last)



    [Single Conversation View with Custom Brand/User Message](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#single-conversation-custom)



    [Single Conversation View with Conversation ID](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#single-conversation-id)



    [Single Conversation View with Video Call](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#single-conversation-video-call)



    [Single Conversation View with Audio Call](https://dev.sprinklr.com/launch-lc-mobile-sdk-android#single-conversation-audio-call)



| Option | Description |
| --- | --- |
|  | Displays only the conversation screen in Live Chat and hides the home screen. |
|  | Initiates a new conversation on behalf of the user. Previous conversations are not shown. |
|  | Opens the most recent active conversation. If none exist, a new one is started with welcome messages. |
|  | Starts a new conversation with predefined brand and/or user messages. Overrides the default welcome message. |
|  | Resumes a specific existing conversation by its unique ID (must be active and not deleted). |
|  | Starts a new conversation and configures the messenger to initiate a video call. |
|  | Starts a new conversation and configures the messenger to initiate an audio call. |

## Single Conversation View

Use the following code to display only the conversation screen in Live Chat and hide the home screen.

**Dev Notes: **The `scope:'CONVERSATION'` option limits Live Chat to only the conversation screen.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("scope", "CONVERSATION");
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);



### Parameters








    ``








| Parameter | Description | Type |
| --- | --- | --- |
| scope | Defines the scope of the messenger launch. In this example, it is set to CONVERSATION, which restricts the launch context to a single conversation view. | String |
| chatInitialisationContext | Contains all launch parameters for the messenger. Developers must place their configuration bundle inside this key so the application starts with the correct context. | Bundle |

## Single Conversation View with New Conversation

When Live Chat is set to a single conversation view with `NEW_CONVERSATION`, it initiates a new conversation on behalf of the user. This conversation starts with the welcome messages set in the Live Chat application builder.

This configuration will always open a conversation view by initiating a new conversation and will not show any previous conversations that are currently open.


**Dev Notes: **Use this configuration when you want the messenger to operate strictly in single conversation mode,
  ensuring that only new conversations are initiated and no previous conversations are displayed.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("scope", "CONVERSATION");
  bundle.putString("landingScreen", "NEW_CONVERSATION");​
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);



### Parameters








    ``




    ``








| Parameter | Description | Type |
| --- | --- | --- |
| scope | Defines the scope of the messenger launch. In this example, it is set to CONVERSATION, which restricts the launch context to a single conversation view. | String |
| landingScreen | Specifies the screen shown when the messenger launches. In this example, it is set to NEW_CONVERSATION, which starts a fresh chat session. | String |
| chatInitialisationContext | A required key that contains all launch parameters for the messenger. Developers must place their configuration bundle inside this key so the application starts with the correct context. | Bundle |

## Single Conversation View with Last Conversation

When Live Chat is set to single conversation view with `LAST_CONVERSATION`, it opens the last conversation of the user that is still open.
If there are no open conversations, it initiates a new conversation on behalf of the user that starts with the welcome messages set in the application builder.


**Dev Notes: **This configuration ensures that users return to their most recent active conversation.
  If no active conversation exists, a new one is automatically started.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("scope", "CONVERSATION");
  bundle.putString("landingScreen", "LAST_CONVERSATION");
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);



### Parameters








    ``




    ``








| Parameter | Description | Type |
| --- | --- | --- |
| scope | Defines the scope of the messenger launch. In this example, it is set to CONVERSATION, which restricts the launch context to a single conversation view. | String |
| landingScreen | Specifies the screen shown when the messenger launches. In this example, it is set to LAST_CONVERSATION, which opens the most recent active conversation. If none exist, a new one is started with welcome messages. | String |
| chatInitialisationContext | Contains all launch parameters for the messenger. Developers must place their configuration bundle inside this key so the application starts with the correct context. | Bundle |

## Single Conversation View with Custom Brand/User Message

Use the following code to open a single conversation view that starts with a custom message from your brand or user.

**Dev Notes: **If a welcome message is configured in the Live Chat builder with this view, the welcome message will not be displayed. Instead, the custom brand message will be displayed.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("scope", "CONVERSATION");
  bundle.putString("landingScreen", "NEW_CONVERSATION");
Bundle brandMessage = new Bundle();
  brandMessage.putString("message", "This is a brand message");
  brandMessage.putBoolean("isSentByUser", false);
Bundle userMessage = new Bundle();
  userMessage.putString("message", "This is a user message");
  userMessage.putBoolean("isSentByUser", true);
  bundle.putParcelableArray("initialMessages", new Bundle[]{brandMessage, userMessage});
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);



### Parameters








    ``




    ``













| Parameter | Description | Type |
| --- | --- | --- |
| scope | Defines the scope of the messenger launch. In this example, it is set to CONVERSATION, which restricts the launch context to a single conversation view. | String |
| landingScreen | Specifies the screen shown when the messenger launches. In this example, it is set to NEW_CONVERSATION, which starts a fresh chat session. | String |
| initialMessages | Contains a list of predefined messages that appear when the chat starts. In this example, one brand message and one user message are included. | Bundle[] |
| chatInitialisationContext | Contains all launch parameters for the messenger. Developers must place their configuration bundle inside this key so the application starts with the correct context. | Bundle |

#### `initialMessages` Parameters








    ````





****
****



| Parameter | Description | Type |
| --- | --- | --- |
| message | The text of the predefined message. For example: "This is a brand message" or "This is a user message". | String |
| isSentByUser | Defines whether the message was sent by the user or by the brand.         true: Indicates that the message is sent by the user.         false: Indicates that the message is sent by the brand. | Boolean |

## Single Conversation View with Conversation ID

Use the following code to open a specific conversation in single conversation view. Ensure that the conversation you want to open is not deleted and has the most recently published message.

To open a specific conversation, you need its conversation ID. You can capture the conversation ID by listening to events indicating the ongoing conversation.


**Dev Notes: **This configuration is useful when you want to resume a specific conversation directly, bypassing the home screen. Make sure the conversation is active and not deleted.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("scope", "CONVERSATION");
  bundle.putString("landingScreen", "EXISTING_CONVERSATION");
Bundle params = new Bundle();
  params.putString("conversationId", "id_of_conversation");
  bundle.putBundle("params", params);
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);



### Parameters








    ``




    ``




    ``








| Parameter | Description | Type |
| --- | --- | --- |
| scope | Defines the scope of the messenger launch. In this example, it is set to CONVERSATION, which restricts the launch context to a single conversation view. | String |
| landingScreen | Specifies the screen shown when the messenger launches. In this example, it is set to EXISTING_CONVERSATION, which resumes a specific conversation by ID. | String |
| params | Holds additional parameters required by the chosen landing screen. For EXISTING_CONVERSATION, this includes the conversation identifier. | Bundle |
| chatInitialisationContext | Contains all launch parameters for the messenger. Developers must place their configuration bundle inside this key so the application starts with the correct context. | Bundle |

#### `param` Parameters












| Parameter | Description | Type |
| --- | --- | --- |
| conversationId | The unique identifier of the conversation to open when the messenger launches. Must be active and not deleted. | String |

## Single Conversation View with Video Call

Use the following code to open a new conversation and configure the messenger to initiate a video call.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("scope", "CONVERSATION");
  bundle.putString("landingScreen", "NEW_CONVERSATION");
  bundle.putStringArray("initialMessages", new String[]{});
Bundle additional = new Bundle();
  additional.putString("callType", "VIDEO");
  bundle.putBundle("additional", additional);
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);



### Parameters








    ``




    ``


















| Parameter | Description | Type |
| --- | --- | --- |
| scope | Defines the scope of the messenger launch. In this example, it is set to CONVERSATION, which restricts the launch context to a single conversation view. | String |
| landingScreen | Specifies the screen shown when the messenger launches. In this example, it is set to NEW_CONVERSATION, which starts a fresh chat session. | String |
| initialMessages | An array of messages that can be preloaded into the new conversation. In this example, the array is empty, meaning no predefined messages are loaded. | String[] |
| additional | A nested bundle that holds extra parameters for the conversation, such as call type. | Bundle |
| chatInitialisationContext | A required key that contains all launch parameters for the messenger. Developers must place their configuration bundle inside this key so the application starts with the correct context. | Bundle |

### `additional` Parameters









    ``

    ````


| Parameter | Description | Type | Possible Values |
| --- | --- | --- | --- |
| callType | Specifies the type of call to initiate within the conversation. In this example, it is set to VIDEO. | String | VIDEO, AUDIO |

## Single Conversation View with Audio Call

Use the following code to open a new conversation and configure the messenger to initiate an audio call.

### Syntax



Bundle bundle = new Bundle();
  bundle.putString("scope", "CONVERSATION");
  bundle.putString("landingScreen", "NEW_CONVERSATION");
  bundle.putStringArray("initialMessages", new String[]{});
Bundle additional = new Bundle();
  additional.putString("callType", "AUDIO");
  bundle.putBundle("additional", additional);
Bundle applicationLaunchBundle = new Bundle();
  applicationLaunchBundle.putBundle("chatInitialisationContext", bundle);
  SPRMessenger.shared().startApplication(applicationLaunchBundle);



### Parameters








    ``




    ``


















| Parameter | Description | Type |
| --- | --- | --- |
| scope | Defines the scope of the messenger launch. In this example, it is set to CONVERSATION, which restricts the launch context to a single conversation view. | String |
| landingScreen | Specifies the screen shown when the messenger launches. In this example, it is set to NEW_CONVERSATION, which starts a fresh chat session. | String |
| initialMessages | An array of messages that can be preloaded into the new conversation. In this example, the array is empty, meaning no predefined messages are loaded. | String[] |
| additional | A nested bundle that holds extra parameters for the conversation, such as call type. | Bundle |
| chatInitialisationContext | A required key that contains all launch parameters for the messenger. Developers must place their configuration bundle inside this key so the application starts with the correct context. | Bundle |

### `additional` Parameters









    ``

    ````


| Parameter | Description | Type | Possible Values |
| --- | --- | --- | --- |
| callType | Specifies the type of call to initiate within the conversation. In this example, it is set to AUDIO. | String | VIDEO, AUDIO |

## Next Steps

[Configure Live Chat Mobile SDK](https://dev.sprinklr.com/configure-lc-mobile-sdk-android)

## Additional Resources

See **All Integration Steps**

  [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-android) >
  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-android) >
  **Launch** >
  [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-android) >
  [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-android)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-android)

  [](https://dev.sprinklr.com/launch-lc-mobile-sdk-android)




[Back to top](https://dev.sprinklr.com/launch-lc-mobile-sdk-android)
