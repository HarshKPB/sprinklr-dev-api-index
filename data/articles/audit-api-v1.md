---
title: "Audit API V1"
slug: audit-api-v1
url: https://dev.sprinklr.com/audit-api-v1
---

# Audit API V1

#
POST  Audit API V1


The Audit API gives a full history of what/who has changed the object over time. That's usually used for governance to trace down who has made what changes and when.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/audit/fetch

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/ /api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Parameters











			``





			``





			``













			````````



			``

			````````




| Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| assetIds | Required | Ids of the asset on which the comment is made. | String |
| assetClass | Required | Asset class string = {UNIVERSAL_CASE,MESSAGE_WORKFLOW,PROFILE_WORKFLOW,MEDIA_ASSET, OUTBOUND_MESSAGE} | String |
| ascending | Optional | If true, will show in ascending order. | Boolean |
| limit | Optional | Limit to which objects are shown in response. | Integer |
| sinceId | Optional | If you are using pagination while retrieving audit data in ascending order and the response has hasMore returned true then to retrieve the next set of subsequent data you need to use the sinceId. The value of the sinceId will be the value of the changeGroupId of the last entry returned in the API response. | String |
| untilId | Optional | If you are using pagination while retrieving audit data in descending order and the response has hasMore returned true then to retrieve the next set of subsequent data you need to use the untilId. The value of the untilId will be the value of the changeGroupId of the last entry returned in the API response. | String |

### Request - Example















Copy Code



	{
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/audit/fetch' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
-d '
	"assetIds": [
        10520954
    ],
    "assetClass":"UNIVERSAL_CASE",
   "ascending":false,
   "limit":100
}'






