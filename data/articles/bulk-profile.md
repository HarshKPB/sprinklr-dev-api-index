---
title: "Bulk Profile"
slug: bulk-profile
url: https://dev.sprinklr.com/bulk-profile
---

# Bulk Profile

#
POST Bulk Profile


You can create profiles in bulk within Sprinklr via this API call and you will get the Id and other related objects as a response after the request are successful. Below are the steps that you need to follow:

**Dev Notes: **To update and delete the profiles, you can use the same API call as each profile will have a unique Id, so in the excel sheet if the system finds a profile with a unique Id it will update otherwise it will create the profile.

- [Download Template](https://dev.sprinklr.com/bulk-profile/#1): Download the excel template from the Sprinklr UI.

- [Import Profiles](https://dev.sprinklr.com/bulk-profile/#2): To import profile in bulk within Sprinklr.

## Download Template

To download the excel template in which you can fill the details of the profiles which you want to create, follow these steps:


**Step 1: **Log in to Sprinklr UI and click on Profile within Modern Engagement.


**Step 2: **Click on the Import icon on the top right.

**Step 3: **Click on Download Excel Template to download the template needed for this API.

**Step 4: **Fill in the details of the profiles in the excel template and upload the file onto the web.

**Dev Notes: **Once you fill all the details in the excel file, you need to upload it to the web so that it can be accessed publicly.

## POST Import Entity

Once you have downloaded the template and filled in the details as per the headers in the excel sheet, now you can make this API call to import the profiles in bulk.

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












			``````




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | The type of data ingestion i.e. PROFILE or INFLUENCER_PROFILE | String |
| name | Required | The name of the task. | String |
| fileUrl | Required | The public URL of the file, can be generated using .Supported file extensions: .csv/.xlsx | String |
| importTag | Required | The tags for filtering. | String |
| templateName | Optional | The name of the excel file. | String |
| callbackUrl | Optional | On success, a payload will be sent to the callback URL.  Note: The Callback URL can be public or with authentication and should return 200 response on receiving an empty payload. This is used for verification purpose, if the callback URL verification is failing, please check with the Sprinklr team that they have valid certificates installed. | String |
| callbackType | OptionalRequired when providing callbackUrl | Refers to the callback type for the callback Url.Supported Values: AUDIENCE_DATA_CONNECTOR, OAUTH2_FAILED_FILE_UPLO, PUBLIC_URL | String |
| callbackUrlHeaders | Optional | You can use this field for Authenticating the call coming to the callback Url specified above. | String |
| identifierFields | Optional | Fields to be used as identifiers, If this is empty, we use sprinklr identifiers for creating/updating profiles. Currently supported field is PARTNER_CUSTOM_PROPERTIES. Only supported when the type is PROFILE. i.e "type": "PROFILE" | String |

### Example - Request















Copy Code


 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/data-ingestion/ingest' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "PROFILE",
    "name": "test payload",
    "fileUrl": "",
    "importTag": "sample tag",
    "templateName": "test template",
    "callbackUrl": "https://webhook.site/0f4251e2-2115-4f22-810a-32c3f02c662d",
    "callbackType": "PUBLIC_URL",
    "callbackUrlHeaders": {
        "key1": "value2",
        "key2": "value2"
    },
    "identifierFields": {
        "PARTNER_CUSTOM_PROPERTIES": [
            "cf label 1",
            "cf label 2"
        ]
    }
}'




    

### Example - Response




 
{
   "data": "{\"taskId\":\"6033961866934b5708a5f40a\"}",
   "errors": []
}





 

On success, a payload will be sent to the callback URL. The Id will be the same as the output from the above call.




 
{
  "id": "6033961866934b5708a5f40a",
  "clientId": 108,
  "userId": 1312,
  "totalRecords": 3,
  "failedRecordsCount": 0,
  "createdRecordsCount": 3,
  "updatedRecordsCount": 0,
  "successfulFileUrl": "https://abc.new.com/EXPORT/5/6574bdab-a179-4ab1-jkhj-1ab0005ca-1477231784/Records_6033963f66934b5708a5f4.csv",
  "failedFileUrl": "https://abc.new.com/EXPORT/5/6574bdab-a179-4ab1-jkhj-1ab0095ca-1477231784/Records_6033963f66934b5708a5f4.csv",
  "startTime": 1613993498264,
  "completionTime": 1613993535613
}





 

**Dev Notes: **
`successfulFileUrl` - Contains rows successfully created with Sprinklr ID in the last column.

`failedFileUrl` - Contains rows failed with failure reason in the last column.

	[](https://dev.sprinklr.com/bulk-profile) 

 

 
[Back to top](https://dev.sprinklr.com/bulk-profile)
