---
title: "Update Draft"
slug: update-draft
url: https://dev.sprinklr.com/update-draft
---

# Update Draft

#
PUT Update Draft

You can Update a draft of a message via this API call.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/publishing/draft/update

### Headers

HTTP headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			```




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
| workspace_id | workspaceId | This field is optional. If your authorization token is associated with multiple workspaces, you'll have to pass workspace_id in the headers for updating a draft. You can use  to check the workspace Id your token is primarily associated with. |

### Request Parameters



















****






























































































































































****

****````





| Parameters | Sub Parameters | Sub-Param objects | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- | --- |
| id |  |  |  | Unique id of the outbound message in Sprinklr.You can extract this id from create draft response.Example: MESSAGE_600000018506001 In this case, the id would be: 600000018506001 | Integer |
| accountId |  |  | Required | List of account ids where the existing draft needs to be updated | List [ Integer] |
| content |  |  | Required | The object containing content details. |  |
|  | title |  | Optional | The title of the meesage. | String |
|  | text |  | Required | The text message. | String |
|  | attachment |  | Required | Type of attachment |  |
|  |  | type | Optional | Type of attachment. VIDEO, IMAGE etc. | String |
|  |  | url | Optional | The url of attachment. | URL |
|  |  | attachmentOptions{ 				channelType 				accountId 				} | Required | Array of attachment properties per channel and/or account.{ChannelType for media options.If the properties are specific to an account inaddition to channelType, accountId can be specified and the properties would then only be used for the given account} | String,Integer |
| scheduleDate |  |  | Optional | Schedule date for the message | Integer |
| taxonomy |  |  |  |  |  |
|  | campaignId |  | Required | Campaign identifier to associate the message. | String |
|  | clientCustomProperties |  |  | client custom properties for the message | String |
|  | partnerCustomProperties |  |  | partner custom properties for the message | String |
|  | tags |  |  | Tags to be added to the message | String |
|  | urlShortenerId |  |  | Url shortner identifier to apply to the message | String |
| approval |  |  |  |  |  |
|  | type |  |  | Type of approval to process. defaults to NONE 				 				Enum: [ ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE | String |
|  | id |  |  | Value for the chosen approval type. | String |
| version |  |  |  | Current version of the message.Note: The version needs to be updated every time you update the draft. Please specify a higher version every time you make update draft API call for ensuring successful response.Example: If you updated the draft using "version": 1 earlier, make the second update call using "version": 2If you do not update the version, you are likely to receive 400 bad request in the response. | Integer |

## Example

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/update' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
    "id": 600000018506001,
    "accountIds": [
        600004211
    ],
    "content": {
    "title": "sample",
    "text": "NEW TEST",
    "attachment": {
        "url": "https://sprcdn-assets.sprinklr.com/1436/0165e222-ec2e-447c-8ef5-a2b98bbe8abf-193321266.jpeg",
        "type": "IMAGE"
      }
  },
    "taxonomy": {
        "campaignId": "2_1"
    },
     "version": 3
}'
 

     
     
   

## Example - Response

 
 
     
 
{
    "data": "MESSAGE_600000018506001",
    "errors": []
}
