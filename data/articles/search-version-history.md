---
title: "Search Version History"
slug: search-version-history
url: https://dev.sprinklr.com/search-version-history
---

# Search Version History

#
  POST - Search Version History


	 Using this API, you can search version history by applying filters.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/search/version-history

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

| Parameters | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| contentIds |  | Optional | List of content Ids you want to search version history for | List [String] |
| sort |  | Optional | Object containing sorting conditions | Object |
|  | key | Optional | Refers to the property on which you want to perform the search.Example: version | String |
|  | order | Optional | Refers to the order in which you want the results to appear, i.e., ascending (ASC) or descending (DESC) | String |
| page |  | Optional | Refers to the object containing pagination information | Object |
|  | page | Optional | Refers to the page number you want the results for.Default:: 0 | Integer |
|  | size | Optional | Refers to the number of results you want in one page result | Integer |

## Example - Request




 Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/search/version-history' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "contentIds": [
        "63cc0f1fddf30d04d8dfc19d"
    ],
    "sort": {
        "key": "version",
        "order": "DESC"
    },
    "page": {
        "page": 0,
        "size": 1
    }
}'
 

     
     
   

**Dev Notes: **For fetching all the available versions for all the articles, send empty curly brackets `{ }` in the API request.

## Example - Response





{
    "data": {
        "searchResults": [
            {
                "id": "643647c93abdff0df2cae10f",
                "contentId": "63cc0f1fddf30d04d8dfc19d",
                "version": 45,
                "title": "Hello world",
                "markUpText": "Hello world markup text",
                "status": "APPROVED",
                "publicContent": false,
                "partnerCustomProperties": {
                    "_c_60e6ef1199ec093f13bf40f5": [
                        "hey You !"
                    ],
                    "_c_62a1cfa93df8d74b0e2846cf": [
                        null
                    ],
                    "_c_62a1cf903df8d74b0e283e57": [
                        "helloooooooooooo"
                    ],
                    "_c_63e69c04986e7106bfef8e29": [
                        null
                    ]
                },
                "ownerUserId": 600038885,
                "createdTime": "Apr 12, 2023, 5:55:21 AM"
            }
        ],
        "hasMore": true,
        "totalHits": 45
    },
    "errors": []
}
 

     
     
   
 
[](https://dev.sprinklr.com/deactivate-account) 

 

 
[Back to top](https://dev.sprinklr.com/deactivate-account)
