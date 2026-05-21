---
title: "Fetch Custom Field Using Field Name"
slug: fetch-custom-field-using-field-name
url: https://dev.sprinklr.com/fetch-custom-field-using-field-name
---

# Fetch Custom Field Using Field Name

#
GET Fetch Custom Field Using Field Name

This API call helps in fetching the custom field details using the corresponding field name.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-field/{customFieldName}


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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameter

















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| customFieldName | Required | The unique name of the custom field. You can either fetch this custom field name from the create custom field response or you can copy this from the UI too.Steps to fetch custom field from are mentioned below | String |

**Steps to Extract Custom Field Name from UI: **

- Click on the hamburger menu on the top left corner on Sprinklr platform's homepage
- Navigate to All Settings Options
- Click on the "Custom Fields" Icon within "Manage Workspace" module
- Click on the three dots placed alongside the respective custom field
- Click on "Copy Field Name" option from the drop-down menu
- Use this field name in the API request path parameters



## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/custom-field/_c_62fc7b88b893784e3db68fa1' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
   

## Example - Response

 
 
     
 
   {
    "data": {
        "id": "62fc7b88b893784e3db68fa6",
        "fieldName": "_c_62fc7b88b893784e3db68fa1",
        "label": "profile check",
        "assetTypes": [
            "PROFILE"
        ],
        "type": "PICKLIST_MULTISELECT",
        "values": [
            {
                "key": "Tag",
                "label": "Tag"
            },
            {
                "key": "Tag1",
                "label": "Tag1"
            }
        ],
        "category": "",
        "enabled": true,
        "visibility": {
            "globallyVisible": true,
            "visibilityConfig": []
        },
        "permissions": []
    },
    "errors": []
}
 

     
     
   
 

### Response Parameters







































****

-
-
-
-
-
-
-

























































| Parameter | Sub-Param | Definition | Type |
| --- | --- | --- | --- |
| id |  | Unique identifier for the custom field | String |
| fieldName |  | The name of the custom field | String |
| label |  | Refers to the label that is set for the custom field | String |
| assetTypes |  | The asset types the custom field is related to | List [String] |
| type |  | Refers to the custom field typeSupported Types:PICKLIST MULTISELECT: for selecting more than one valuePICKLIST: for selecting only one value NUMBER: for selecting value in the numerical formDATE: value will be in date-type formatTEXT MULTI: no need to define values when creating assets. You can create values on the goTEXT: add values in textual format TEXT AREA: for adding values in textual format and can support lengthy text format | String |
| values |  | Array defining the corresponding values of the custom field | Array |
|  | key | The value of the custom field | String |
|  | label | The label set for the custom field value | String |
| category |  | Refers to the category under which the custom field is defined | String |
| enabled |  | If yes, the custom field is enabled. Else, it is disabled | Boolean |
| visibility |  | Object defining the visibility details of the custom field | Object |
|  | globallyVisible | If True, the Custom Field will be visible across all users and across workspaces | Boolean |
|  | visibilityConfig | Defines the custom visibility configurations for the custom field (if any) | list[String] |
| permissions |  | Defines the different permission levels set for the custom field | List [String] |

	[](https://dev.sprinklr.com/fetch-custom-field-using-field-name) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-custom-field-using-field-name)
