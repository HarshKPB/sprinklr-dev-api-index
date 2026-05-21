---
title: "Update Comment"
slug: update-comment
url: https://dev.sprinklr.com/update-comment
---

# Update Comment

#
  PUT - Update Comment



 You can use this API to update comment on assets in different entity types

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/comment/`{entityType}`/`{entityId}`/`{commentId}`

**Dev Note: ** Supported entity types: `MESSAGE, CASE, CAMPAIGN, PROFILE.`

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/getting-started)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

## Path Parameters































| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityType | Required | Entity type can be MESSAGE, CASE, CAMPAIGN and PROFILE. | String |
| entityId | Required | Entity id with respect to entity types. e.g  MESSAGE - Message Id , CASE - Case number, CAMPAIGN - Campaign Id and PROFILE - Profile Id. | String |
| commentId | Required | Comment id with respect entity Id within entity types. | String |


## Example - Update Case Comment





 Copy Code



curl -X PUT \
  https://api3.sprinklr.com/{env}/api/v2/comment/CASE/7005734/5e2186f430372d4b8f2d40de \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -H 'accept: application/json' \
  -d  '{
        "text": "new comment updated"
       }'





## Example - Response




  "data": {
        "id": "5e2186f430372d4b8f2d40de",
        "text": "new comment updated",
        "createdTime": 1579668279487,
        "modifiedTime": 1579668279489,
        "entityType": "CASE",
        "entityId": "7005734"
    },
    "errors": []
}





**API Endpoints for PROFILE, MESSAGE and CAMPAIGN: **




















| Entity Type | Endpoint |
| --- | --- |
| PROFILE | https://api3.sprinklr.com/{env}/api/v2/comment/PROFILE/{profileId}/{commentId} |
| MESSAGE | https://api3.sprinklr.com/{env}/api/v2/comment/MESSAGE/{messageId}/{commentId} |
| CAMPAIGN | https://api3.sprinklr.com/{env}/api/v2/comment/CAMPAIGN/{campaignId}/{commentId} |

## Response Parameters









































| Parameters | Description | Type |
| --- | --- | --- |
| id | Unique Id of the comment. | String |
| text | Text of the comment. | String |
| createdTime | Time when the comment was made. | Epoch |
| modifiedTime | Time when the comment was modified. | Epoch |
| entityType | Entity type on which the asset was created. | String |
| entityId | Id of the entity on which the comment was created. | String |

[](https://dev.sprinklr.com/update-comment)




[Back to top](https://dev.sprinklr.com/update-comment)
