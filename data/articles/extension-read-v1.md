---
title: "Extension Read v1"
slug: extension-read-v1
url: https://dev.sprinklr.com/extension-read-v1
---

# Extension Read v1

#
  GET Extension Read




Using this API, you can fetch the extension details using the unique extension Id.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v1/extension/{Id}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














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


















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | The id of the Extension point on which you want to make a Read API call. | String |

## Example - Request















Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}api/v1/extension/5c2f44c8e4b08015475d35ac' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \






## Example - Response




 {
    "id": "5c2f44c8e4b08015475d35ac",
    "name": "Chatbot Service Call",
    "extName": "Chatbot Service Call",
    "type": "RULE",
    "assetClass": "UNIVERSAL_CASE",
    "url": "http://requestbin.net/r/18p3kxa1",
    "inputFields": [
        {
            "fieldName": "caseName",
            "fieldLabel": "Case Name"
        },
        {
            "fieldName": "caseNumber",
            "fieldLabel": "Case Number"
        }
    ],
    "outputFields": [
        {
            "fieldName": "thirdPartyCaseName",
            "fieldLabel": "Third party case name"
        },
        {
            "fieldName": "thirdPartyCaseNumber",
            "fieldLabel": "Third party case number"
        }
    ],
    "method": "POST",
    "headers": {
        "apiKey": "[apikey]",
        "accessToken": "[token]"
    },
    "enabled": true,
    "encodeQueryParamValues": false
}







	[](https://dev.sprinklr.com/extension-read-v1)






[Back to top](https://dev.sprinklr.com/extension-read-v1)
