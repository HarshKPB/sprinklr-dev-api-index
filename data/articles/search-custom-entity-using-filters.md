---
title: "Search Custom Entity using Filters"
slug: search-custom-entity-using-filters
url: https://dev.sprinklr.com/search-custom-entity-using-filters
---

# Search Custom Entity using Filters

#   POST Search Custom Entity using Filters
 

This API helps fetch the custom entities based on the passed filter values and conditions.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/search/{entityType}

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











			[custom entity definition](https://dev.sprinklr.com/create-entity-definition)

****




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityDefinitionId | Required | The type of entity, i.e., the unique id of the Example: _c_caller | String |

### Request Parameters






































| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| filter | Required | Filter to be applied on the custom entity type.Refer to the table below for filter object parameters description | Object |
| sort | Optional | The array of objects that contain the query details. Refer to the table below for sort array parameters description | Array |
| page | Optional | Object defining pagination information. Refer to the table below for page object parameters description | Object |
| returnTotalCount | Optional | If true, it returns the number of searched entities in the response | Boolean |

### filter Object Description Table


















| Parameters | Sub-Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| filterType |  | Required | Refers to the applied filter type.Supported filter types:AND, OR, NOT, IN, GT, GTE, LT, LTE, NIN, EQUALS, NOT_EQUALS, CONTAINS | String |
| filters |  | Required | Array defining the filter conditions for custom entity fields | Array |
|  | filterType | Required | The type of filter for the given custom entity field | String |
|  | field | Required | Refers to the custom entity field | String |
|  | values | Required | Refers to the value stored for the given custom entity field | List[Integer] |

### sort Array Description Table















****

********



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| key | Optional | Refers to the parameter based on which you need to search custom entity | String |
| order | Required if the key is defined | Determines whether to sort the search results in ascending or descending orderSupported Values:ASC: for ascendingDESC: for descending | String |

### page Object Description Table

















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| page | Optional | Page helps specify the page number you want in the response. If no page number is provided, the first page results are displayed by default. | Integer |
| size | Optional | Refers to the number of results that will be shown in the response | Integer |

## Example - Request




 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/custom-entity/search/_c_caller’  \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
   "query": {
       "filter": {
           "filterType": "AND",
           "filters": [
               {
                   "filterType": "IN",
                   "field": "_c_credit_score",
                   "values": [
                       20
                   ]
               }
           ]
       },
       "sort": [
           {
               "key": "createdTime",
               "order": "DESC"
           }
       ],
       "page": {
           "page": 0,
           "size": 50
       },
       "returnTotalCount": true
   }
}'



## Example - Response





{
    "data": {
        "results": [
            {
                "id": "63106c5a9299522cd890e0dc",
                "entityId": "Test1",
                "name": "Test2",
                "type": "_c_caller",
                "values": {
                    "_c_credit_score": 20
                },
                "createdTime": "Thu Sep 01 09:05:20 UTC 2022",
                "createdTimeInMillis": 1662023120322,
                "modifiedTime": "Thu Sep 01 09:05:20 UTC 2022",
                "modifiedTimeInMillis": 1662023120322
            },
            {
                "id": "62f26e2be13d6a631e5aec12",
                "entityId": "62f26e2be13d6a631e5aec12",
                "name": "Test",
                "type": "_c_caller",
                "values": {
                    "_c_credit_score": 20,
                    "_c_customer_bio": "fgt",
                    "_c_rating": 3
                },
                "createdTime": "Tue Aug 09 14:24:43 UTC 2022",
                "createdTimeInMillis": 1660055083844,
                "modifiedTime": "Wed Jan 04 07:40:48 UTC 2023",
                "modifiedTimeInMillis": 1672818048847
            }
        ],
        "hasMore": false,
        "totalCount": 2
    },
    "errors": []
}



### Response Parameters













| Parameters | Sub-Param | Description | Type |
| --- | --- | --- | --- |
| results |  | Array describing the response parameters | Array |
|  | id | Refers to the unique identifier for the custom entity | String |
|  | entityId | Configured from client-side and needs to be unique for every entity. The entity Id is a unique reference for the entity that helps identifying the created entity | String |
|  | name | Refers to the API name of the custom entity | String |
|  | type | Refers to the custom entity definition Id | String |
|  | values | Object defining custom entity field and its corresponding value pair | Object |
|  | createdTime | The time at which the custom entity was created | String |
|  | createdTimeInMillis | The time at which the custom entity was created (in milliseconds) | Integer |
|  | modifiedTime | The time at which the custom entity was last modified | String |
|  | modifiedTimeInMillis | he time at which the custom entity was last modified (in milliseconds) | Integer |
| hasMore |  | If true, there are more results that match the filter but are not shown in the response | Boolean |
| totalCount |  | Refers to the total counts of results that match the filters applied | Integer |

[](https://dev.sprinklr.com/search-custom-entity-using-filters) 

 

 
[Back to top](https://dev.sprinklr.com/search-custom-entity-using-filters)
