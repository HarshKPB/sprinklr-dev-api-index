---
title: "Publishing SMS"
slug: publishing-sms
url: https://dev.sprinklr.com/publishing-sms
---

# Publishing SMS

#
POST Publishing SMS


You can publish SMS via this API call.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/publishing/post

### Headers

HTTP headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			``




			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)


``
[ME API](https://dev.sprinklr.com/me-api)



| Key | Value | Description |
| --- | --- | --- |
| accept | application/json | Determines the acceptable response type from the server |
| Content-Type | application/json | Content-Type is representation header determines the type of data (media/resource) present in the request body. |
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the dev portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  article |
| workspace_id | workspaceId | This field is optional. If your authorization token is associated with multiple workspaces, you'll have to pass workspace_id in the headers for publishing SMS. You can use  to check the workspace Id your token is primarily associated with. |

### Request Parameters















































































































| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| accountId |  | Required | The Id of the account which will be used to publish SMS. | Integer |
| content |  | Required | The object containing Content details. |  |
|  | text | Required | The text message you want to send as sms. | String |
| scheduleDate |  | Optional | Schedule date for the message | Integer |
| taxonomy |  | Required | Object containing taxonomy details. |  |
|  | campaignId | Required | Campaign identifier to associate the message. | String |
|  | clientCustomProperties | Optional | Refers to the key and value pair for custom properties at the workspace level | String |
|  | partnerCustomProperties | Optional | Refers to the key and value pair for custom properties at the customer (global) level | String |
|  | tags | Optional | Tags to be added to the post | String |
|  | urlShortenerId | Optional | Url shortner identifier to apply to the post | String |
| channelOptions |  | Required | Object containing user details. |  |
|  | channelType | Required | The channel type will be SMS only. | String |
|  | toPhoneNumber | Required | The mobile number of the user to whom you want to send sms. | String |
|  | countryCode | Required | The country code of the user mobile number. | Integer |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/publishing/post \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
    "accountIds": [
        "10000755"
    ],
    "content": {
        "text": "SMS testing"
    },
    "scheduleDate": 0,
    "taxonomy": {
        "campaignId": "1000009_367"
    },
    "channelOptions": [
        {
            "channelType": "SMS",
            "toPhoneNumber": "7974027000",
            "countryCode": 91
        }
    ]
}'
 

     
     
   

## Example - Response

 
 
     
 
{
    "data": [
        "POST_2072146116"
    ],
    "errors": []
}
 

     
     
   
 

	[](https://dev.sprinklr.com/publishing-sms) 

 

 
[Back to top](https://dev.sprinklr.com/publishing-sms)
