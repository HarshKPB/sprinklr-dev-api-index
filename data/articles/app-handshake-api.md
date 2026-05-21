---
title: "App Handshake API"
slug: app-handshake-api
url: https://dev.sprinklr.com/app-handshake-api
---

# App Handshake API

#
		 App Handshake API




The user can be authenticated using this app handshake API call. If the user has already logged in to the website/application, the user details can be passed in the chatUser object in the payload. Adding the user details in the payload will authenticate the user and will improve chat experience as you don't need to ask customer for their basic details during the chat session. If the user hasn't logged in, chatUser object can be skipped and the user will be considered as an anonymous user.

**Prerequisite for User Authentication: **The user details passed in the chatUser object are authenticated by passing a signature within this API. The signature is a HMAC or hash-based message authentication code. To generate the signature SHA256 hash function is used. Prior to generating the signature, user string needs be generated for which the syntax is as follows: `userId_firstName_lastName_profileImageUrl_phoneNo_email`. The HMAC of the user string will be signature that needs to be passed in the API.

**Generating the User String - Examples**

**Example 1:**

User string when all the user details are present: "12345_John_Doe_https://www.example.com/profilepic1.jpg_1234567890_john.does@sprinklr.com"

**Example 2:**

User string when the user doesn't have a registered phone number or profile image URL: "12345_John_Doe___john.does@sprinklr.com (*Don't skip underscore even when you have missing fields. For example, this string has three consecutive underscores between last name and email Id*)

**Note:** Once the user string is generated, you can use the API key (*generated from Live Chat application configuration on the UI*) and the User String to generate the signature using Java code

## How to Extract the Live Chat Application's API key?

- Navigate to Sprinklr Service on the platform and click on "Live Chat Care" Option under "Brand Care"

- Search for the desired live chat application and click on the three dots beside the application name

- Choose the "Edit" option from the drop-down menu

- Navigate to "Dev Tools" within the "Configure Your Live Chat" window

- Use the existing API key or generate a new one and use it in to generate the SHA256 signature

**Dev Notes: **

- If you don't have the profile image Url, you can skip it from the above string. For instance, you skip the last image url, there will be two underscores after the lastName, i.e., userId_firstName_lastName__phoneNo_email
- Hash generation should only be done on server side. This practice ensures that the API key is secure and not exposed on the client side.
- On every app/page refresh, send a new handshake call with user details mentioned within chatUserObject along with signature details for pre-authentication. It is not recommended to use the same chat token from previous handshake
- After the user logs out or exits the chat, it is recommended to discard the chat session token from the database
- Two distinct users shouldn't use the same user id during pre-authorization

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/handshake/appHandshake

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.
















			``



| Key | Value | Description |
| --- | --- | --- |
| origin | {Live Chat Application Landing Page Url} | Refers to the landing page base url where the live chat application is hosted |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters













****

-
-

[article](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)

| Parameters | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| appId |  | Required | Refers to the unique identifier for the live chat applicationHow to Extract appId from UI?Navigate to Sprinklr Service on the platform and click on "Live Chat Care" Option under "Brand Care"Search for the desired live chat application and copy and use the "Application ID" from the third column mentioned against the application name | String |
| page |  | Required | Refers to the landing page url where the live chat application is hosted | String |
| pageTitle |  | Optional | Refers to the page title of the live chat application | String |
| timezone |  | Required | Refers to the time zone in which the user is interacting with the live chat application | String |
| userAgent |  | Required | Refers to the device and browser that the customer is using.Refer to this  for more information | String |
| fallbackLocales |  | Optional | Refers to the language codes that will be supported on the live chat application | List [String] |
| chatUser |  | OptionalRequired when the user has logged in to the website/application | Refers to the object containing the user details | Object |
|  | userId | Required for a logged in user | Refers to the unique identifier for the user on the webiste/application | String |
|  | firstName | Optional | Refers to the first name of the user | String |
|  | lastName | Optional | Refers to the last name of the user | String |
|  | profileImageUrl | Optional | Refers to the profile image/display image URL of the user on the website/application | String |
|  | phoneNo | Optional | Refers to the contact number of the user | String |
|  | email | Optional | Refers to the email Id of the user | String |
| chatUserSignature |  | OptionalRequired if the existing user needs to be authenticated | Refers to the SHA256, which is a hash-based message authentication code | String |
| customContext |  | Optional | Refers to the object containing key and value pairs for profile custom field names and corresponding values | Object |

