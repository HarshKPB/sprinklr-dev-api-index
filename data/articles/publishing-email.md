---
title: "Publishing Email"
slug: publishing-email
url: https://dev.sprinklr.com/publishing-email
---

# Publishing Email

#
POST Publishing Email


You can use this API endpoint to send either a proactive reply or to reply  using existing message Id.

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
| workspace_id | workspaceId | This field is optional. If your authorization token is associated with multiple workspaces, you'll have to pass workspace_id in the headers for publishing email. You can use  to check the workspace Id your token is primarily associated with. |

### Request Parameters

































































































































		``
















































































		``




















| Parameters | Sub Parameters | Sub-Param objects | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- | --- |
| accountId |  |  | Required | array of account ids to schedule message to | Integer |
| content |  |  | Required | The object containing content details. | Object |
|  | title |  | Optional | The title of the meesage. | String |
|  | text |  | Required | The text message. | String |
|  | attachment |  | Optional | Type of attachment | Object |
|  |  | type | Optional | Type of attachment. VIDEO, IMAGE etc. | String |
|  |  | url | Optional | The url of attachment. | URL |
| scheduleDate |  |  | Optional | Schedule date for the message | Epoch (miliseconds) |
| taxonomy |  |  | Required | The object containing taxonomy details | Object |
|  | campaignId |  | Required | Campaign identifier to associate the message. | String |
|  | clientCustomProperties |  | Optional | client custom properties for the message | String |
|  | partnerCustomProperties |  | Optional | partner custom properties for the message | String |
|  | tags |  | Optional | Tags to be added to the message | String |
|  | urlShortenerId |  | Optional | Url shortner identifier to apply to the message | String |
| inReplyToMessageId |  |  | Optional | The message id on which the reply is being sent. This should only be used in case of reply. Please check the sample api call "Email Reply" below. | String |
| approval |  |  | Optional | The object containing approval details |  |
|  | type |  | Optional | Type of approval to process. defaults to NONE 			 			Enum: [ ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE ] | String |
|  | id |  | Optional | Value for the chosen approval type. | String |
| channelOptions |  |  | Required | The object containing email details. | Object |
|  | toEmailAddress |  | Required | The email address, to whom you want to send email. | String |
|  | ccEmailAddress |  | Optional | The cc email addresses. | String |
|  | bccEmailAddress |  | Optional | The bcc email addresses. | String |
|  | channelType |  | Required | The channel type, by-default EMAIL. | String |
|  | caseId |  | Optional | The case to which you want to associate this email. Required incase of proactive email if you want to associate it with existing case. | String |
| toProfile |  |  | Required | The profile information.This should only be used incase of proactive email. Please check the sample api call "Proactive Email" below. | Integer |
|  | channelType |  | Required | Channel Type of the profile | String |
|  | channelId |  | Required | Channel Id of the profile | String |

### Example: Email Reply

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
    "inReplyToMessageId": "ACCOUNT_67106_1631765597768_EMAIL_175_31EC3EF2E76BC302298B699D7D3ED",
    "accountId": 600017106,
    "content": {
        "text": "TEST EMAIL FROM API WITH IMAGE",
        "title":"IMAGE EMAIL",
        "attachment": {
            "type": "IMAGE",
            "url": "https://sprcdn-prod0-sam.sprinklr.com/9004/path.jpeg-3b11b945-536a-4eb5-8957-ffd8a582b698-2004310276.jpg",
			"previewUrl":"https://sprcdn-prod0-sam.sprinklr.com/9004/path.jpeg-3b11b945-536a-4eb5-8957-ffd8a582b698-2004310276_p.jpg"
        }
    },
    "taxonomy": {
        "campaignId": "2_3642"
    },
    "approval": {},
    "channelOptions": [
        {
            "toEmailAddress": [
                "xyz@abc.com"
            ],
            "ccEmailAddress": [],
            "bccEmailAddress": [],
             "channelType":"EMAIL"
        }
    ]
}'
 

     
     
   

### Example - Response

 
 
     
 
{
    "data": [
        "POST_4709998975"
    ],
    "errors": []
}
 

     
     
   
 

### Example: Proactive Email

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/message' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
    "accountId": 6000106,
    "content": {
        "text": "https://doubleclick.net/ddm/trackclk/N195005.",
        "title": "test link EMAIL"
  },
    "taxonomy": {
        "campaignId": "2_3642"
    },
    "approval": {},
    "channelOptions": [
        {
            "toEmailAddress": [
                "abc@xyz.com"
            ],
            "ccEmailAddress": ["a1@xyz.com"],
            "bccEmailAddress": ["a2@xyz.com"],
            "channelType": "EMAIL",
            "caseId": "61dc02830ae48f793a02b454"
        }
    ],
    "toProfile": {
			"channelType": "EMAIL",
            "channelId": "abc@xyz.com"
		}
}'
 

     
     
   

### Example - Response

 
 
     
 
{
    "data": [
        "POST_4709998998"
    ],
    "errors": []
}
 

     
     
   

	[](https://dev.sprinklr.com/publishing-email) 

 

 
[Back to top](https://dev.sprinklr.com/publishing-email)
