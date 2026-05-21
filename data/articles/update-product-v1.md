---
title: "Update Product v1"
slug: update-product-v1
url: https://dev.sprinklr.com/update-product-v1
---

# Update Product v1

#
  POST - Update Product

Using this API, you can update the custom properties of the product.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v1/universal-commerce/product/update/{productId}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/getting-started)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

## Path Parameter














| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| productid |  | Refers to the unique identifier for the product for which the custom properties need to be updated | String |

## Request Parameters












****

-
-
-

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| partnerCustomProperties | Required | Refers to the key and value pair of the custom property name and its corresponding valueNotes:Kindly note that the custom property should belong to the universal product asset classThe existing values of the custom property will be overridden if not passed in the request payloadPassing empty quotes will unset the custom property value altogether | Object |

### Example - Request




 Copy Code


curl -X POST \
  https://api3.sprinklr.com/{env}/api/v1/universal-commerce/product/update/65e5cc2efcac603b0b7a82b1 '\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "partnerCustomProperties" : {
        "_c_65deece46f327f2948956149" : ["Test1", "Test2"]
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
            "NN1",
            "NN2"
        ]
    },
    "delisted": false,
    "customProperties": {
        "flatCustomProperties": [
            "ALL",
            "ALLµ_c_65deece46f327f2948956149",
            "ALLµ_c_65deece46f327f2948956149µNN2",
            "ALLµ_c_65deece46f327f2948956149µNN1"
        ],
        "customPropertyNames": [
            "_c_65deece46f327f2948956149"
        ],
        "mappedCustomProperties": {
            "_c_65deece46f327f2948956149": [
                "NN1",
                "NN2"
            ]
        },
        "mappedControllingCustomPropertyList": [],
        "customProperties": [
            {
                "key": "_c_65deece46f327f2948956149",
                "values": [
                    "Test1",
                    "Test2"
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
    "modifiedTime": 1709559577542,
    "lastModifiedUserId": 1000157828,
    "deleted": false,
    "canEdit": false
}





[](https://dev.sprinklr.com/update-product-v1)




[Back to top](https://dev.sprinklr.com/update-product-v1)
