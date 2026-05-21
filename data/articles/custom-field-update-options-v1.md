---
title: "Custom Field Update Options V1"
slug: custom-field-update-options-v1
url: https://dev.sprinklr.com/custom-field-update-options-v1
---

# Custom Field Update Options V1

#
PUT - Custom Field Update Options




Using this API, you can Add, Delete and Set user defined values for a custom field. In this call request, body/payload can be changed to perform three different tasks using the same API endpoint. After making the PUT Request you will get 204 (No Content) as Response on success.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/customField/{CustomFieldId}/updateOptions

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

****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Id | Required | The id of the customField for which you want to update options | String |

## Example 1 - Add Options

You can add new user defined values in a custom field by using this PUT call.


### Example - Request

 Copy Code



curl -X POST \
https://api3.sprinklr.com/{env}/api/v1/customField/{CustomFieldId}/updateOptions' \
-H 'Authorization: Bearer {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'Content-Type: application/json' \
-d '{
"addOptions" : ["11"]
}'




### Example - Response




204 No Content





## Example 2 - Delete Options

You can delete pre defined user values of a custom field by using this PUT call.


### Example - Request

 Copy Code



curl -X POST \
https://api3.sprinklr.com/{env}/api/v1/customField/{CustomFieldId}/updateOptions' \
-H 'Authorization: Bearer {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'Content-Type: application/json' \
-d '{
"deleteOptions" : ["E"]
}'




### Example - Response




204 No Content





**Dev Notes: **addOptions and deleteOptions can be used together but neither addOptions nor deleteOptions will give success together with setOptions.

## Example 3 - Set Options

You can set completely new user defined values for a custom field by using this call.

### Example - Request

 Copy Code



curl -X POST \
https://api3.sprinklr.com/{env}/api/v1/customField/{CustomFieldId}/updateOptions' \
-H 'Authorization: Bearer {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'Content-Type: application/json' \
-d '{
"setOptions" : ["1","5","7"]
}'




### Example - Response




204 No Content





### Response Parameters





| Parameters | Description | Data type |
| --- | --- | --- |
| 204 (No Content) | It indicates that the server has successfully fulfilled the request and that there is no content to send in the response payload body. | HTTP |

**Need assistance? Fill out our [feedback form](https://forms.office.com/r/5wTBFPQ7DC) and we’ll get back to you. **

[](https://dev.sprinklr.com/custom-field-update-options-v1)




[Back to top](https://dev.sprinklr.com/custom-field-update-options-v1)
