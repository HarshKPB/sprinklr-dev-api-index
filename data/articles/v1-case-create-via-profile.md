---
title: "v1 Case Create via Profile"
slug: v1-case-create-via-profile
url: https://dev.sprinklr.com/v1-case-create-via-profile
---

# v1 Case Create via Profile

#
POST v1 Case Create via Profile

	Using this API, you can create a case on top of an external profile existing within Sprinklr.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v1/universalcase/profile-case

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






















































































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| snType |  | Optional | The social network in which the profile exsist. | String |
| snId |  | Required | The social network Id of the profile. | String |
| email |  | Optional | The email Id of the profile. | String |
| firstName |  | Optional | The user first name associated with profile. | String |
| lastName |  | Optional | The user last name associated with profile. | String |
| fullName |  | Optional | The fullname of the user associated with profile. | String |
| phoneNumber |  | Optional | The phone number associated with profile. | Long |
| customProperties |  | Optional | The object of custom properties associated with profile. | String |
| commentDTO |  | Optional | The object containing details regarding the case. | Object |
|  | comment | Optional | The comments which describes the issue type related to profile. | String |
|  | mediaList | Optional | The object containing details related to profile on which the case has to be created.  More details are given below in Media List Description Table. | String |
|  | assetClass | Optional | The asset class associated with profile. | String |
|  | assetId | Optional | The asset Id used in profile. | String |
| subject |  | Optional | The subject of the case. | String |
| description |  | Optional | The description of the case. | String |

## Example

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
		curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/case/universalcase/create-profile-case \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "snType": "EXTERNAL_APPLICATION",
    "snId" : "SDM_12344567",
    "firstName" : "Veenu",
    "lastName" : "J N",
    "fullName" : "Veenu J N",
    "phoneNumber" : "123456789",
    "email": "ABC@gmail.com",
    "customProperties" : {
        "_c_60efc3a3dd249c300841bcd7" : ["Yes"]
    },
    "commentDTO": {
            "comment": "
Hi there
",
            "mediaList": [
                {
                    "type": "PHOTO",
                    "title": "am determined Message modified ; 1621810995341",
                    "mediaAssetId": "60c582ccbe9d89hj068378bd",
                    "source": "https://qa4-sprcdn-assets.sprinklr.com/400002/073e4e5c-c57a-45eb-a4db-79154e2dfe5a-1541641981/https___testproxy-qa4.sprinklr.jpg",
                    "previewImageUrl": "https://qa4-sprcdn-assets.sprinklr.com/400002/073e4e5c-c57a-45eb-a4db-79154e2dfe5a-1541641981/https___testproxy-qa4.sprinklr_p.jpg"
                }
            ],
            "assetClass": "",
            "assetId": ""
        },
    "subject": "This is subject",
    "description": "This is description"
}'
 

     
     
 
 
 
     
 
{
    "universalCase": {
        "id": "60ffc2f1badda3729d8989d5",
        "version": 0,
        "cType": "SPRINKLR",
        "sub": "This is subject",
        "desc": "This is description",
        "cByUI": 429501,
        "aUM": [],
        "cCMT": 1627374321674,
        "cCT": 1627374321653,
        "cMT": 1627374321674,
        "del": false,
        "uCW": {
            "que": [],
            "comm": [],
            "cProp": {
                "_c_60efc3a3dd249c300841bcd7": [
                    "Yes"
                ]
            },
            "subs": [],
            "arc": false,
            "kbD": {},
            "acl": {},
            "aclM": {},
            "clW": [],
            "surveyRespDets": {},
            "smRU": false,
            "smRP": false,
            "smRE": false,
            "uSmResDets": [],
            "predSmResConf": [],
            "predFaqBotQues": [],
            "predFaqBotIntents": [],
            "predFaqBotThemes": [],
            "usedFaqBotQues": [],
            "usedFaqBotIntents": [],
            "usedFaqBotThemes": [],
            "nOCRU": 0
        },
        "uCSW": {
            "stagesCapturedCount": 0,
            "stageDetails": {}
        },
        "addInfo": {
            "rCP": {
                "flatCustomProperties": [
                    "ALL"
                ],
                "customPropertyNames": [],
                "mappedCustomProperties": {},
                "mappedControllingCustomPropertyList": []
            }
        },
        "fSAUId": "EXTERNAL_APPLICATION_SDM_12344567",
        "fUSN": "EXTERNAL_APPLICATION",
        "fSUId": "SDM_12344567",
        "fU": {
            "pK": "EXTERNAL_APPLICATION-:-SDM_12344567"
        },
        "caseNu": 25374626,
        "dCNu": "25374626",
        "sSummary": "25374626 This is subject This is description null",
        "lSsSummary": {
            "ja": "25374626 This is subject This is description null"
        },
        "aMCnt": 0,
        "aFMCnt": 0,
        "aBMCnt": 0,
        "aUBMCnt": 0,
        "fBRCnt": 0,
        "hBR": false,
        "cCnt": 0,
        "cPAInfo": {
            "assignmentInfoMap": {
                "_c_60efc3a3dd249c300841bcd7_Yes": {
                    "value": "Yes",
                    "assignmentTime": 1627374321676
                }
            }
        },
        "cCProp": {},
        "hasRating": false,
        "videoChatEnabled": false,
        "iSG": false,
        "caseAssetTags": [
            {
                "name": "NEW",
                "colorCode": "#e7e7e7",
                "iconUrl": "",
                "taggingRuleId": "5ddfcce7b74e70741219af66",
                "clientId": -1
            }
        ],
        "resolvedFields": [
            "caseAssetTags"
        ],
        "matchedIntents": [],
        "deflectionInfo": {
            "deflectionLinkSent": false,
            "deflectionLinkClicked": false,
            "deflectedConversationCreated": false,
            "deflectedConversationStarted": false
        },
        "similarAsset": {},
        "assetFeedbackStats": {},
        "read": false,
        "allEngagedUsersList": [],
        "allAddedWorkQueues": [],
        "gpExecuted": false
    },
    "profile": {
        "snType": "EXTERNAL_APPLICATION",
        "age": 0,
        "snId": "SDM_12344567",
        "name": "Veenu J N",
        "firstName": "Veenu",
        "lastName": "J N",
        "screenName": "ABC@gmail.com",
        "email": "ABC@gmail.com",
        "subType": "",
        "following": 0,
        "followers": 0,
        "favCount": 0,
        "statusCount": 0,
        "createdTime": "0",
        "unSubscribed": false,
        "profileWorkflowProperties": {
            "comments": [],
            "notifyUserIds": [],
            "partnerProfileLists": [],
            "clientProfileLists": [],
            "partnerCustomProperties": {},
            "clientCustomProperties": {},
            "spaceCustomProperties": {},
            "userCustomProperties": {},
            "clientTags": []
        },
        "universalProfileId": "60ffc2f1ddf7722d4140c755",
        "participationIndex": 0.0,
        "influencerIndex": 0.0,
        "spamIndex": 0.0,
        "accountsFollowedByUser": [],
        "accountsFollowingUser": [],
        "accountsUnFollowingUser": [],
        "accountsUnFollowedByUser": [],
        "accountsBlockingUser": [],
        "accountsSuspendingUser": [],
        "accountsDeactivatingUser": [],
        "accountSpecificInfoMap": {},
        "additional": {
            "lCEmail": [
                "abc@gmail.com"
            ]
        }
    },
    "actionTime": 0
}
 

     
     
   
 

	[](https://dev.sprinklr.com/v1-case-create-via-profile) 

 

 
[Back to top](https://dev.sprinklr.com/v1-case-create-via-profile)
