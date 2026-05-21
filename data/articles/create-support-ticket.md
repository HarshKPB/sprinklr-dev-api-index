---
title: "Create Support Ticket"
slug: create-support-ticket
url: https://dev.sprinklr.com/create-support-ticket
---

# Create Support Ticket

#
  POST Create Support Ticket




Using this API, you can create support tickets and register cases in Sprinklr Care Lite. When the required user and case details are passed in the request payload, a support ticket is automatically created in the backend.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/support-ticket/create-case

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
| title | Required | Refers to the subject of the case/issue | String |
| description | Optional | The description of the issue | String |
| email | Required | The email id of the user for further communication | String |
| firstName | Optional | The first name of the user creating the case | String |
| lastName | Optional | The last name of the user creating the case | String |
| fullName | Optional | The full name of the user | String |
| caseCustomProperties | Optional | Object defining the custom properties of the case | Object |
| messageCustomProperties | Optional | Object defining the custom properties of the message | Object |
| accountId | Required | Unique identifier for the account for which the case is being created | Integer |

## Example - Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/support-ticket/create-case' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
"title":"test api case",
"description":"this is a test case",
"email":"sumit.kaushik@abc.com",
"firstName":"sumit",
"lastName":"kaushik",
"fullName":"sumit kaushik",
"caseCustomProperties":{},
"messageCustomProperties":{},
"accountId": 600002248
}'






## Example - Response





{
    "id": "6312016ca16cec5711fe2756",
    "version": 0,
    "cType": "EMAIL",
    "sub": "test api case",
    "desc": "\n \n \n  this is a test case\n \n",
    "cByUI": 600000001,
    "aUM": [
        {
            "universalMessageKey": {
                "universalMessageId": "EMAIL_175_6312016ca16cec5711fe2755",
                "snType": "EMAIL",
                "msgType": 175,
                "snMsgId": "6312016ca16cec5711fe2755",
                "sourceId": 600002248,
                "sourceType": "ACCOUNT",
                "snCreatedTimeYearMonth": "2022_09",
                "snCreatedTime": 1662124396000
            },
            "universalMessageKeyStr": "EMAILπ175π6312016ca16cec5711fe2755πACCOUNTπ600002248π1662124396000π2022_09",
            "universalMessageKeyStrWithBrandPost": "EMAILπ175π6312016ca16cec5711fe2755πACCOUNTπ600002248π1662124396000π2022_09πfalse",
            "conversationId": "6312016ca16cec5711fe2756",
            "fromSnUserId": "EMAIL_sumit.kaushik@abc.com",
            "associatedTime": 1662124397050,
            "associationType": "Case",
            "fromSnUser": {
                "uI": "sumit.kaushik@abc.com",
                "e": "sumit.kaushik@abc.com",
                "sN": "sumit.kaushik@abc.com",
                "pK": "EMAIL-:-sumit.kaushik@abc.com",
                "n": "sumit kaushik"
            },
            "slaIndex": 1,
            "isBrandPost": false,
            "sentiment": 0,
            "message": "\n \n \n  this is a test case\n \n",
            "nonSLAResponse": false,
            "isFirstSLA": false,
            "autoResponse": false,
            "autoImported": false,
            "sourceInfos": [
                {
                    "sourceId": 600002248,
                    "sourceType": "ACCOUNT",
                    "sourceTypeAndId": "ACCOUNT_600002248"
                }
            ],
            "langCode": "en"
        }
    ],
    "cCMT": 1662124397142,
    "cCT": 1662124397050,
    "cMT": 1662124397142,
    "del": false,
    "uCW": {
        "que": [],
        "comm": [],
        "cProp": {},
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
    "Ad": {
        "profileCaseCreatedUpdated": "true",
        "rmCTm": "1662124396643"
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
    "fSAUId": "EMAIL_sumit.kaushik@abc.com",
    "fUSN": "EMAIL",
    "fSUId": "sumit.kaushik@abc.com",
    "fU": {
        "uI": "sumit.kaushik@abc.com",
        "e": "sumit.kaushik@abc.com",
        "sN": "sumit.kaushik@abc.com",
        "pK": "EMAIL-:-sumit.kaushik@abc.com",
        "n": "sumit kaushik"
    },
    "caseNu": 15460129,
    "dCNu": "15460129",
    "sSummary": "15460129 test api case \n \n \n  this is a test case\n \n null sumit.kaushik@abc.com sumit kaushik 6312016ca16cec5711fe2755",
    "lPASCT": 1662124396000,
    "lMAUT": 1662124397050,
    "lFMAT": 1662124397050,
    "lAUMSCT": 1662124396000,
    "lWT": 0,
    "sId": 600002248,
    "aMCnt": 1,
    "aFMCnt": 1,
    "aBMCnt": 0,
    "aUBMCnt": 0,
    "fBRCnt": 1,
    "hBR": false,
    "rAUMSCT": 1662124396000,
    "fFMSCT": 1662124396000,
    "cCnt": 0,
    "cPAInfo": {
        "assignmentInfoMap": {}
    },
    "cCProp": {},
    "hasRating": false,
    "videoChatEnabled": false,
    "sentiment": {
        "value": 0
    },
    "rMK": {
        "universalMessageId": "EMAIL_175_6312016ca16cec5711fe2755",
        "snType": "EMAIL",
        "msgType": 175,
        "snMsgId": "6312016ca16cec5711fe2755",
        "sourceId": 600002248,
        "sourceType": "ACCOUNT",
        "snCreatedTimeYearMonth": "2022_09",
        "snCreatedTime": 1662124396000
    },
    "iSG": true,
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
    "gpExecuted": false,
    "cbInitiated": false,
    "participatedAgents": [],
    "nonEditable": false
}







	[](https://dev.sprinklr.com/create-support-ticket)




[Back to top](https://dev.sprinklr.com/create-support-ticket)
