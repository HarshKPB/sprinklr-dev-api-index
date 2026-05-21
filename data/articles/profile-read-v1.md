---
title: "Profile Read v1"
slug: profile-read-v1
url: https://dev.sprinklr.com/profile-read-v1
---

# Profile Read v1

#
  GET - Profile Read

Using this API, you can fetch profile details for the given channel type and user Id.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v1/profile

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













			[Channel Type](https://dev.sprinklr.com/channels-v1)










| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| snType | Requied | for the message | String |
| snUserId | Required | User Id of the channel. | String |


## Example - Request





 Copy Code


curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/profile?snType=INSTAGRAM&snUserId=181037639' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'





## Example - Response




[{
    "id": "56f76964e4b0561cc540ba0f",
    "contactInfo": {
        "fullName": "amyschumer"
    },
    "socialProfiles": [{
        "name": "",
        "type": "INSTAGRAM",
        "snId": "181037639",
        "username": "amyschumer",
        "bio": "",
        "following": 330,
        "followers": 3839371,
        "favCount": 0,
        "reach": 0,
        "statusCount": 1671,
        "url": "https://instagram.com/amyschumer",
        "profileImageUrl": "https://scontent.cdninstagram.com/t51.2885-19/11849068_1616971591925315_1106846098_a.jpg",
        "snCreatedTime": 0,
        "snModifiedTime": 0
    }],
    "socialScoreCard": {
        "participationIndex": 0,
        "influencerIndex": 0,
        "spamIndex": 0
    },
    "profileWorkflowProperties": {
        "tags": [],
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
    "snCreatedTime": 0,
    "snModifiedTime": 0,
    "createdTime": 1459054948853,
    "modifiedTime": 1459054948853,
    "accountsFollowedByUser": [],
    "accountsFollowingUser": [],
    "accountsUnFollowingUser": [],
    "accountsUnFollowedByUser": [],
    "accountsBlockingUser": [],
    "additional": {
        "pT": ["COMPLETE"]
    }
}]





[](https://dev.sprinklr.com/profile-read-v1)




[Back to top](https://dev.sprinklr.com/profile-read-v1)
