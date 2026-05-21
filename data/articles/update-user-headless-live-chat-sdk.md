---
title: "Update User Headless Live Chat SDK"
slug: update-user-headless-live-chat-sdk
url: https://dev.sprinklr.com/update-user-headless-live-chat-sdk
---

# Update User Headless Live Chat SDK

# Update User


The `updateUser()` method dynamically updates the details of the currently logged-in user, including their profile information, custom user data, and context metadata.

## SDK Method

`updateUser()`

## Example Usage




 Copy Code


try {
  const updatedUser = await window.sprinklr.chat.updateUser({
    user: {
      userId: 'A_6800a4d15683490e558978a4',
      email: 'vedant.shah@sprinklr.com',
      firstName: 'Vedant',
      lastName: 'Shah',
      fullName: 'Vedant Shah',
      locale: 'en',
      phoneNo: '+919825413555',
      profileImageUrl: 'https://xyz.jpeg',
    },
    userContext: {
      'department': ['engineering'],
      'priority': ['high']
    },
    customUser: {
      'customField1': 'value1',
      'customField2': 'value2'
    }
  });
  console.log(updatedUser);
} catch (error) {
  console.error("Failed to update user:", error);
}



## Parameters



































| Parameter | Description | Type | Required/Optional | Example |
| --- | --- | --- | --- | --- |
| user | Contains user details such as userId, firstName, lastName, etc. | Object | Optional | {     userId: 'A_6800a4d15683490e558978a4',     email: "vedant.shah@sprinklr.com",     firstName: "vedant",     lastName: "shah",     fullName: "vedant shah",     locale: "en",     phoneNo: '+919825413555',     profileImageUrl: 'https://xyz.jpeg', } |
| userContext | Additional metadata as key-value pairs, where values are arrays of strings. | StringTMap<string[]> | Optional | { "department": ["engineering"], "priority": ["high"] } |
| customUser | Custom user data as key-value pairs. | StringAnyMap | Optional | { "customField1": "value1", "customField2": "value2" } |

## Response Format - User Object

The resolved `user` object will look like this:




 Copy Code


{
  userId: string;
  firstName: string;
  lastName?: string;
  fullName?: string;
  profileImageUrl: string;
  email: string;
  phoneNo: string;
  locale: string;
}



## Response Format - User Object



















































| Parameter | Description | Type |
| --- | --- | --- |
| userId | Unique identifier for the user. | string |
| firstName | User's first name. | string |
| lastName | User's last name. | string |
| fullName | User's full name. | string |
| profileImageUrl | URL to the user's profile image. | string |
| email | User's email address. | string |
| phoneNo | User's phone number. | string |
| locale | User's locale or language preference. | string |

  **Dev Notes: **


- **Initialization Required:** Always call `init()` before using `updateUser()`. The method will throw `CHAT_NOT_INITIATED` error if called before initialization.

- **Authentication Handling:** User authentication/login is handled by a different SDK. This method only updates user profile information.

- **Partial Updates:** The user object supports partial updates. You only need to provide the fields you want to update.

## Error Types

**Dev Notes: **For robustness, always handle `UNEXPECTED_ERROR` as a catch-all in UI or telemetry.









      ``



      ``



      ``



      ``
      ``````



| Error Type | When It Occurs |
| --- | --- |
| NOT_FOUND | Occurs when a conversation or resource is missing. |
| NOT_ACCEPTABLE | Occurs when the input format is invalid or the data is unprocessable. |
| UNEXPECTED_ERROR | Occurs for any unexpected or unclassified error. Used as a fallback for debugging purposes. |
| CHAT_NOT_INITIATED | Occurs when chat SDK methods (sendMessage, createConversation, etc.) are called before init(). |


  [](https://dev.sprinklr.com/update-user-headless-live-chat-sdk)




[Back to top](https://dev.sprinklr.com/update-user-headless-live-chat-sdk)