## Example 1 - If User Details are Missing




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/handshake/appHandshake \
  -H 'origin: {https://live-chat-static.sprinklr.com}' \
  -H 'Content-Type: application/json' \
  -d '{
    "appId": "65015cddb2678b575c01b175_app_1000163501",
    "page": "https://live-chat-static.sprinklr.com/test-html/index.html?appId=65015cddb2678b575c01b175_app_1000163501&env=prod0",
    "pageTitle": "Sprinklr Live Chat",
    "timezone": "Asia/Calcutta",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "fallbackLocales": [
        "en-GB"
    ]
}'



### Example - Response



{
    "chatSessionToken": "eyJhbGciOiJSUzI1NiJ9.eyJ2aXNpdFNlc3Npb25JZCI6IjY1YWU1NWVkZTBiNDhjMjYxMDRkODMyZSIsInN1YiI6IkFjY2VzcyBUb2tlbiBHZW5lcmF0ZWQgQnkgU3ByaW5rbHIiLCJjaGF0TG9jYWxlIjoiZW4iLCJjaGF0VXNlckhhc0NvbnZlcnNhdGlvblN0YXJ0ZWQiOmZhbHNlLCJpc3MiOiJTUFJJTktMUiIsInZpc2l0U2Vzc2lvbklkRXhwaXJlQXQiOjE3MDU5NjcyNzc4MjcsInR5cCI6IkpXVCIsImlzRGVmbGVjdGlvblRva2VuIjpmYWxzZSwidXNlclNlc3Npb25Mb2dpbk1ldGhvZCI6IntcInR5cGVcIjpcIkFOT05ZTU9VU1wifSIsImNoYXRVc2VySWQiOiJBXzY1YWU1NWVkZTBiNDhjMjYxMDRkODMyZCIsImFwcElkIjoiYXBwXzEwMDAxNjM1MDEiLCJzY29wZSI6WyJSRUFEIiwiV1JJVEUiXSwiZXhwIjoxNzA1OTY3Mjc3LCJhdXRoVHlwZSI6IlNQUl9LRVlfUEFTU19MT0dJTiIsImlhdCI6MTcwNTkyNDA3NywianRpIjoiNGY5NzY4ZmQtM2U1MS00MGIzLWFlMmUtMDNmYjUwNTBjOTIxIiwiYW5vbnltb3VzSWQiOiJBXzY1YWU1NWVkZTBiNDhjMjYxMDRkODMyZCIsImNsaWVudElkIjoxMDAwMDA1NjcyLCJzdHJpY3RVc2VyQXV0aGVudGljYXRpb24iOmZhbHNlLCJ1c2VySWQiOjAsImF1ZCI6IlNQUklOS0xSIiwibmJmIjoxNzA1OTIyODc3LCJtcXR0QWNsIjoie1wicFwiOltcInB1Ymxpc2gvQV82NWFlNTVlZGUwYjQ4YzI2MTA0ZDgzMmQvcHRyLTkxNzgtdG9waWNcIl0sXCJzXCI6W1wiYXBwXzEwMDAxNjM1MDFfaW5ib3gvQV82NWFlNTVlZGUwYjQ4YzI2MTA0ZDgzMmRcIixcImluYm94L0FfNjVhZTU1ZWRlMGI0OGMyNjEwNGQ4MzJkXCJdfSIsImNoYXRVc2VyVHlwZSI6IkFOT05ZTU9VUyIsInBhcnRuZXJJZCI6OTE3OCwidG9rZW5UeXBlIjoiQUNDRVNTIn0.CHPIyQH73LOXfls-CLmpAbW9Er9j0-CJBCL9v-5EnhMUz4FPSCZOTVLw6wgL72o5jp_V4hpT-FGJXtDGZ7DloeVZim-p21nJy4ne3lXX5yikAaI8R2tt4ilaZODzrhrqr9PQeKkWENArdLz2ediDFPHhgRuQX4UShn0oQ73x1tBcKbpU-fNVAayyfdUsrjd7f9BbKWZ0TDAAHpfNaIwcnRvjS0UBJmJzInyyaPkSrYh6PMEZcpDKfpp_yo5sFMCQJvtUC6um4CjTVbKRn9CvG9EFBKhuu0lEu1zw8qYegIHsMW3AiOIxE-wBfxpGeKdRyLSjeCLqo9lkIXViUkzDpQ",
    "anonymousInbox": "app_1000163501_inbox/A_65ae55ede0b48c26104d832d",
    "userInbox": "app_1000163501_inbox/A_65ae55ede0b48c26104d832d",
    "inboxServerUrl": "wss://prod0-live-chat-emqx.sprinklr.com/mqtt",
    "anonymousId": "A_65ae55ede0b48c26104d832d",
    "chatUser": {
        "userId": "A_65ae55ede0b48c26104d832d",
        "userType": "ANONYMOUS",
        "fullName": ""
    },
    "botUsers": [
        {
            "userId": "P_0",
            "userType": "PARTNER"
        },
        {
            "userId": "P_-100",
            "userType": "PARTNER"
        },
        {
            "userId": "P_-30002",
            "userType": "PARTNER"
        },
        {
            "userId": "P_-30001",
            "userType": "PARTNER"
        },
        {
            "userId": "P_-200",
            "userType": "PARTNER"
        }
    ]
}



