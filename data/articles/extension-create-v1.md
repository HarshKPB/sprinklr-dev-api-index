---
title: "Extension Create v1"
slug: extension-create-v1
url: https://dev.sprinklr.com/extension-create-v1
---

# Extension Create v1

#
  POST Extension Create




You can create an extension point via this API call and you will get the Response after making the Request. Here, extension point defines the callback URL destinations to push data payload from Sprinklr to external system and also to receive the data fields as response from external system.


**Note:**Kindly reach out to Sprinklr Support for the enabling the feature that facilitates making calls to external system via Sprinklr Rule Engine.

You can configure the Sprinklr Rules based on the assetClass and can use the action Make External Call. You need to set the set the extension name that comes as a response after making the API call.



 For more information, [click here](https://www.sprinklr.com/help/articles/external-api-calls/make-external-api-calls-via-guided-workflows/647d967129354c07912f63fb).

## API Endpoint

https://api3.sprinklr.com/{env}/api/v1/extension

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























































































| Request Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| name | Optional | Unique name for the extension. This needs to be set on the client side | String |
| extName | Optional | Description of the extension. | String |
| type | Required | Extension point type. RULE, PROACTIVE_PROMPT, ASSET_PANE, CUSTOM_BOT. | String |
| assetClass | Required | List of supported asset classes. Example: UNIVERSAL_CASE, UNIVERSAL_MESSAGE, QUEUE | List<String> |
| url | Required | Iframe url for the extension service with parameters. | String |
| inputFields | Optional | Input fields X by external api.Supported input fields: defaultValue, externalAssetClass, fieldType, fieldName, fieldLabel, multiValued, optional, separator, regex, regexProcEnabled | List<Field> |
| outputFields | Optional | Output fields returned by external api.Supported output fields: defaultValue, externalAssetClass, fieldType, fieldName, fieldLabel, multiValued, optional, separator, regex, regexProcEnabled | List<Field> |
| inputFieldMappings | Optional | Input field mappings, the field from the asset which maps to the input field X by external api. Asset field type could be a standard or custom field. | Map<String,Field> |
| outputFieldMappings | Optional | Output field mappings, which field from asset should be set from the output field returned by external api. Asset field type could be a standard or custom field. | Map<String,Field> |
| method | Optional | Http method of the extension api endpoint. GET,HEAD,POST,PUT,PATCH,DELETE,OPTIONS,TRACE. | String |
| headers | Optional | Key value mapping of the headers to be passed while calling the extension. | Map<String,String> |
| enabled | Optional | Enable or disable the extension. Only enabled ones will appear in the UI. | Boolean |

## Field Definitions



























| Parameter | Type | Description |
| --- | --- | --- |
| fieldName | String | Field Name |
| fieldType | String | Field type like STANDARD, CUSTOM_FIELD. Used only for Sprinklr field. |
| fieldLabel | String | The UI label of the field. |
| multiValued | Boolean | If true, multiple values have to be sent if field value/s are coming from multi pick list in Sprinklr, defaults to picking single value if false. |
| isOptional | Boolean | If true, the input field is optional |
| separator | String | Used to separate inputs. If multivalued is true, all the values will be concatenated using this separator. |
| isRegexProcEnabled | Boolean | If true, it returns value matching the regex pattern defined in regex field from the input |

## Example - Request















Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}api/v1/extension' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
  "name":"Chatbot Service Call",
  "extName":"Chatbot Service Call",
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
  "method":"POST",
  "headers":{
    "apiKey":"[apikey]",
    "accessToken":"[token]"
  }
}'






## Example - Response




 {
    "id": "5c2f44c8e4b08015475d35ac",
    "name": "Chatbot Service Call",
    "extName": "Chatbot Service Call",
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
    "method": "POST",
    "headers": {
        "apiKey": "[apikey]",
        "accessToken": "[token]"
    },
    "enabled": true,
    "encodeQueryParamValues": false
}







	[](https://dev.sprinklr.com/extension-create-v1)






[Back to top](https://dev.sprinklr.com/extension-create-v1)
