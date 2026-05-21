---
title: "GDPR - Create Edit Request"
slug: v1-gdpr-create-edit-request
url: https://dev.sprinklr.com/v1-gdpr-create-edit-request
---

# GDPR - Create Edit Request

#
  POST GDPR - Create Edit Request

Using this API, you can submit an edit request to modify the data received in the fetch profile data API.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/gdpr/edit

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













[GDPR create view request API](https://dev.sprinklr.com/v1-gdpr-create-view-request)

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| updateRequest | Optional | Object defining the edit request type and the associated parameters | Object |
| requestId | Required | The request id that you received in the  response | string |
| reason | Optional | Unique identifier from client side defining the reason for submitting the edit requestYou can set a custom value as per your requirements | String |


## Sample - Request














Copy Code




curl -X POST \
 https://api3.sprinklr.com/{env}/api/v1/gdpr/edit \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "updateRequest": {
    "clientCustomProperties": {
      "5b1006f1e4b0a54914f86df2": [
        "France",
        "USA"
      ]
    }
    },
  "requestId": "62d00c0c4b29c33db08c06e7",
  "reason": "API Testing rocks",
  "referenceId": "internal 3",
  "callbackUrl": ""
}'





## Sample - Response





"62d00c0c4b29c33db08c06e7"





### Response Parameters















| Parameters | Description | Type |
| --- | --- | --- |
| requestId | The request id, which can be used to fetch the status of the submitted edit request | String |

**Dev Notes: **Use the [Fetch GDPR request status API](https://dev.sprinklr.com/v1-gdpr-fetch-request-status) to fetch the status of the submitted edit request.

[](https://dev.sprinklr.com/v1-gdpr-fetch-profile-data)




[Back to top](https://dev.sprinklr.com/v1-gdpr-fetch-profile-data)
