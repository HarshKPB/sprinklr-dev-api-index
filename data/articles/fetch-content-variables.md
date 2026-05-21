---
title: "Fetch Content Variables"
slug: fetch-content-variables
url: https://dev.sprinklr.com/fetch-content-variables
---

# Fetch Content Variables

#  GET  Fetch Content Variables

This endpoint retrieves a paginated list of Content Variables. It is useful for browsing, filtering, and managing large sets of variables efficiently without overloading the response payload.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/knowledgebase/content-variable/search

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



































  ``























  ````



| Parameters | Sub-Parameters | Required/Optional | Type | Description |
| --- | --- | --- | --- | --- |
| page |  | Optional | Object | Limits the number of items returned when the response size is large. |
|  | page | Optional | Integer | Specifies the page number to return. Defaults to the first page if not provided. |
|  | size | Required | Integer | Specifies the maximum number of results returned in a single response. |
| returnTotalCount |  | Required | Boolean | Whether to return the total number of matching content variables (totalCount). |
| query |  | Optional | String | Optional search query. When empty, returns all content variables (subject to permissions). |
| sort |  | Required | Array of Objects | List of sort criteria. |
|  | key | Required | String | Field name to sort by. |
|  | order | Required | String | Sort order: ASC for ascending or DESC for descending. |

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/knowledgebase/content-variable/search' \ 
--header 'Authorization: Bearer {Access_token}' \ 
--header 'Key: {API_KEY}' \ 
--header 'Content-Type: application/json' \ 
--header 'Accept: application/json' \ 
--data '{ 
  "page": { 
    "page": 1, 
    "size":2 
 
  }, 
  "returnTotalCount": true, 
  "query": "", 
  "sort": [ 
    { 
      "key": "modifiedTime", 
      "order": "DESC" 
    } 
  ] 
}'

## Example - Response


{ 
    "data": { 
        "results": [ 
            { 
                "id": "697ae04fda8fb75dd25c3d0b", 
                "name": "PlaintextSingleSelectCFInvalidValueAPI", 
                "subType": "PLAIN_TEXT", 
                "countrySpecificDetails": {}, 
                "conditionalFunctions": [ 
                    { 
                        "filters": [ 
                            { 
                                "filterType": "AND", 
                                "userFilter": false, 
                                "allValuesAllowed": true, 
                                "lockedWithValues": false, 
                                "hidden": false, 
                                "favourite": false, 
                                "mandatory": false, 
                                "locked": false, 
                                "ignoreAddingToDimensionFilter": false, 
                                "details": { 
                                    "__id": "e5c91512-619c-4b2c-967d-ed933c5d85d9" 
                                }, 
                                "filters": [ 
                                    { 
                                        "filterType": "IN", 
                                        "field": "_c_67692a9b01cb805e3f417320", 
                                        "values": [ 
                                            "abc" 
                                        ], 
                                        "userFilter": false, 
                                        "allValuesAllowed": true, 
                                        "lockedWithValues": false, 
                                        "hidden": false, 
                                        "favourite": false, 
                                        "mandatory": false, 
                                        "locked": false, 
                                        "ignoreAddingToDimensionFilter": false, 
                                        "details": {} 
                                    } 
                                ] 
                            } 
                        ], 
                        "countrySpecificLanguageDetails": { 
                            "IN": { 
                                "defaultValue": "10", 
                                "description": "" 
                            } 
                        } 
                    } 
                ], 
                "clientId": 66001165, 
                "ownerUserId": 66014646, 
                "createdTime": "Jan 29, 2026, 04:59:21 AM", 
                "modifiedTime": "Jan 29, 2026, 04:59:21 AM", 
                "lastModifiedUserId": 66014646, 
                "deleted": false, 
                "canEdit": false 
            }, 
            { 
                "id": "697ae021da8fb75dd25c3cf1", 
                "name": "PlaintextSingleSelectCF", 
                "subType": "PLAIN_TEXT", 
                "countrySpecificDetails": {}, 
                "conditionalFunctions": [ 
                    { 
                        "filters": [ 
                            { 
                                "filterType": "AND", 
                                "userFilter": false, 
                                "allValuesAllowed": true, 
                                "lockedWithValues": false, 
                                "hidden": false, 
                                "favourite": false, 
                                "mandatory": false, 
                                "locked": false, 
                                "ignoreAddingToDimensionFilter": false, 
                                "details": { 
                                    "__id": "e5c91512-619c-4b2c-967d-ed933c5d85d9" 
                                }, 
                                "filters": [ 
                                    { 
                                        "filterType": "IN", 
                                        "field": "_c_67692a9b01cb805e3f417320", 
                                        "values": [ 
                                            "abc" 
                                        ], 
                                        "userFilter": false, 
                                        "allValuesAllowed": true, 
                                        "lockedWithValues": false, 
                                        "hidden": false, 
                                        "favourite": false, 
                                        "mandatory": false, 
                                        "locked": false, 
                                        "ignoreAddingToDimensionFilter": false, 
                                        "details": {} 
                                    } 
                                ] 
                            } 
                        ], 
                        "countrySpecificLanguageDetails": { 
                            "IN": { 
                                "defaultValue": "10", 
                                "description": "" 
                            } 
                        } 
                    } 
                ], 
                "clientId": 66000002, 
                "ownerUserId": 66014646, 
                "createdTime": "Jan 29, 2026, 04:20:49 AM", 
                "modifiedTime": "Jan 29, 2026, 04:58:47 AM", 
                "lastModifiedUserId": 66014646, 
                "deleted": false, 
                "canEdit": false 
            } 
        ], 
        "hasMore": true, 
        "totalCount": 1502 
    }, 
    "errors": [] 
}

