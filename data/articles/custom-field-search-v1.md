---
title: "Custom Field Search v1"
slug: custom-field-search-v1
url: https://dev.sprinklr.com/custom-field-search-v1
---

# Custom Field Search v1

#
POST - Custom Field Search


You can search for a Custom Field with different objects via this API call and you will get the list of custom fields that match your search request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/customfield/search

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
| clientIds | Optional | Search for custom fields matching at least one of client Ids provided. | List<String> |
| assetClassList | Optional | Assets classes to which the custom fields will be related. Example: UNIVERSAL_CASE, MESSAGE_WORKFLOW, PROFILE_WORKFLOW, MEDIA_ASSET | List<String> |
| fieldNames | Optional | Represents the name of a specific field that should be returned. | List<String> |
| fieldTypes | Optional | Custom Field Type. You can select from PICKLIST MULTISELECT, PICKLIST, NUMBER, DATE, TEXT MULTI, TEXT AREA, OR TEXT. | List<String> |
| keyword | Optional | The keyword on the basis of which you want to search. | String |
| sort | Optional | To sort the search data. | Sort |
| page | Optional | Page number to seach the data from. | Page |
| isGlobal | Optional | If True, will search partner custom field. vice versa client custom field. | Boolean |
| isEnabled | Optional | If True, enabled. | Boolean |

**Dev Notes: **If the request payload is not specified — it will return all the available custom fields.

### Example - Request

 Copy Code



curl -X POST \
https://api3.sprinklr.com/{env}/api/v1/customfield/search' \
-H 'Authorization: Bearer {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'accept: application/json' \
-d '{
"isGlobal": true,
"assetClassList": [
"MESSAGE",
"PROFILE"
],
"fieldTypes": [
"TEXT",
"PICKLIST",
"PICKLIST_MULTISELECT",
"NUMBER",
"DATE",
"TEXTAREA",
"TEXT_MULTI"
],
"page": {
"page": 0,
"size": 2
}
}'




### Example - Response




{
    "totalFound": 22,
    "customFields": [
        {
            "id": "5b1559e4e4b002f5a048e07f",
            "createdTime": 1528125924272,
            "modifiedTime": 1540436206482,
            "fieldName": "5b1559e4e4b002f5a048e07c",
            "globalAsset": true,
            "assetClassList": [
                "MESSAGE"
            ],
            "fieldType": "PICKLIST",
            "name": "Intuition Feedback",
            "description": "",
            "helpText": "",
            "options": [
                "Engageable",
                "Non-Engageable",
                "None"
            ],
            "category": "1. INTUITION",
            "facetEnabled": false,
            "adhocSearchEnabled": false,
            "enabled": true,
            "contentReplacementEnabled": false,
            "preferred": false,
            "required": false,
            "isHidden": false,
            "isHiddenFromMonitoring": false,
            "order": 1,
            "customFieldControllerById": {}
        },
        {
            "id": "5acdc183e4b08b6f64b377b3",
            "createdTime": 1523433859656,
            "modifiedTime": 1540436196409,
            "fieldName": "5acdc183e4b08b6f64b377af",
            "globalAsset": true,
            "assetClassList": [
                "MESSAGE"
            ],
            "fieldType": "PICKLIST",
            "name": "Intuition Predicts",
            "description": "",
            "helpText": "",
            "options": [
                "Engageable",
                "Non-Engageable"
            ],
            "category": "1. INTUITION",
            "facetEnabled": false,
            "adhocSearchEnabled": false,
            "enabled": true,
            "contentReplacementEnabled": false,
            "preferred": false,
            "required": false,
            "isHidden": false,
            "isHiddenFromMonitoring": false,
            "order": 1,
            "customFieldControllerById": {}
        }
    ]
}





### Response Parameters





| Parameters | Description | Type |
| --- | --- | --- |
| totalFound | The number of fields found based on search. | Int |
| customFields | List of the custom field found. | List<{Ids}> |
| Id | The {Id} is associated with the custom field you have created via API call. | String |
| createdTime | Represents the time of creation of custom field. | Int |
| modifiedTime | Represents the time of custom field modification. | Int |
| fieldName | Represents the name of a specific field that is returned. | 24-character hashes in the dataset. |
| globalAsset | If True, the Custom Field will be visible across all clients in that partner only. | Boolean |
| assetClassList | Assets classes to which the custom fields will be related. The Asset Classes are Account, Outbound Message, Message, Profile, Media Asset, User, Workspace (Client), Campaign, Community Product, Paid Initiative, Ad Set, Ad Variant, Case, and Task. | List<String> |
| fieldType | Custom Field Type. You can select from PICKLIST MULTISELECT, PICKLIST, NUMBER, DATE, TEXT MULTI, TEXT AREA, OR TEXT. | String |
| name | Name of the custom field. | String |
| description | Description of the custom field. Not exceeding 500 characters. | String |
| facetEnabled | If True, you can check response based on a custom field with respect to the native channel. For example, suppose you are using the reporting module to check how many tweets were posted to Twitter today which had this custom field. So, you can see custom fields as filtering option on any asset. | Boolean |
| adhocSearchEnabled | If True, the field will be shown in the Universal Search field bar while searching. | Boolean |
| enabled | Represents whether the Custom Field is enabled or not. For example, from UI, you can enable and disable custom fields based on your requirement. | Boolean |
| contentReplacementEnabled | If True, you can use this as a placeholder. For example, if you want to publish a message to twitter then this Custom Field can hold that value. | Boolean |
| required | Controls whether the custom field is mandatory or not. | Boolean |
| isHidden | If TRUE, this field will not be available on Engagement and Reporting Dashboard and in the UI. | Boolean |
| isHiddenFromMonitoring | If True, Custom Field will not be available for monitoring purpose. | Boolean |
| order | The order will define where the custom fields need to be shown in UI. Like in top or bottom based on order value. For example, order: 0, means it shows in the top section. | Int |

**Need assistance? Fill out our [feedback form](https://forms.office.com/r/5wTBFPQ7DC) and we’ll get back to you. **

 [](https://dev.sprinklr.com/custom-field-search-v1)




[Back to top](https://dev.sprinklr.com/custom-field-search-v1)
