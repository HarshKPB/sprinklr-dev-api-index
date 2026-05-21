---
title: "Initialize Headless Live Chat SDK"
slug: initialize-headless-live-chat-sdk
url: https://dev.sprinklr.com/initialize-headless-live-chat-sdk
---

# Initialize Headless Live Chat SDK

# Initialize Headless Live Chat SDK


The `init()` method initializes the session and retrieves application details required for all chat features.

**Dev Notes: **The `init()` method must be called before using any other SDK methods.

## SDK Method

`init()`

## Example Usage




 Copy Code


try {
  const SprChat = await window.sprinklr.chat.init({
    appId,
    locale,
    user,
    userContext,
    clientContext,
  });
  // SprChat and window.sprinklr.chat refer to the same initialized instance
  // You can continue using either:
  // - SprChat.sendMessage(...) OR
  // - window.sprinklr.chat.sendMessage(...)
} catch (error) {
  // Handle initialization errors
  console.error("Chat SDK initialization failed:", error);
}



## Parameters






























****




















[How to Generate Hash](https://www.sprinklr.com/help/articles/initialize-sprinklr-live-chat/how-to-generate-hash/683930dc0a718d29a525c7e0)






















































****

























| Parameter | Sub-Parameter | Description | Type | Required/Optional | Example |
| --- | --- | --- | --- | --- | --- |
| appId |  | Id of the Live Chat app. You can get this Id from the Sprinklr UI. | string | Required | 64ecba79c7648a7c177c4c8c_app_66000405 |
| locale |  | Specify the locale for the Live Chat. See the Locale table. | string | Optional | en, "ar" |
| user(for pre-authentication) |  | User object containing user info | object | Optional | {       id: string;       hash: string;       userName?: string;       firstName: string;       lastName?: string;       profileImageUrl: string;       email: string;       phoneNo: string;     } |
|  | id | Unique user Id. | string | Required (if user) | 123 |
|  | hash | Encrypted or hashed IDFor steps, see | string | Required (if user) | abc123xyz |
|  | userName | Username of the user | string | Optional | john_doe |
|  | firstName | First name of the user | string | Required (if user) | JOHN |
|  | lastName | Last name of the user | string | Optional | DOE |
|  | profileImageUrl | Profile image URL | string | Required (if user) | https://example.com/profile.jpg |
|  | email | Email address | string | Required (if user) | john@example.com |
|  | phoneNo | Phone number | string | Required (if user) | 1234567890 |
| customUser(for custom authentication) |  | Custom user object containing custom fields and values in key-value format. | object | Optional | {     tokenA: "ABC";     tokenB: "ABC";     hash: "string";   } |
| userContext |  | Metadata specific to the user | { [key: string]: string[] } | Optional | { "preferredLanguage": ["en"] } |
| clientContext |  | Metadata about client or session | { [key: string]: string[] } | Optional | { "platform": ["web"] } |

## Error Types

**Dev Notes: **For robustness, always handle UNEXPECTED_ERROR as a catch-all in UI or telemetry.






















| Error Type | When it Occurs |
| --- | --- |
| ALREADY_INITIATED | Thrown when init() is called after the chat SDK is already initialized. |
| SETTINGS_NOT_FOUND | Thrown when init() is called with empty payload object. |
| BOOT_FAILED | Thrown when it fails to fetch application details or establish a session with Sprinklr server. |


  [](https://dev.sprinklr.com/initialize-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/initialize-headless-live-chat-sdk)
