---
title: "v1 Case Update"
slug: v1-case-update
url: https://dev.sprinklr.com/v1-case-update
---

# v1 Case Update

#
POST v1 Case Update


Using this API, you can update a case within Sprinklr.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/case/update

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
| caseIds | Required | The Sprinklr id for the case. | String |
| caseNumbers | Required | The case numbers. | Long |
| addedAssociatedMessages | Required | Messages to associate to the case. | List of Associated Universal Message Object |
| removedAssociatedMessages | Required | Messages to disassociate to the case. | List of Associated Universal Message Object |
| subject | Required | The subject of the case. | String |
| description | Required | The description of the case. | String |
| additionalInformation | Required | Additional information related to the case. | Map String, Object |
| syncedMediaList | Required | Media lists associated with a case. | List of Media Objects |
| type | Required | The type of case. | String |
| additionalCustomProperties | Required | Custom properties associated with the case. | Map<String, List<String>> |
| removedCustomProperties | Required | Custom properties to be removed from a case. | Map<String, List<String>> |
| synchedCustomProperties | Required | Custom properties in sync with the case. | Map<String, List<String>> |
| assignedTo | Required | The assigned user for the case. | Long |
| dueDate | Required | The due date of the case. | Long |
| addedNotifyUsers | Required | Users to be notified. | Long |
| removedNotifyUsers | Required | Users to be removed from notification. | Long |
| syncedNotifyUsers | Required | Users to be notified. | Long |
| comment | Required | The comment on the case. | String |
| archived | Optional | Set to TRUE if you wish to archive the case. | Boolean |
| sentiment | Required | The sentiment of the case. | Integer |
| addedQueues | Required | Queues to which to add the case. Queues are used to store cases based on like conditions that can be configured and automated in the Rule Engine. You can think of queues as invisible folders that house and organise your cases. | Long |
| removedQueues | Required | Queues to remove the case from. To disassociate a case from similar cases. | Long |
| syncedQueues | Required | Queues to sync the case. | Long |
| updateActions | Required | Actions to be performed. | Universal Case Update Actions |
| changeInCommentCount | Required | The comment count. | Long |
| dissociateCaseIds | Required | The case Ids to dissociate from the case. When you disassociate a case, all the information from the similar cases will be removed. | String |
| installedAppId | Required | The App Id of the application installed and related to the case. | String |
| applicationUserId | Required | The App User Id of the application installed and related to the case. | String |
| updateCustomFieldsinCRM | Required | If True, the custom field will get updated in the CRM. Default = TRUE. | Boolean |
| ignoreSLAReporting | Optional | A service-level agreement (SLA) is a part of a service contract where a service is formally defined. In practice, the term SLA is sometimes used to refer to the contracted delivery time (of the service or performance).Default = FALSE. | Boolean |
| summary | Required | The summary of the case. | String |
| shouldTriggerUpdateEventRuleEvent | Optional | Rule Triggers are initiated to prompt content in the case to run through the Rule Engine according to the configuration of that Rule Trigger. Default = TRUE. | Boolean |
| latestBrandResponseByUserId | Required | An id of the user for the brand response. | Long |
| latestBrandResponseTime | Required | Time of the brand response. | Long |

### Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/case/update' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "caseNumbers": [22397],
  "updateActions": ["REMOVE_ASSOCIATED_MESSAGES"],
  "addedAssociatedMessages": [{
  "universalMessageKey": {
  "universalMessageId": "FACEBOOK_15_552086084921463_885739281556140",
  "snType": "FACEBOOK",
  "msgType": 15,
  "snMsgId": "552086084921463_885739281556140",
  "sourceType": "ACCOUNT",
  "snCreatedTimeYearMonth": "2016_09"
    }
  }
]
}'
 

     
     
   

