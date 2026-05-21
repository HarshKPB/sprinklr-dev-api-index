---
title: "Post Draft Read v1"
slug: post-draft-read-v1
url: https://dev.sprinklr.com/post-draft-read-v1
---

# Post Draft Read v1

#
GET Post Draft Read v1

You can fetch a Drafted Message via this API call. After making the GET Request, you will get the Message Objects in JSON format as Response.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/outbound/drafts

## Headers

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

## Query Parameters

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| messageId | Required | The id of the drafted post | Integer |

### Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/outbound/drafts?messageIds=78377'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
   

### Example - Response

 
 
     
 
[
   {
      "messageId":5762499,
      "accountIds":[
         2693
      ],
      "accountGroupIds":[
      ],
      "channelSpecificContentList":[
         {
            "data":{
               "message":"replying from api as draft",
               "languageCode":"en",
               "hasContentVariants":false
            },
            "channelInfo":{
               "channelType":"FACEBOOK",
               "accountId":2693
            }
         }
      ],
      "ruleEngineExecuted":false,
      "editable":true,
      "documentType":"MESSAGE",
      "universalId":"MESSAGE_5762499",
      "authorId":2008,
      "clientId":193,
      "messageType":14,
      "content":{
         "message":"replying from api as draft",
         "languageCode":"en",
         "hasContentVariants":false
      },
      "taxonomy":{
         "campaignId":"193_6",
         "clientCustomProperties":{
            "AM_Local_1":[
               "field1"
            ],
            "AM_Local_2":[
               "pick1"
            ]
         },
         "tags":[
         ],
         "urlShortnerDomain":"5532909ee4b0162c9d34aa6b",
         "assetVisibility":{
            "shareConfigList":[
               {
                  "shareLevel":"GLOBAL"
               }
            ]
         }
      },
      "approval":{
         "approvalOption":"NONE",
         "comment":""
      },
      "createdDate":1462569370000,
      "createdTime":1462569370102,
      "modifiedDate":1462569370000,
      "modifiedTime":1462569370102,
      "scheduleDate":1462579200000,
      "scheduledTime":1462579200000,
      "status":"DRAFT",
      "parentUniversalMessageKey":{
         "universalMessageId":"FACEBOOK_15_388774087838191_949169871798607",
         "snType":"FACEBOOK",
         "msgType":14,
         "snMsgId":"388774087838191_949169871798607",
         "sourceId":2693,
         "sourceType":"ACCOUNT",
         "snCreatedTimeYearMonth":"1970_01",
         "snCreatedTime":0
      },
      "inReplyToUniversalMessageKey":{
         "universalMessageId":"FACEBOOK_15_388774087838191_949169871798607",
         "snType":"FACEBOOK",
         "msgType":14,
         "snMsgId":"388774087838191_949169871798607",
         "sourceId":2693,
         "sourceType":"ACCOUNT",
         "snCreatedTimeYearMonth":"1970_01",
         “snCreatedTime”:”1470394900000”
      },
      "version":0,
      "deleted":false,
      "category":"COMMENT",
      "hasConversation":false,
      "lockedUntil":0
   }
]
	 

     
     
   
 

	[](https://dev.sprinklr.com/post-draft-read-v1) 

 

 
[Back to top](https://dev.sprinklr.com/post-draft-read-v1)
