---
title: "Fetch Content Variable by Id"
slug: fetch-content-variable-by-id
url: https://dev.sprinklr.com/fetch-content-variable-by-id
---

# Fetch Content Variable by Id

#  GET  Fetch Content Variable by Id

Use this endpoint to fetch the details of a specific Content Variable using its unique ID. This is helpful when you need to view or reference a single variable in detail.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/knowledgebase/content-variable/`{id}`

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

## Path Parameter

















| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| id | Required | String | The unique identifier of the Content Variable. |

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/content-variable/6937e59326a51f27fb798144' \
--header 'Authorization: Bearer {Access_Token}'
--header 'Key: {API_Key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \

## Example - Response


{ 
    "data": { 
        "id": "6937e59326a51f27fb798144", 
        "name": "RKP Test 26.1", 
        "description": "RKP Test 26.1", 
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
                            "__id": "3f248500-6258-48ee-b3a2-8482a8eb3449" 
                        }, 
                        "filters": [ 
                            { 
                                "filterType": "IN", 
                                "field": "_c_650aa3028dce2e4cbe45ccc9", 
                                "values": [ 
                                    "Yes" 
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
                    "global": { 
                        "defaultValue": "12", 
                        "description": "", 
                        "lngVsValue": { 
                            "az": { 
                                "value": "14", 
                                "mobileValue": "13.5" 
                            } 
                        } 
                    } 
                } 
            } 
        ], 
        "clientId": 66000002, 
        "ownerUserId": 66011271, 
        "createdTime": "Dec 09, 2025, 09:02:11 AM", 
        "modifiedTime": "Feb 02, 2026, 10:39:44 AM", 
        "lastModifiedUserId": 66011271, 
        "deleted": false, 
        "canEdit": false 
    }, 
    "errors": [] 
}

## Response Parameters

### Top-Level Response



















  **




  ``



| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | Object | Container for paginated results. |
|  | results | Array of Objects | See the results table below. |
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

[](https://dev.sprinklr.com/fetch-content-variable-by-id)

[Back to top](https://dev.sprinklr.com/fetch-content-variable-by-id)
