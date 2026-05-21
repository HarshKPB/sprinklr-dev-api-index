---
title: "v1 Case Read"
slug: v1-case-read
url: https://dev.sprinklr.com/v1-case-read
---

# v1 Case Read

#
GET v1 Case Read

You can fetch case details using the case Id with this API call. This call allows you to get customer interaction data as a threaded set of messages.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/case

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

## Query Parameter

****
****
****
****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| caseNumbers | Required | The unique case number you want to fetch details for | String |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v1/case?caseNumbers=123' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
 

     
     
   

### Example - Response

 
 
     
 
{
   "searchResults":[
      {
         "universalCaseApiDTO":{
            "id":"53c64a96e4b04bab28fd5f09",
            "version":0,
            "channelType":"SPRINKLR",
            "subject":"#20735 Twitter # Twitter adamwainwright I signed up for #Lea",
            "description":"I signed up for #LeadRocket. A #socialcrm #Sales App that helps me close deals via #email and #SocialMedia. Check it! http://t.co/0mjiqvs8xs",
            "createdByUserId":-100,
            "dueDate":1405881000000,
            "associatedUniversalMessages":[
               {
                  "universalMessageKey":{
                     "universalMessageId":"TWITTER_1_488883228808187904",
                     "snType":"TWITTER",
                     "msgType":1,
                     "snMsgId":"488883228808187904",
                     "sourceId":3156,
                     "sourceType":"ACCOUNT",
                     "snCreatedTimeYearMonth":"2014_07",
                     "snCreatedTime":1405393819000
                  },      "universalMessageKeyStr":"TWITTERπ1π488883228808187904πACCOUNTπ3156π1405393819000π2014_07",   "universalMessageKeyStrWithBrandPost":"TWITTERπ1π488883228808187904πACCOUNTπ3156π1405393819000π2014_07πfalse",
                  "conversationId":"488883228808187904",
                  "fromSnUserId":"TWITTER_9952532",
                  "associatedTime":1405504150113,
                  "associationType":"Case",
                  "fromSnUser":{
                     "sN":"adamwainwright",
                     "pIU":"http://pbs.twimg.com/profile_images/431878327230427136/suMvsLLS_normal.jpeg",
                     "uI":"9952532"
                  },
                  "slaIndex":1,
                  "isBrandPost":false,
                  "isFirstSLA":false
               }
            ],
            "caseCreationTime":1405504150113,
            "caseModificationTime":1426863921886,
            "deleted":false,
            "universalCaseWorkflow":{
               "que":[
                  {
                     "qId":306,
                     "qTm":1405504150113
                  }
               ],
               "comm":[
               ],
               "cProp":{
                  "spr_uc_type":[
                     "Complaint"
                  ],
                  "spr_uc_priority":[
                     "High"
                  ]
               },
               "subs":[
                  2610
               ],
               "uAD":{
                  "aTId":2610,
                  "aBId":-100,
                  "aTm":1405504150113
               },
               "arc":false
            },
            "fromSnAndUserId":"TWITTER_9952532",
            "fromUserSocialNetwork":"TWITTER",
            "fromSnUserId":"9952532",
            "caseNumber":20735,
            "dynamicTimeFields":{
               "q_306_d":1405504150113
            },
            "latestProfileAUMSnCreatedTime":1405393819000,
            "latestMessageAssociationUpdateTime":1405504150113,
            "latestAUMSnCreatedTime":1405393819000,
            "sourceId":3156,
            "associatedMessageCount":1,
            "associatedFanMessageCount":1,
            "associatedBrandMessageCount":0,
            "hasBrandResponded":false,
            "rootAUMSnCreatedTime":1405393819000,
            "commentCount":0,
            "customPropertyAssignmentInfo":{
               "assignmentInfoMap":{
                  "spr_uc_priority_High":{
                     "value":"High",
                     "assignmentTime":1415337539869
                  },
                  "spr_uc_type_Complaint":{
                     "value":"Complaint",
                     "assignmentTime":1415337539869
                  }
               }
            },
            "hasRating":false,
            "fanMsgCountSinceLastBrandResponse":0
         },
         "actionTime":0
      }
   ],
   "timeBasedCursor":1405504150113,
   "hasMore":false,
   "totalHits":1
}
	 

     
     
   

### Response Parameters

























































































































































































































































































































































































































































































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

### Rating

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
 

     
     
   
 

### Response Parameters



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

	[](https://dev.sprinklr.com/v1-case-read) 

 

 
[Back to top](https://dev.sprinklr.com/v1-case-read)
