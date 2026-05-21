---
title: "Create Product"
slug: create-product
url: https://dev.sprinklr.com/create-product
---

# Create Product

#
POST Create Product


You can create a product within Sprinklr via this API call and you will get the Id and other related objects as response after making the request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/product

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

### Request Parameters
























****








****

































































































































| Parameter | Sub Parameter | Required/optional | Description | Type |
| --- | --- | --- | --- | --- |
| Source |  | Required | Object containing source details. | Object |
|  | sourceType | Required | Refers to the source type for which the product will be createdSupported Value:ACCOUNT | String |
|  | channelType | Required | Refers to the channel type with reference to which the product is being createdSupported Values:SOURCE_AGNOSTIC | String |
|  | sourceProductId | Required | Refers to the unique identifier for the product. This is client-generated | String |
| catalogId |  | Required | Refers to the unique identifier for the catgory you want to add the product to | String |
| categoryIds |  | Optional | Refers to the unique identifier for the product category. This is client-side generated field | String |
| title |  | Optional | The title of the product | String |
| description |  | Optional | Refers to the description of the product | String |
| link |  | Optional | Refers to the link of the product | String |
| price |  | Optional | Refers to the object containing price details | Object |
|  | value | Required | Refers to the price of the object | Double |
|  | currency | Optional | Refers to the currency of the product price | String |
| availability |  | Optional | Refers to inventory status of the product | String |
| brand |  | Optional | Refers to the brand name of product | String |
| specification |  | Optional | The key and value pair object containing the additional contextual parameters for the product that help distinguish it from its variants. These details will be displayed besides the product image | Object |
| groupId |  | Optional | The product group Id which can be used to group variants of a product having with different attributes | String |
| attachment |  | Optional | The object containing attachment details. | object |
|  | type | Optional | The type of attachment. Example: Image, Video, etc. | String |
|  | url | Optional | The url of the attachment. | String |
| workflow |  | Optional | The object containing workflow properties attached to the product. | Object |
|  | customProperties | Optional | The key and value pair object containing universal product custom properties that you need to associate with the product | Object |

**Steps to Extract Catalog Id from UI: **

- Open a new tab on Sprinklr platform's homepage
- Search "Product Catalog"

- Search the product catalog you want to add the product to
- Click on the three dots placed alongside the respective catalog and click on open

- The catalog Id will be embedded in the browser URL
- Browser URL example: https://space-prod0.sprinklr.com/social/product-catalog/632866b24423b4217dd08a0b/products. The catalog Id: 632866b24423b4217dd08a0b

## Example: SourceType - ACCOUNT

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
		curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/product' \
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
        "channelType": "SOURCE_AGNOSTIC"
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
            "_c_62b2f38107fc693d373ea40e": [
                "nnlb"
            ],
            "_c_5fa41eba513a9e238d7a810a": [
                "New"
            ]
        }
    }
}'
 

     
     
   

## Example - Response

 
 
     
 
{
    "data": {
        "id": "66dfe693d2617770598181e5",
        "source": {
            "sourceType": "ACCOUNT",
            "sourceProductId": "PE897Ω0524",
            "channelType": "SOURCE_AGNOSTIC"
        },
        "catalogIds": [
            "5f981c65d1cce029d67b09d2"
        ],
        "categoryIds": [
            "FRAG"
        ],
        "title": "sonos_catalog_additional",
        "description": "Sample Description",
        "link": "https://sprinklr.com/pe/p/200897",
        "price": {
            "value": 78.0,
            "currency": "INR"
        },
        "availability": "Yes",
        "inventory": 40,
        "gtin": "sample",
        "mpn": "manufacter_part_number",
        "brand": "loreal",
        "retailerId": "1234",
        "specification": {
            "product_type": "PERFUME",
            "cuv": "41",
            "campaign_code": "216",
            "country_iso": "PE"
        },
        "sku": "100",
        "groupId": "20097",
        "attachment": {
            "url": "https://cloudfront.net/PE/202016/05841.jpg",
            "type": "IMAGE"
        },
        "workflow": {
            "customProperties": {
                "_c_62b2f38107fc693d373ea40e": [
                    "nnlb"
                ],
                "_c_5fa41eba513a9e238d7a810a": [
                    "New"
                ]
            }
        },
        "delisted": false
    },
    "errors": []
}
 

     
     
   
 

### Response Parameters
















































































































































| Parameter | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | The unique product Id within Sprinklr. | String |
| Source | Required | Object containing source details. | Object |
|  | sourceType | The source type can either be ACCOUNT or External. Checkout the tables below for more information on response parameter for ACCOUNT and EXTERNAL | String |
| catalogIds |  | The unique identifiers of the catalogs to which the product belongs within sprinklr. | Array |
| categoryIds |  | The category of the product.Example: Fragance, Diaper, etc. | Array |
| title |  | The title of the product. | String |
| description |  | The description about the product. | String |
| link |  | The link to product page. | String |
| price |  | The object containing price details. | Object |
|  | value | The price of the product. | Double |
|  | currency | The currency of the product price. | String |
| availability |  | The availability status of the product. | String |
| inventory |  | The inventory amount of product. | Integer |
| brand |  | The brand name of product. | String |
| specification |  | The object containg product attributes which distinguish a product from its variant. | Object |
| sku |  | The stock keeping unit of a product. | String |
| groupId |  | The product group Id which can be used to group variants of a product having with different attributes. | String |
| attachment |  | The object containing attachment details. | object |
|  | type | The type of attachment. Example: Image, Video, etc. | String |
|  | url | The url of the attachment. | String |
| workflow |  | The object containing workflow properties attached to the product. | Object |
|  | customProperties | The object containing workflow custom properties. | Object |

	[](https://dev.sprinklr.com/create-product) 

 

 
[Back to top](https://dev.sprinklr.com/create-product)
