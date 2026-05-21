---
title: "Case Management Stream v1"
slug: case-management-stream-v1
url: https://dev.sprinklr.com/case-management-stream-v1
---

# Case Management Stream v1

#
  POST Case Management Stream



Using this API, you can fetch the most recent messages associated with a case from the monitoring dashboard.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v1/universalcase/stream/{stream id}/feed

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














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

## Path Parameter












[Read Dashboard by Dashboard Name](https://dev.sprinklr.com/fetch-engagement-dashboard-v1)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| streamId | Required | Refers to the unique identifier for the engagement columnYou can fetch the stream Id from the "" API | String |

## Request Parameters
























``
``






































			````




| Parameter | Sub Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| casePaginationInfo |  | Required | Pagination object containing pagination information. | String |
|  | start | Required | The start offset to tell the client where to begin pulling data. The default is 0. To pull multiple batches of data, use the start and row paramaters to iterate through the available data. Example: Pull #1: start=0&rows=20 Example: Pull #2: start=1&rows=21 | String |
|  | rows | Required | The number of rows to be fetched starting from the start. The default is 21 rows. | Integer |
|  | sortDirection | Optional | Used to return response after sorting either in DESC/ASC order.sortDirection is w.r.t the case creation time(cCT) | String |
|  | sinceDate | Optional | Time from which you want to pull the stream.sinceDate is w.r.t the case creation time (cCT) | String |
|  | untilDate | Optional | Time to which you want to pull the stream.untilDate is w.r.t the case creation time (cCT) | String |
|  | sortKey | Optional | To sort the response either on caseCreationTime or  caseModificationTime. By default the response are sorted based on case created time. | String |

## Example - Request















Copy Code



curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v1/universalcase/stream/598dd97ee4b0ec5110f2d803/feed' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "casePaginationInfo": {
    	"start":0,
    	"rows":200,
    	"sortDirection": "ASC"
    }
}'






