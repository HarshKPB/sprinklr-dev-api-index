---
title: "Update Account Custom Properties"
slug: update-account-custom-properties
url: https://dev.sprinklr.com/update-account-custom-properties
---

# Update Account Custom Properties

#
  PUT Update Account Custom Properties

You can update an account's partner/client custom properties using this API call.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/account/update/{accountId}/customProperties

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

### Path Parameter















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| accountId | Required | Unique Id of the account. | String |

### Request Parameters










| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| spaceId | Optional | Refers to the workspace Id where the account exists | Integer |
| partnerCustomProperties | Optional | Refers to the object containing key and value pair for partner level customer properties and corresponding values | Object |
| clientCustomProperties | Optional | Refers to the object containing key and value pair for workspace level customer properties and corresponding values | Object |

## Example - Request




 Copy Code



curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/account/update/600000132/customProperties' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
        "spaceId":0,
        "partnerCustomProperties": {
    },
    "clientCustomProperties": {

    }
}'



## Example - Response




204 No Content




[](https://dev.sprinklr.com/update-account-custom-properties)




[Back to top](https://dev.sprinklr.com/update-account-custom-properties)
