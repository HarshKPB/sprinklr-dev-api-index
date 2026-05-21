---
title: "Post Draft Create v1"
slug: post-draft-create-v1
url: https://dev.sprinklr.com/post-draft-create-v1
---

# Post Draft Create v1

#
POST Post Draft Create v1

You can create a Draft Post via this API call, it can be either an original post or a reply to existing post. After making the API request, you will receive Message {Id} in the response.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/publishing/draft/new

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

## Request Parameters















            [type of message](https://dev.sprinklr.com/message)



[account](https://dev.sprinklr.com/account)

| Parameter | Sub Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| messageType |  | Required | Refers to the  you want to create draft forConfigure messagetype as "2" for original post for all channels | Enum |
| accountIds |  | Required | Account id refers to the unique identifier for the social  existing within Sprinklr | List [String] |
| content |  | Required | Object containing the message details | Object |
|  | message | Required | Refers to the message of the draft post | String |
|  | postName | Optional | Refers to the title of the post | String |
|  | attachment | Optional | Object Containing the attachment detailsRefer to the table below for attachment object details | Object |
| channelSpecificContentDetails |  | Required | Array containing channel specfic content details | Array |
|  | data | Required | Object containing channel specfic content detailsRefer to the table below for the data object details | Object |
|  | channelInfo | Required | Object Containing channel detailsRefer to the table below for channel info object description | Object |
| taxonomy |  | Required | Object containing the taxonomy details | Object |
|  | campaignId | Required | Refers to the campaign under which the post will be published | String |
|  | clientCustomProperties | Optional | The custom properties associated with the draft post | Object |
|  | partnerCustomProperties | Optional | The partner properties associated with the draft post | Object |
|  | tags | Optional | Tags to be assoviated with the draft post | String |
|  | campaignStartDate | Optional | The campaign start date | Epoch |
|  | campaignEndDate | Optional | The campaign end date | Epoch |
| parentUniversalMessageKey |  | Optional | If this post is in reply to a message like a comment/reply to a post, then this field is the reference to the parent message | String |
| inReplyToUniversalMessageKey |  | Optional | This uniquely identifies the message this post is replying toIt’s different from parentUniversalMessageKey.E.g., Client chooses to reply to a comment on a brand post. The parentUniversalMessageKey points to the brand post and inReplyToUniversalMessageKey points to the comment to reply |  |
| SCHEDULE_ON_FB |  | Optional | True, If the message is scheduled on FB | Boolean |
| originalPostId |  | Optional | If this message is a republish message, then originalPostId equals to the post to be republished | String |
| postAssetId |  | Optional | if this post was created by reusing a post type asset, then you should provide postAssetId | String |
| approval |  | Optional | Object containing the approval details (if any) | Object |
|  | approvalOption | Optional | Refers to the approval option | String |
|  | comment | Optional | Refers to the comment for approval (if any) | String |
| scheduledDate |  | Optional | Refers to the date and time at which the post will be scheduled for publishing | Epoch (milliseconds) |

### attachment Object Description Table

| Parameter | Sub Paramter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Refers to the type of attachment | String |
| mediaList |  | Required when attachment is configured | Refers to the media list for the attachement | Array |
|  | type | Optional | Refers to the type of the attachment | String |
|  | source | Required | Refers to the publically accessible url of the attachment | Url |

### channel Specific Content List Array Details

| Parameter | Sub Param | Sub Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- | --- |
| attachment |  |  | Required | Refers to the object defining the attachment details | Object |
|  | type |  | Required | Refers to the type of attachment | String |
|  | mediaList |  | Required when attachment is configured | Refers to the media list for the attachement | Array |
|  |  | type | Optional | Refers to the type of the attachment | String |
|  |  | source | Required | Refers to the publically accessible url of the attachment | Url |
|  |  | sizeInBytes | Optional | Refers to the size of the attachment | Integer |
| textEntities |  |  | Optional | Provides metadata and any additional details related to a message | Object |
| hasContentVariants |  |  | Optional |  | Boolean |

### channel Info Object Description Table

[channel type](https://dev.sprinklr.com/channels-v1)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| channelType | Required | Refers to the  for the post | string |
| accountType | Required | Refers to the account type associated with the post | String |

## Example: Reply to an Inbound message.

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/publishing/draft/new' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
   "messageType":14,
   "accountIds": ["2693"],
   "content":{
      "message":"replying from api as draft",
      "mediaList":[
      ]
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
   "parentUniversalMessageKey":{
      "universalMessageId":"FACEBOOK_15_388774087838191_949169871798607",
      "snType":"FACEBOOK",
      "msgType":14,
      "snMsgId":"388774087838191_949169871798607",
      "sourceId":"2693",
      "sourceType":"ACCOUNT",
      "snCreatedTime":"1470394900000",
      "snCreateTimeYearMonth":"2016_01"
   },
   "inReplyToUniversalMessageKey":{
      "universalMessageId":"FACEBOOK_15_388774087838191_949169871798607",
      "snType":"FACEBOOK",
      "msgType":14,
      "snMsgId":"388774087838191_949169871798607",
      "sourceId":"2693",
      "sourceType":"ACCOUNT",
      "snCreatedTime":"1470394900000",
      "snCreateTimeYearMonth":"2016_01"
   },
   "approval":{
      "approvalOption":"NONE",
      "comment":""
   },
   "scheduledDate":1462579200000
}'
 

     
     
   

## Example: Draft a new message.

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}api/v1/publishing/draft/new' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
    "messageType": 2,
    "accountIds": ["600001490"],
    "content": {
        "message": "test-3",
        "postName": "test-3",
        "attachment": {
            "type": "PHOTO",
            "mediaList": [
                {
                    "type": "PHOTO",
                    "source": "https://prod3-sprcdn-assets.sprinklr.com/150127/349c143f-3e04-1695943313/eyJhc3NldElkIjoiNjM3MjgxMDI5NT.png"
                }
            ]
        }
    },
    "channelSpecificContentList": [
        {
            "data": {
                "attachment": {
                    "type": "PHOTO",
                    "mediaList": [
                        {
                            "type": "PHOTO",
                            "source": "https://prod3-sprcdn-assets.sprinklr.com/150127/349c143f-3e04-1695943313/eyJhc3NldElkIjoiNjM3MjgxMDI5NT.png",
                            "sizeInBytes": 138382
                        }
                    ]
                },
                "textEntities": {
                    "message": []
                },
                "hasContentVariants": false
            },
            "channelInfo": {
                "channelType": "FACEBOOK",
                "accountType": "FBPAGE"
            }
        }
    ],
    "taxonomy": {
        "campaignId": "0_12730"
    },
    "scheduledDate": 1680766473000
}'
 

     
     
 

## Example - Response

 
 
     
 
{
    "messageId": 600000020777388,
    "channelSpecificAdditionalProperties": [
        {
            "data": {
                "SOURCE_ID": [
                    "MESSAGE_600000020777388"
                ],
                "AUTHOR_LOCALE": [
                    "en_US"
                ],
                "REQUEST_SOURCE": [
                    "API"
                ]
            },
            "channelInfo": {
                "channelType": "OUTBOUND"
            }
        }
    ],
    "channelSpecificContentList": [
        {
            "data": {
                "attachment": {
                    "type": "PHOTO",
                    "mediaList": [
                        {
                            "type": "PHOTO",
                            "source": "https://prod3-sprcdn-assets.sprinklr.com/150127/349c143f-3e04-43b2-8697-2bbaecff66f0-1695943313/eyJhc3NldElkIjoiNjM3MjgxMDI5NT.png",
                            "sizeInBytes": 138382
                        }
                    ]
                },
                "textEntities": {
                    "message": []
                },
                "hasContentVariants": false
            },
            "channelInfo": {
                "channelType": "FACEBOOK",
                "accountType": "FBPAGE"
            }
        }
    ],
    "ruleEngineExecuted": false,
    "editable": false,
    "unMaskedData": {},
    "universalId": "MESSAGE_600000020777388",
    "authorId": 600000003,
    "clientId": 1,
    "messageType": 2,
    "content": {
        "message": "test-3",
        "attachment": {
            "type": "PHOTO",
            "mediaList": [
                {
                    "type": "PHOTO",
                    "source": "https://prod3-sprcdn-assets.sprinklr.com/150127/349c143f-3e04-43b2-8697-2bbaecff66f0-1695943313/eyJhc3NldElkIjoiNjM3MjgxMDI5NT.png"
                }
            ]
        },
        "languageCode": "fr",
        "postName": "test-3",
        "hasContentVariants": false
    },
    "taxonomy": {
        "campaignId": "0_12730",
        "campaignStartDate": 0,
        "campaignEndDate": 0
    },
    "approval": {
        "approvalOption": "NONE"
    },
    "createdDate": 1681223702985,
    "createdTime": 1681223702985,
    "modifiedDate": 1681223702985,
    "modifiedTime": 1681223702985,
    "scheduleDate": 1680766473000,
    "scheduledTime": 1680766473000,
    "status": "DRAFT",
    "version": 0,
    "deleted": false,
    "category": "UPDATE",
    "hasConversation": false,
    "lockedUntil": 0,
    "documentType": "MESSAGE"
}
 

     
     
   
 

	[](https://dev.sprinklr.com/post-draft-create-v1) 

 

 
[Back to top](https://dev.sprinklr.com/post-draft-create-v1)
