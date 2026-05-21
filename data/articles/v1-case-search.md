---
title: "v1 Case Search"
slug: v1-case-search
url: https://dev.sprinklr.com/v1-case-search
---

# v1 Case Search

#
POST v1 Case Search

You can search for Case details using sorting and filters via this API call. You will get the list of objects that match your search call after making the request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/case/search

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

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| query | Required | Keywords to search | String |
| filters | Required | Filters for searchingfilterType:IN("Containing"), EQUALS("Equals") | List of Case Filter Objects given below |
| paginationInfo | Required | Pagination information.Refer to the table below for paginationInfo object fields' description. | Pagination Object |
| channelType | Required | Channel type will always remain SPRINKLR | String |

### paginationInfo Object Description

****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| sinceDate | Optional | The starting date from when you want to fetch cases | Epoch |
| untilDate | Optional | The ending date till when you want to fetch cases | Epoch |
| start | Optional | Refers to the start offsetDefault=0 | Integer |
| rows | Optional | The number of rows to fetch, starting from the configured start offset | Integer |
| sortKey | Optional | Refers to how you want to sort the results in the response.Example: caseCreatedTime, caseModifiedTime | String |

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
caseNumber
channelCaseNumber
caseCreationTime
insAppId
caseSubTypes
insAppOrgId
caseModificationTime
queueAssignedTime
userAssignedTime
message
messageAssociationTime
deleted
archived
subscriber
subscribedByMe
queue
assignedToUserId
tags
createdBy
assignedByUserId
assignedToMe,
assignedByMe
assignedByUserId
searchSummary
channelCustomField
sourceChannelType
sourceId
caseChannelCreationTime
caseChannelModificationTime
 

     
     
   

### Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
		curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/case/search' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
 "query":"hello",
    "filters":[
        {
            "filterType":"IN",
            "field":"channelType",
            "values":[
                "SPRINKLR"
            ]           /* channelType is always SPRINKLR */
        }
    ],
    "paginationInfo":{
        "sinceDate":1475055642000,
        "untilDate":1476092504000,
        "start":0,
        "rows":0,
        "sortKey":"caseModificationTime"
    }
}'
 

     
     
 

### Example - Response

 
 
     
 
{
   "searchResults":[
      {
         "universalCaseApiDTO":{
            "id":"57f4e123e4b0aac4b307b1d1",
            "version":0,
            "channelType":"SPRINKLR",
            "subject":"#2161049 Twitter A mother's love for ",
            "description":"A mother's love for her disabled son - carers call for more help to plan for the future @bbcnewsline 6.30 https://t.co/cvgFcoBVY7",
            "createdByUserId":-100,
            "associatedUniversalMessages":[
               {
                  "universalMessageKey":{
                     "universalMessageId":"TWITTER_4_781159648669892608",
                     "snType":"TWITTER",
                     "msgType":4,
                     "snMsgId":"781159648669892608",
                     "sourceId":10083,
                     "sourceType":"PERSISTENT_SEARCH",
                     "snCreatedTimeYearMonth":"2016_09",
                     "snCreatedTime":1475077948000
                  }, "universalMessageKeyStr":"TWITTERπ4π781159648669892608πPERSISTENT_SEARCHπ10083π1475077948000π2016_09", "universalMessageKeyStrWithBrandPost":"TWITTERπ4π781159648669892608πPERSISTENT_SEARCHπ10083π1475077948000π2016_09πfalse",
                  "conversationId":"781159648669892608",
                  "fromSnUserId":"TWITTER_485844797",
                  "associatedTime":1475666211304,
                  "associationType":"Case",
                  "fromSnUser":{
                     "sN":"taramillstv",
                     "pIU":"http://pbs.twimg.com/profile_images/725785199007662080/sBbQkSDC_normal.jpg",
                     "uI":"485844797"
                  },
                  "slaIndex":1,
                  "isBrandPost":false,
                  "sentiment":0,
                  "isFirstSLA":false
               }
            ],
            "caseChannelModificationTime":1475666211314,
            "caseCreationTime":1475666211304,
            "caseModificationTime":1475666211314,
            "deleted":false,
            "universalCaseWorkflow":{
               "que":[
               ],
               "comm":[
               ],
               "cProp":{
               },
               "arc":false
            },
            "fromSnAndUserId":"TWITTER_485844797",
            "fromUserSocialNetwork":"TWITTER",
            "fromSnUserId":"485844797",
            "caseNumber":2161049,
            "latestProfileAUMSnCreatedTime":1475077948000,
            "latestMessageAssociationUpdateTime":1475666211304,
            "latestAUMSnCreatedTime":1475077948000,
            "sourceId":10083,
            "associatedMessageCount":1,
            "associatedFanMessageCount":1,
            "associatedBrandMessageCount":0,
            "hasBrandResponded":false,
            "rootAUMSnCreatedTime":1475077948000,
            "commentCount":0,
            "customPropertyAssignmentInfo":{
               "assignmentInfoMap":{
               }
            },
            "hasRating":false,
            "sentiment":{
               "value":0,
               "computed":0,
               "normalizedComputed":0,
               "strategy":"FAN_MESSAGE_SUM"
            },
            "fanMsgCountSinceLastBrandResponse":0
         },
         "profile":{
            "snType":"TWITTER",
            "age":0,
            "location":"Belfast",
            "snId":"485844797",
            "name":"Tara Mills",
            "screenName":"taramillstv",
            "bio":"@bbcnewsline presenter and reporter 6.30/10.25pm @bbconeni",
            "following":1416,
            "followers":10315,
            "favCount":2751,
            "statusCount":3297,
            "permalink":"https://twitter.com/taramillstv",
            "createdTime":"1328633732000",
            "profileImgUrl":"http://pbs.twimg.com/profile_images/725785199007662080/sBbQkSDC_normal.jpg",
            "verified":false,
            "profileWorkflowProperties":{
               "comments":[
               ],
               "notifyUserIds":[
               ],
               "partnerProfileLists":[
               ],
               "clientProfileLists":[
               ],
               "partnerCustomProperties":{
               },
               "clientCustomProperties":{
               },
               "spaceCustomProperties":{
               },
               "userCustomProperties":{
               },
               "clientTags":[
               ]
            },
            "universalProfileId":"56308ceae4b068d744c66fd9",
            "participationIndex":0,
            "influencerIndex":0,
            "spamIndex":0,
            "accountsFollowedByUser":[
            ],
            "accountsFollowingUser":[
            ],
            "accountsUnFollowingUser":[
            ],
            "accountsUnFollowedByUser":[
            ],
            "accountsBlockingUser":[
            ],
            "urlEntities":{
               "bio":[
               ]
            },
            "textEntities":{
               "bio":[
                  {
                     "indices":[
                        0,
                        12
                     ],
                     "screenName":"bbcnewsline"
                  },
                  {
                     "indices":[
                        49,
                        58
                     ],
                     "screenName":"bbconeni"
                  }
               ]
            }
         },
         "actionTime":0
      }
  ],
"timeBasedCursor": 1475083000235,
"hasMore": false,
"totalHits": 59
}
 

     
     
   