### Response - Example





		{
   "data":[
      {
         "moduleAdditionalProps":{
            "UI":{
            }
         },
         "changes":[
            {
               "fieldName":"Queues",
               "fieldType":"CASE_QUEUES",
               "oldValues":[
               ],
               "newValues":[
                  "466"
               ],
               "lookupInfo":{
                  "fieldType":"CASE_QUEUES",
                  "lookupType":"CASE_QUEUE"
               }
            }
         ],
         "partnerId":9004,
         "userId":1000053168,
         "assetId":"10001",
         "changeDate":1526036873070,
         "changeType":"UNIVERSAL_CASE_UPDATED",
         "changeGroupId":"5af57989e4b0ed867fa2745b",
         "assetClass":"UNIVERSAL_CASE"
      },
      {
         "moduleAdditionalProps":{
            "UI":{
               "Case macro":"/ui/v3/admin/settings#macros"
            }
         },
         "changes":[
            {
               "fieldName":"Assigned To User",
               "fieldType":"ASSIGN_TO",
               "oldValues":[
               ],
               "newValues":[
                  "1000053168"
               ],
               "lookupInfo":{
                  "fieldType":"ASSIGN_TO",
                  "lookupType":"USER_ID"
               }
            }
         ],
         "partnerId":9004,
         "userId":1000053168,
         "assetId":"10001",
         "changeDate":1526036683295,
         "changeType":"UNIVERSAL_CASE_UPDATED",
         "changeGroupId":"5af578cbe4b0ed867fa12d69",
         "assetClass":"UNIVERSAL_CASE"
      },
      {
         "moduleAdditionalProps":{
            "RE":{
               "Rams_Case_rule":"https://prod0.sprinklr.com/ui/v3/admin/rule-engine#client/56dce4c6e4b0a1bd56d86c50"
            },
            "universalMessageKeyStr":{
               "LINKEDINπ16πUPDATE-c2716702-6142041475082448896πACCOUNTπ1000067732π1464376801310π2016_05":{
                  "postType":"COMPANY_FOLLOW_UPDATE",
                  "likeFlag":false,
                  "partnerId":9004,
                  "clientId":1000004509,
                  "sourceId":1000067732,
                  "accountId":1000067732,
                  "sourceType":"ACCOUNT",
                  "snType":"LINKEDIN",
                  "snMsgId":"UPDATE-c2716702-6142041475082448896",
                  "messageType":16,
                  "messageSubType":46,
                  "universalMessageId":"LINKEDIN_16_UPDATE-c2716702-6142041475082448896",
                  "permalink":"https://www.linkedin.com/nhome/updates?topic=6142041475082448896",
                  "message":"test prod0 116",
                  "textEntities":{
                     "message":[
                     ]
                  },
                  "senderProfile":{
                     "snType":"LINKEDIN",
                     "age":0,
                     "snId":"2716702",
                     "name":"DreamMalar",
                     "screenName":"DreamMalar",
                     "bio":"All about paid, ads, advertisement and social advertising. The world heading to social hence the marketing is heading to social",
                     "subType":"PAGE",
                     "following":0,
                     "followers":356,
                     "favCount":0,
                     "statusCount":0,
                     "permalink":"https://www.linkedin.com/company/2716702",
                     "createdTime":"0",
                     "profileImgUrl":"https://media.licdn.com/mpr/mpr/AAEAAQAAAAAAAAQbAAAAJDk3NWIyYWZiLTEwNWMtNGNlMi04NzZkLWViMTRhMDVmMWE5Mw.png",
                     "profileWorkflowProperties":{
                        "tags":[
                           {
                              "tagName":"sports",
                              "iconUrl":"http://pz.cdata.prod0.sprinklr.com/DAM/9004/http---cdata.staging.sprinklr.-dc26100f-4ec5-4877-8429-005d362ab5f2-342647189.jpg"
                           },
                           {
                              "tagName":"ank-123",
                              "iconUrl":"http://pz.cdata.prod0.sprinklr.com/DAM/9004/1982172_837685306321440_552042-7fa27056-fe29-4570-b40a-2203c6349a10-1068894126.jpg"
                           },
                           {
                              "tagName":"NoRuleTag",
                              "iconUrl":"http://pz.cdata.prod0.sprinklr.com/DAM/9004/11811473_882223838542043_42641-4b00077a-c4d2-4a35-839e-911a3d635739-1583664707.jpg"
                           },
                           {
                              "tagName":"11.1.0",
                              "iconUrl":"https://sprcdn-prod0-sam.sprinklr.com/9004/Japanese_Tea_Garden_(San_Franc-691060b1-926f-4747-a7d9-98b3eeb4684e-712355925.jpg"
                           },
                           {
                              "tagName":"dqsdqsd",
                              "iconUrl":""
                           },
                           {
                              "tagName":"new profile",
                              "iconUrl":""
                           },
                           {
                              "tagName":"34",
                              "iconUrl":""
                           }
                        ],
                        "comments":[
                        ],
                        "notifyUserIds":[
                        ],
                        "partnerProfileLists":[
                        ],
                        "clientProfileLists":[
                           3,
                           9
                        ],
                        "partnerCustomProperties":{
                           "5a030faee4b05c3793563fc4":[
                              ""
                           ],
                           "570de778e4b020af03efb53b":[
                              "24"
                           ],
                           "5809acb8e4b027d61cf7d4d0":[
                              ""
                           ],
                           "57bafc34e4b01efb5609d67c":[
                              ""
                           ],
                           "57baf9f7e4b01efb5609d5dd":[
                              ""
                           ],
                           "5809af23e4b027d61cf7d526":[
                              "test"
                           ],
                           "57507a18e4b02aaccdaf4851":[
                              ""
                           ],
                           "589583f0e4b035a892f57632":[
                              "2"
                           ],
                           "5809b05ee4b027d61cf7d554":[
                              ""
                           ],
                           "58e9c13ee4b0d91456ca8ea8":[
                              ""
                           ],
                           "594a4252e4b02f890c71a253":[
                              ""
                           ]
                        },
                        "clientCustomProperties":{
                           "57bc22ffe4b01efb560a5b67":[
                              ""
                           ],
                           "57e35db6e4b0774076ac2d96":[
                              "Available"
                           ],
                           "591d7c1ce4b0de015d42885f":[
                              "1"
                           ],
                           "56fce6135f94c60904000001":[
                              "1456876800000"
                           ],
                           "591d7b97e4b0de015d428856":[
                              "2"
                           ],
                           "57e35d6fe4b0774076ac2d93":[
                              "3/5 Stag"
                           ],
                           "58f9e8b4e4b0dc1273e3cb34":[
                              "q"
                           ],
                           "5880b190e4b05642ae53d6ee":[
                              ""
                           ],
                           "57e35eb5e4b0774076ac2da6":[
                              ""
                           ],
                           "57bc16f5e4b01efb560a4f1b":[
                              ""
                           ],
                           "5847b7b2e4b056818a8ebd40":[
                              ""
                           ],
                           "5912b0e3e4b0e75c4103ec35":[
                              "aa"
                           ],
                           "57ce924ee4b0c6ed5cf40bdb":[
                              ""
                           ],
                           "58c78bb0e4b08e7cbb95f37f":[
                              ""
                           ],
                           "591d7ab6e4b0de015d428832":[
                              "1"
                           ],
                           "58f4a65ee4b098dec86c5384":[
                              "100"
                           ],
                           "5709fbf1e4b0e249972c6e10":[
                              ""
                           ],
                           "57e35d36e4b0774076ac2d90":[
                              "4.2/5"
                           ],
                           "57e35cf7e4b0774076ac2d8d":[
                              "7.6"
                           ],
                           "57e6b065e4b0d2f9340bbdae":[
                              "Test for audience update rule only actions"
                           ]
                        },
                        "spaceCustomProperties":{
                        },
                        "userCustomProperties":{
                        },
                        "clientTags":[
                        ]
                     },
                     "universalProfileId":"562f2aafe4b018e513d003cc",
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
                     "accountsSuspendingUser":[
                     ],
                     "profileTags":[
                        {
                           "tagName":"sports",
                           "iconUrl":"http://pz.cdata.prod0.sprinklr.com/DAM/9004/http---cdata.staging.sprinklr.-dc26100f-4ec5-4877-8429-005d362ab5f2-342647189.jpg"
                        },
                        {
                           "tagName":"ank-123",
                           "iconUrl":"http://pz.cdata.prod0.sprinklr.com/DAM/9004/1982172_837685306321440_552042-7fa27056-fe29-4570-b40a-2203c6349a10-1068894126.jpg"
                        },
                        {
                           "tagName":"NoRuleTag",
                           "iconUrl":"http://pz.cdata.prod0.sprinklr.com/DAM/9004/11811473_882223838542043_42641-4b00077a-c4d2-4a35-839e-911a3d635739-1583664707.jpg"
                        },
                        {
                           "tagName":"11.1.0",
                           "iconUrl":"https://sprcdn-prod0-sam.sprinklr.com/9004/Japanese_Tea_Garden_(San_Franc-691060b1-926f-4747-a7d9-98b3eeb4684e-712355925.jpg"
                        },
                        {
                           "tagName":"dqsdqsd",
                           "iconUrl":""
                        },
                        {
                           "tagName":"new profile",
                           "iconUrl":""
                        },
                        {
                           "tagName":"34",
                           "iconUrl":""
                        }
                     ]
                  },
                  "receiverProfile":{
                     "age":0,
                     "following":0,
                     "followers":0,
                     "favCount":0,
                     "statusCount":0,
                     "profileWorkflowProperties":{
                        "tags":[
                        ],
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
                     "accountsSuspendingUser":[
                     ]
                  },
                  "isSenderFollower":false,
                  "createdTime":1464382186773,
                  "modifiedTime":1501560306681,
                  "snCreatedTime":1464376801310,
                  "snCreatedTimeYearMonth":"2016_05",
                  "snModifiedTime":1464376801310,
                  "snStats":{
                     "nAC":1
                  },
                  "mediaList":[
                  ],
                  "geoTarget":{
                     "countries":[
                        ""
                     ]
                  },
                  "workflowProperties":{
                     "sentiment":0,
                     "isSpam":false,
                     "isProfane":false,
                     "read":false
                  },
                  "language":"en",
                  "conversationId":"UPDATE-c2716702-6142041475082448896",
                  "parentMsgType":0,
                  "deleted":false,
                  "archived":false,
                  "brandPost":false,
                  "parentBrandPost":false,
                  "hasBrandComment":false,
                  "hasBrandResponded":false,
                  "hasScheduledComment":false,
                  "hasParentPost":false,
                  "hasApplicationConversation":false,
                  "rootUniversalMessageId":"LINKEDIN_16_UPDATE-c2716702-6142041475082448896",
                  "isSharedPost":false,
                  "hasConversation":false,
                  "caseCount":3,
                  "associatedCases":[
                     "9661",
                     "10001",
                     "10633"
                  ],
                  "hasChildren":false,
                  "workflowComments":[
                  ],
                  "userActions":[
                  ]
               }
            }
         },
         "changes":[
            {
               "fieldName":"Messages",
               "fieldType":"MESSAGE",
               "oldValues":[
               ],
               "newValues":[
                  "LINKEDINπ16πUPDATE-c2716702-6142041475082448896πACCOUNTπ1000067732π1464376801310π2016_05"
               ],
               "lookupInfo":{
                  "fieldType":"MESSAGE"
               }
            }
         ],
         "partnerId":9004,
         "userId":-100,
         "assetId":"10001",
         "changeDate":1464382187904,
         "changeType":"UNIVERSAL_CASE_CREATED",
         "changeGroupId":"5748b2ebe4b00057e58c2db9",
         "assetClass":"UNIVERSAL_CASE"
      }
   ],
   "hasMore":true
}






	[](https://dev.sprinklr.com/audit-api-v1)




[Back to top](https://dev.sprinklr.com/audit-api-v1)
