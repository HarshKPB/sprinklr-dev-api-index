---
title: "Extension Update v1"
slug: extension-update-v1
url: https://dev.sprinklr.com/extension-update-v1
---

# Extension Update v1

#
  PUT Extension Update




You can update an extension point which defines the callback URL destinations to receive a pushed data payload from Sprinklr via this API call. You will get the updated response after making the Request.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v1/extension/{Id}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














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

































****







****




















































| Query Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| id | Required | Extension ID. | String |
| name | Optional | Name of the extension. | String |
| extName | Optional | Refers to the name of the extension. | String |
| type | Required | Extension point type.Example: RULE, ASSET_PANE. | String |
| assetClass | Required | List of supported asset classes.Example: UNIVERSAL_CASE, UNIVERSAL_MESSAGE, QUEUE | List<String> |
| url | Required | Iframe url for the extension service with parameters. | String |
| inputFields | Required | Input fields you want to update for the external API | List<Field> |
| outputFields | Required | Output fields you want to return for the external api. | List<Field> |
| inputFieldMappings | Required | Input field mappings, the field from the asset which maps to the input field X by external api. Asset field type could be a standard or custom field. | Map<String,Field> |
| outputFieldMappings | Required | Output field mappings, which field from asset should be set from the output field returned by external api. Asset field type could be a standard or custom field. | Map<String,Field> |
| method | Optional | Http method of the extension api endpoint. GET,HEAD,POST,PUT,PATCH,DELETE,OPTIONS,TRACE. | String |
| headers | Optional | Key value mapping of the headers to be passed while calling the extension. | Map<String,String> |
| enabled | Optional | Enable or disable the extension. Only enabled ones will appear in the UI. | Boolean |

## Field Definitions































| Parameter | Type | Description |
| --- | --- | --- |
| fieldName | String | Field Name |
| fieldType | String | Field type like STANDARD, CUSTOM_FIELD. Used only for Sprinklr field. |
| fieldLabel | String | The UI label of the field. |
| attributes | Map<String,String> | UI layout attributes. |

## Example - Request















Copy Code



curl -X PUT \
  'https://api3.sprinklr.com/{env}api/v1/extension/5c2f44c8e4b08015475d35ac' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
  "name":"Update Chatbot Service Call",
  "extName":"Update Chatbot Service Call",
  "type":"RULE",
  "assetClass":"UNIVERSAL_CASE",
  "url":"http://requestbin.net/r/18p3kxa1",
  "inputFields":[
    {
      "fieldName":"caseName",
      "fieldLabel":"Case Name"
    },
    {
      "fieldName":"caseNumber",
      "fieldLabel":"Case Number"
    }
  ],
  "outputFields":[
    {
      "fieldName":"thirdPartyCaseName",
      "fieldLabel":"Third party case name"
    },
    {
      "fieldName":"thirdPartyCaseNumber",
      "fieldLabel":"Third party case number"
    }
  ],
  "method":"PUT",
  "headers":{
    "cookies":"sid:aweazdasrareteadrzreaer"
  }
}'






## Example - Response




 {
    "id": "5c2f44c8e4b08015475d35ac",
    "name": "Update Chatbot Service Call",
    "extName": "Update Chatbot Service Call",
    "type": "RULE",
    "assetClass": "UNIVERSAL_CASE",
    "url": "http://requestbin.net/r/18p3kxa1",
    "inputFields": [
        {
            "fieldName": "caseName",
            "fieldLabel": "Case Name"
        },
        {
            "fieldName": "caseNumber",
            "fieldLabel": "Case Number"
        }
    ],
    "outputFields": [
        {
            "fieldName": "thirdPartyCaseName",
            "fieldLabel": "Third party case name"
        },
        {
            "fieldName": "thirdPartyCaseNumber",
            "fieldLabel": "Third party case number"
        }
    ],
    "method": "PUT",
    "headers": {
        "cookies": "sid:aweazdasrareteadrzreaer"
    },
    "enabled": true,
    "encodeQueryParamValues": false
}







	[](https://dev.sprinklr.com/extension-update-v1)






[Back to top](https://dev.sprinklr.com/extension-update-v1)
