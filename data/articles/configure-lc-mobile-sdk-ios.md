---
title: "Configure LC Mobile SDK - iOS"
slug: configure-lc-mobile-sdk-ios
url: https://dev.sprinklr.com/configure-lc-mobile-sdk-ios
---

# Configure LC Mobile SDK - iOS

# Configure Live Chat Mobile SDK - iOS


The Sprinklr Live Chat Messenger provides a set of methods that allow you to customize and control the chat experience beyond its initial launch. These configuration options enable you to update user details, manage conversation and profile contexts, adjust interface behavior, and integrate with analytics or external events.

By using these methods, you can tailor Live Chat to align with your brand’s requirements, deliver contextual interactions, and ensure a seamless experience for your users.

The following are the steps for integrating Sprinklr Messenger. This page covers the **fifth step: Configure**. Use the flow below to navigate through all steps of the integration process.

 [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-ios) > [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios) > **Configure** > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios)

### SDK Methods Quick Reference









      [Update User](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#update-user)



      [Update Custom User](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#update-custom-user)



      [Update Locale](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#update-locale)



      [Capture Context in New Conversation (Custom View)](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#capture-customer-context-custom-view)



      [Capture Customer Context on All Cases](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#capture-context-all-cases)



      [Update Conversation Context on Demand](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#update-conversation-context)



      [Update Profile Context](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#update-profile-context)



      [Get Number of Open Conversations](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#get-open-conversations)



      [Get Number of Unread Messages](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#get-unread-messages)



      [Update Theme Mode](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#update-theme-mode)



      [Configure Status Card](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#configure-status-card)



      [Disable Attachments](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#disable-attachments)



      [Integrate Custom Header](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#integrate-custom-header)



      [Implement Back Button Handling](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#back-button)



      [Close Conversation](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#close-conversation)



      [Close All Conversations](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#close-all-conversations)



      [Delete Conversation](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#delete-conversation)



      [Delete All Conversations](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#delete-all-conversations)



      [Clear User Session](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#clear-session)



      [Use Custom Font](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#custom-font)



      [Enabling Sentry for Crash Monitoring](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#sentry-crash-monitoring)



      [Configure Keyboard Send/Enter Button Behavior](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios#keyboard-behavior)




| Method / Section | Purpose |
| --- | --- |
|  | Authenticate and update user details |
|  | Authenticate and update details of a custom user |
|  | Change the language/locale of Live Chat |
|  | Pass contextual information when opening a new conversation |
|  | Pass or update client context for all cases |
|  | Update case custom fields for an active conversation |
|  | Update profile-level custom fields |
|  | Fetch the number of open conversations |
|  | Fetch the number of unread messages |
|  | Switch between default and dark theme |
|  | Update status card in Live Chat |
|  | Enable or disable file attachments in chat |
|  | Customize chat UI header and full view |
|  | Handle hardware back button navigation |
|  | Close an active conversation |
|  | Close all open conversations |
|  | Permanently delete an active conversation |
|  | Delete all conversations in Live Chat |
|  | Clear user session and reset context |
|  | Apply custom fonts for branding consistency |
|  | Enable Sentry integration to monitor crash logs |
|  | Control how the Send/Enter key behaves in chat |

## Update User

Use the `updateUser` method to authenticate the user and update their details such as user ID, first name, last name, and more.

### Syntax

**Swift**



let user = SPRMessengerUser();
user.id = "12345";
user.firstName = "John";
user.lastName = "Doe";
user.phoneNo = "9876543210";
user.email = "John.Doe@example.com";
user.profileImageUrl = "https://example.com/profilePic.jpg";
user.hashValue = "fa91cafc6522662a70ad521ae050acce996190aa38b72ac66b48c68d4666ba38";
user.hashCreationTime = 1734156789; // should be the same one that is used for generating the hash
SPRMessenger.shared().updateUser(user)




**Objective‑C**



let user = SPRMessengerUser();
user.id = "12345";
user.firstName = "John";
user.lastName = "Doe";
user.phoneNo = "9876543210";
user.email = "John.Doe@example.com";
user.profileImageUrl = "https://example.com/profilePic.jpg";
user.hashValue = "fa91cafc6522662a70ad521ae050acce996190aa38b72ac66b48c68d4666ba38";
user.hashCreationTime = 1734156789; // should be the same one that is used for generating the hash
SPRMessenger.shared().updateUser(user)




### Parameters










































**





**




| Parameter | Description | Required/Optional |
| --- | --- | --- |
| id | Unique identifier of the user. | Required |
| firstName | First name of the user. | Optional |
| lastName | Last name of the user. | Optional |
| phoneNo | Phone number of the user. | Optional |
| email | Email ID of the user. | Optional |
| profileImageUrl | URL to the profile image of the user. | Optional |
| hash | Hash should be generated for every change in user object.         For the steps to generate hash, see How to Generate User Hash? | Required |
| hashCreationTime | Hash Creation Time should be the same one that is used for generating the hash.         For the steps to generate hash, see How to Generate User Hash? | Required |

## Update Custom User

Use the `updateCustomUser` method to authenticate the user and update details of a custom user.


**Note:** If you want to implement a custom user authentication flow, contact the Sprinklr Support team at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

### Syntax

**Swift**



let customUser = ["customAttribute1": "value1", "customAttribute2": "value2", "hash": "8cf5a3815eedc5305b53f2cb8c1785d46a94abe39cfb15bd26d1e1f75e66056a", "hashCreationTime": 1734156789] // hashCreationTime should be the same one that is used for generating the hash
SPRMessenger.shared().updateCustomUser(customUser) 




**Objective-C**



NSDictionary *customUser = @{@"customAttribute1": @"value1", @"customAttribute2": @"value2", @"hash": @"8cf5a3815eedc5305b53f2cb8c1785d46a94abe39cfb15bd26d1e1f75e66056a", @"hashCreationTime": @(1734156789)} // hashCreationTime should be the same one that is used for generating the hash
[[SPRMessenger shared] updateCustomUser:customUser];




### Parameters














[How to Generate User Hash](https://dev.sprinklr.com/)





[How to Generate User Hash](https://dev.sprinklr.com/)



| Parameter | Description | Required/Optional |
| --- | --- | --- |
| Custom Attribute | This is a custom attribute that could be defined by you. You can define multiple custom attributes. | Required |
| hash | A new hash should be generated whenever the user object is modified.       For the steps to generate hash, see . | Required |
| hashCreationTime | Hash Creation Time should be the same one that is used for generating the hash.       For the steps to generate hash, see . | Required |

## Update Locale

Use the `updateLocale` method to update the language in which Live Chat will be displayed.

### Syntax

**Swift**



SPRMessenger.shared().updateLocale(locale)




**Objective‑C**



[[SPRMessenger shared] updateLocale:locale];




### Parameters















| Parameter | Type | Description | Required/Optional |
| --- | --- | --- | --- |
| locale | String | A locale identifier that sets the messenger’s language and regional formatting.        Examples: en-GB (English, United Kingdom), fr-CA (French, Canada)       See Supported Languages. | Required |

 **Dev Notes:**  **Handling Language Direction Change**

  When a user updates the locale, the language direction might change for certain languages. For example, changing from English to Arabic switches the direction from left-to-right to right-to-left.

-  **If Live Chat is open:** An alert notifies the user that the language direction has been updated. After clicking **OK**, they are redirected to the brand app and must reopen the Live Chat app.
-  **If Live Chat is not running in the foreground (brand app is open):** No alert is shown, and the update is applied automatically.

## Capture Context in New Conversation (Custom View)

When a user opens Live Chat with a custom view, you might want to capture additional context on the conversation or case.

For example, consider a button called *Know More about this laptop* next to a laptop product.
When this button is clicked, you want to open a chat with a predefined contextual welcome message:
**Hi there! It looks like you are interested in buying a laptop.**
You also want to set the case custom fields `product category: laptop` and `case type: inquiry`.

### Steps


- Create case custom fields. For steps to create a custom field, see [Add a Custom Field](https://www.sprinklr.com/help/articles/custom-fields/add-a-custom-field/6452201b0d27fc559bbe4707).

- Copy the field names of the custom fields you created from the Sprinklr UI.

-
    Pass the `conversationContext` object with these custom fields to
    `chatInitialisationContext` when a new conversation is opened directly.


Example field names: `5ea7fa9e87651f356209878f` and `5eb7fa9e87651f356219348e`.

### Syntax

**Swift**



let conversationContext = ["5ea7fa9e87651f356209878f": ["laptop"], "5eb7fa9e87651f356219348e": ["inquiry"]];
let chatInitialisationContext = ["conversationContext": conversationContext] as [String : Any]




**Objective‑C**



NSDictionary *conversationContext = @{
    @"5ea7fa9e87651f356209878f": @[@"laptop"],
    @"5eb7fa9e87651f356219348e": @[@"inquiry"]
};
NSDictionary *chatInitialisationContext = @{ 
    @"conversationContext": conversationContext 
};




### Parameters













| Parameter | Description | Required/Optional |
| --- | --- | --- |
| conversationContext | Object containing the key-value pairs of custom field names and their values.       You can copy the custom field from the Sprinklr UI. | Required |

## Capture Customer Context on All Cases of the User

When a user starts a new conversation, you might want to pass some contextual information in case custom fields.

### Steps


- Create case custom fields. For steps to create a custom field, see [Add a Custom Field](https://www.sprinklr.com/help/articles/custom-fields/add-a-custom-field/6452201b0d27fc559bbe4707).

- Copy the field names of the custom fields you created from the Sprinklr UI.

- Pass or update context. You can pass context in two ways:

### Pass Context When the Chat Is Initiated

You can pass these values in `clientContext` in the `takeOff` method. In this example, the custom field name is `5e281d040844e435b`.

### Syntax

**Swift**



let clientContext = ["5ea7fa9e87651f356209878f": ["laptop"], "5eb7fa9e87651f356219348e": ["inquiry"]];
config.clientContext = clientContext




**Objective‑C**



NSDictionary *clientContext = @{
     @"5ea7fa9e87651f356209878f": @[@"laptop"],
     @"5eb7fa9e87651f356219348e": @[@"inquiry"]
};
config.clientContext = clientContext;




### Update Context at Runtime

You can update the client context in runtime by calling the following method:

### Syntax

**Swift**



let clientContext = ["5ea7fa9e87651f356209878f": ["laptop"], "5eb7fa9e87651f356219348e": ["inquiry"]];
SPRMessenger.shared().updateClientContext(clientContext)




**Objective‑C**



NSDictionary *clientContext = @{
     @"5ea7fa9e87651f356209878f": @[@"laptop"],
     @"5eb7fa9e87651f356219348e": @[@"inquiry"]
};
[[SPRMessenger shared] updateClientContext:clientContext];




### Parameters













| Parameter | Description | Required/Optional |
| --- | --- | --- |
| Custom Field Name with its values | Object containing the key-value pairs of custom field names and their values.       You can copy the custom field from the Sprinklr UI. | Required |

## Update Conversation Context on Demand

You might want to update case custom fields for an active conversation. For example, after a customer completes a purchase on the website, you can add the transaction amount or ID to the case for reporting purposes. This allows you to attribute sales to specific conversations or cases.

### Steps


- Create case custom fields. For steps to create a custom field, see [Add a Custom Field](https://www.sprinklr.com/help/articles/custom-fields/add-a-custom-field/6452201b0d27fc559bbe4707).

- Copy the field names of the custom fields you created from the Sprinklr UI.

- Update the conversation context using one of the following approaches.

### Based on Latest and Active Case

If you want to update the custom fields for the latest and active case, use the following code:

### Syntax

**Swift**



let conversationContext = ["context": ["5ea7fa9e87651f356209878f": ["laptop"],"5eb7fa9e87651f356219348e": ["inquiry"]]];
SPRMessenger.shared().updateConversationContext(conversationContext)




**Objective‑C**



NSDictionary *conversationContext = @{
    @"context": @{
      @"5ea7fa9e87651f356209878f": @[@"laptop"],
      @"5eb7fa9e87651f356219348e": @[@"inquiry"]
    }
  };
  [[SPRMessenger shared] updateConversationContext:conversationContext];




### Parameters








    ````````



| Parameter | Description | Required/Optional |
| --- | --- | --- |
| Custom Field ID and values | The unique identifier of the case custom field created in Sprinklr (e.g., 5ea7fa9e87651f356209878f).        Developers define a context object (e.g., conversationContext) that contains key‑value pairs,        where each custom field ID is the key and its associated values are provided as an array of strings (e.g., ["laptop"], ["inquiry"]). | Required |

## Update Profile Context

When opening a chat from a custom button or hyperlink, you may want to capture relevant context about the user or profile for an active conversation.

### Steps


- Create case custom fields. For steps to create a custom field, see [Add a Custom Field](https://www.sprinklr.com/help/articles/custom-fields/add-a-custom-field/6452201b0d27fc559bbe4707).

- Copy the field names of the custom fields you created from the Sprinklr UI.

-
    Whenever you want to update the profile custom field, call the following JavaScript function and
    pass the information for profile-level custom fields. This can be done via SDK for updating on demand.


### Syntax

**Swift**



let userContext = ["5ea7fa9e87651f356209878f":
 ["laptop"],"5eb7fa9e87651f356219348e": ["inquiry"]];
SPRMessenger.shared().updateUserContext(userContext)




**Objective‑C**



NSDictionary *userContext = @{
    @"5ea7fa9e87651f356209878f":
 @[@"laptop"],
    @"5eb7fa9e87651f356219348e":
 @[@"inquiry"]
};
[[SPRMessenger shared] updateUserContext:userContext];




### Parameters








    ``````



| Parameter | Description | Required/Optional |
| --- | --- | --- |
| Custom Field ID and values | The unique identifier of the case custom field created in Sprinklr (e.g., 5ea7fa9e87651f356209878f).        Developers define a context object (e.g., userContext, conversationContext) that contains key‑value pairs,        where each custom field ID is the key and its associated values are provided as an array of strings. | Required |

## Get Number of Open Conversations

You might want to get the number of open conversations. This information can be used to hide the Live Chat widget based on the number of open conversations, preventing customers from starting more conversations unnecessarily.

To get the number of open conversations, follow these steps:

- Call the the below function to get the number of open conversations.

**Syntax**

**Swift**



SPRMessenger.shared().getNumberOfOpenConversations() 


**Objective‑C**



[[SPRMessenger shared] getNumberOfOpenConversations]; 




- Add Delegate to listen to the output of above function.

**Syntax**

**Swift**


  -
    Add messenger delegate where you have defined your `takeOff` method:





class ClassName: SPRMessengerDelegate








  -
    Inside the initialisation function of the class add after `takeOff`:





let sprMessenger = SPRMessenger.shared()
sprMessenger.delegate = self








  -
    Add function to listen to external events payload:





func onUpdateNumberOfOpenConversations(_ count: NSNumber) {}









**Objective‑C**



  -
    At top of the class, add:




          @interface ClassName ()
@end







  -
    Inside the initialisation function of the class, add the following after `takeOff`:




          SPRMessenger* sprMessenger = [SPRMessenger shared];
sprMessenger.delegate = self;








  -
    Add function to listen to external events payload:




          - (void) onUpdateNumberOfOpenConversations:(NSNumber*) count {} 









## Get Number of Unread Messages

You might want to be notified whenever there’s a change in the unread message count. This helps track the number of unread messages in real-time.

**Dev Notes: **If the app is killed (meaning the user has completely closed the app and it is no longer running on their mobile device), you cannot fetch the number of unread messages. If you want the unread message count to appear in the push notification payload, reach out to Sprinklr Support at
[tickets@sprinklr.com](mailto:tickets@sprinklr.com)

To get the number of unread message, follow these steps:


-
    Add Delegate to listen to the updates in unread messages count.

**Swift**



  - Add messenger delegate where you have defined the `takeOff` method.




          class ClassName: SPRMessengerDelegate




  - Inside the initialisation function of the class, add the following after the `takeOff` method.




          let sprMessenger = SPRMessenger.shared()
sprMessenger.delegate = self




  - Add function to listen unread messages count update payload.




          func onUpdateUnreadMessagesCount(_ response: SPRMessengerUnreadMessagesCountResponse) {
    let success = response.success
    if success {
        let unreadMessagesCount = response.unreadMessagesCount
        // Add your logic here
    } else {
        if let error = response.error {
            let errorMessage = error.localizedDescription
            // Add your logic here
        }
    }
}





**Objective-C**



  - At top of the class, add the following.



          @interface ClassName ()
 @end



  -
  Inside the class’s initialization function, add the following code after calling the `takeOff` method.




SPRMessenger* sprMessenger = [SPRMessenger shared];
sprMessenger.delegate = self;








  - Add function to listen to external events payload.




          - (void)onUpdateUnreadMessagesCount:(nonnull SPRMessengerUnreadMessagesCountResponse *)response {
    BOOL success = response.success;
    if (success) {
        NSInteger unreadMessagesCount = response.unreadMessagesCount;
        // Add your logic here
    } else {
        NSError *error = response.error;
        NSString *errorMessage = [error localizedDescription];
        // Add your logic here
    }
}






-
    You can also trigger the event to get the current unread messages count by calling the following method:


**Swift**




          SPRMessenger.shared().getUnreadMessagesCount ()




**Objective‑C**




          [[SPRMessenger shared] getUnreadMessagesCount];





**Dev Notes: **You will receive the current unread messages count response in the onUpdateUnreadMessagesCount method of the delegate you attached earlier.

## Add Delegate to Listen to External Events from Messenger

You can register a delegate to listen for external events emitted by the Live Chat SDK. These events act as a bridge between the chat interface and your mobile app, enabling your app to perform specific actions in response.
This functionality allows for tighter integration between chat and app experiences, helping brands deliver contextual interactions, streamline user flows, and drive deeper user engagement.

### Common Use Cases


-
    **App Deeplinking:** Trigger in-app navigation based on deep link instructions received via chat.
    For example, direct users to a payment screen when an agent shares a prompt.


-
    **Custom Brand Workflows:** Configure external events within Sprinklr (for example, `CUSTOM_REDIRECT`, `SHOW_PROMO_BANNER`).
    This allows your mobile app to listen for these events and respond with tailored actions such as redirecting to a specific feature, displaying a modal, or logging analytics events.


### Syntax

**Swift**

- Add messenger delegate where you have defined the `takeOff` method:



          class ClassName: SPRMessengerDelegate



- Inside the initialization function of the class, add the following after the `takeOff` method:



          let sprMessenger = SPRMessenger.shared() 
sprMessenger.analyticsHandler= self 



- Add function to listen to external events payload:



          func handleExternalAction(_ payload: [AnyHashable : Any]) {}



**Objective‑C**

- At top of the class, add the following:



          @interface ClassName ()  
@end 



- Inside the initialization function of the class, add the following after the `takeOff` method:



          SPRMessenger* sprMessenger = [SPRMessenger shared]; 
sprMessenger.analyticsHandler = self; 



- Add function to listen to external events payload:



          - (void)trackEvent:(nonnull NSString *)eventType withPayload:(nonnull NSString *)payload {} 
- (void)trackScreen:(nonnull NSString *)screenName {} 



## Add Messenger Analytics Handler to Track Events & Screens

You can register a Messenger Analytics handler to connect your analytics system with the Live Chat SDK.
This handler tracks user interactions and screen transitions within the chat interface.

Using this handler, brands can capture real-time insights such as screen views, conversation lifecycle events, call actions, and button clicks.
These insights can then be forwarded to platforms like Firebase, Adobe Analytics, or internal dashboards.

By listening to both `trackEvent` and `trackScreen` callbacks, brands gain visibility into how users interact with the Live Chat experience
and can measure engagement, optimize flows, or trigger follow-up actions based on in-app events.

**Swift**

- Add the analytics handler in the same class where you have defined the `takeOff` method:



          class ClassName: SPRMessengerAnalyticsHandler 



- Within the class’s initialization function, add the following code after the `takeOff` method:



          let sprMessenger = SPRMessenger.shared() 
sprMessenger.analyticsHandler= self



- Add below functions to listen to track event and screen:



          func trackEvent(_ eventType: String, withPayload payload: String) {} 
func trackScreen(_ screenName: String) 



**Objective‑C**

- At the top of the class, add the following declaration:



          @interface ClassName ()  
@end 



- Within the class’s initialization function, add the following code after the `takeOff` method:



          SPRMessenger* sprMessenger = [SPRMessenger shared]; 
sprMessenger.analyticsHandler = self; 



- Add below functions to listen to track event and screen:



          - (void)trackEvent:(nonnull NSString *)eventType withPayload:(nonnull NSString *)payload {} 
- (void)trackScreen:(nonnull NSString *)screenName {} 



## Update Theme Mode for User on Demand

You can update the theme mode on demand using the `updateThemeMode` method.

### Syntax

**Swift**



          SPRMessenger.shared().updateThemeMode("DARK") // options: DEFAULT | DARK



**Objective‑C**



          [[SPRMessenger  shared] updateThemeMode:(@"DARK")]; // options: DEFAULT | DARK




**Dev Notes:**


**Handle Theme Mode Change**



-
      When a user switches between the default and dark theme while Live Chat is open,
      an alert will notify the user that the theme has been changed. After clicking **OK**,
      they are redirected to the brand app and must reopen the Live Chat app.


-
      **If Live Chat is not running in the foreground (brand app is open):**
      No alert is shown, and the update is applied automatically.



### Parameters











      ``

****
``
``





| Parameter | Description | Required/Optional | Type |
| --- | --- | --- | --- |
| themeMode | Specifies the theme mode to apply.         Supported Values:         DEFAULT: Applies the default theme (typically light mode).         DARK: Enables the dark mode interface for Messenger. | Required | String |

## Configure Status Card

Status cards are used to indicate the health of a key resource to your customers.
The key resource can be a tool or service that they interact with frequently.

By showing the status of this resource upfront, customers can stay informed without repeatedly contacting support.
This enhances the customer experience while reducing agent workload.


**Note:** To enable this capability, contact our support team at
  [tickets@sprinklr.com](mailto:tickets@sprinklr.com) and provide your Live Chat application ID.
  Status cards are available only for the modern skin version of the Live Chat widget.

### Syntax

**Swift**

Once the status card feature is enabled for your Live Chat widget, you can update the status card by using the following code:



          let details = SPRMessengerWidgetDetailsConfig()
details.title = "Your title, %%[status]"
details.desc = "Your description, %%[updatedAt]"
details.updatedAt = Int(Date().timeIntervalSince1970 * 1000)
details.status = SPRStatus.ALL_SYSTEMS_OPERATIONAL
SPRMessenger.shared().updateWidget("WIDGET_ID", withDetails: details)
// The same ID configured in the Live Chat builder must also be used here



**Objective‑C**

Once the status card feature is enabled for your Live Chat widget, you can update the status card by using the following code:



          SPRMessengerWidgetDetailsConfig *widgetDetails = [[SPRMessengerWidgetDetailsConfig alloc] init];
widgetDetails.title = @"Your title, %%[status]";
widgetDetails.desc = @"Your description, %%[updatedAt]";
widgetDetails.status = SPR_MAJOR_SYSTEM_OUTAGE;
widgetDetails.updatedAt = [[NSDate date] timeIntervalSince1970] * 1000;
[[SPRMessenger shared] updateWidget:@"WIDGET_ID" withDetails:widgetDetails];
// The same ID configured in the Live Chat builder must also be used here



### Parameters

















      ****



| Parameter | Required/Optional | Description |
| --- | --- | --- |
| id | Required | The widget ID, which must match the ID configured in the Live Chat builder. |
| details | Required | An object containing metadata about the status card displayed in the Live Chat widget.          It allows customization of the widget’s title, description, status, and last updated timestamp.          For more information, see the Details Object Parameters table below. |

### Details Object Parameters






















      ``




      ``



| Parameter | Required/Optional | Description |
| --- | --- | --- |
| title | Required | The title displayed on the status card. |
| description | Required | A brief description of the status update. |
| status | Required | Indicates the current state of the resource.          You can use the %%[status] placeholder for status.          For supported statuses, see the Supported Status table. |
| updatedAt | Required | Timestamp of the last status update.          You can use the %%[updatedAt] placeholder to show when the status was last updated. |

## Disable Attachments for Customers

By default, users can attach files in chat. You can disable attachments in the chat widget to prevent customers from adding files such as images, videos, or documents. To do this, hide the attachment icon by passing
`disableAttachment: true` to the `takeOff()` method.

### Syntax

**Swift**



          config.disableAttachment = true  // by default, attachments are enabled



**Objective‑C**



          config.disableAttachment = true  // by default, attachments are enabled



### Parameters












      ````
``



| Parameter | Description | Values |
| --- | --- | --- |
| disableAttachment | Enables or disables the attachment feature in Live Chat. | true \| false         Default value: false |

## Integrate Your Brand's Custom Header in Live Chat

Instead of using Sprinklr’s default chat header, you can replace it with a custom header that aligns with your brand identity. This will help create a consistent and seamless experience for your customers.

### Syntax

**Swift**



          let chatInitialisationContext = [
    "disableHeader": false, // Default: false. To disable Sprinklr's header, set to true
    "isRenderedAsFullView": true // Default: true. If set to false, the brand must manage device top insets
]
let viewController = SPRMessengerViewController.init(
    launchOptions: launchOptions,
    andChatInitialisationContext: chatInitialisationContext
)



**Objective‑C**



          NSDictionary *chatInitialisationContext = @{
    @"disableHeader": @NO, // Default: NO. To disable Sprinklr's header, set to YES
    @"isRenderedAsFullView": @YES // Default: YES. If set to NO, the brand must manage device top insets
};
SPRMessengerViewController *viewController = [[SPRMessengerViewController alloc] initWithLaunchOptions:launchOptions                                                                         andChatInitialisationContext:chatInitialisationContext];



### Parameters












****````
``
``





****````
``
``




| Parameter | Description | Required/Optional |
| --- | --- | --- |
| disableHeader | Enables or disables the Sprinklr default header.         Supported Values: true, false         true: Hides the Sprinklr default header.         false: Shows the Sprinklr default header. | Optional |
| isRenderedAsFullView | Indicates whether Live Chat is displayed in the full screen.         Supported Values: true, false         true: Chat takes up the full screen.         false: Layout must be handled by the app. | Optional |

## Implement Back Button Handling to Control Hardware Back Button

You can use the `MessengerClient.goBack()` function to manage the hardware back button behavior in your Live Chat application.
This allows users to seamlessly navigate back to the previous screen when they press the back button on their device,
enhancing the overall user experience with intuitive and efficient navigation.

### Syntax

**Swift**



          SPRMessenger.shared().goBack() // Handles the back action 



**Objective‑C**



          [[SPRMessenger shared] goBack]; // Handles the back action 



### Close Conversation

Use `closeConversation()` to close an active conversation in Live Chat.
This helps brands manage conversation endings efficiently, ensuring control over when and how interactions end.
Apply this method only on the conversation screen when the case is open.

### Syntax

**Swift**



          SPRMessenger.shared().closeConversation() 



**Objective‑C**



          [[SPRMessenger shared] closeConversation]; 



### Close All Conversations

Use `closeAllConversations()` to close all conversations in Live Chat at once.
This option is visible only to users with open cases. If there are no open cases or if all existing cases are already closed,
this option will not be available.

### Syntax

**Swift**



          SPRMessenger.shared().closeAllConversations() 



**Objective‑C**



          [[SPRMessenger shared] closeAllConversations]; 



### Delete Conversation

Use `MessengerClient.deleteConversation()` to permanently delete a conversation in Live Chat.
This feature gives brands control over removing interactions when necessary.
Apply this method only on the conversation screen.

### Syntax

**Swift**



          SPRMessenger.shared().deleteConversation()  



**Objective‑C**



          [[SPRMessenger shared] deleteConversation];  



### Delete All Conversations

Use `MessengerClient.deleteAllConversations()` to delete all conversations in Live Chat.
This feature allows brands to efficiently remove interactions as needed.
Apply this method only on the home screen to manage deletions effectively.

### Syntax

**Swift**



          SPRMessenger.shared().deleteAllConversations()  



**Objective‑C**



          [[SPRMessenger shared] deleteAllConversations];  



### Clear User Session

Use `MessengerClient.clearSession()` to enable users to clear their session details.
Once a user clears their session, any new conversation is treated as if it’s from a new user.
This method is particularly useful for users interacting with your brand in public spaces or over a public network.

### Syntax

**Swift**



          SPRMessenger.shared().clearSession()  



**Objective‑C**



          [[SPRMessenger shared] clearSession];  



## Use a Custom Font

You can use a custom font in your Live Chat app to ensure consistent branding across your applications.

To use a custom font in Live Chat, follow these steps:


-
    Link your custom font files in your iOS and Android projects natively, such that the fonts are available throughout the project.
    For steps, see iOS and Android documentation.


-
    Open a Sprinklr support ticket at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).
    In the support ticket, mention the font file names and the supported font weights for the texts.
    Refer to the following table for the supported font weights.



**Dev Notes: ** Ensure you provide at least one of the supported font weights in the support ticket.
  If you provide a single font weight, it will be applied throughout the app, overriding all the other font weights.
  Similarly, if any of the font weights are not mentioned in the support ticket, the font weight closest to the non-mentioned font weight will be applied in the app.

### Supported Font Weights

















| Font Weight | Description |
| --- | --- |
| Light | For subtle accents, secondary text, and areas where minimal emphasis is required. |
| Regular | The standard font weight for most text elements. |
| Medium | Used for subheadings, labels, or emphasis on certain text sections without the bold impact. |
| Semibold | Works well for headings, button labels, or any text that needs more attention but doesn’t require bold styling. |
| Bold | Designed for titles, primary headings, and call-to-action elements. |
| Regular Italics | Used to subtly emphasize specific words or phrases within a message. |
| Bold Italics | Combines bold and italic styles to strongly emphasize words or phrases. Ideal for highlighting key points or important actions within a chat conversation. |

## Enabling Sentry for Crash Monitoring

You can enable Sentry in your application to monitor crash logs in mobile apps.


**Dev Notes: ** To enable Sentry, raise a support ticket at
  [tickets@sprinklr.com](mailto:tickets@sprinklr.com) with the following information:



- **Live Chat App Id:** ID of the Live Chat app. You can get this from the Sprinklr UI. For more information, see Manage your Live Chat application.

- **Partner Id**

- **Environment:** Sprinklr environment (for example, prod1, prod2)


## Change Font Scale Settings​​

Sprinklr Live Chat supports font scaling, which adjusts the font size of Sprinklr Live Chat according to the end user's device settings.


**Dev Notes:** By default, font scaling is enabled.
    To enable or disable font scaling again for Sprinklr Live Chat, contact Sprinklr Support at
    [tickets@sprinklr.com](mailto:tickets@sprinklr.com).



**Handle Font Scale Change:**



-
      When a user changes the font scale while Live Chat is open, an alert will notify the user that the font scale has changed.
      After they click the OK button, they will be redirected to the brand app and will need to reopen the Live Chat app.


-
      If Live Chat is not running in the foreground and the brand app is open when the change occurs,
      no alert is shown, and the update is applied automatically.



## Configure Keyboard Send/Enter Button Behavior

The behavior of the Send/Enter key on mobile keyboards can be configured to control how it functions.

This configuration is set at the app level, with the following two options:


- **Send on Enter:** Pressing the Enter key sends the message directly.

- **Insert New Line:** Pressing the Enter key inserts a new line within the message input field.


**Dev Notes: ** To configure the Send/Enter button behavior for Sprinklr Live Chat, contact Sprinklr Support at
  [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

## Next Steps

[Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios)

## Additional Resources

See **All Integration Steps**
 [Install and Setup](https://dev.sprinklr.com/install-and-setup-lc-mobile-sdk-ios) > [Initialize](https://dev.sprinklr.com/initialize-lc-mobile-sdk-ios) > [Launch](https://dev.sprinklr.com/launch-lc-mobile-sdk-ios) > [Configure](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios) > [Advanced Configuration (Optional)](https://dev.sprinklr.com/advanced-configurations-for-lc-mobile-sdk-ios)

See [Troubleshooting](https://dev.sprinklr.com/troubleshooting-lc-mobile-sdk-ios)

  [](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios)




[Back to top](https://dev.sprinklr.com/configure-lc-mobile-sdk-ios)
