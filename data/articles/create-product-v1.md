---
title: "Create Product v1"
slug: create-product-v1
url: https://dev.sprinklr.com/create-product-v1
---

# Create Product v1

#
  POST - Create Product

Using this API, you can add a product within an existing product catalog.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v1/universal-commerce/product/create

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

[channel type](https://dev.sprinklr.com/channels-v1)

| Parameter | Sub Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| source |  | Required | Refers to the object containing the product source details | Object |
|  | sourceType | Required | Refers to the source type of the productSupported Values:ACCOUNT | String |
|  | sourceProductId | Required | Refers to the unique identifier for the product added and should be a client generated field.Kindly note that for every product, the product Id should be unique, else the APi will throw an error | String |
|  | sourceId | Required | Refers to the account Id associated with the mentioned channel type | String |
|  | channelType | Required | Refers to the  from where the product is being sourced | String |
| catalogIds |  | Required | Refers to the unique identifier where the product needs to be added | String |
| title |  | Required | Refers to the name of the product | String |
| price |  | Required | Refers to the listed price of the product | Integer |
| partnerCustomProperties |  | Optional | Refers to the key and value pair of the custom property name and its corresponding valueKindly note that the custom property should belong to the universal product asset class | Object |

### Example - Request




 Copy Code


curl -X POST \
  https://api3.sprinklr.com/{env}/api/v1/universal-commerce/product/create \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "source": {
        "sourceType": "ACCOUNT",
        "sourceProductId": "FPK.VN25.MCC01.5",
        "sourceId" : "1000136429",
        "channelType" : "FACEBOOK"
    },
    "catalogIds" : ["65d33bf1d10280313c668fdf"],
    "title": "Testing API",
    "price": 1300.0,
    "partnerCustomProperties" : {
        "_c_65deece46f327f2948956149" : "Test 123"
    }
}'





### Example - Response




{
    "id": "65e5cc2efcac603b0b7a82b1",
    "pS": {
        "sTp": "ACCOUNT",
        "sId": "1000136429",
        "spId": "FPK.VN25.MCC01.5",
        "snT": "FACEBOOK"
    },
    "ctId": [
        "65d33bf1d10280313c668fdf"
    ],
    "title": "Testing API",
    "prc": 1300.0,
    "pCp": {
        "_c_65deece46f327f2948956149": [
            "Test 123"
        ]
    },
    "delisted": false,
    "customProperties": {
        "flatCustomProperties": [
            "ALL",
            "ALLµ_c_65deece46f327f2948956149µTest 123",
            "ALLµ_c_65deece46f327f2948956149"
        ],
        "customPropertyNames": [
            "_c_65deece46f327f2948956149"
        ],
        "mappedCustomProperties": {
            "_c_65deece46f327f2948956149": [
                "Test 123"
            ]
        },
        "mappedControllingCustomPropertyList": [],
        "customProperties": [
            {
                "key": "_c_65deece46f327f2948956149",
                "values": [
                    "Test 123"
                ]
            }
        ]
    },
    "grants": [
        "CLIENT/1000004509/OWNERSHIP",
        "USER/1000157828/OWNERSHIP"
    ],
    "clientId": 1000004509,
    "ownerUserId": 1000157828,
    "createdTime": 1709558830560,
    "modifiedTime": 1709558830560,
    "deleted": false,
    "canEdit": false
}





[](https://dev.sprinklr.com/create-product-v1)




[Back to top](https://dev.sprinklr.com/create-product-v1)
