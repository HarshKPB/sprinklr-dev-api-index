---
title: "Audit API"
slug: audit-api
url: https://dev.sprinklr.com/audit-api
---

# Audit API

#
  POST Audit API

Audit API helps track the changes made to an asset over time. In other words, Audit API helps identify and analyze the user actions made to assets, i.e., who made what changes and when.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/audit/fetch

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

## Request Parameters









****


****

****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| assetId | Required | The unique identifier for the given asset class | String |
| assetClass | Required | Several feature levels that are available in the Sprinklr platform such as Account, Outbound Message, Message, or ProfileExamples: UNIVERSAL_CASE, MESSAGE_WORKFLOW, PROFILE_WORKFLOW, MEDIA_ASSET, OUTBOUND_MESSAGE, USER, SPR_TASK | String |
| order | Optional | The order in which the response will appearExample: ASC for ascending and DESC for descending | String |
| limit | Optional | Number of results in the responseDefault: 50Maximum Limit/API Call: 200 | Integer |

## Example - Request














Copy Code




curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/audit/fetch \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
-d '{
	"assetIds": [
        10520954
    ],
    "assetClass": "UNIVERSAL_CASE",
    "order": "DESC",
    "limit" : 2
}'





## Example - Response





{
    "data": {
        "results": [
            {
                "assetClass": "UNIVERSAL_CASE",
                "assetId": "10520954",
                "auditDate": 1650461298712,
                "userId": 0,
                "changes": [
                    {
                        "fieldName": "Messages",
                        "oldValues": [],
                        "newValues": [
                            "New value 1"
                        ]
                    }
                ]
            },
            {
                "assetClass": "UNIVERSAL_CASE",
                "assetId": "10520954",
                "auditDate": 1650461298594,
                "userId": 0,
                "changes": [
                    {
                        "fieldName": "Message Sentiment",
                        "oldValues": [],
                        "newValues": [
                            "New value 2"
                        ]
                    }
                ]
            }
        ],
        "cursor": "638e12816d414169dc5ad755"
    },
    "errors": []
}





### Response Parameters




















































































| Parameters | Sub-Params | Sub-Params | Description | Type |
| --- | --- | --- | --- | --- |
| Results |  |  | Array listing the details of the response | Array |
|  | assetClass |  | assetClass for which the request is made | String |
|  | assetId |  | The assetId mentioned in the request | String |
|  | auditDate |  | The date on which the asset was analyzed | Epoch |
|  | userId |  | The Id of the user who made the changes | Integer |
|  | changes |  | Lists the change details | Array |
|  |  | fieldName | The name of the field that was modified | String |
|  |  | oldValues | The old value of the field | String |
|  |  | newValues | The new or the changed value of the field | String |
| cursor |  |  | If the API response has additional data that exceeds the mentioned limit in the request, a cursor Id is returnedYou can use this cursor Id to fetch the next set of data | String |

**Next Up**: [Fetch Audit Details using Cursor Id](https://dev.sprinklr.com/fetch-audit-details-by-cursor)

	 [](https://dev.sprinklr.com/create-asset-group)




[Back to top](https://dev.sprinklr.com/create-asset-group)
