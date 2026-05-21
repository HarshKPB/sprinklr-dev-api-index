---
title: "Custom Field Read v1"
slug: custom-field-read-v1
url: https://dev.sprinklr.com/custom-field-read-v1
---

# Custom Field Read v1

#
GET - Custom Field Read

Using this API, you can fetch an existing custom field using the unique field Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/customfield/{id}

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







| Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| id | Required | The id of the Custom Field on which you want to make a Read API call. | String |


**Steps to fetch a Custom Field ID:**



- Open the Custom Field Record Manager from the Sprinklr Launchpad.

- Find the custom field you want.

- Click the vertical ellipsis icon for that custom field.

- Select `View Details`.

- Look at the browser address bar. The custom field ID appears in the URL.


### Example - Request

 Copy Code


curl -X GET \'https://api3.sprinklr.com/{env}/api/v1/customfield/6904e3a49143db688ce06872'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'





### Example - Response




{{
    "id": "6904e3a49143db688ce06872",
    "createdTime": 1761928100955,
    "modifiedTime": 1762164571672,
    "fieldName": "_c_6904e3a49143db688ce06870",
    "globalAsset": true,
    "assetClassList": [
        "MESSAGE"
    ],
    "fieldType": "PICKLIST",
    "name": "vidyatest",
    "options": [
        "unknown",
        "null"
    ],
    "optionsWithLabels": [
        {
            "label": "unknown",
            "value": "unknown",
            "langVsTranslatedFieldValues": {
                "fr_FR": {
                    "label": "aref"
                }
            }
        },
        {
            "label": "nullsd",
            "value": "null",
            "langVsTranslatedFieldValues": {
                "fr_FR": {
                    "label": "wefwe"
                }
            }
        }
    ],
    "additional": {},
    "facetEnabled": false,
    "adhocSearchEnabled": false,
    "enabled": true,
    "contentReplacementEnabled": false,
    "preferred": false,
    "required": false,
    "isHidden": false,
    "isHiddenFromMonitoring": false,
    "order": 0,
    "customFieldControllerById": {}
}





### Response Parameters







| Parameters | Description | Data type |
| --- | --- | --- |
| Id | The {Id} is associated with the custom field you have created via API call. | String |
| createdTime | Represents the time of creation of custom field. | int |
| modifiedTime | Represents the time of custom field modification. | int |
| fieldName | Represents the name of a specific field that should be returned. | String |
| globalAsset | If True, the Custom Field will be visible across all clients in that partner only. | Boolean |
| assetClassList | Assets classes to which the custom fields will be related. The Asset Classes are Account, Outbound Message, Message, Profile, Media Asset, User, Workspace (Client), Campaign, Community Product, Paid Initiative, Ad Set, Ad Variant, Case, and Task. | List<String> |
| fieldType | Custom Field Type. You can select from PICKLIST MULTISELECT, PICKLIST, NUMBER, DATE, TEXT MULTI, TEXT AREA, OR TEXT. | String |
| name | Name of the custom field. | String |
| description | Description of the custom field. Not exceeding 500 characters. | String |
| facetEnabled | If True, you can check response based on the custom field with respect to the native channel. For example, suppose you are using the reporting module to check how many tweets were posted to Twitter today which had this custom field. So you can see custom fields as filtering option on any asset. | Boolean |
| adhocSearchEnabled | If True, the field will be shown in the Universal Search field bar while searching. | Boolean |
| enabled | Represents whether the Custom Field is enabled or not. For example, from UI you can enable and disable custom fields based on your requirement. | Boolean |
| contentReplacementEnabled | If True, you can use this as a placeholder. For example, if you want to publish a message to twitter then this Custom Field can hold that value. | Boolean |
| required | Controls whether the custom field is mandatory or not. | Boolean |
| isHidden | If TRUE, this field will not be available on Engagement and Reporting Dashboard and in the UI. | Boolean |
| isHiddenFromMonitoring | If True, Custom Field will not be available for monitoring purpose. | Boolean |
| order | The order will define where the custom fields need to be shown in UI. Like in top or bottom based on order value. For example, order: 0, means it shows in the top section. | int |

## Custom Field Read - Bulk

Using this API, you can fetch custom fields in bulk.

https://api3.sprinklr.com`/{env}/`api/v1/customfield/bulk

## Query Parameters







| Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| id | Required | The id of the Custom Field on which you want to make a Read API call. | List<String> |

### Example - Request

 Copy Code



curl -X GET \
'https://api3.sprinklr.com/{env}/api/v1/customfield/bulk?ids=5ba35f37e4b0dd6057312b5c,57e2de6fe4b07e163ac2cde3' \
-H 'Authorization: Bearer {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'accept: application/json'




### Example - Response




{
        "id": "57e2de6fe4b07e163ac2cde3",
        "createdTime": 1474485871770,
        "modifiedTime": 1544981455519,
        "fieldName": "57e2de6fe4b07e163ac2cde2",
        "clientId": 5547,
        "globalAsset": false,
        "assetClassList": [
            "OUTBOUND_MESSAGE"
        ],
        "fieldType": "PICKLIST_MULTISELECT",
        "name": "Objective",
        "description": "",
        "helpText": "",
        "options": [
            "Leads",
            "Awareness",
            "Reduce Churn",
            "Retention",
            "Recruitment",
            "Revenue"
        ],
        "facetEnabled": false,
        "adhocSearchEnabled": false,
        "enabled": true,
        "contentReplacementEnabled": false,
        "preferred": false,
        "required": false,
        "isHidden": false,
        "isHiddenFromMonitoring": false,
        "order": 7,
        "customFieldControllerById": {}
    },
    {
        "id": "5ba35f37e4b0dd6057312b5c",
        "createdTime": 1537433399107,
        "modifiedTime": 1543970535554,
        "fieldName": "5ba35f37e4b0dd6057312b59",
        "globalAsset": true,
        "assetClassList": [
            "MESSAGE"
        ],
        "fieldType": "PICKLIST",
        "name": "Country",
        "options": [
            "UK",
            "US",
            "Austria",
            "Germany"
        ],
        "facetEnabled": false,
        "adhocSearchEnabled": false,
        "enabled": true,
        "contentReplacementEnabled": false,
        "preferred": false,
        "required": false,
        "isHidden": false,
        "isHiddenFromMonitoring": false,
        "order": 0,
        "customFieldControllerById": {}
    }





### Response Parameters







| Parameters | Description | Data type |
| --- | --- | --- |
| Id | The {Id} is associated with the custom field you have created via API call. | String |
| createdTime | Represents the time of creation of custom field. | int |
| modifiedTime | Represents the time of custom field modification. | int |
| fieldName | Represents the name of a specific field that should be returned. | String |
| globalAsset | If True, the Custom Field will be visible across all clients in that partner only. | Boolean |
| assetClassList | Assets classes to which the custom fields will be related. The Asset Classes are Account, Outbound Message, Message, Profile, Media Asset, User, Workspace (Client), Campaign, Community Product, Paid Initiative, Ad Set, Ad Variant, Case, and Task. | List<String> |
| fieldType | Custom Field Type. You can select from PICKLIST MULTISELECT, PICKLIST, NUMBER, DATE, TEXT MULTI, TEXT AREA, OR TEXT. | String |
| name | Name of the custom field. | String |
| description | Description of the custom field. Not exceeding 500 characters. | String |
| facetEnabled | If True, you can check response based on the custom field with respect to the native channel. For example, suppose you are using the reporting module to check how many tweets were posted to Twitter today which had this custom field. So you can see custom fields as filtering option on any asset. | Boolean |
| adhocSearchEnabled | If True, the field will be shown in the Universal Search field bar while searching. | Boolean |
| enabled | Represents whether the Custom Field is enabled or not. For example, from UI you can enable and disable custom fields based on your requirement. | Boolean |
| contentReplacementEnabled | If True, you can use this as a placeholder. For example, if you want to publish a message to twitter then this Custom Field can hold that value. | Boolean |
| required | Controls whether the custom field is mandatory or not. | Boolean |
| isHidden | If TRUE, this field will not be available on Engagement and Reporting Dashboard and in the UI. | Boolean |
| isHiddenFromMonitoring | If True, Custom Field will not be available for monitoring purpose. | Boolean |
| order | The order will define where the custom fields need to be shown in UI. Like in top or bottom based on order value. For example, order: 0, means it shows in the top section. | int |

**Need assistance? Fill out our [feedback form](https://forms.office.com/r/5wTBFPQ7DC) and we’ll get back to you. **

[](https://dev.sprinklr.com/custom-field-read-v1)




[Back to top](https://dev.sprinklr.com/custom-field-read-v1)
