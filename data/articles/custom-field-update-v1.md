---
title: "Custom Field Update v1"
slug: custom-field-update-v1
url: https://dev.sprinklr.com/custom-field-update-v1
---

# Custom Field Update v1

#
PUT - Custom Field Update


You can update a Custom Field via this API call. After making the PUT Request you will get 204 (No Content) as Response.

## API Endpoint

https://api3.sprinklr.com`/{{env}}/`api/v1/customfield/{id}

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

## Path Parameters







[create custom field API](https://dev.sprinklr.com/create-custom-field)[search custom field API](https://dev.sprinklr.com/custom-field-search-v1)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | The unique identifier for the custom field. This is the Id you received in the  response. You can also use the  to look for the associated custom field Ids. | String |

## Request Parameters







| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| assetClassList | Required | Assets classes to which the custom fields will be related. The Asset classes are Account, Outbound Message, Message, Profile, Media Asset, User, Workspace (Client), Campaign, Community Product, Paid Initiative, Ad Set, Ad Variant, Case, and Task. | List<String> |
| fieldType | Optional | Custom Field Type. You can select from PICKLIST MULTISELECT, PICKLIST, NUMBER, DATE, TEXT MULTI, TEXT AREA, OR TEXT. | List<String> |
| name | Required | Name of the custom field. | String |
| globalAsset | Optional | If True, the Custom Field will be visible across all workspaces in the respective partner environment. | Boolean |
| description | Optional | Description of the custom field. Not exceeding 500 characters. | String |
| helpText | Optional | Help text for the custom field. This additional information related to the custom field will appear for the user in the UI. | String |
| options | Optional | List of options. Applicable for PICKLIST field types. | List<String> |
| defaultValue | Optional | The default value of the custom field. | String |
| optionsLabels | Optional | Names of the options. These will be reflecting in the UI. | List<String> |
| category | Optional | Category of the custom field. | String |
| enabled | Optional | Is the Enabled or Disabled. | Boolean |
| order | Optional | The ordering of the custom field. | int |
| isHidden | Optional | If TRUE, this field will not be available on Engagement and Reporting Dashboard and in the UI. | Boolean |
| required | Optional | Controls whether the custom field is mandatory or not. | Boolean |

### Example - Request

 Copy Code



curl -X PUT \
'https://api3.sprinklr.com/{env}/api/v1/customfield/5b1559e4e4b002f5a048e07f' \
-H 'Authorization: Bearer {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'accept: application/json' \
-d '{
"fieldType":"PICKLIST",
"description": "Intuition Feedback",
"name":"Intuition Feedback",
"globalAsset":true,
"assetClassList":[
"MESSAGE"
]
}'




**Dev Notes: **There might be a few restrictions like immutability of type of custom fields, asset class list cannot be removed, etc.

### Response Parameters





| Response item | Description | Data type |
| --- | --- | --- |
| 204 (No Content) | It indicates that the server has successfully fulfilled the request and that there is no content to send in the response payload body. | HTTP |

[](https://dev.sprinklr.com/custom-field-update-v1)




[Back to top](https://dev.sprinklr.com/custom-field-update-v1)