## Example 2 - If User Details are Provided




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/handshake/appHandshake \
  -H 'origin: {https://live-chat-static.sprinklr.com}' \
  -H 'Content-Type: application/json' \
  -d '{
    "appId": "65015cddb2678b575c01b175_app_1000163501",
    "page": "https://live-chat-static.sprinklr.com/test-html/index.html?appId=65015cddb2678b575c01b175_app_1000163501&env=prod0",
    "pageTitle": "Sprinklr Live Chat",
    "referralPage": "",
    "timezone": "Asia/Calcutta",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "chatUser": {
        "userId": "123456",
        "firstName": "John",
        "lastName": "Doe",
        "profileImageUrl": "https://xyz.com/image.png",
        "phoneNo": "+12223334444",
        "email": "john.doe@xyz.com"
    },
    "chatUserSignature": "9c964d61fee63625cfd3246fbdd93292e5e1705ff015379df452f37b1f39dc77",
    "customContext": {
        "_c_65829df5a233b35d70eed593": [
            "ABC"
        ]
    }
}'



### Example - Response



{
    "chatSessionToken": "eyJhbGciOiJSUzI1NiJ9.eyJ2aXNpdFNlc3Npb25JZCI6IjY1YWU1Njc2MTMzY2Q2M2ZjMjA2Yzg5NSIsInN1YiI6IkFjY2VzcyBUb2tlbiBHZW5lcmF0ZWQgQnkgU3ByaW5rbHIiLCJjaGF0TG9jYWxlIjoiZW4iLCJjaGF0VXNlckhhc0NvbnZlcnNhdGlvblN0YXJ0ZWQiOmZhbHNlLCJpc3MiOiJTUFJJTktMUiIsInZpc2l0U2Vzc2lvbklkRXhwaXJlQXQiOjE3MDU5Njc0MTQyNTEsInR5cCI6IkpXVCIsImlzRGVmbGVjdGlvblRva2VuIjpmYWxzZSwidXNlclNlc3Npb25Mb2dpbk1ldGhvZCI6IntcInR5cGVcIjpcIlBSRV9BVVRIXCJ9IiwiY2hhdFVzZXJJZCI6IkNfMTIzNDU2IiwiYXBwSWQiOiJhcHBfMTAwMDE2MzUwMSIsInNjb3BlIjpbIlJFQUQiLCJXUklURSJdLCJleHAiOjE3MDU5Njc0MTQsImF1dGhUeXBlIjoiU1BSX0tFWV9QQVNTX0xPR0lOIiwiaWF0IjoxNzA1OTI0MjE0LCJqdGkiOiI0NTY0YzVkNS0yMWU4LTRhNjktYjNkOC01ODhiOGEzYTEyMzUiLCJhbm9ueW1vdXNJZCI6IkFfNjVhZTU2NzYxMzNjZDYzZmMyMDZjODk0IiwiY2xpZW50SWQiOjEwMDAwMDU2NzIsInN0cmljdFVzZXJBdXRoZW50aWNhdGlvbiI6dHJ1ZSwidXNlcklkIjowLCJhdWQiOiJTUFJJTktMUiIsIm5iZiI6MTcwNTkyMzAxNCwibXF0dEFjbCI6IntcInBcIjpbXCJwdWJsaXNoL0NfMTIzNDU2L3B0ci05MTc4LXRvcGljXCJdLFwic1wiOltcImFwcF8xMDAwMTYzNTAxX2luYm94L0NfMTIzNDU2XCIsXCJpbmJveC9DXzEyMzQ1NlwiXX0iLCJjaGF0VXNlclR5cGUiOiJDVVNUT01FUiIsInBhcnRuZXJJZCI6OTE3OCwidG9rZW5UeXBlIjoiQUNDRVNTIn0.EREyBdfF5hV4w1n0Zb_wOyH2CCLkMkhVd9d7Rl6oRK7A0vREy4Z0HKwI9Zu7stWZPb2497LtnieoynWO7Hq265IkLW4Pql8TZNaYznj03KMie9XWk3JqlZAvLUzC8ZMhpSwnUWb5fqvpya1-YhCJ1Q2Vu3rRZ1w-FIkAaUsMQYWkgAzQf_VV79Xc1OFuwWnhTZ6ebphObuwGrxqGysFztPZleLQENTXBKCwGc_WP2RkmbU3HnnVdNGMRFxQw3Ra1v6BmxvvehAN_L110aqDIqjEBNjZ7vJaVEvD0cwzPgXQkHBk1GSpFeOmrCEPMOlKfhRKmJxLlJA2SADk1zqNjqQ",
    "anonymousInbox": "app_1000163501_inbox/A_65ae5676133cd63fc206c894",
    "userInbox": "app_1000163501_inbox/C_123456",
    "inboxServerUrl": "wss://prod0-live-chat-emqx.sprinklr.com/mqtt",
    "anonymousId": "A_65ae5676133cd63fc206c894",
    "chatUser": {
        "userId": "C_123456",
        "userType": "CUSTOMER",
        "firstName": "John",
        "lastName": "Doe",
        "fullName": "John Doe",
        "profileImageUrl": "https://xyz.com/image.png",
        "phoneNo": "+12223334444",
        "email": "john.doe@xyz.com",
        "customContext": {
            "_c_65829df5a233b35d70eed593": [
                "ABC"
            ]
        }
    },
    "botUsers": [
        {
            "userId": "P_0",
            "userType": "PARTNER"
        },
        {
            "userId": "P_-100",
            "userType": "PARTNER"
        },
        {
            "userId": "P_-30002",
            "userType": "PARTNER"
        },
        {
            "userId": "P_-30001",
            "userType": "PARTNER"
        },
        {
            "userId": "P_-200",
            "userType": "PARTNER"
        }
    ]
}



**Dev Notes: **The appHandshake call returns a chat session token that is unique to that user. It is a JWT token and ensures that that user can only access conversations and messages pertaining to that user

 [](https://dev.sprinklr.com/app-handshake-api)




[Back to top](https://dev.sprinklr.com/app-handshake-api)
