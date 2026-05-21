---
title: "Update Options with Label"
slug: update-options-with-label
url: https://dev.sprinklr.com/update-options-with-label
---

# Update Options with Label

#
PUT Update Options with Label

Using thsi API, you can assign a new value or delete an existing value for the given custom field name.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-field/{customFieldId}/updateOptionsWithLabel

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













[fetch custom field using field name API](https://dev.sprinklr.com/fetch-custom-field-using-field-name)




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| customFieldId | Required | The unique identifier for the custom field.You can use  to fetch custom field Id. | String |

### Request Parameters

















| Parameter | Sub-Parameter | Required/Optional | Definition | Type |
| --- | --- | --- | --- | --- |
| optionsWithLabels |  | Optional | Array defining the new key and label for the value | Array |
|  | label | Required | Refers to the label for the new value | String, Integer |
|  | value | Required | Refers to the new value you want to assign | String, Integer |
| deleteOptions |  | Optional | List referring to the values you want to delete from the custom field | List [String, Integer] |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/custom-field/62fc7b88b893784e3db68fa1/updateOptionsWithLabel' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "optionsWithLabels": [
        {
            "label": "5",
            "value": "5"
        }
    ],"deleteOptions":["1"]
}'
 

     
     
   

## Example - Response

 
 
     
 
204 No Content
 

     
     
   
 

**Dev Notes: **

- 204 No Content implies that the custom field has been successfully updated
- Options can be updated only for PICKLIST and PICKLIST_MULTISELECT types

### Old Values

### Updated Values
