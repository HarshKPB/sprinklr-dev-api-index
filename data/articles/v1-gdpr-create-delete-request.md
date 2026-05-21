---
title: "GDPR - Create Delete Request"
slug: v1-gdpr-create-delete-request
url: https://dev.sprinklr.com/v1-gdpr-create-delete-request
---

# GDPR - Create Delete Request

#
  POST GDPR - Create Delete Request

Using this API, you can delete the cases and profile associated with the user profile.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/gdpr/delete

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












****

``

[create view GDPR request API](https://dev.sprinklr.com/v1-gdpr-create-view-request)

****

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| deleteType | Optional | Enum: CUSTOM, EVERYTHINGIf the deleteType is set to EVERYTHING, you only need to pass deleteType and requestId in the request body | String |
| requestId | Required | The request Id you receive from the | String |
| reason | Optional | The reason for deleting the profile data | String |
| activityType | Optional | Enum: SOCIAL, AUDIENCE, LISTENING | String |

## Sample - Request 1














Copy Code




curl -X POST \
 https://api3.sprinklr.com/{env}/api/v1/gdpr/delete \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "deleteType": "CUSTOM",
  "reason": "API Testing rocks",
  "requestId": "62cffa1ab31d3e637cf01369",
  "callbackUrl": "",
  "activityType": "SOCIAL"
}'





## Sample - Response





"62cffa1ab31d3e637cf01369"





### Response Parameters















| Parameters | Description | Type |
| --- | --- | --- |
| requestId | The request id you passed in the request body. It indicates that the delete action has been successful. | String |

**Dev Notes: **Use the [Fetch GDPR request status API](https://dev.sprinklr.com/v1-gdpr-fetch-request-status) to fetch the status of the submitted delete request.

## Delete Request with `profileKeys`

You can pass the profile identifier in the request body. Specify the identifier using either:


- `id` and `type` (for example, `INSTAGRAM`), or

- `externalSnType` and `externalSnId` (for example, `LITHIUM`).

The API responds with a `requestId`, which you can use to check the status of the deletion request.


### Request Body











      ``


      ````````


      ``






| Field | Type | Required | Description |
| --- | --- | --- | --- |
| profileKeys | array | Yes | List of profile identifiers to delete. Each object must include either (id, type) or (externalSnType, externalSnId). |
| referenceId | number | Yes | Client-defined reference ID to associate with the deletion request. |

#### profileKeys object (option 1: id + type)











      ``





      ``


      ``



| Field | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes | Unique identifier of the profile. |
| type | string | Yes | Type of the profile (for example, INSTAGRAM). |

#### profileKeys object (option 2: externalSnType + externalSnId)











      ``


      ``


      ``






| Field | Type | Required | Description |
| --- | --- | --- | --- |
| externalSnType | string | Yes | External system type (for example, LITHIUM). |
| externalSnId | string | Yes | External system identifier. |

## Sample - Request 2














Copy Code




curl -X POST \
 https://api3.sprinklr.com/{env}/api/v1/gdpr/delete \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "profileKeys": [
        {
            "id": "7481042153",
            "type": "INSTAGRAM"
        }
    ],
    "referenceId": 98671120356
}'





## Sample - Response





"62cffa1ab31d3e673645abc"







## Sample - Request 3














Copy Code




curl -X POST \
 https://api3.sprinklr.com/{env}/api/v1/gdpr/delete \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "profileKeys": [
    {
      "externalSnType": "LITHIUM",
      "externalSnId": "3700283"
    }
  ],
  "referenceId": 986711202
}'





## Sample - Response





"62cffa1ab31d3e637ab0234569"






[](https://dev.sprinklr.com/v1-gdpr-create-delete-request)




[Back to top](https://dev.sprinklr.com/v1-gdpr-create-delete-request)
