---
title: "GDPR - Create View Request"
slug: v1-gdpr-create-view-request
url: https://dev.sprinklr.com/v1-gdpr-create-view-request
---

# GDPR - Create View Request

#
  POST GDPR - Create View Request

Using this API, you can submit a profile view request using the snUserId and channel type

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/gdpr/view

### Headers

API headers include the mandatory information that you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











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

### Request Parameters






























        [channel type associated with the customer's audience profile](https://dev.sprinklr.com/channels-v1)











| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| profileKeys |  | Required | Array containing the profile details of the users such as snUserId (channelId) and snType (channel type) | Array |
|  | id | Required | Refers to the snUserid (channelId) of the profile. You can find this Id from the properties section mentioned under user profile on Sprinklr's platform | String |
|  | type | Required | The respective | String |
| referenceId |  | Required | Refers to the unique identifier for the view request. This needs to be set from the client side. | String |

## Sample - Request














Copy Code




curl -X POST \
 https://api3.sprinklr.com/{env}/api/v1/gdpr/view \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "profileKeys": [
       {
           "id" : "12345678",
           "type": "TWITTER"
       }
   ],
   "referenceId": "System_ID"
}'





## Sample - Response





"62c6e115367dcd0eb5f6f996"





### Response Parameters











        [fetch request status API](https://dev.sprinklr.com/v1-gdpr-fetch-request-status)



| Parameters | Description | Type |
| --- | --- | --- |
| requestId | Refers to the unique identifier for tracking the request status. You can pass this Id as a path parameter in the  to check the status of your view request | String |

[](https://dev.sprinklr.com/v1-gdpr-create-view-request)




[Back to top](https://dev.sprinklr.com/v1-gdpr-create-view-request)
