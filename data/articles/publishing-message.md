---
title: "Publishing Message"
slug: publishing-message
url: https://dev.sprinklr.com/publishing-message
---

# Publishing Message

#
POST Publishing Message


Using this API, you can create and publish messages across channel types.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/publishing/message

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
| workspace_id | workspaceId | This field is optional. If your authorization token is associated with multiple workspaces, you'll have to pass workspace_id in the headers for publishing a message. You can use  to check the workspace Id your token is primarily associated with. |

### Request Parameters














****









[Read Account API documentation](https://dev.sprinklr.com/read-account)


































































[ChannelType](https://dev.sprinklr.com/channels-v1)


































































































			[Channel Type](https://dev.sprinklr.com/channels-v1)















			``




| Parameters | Sub Parameters | Sub-Param objects | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- | --- |
| inReplyToMessageId |  |  | Requiredoptional for WHATSAPP BUSINESSl | Message id of the message you want to send the reply for | String |
| accountId |  |  | Required | Account Id where you want to schedule message.Refer to  for the steps to fetch account Id | Integer |
| content |  |  | Required | The object containing content details. |  |
|  | title |  | Optional | The title of the meesage. | String |
|  | text |  | Required | The text message. | String |
|  | attachment |  | Optional | Refers to the object containing the attachment details if any | Object |
|  |  | type | Optional | Type of attachment. VIDEO, IMAGE, DOC, AUDIO, etc. | String |
|  |  | url | Optional | The url of the attachment. | URL |
|  |  | title | Optional | The title of the attachment. | URL |
|  |  | attachmentOptions{ 				channelType 				accountId 				} | Required | Array of attachment properties per channel and/or account.{ for media options.If the properties are specific to an account inaddition to channelType, accountId can be specified and the properties would then only be used for the given account} | String,Integer |
| scheduleDate |  |  | Required | Schedule date for the message | Epoch |
| taxonomy |  |  | Required | The object containing taxonomy details |  |
|  | campaignId |  | Required | Campaign identifier to associate the message. | String |
|  | clientCustomProperties |  | Optional | client custom properties for the message | String |
|  | partnerCustomProperties |  | Optional | partner custom properties for the message | String |
|  | tags |  | Optional | Tags to be added to the message | String |
|  | urlShortenerId |  | Optional | Url shortner identifier to apply to the message | String |
| approval |  |  | Optional | The object containing approval details |  |
|  | type |  | Required | Type of approval to process. defaults to NONE 				 				Enum: [ ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE ] | String |
|  | id |  | Required | Value for the chosen approval type. | String |
| toProfile |  |  | Required | The object containing fan profile details | Integer |
|  | channelType |  | Required | of the profile | String |
|  | channelId |  | Required | Channel Id of the profile | String |
|  | screenName |  | Optional | Screen name of the profile.Required if the channelType is TWITTER | String |

**Dev Notes: **`messageId`= **sourceType** (ACCOUNT, PERSISTENT_SEARCH, LISTENING) + “_”+ **sourceId** + “_” + **channelCreatedTime** + “_” + “**[channelType](https://dev.sprinklr.com/channels-v1)**” + “_” + ” **[messageType](https://dev.sprinklr.com/message-v1)**“ +”_” + **channelMessageId**

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
     "accountId": 600039042,
    "content": {
        "text":"hello from spr",
         "attachment": {
            "type": "IMAGE",
            "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg"
        }
    },
    "taxonomy": {
        "campaignId": "2_8104"
    },
    "inReplyToMessageId": "ACCOUNT_100172984_1619184258756_SPRINKLR_LIVE_CHAT_313_6082ca8257bc666265911034",
    "toProfile": {
        "channelType": "SPRINKLR_LIVE_CHAT",
        "channelId": "6082ca8257bc666260011034"
    },
    "approval": {}
}'
 

     
     
   

## Example - Response

 
 
     

{
    "data": [
        "POST_600000018628713"
    ],
    "errors": []
}
 

     
     
   
 

	[](https://dev.sprinklr.com/publishing-message) 

 

 
[Back to top](https://dev.sprinklr.com/publishing-message)
