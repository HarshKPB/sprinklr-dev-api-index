---
title: "Update Product"
slug: update-product
url: https://dev.sprinklr.com/update-product
---

# Update Product

#
PUT Update Product

You can update a product within Sprinklr via this API call and you will get the Id as response after making the request.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/product/{Id}

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

###  Path Parameters



















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Id | Required | The unique Id of the product. | String |

### Request Parameters
















    [ACCOUNT](https://dev.sprinklr.com/update-product#account)[EXTERNAL](https://dev.sprinklr.com/update-product#external)






















































































































































| Parameter | Sub Parameter | Required/optional | Description | Type |
| --- | --- | --- | --- | --- |
| Source |  | Required | Object containing source details. | Object |
|  | sourceType | Required | The source type can either be ACCOUNT or External. Checkout the tables below for more information on parameter for  and . | String |
| catalogIds |  | Optional | The unique identifiers of the catalogs to which the product belongs within sprinklr. | Array |
| categoryIds |  | Optional | The category of the product.Example: Fragance, Diaper, etc. | Array |
| title |  | Optional | The title of the product. | String |
| description |  | Optional | The description about the product. | String |
| link |  | Optional | The link to product page. | String |
| price |  | Optional | The object containing price details. | Object |
|  | value | Optional | The price of the product. | Double |
|  | currency | Optional | The currency of the product price. | String |
| availability |  | Optional | The availability status of the product. | String |
| inventory |  | Optional | The inventory amount of product. | Integer |
| gtin |  | Optional | The GTin number of the product. | String |
| mpn |  | Optional | The manufaturer part number of product. | String |
| brand |  | Optional | The brand name of product. | String |
| retailerId |  | Optional | The retailer Id of product. | String |
| specification |  | Optional | The object containg product attributes which distinguish a product from its variant. | Object |
| sku |  | Optional | The stock keeping unit of a product. | String |
| groupId |  | Optional | The product group Id which can be used to group variants of a product having with different attributes. | String |
| attachment |  | Optional | The object containing attachment details. | object |
|  | type | Optional | The type of attachment. Example: Image, Video, etc. | String |
|  | url | Optional | The url of the attachment. | String |
| workflow |  | Optional | The object containing workflow properties attached to the product. | Object |
|  | customProperties | Optional | The object containing workflow custom properties. | Object |

###  For Source Type: EXTERNAL
















| Parameter | Required/optional | Description | Type |
| --- | --- | --- | --- |
| sourceType | Required | EXTERNAL | String |
| sourceProductId | Required | The sourceId of the product. | String |

###  For Source Type: ACCOUNT


























| Parameter | Required/optional | Description | Type |
| --- | --- | --- | --- |
| sourceType | Required | ACCOUNT | String |
| sourceId | Required | The source id of the product | String |
| sourceProductId | Required | The sourceId of the product which is unique identifier of product at source. | String |
| channelType | Required | The channel type of the product. | String |

### Example: SourceType - EXTERNAL




 Copy Code


 
curl -X PUT \
   'https://api3.sprinklr.com/{env}/api/v2/product/5ffc8036c6709b68ada97523' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
 {
    "source": {
        "sourceType": "EXTERNAL",
        "sourceProductId": "PE897Ω0524"
    },
     "catalogIds": [
            "ONE"
        ],
    "categoryIds": [
        "FRAG"
    ],
    "title": "The EPIC",
    "link": "https://spriklr.com/pe/p/200897",
    "price": {
        "value": 78.0
    },
    "inventory": 40,
    "specification": {
        "product_type": "PERFUME",
        "cuv": "41",
        "campaign_code": "216",
        "country_iso": "PE"
    },
    "groupId": "20097",
    "attachment": {
        "type": "IMAGE",
        "url": "https://cloudfront.net/PE/202016/05841.jpg"
    },
    "workflow": {
        "customProperties": {
            "OFFER_PRICE_CF_NEW": [
                "2.9"
            ],
            "STRATEGY_CODE_CF_VALUE": [
                "0"
            ]
        }
    }
}'
 

     
     
   

### Example - Response



 
{
    "data": "5ffc8036c6709b68ada97523",
    "errors": []
}
 

     
     
   
 

### Example: SourceType - ACCOUNT




 Copy Code


 
curl -X PUT \
   'https://api3.sprinklr.com/{env}/api/v2/product/5ffc8036c6709b68ada97524' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
    "source": {
        "sourceType": "ACCOUNT",
        "sourceProductId": "PE897Ω0524",
        "sourceId": "2567865",
        "channelType": "FACEBOOK_CHANNEL_TYPE"
    },
     "catalogIds": [
            "ONE"
        ],
    "categoryIds": [
        "FRAG"
    ],
    "title": "The EPIC",
    "link": "https://spriklr.com/pe/p/200897",
    "price": {
        "value": 78.0
    },
    "inventory": 40,
    "specification": {
        "product_type": "PERFUME",
        "cuv": "41",
        "campaign_code": "216",
        "country_iso": "PE"
    },
    "groupId": "20097",
    "attachment": {
        "type": "IMAGE",
        "url": "https://cloudfront.net/PE/202016/05841.jpg"
    },
    "workflow": {
        "customProperties": {
            "OFFER_PRICE_CF_NEW": [
                "2.9"
            ],
            "STRATEGY_CODE_CF_VALUE": [
                "0"
            ]
        }
    }
}'
 

     
     
   

### Example - Response



 
{
    "data": "5ffc8036c6709b68ada97524",
    "errors": []
}
 

     
     
   
 

### Response Parameters









| Parameter | Description | Type |
| --- | --- | --- |
| data | The unique product Id. | String |

	[](https://dev.sprinklr.com/update-product) 

 

 
[Back to top](https://dev.sprinklr.com/update-product)