## Example - Response




 {
    "data": [
        {
            "universalCase": {
                "id": "5e2ee4be54e68b71ffb37bbf",
                "version": 24,
                "cType": "SPRINKLR",
                "sub": "BusinessInd",
                "desc": "Some members may be experiencing an issue with the site. We’re working on this as we speak and will provide updates as we have them. Thanks for your patience!",
                "cByUI": 200551,
                "aUM": [
                    {
                        "universalMessageKey": {
                            "universalMessageId": "FACEBOOK_14_121979102646537_127117082132739",
                            "snType": "FACEBOOK",
                            "msgType": 14,
                            "snMsgId": "121979102646537_127117082132739",
                            "sourceId": 372010,
                            "sourceType": "ACCOUNT",
                            "snCreatedTimeYearMonth": "2020_01",
                            "snCreatedTime": 1580291023000
                        },
                        "universalMessageKeyStr": "FACEBOOKπ14π121979102646537_127117082132739πACCOUNTπ372010π1580291023000π2020_01",
                        "universalMessageKeyStrWithBrandPost": "FACEBOOKπ14π121979102646537_127117082132739πACCOUNTπ372010π1580291023000π2020_01πtrue",
                        "conversationId": "112648423579605_121979102646537",
                        "fromSnUserId": "FACEBOOK_112648423579605",
                        "associatedTime": 1580291024789,
                        "associationType": "Case",
                        "fromSnUser": {
                            "uI": "112648423579605",
                            "sN": "BusinessInd",
                            "pK": "FACEBOOK-:-112648423579605"
                        },
                        "slaIndex": 1,
                        "userSlaIndex": 1,
                        "isBrandPost": true,
                        "brandResponseByUser": 215986,
                        "sentiment": 0,
                        "message": "Gdhdbcn",
                        "lSMessage": {
                            "ja": "Gdhdbcn"
                        },
                        "isFirstSLA": true,
                        "surveyMessage": false,
                        "autoResponse": false,
                        "sourceInfos": [
                            {
                                "sourceId": 372010,
                                "sourceType": "ACCOUNT",
                                "sourceTypeAndId": "ACCOUNT_372010"
                            }
                        ]
                    },
                    {
                        "universalMessageKey": {
                            "universalMessageId": "FACEBOOK_14_121979102646537_131460758365038",
                            "snType": "FACEBOOK",
                            "msgType": 14,
                            "snMsgId": "121979102646537_131460758365038",
                            "sourceId": 372010,
                            "sourceType": "ACCOUNT",
                            "snCreatedTimeYearMonth": "2020_02",
                            "snCreatedTime": 1581231925000
                        },
                        "universalMessageKeyStr": "FACEBOOKπ14π121979102646537_131460758365038πACCOUNTπ372010π1581231925000π2020_02",
                        "universalMessageKeyStrWithBrandPost": "FACEBOOKπ14π121979102646537_131460758365038πACCOUNTπ372010π1581231925000π2020_02πtrue",
                        "conversationId": "112648423579605_121979102646537",
                        "fromSnUserId": "FACEBOOK_112648423579605",
                        "associatedTime": 1581231928775,
                        "associationType": "Case",
                        "fromSnUser": {
                            "uI": "112648423579605",
                            "sN": "BusinessInd",
                            "pK": "FACEBOOK-:-112648423579605"
                        },
                        "slaIndex": 2,
                        "userSlaIndex": 2,
                        "isBrandPost": true,
                        "brandResponseByUser": 215987,
                        "sentiment": 0,
                        "message": "Adds",
                        "lSMessage": {
                            "ja": "Adds"
                        },
                        "isFirstSLA": false,
                        "surveyMessage": false,
                        "autoResponse": false,
                        "sourceInfos": [
                            {
                                "sourceId": 372010,
                                "sourceType": "ACCOUNT",
                                "sourceTypeAndId": "ACCOUNT_372010"
                            }
                        ]
                    },
                    {
                        "universalMessageKey": {
                            "universalMessageId": "FACEBOOK_14_121979102646537_131636761680771",
                            "snType": "FACEBOOK",
                            "msgType": 14,
                            "snMsgId": "121979102646537_131636761680771",
                            "sourceId": 372010,
                            "sourceType": "ACCOUNT",
                            "snCreatedTimeYearMonth": "2020_02",
                            "snCreatedTime": 1581272718000
                        },
                        "universalMessageKeyStr": "FACEBOOKπ14π121979102646537_131636761680771πACCOUNTπ372010π1581272718000π2020_02",
                        "universalMessageKeyStrWithBrandPost": "FACEBOOKπ14π121979102646537_131636761680771πACCOUNTπ372010π1581272718000π2020_02πtrue",
                        "conversationId": "112648423579605_121979102646537",
                        "fromSnUserId": "FACEBOOK_112648423579605",
                        "associatedTime": 1581272720225,
                        "associationType": "Case",
                        "fromSnUser": {
                            "uI": "112648423579605",
                            "sN": "BusinessInd",
                            "pK": "FACEBOOK-:-112648423579605"
                        },
                        "slaIndex": 3,
                        "userSlaIndex": 3,
                        "isBrandPost": true,
                        "brandResponseByUser": 215987,
                        "sentiment": 0,
                        "message": "Dads",
                        "lSMessage": {
                            "ja": "Dads"
                        },
                        "isFirstSLA": false,
                        "surveyMessage": false,
                        "autoResponse": false,
                        "sourceInfos": [
                            {
                                "sourceId": 372010,
                                "sourceType": "ACCOUNT",
                                "sourceTypeAndId": "ACCOUNT_372010"
                            }
                        ]
                    },
                    {
                        "universalMessageKey": {
                            "universalMessageId": "FACEBOOK_14_121979102646537_132554491588998",
                            "snType": "FACEBOOK",
                            "msgType": 14,
                            "snMsgId": "121979102646537_132554491588998",
                            "sourceId": 372010,
                            "sourceType": "ACCOUNT",
                            "snCreatedTimeYearMonth": "2020_02",
                            "snCreatedTime": 1581516301000
                        },
                        "universalMessageKeyStr": "FACEBOOKπ14π121979102646537_132554491588998πACCOUNTπ372010π1581516301000π2020_02",
                        "universalMessageKeyStrWithBrandPost": "FACEBOOKπ14π121979102646537_132554491588998πACCOUNTπ372010π1581516301000π2020_02πtrue",
                        "conversationId": "112648423579605_121979102646537",
                        "fromSnUserId": "FACEBOOK_112648423579605",
                        "associatedTime": 1581516303672,
                        "associationType": "Case",
                        "fromSnUser": {
                            "uI": "112648423579605",
                            "sN": "BusinessInd",
                            "pK": "FACEBOOK-:-112648423579605"
                        },
                        "slaIndex": 4,
                        "userSlaIndex": 4,
                        "isBrandPost": true,
                        "brandResponseByUser": 215987,
                        "sentiment": 0,
                        "message": "Adscasd",
                        "lSMessage": {
                            "ja": "Adscasd"
                        },
                        "isFirstSLA": false,
                        "surveyMessage": false,
                        "autoResponse": false,
                        "sourceInfos": [
                            {
                                "sourceId": 372010,
                                "sourceType": "ACCOUNT",
                                "sourceTypeAndId": "ACCOUNT_372010"
                            }
                        ]
                    },
                    {
                        "universalMessageKey": {
                            "universalMessageId": "FACEBOOK_14_121979102646537_132807254897055",
                            "snType": "FACEBOOK",
                            "msgType": 14,
                            "snMsgId": "121979102646537_132807254897055",
                            "sourceId": 372010,
                            "sourceType": "ACCOUNT",
                            "snCreatedTimeYearMonth": "2020_02",
                            "snCreatedTime": 1581576495000
                        },
                        "universalMessageKeyStr": "FACEBOOKπ14π121979102646537_132807254897055πACCOUNTπ372010π1581576495000π2020_02",
                        "universalMessageKeyStrWithBrandPost": "FACEBOOKπ14π121979102646537_132807254897055πACCOUNTπ372010π1581576495000π2020_02πtrue",
                        "conversationId": "112648423579605_121979102646537",
                        "fromSnUserId": "FACEBOOK_112648423579605",
                        "associatedTime": 1581576496775,
                        "associationType": "Case",
                        "fromSnUser": {
                            "uI": "112648423579605",
                            "sN": "BusinessInd",
                            "pK": "FACEBOOK-:-112648423579605"
                        },
                        "slaIndex": 5,
                        "userSlaIndex": 5,
                        "isBrandPost": true,
                        "brandResponseByUser": 215987,
                        "sentiment": 0,
                        "message": "As favsasdcsd",
                        "lSMessage": {
                            "ja": "As favsasdcsd"
                        },
                        "isFirstSLA": false,
                        "surveyMessage": false,
                        "autoResponse": false,
                        "sourceInfos": [
                            {
                                "sourceId": 372010,
                                "sourceType": "ACCOUNT",
                                "sourceTypeAndId": "ACCOUNT_372010"
                            }
                        ]
                    },
                    {
                        "universalMessageKey": {
                            "universalMessageId": "FACEBOOK_14_121979102646537_133663974811383",
                            "snType": "FACEBOOK",
                            "msgType": 14,
                            "snMsgId": "121979102646537_133663974811383",
                            "sourceId": 372010,
                            "sourceType": "ACCOUNT",
                            "snCreatedTimeYearMonth": "2020_02",
                            "snCreatedTime": 1581759383000
                        },
                        "universalMessageKeyStr": "FACEBOOKπ14π121979102646537_133663974811383πACCOUNTπ372010π1581759383000π2020_02",
                        "universalMessageKeyStrWithBrandPost": "FACEBOOKπ14π121979102646537_133663974811383πACCOUNTπ372010π1581759383000π2020_02πtrue",
                        "conversationId": "112648423579605_121979102646537",
                        "fromSnUserId": "FACEBOOK_112648423579605",
                        "associatedTime": 1581759385585,
                        "associationType": "Case",
                        "fromSnUser": {
                            "uI": "112648423579605",
                            "sN": "BusinessInd",
                            "pK": "FACEBOOK-:-112648423579605"
                        },
                        "slaIndex": 6,
                        "userSlaIndex": 6,
                        "isBrandPost": true,
                        "brandResponseByUser": 215987,
                        "sentiment": 0,
                        "message": "This is awesome",
                        "lSMessage": {
                            "ja": "This is awesome"
                        },
                        "isFirstSLA": false,
                        "surveyMessage": false,
                        "autoResponse": false,
                        "sourceInfos": [
                            {
                                "sourceId": 372010,
                                "sourceType": "ACCOUNT",
                                "sourceTypeAndId": "ACCOUNT_372010"
                            }
                        ]
                    },
                    {
                        "universalMessageKey": {
                            "universalMessageId": "FACEBOOK_14_121979102646537_135822904595490",
                            "snType": "FACEBOOK",
                            "msgType": 14,
                            "snMsgId": "121979102646537_135822904595490",
                            "sourceId": 372010,
                            "sourceType": "ACCOUNT",
                            "snCreatedTimeYearMonth": "2020_02",
                            "snCreatedTime": 1582296630000
                        },
                        "universalMessageKeyStr": "FACEBOOKπ14π121979102646537_135822904595490πACCOUNTπ372010π1582296630000π2020_02",
                        "universalMessageKeyStrWithBrandPost": "FACEBOOKπ14π121979102646537_135822904595490πACCOUNTπ372010π1582296630000π2020_02πtrue",
                        "conversationId": "112648423579605_121979102646537",
                        "fromSnUserId": "FACEBOOK_112648423579605",
                        "associatedTime": 1582296632526,
                        "associationType": "Case",
                        "fromSnUser": {
                            "uI": "112648423579605",
                            "sN": "BusinessInd",
                            "pK": "FACEBOOK-:-112648423579605"
                        },
                        "slaIndex": 7,
                        "userSlaIndex": 7,
                        "isBrandPost": true,
                        "brandResponseByUser": 215987,
                        "sentiment": 0,
                        "message": "Comment on post",
                        "lSMessage": {
                            "ja": "Comment on post"
                        },
                        "isFirstSLA": false,
                        "surveyMessage": false,
                        "autoResponse": false,
                        "sourceInfos": [
                            {
                                "sourceId": 372010,
                                "sourceType": "ACCOUNT",
                                "sourceTypeAndId": "ACCOUNT_372010"
                            }
                        ]
                    },
                    {
                        "universalMessageKey": {
                            "universalMessageId": "FACEBOOK_14_121979102646537_137591391085308",
                            "snType": "FACEBOOK",
                            "msgType": 14,
                            "snMsgId": "121979102646537_137591391085308",
                            "sourceId": 372010,
                            "sourceType": "ACCOUNT",
                            "snCreatedTimeYearMonth": "2020_02",
                            "snCreatedTime": 1582715092000
                        },
                        "universalMessageKeyStr": "FACEBOOKπ14π121979102646537_137591391085308πACCOUNTπ372010π1582715092000π2020_02",
                        "universalMessageKeyStrWithBrandPost": "FACEBOOKπ14π121979102646537_137591391085308πACCOUNTπ372010π1582715092000π2020_02πtrue",
                        "conversationId": "112648423579605_121979102646537",
                        "fromSnUserId": "FACEBOOK_112648423579605",
                        "associatedTime": 1582715095048,
                        "associationType": "Case",
                        "fromSnUser": {
                            "uI": "112648423579605",
                            "sN": "BusinessInd",
                            "pK": "FACEBOOK-:-112648423579605"
                        },
                        "slaIndex": 8,
                        "userSlaIndex": 8,
                        "isBrandPost": true,
                        "brandResponseByUser": 215987,
                        "sentiment": 0,
                        "message": "I am going",
                        "lSMessage": {
                            "ja": "I am going"
                        },
                        "isFirstSLA": false,
                        "surveyMessage": false,
                        "autoResponse": false,
                        "sourceInfos": [
                            {
                                "sourceId": 372010,
                                "sourceType": "ACCOUNT",
                                "sourceTypeAndId": "ACCOUNT_372010"
                            }
                        ]
                    },
                    {
                        "universalMessageKey": {
                            "universalMessageId": "FACEBOOK_97_121979102646537_137616244416156",
                            "snType": "FACEBOOK",
                            "msgType": 97,
                            "snMsgId": "121979102646537_137616244416156",
                            "sourceId": 372010,
                            "sourceType": "ACCOUNT",
                            "snCreatedTimeYearMonth": "2020_02",
                            "snCreatedTime": 1582721623000
                        },
                        "universalMessageKeyStr": "FACEBOOKπ97π121979102646537_137616244416156πACCOUNTπ372010π1582721623000π2020_02",
                        "universalMessageKeyStrWithBrandPost": "FACEBOOKπ97π121979102646537_137616244416156πACCOUNTπ372010π1582721623000π2020_02πtrue",
                        "conversationId": "112648423579605_121979102646537",
                        "fromSnUserId": "FACEBOOK_112648423579605",
                        "associatedTime": 1582721626200,
                        "associationType": "Case",
                        "fromSnUser": {
                            "uI": "112648423579605",
                            "sN": "BusinessInd",
                            "pK": "FACEBOOK-:-112648423579605"
                        },
                        "slaIndex": 9,
                        "userSlaIndex": 9,
                        "isBrandPost": true,
                        "brandResponseByUser": 215987,
                        "sentiment": 0,
                        "message": "R madhava the same",
                        "lSMessage": {
                            "ja": "R madhava the same"
                        },
                        "isFirstSLA": false,
                        "surveyMessage": false,
                        "autoResponse": false,
                        "sourceInfos": [
                            {
                                "sourceId": 372010,
                                "sourceType": "ACCOUNT",
                                "sourceTypeAndId": "ACCOUNT_372010"
                            }
                        ]
                    }
                ],
                "cCMT": 1580131518416,
                "cCT": 1580131518404,
                "cMT": 1583235098817,
                "del": false,
                "uCW": {
                    "que": [
                        {
                            "qId": 2777,
                            "qTm": 1580291025149
                        },
                        {
                            "qId": 144,
                            "qTm": 1583235098817
                        },
                        {
                            "qId": 34,
                            "qTm": 1583235098817
                        }
                    ],
                    "comm": [],
                    "cProp": {
                        "spr_uc_priority": [
                            "Very High"
                        ],
                        "spr_uc_tag": [
                            "Tag2"
                        ],
                        "spr_uc_status": [
                            "New"
                        ]
                    },
                    "subs": [],
                    "uAD": {
                        "aTId": 200551,
                        "aBId": 200551,
                        "aTm": 1580131518404,
                        "aBR": false
                    },
                    "arc": false,
                    "acl": {},
                    "aclM": {},
                    "clW": [],
                    "pUD": [
                        {
                            "userId": 200551,
                            "startTime": 1580131527106,
                            "duration": 1999256,
                            "pauseTime": 1580133526362,
                            "state": "PAUSED"
                        }
                    ],
                    "resumeClockSeq": 1,
                    "surveyRespDets": {},
                    "smRU": false,
                    "smRP": false,
                    "smRE": false,
                    "predSmResConf": []
                },
                "Ad": {
                    "rmCTm": "1579221705885",
                    "iFSAC": "true"
                },
                "addInfo": {
                    "rCP": {
                        "flatCustomProperties": [
                            "ALLµspr_uc_priorityµVery High",
                            "ALL",
                            "ALLµspr_uc_tagµTag2",
                            "ALLµspr_uc_statusµNew",
                            "ALLµspr_uc_tag",
                            "ALLµspr_uc_priority",
                            "ALLµspr_uc_status"
                        ],
                        "customPropertyNames": [
                            "spr_uc_priority",
                            "spr_uc_tag",
                            "spr_uc_status"
                        ],
                        "mappedCustomProperties": {
                            "spr_uc_tag": [
                                "Tag2"
                            ],
                            "spr_uc_status": [
                                "New"
                            ],
                            "spr_uc_priority": [
                                "Very High"
                            ]
                        },
                        "customProperties": [
                            {
                                "key": "spr_uc_tag",
                                "values": [
                                    "Tag2"
                                ]
                            },
                            {
                                "key": "spr_uc_priority",
                                "values": [
                                    "Very High"
                                ]
                            },
                            {
                                "key": "spr_uc_status",
                                "values": [
                                    "New"
                                ]
                            }
                        ]
                    }
                },
                "fSAUId": "FACEBOOK_112648423579605",
                "fUSN": "FACEBOOK",
                "fSUId": "112648423579605",
                "fU": {
                    "n": "BusinessInd",
                    "sN": "BusinessInd",
                    "uI": "112648423579605"
                },
                "caseNu": 23934565,
                "dCNu": "23934565",
                "dtf": {
                    "q_2777_d": 1580291025149,
                    "q_34_d": 1583235098817,
                    "q_144_d": 1583235098817
                },
                "lPASCT": 1582721623000,
                "lMAUT": 1582721626200,
                "lBMAT": 1582721626200,
                "lAUMSCT": 1582721623000,
                "sId": 372010,
                "aMCnt": 9,
                "aFMCnt": 0,
                "aBMCnt": 9,
                "aUBMCnt": 9,
                "fBRCnt": 0,
                "hBR": true,
                "rAUMSCT": 1580291023000,
                "fBAUMSCT": 1580291023000,
                "fUBAUMSCT": 1579221703000,
                "fUBRTEAI": 1580291023000,
                "cCnt": 14,
                "cPAInfo": {
                    "assignmentInfoMap": {
                        "spr_uc_status_New": {
                            "value": "New",
                            "assignmentTime": 1580131518418
                        },
                        "spr_uc_priority_Very_High": {
                            "value": "Very High",
                            "assignmentTime": 1583235098819
                        },
                        "spr_uc_tag_Tag2": {
                            "value": "Tag2",
                            "assignmentTime": 1580131518577
                        }
                    }
                },
                "hasRating": false,
                "lBRBU": 215987,
                "lBRT": 1582721623000,
                "sentiment": {
                    "value": -1
                },
                "rMK": {
                    "universalMessageId": "FACEBOOK_14_121979102646537_127117082132739",
                    "snType": "FACEBOOK",
                    "msgType": 14,
                    "snMsgId": "121979102646537_127117082132739",
                    "sourceId": 372010,
                    "sourceType": "ACCOUNT",
                    "snCreatedTimeYearMonth": "2020_01",
                    "snCreatedTime": 1580291023000
                },
                "iSG": false,
                "caseAssetTags": [
                    {
                        "name": "case time",
                        "colorCode": "#e7e7e7",
                        "iconUrl": "",
                        "taggingRuleId": "5db033c3b74e70734a31eda9",
                        "clientId": -1
                    },
                    {
                        "name": "NEW",
                        "colorCode": "#e7e7e7",
                        "iconUrl": "",
                        "taggingRuleId": "5ddfcce7b74e70741219af66",
                        "clientId": -1
                    }
                ],
                "hasSurveyResponse": false,
                "read": false
            },
            "profile": {
                "snType": "FACEBOOK",
                "age": 0,
                "gender": "Other/Unspecified",
                "snId": "112648423579605",
                "name": "BusinessInd",
                "firstName": "BusinessInd",
                "screenName": "BusinessInd",
                "subType": "PAGE",
                "following": 0,
                "followers": 0,
                "favCount": 0,
                "statusCount": 0,
                "permalink": "https://www.facebook.com/112648423579605",
                "createdTime": "0",
                "profileImgUrl": "https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-1/c65.0.200.200a/p200x200/80776074_112650980246016_4273703162025607168_n.png?_nc_cat=103&_nc_sid=dbb9e7&_nc_ohc=Wgwf9CA4diIAX_kH6Hw&_nc_ht=scontent-iad3-1.xx&oh=2f72f41aa03013c1ddb921d00e47719c&oe=5EDF8107",
                "verified": false,
                "demographicsAdditional": {
                    "country": "India",
                    "city": "Bangalore",
                    "latitude": "13.00437",
                    "longitude": "77.71258"
                },
                "profileWorkflowProperties": {
                    "tags": [],
                    "comments": [],
                    "notifyUserIds": [],
                    "partnerProfileLists": [
                        12
                    ],
                    "clientProfileLists": [],
                    "partnerCustomProperties": {
                        "5b2bf053e4b0cde609a8191b": [
                            "B"
                        ],
                        "5b53772fe4b0ff9e16cf306b": [
                            "profile"
                        ],
                        "5d4718ed94de9d68e81c5447": [
                            "2"
                        ]
                    },
                    "clientCustomProperties": {
                        "5bf2e3ffe4b00a62cc74df75": [
                            "12"
                        ]
                    },
                    "spaceCustomProperties": {},
                    "userCustomProperties": {},
                    "clientTags": []
                },
                "universalProfileId": "5e0783b199553c54e367c02a",
                "participationIndex": 0.0,
                "influencerIndex": 0.0,
                "spamIndex": 0.0,
                "accountsFollowedByUser": [],
                "accountsFollowingUser": [],
                "accountsUnFollowingUser": [],
                "accountsUnFollowedByUser": [],
                "accountsBlockingUser": [],
                "accountsSuspendingUser": [],
                "profileTags": [],
                "accountSpecificInfos": [
                    {
                        "accountId": 372010,
                        "externalId": "112648423579605"
                    }
                ],
                "accountSpecificInfoMap": {
                    "372010": {
                        "accountId": 372010,
                        "externalId": "112648423579605"
                    }
                }
            },
            "actionTime": 1580131518404,
            "actionKey": "caseCreationTime"
        }
    ],
    "messagesCount": 1,
    "lastProcessedCaseTime": 1580131518404,
    "hasMore": false
}







[](https://dev.sprinklr.com/case-management-stream-v1)




[Back to top](https://dev.sprinklr.com/case-management-stream-v1)
