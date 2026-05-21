---
title: "Fetch Product Set "
slug: fetch-product-set
url: https://dev.sprinklr.com/fetch-product-set
---

# Fetch Product Set 

#   GET Fetch Product Set


In Sprinklr Product Catalog, you can make changes to improve the functionality in the Product Catalog screen to edit a product set, see what products make up a product set and email notifications based on diagnostics for Product Catalogs.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/productSets/`{catalogChannelId}`

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


















| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| catalogChannelId | Required | String | Unique ID of the required Product Set. |

## Example - Request




 Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/productSets/{catalogChannelId}’ \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'key: {Enter Your API Key}'



## Example - Response





{
  "data": {
    "responseEntities": [
      {
        "channelId": "0903fac1-e169-4fbf-862a-907eb39a102f",
        "catalogChannelId": "791f74f3-c59f-44e0-a28c-63d1a11d2034",
        "businessChannelId": "25820d7d-8a90-4499-8dae-d7fae3246015",
        "productIds": [
          "9036910323376196358",
          "8685050597613790838",
          "5871167860751799650"
        ],
        "productCount": 3,
        "vertical": "COMMERCE",
        "channelType": "SNAPCHAT",
        "stringifiedRule": "",
        "id": "SNAPCHAT_0903fac1-e169-4fbf-862a-907eb39a102f",
        "name": "All Products",
        "deleted": false,
        "modifiedTime": 1754319082083,
        "createdTime": 1683029905424
      }
    ]
  },
  "errors": []
}




### Response Parameters



























| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | Array | Contains the main data objects. |
|  | responseEntities | Array of Objects | Details of the response received. |
| errors |  | Array | List of errors, if any. |


### responseEntities Description Table









































































| Parameter | Type | Description |
| --- | --- | --- |
| channelId | String | Channel ID associated with the Product Set. |
| catalogChannelId | String | Unique ID of the required Product Set. |
| businessChannelId | String | Business Channel ID associated with the Product Set. |
| productIds | Array of Integers | IDs of the products under the Product Set. |
| productCount | Integer | Number of products under the Product Set. This will be equal to the number of Product IDs listed. |
| Vertical | String |  |
| channelType | String | Name of the channel for the Product Set has been created. |
| stringifiedRule |  |  |
| Id | String | Catalog Channel ID with the Channel Type as prefix. |
| name | String | Name of the Product Set. |
| deleted | Boolean | Indicates whether the parameter has been deleted (true) or is still active (false). |
| modifiedTime | Integer | Shows the epoch timestamp when the Product Set was last modified. |
| createdTime | Integer | Shows the epoch timestamp when the Product Set was created. |

[](https://dev.sprinklr.com/fetch-product-set) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-product-set)
