---
title: "Fetch Notifications and User Heartbeat"
slug: fetch-notifications-and-user-heartbeat
url: https://dev.sprinklr.com/fetch-notifications-and-user-heartbeat
---

# Fetch Notifications and User Heartbeat

# Fetch Notifications and User Heartbeat



This API addresses the following use cases:

- Fetch notifications for NEW_MESSAGE, CONVERSATION_UPDATED, and MESSAGE_UPDATED. The notifications have an expiry time of ten minutes, so any notification prior to that won't be returned.

- Returns user's heartbeat, i.e., it notifies the servers that the user is online. t is recommended to make this API call every 15 seconds.

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/event/fetch-notifications


### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			``



| Key | Value | Description |
| --- | --- | --- |
| x-chat-token | The token you received in the App Handshake API response | The token for authenticating the live chat session |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Query Parameters












****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| size | Optional | Refers to the indicator implying the number of notifications to be fetched | Integer |
| cursor | Optional | Specifies whether looking before or after a particular notification Id. If not present, the last (size) notifications will be fetched | String |
| sortDirection | Optional | Refers if you want the results in ascending or descending orderDefault:ASC | String |
| lastActiveDiff | Optional | Refers to the time in milliseconds since the user was not online on the live chat application. Send 0 if the user is currently on the application | Integer (milliseconds) |

**Dev Notes: **

- The lastActiveDiff does not affect the API response but helps set the timestamp when the user was last active. If this parameter is missing in the API query parameters, the last active status won't be returned in the response

- When the user last active status is returned, it helps determine if the user has been inactive long enough to unassign the agent

## Example - Request




  Copy Code


curl -X GET \
 'https://{env}-live-chat.sprinklr.com/api/livechat/v1//event/fetch-notifications'\
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \





## Example - Response



{
    "results": [
        {
            "id": "6544e7852be0294f35fd2447",
            "payload": {
                "type": "NEW_MESSAGE",
                "retain": true,
                "sendPushNotification": true,
                "messageId": "6544e7842be0294f35fd2441",
                "description": "First customer message",
                "mobilePushContent": "First customer message"
            },
            "conversationId": "6544dd1c2be0294f35fd1577",
            "sender": "A_6544dcfe0bb9e11ed1dcb137",
            "creationTime": 1699014533436,
            "appId": "app_1000163501"
        }
    ],
    "hasMore": false,
    "totalCount": 0,
    "beforeCursor": "B_6544e7852be0294f35fd2449",
    "afterCursor": "A_6544e7852be0294f35fd2449"
}





**Dev Notes: **For fetching the previous or next set of results, kindly use the beforeCursor and afterCursor respectively in the query parameters. If hasMore is true, you can use the beforeCursor and afterCursor from the response in the API request for fetching the previous/next set of results.

[](https://dev.sprinklr.com/fetch-notifications-and-user-heartbeat)

[Back to top](https://dev.sprinklr.com/fetch-notifications-and-user-heartbeat)
