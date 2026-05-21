---
title: "Create Custom Field"
slug: create-custom-field
url: https://dev.sprinklr.com/create-custom-field
---

# Create Custom Field

#
POST Create Custom Field

Using this API, you can create a new custom field.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-field

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

-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-

****

| Parameter | Sub-Param | Required/Optional | Definition | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Refers to the data type of the custom field. Supported Data Types: TEXT, PICKLIST, MULTISELECT PICKLIST, NUMBER, DATE, TEXT MULTI, TEXTAREA | String |
| description |  | Optional | The description of the custom field. Note: Should not exceed 500 characters. | String |
| label |  | Required | Label or tag that you want to add to the custom field. | String |
| description |  | Optional | The description of the custom field.Note:Should not exceed 500 characters. | String |
| assetTypes |  | Required | The asset type you want to add the custom field to.Supported Asset Types: Account Outbound Message Message Profile Media Asset User Campaign Sub-Campaign Community Product Paid Initiative Ad Set Ad Variant Case Universal Case Survey Task | String |
| category |  | Optional | Refers to the category you want the custom field to fall under | String |
| enabled |  | Optional | If true, the custom field is enabled | Boolean |
| visibility |  | Optional | Object defining the visibility of the custom field. | Object |
|  | globallyVisible | Optional | If true, the custom field is globally visible. | Boolean |
|  | visibilityConfig | Optional | Array defining the visibility configuration for the custom field.Note:If visibilityConfig is defined, globallyVisible needs to be false. | Array |
| permissions |  | Optional | Array defining the permission levels for the custom field. | Array |
|  | spaceType |  | Refers to the space type where to add the custom field. | String |
|  | spaceId |  | Refers to the space Id where to add the custom field. | Integer |
|  | permissionConfigs |  | Refers to the permission configurations for the custom field.Refer to the table below for array details | Array |
| customFieldControllerById |  | Optional | Object defining the controlling custom field logic. | Object |

### visibilityConfig Array Description Table











****

| Parameter | Required/Optional | Definition | Type |
| --- | --- | --- | --- |
| type | Required | Refers to the type of client/user you want to share the custom field withSupported Values: CLIENT, CLIENT_GROUP, USER, USER_GROUP. | String |
| ids | Optional | The Ids with respect to the type defined. | List [String, Integer] |

### permissionConfigs Array Description Table











****

| Parameter | Required/Optional | Definition | Type |
| --- | --- | --- | --- |
| permissions | Required | Refers to the permissions you want to give to the custom field.Select “ALL” to give all the permissions to the selected group. | List [String] |
| type | Required | Refers to the type of group you want to give permission toSupported Values: CLIENT, CLIENT_GROUP, USER, USER_GROUP. | String |
| ids | Required | The Ids with respect to the type defined. | List [String, Integer] |

### Controlling Logic for Custom Field Object Details

| Parameter | Sub-Param | Sub-Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- | --- |
| id (Only add the value here without adding the parameter) |  |  | Required | The id of the controlling custom field. | Object |
|  | controllingFieldConfig |  | Required | Object defining the controlling custom field logic. | Object |
|  |  | controllingFieldValue (Only add the value here without adding the parameter) | Required | Controlling field value and the list of values that it wants to control from the defined set of controlled custom field , i.e., the values that will be added in the list, its visibility will be dependent on the defined controlling field value.Syntax:"Test1": [1, 2],Where test1 is the controlling field and 1, 2 are the controlled fields. | List[String, Integer] |

**Dev Notes: **When applying the controlling custom field logic, the asset type for both the controlling and controlled custom field should be same.

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/custom-field' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "PICKLIST",
    "description": "API Verification",
    "label": "Deepak Control API V3",
    "assetTypes": [
        "UNIVERSAL_CASE"
    ],
    "values": [
        {
            "key": "test1",
            "label": "test1"
        },
        {
            "key": "test2",
            "label": "test2"
        },
        {
            "key": "test3",
            "label": "test3"
        }
    ],
    "customFieldControllerById": {
        "66b0b924b8f96b59e3003ce3": {
            "controllingFieldConfig": {
                "option 1": [
                    "test1"
                ],
                "option 2": [
                    "test2"
                ]
            }
        }
    },
    "enabled": true,
    "visibility": {
        "globallyVisible": true,
        "visibilityConfig": []
    },
    "permissions": [],
    "optionType": "GENERAL",
    "accessibleClientIds": [
        66000004,
        66000010,
        66000050,
        66000242,
        66000437,
        66000594,
        66000726,
        66000002,
        66000003
    ]
}’






## Example - Response





{
    "data": {
        "id": "66dadcadf4dd0716012c4995",
        "fieldName": "_c_66dadcadf4dd0716012c4990",
        "label": "Deepak Control API v3",
        "description": "API Verification",
        "assetTypes": [
            "CASE"
        ],
        "type": "PICKLIST",
        "values": [
            {
                "key": "test1",
                "label": "test1"
            },
            {
                "key": "test2",
                "label": "test2"
            },
            {
                "key": "test3",
                "label": "test3"
            }
        ],
        "enabled": true,
        "visibility": {
            "globallyVisible": true,
            "visibilityConfig": []
        },
        "permissions": [],
        "optionType": "GENERAL",
        "accessibleClientIds": [
            66000004,
            66000010,
            66000050,
            66000242,
            66000437,
            66000594,
            66000726,
            66000002,
            66000003
        ],
        "createdTime": 1725619373111,
        "modifiedTime": 1725619373111,
        "customFieldControllerById": {
            "66b0b924b8f96b59e3003ce3": {
                "enableReverseMapping": false,
                "controllingFieldConfig": {
                    "option 1": [
                        "test1"
                    ],
                    "option 2": [
                        "test2"
                    ]
                }
            }
        }
    },
    "errors": []
}







### Response Schema


















































































































| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | Object | Main object containing the custom field details. |
|  | id | String | Unique identifier for the custom field. |
|  | fieldName | String | Internal name of the custom field. |
|  | label | String | Display label for the custom field. |
|  | description | String | Description of the custom field. |
|  | assetTypes | Array of Strings | Array of asset types the custom field is associated with. |
|  | type | String | Data type of the custom field. |
|  | values | Array of Objects | Array of key-value pairs representing the picklist options. |
|  | enabled | Boolean | Boolean indicating if the custom field is enabled. |
|  | visibility | Object | Object defining the visibility of the custom field. |
|  | permissions | Array of Objects | Array defining the permission levels for the custom field. |
|  | optionType | String | Type of the option |
|  | accessibleClientIds | Array of Integers | Array of client IDs that can access the custom field. |
|  | createdTime | Integer | Timestamp of when the custom field was created. |
|  | modifiedTime | Integer | Timestamp of when the custom field was last modified. |
|  | customFieldControllerById | Object | Object defining the controlling custom field logic. |
| errors |  | Array of Objects | Array of error objects, if any. |

	[](https://dev.sprinklr.com/create-custom-field) 

 

 
[Back to top](https://dev.sprinklr.com/create-custom-field)