### Response Definitions


























































































































































































































































































































































































































































































| Parameter | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Unique caseId in Sprinklr. | String |
| version |  | Version of the case. | Integer |
| channelType |  | Channel type on which the case is created. e.g Sprinklr | String |
| channelCaseId |  | Unique id of the case in the channel. | String |
| channelCaseNumber |  | Unique and readable Id in the channel | String |
| subject |  | The subject of the case. | String |
| description |  | The description of the case. | String |
| channelOwnerId |  | UserId of the CRM user. e.g. salesforce userId | String |
| createdByUserId |  | Id of the Sprinklr user who created this case | String |
| dueDate |  | Due date of the case | Epoch |
| associatedUniversalMessages |  | Object containing multiple universal messages which are linked to this case | List |
|  | universalMessageKey | Object containing details related to a messsage. The deails are given below in Universal Message Key Object definitions. | List <String> |
|  | universalMessageKeyStr | The univesal message key as a string. | String |
|  | universalMessageKeyStrWithBrandPost | The universal message key as string for brandpost. | String |
|  | conversationId | The conversation Id generated on sprinklr side with respect to a case conversation. | String |
|  | fromSnUserId | The user id of the user. | String |
|  | associatedTime | The time of association od message. | String |
|  | associationType | The type of association. | String |
|  | fromSnUser | The object containg the userName, user profile image and unique userId. | List<String> |
|  | isBrandPost | If true, brand response is present. | Boolean |
|  | sentiment | The Sentiment of the associated message. | Integer |
|  | isFirstSLA | Boolean value representing the SLA. | Boolean |
| caseChannelCreationTime |  | Creation time of case in the channel | Epoch |
| caseChannelModificationTime |  | Modification time of case in the channel | Epoch |
| caseCreationTime |  | Creation time of the universal case. | Epoch |
| caseModificationTime |  | Modification time of the universal case. | Epoch |
| universalCaseWorkflow |  | Case workflow details | object |
| fromSnAndUserId |  | The social network and unique id of the user. | String |
| fromUserSocialNetwork |  | The social network to which user belogs. | String |
| fromSnUserId |  | The user unique Id. | String |
| caseNumber |  | The case number associated with user message. | Long |
| latestProfileAUMSnCreatedTime |  | Time when the latest message from the snUser is associated. snUser is the user of the first message associated to the case. | Epoch |
| latestMessageAssociationUpdateTime |  | The time when the last modification was done on associated messages be it deletion or addition. | Epoch |
| latestAUMSnCreatedTime |  | The SnCreated time of the latest associated universal message (AUM). | Epoch |
| sourceId |  | re>Source id of the first message associated while creation. | String |
| associatedMessageCount |  | The number of associated message. | Integer |
| associatedFanMessageCount |  | The number of fan associated message. | Integer |
| associatedBrandMessageCount |  | The number of  brand associated message. | Integer |
| hasBrandResponded |  | Boolean value, is there a associated message to this case which has been posted by brand. | Boolean |
| rootAUMSnCreatedTime |  | First associated universal message (AUM) sn created time. | Epoch |
| commentCount |  | The comment count. | Integer |
| customPropertyAssignmentInfo |  | Object containing channel custom properties details. | Object |
| hasRating |  | If true, the rating object will come in response. | Object |
| sentiment |  | The object containing sentiment details. | Object |
| profile |  | The object containing profile details. |  |
|  | snType | The native channel of the user. | String |
|  | age | The age of the user. | Integer |
|  | location | The location of the user. | String |
|  | snId | The unique Id of the user. | String |
|  | name | The name of the user. | String |
|  | screenName | The screen name of the user. | String |
|  | bio | The bio of the user. | String |
|  | following | The number of profile that user is following | Integer |
|  | followers | The number of followers of the user. | Integer |
|  | favCount | The fav count of the user. | Integer |
|  | statusCount | The status count of the user. | Integer |
|  | permalink | The permalink to user profile. | String |
|  | createdTime | The created time of the profile | Epoch |
|  | profileImgUrl | The url to user profile image. | String |
|  | verified | If true, the user have a verified profile. | Boolean |
|  | profileWorkflowProperties | Object containing profile workflow details. |  |
|  | universalProfileId | The universal profile id of the user in Sprinklr. | String |
|  | participationIndex | The participation index. | Integer |
|  | influencerIndex | The influencer index of the user. | Integer |
|  | spamIndex | The spam index of the user. | Integer |
|  | accountsFollowedByUser | The list of accounts followed by the user. | Integer |
|  | accountsFollowingUser | The list of accounts following the user. | Integer |
|  | accountsUnFollowingUser | The list of accounts unfollowed the user. | Integer |
|  | accountsUnFollowedByUser | The list of accounts unfollowed by user. | Integer |
|  | accountsBlockingUser | The list of accounts blocing user. | Integer |
|  | urlEntities | The object of url entities. |  |
|  | textEntities | The object of text entities, |  |
|  | actionTime | The action time. | Integer |
| timeBasedCursor |  | The cursor representing time in Epoch | Epoch |
| hasMore |  | If true, more data is available within the same time range. | Boolean |
| totalHits |  | The number of total hits. | Integer |

