---
title: "Publishing Reply"
slug: publishing-reply
url: https://dev.sprinklr.com/publishing-reply
---

# Publishing Reply

#
POST Publishing Reply


You can either send or schedule a reply via this API call.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/publishing/reply

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
| workspace_id | workspaceId | This field is optional. If your authorization token is associated with multiple workspaces, you'll have to pass workspace_id in the headers for publishing a reply. You can use  to check the workspace Id your token is primarily associated with. |

### Request Parameters











































































































































































































| Parameters | Sub Parameters | Sub-Param objects | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- | --- |
| accountId |  |  | Required | array of account ids to schedule message to | Integer |
| content |  |  | Required | The object containing content details. |  |
|  | title |  | Optional | The title of the meesage. | String |
|  | text |  | Required | The text message. | String |
|  | attachment |  | Optional | Type of attachment |  |
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
| channelOptions |  | Optional | Refers to the available channel specific options | Object |  |
|  | channelType | Required | Refers to the channel where the reply will be sent | String |  |
|  | addPrivateMsgLink | Optional | If true, a CTA button will be sent along with the reply that allows sending a private message instead | Boolean |  |
|  | accountId | Optional | Refers to the account id related to the account you are sending reply from | String |  |
| inReplyToMessageId |  |  | Required | The message id on which the reply is being sent | String |
| approval |  |  | Optional | Object Containing the approver details. |  |
|  | type |  | Required | Type of approval to process. defaults to NONE 				 				Enum: [ ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE ] | String |
|  | id |  | Required | Value for the chosen approval type. | String |
| toProfile |  |  | Required | Object containing the profile details. | Integer |
|  | channelType |  | Required | Channel Type of the profile | String |
|  | channelId |  | Required | Channel Id of the profile | String |
|  | screenName |  | Optional | Screen name of the profile | String |

**Dev Notes: **`inReplyToMessageId`= **sourceType** (ACCOUNT, PERSISTENT_SEARCH, LISTENING) + “_”+ **sourceId** + “_” + **channelCreatedTime** + “_” + “**[channelType](https://dev.sprinklr.com/channels-v1)**” + “_” + ” **[messageType](https://dev.sprinklr.com/message-v1)**“ +”_” + **channelMessageId**

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/publishing/reply' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountId": 600039042,
    "content": {
        "text": "Test Publish Reply API"
    },
    "taxonomy": {
        "campaignId": "2_12507"
    },
    "channelOptions": {
        "channelType": "TWITTER",
        "addPrivateMsgLink": true,
        "accountId": 600039042
    },
    "inReplyToMessageId": "ACCOUNT_600039042_1681712914200_TWITTER_7_1647849513338679298",
    "toProfile": {
        "channelType": "TWITTER",
        "channelId": "1403229140287848455"
    }
}'
 

     
     
   

**Dev Notes: **When publishing a reply to a Twitter mention, kindly append `@username` (sender's username) as a prefix in the "`text`" field under the content object.

## Example - Response

 
 
     
 
{
    "data": [
        "POST_4908765975"
    ],
    "errors": []
}
 

     
     
   
 

	[](https://dev.sprinklr.com/publishing-reply) 

 

 
[Back to top](https://dev.sprinklr.com/publishing-reply)
