---
title: "Read Product"
slug: read-product
url: https://dev.sprinklr.com/read-product
---

# Read Product

#
GET Read Product

You can fetch a product and all related objects via this api using the unique identifier Id of the product within sprinklr.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/product/{Id}

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

### Path Parameters



















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Id | Required | The unique Id of the product. | String |

## Example

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X GET \
   'https://api3.sprinklr.com/{env}/api/v2/product/5ffc72931b36a02632e347a8' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Typ: application/json'
 

     
     
   

## Example - Response

 
 
     
 
{
    "data": {
        "id": "5ffc72931b36a02632e347a8",
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
        "type": "IMAGE"
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
},
    "errors": []
}
 

     
     
   
 
[Click here](https://dev.sprinklr.com/create-product) for response definitions.

	[](https://dev.sprinklr.com/read-product) 

 

 
[Back to top](https://dev.sprinklr.com/read-product)
