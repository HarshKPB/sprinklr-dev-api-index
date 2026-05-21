---
title: "Bulk Import Entity"
slug: bulk-import-entity
url: https://dev.sprinklr.com/bulk-import-entity
---

# Bulk Import Entity

#
  GET and POST - Bulk Import Entity

You can import supported entities in bulk within Sprinklr via this API call and you will get the Id and other related objects as response after the request is successful. To import the entities in bulk, you need to follow the steps given below:

Note: To `update the entity` you can use the same API call as each entity will have a unique Id, so in the excel sheet, if the system finds a entity with a unique Id it will update otherwise it will create it.

## GET Download Template

To download the excel template in which you can fill the details of the entity which you want to import.

### API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/file-import/download/template

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

### Query Parameters



















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityType | Required | The entity type you want to import like UNIVERSAL_PRODUCT, USER_GROUP, etc. | String |

`Supported Entity Types`: USER,
UNIVERSAL_PRODUCT,
UNIVERSAL_MESSAGE_STATUS,
MEDIA_ASSET,
ROLES_AND_PERMISSIONS,
PARTNER_QUEUE,
CLIENT_QUEUE,
PROFILE_LIST,
PROFILE_TAGGING_RULE,
CUSTOM_FIELD,
CAMPAIGN,
USER_GROUP,
ACCOUNT_GROUP,
ACCOUNT.

## Example - Request














Copy Code




curl -X GET \
https://api3.sprinklr.com/{env}/api/v2/file-import/download/template?entityType=UNIVERSAL_PRODUCT \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'





## Example - Response





200 Ok





**Dev Note**:
Once you fill in all the details in the excel file, you need to upload it to the web to using [Media Upload API](https://dev.sprinklr.com/media-upload). This will make the file publicly accessible, which can then be configured as a fileUrl in the bulk import API call.

## POSTImport Entity

Once you have downloaded the template and filled in the details as per the headers in the excel sheet, you can now make this API call to import the entity in bulk.

### API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/file-import/entity

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

### Request Parameters










































			``















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| fileUrl | Required | The public URL of the file. | String |
| callbackUrl | Required | On success, a payload will be sent to the callback URL.  Note: The callback URL can be public or with authentication and should return 200 response on receiving an empty payload. This is used for verification purpose, if the callback URL verification is failing, please check with the Sprinklr team that they have valid certificates installed. | String |
| callbackUrlHeaders | Optional | You can use this field for Authenticating the call coming to the callback Url specified above. | String |
| entityType | Required | The supported entity type. | String |
| fileExtension | Required | The file extension.  Supported file extensions are  .xls , .xlt, .xltx, .xlsx, .csv , .txt | String |
| outputFileExtension | Optional | File extension of output either .csv or .xlsx. Default value is .xlsx | String |
| onlyFailedOutput | Optional | Whether to include all rows or only failed rows in the output. Default value false. | Boolean |

## Example - Request














Copy Code




curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/file-import/entity \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
   "fileUrl": "",
   "callbackUrl": "",
   "entityType": " ",
   "outputFileExtension": "csv",
   "onlyFailedOutput": "true",
   "callbackUrlHeaders": {
          "Key1":"Value1",
          "Key2":"Value2"
          },
   "fileExtension": "xlsx"
}'





## Example - Response





{
   "data": "{\"taskId\":\"6026440df0f98a17b6529eb6\"}",
   "errors": []
}





On success, a payload will be sent to the callback URL. The Id will be the same as the output from the above call.





{
  "id": "6026440df0f98a17b6529eb6",
  "entityType": "Universal Product",
  "userId": ,
  "uploadedAt": ,
  "numberOfRows": ,
  "numberOfRowsCreated": ,
  "numberOfRowsUpdated": ,
  "status": "",
  "fileUrl": "",
  "responseFileUrl": "",
  "clientId": ,
  "partnerId": ,
  "skippedRows":
}





[](https://dev.sprinklr.com/bulk-import-entity)




[Back to top](https://dev.sprinklr.com/bulk-import-entity)