###  Universal Message Key Object Definitions



| Parameter | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| universalMessageKey |  | The object containg message details. |  |
|  | universalMessageId | The universal message Id of the message within Sprinklr. | String |
|  | snType | The social network from ehich the message is grabbed. | String |
|  | msgType | The type of message as per Sprinklr. | Integer |
|  | snMsgId | The unique message id. | String |
|  | sourceId | The source account Id if the message. | String |
|  | sourceType | The source type of the message. | String |
|  | snCreatedTimeYearMonth | The created time of year and month. | Year_Month |
|  | snCreatedTime | The created time of the message. | Epoch |

###  Rating

If the response have `"hasRating":true` then you will receive the object containing rating details.
 
 
     
 
"rating": {
                    "min": 1.0,
                    "max": 5.0,
                    "actual": 5.0,
                    "normalized": 5.0,
                    "date": 1590461567000,
                    "entity": {
                        "FROM_USER_ID": "627081281",
                        "HAS_FEEDBACK_RECEIVED": "true",
                        "CREATED_TIME": "1590461567000",
                        "FEEDBACK_STATUS_ID": "1265113266340204554",
                        "TO_USER_ID": "2815754953",
                        "ID": "1265113266294083585",
                        "TYPE": "csat"
                    }
                },
 

     
     
   
 

### Response Definition



| Parameter | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| min |  | Minimum Rating option given to user. | Float |
| max |  | Maximum Rating option given to user. | Float |
| actual |  | The rating given by user. | Float |
| normalized |  | [(actual*5)/max], Since there are different types, like CSAT, NPS etc to normalize it. | Float |
| date |  | Feedback Updated Date or the time it was stored in sprinklr if the data was missing from twitter. | Epoch |
| entity |  | Object containg the details. |  |
|  | FROM_USER_ID | Brand User Id. | String |
|  | HAS_FEEDBACK_RECEIVED | Whether user has clicked on feedback button. | Boolean |
|  | CREATED_TIME | Time when the user clicked on feedback or the time it was stored in sprinklr if the data was missing from twitter. | Epoch |
|  | FEEDBACK_STATUS_ID | The Direct Message ID. | String |
|  | TO_USER_ID | Fan User Id. | String |
|  | ID | Id | String |
|  | TYPE | CSAT is from 1 to 5, NPS is from 0 to 10 | Integer |

	[](https://dev.sprinklr.com/v1-case-search) 

 

 
[Back to top](https://dev.sprinklr.com/v1-case-search)
