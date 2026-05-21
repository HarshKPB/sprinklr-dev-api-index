---
title: "Launch LC Mobile SDK - iOS"
slug: launch-lc-mobile-sdk-ios
url: https://dev.sprinklr.com/launch-lc-mobile-sdk-ios
---

# Launch LC Mobile SDK - iOS

# Launch Live Chat Mobile SDK - iOS


The Sprinklr Messenger can be launched and customized to fit your application’s needs. By default, the messenger opens with both the home screen and conversation view, but you can configure it to start in different modes such as a new conversation, the last active conversation, or even a specific conversation by ID.

This flexibility allows you to tailor the chat experience for your users, whether they need quick access to ongoing conversations, knowledge base articles, or predefined brand messages.

The following are the steps for integrating Sprinklr Messenger. This page covers the **third step: Launch**. Use the flow below to navigate through all steps of the integration process.

 [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-ios) >  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios) > **Launch** > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios)


**On this page:**



- [Launch Messenger](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#launch-messenger)

- [Customize Messenger View](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#customize-messenger-view)


## Launch Sprinklr Messenger

Add the following code in the onClick event of the button you want to use to launch the chat.

### Syntax

**Swift**



let viewController = SPRMessengerViewController.init(launchOptions: launchOptions);
viewController.modalPresentationStyle = .fullScreen
self.present(viewController, animated: true, completion: nil)




**Objective-C**



[[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions]
viewController.modalPresentationStyle = UIModalPresentationFullScreen;
[self presentViewController:viewController animated:YES completion:nil];




### Parameters










      ``



      ``



      ``



      ``



| Parameter | Description |
| --- | --- |
| launchOptions | Provide this parameter when the chat is opened from a notification tap so the messenger can use the notification context. For all other launch scenarios, set this parameter to nil. |
| modalPresentationStyle | Controls how the messenger view controller is presented. In this example, set to .fullScreen. |
| animated | Boolean flag that determines whether the presentation is animated. Example: true. |
| completion | Callback executed after the view controller is presented. Example: nil when no action is needed. |


**Dev Notes: **Add the launch code in the `onClick` event of the button you want to use to open the chat. Pass `launchOptions` when opening from a notification tap; otherwise, you can pass `nil`.

## Customize Live Chat Messenger View

By default, the messenger opens with a home screen displaying all conversations. You can customize this behavior to launch Messenger with either the **default view** (home + conversation screens) or a **single conversation view**.

### See the relevant section:



- [Default View](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#default-view-main)

- [Single Conversation View](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#single-conversation-main)

### Default View

The default view shows both home and conversation screens.

#### Default View Options Quick Reference









      [Default View](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#default-view)



      [Default View with New Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#default-view-new-conversation)



      [Default View with Last Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#default-view-last-conversation)



      [Default View with Knowledge Base List](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#default-view-kb-list)



      [Default View with Custom Brand/User Messages](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#default-view-custom-message)



      [Default View with Particular Conversation ID](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#default-view-conversation-id)



    [Default View with Video Call](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#default-view-video-call)



    [Default View with Audio Call](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#default-view-audio-call)




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

**Swift**



let viewController = SPRMessengerViewController.init(launchOptions: launchOptions)




**Objective-C**



SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions];





### Parameters







    ``


| Parameter | Description |
| --- | --- |
| launchOptions | Defines how the messenger should be launched. You can also use launchOptions to open the messenger in response to events like notifications. |

## Default View with New Conversation

Use the following code to open the default view with a new conversation. This configuration will initiate a new conversation
on behalf of the user that starts with the welcome messages set in the application builder. To continue any existing conversations,users must return to the home screen.


**Dev Notes: **This configuration will open a new conversation every time, irrespective of whether the previous conversation was closed or not.

### Syntax

**Swift**



let chatInitialisationContext = ["landingScreen": "NEW_CONVERSATION"]
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions, andChatInitialisationContext: chatInitialisationContext)




**Objective-C**



NSDictionary *chatInitialisationContext = @{
    @"landingScreen":@"NEW_CONVERSATION"
};
SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions andChatInitialisationContext:chatInitialisationContext];





### Parameters









    ``




    ``


| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| launchOptions |  | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to NEW_CONVERSATION to start a new conversation when the messenger is launched. |

## Default View with Last Conversation

Use the following code to open the default view with the last conversation. This configuration will open the last conversation
that is still active. If there are no open conversations, Live Chat will initiate a new conversation on behalf of the user,
starting with the welcome messages set in the application builder.


**Dev Notes: **This configuration ensures that users return to their most recent active conversation. If none exist, a new conversation is automatically started.

### Syntax

**Swift**



let chatInitialisationContext = ["landingScreen": "LAST_CONVERSATION"]
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions, andChatInitialisationContext: chatInitialisationContext)




**Objective-C**



NSDictionary *chatInitialisationContext = @{
     @"landingScreen":@"LAST_CONVERSATION"
};
SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions andChatInitialisationContext:chatInitialisationContext];





### Parameters









    ``




    ``


| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| launchOptions |  | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to LAST_CONVERSATION to open the last active conversation when the messenger is launched. |

## Default View with Knowledge Base List

Use the following code to open the Knowledge Base list view in the Sprinklr Live Chat widget.
This will launch Live Chat with the Knowledge Base list view, enabling users to browse relevant articles before starting a conversation.

### Syntax

**Swift**



let chatInitialisationContext = ["landingScreen": "KNOWLEDGE_BASE_LIST"]
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions, andChatInitialisationContext: chatInitialisationContext)




**Objective-C**



NSDictionary *chatInitialisationContext = @{
     @"landingScreen":@"KNOWLEDGE_BASE_LIST"
};
SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions andChatInitialisationContext:chatInitialisationContext];





### Parameters









    ``




    ``


| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| launchOptions |  | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to KNOWLEDGE_BASE_LIST to open the knowledge base articles list when the messenger is launched. |

## Default View with Custom Brand/User Message

Use the following code to open the default view with a new conversation that starts with custom brand/user messages. To continue any existing conversations, users must return to the home screen.

### Syntax

**Swift**



let initialMessages = [
    [
        "message": "This is a brand message",
        "isSentByUser": false
    ],
    "This is another brand message",
    [
        "message": "This is a user message",
        "isSentByUser": true
    ]
] as [Any]
let chatInitialisationContext = [
    "landingScreen": "NEW_CONVERSATION",
    "initialMessages": initialMessages
] as [String: Any]
let viewController = SPRMessengerViewController.init(
    launchOptions: launchOptions,
    andChatInitialisationContext: chatInitialisationContext
)




**Objective-C**



NSMutableArray *initialMessages = [NSMutableArray new];
NSDictionary *brandMessage = @{
    @"message": @"This is a brand message",
    @"isSentByUser": @NO
};
[initialMessages addObject:brandMessage];
NSString *anotherBrandMessage = @"This is another brand message";
[initialMessages addObject:anotherBrandMessage];
NSDictionary *userMessage = @{
    @"message": @"This is a user message",
    @"isSentByUser": @YES
};
[initialMessages addObject:userMessage];
NSDictionary *chatInitialisationContext = @{
    @"landingScreen": @"NEW_CONVERSATION",
    @"initialMessages": [initialMessages copy]
};
SPRMessengerViewController *viewController =
    [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions                               andChatInitialisationContext:chatInitialisationContext];





### Parameters









    ``




    ``







| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| launchOptions |  | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to NEW_CONVERSATION to start a new conversation when the messenger is launched. |
|  | initialMessages | Contains a list of predefined messages that appear when the chat starts. For more information, see the Initial Messages table. |

#### Initial Messages














    ````
****
****


| Parameter | Description | Possible Values |
| --- | --- | --- |
| message | The text of the message. | Any string value |
| isSentByUser | Defines whether the message was sent by the user or by the brand. | true, false         true: Indicates that the message is sent by the user.         false: Indicates that the message is sent by the brand. |

## Default View with Particular Conversation ID

Use the following code to open a specific conversation using its conversation ID. Ensure that the conversation you want to open is not deleted and has the most recently published message.

To open a specific conversation, you need its conversation ID. You can capture the conversation ID by listening to events
indicating the ongoing conversation.

### Syntax

**Swift**



let chatInitialisationContext = ["landingScreen": "EXISTING_CONVERSATION", "params": ["conversationId": "id_of_conversation"]]
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions, andChatInitialisationContext: chatInitialisationContext)




**Objective-C**



NSDictionary *chatInitialisationContext = @{
    @"scope": @"CONVERSATION", @"landingScreen":@"EXISTING_CONVERSATION", @"params":@{
      @"conversationId": @"id_of_conversation"
}};
SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions andChatInitialisationContext:chatInitialisationContext];





### Parameters









    ``




    ``







| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| launchOptions |  | Defines how the messenger is launched. You can use launchOptions to open the messenger in response to events like notifications. |
| chatInitialisationContext | landingScreen | Specifies which screen the chat opens with. In this configuration, it is set to EXISTING_CONVERSATION to open an existing conversation. |
|  | params | Contains the parameters required for initializing the chat. For more information, see the params table below. |

#### `params` Object










| Parameter | Description |
| --- | --- |
| conversationId | The unique ID of the conversation that you want to open. |

## Default View with Video Call

Use the following code to open a new conversation and configure the messenger to initiate a video call.

### Syntax

**Swift**



var initialMessages = [Any]()
let chatInitialisationContext = [
    "landingScreen": "NEW_CONVERSATION",
    "initialMessages": initialMessages,
    "additional": [
        "callType": "VIDEO"
    ]
] as [String : Any]
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions, andChatInitialisationContext: chatInitialisationContext)




**Objective-C**



NSMutableArray *initialMessages = [NSMutableArray new];
  NSDictionary *chatInitialisationContext = @{
@"landingScreen":@"NEW_CONVERSATION", @"initialMessages": [initialMessages copy], @"additional": @{
      @"callType": @"VIDEO"
    }
  };
  SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions andChatInitialisationContext:chatInitialisationContext];





### Parameters








    ``


















| Parameter | Description | Type |
| --- | --- | --- |
| landingScreen | Specifies the screen shown when the messenger launches. In this example, it is set to NEW_CONVERSATION. | String |
| initialMessages | An array of messages that can be preloaded into the new conversation. This can be empty if no messages are required. | Array |
| chatInitialisationContext | Contains all launch parameters for the messenger. Developers must place their configuration bundle inside this key so the application starts with the correct context. | Dictionary[String: Any] |
| additional | Holds extra parameters for the conversation, such as call type. | Dictionary[String: Any] |

### `additional` Parameters








    ``



| Parameter | Description | Type |
| --- | --- | --- |
| callType | Specifies the type of call to initiate within the conversation. In this example, it is set to VIDEO. | String |

## Default View with Audio Call

Use the following code to open a new conversation and configure the messenger to initiate an audio call.

### Syntax

**Swift**



var initialMessages = [Any]()
let chatInitialisationContext = [
    "landingScreen": "NEW_CONVERSATION",
    "initialMessages": initialMessages,
    "additional": [
        "callType": "AUDIO"
    ]
] as [String : Any]
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions, andChatInitialisationContext: chatInitialisationContext)




**Objective-C**



NSMutableArray *initialMessages = [NSMutableArray new];
  NSDictionary *chatInitialisationContext = @{
@"landingScreen":@"NEW_CONVERSATION", @"initialMessages": [initialMessages copy], @"additional": @{
      @"callType": @"AUDIO"
    }
  };
  SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions andChatInitialisationContext:chatInitialisationContext];





