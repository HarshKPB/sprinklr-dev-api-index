---
title: "Profile Conversation Read v1"
slug: profile-conversation-read-v1
url: https://dev.sprinklr.com/profile-conversation-read-v1
---

# Profile Conversation Read v1

#
  GET - Profile Conversation Read

Using this API, you can fetch profile conversations using channel type and user Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/profile/conversations

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Query Parameters



















































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| snType | Requied | Channel Type for the message | String |
| snUserId | Required | User Id of the channel. | String |
| sinceDate | Optional | The date in milliseconds since Unix Epoch from which to begin pulling conversations (Unix Time * 1000) Example: sinceDate=1471842000000 | Long |
| untilDate | Optional | The date in milliseconds since Unix Epoch from which to begin pulling conversations (Unix Time * 1000) Example: untilDate=1471842000000 | Long |
| start | Optional | The start offset. Start offset example: "A" as an array of characters containing "abcdef", the fourth element containing the character "D" has an offset of three from the start of "A". Default = 0 | Integer |
| rows | Optional | The number of rows (conversations) to fetch from the start offset | Integer |

**Dev Notes: **The conversations appear in descending order from the time the conversation was created on the social network (snCreatedTime).

## Example - Request




 Copy Code



 curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v1/profile/conversations?snType=INSTAGRAM&snUserId=181037639&start=0&rows=1' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'key: {apikey}'





### Example - Response




 [{
    "like": false,
    "partnerId": 3,
    "clientId": 4,
    "sourceId": 41,
    "accountId": 41,
    "sourceType": "ACCOUNT",
    "snType": "INSTAGRAM",
    "snMsgId": "17848334350107089",
    "messageType": 37,
    "messageSubType": 0,
    "universalMessageId": "INSTAGRAM_37_17848334350107089",
    "permalink": "https://www.instagram.com/p/BGj0NT2oVWE/",
    "message": "Tight ferret @amyschumer",
    "textEntities": {
        "message": [{
            "indices": [13, 24],
            "screenName": "amyschumer"
        }]
    },
    "senderProfile": {
        "snType": "INSTAGRAM",
        "age": 0,
        "snId": "13821047",
        "name": "spennes",
        "screenName": "spennes",
        "following": 0,
        "followers": 0,
        "favCount": 0,
        "statusCount": 0,
        "permalink": "https://instagram.com/spennes",
        "createdTime": "0",
        "profileImgUrl": "https://igcdn-photos-g-a.akamaihd.net/hphotos-ak-xap1/t51.2885-19/s150x150/12070872_1647106998909950_1262816922_a.jpg",
        "profileWorkflowProperties": {
            "comments": [],
            "notifyUserIds": [],
            "partnerProfileLists": [],
            "clientProfileLists": [],
            "partnerCustomProperties": {},
            "clientCustomProperties": {},
            "spaceCustomProperties": {},
            "userCustomProperties": {},
            "clientTags": []
        },
        "universalProfileId": "563cd3e0e4b0b8b87cd1fecc",
        "participationIndex": 20,
        "influencerIndex": 0,
        "spamIndex": 0,
        "accountsFollowedByUser": [],
        "accountsFollowingUser": [],
        "accountsUnFollowingUser": [],
        "accountsUnFollowedByUser": [],
        "accountsBlockingUser": []
    },
    "receiverProfile": {
        "snType": "INSTAGRAM",
        "age": 0,
        "snId": "787132",
        "name": "National Geographic",
        "screenName": "natgeo",
        "bio": "Life is an adventure—enjoy the ride and the world through the eyes of the National Geographic photographers.",
        "following": 95,
        "followers": 34147005,
        "favCount": 0,
        "statusCount": 8614,
        "permalink": "https://instagram.com/natgeo",
        "createdTime": "0",
        "profileImgUrl": "https://igcdn-photos-g-a.akamaihd.net/hphotos-ak-xaf1/t51.2885-19/11349315_1620970341492406_1971976479_a.jpg",
        "profileWorkflowProperties": {
            "comments": [],
            "notifyUserIds": [],
            "partnerProfileLists": [],
            "clientProfileLists": [],
            "partnerCustomProperties": {},
            "clientCustomProperties": {},
            "spaceCustomProperties": {},
            "userCustomProperties": {},
            "clientTags": []
        },
        "universalProfileId": "5627f407e4b0b8b87cbc9c7b",
        "participationIndex": 100,
        "influencerIndex": 100,
        "spamIndex": 0,
        "accountsFollowedByUser": [],
        "accountsFollowingUser": [],
        "accountsUnFollowingUser": [],
        "accountsUnFollowedByUser": [],
        "accountsBlockingUser": []
    },
    "isSenderFollower": false,
    "createdTime": 1465750997587,
    "modifiedTime": 1465750997587,
    "snCreatedTime": 1465750611000,
    "snCreatedTimeYearMonth": "2016_06",
    "snModifiedTime": 1465750611000,
    "actionTime": 1465750611000,
    "workflowProperties": {
        "sentiment": 0,
        "isSpam": false,
        "isProfane": false
    },
    "language": "en",
    "conversationId": "1271089132938024324_787132",
    "parentSnMsgId": "1271089132938024324_787132",
    "parentSnCreatedTimeYearMonth": "2016_06",
    "parentMsgType": 36,
    "deleted": false,
    "archived": false,
    "brandPost": false,
    "parentBrandPost": false,
    "hasBrandComment": false,
    "hasBrandResponded": false,
    "hasScheduledComment": false,
    "hasParentPost": true,
    "hasApplicationConversation": false,
    "hasConversation": false,
    "defaultActionTime": 1465750611000
}]





[](https://dev.sprinklr.com/profile-conversation-read-v1)




[Back to top](https://dev.sprinklr.com/profile-conversation-read-v1)
