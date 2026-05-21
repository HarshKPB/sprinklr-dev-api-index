---
title: "Fetch Transaction"
slug: fetch-transaction
url: https://dev.sprinklr.com/fetch-transaction
---

# Fetch Transaction

#   GET Fetch CFM Transaction

The API retrieves detailed information about a specific transaction using its unique Transaction ID. This allows you to validate and review transaction attributes, including user details, distribution channel, and status.

 **Developer Note:**

 To fetch all transaction details within a transaction group, use the [Search by Entity API](https://dev.sprinklr.com/search-by-entity) with `TRANSACTION` as the `entityType` and sending `transactionGroupId`  in the `filters` object. The API response includes a **cursor** that you can pass to the [Search by Cursor API](https://dev.sprinklr.com/search-by-cursor) to retrieve the next set of results.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/survey-transactions/`{transactionId}`

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

## Path Parameter



















| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| transactionId | string | Yes | The unique identifier of the transaction. |

## Example Request

Copy Code


	curl --location 'https://api3.sprinklr.com/{env}/api/v2/survey-transactions/68b84e609cc8a225da9e269d' \
--header 'Authorization: Bearer {token}' \
--header 'Key: {api_key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \

## Example - Response


{
    "data": {
        "id": "68b84e609cc8a225da9e269d",
        "userId": "shivangi+qa6@sprinklr.com",
        "profileName": "shivi",
        "transactionGroupId": "68adc96c444bb074f1fd28f7",
        "distributionChannel": "SMS",
        "transactionGroupType": "UDC",
        "customProperties": {
            "orderId": [
                "ORD-123654"
            ],
            "purchaseAmount": [
                "180.75"
            ],
            "purchaseCategory": [
                "Grocery"
            ]
        },
        "isArchived": false,
        "ownerUserId": 66014640,
        "createdTime": "Sep 03, 2025, 02:19:12 PM",
        "lastModifiedUserId": 66014640,
        "deleted": false,
        "canEdit": false
    },
    "errors": []
}



## Response Schema






































      ````````






































| Parameter | Type | Description |
| --- | --- | --- |
| id | string | Unique identifier of the transaction. |
| userId | string | User identifier used in the request. |
| profileName | string | User profile name. |
| transactionGroupId | string | ID of the transaction group. |
| distributionChannel | string | Distribution channel used. |
| transactionGroupType | string | Type of the transaction group. It can be API, UDC, Import, or Workflow based on ingestion method. |
| customProperties | object | Custom key-value metadata for the transaction. |
| isArchived | boolean | Status of the transaction (archived or active). |
| ownerUserId | number | Owner user ID who created the transaction. |
| createdTime | string | Timestamp of transaction creation. |
| lastModifiedUserId | number | User ID who last modified the transaction. |
| deleted | boolean | Indicates if the transaction is deleted. |
| canEdit | boolean | Indicates if the transaction can be edited. |

[](https://dev.sprinklr.com/fetch-transaction)

[Back to top](https://dev.sprinklr.com/fetch-transaction)