### Parameters








    ``


















| Parameter | Description | Type |
| --- | --- | --- |
| landingScreen | Specifies the screen shown when the messenger launches. In this example, it is set to NEW_CONVERSATION. | String |
| initialMessages | An array of messages that can be preloaded into the new conversation. This can be empty if no messages are required. | Array |
| chatInitialisationContext | Contains all launch parameters for the messenger. Developers must place their configuration bundle inside this key so the application starts with the correct context. | Dictionary[String: Any] |
| additional | Holds extra parameters for the conversation, such as call type. | Dictionary[String: Any] |

### `additional` Parameters








    ``



| Parameter | Description | Type |
| --- | --- | --- |
| callType | Specifies the type of call to initiate within the conversation. In this example, it is set to AUDIO. | String |

## Single Conversation View

You can choose to display only the conversation screen and hide the home screen completely.







    [Single Conversation View](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#single-conversation-view)



    [Single Conversation View with New Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#single-conversation-new)



    [Single Conversation View with Last Conversation](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#single-conversation-last)



    [Single Conversation View with Custom Brand/User Message](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#single-conversation-custom)



    [Single Conversation View with Conversation ID](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#single-conversation-id)



    [Single Conversation View with Video Call](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#single-conversation-video-call)



    [Single Conversation View with Audio Call](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios#single-conversation-audio-call)



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

**Swift**



let chatInitialisationContext = ["scope": "CONVERSATION"]
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions, andChatInitialisationContext: chatInitialisationContext)




**Objective-C**



NSDictionary *chatInitialisationContext = @{
    @"scope": @"CONVERSATION"
};
SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions andChatInitialisationContext:chatInitialisationContext];





### Parameters










    ``











    ``



| Parameter | Sub-parameter | Description | Type |
| --- | --- | --- | --- |
| launchOptions |  | Top-level parameter passed into the initializer. Defines how the messenger should be launched.        Use when opening from a notification tap; otherwise set to nil. | Dictionary[String: Any] or nil |
| chatInitialisationContext |  | Dictionary containing configuration for the messenger. Developers place their configuration here so the messenger starts with the correct context. | Dictionary[String: Any] |
|  | scope | Defines the scope of the messenger launch. Example: CONVERSATION restricts the view to a single conversation screen. | String |

## Single Conversation View with New Conversation

When Live Chat is set to a single conversation view with `NEW_CONVERSATION`, it initiates a new conversation on behalf of the user.
This conversation starts with the welcome messages set in the Live Chat application builder.

This configuration will always open a conversation view by initiating a new conversation and will not show any previous conversations that are currently open.


**Dev Notes: **Use this configuration when you want the messenger to operate strictly in single conversation mode,
  ensuring that only new conversations are initiated and no previous conversations are displayed.

### Syntax

**Swift**



let chatInitialisationContext = ["scope": "CONVERSATION", "landingScreen": "NEW_CONVERSATION"]
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions, andChatInitialisationContext: chatInitialisationContext)




**Objective-C**



NSDictionary *chatInitialisationContext = @{
    @"scope": @"CONVERSATION", @"landingScreen":@"NEW_CONVERSATION"
};
SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions andChatInitialisationContext:chatInitialisationContext];





### Parameters










    ``











    ``



| Parameter | Sub-parameter | Description | Type |
| --- | --- | --- | --- |
| launchOptions |  | Top-level parameter passed into the initializer. Defines how the messenger should be launched.        Use when opening from a notification tap; otherwise set to nil. | Dictionary[String: Any] or nil |
| chatInitialisationContext |  | Dictionary containing configuration for the messenger. Developers place their configuration here so the messenger starts with the correct context. | Dictionary[String: Any] |
|  | scope | Defines the scope of the messenger launch. Example: CONVERSATION restricts the view to a single conversation screen. | String |

## Single Conversation View with Last Conversation

When Live Chat is set to single conversation view with `LAST_CONVERSATION`, it opens the last conversation of the user that is still open.
If there are no open conversations, it initiates a new conversation on behalf of the user that starts with the welcome messages set in the application builder.


**Dev Notes: **This configuration ensures that users return to their most recent active conversation.
  If no active conversation exists, a new one is automatically started.

### Syntax

**Swift**



let chatInitialisationContext = ["scope": "CONVERSATION", "landingScreen": "LAST_CONVERSATION"]​
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions, andChatInitialisationContext: chatInitialisationContext)




**Objective-C**



NSDictionary *chatInitialisationContext = @{
    @"scope": @"CONVERSATION", @"landingScreen":@"LAST_CONVERSATION"
};
SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions andChatInitialisationContext:chatInitialisationContext];





### Parameters










    ``











    ``





    ``



| Parameter | Sub-parameter | Description | Type |
| --- | --- | --- | --- |
| launchOptions |  | Top-level parameter passed into the initializer. Defines how the messenger should be launched.        Use when opening from a notification tap; otherwise set to nil. | Dictionary[String: Any] or nil |
| chatInitialisationContext |  | Dictionary containing configuration for the messenger. Developers place their configuration here so the messenger starts with the correct context. | Dictionary[String: Any] |
|  | scope | Defines the scope of the messenger launch. Example: CONVERSATION restricts the view to a single conversation screen. | String |
|  | landingScreen | Specifies the starting screen when the messenger launches. Example: LAST_CONVERSATION. | String |

## Single Conversation View with Custom Brand Message

Use the following code to open a single conversation view that starts with a custom message from your brand or user.

**Dev Notes: **If a welcome message is configured in the Live Chat builder with this view, the welcome message will not be displayed. Instead, the custom brand message will be displayed.

### Syntax

**Swift**



let initialMessages = [
    [
        "message": "This is a brand message",
        "isSentByUser": false
    ],
    "This is another brand message",
    [
        "message": "This is a user message",
        "isSentByUser": true
    ]
] as [Any]
let chatInitialisationContext = [
    "scope": "CONVERSATION",
    "landingScreen": "NEW_CONVERSATION",
    "initialMessages": initialMessages
] as [String: Any]
let viewController = SPRMessengerViewController.init(
    launchOptions: launchOptions,
    andChatInitialisationContext: chatInitialisationContext
)




**Objective-C**



NSMutableArray *initialMessages = [NSMutableArray new];
NSDictionary *brandMessage = @{
    @"message": @"This is a brand message",
    @"isSentByUser": @NO
};
[initialMessages addObject:brandMessage];
NSString *anotherBrandMessage = @"This is another brand message";
[initialMessages addObject:anotherBrandMessage];
NSDictionary *userMessage = @{
    @"message": @"This is a user message",
    @"isSentByUser": @YES
};
[initialMessages addObject:userMessage];
NSDictionary *chatInitialisationContext = @{
    @"scope": @"CONVERSATION",
    @"landingScreen": @"NEW_CONVERSATION",
    @"initialMessages": [initialMessages copy]
};
SPRMessengerViewController *viewController =
    [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions                                 andChatInitialisationContext:chatInitialisationContext];





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

**Swift**



let chatInitialisationContext = ["scope": "CONVERSATION", "landingScreen": "EXISTING_CONVERSATION", "params": ["conversationId": "id_of_conversation"]]
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions, andChatInitialisationContext: chatInitialisationContext)




