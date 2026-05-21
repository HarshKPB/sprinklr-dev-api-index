---
title: "Custom Field Create v1"
slug: custom-field-create-v1
url: https://dev.sprinklr.com/custom-field-create-v1
---

# Custom Field Create v1

#
POST - Custom Field Create


Using this API, you can create a custom field — a fully customizable property or tag that is created at several feature levels.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/customfield

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

## Request Parameters







****

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| assetClassList | Required | Assets classes to which the custom fields will be related.Supported asset classes include:Account, Outbound Message, Message, Profile, Media Asset, User, Workspace (Client), Campaign, Community Product, Paid Initiative, Ad Set, Ad Variant, Case, and Task. | List<String> |
| fieldType | Required | Custom Field Type. You can select from PICKLIST MULTISELECT, PICKLIST, NUMBER, DATE, TEXT MULTI, TEXT AREA, OR TEXT. | String |
| name | Required | Name of the custom field. | String |
| description | Optional | Description of the custom field. Not exceeding 500 characters. | String |
| globalAsset | Optional | If True, the Custom Field will be visible across all workspaces in the respective partner environment. | Boolean |
| helpText | Optional | Help text for the custom field. This additional information related to the custom field will appear for the user in the UI. | String |
| options | Optional | List of options. Applicable for PICKLIST field types. | List<String> |
| defaultValue | Optional | The default value of the custom field. | String |
| optionsLabels | Optional | Names of the options. These will be reflecting in the UI. | List<String> |
| category | Optional | Category of the custom field. | String |
| enabled | Optional | Is the Enabled or Disabled. | Boolean |
| order | Optional | The ordering of the custom field. | int |
| isHidden | Optional | If TRUE, this field will not be available on Engagement and Reporting Dashboard and in the UI. | Boolean |
| required | Optional | Controls whether the custom field is mandatory or not. | Boolean |
| customFieldControllerById | Optional | The object defining the controlling field id and controlled field configuration.Refer to the table below for the object details | Object |

### Controlling Logic for Custom Field Object Details

| Parameter | Sub-Param | Sub-Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- | --- |
| id (Only add the value here without adding the parameter) |  |  | Required | The id of the controlling custom field | Object |
|  | controllingFieldConfig |  | Required | Object defining the controlling custom field logic | Object |
|  |  | controllingFieldValue (Only add the value here without adding the parameter) | Required | Controlling field value and the list of values that it wants to control from the defined set of controlled custom field , i.e., the values that will be added in the list, its visibility will be dependent on the defined controlling field value.Syntax:"Test1": [1, 2],Where test1 is the controlling field and 1, 2 are the controlled fields | List[String, Integer] |

**Dev Notes: **When applying the controlling custom field logic, the asset type for both the controlling and controlled custom field should be same.

### Example - Request

 Copy Code



curl -X POST

'https://api3.sprinklr.com/{env}/api/v1/customfield'

-H 'Authorization: Bearer {Enter your Access Token}'

-H 'Key: {Enter your API KEY}'

-H 'accept: application/json'

-H 'Content-Type: application/json'

-d '
{
"fieldType":"PICKLIST",
"description":"Verified Account",
"name":"Is this a verified account",
"globalAsset":true,
"assetClassList":[
"PROFILE"
],
"options":[
"1",
"2",
"3"
],
"customFieldControllerById": {
"601ce7527a8c3309510b99f0": {
"controllingFieldConfig": {
"Test1": [
1, 2
],
"Test2": [
2
]
}
}
}
}'




### Example - Response




"5c2ca9bfe4b04b80d705153f"





### Response Parameters







| Parameter | Description | Data type |
| --- | --- | --- |
| {Id} | The {Id} is associated with the custom field you have created via API call or in the UI. Example: You can use the Read API call with the {Id} to get the information related to Custom Create Field after creating it. | String. This actually is a key for a custom field in our API dataset. |

**Need assistance? Fill out our [feedback form](https://forms.office.com/r/5wTBFPQ7DC) and we’ll get back to you. **

 [](https://dev.sprinklr.com/custom-field-create-v1)




[Back to top](https://dev.sprinklr.com/custom-field-create-v1)
