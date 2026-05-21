---
title: "Update Custom Field"
slug: update-custom-field
url: https://dev.sprinklr.com/update-custom-field
---

# Update Custom Field

#
PUT Update Custom Field

This API call helps update the custom field using the unique field Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-field/{customFieldId}

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

### Path Parameters
















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| customFieldId | Required | The unique identifier for the custom field | String |

### Request Parameters

























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


















































``

- ****

- ****



| Parameter | Sub-Param | Required/Optional | Definition | Type |
| --- | --- | --- | --- | --- |
| description |  | Optional | The description of the custom field. Should not exceed 500 characters. | String |
| assetTypes |  | OptionalRequired if you want to update the asset type | The asset types the custom field is related toSupported Asset Types: Account Outbound Message Message Profile Media Asset User Campaign Sub-Campaign Community Product Paid Initiative Ad Set Ad Variant Case Universal Case Survey Task | List [String] |
| values |  | OptionalRequired when you want to update the custom field values | Array defining the corresponding values of the custom field | Array |
|  | key |  | The value of the custom field | String |
|  | label |  | The label set for the custom field value | String |
| options2 |  | Optional | Extended options with multilingual support. | Array of Objects |
|  | label | Required | Display label of the option. | String |
|  | value | Required | Value of the option. | String |
| langVsTranslatedFieldValues |  | Optional | This object enables localization support by mapping language codes to translated field content.   Example:  "langVsTranslatedFieldValues": {         "es_ES": {             "description": "Updated Desc again spanish"         }     }  Key:Represents the language code, in this case, Spanish (es_ES). 				Value (Nested Object):The translated description text for the specified language. | Object |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/custom-field/62fc7b88b893784e3db68fa1' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
   "description": "api3 cf",
   "assetTypes": [
       "UNIVERSAL_CASE"
   ],
   "values": [
       {
           "key": "Yes",
           "label": "Yes"
       },
       {
           "key": "No",
           "label": "No"
       },
       {
           "key": "True",
           "label": "True"
       }
   ]
	    "options2": [
        {
            "label": "TEST 1",
            "value": "TEST 1",
            "langVsTranslatedFieldValues": {
                "es_ES": {
                    "label": "Test-spanish-updated"
                }
            }
        },
        {
            "label": "TEST 2",
            "value": "TEST 2",
            "langVsTranslatedFieldValues": {
                "es_ES": {
                    "label": "Test-b-spanish-updated"
                }
            }
        }
    ],
    "langVsTranslatedFieldValues": {
        "es_ES": {
            "description": "Updated Desc again spanish"
        }
    }
}'
 

     
     
   

## Example - Response

 
 
     
 
204 No Content
 

     
     
   
 

**Dev Notes: **204 No Content implies that the custom field has been successfully updated

[](https://dev.sprinklr.com/update-custom-field) 

 

 
[Back to top](https://dev.sprinklr.com/update-custom-field)
