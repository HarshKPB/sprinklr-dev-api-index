---
title: "Delete Comment"
slug: delete-comment
url: https://dev.sprinklr.com/delete-comment
---

# Delete Comment

#
  DELETE - Delete Comment


 You can use the Delete Comment API to delete comments in different entity types using entity Id and comment Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/comment/`{entityType}`/`{entityId}`/`{commentId}`

**Dev Note: ** Supported entity types: `MESSAGE, CASE, CAMPAIGN, PROFILE.`

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

## Path Parameters































| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityType | Required | Entity type can be MESSAGE, CASE, CAMPAIGN and PROFILE. | String |
| entityId | Required | Entity id with respect to entity types. e.g  MESSAGE - Message Id , CASE - Case number, CAMPAIGN - Campaign Id and PROFILE - Profile Id. | String |
| commentId | Required | Comment id with respect entity Id within entity types. | String |


## Example - Delete Case Comment





 Copy Code



curl -X DELETE \
  https://api3.sprinklr.com/{env}/api/v2/comment/CASE/7002641/5e2049c50844e44647eb017f \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -H 'accept: application/json'





## Example - Response




HTTP/1.1 204 (No Content)





API Endpoint for PROFILE, MESSAGE and CAMPAIGN:










         `
`



         `
`



         `
`


| Entity Type | Endpoint |
| --- | --- |
| PROFILE | https://api3.sprinklr.com/{env}/api/v2/comment/PROFILE/{profileId}/{commentId} |
| MESSAGE | https://api3.sprinklr.com/{env}/api/v2/comment/MESSAGE/{messageId}/{commentId} |
| CAMPAIGN | https://api3.sprinklr.com/{env}/api/v2/comment/CAMPAIGN/{campaignId}/{commentId} |

[](https://dev.sprinklr.com/delete-comment)

[Back to top](https://dev.sprinklr.com/delete-comment)
