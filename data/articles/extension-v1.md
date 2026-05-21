---
title: "Extension v1"
slug: extension-v1
url: https://dev.sprinklr.com/extension-v1
---

# Extension v1

#   Extension


An API extension automates the interaction between Sprinklr and any third-party web service. By building an API extension, the third-party web service features get automatically integrated with Sprinklr using the openAPI specification that defines what the API can do.

With extension API, you can receive the callback URL destinations to push data payload from Sprinklr to external system and also to receive the data fields as response from external system.

## Extension Object












































































| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Extension ID |
| name | String | Name of the extension |
| extName | String | Description of the extension. |
| type | String | Extension point type. RULE, ASSET_PANE |
| assetClass | List<String> | List of supported asset classes. |
| url | String | Iframe url for the extension service with parameters. |
| inputFields | List<Field> | Input fields required by external api |
| outputFields | List<Field> | Output fields returned by external api |
| inputFieldMappings | Map<String,Field> | Input field mappings, which field from asset maps to input field required by external api. Asset field type could be standard or custom field. |
| outputFieldMappings | Map<String,Field> | Output field mappings, which field from asset should be set from output field returned by external api. Asset field type could be standard or custom field. |
| method | String | Httpmethod of the extension api endpoint. GET,HEAD,POST,PUT,PATCH,DELETE,OPTIONS,TRACE; |
| headers | Map<String,String> | Key value mapping of the headers to be passed when calling the extension. |
| enabled | boolean | Enable or disable the extension. Only enabled ones will appear in the UI. |

## Input/Output Field Array Description































| Parameter | Type | Description |
| --- | --- | --- |
| fieldName | String | Field Name |
| fieldType | String | Field type like STANDARD, CUSTOM_FIELD. Used only for Sprinklr field. |
| fieldLabel | String | The UI label of the field. |
| attributes | Map<String,String> | UI layout attributes. |

**Related Knowledge Base Article:** **[Building API Extensions Through UI](https://www.sprinklr.com/help/articles/configure-an-extension-in-sprinklr/add-external-rest-api-in-sprinklr/64833289723d925979db8cf3)**