## Response Parameters

### Top-Level Response



















  **







  ****




  ``



| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | Object | Container for paginated results. |
|  | results | Array of Objects | See the results table below. |
| hasMore | Boolean | Indicates whether additional pages of results are available. |  |
| totalCount | Integer | Total number of records. Shown only if returnTotalCount=true     in the request. |  |
| errors |  | Array | List of errors, if any. Empty ([]) on success. |

### results Array of Objects

























********

****
****







































| Parameter | Type | Description |
| --- | --- | --- |
| id | String | The unique identifier of the Content Variable. |
| name | String | The name of the Content Variable. |
| description | String | The description of the Content Variable. |
| subType | String | Type of Content Variable.     Supported: PLAIN_TEXT, RICH_TEXT.     Plain Text: Unformatted, inline text.     Rich Text: Supports HTML and styling for standalone content. |
| countrySpecificDetails | String | Country-specific configuration details. |
| conditionalFunctions | Array of Objects | Filtering configuration and language settings. |
| clientId | Integer | ID of the workspace where the Content Variable exists. |
| ownerUserId | Integer | User ID of the creator. |
| createdTime | String | Creation timestamp. |
| modifiedTime | String | Last updated timestamp. |
| lastModifiedUserId | Integer | User ID of the last modifier. |
| deleted | Boolean | Indicates whether the Content Variable is deleted. |
| canEdit | Boolean | Indicates whether the Content Variable is editable. |

### conditionalFunctions Array Description













































































| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| filters |  | Array of Objects | The Custom Field filtering configuration. |
|  | filterType | String | Logical operator: AND, OR, IN. |
|  | userFilter | Boolean | Indicates whether the filter is user-defined. |
|  | allValuesAllowed | Boolean | Whether any value is accepted. |
|  | lockedWithValues | Boolean | Restricts to enforced predefined values. |
|  | Hidden | Boolean | Hides the filter from UI. |
|  | favourite | Boolean | Marks filter as favorite. |
|  | mandatory | Boolean | Indicates if the filter is required. |
|  | Locked | Boolean | Indicates if the filter is read-only. |
|  | ignoreAddingToDimensionFilter | Boolean | Prevents adding to dimension-level filter sets. |
|  | Details | Object | Unique identifier of the filter. |
| countrySpecificLanguageDetails |  | Object | Map of country codes to localized configuration. |
|  | defaultValue | String | The default value of the Content Variable. |
|  | description | String | Description of the filter. |
|  | lngVsValue | Object | Language-specific values. |

### lngVsValue Object Description




















| Parameter | Type | Description |
| --- | --- | --- |
| value | String | The value of the Content Variable for the selected language. |
| mobileValue | String | The value used in mobile interfaces. |

[](https://dev.sprinklr.com/fetch-content-variables)

[Back to top](https://dev.sprinklr.com/fetch-content-variables)
