---
title: "Create Transaction"
slug: create-transaction
url: https://dev.sprinklr.com/create-transaction
---

# Create Transaction

#   POST Create CFM Transaction

This API enables you to create one or more transactions within an existing Transaction Group. Each transaction represents a single interaction record for a user.


 **Developer Note:**



- A **user profile** is a prerequisite for creating a transaction. If the specified profile does not exist, you must create it before calling this API.
Refer to [Create Profile API](https://dev.sprinklr.com/create-update-universal-profile) to create a new profile.


- A **transaction group** must also exist. Transactions can only be created within an existing transaction group.


## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/survey-transactions?transactionGroupId={transactionGroupId}

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

## Query Parameter



















| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| transactionGroupId | string | Yes | The unique identifier of the transaction group where the transaction will be created.         You must create a transaction group in your CFM persona app before using this API. |

## Request Parameters



























      ``````









| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| userId | string | Yes | The unique identifier of the Sprinklr profile, like Email or Phone number. |
| profileName | string | Yes | User profile name. |
| distributionChannel | string | Yes | Channel used for distribution. Supported values: EMAIL, WHATSAPP_BUSINESS, SMS |
| customProperties | object | No | Custom key-value metadata for the transaction. |

## Example Request

Copy Code


	curl --location 'https://api3.sprinklr.com/{env}/api/v2/survey-transactions?transactionGroupId=68adc96c444bb074f1fd28f7' \
--header 'Authorization: Bearer {token}' \
--header 'Key: {api_key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data-raw '[
    {
        "userId": "lalith.p+704@sprinklr.com",
        "profileName": "lalith",
        "distributionChannel": "EMAIL",
        "customProperties": {
            "orderId": "ORD-987654",
            "purchaseAmount": "150.75",
            "purchaseCategory": "Electronics"
        }
    },
    {
        "userId": "shivangi+qa6@sprinklr.com",
        "profileName": "shivi",
        "distributionChannel": "SMS",
        "customProperties": {
            "orderId": "ORD-123654",
            "purchaseAmount": "180.75",
            "purchaseCategory": "Grocery"
        }
    },
        {
        "userId": "shivangi+qa6@sprinklr.com",
        "profileName": "shivi",
        "distributionChannel": "WHATSAPP_BUSINESS",
        "customProperties": {
            "orderId": "ORD-123890",
            "purchaseAmount": "500",
            "purchaseCategory": "Home_Appliance"
        }
    }
]'

## Example - Response


{
    "data": [
        {
            "id": "68b84e609cc8a225da9e269c",
            "userId": "lalith.p+704@sprinklr.com",
            "profileName": "lalith",
            "transactionGroupId": "68adc96c444bb074f1fd28f7",
            "distributionChannel": "EMAIL",
            "transactionGroupType": "API",
            "customProperties": {
                "orderId": [
                    "ORD-987654"
                ],
                "purchaseAmount": [
                    "150.75"
                ],
                "purchaseCategory": [
                    "Electronics"
                ]
            },
            "isArchived": false,
            "ownerUserId": 66014640,
            "createdTime": "Sep 03, 2025, 02:19:12 PM",
            "lastModifiedUserId": 66014640,
            "deleted": false,
            "canEdit": false
        },
        {
            "id": "68b84e609cc8a225da9e269d",
            "userId": "shivangi+qa6@sprinklr.com",
            "profileName": "shivi",
            "transactionGroupId": "68adc96c444bb074f1fd28f7",
            "distributionChannel": "SMS",
            "transactionGroupType": "API",
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
        {
            "id": "68b84e609cc8a225da9e269e",
            "userId": "shivangi+qa6@sprinklr.com",
            "profileName": "shivi",
            "transactionGroupId": "68adc96c444bb074f1fd28f7",
            "distributionChannel": "WHATSAPP_BUSINESS",
            "transactionGroupType": "API",
            "customProperties": {
                "orderId": [
                    "ORD-123890"
                ],
                "purchaseAmount": [
                    "500"
                ],
                "purchaseCategory": [
                    "Home_Appliance"
                ]
            },
            "isArchived": false,
            "ownerUserId": 66014640,
            "createdTime": "Sep 03, 2025, 02:19:12 PM",
            "lastModifiedUserId": 66014640,
            "deleted": false,
            "canEdit": false
        }
    ],
    "errors": []
}



## Response Schema













































































| Parameter | Type | Description |
| --- | --- | --- |
| id | string | Unique identifier of the transaction. |
| userId | string | User identifier used in the request. |
| profileName | string | User profile name. |
| transactionGroupId | string | ID of the transaction group. |
| distributionChannel | string | Distribution channel used. |
| transactionGroupType | string | Type of the transaction group. This will always be API. |
| customProperties | object | Custom key-value metadata for the transaction. |
| isArchived | boolean | Status of the transaction (archived or active). |
| ownerUserId | number | Owner user ID who created the transaction. |
| createdTime | string | Timestamp of transaction creation. |
| lastModifiedUserId | number | User ID who last modified the transaction. |
| deleted | boolean | Indicates if the transaction is deleted. |
| canEdit | boolean | Indicates if the transaction can be edited. |

[](https://dev.sprinklr.com/create-transaction)

[Back to top](https://dev.sprinklr.com/create-transaction)
