---
title: "Bulk Messages"
slug: bulk-messages
url: https://dev.sprinklr.com/bulk-messages
---

# Bulk Messages

#
POST Bulk Messages

You can import messages in bulk within Sprinklr via this API call and you will get the Id and other related objects as a response after the request are successful. Below are the steps that you need to follow:

- [Create Template](https://dev.sprinklr.com/bulk-messages): Upload file from your local to Sprinklr.

- [Import Messages](https://dev.sprinklr.com/bulk-messages): To import Messages in bulk within Sprinklr.

## Create Template

Create the template that you can use in reoccurring API calls. For the very first time you need to upload the file containing message details and map the file headers within the Sprinklr UI and save it with a unique name to use it again in API calls directly without repeating the Sprinklr UI process for the same template. Below are the steps:

**Step 1: **Login into Sprinklr UI and click on First Party Data Ingestion within Modern Research.

**Step 2: **Click on the Import from Excel on the top right.
**Step 3: **Upload the excel file from your local.
**Step 4: **Enter the unique file name and map the Sprinklr fields with the headers used in the excel.

**Note:** Once you map the file headers within Sprinklr and save it with unique name, now you can use the same file with same headers to import more data via uploading it to the web so that it can be accessed publicly.

## POST Import Entity

Once you have template mapped within Sprinklr, now you can make this API call to import the messages in bulk.

### API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/data-ingestion/ingest

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

























			[Media Upload API](https://dev.sprinklr.com/media-upload)























****









| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | The type of data ingestion i.e. LISTENING_MESSAGE | String |
| name | Required | The name of the task. | String |
| fileUrl | Required | The public URL of the file, can be generated using .Supported file extensions: .csv/.xlsx | String |
| importTag | Required | The tags for filtering. | String |
| templateName | Required | The name of the template, saved in Sprinklr. | String |
| callbackUrl | Required | On success, a payload will be sent to the callback URL.  Note: The Callback URL can be public or with authentication and should return 200 response on receiving an empty payload. This is used for verification purpose, if the callback URL verification is failing, please check with the Sprinklr team that they have valid certificates installed. | String |
| callbackType | OptionalRequired when providing callbackUrl | Refers to the callback type for the callback Url.Supported Values: AUDIENCE_DATA_CONNECTOR, OAUTH2_FAILED_FILE_UPLO, PUBLIC_URL | String |
| callbackUrlHeaders | Optional | You can use this field for Authenticating the call coming to the callback Url specified above. | String |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/data-ingestion/ingest' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "LISTENING_MESSAGE",
    "name": "test payload",
    "fileUrl": "",
    "importTag": "sample tag",
    "templateName": "test template",
    "callbackUrl": "https://webhook.site/0f4251e2-2115-4f22-810a-32c3f02c662d",
    "callbackType": "PUBLIC_URL",
    "callbackUrlHeaders": {
        "key1": "value2",
        "key2": "value2"
    }
}'
 

     
     
   

## Example - Response

 
 
     
 
{
   "data": "{\"taskId\":\"6033961866934b5708a5f90a\"}",
   "errors": []
}
 

     
     
   
 
On success, a payload will be sent to the callback URL. The Id will be the same as the output from the above call.
 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
{
  "id": "6033961866934b5708a5f90a",
  "clientId": 108,
  "userId": 1312,
  "totalRecords": 3,
  "failedRecordsCount": 0,
  "createdRecordsCount": 3,
  "updatedRecordsCount": 0,
  "startTime": 1613993498264,
  "completionTime": 1613993535613
}
 

     
     
   

	[](https://dev.sprinklr.com/bulk-messages) 

 

 
[Back to top](https://dev.sprinklr.com/bulk-messages)
