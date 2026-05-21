---
title: "Twitter Dynamic Templates"
slug: twitter-dynamic-templates
url: https://dev.sprinklr.com/twitter-dynamic-templates
---

# Twitter Dynamic Templates

#
POST Twitter Dynamic Templates

You can use this API to publish quick replies on supported social and messaging channels. Within the Request Parameters you will find the fields that you can pass in API payload while calling the API. Once you make a successful call you will get the Post Id of the published message. The API samples for different channel types are given below:


**Dev Notes: **This API enhancement strictly works for ` "channelType": "TWITTER"`.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/publishing/message

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

##  Request Parameters



























































































```

```


































































































































| Parameters | Sub Parameters | Sub-Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- | --- |
| accountId |  |  | Required | array of account ids to schedule message to | Integer |
| content |  |  | Required |  |  |
|  | title |  | Optional | Title of the message. | String |
|  | text |  | Optional | Text of the message. | String |
|  | attachment |  | Required | Type of attachment | String |
|  |  | type | Required | QUICK_REPLY, by default. | String |
|  |  | title | Required | Title of the card. | String |
|  |  | previewImageUrl | Required | Preview image URL. | String |
|  |  | disableManualResponse | Required | false, by default. | Boolean |
|  |  | buttons 				                         [ { "id" : "", "title" : "", "subtitle" : "", "payload" : "", "actionDetail" : { "action" : "" } } ] | Required | Check the Button Description Table below. | String,Integer |
| scheduleDate |  |  | Required | Schedule date for the message | Integer |
| taxonomy |  |  | Required | Object containing taxonomy details. |  |
|  | campaignId |  | Required | Campaign identifier to associate the message. | String |
|  | clientCustomProperties |  | Optional | client custom properties for the message | String |
|  | partnerCustomProperties |  | Optional | partner custom properties for the message | String |
|  | tags |  | Optional | Tags to be added to the message | String |
|  | urlShortenerId |  | Optional | Url shortner identifier to apply to the message | String |
| inReplyToMessageId |  |  | Required | The message id on which the reply is being sent | String |
| approval |  |  | Optional |  |  |
|  | type |  | Optional | Type of approval to process. defaults to NONE 				 				Enum: [ ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE ] | String |
|  | id |  | Optional | Value for the chosen approval type. | String |
| toProfile |  |  | Required | Current version of the message. | Integer |
|  | channelType |  | Required | Channel Type of the profile | String |
|  | channelId |  | Required | Channel Id of the profile | String |
|  | screenName |  | Required | Screen name of the profile | String |

### Button Parameter Description






































``




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Id | Required | Any unique id. | String |
| title | Required | Title of button. | String |
| subtitle | Optional | Sub-title of button. | String |
| payload | Optional | Payload of button. Not supported in Facebook and Twitter | String |
| action Details | Required | In case of  QUICK_REPLY the possible action is:  "actionDetail" : {               "action" : "TEXT"             } | String |

## Example: Twitter

 
 
       
 
 
 
 
 
 
 
 
 
 
 
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
        "text": "again template check",
    "attachment": {
        "type": "QUICK_REPLY",
        "message": "Question 16",
        "quickReplies": [
            {
                "title": "Option 16",
                "subtitle": "Flower",
                "imageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/510adab7-9d1f-4fb1-83d4-56d28615c36a-738970249/headline_firstimage11_p.jpg",
                "actionDetail": {
                    "action": "TEXT"
                }
            }
        ]
    }
    },
    "taxonomy": {
        "campaignId": "4_4041"
    },
    "inReplyToMessageId": "ACCOUNT_600039042_1632239340936_TWITTER_5_1440342307102879748",
    "toProfile": {
        "channelType": "TWITTER",
        "channelId": "2558998452",
        "screenName" : "ITest"
    }
}'
 

     
     
   

## Example - Response





{
    "data": [
        "POST_600000006374279"
    ],
    "errors": []
}
 

     
     
   
 

	[](https://dev.sprinklr.com/twitter-dynamic-templates) 

 

 
[Back to top](https://dev.sprinklr.com/twitter-dynamic-templates)
