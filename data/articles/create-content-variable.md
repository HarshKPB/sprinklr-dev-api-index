---
title: "Create Content Variable"
slug: create-content-variable
url: https://dev.sprinklr.com/create-content-variable
---

# Create Content Variable

#  POST Create Content Variable

Use this endpoint to create a new Content Variable. It allows you to define reusable key-value elements that can be referenced across your Knowledge Base content.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/knowledgebase/content-variable

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





























































































































| Parameter | Sub-Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- | --- |
| subType |  | Required | String | The type of Content Variables. Supported Values: PLAIN_TEXT, RICH_TEXT. |
| name |  | Optional | String | The name of the Content Variable. |
| description |  | Optional | String | The description of the Content Variable. |
| conditionalFunctions |  | Required | Array of Objects | The Custom Fields filtering configuration and the Language Settings. |
| filters |  | Optional | Array of Objects | The Custom Field filtering configuration. Refer to the filters table below for more details. |
| countrySpecificLanguageDetails |  | Required | Object | A map where each key is a country code (e.g., "IN") and each value is an object.         Refer to the countrySpecificLanguageDetails table below for more details. |
| ownerUser |  | Optional | Object | Contains identifying and display-related information about the creator of the Content Variable. |
|  | id | Optional | String | A unique internal identifier for the owner user. |
|  | userId | Optional | Integer | The platform-wide user identifier. |
|  | firstName | Optional | String | The first name of the creator. |
|  | lastName | Optional | String | The last name of the creator. |
|  | fullName | Optional | String | The complete name of the owner. |
|  | name | Optional | String | A user-friendly display name of the owner. |
|  | visibleId | Required | String | A user-facing unique identifier. Displayed in UI. |
| createdTime |  | Optional | Integer | The timestamp (Unix epoch milliseconds) when created. |
| modifiedTime |  | Required | Integer | The timestamp (Unix epoch milliseconds) of the most recent update. |

### `filters` Object Description








































































| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| filterType | Optional | String | Logical operator for combining values. Supported: AND, OR. |
| userFilter | Optional | Boolean | Indicates whether the filter is user-defined. |
| allValuesAllowed | Optional | Boolean | Specifies whether the filter can accept any value. |
| lockedWithValues | Optional | Boolean | Locked to a predefined set of enforced values. |
| Hidden | Optional | Boolean | Hides the filter from UI while still active. |
| favourite | Optional | Boolean | Marks as favorite/pinned. |
| mandatory | Optional | Boolean | Indicates whether the filter must be set before executing a query. |
| Locked | Optional | Boolean | Indicates whether the filter is read-only. |
| ignoreAddingToDimensionFilter | Optional | Boolean | Prevents adding this filter to the dimension-level filter set. |
| Details | Optional | Object | Unique identifier of the filter. |

### `countrySpecificLanguageDetails` Object Description






























| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| defaultValue | Optional | String | The default value of the Content Variable. |
| description | Optional | String | Description of the Content Variable for this country. |
| lngVsValue | Required | Object | Language‑specific values used for localization. |

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/content-variable' \
--header 'Authorization: Bearer {Access_Token}' \
--header 'Key: {API_Key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "subType": "RICH_TEXT",
    "name": "RKP test variable API",
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
                    "defaultValue": "This is an API creation test.",
                    "description": "",
                    "lngVsValue": null
                }
            }
        }
    ],
    "ownerUser": {
        "id": "6601127",
        "userId": 66011271,
        "firstName": "Rohan",
        "lastName": "Prasad",
        "fullName": "Rohan Prasad",
        "name": "Rohan Prasad",
        "visibleId": "Rohan Prasad"
    },
    "createdTime": 1769177544296,
    "modifiedTime": 1769177544296
}'

## Example - Response


{ 
    "data": { 
        "id": "6981f625851763543848c37f", 
        "name": "RKP test variable API", 
        "subType": "RICH_TEXT", 
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
                        "details": {}, 
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
                        "defaultValue": "This is an API creation test. updated version", 
                        "description": "" 
                    } 
                } 
            } 
        ], 
        "clientId": 66001165, 
        "ownerUserId": 66011271, 
        "createdTime": "Feb 03, 2026, 01:20:37 PM", 
        "modifiedTime": "Feb 03, 2026, 01:20:37 PM", 
        "lastModifiedUserId": 66011271, 
        "deleted": false, 
        "canEdit": false 
    }, 
    "errors": [] 
}

### Response Schema

























  ********
****
****







































| Parameter | Type | Description |
| --- | --- | --- |
| id | String | The unique identifier of the Content Variable. |
| name | String | The name of the Content Variable. |
| Description | String | The description of the Content Variable. |
| subType | String | The type of Content Variables. Supported Values: PLAIN_TEXT, RICH_TEXT.     Plain Text: Supports unformatted, inline text.     Rich Text: Supports HTML and styling for standalone content. |
| countrySpecificDetails | String | Country-specific configuration details. |
| conditionalFunctions | Array of Objects | The Custom Fields filtering configuration and Language Settings. |
| clientId | Integer | The workspace ID where the Content Variable was added or updated. |
| ownerUserId | Integer | User ID of the Sprinklr user who created the Content Variable. |
| createdTime | String | Timestamp when the Content Variable was created. |
| modifiedTime | String | Timestamp when the Content Variable was last modified. |
| lastModifiedUserId | Integer | User ID of the Sprinklr user who last modified the Content Variable. |
| deleted | Boolean | Indicates whether the Content Variable is deleted. |
| canEdit | Boolean | Indicates whether the Content Variable can be edited. |

[](https://dev.sprinklr.com/create-content-variable)

[Back to top](https://dev.sprinklr.com/create-content-variable)