**Objective-C**



NSDictionary *chatInitialisationContext = @{
    @"scope": @"CONVERSATION", @"landingScreen":@"EXISTING_CONVERSATION", @"params":@{
      @"conversationId": @"id_of_conversation"
}};
SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions andChatInitialisationContext:chatInitialisationContext];





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

#### `params` Parameters












| Parameter | Description | Type |
| --- | --- | --- |
| conversationId | The unique identifier of the conversation to open when the messenger launches. Must be active and not deleted. | String |

## Single Conversation View with Video Call

Use the following code to open a new conversation and configure the messenger to initiate a video call.

### Syntax

**Swift**



var initialMessages = [Any]()
let chatInitialisationContext = [
    "scope": "CONVERSATION",
    "landingScreen": "NEW_CONVERSATION",
    "initialMessages": initialMessages,
    "additional": [
        "callType": "VIDEO"
    ]
] as [String : Any]
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions, andChatInitialisationContext: chatInitialisationContext)




**Objective-C**



NSMutableArray *initialMessages = [NSMutableArray new];
  NSDictionary *chatInitialisationContext = @{
    @"scope": @"CONVERSATION", @"landingScreen":@"NEW_CONVERSATION", @"initialMessages": [initialMessages copy], @"additional": @{
      @"callType": @"VIDEO"
    }
  };
SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions andChatInitialisationContext:chatInitialisationContext];




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

**Swift**



var initialMessages = [Any]()
let chatInitialisationContext = [
    "scope": "CONVERSATION",
    "landingScreen": "NEW_CONVERSATION",
    "initialMessages": initialMessages,
    "additional": [
        "callType": "AUDIO"
    ]
] as [String : Any]
let viewController = SPRMessengerViewController.init(launchOptions: launchOptions, andChatInitialisationContext: chatInitialisationContext)




**Objective-C**



NSMutableArray *initialMessages = [NSMutableArray new];
  NSDictionary *chatInitialisationContext = @{
    @"scope": @"CONVERSATION", @"landingScreen":@"NEW_CONVERSATION", @"initialMessages": [initialMessages copy], @"additional": @{
      @"callType": @"AUDIO"
    }
  };
  SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions andChatInitialisationContext:chatInitialisationContext];




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

[Configure Live Chat Mobile SDK](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios)

## Additional Resources

See **All Integration Steps**
 [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-ios) >  [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-ios)

  [](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios)




[Back to top](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios)