### Example - Response

 
 
     
 
		{
   "id":"5800bed2e4b0b2161708a4ae",
   "version":3,
   "cType":"SPRINKLR",
   "sub":"Testing1",
   "desc":"Testing the case api endpoint for create a case1",
   "cByUI":420,
   "aUM":[
      {
         "universalMessageKey":{
            "universalMessageId":"FACEBOOK_15_552086084921463_885739874889414",
            "snType":"FACEBOOK",
            "msgType":15,
            "snMsgId":"552086084921463_885739874889414",
            "sourceId":1163,
            "sourceType":"ACCOUNT",
            "snCreatedTimeYearMonth":"2016_10",
            "snCreatedTime":1475147952000
         }, "universalMessageKeyStr":"FACEBOOKπ15π552086084921463_885739874889414πACCOUNTπ1163π1475147952000π2016_10",         "universalMessageKeyStrWithBrandPost":"FACEBOOKπ15π552086084921463_885739874889414πACCOUNTπ1163π1475147952000π2016_10πfalse",
         "fromSnUserId":"FACEBOOK_552086084921463",
         "associatedTime":1476443858843,
         "associationType":"Case",
         "fromSnUser":{
            "uI":"552086084921463",
            "n":"Apple",
            "uN":"Apple"
         },
         "slaIndex":1,
         "isBrandPost":false,
         "sentiment":1,
         "isFirstSLA":false
      },
      {
         "universalMessageKey":{
            "universalMessageId":"FACEBOOK_15_552086084921463_885739281556140",
            "snType":"FACEBOOK",
            "msgType":15,
            "snMsgId":"552086084921463_885739281556140",
            "sourceId":-1,
            "sourceType":"ACCOUNT",
            "snCreatedTimeYearMonth":"2016_09",
            "snCreatedTime":0
         },         "universalMessageKeyStr":"FACEBOOKπ15π552086084921463_885739281556140πACCOUNTπ-1π0π2016_09",    "universalMessageKeyStrWithBrandPost":"FACEBOOKπ15π552086084921463_885739281556140πACCOUNTπ-1π0π2016_09πfalse",
         "associatedTime":1476512746062,
         "associationType":"Case",
         "slaIndex":1,
         "isBrandPost":false,
         "isFirstSLA":false
      }
   ],
   "cCMT":1476443858856,
   "cCT":1476443858843,
   "cMT":1476513534957,
   "del":false,
   "uCW":{
      "que":[
         {
            "qId":2998,
            "qTm":1476512190647
         }
      ],
      "comm":[
      ],
      "cProp":{
      },
      "subs":[
      ],
      "uAD":{
         "aTId":420,
         "aBId":420,
         "aTm":1476512190647
      },
      "arc":true
   },
   "Ad":{
      "iFSAC":"true"
   },
   "addInfo":{
      "rCP":{
         "flatCustomProperties":[
            "ALL"
         ],
         "customPropertyNames":[
         ],
         "mappedCustomProperties":{
         }
      }
   },
   "fSAUId":"FACEBOOK_552086084921463",
   "fUSN":"FACEBOOK",
   "fSUId":"552086084921463",
   "caseNu":22397,
   "dCNu":"22397",
   "dtf":{
      "q_2998_d":1476512190647
   },
   "sSummary":"22397 Testing1 Testing the case api endpoint for create a case1 null 552086084921463_885739874889414 552086084921463_885739281556140",
   "lPASCT":1475147952000,
   "lMAUT":1476513534957,
   "lFMAT":1476512746062,
   "lAUMSCT":0,
   "sId":1163,
   "aMCnt":2,
   "aFMCnt":2,
   "aBMCnt":0,
   "hBR":false,
   "rAUMSCT":1475147952000,
   "cCnt":1,
   "cPAInfo":{
      "assignmentInfoMap":{
      }
   },
   "hasRating":false,
   "sentiment":{
      "value":1,
      "computed":1,
      "normalizedComputed":1,
      "strategy":"FAN_MESSAGE_SUM"
   },
   "rMK":{
      "universalMessageId":"FACEBOOK_15_552086084921463_885739874889414",
      "snType":"FACEBOOK",
      "msgType":15,
      "snMsgId":"552086084921463_885739874889414",
      "sourceId":1163,
      "sourceType":"ACCOUNT",
      "snCreatedTimeYearMonth":"2016_10",
      "snCreatedTime":1475147952000
   }
}
	 

     
     
   
 

	[](https://dev.sprinklr.com/v1-case-update) 

 

 
[Back to top](https://dev.sprinklr.com/v1-case-update)
