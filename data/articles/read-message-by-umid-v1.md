---
title: "Read Message by UMID v1"
slug: read-message-by-umid-v1
url: https://dev.sprinklr.com/read-message-by-umid-v1
---

# Read Message by UMID v1

# GET Read Message by UMID v1

You can fetch a message by UMID (Universal Message Id) using this API.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/message/{umId}

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

### Path Parameter
















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| umId | Required | Universal message Id. | String |

## Example - Request




 Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v1/message/FACEBOOK_38_m_twzI1_jyxOGluQszKFygpqvPon4OcDB9fenOopASnXgOo9wCX5O0Ahn2sIHUZ1-I1PAGzAXE-_EykBn3LcQYfA' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'


## Example - Response




{
    "canEdit": false,
    "hasThreadControl": true,
    "isPrimaryReceiver": false,
    "isSecondaryReceiver": false,
    "threadKey": "t_757285288058965",
    "partnerId": 9004,
    "clientId": 1000004509,
    "sourceId": 1000067750,
    "accountId": 1000067750,
    "sourceType": "ACCOUNT",
    "snType": "FACEBOOK",
    "snMsgId": "m_twzI1_jyxOGluQszKFygpqvPon4OcDB9fenOopASnXgOo9wCX5O0Ahn2sIHUZ1-I1PAGzAXE-_EykBn3LcQYfA",
    "messageType": 38,
    "messageSubType": 46,
    "universalMessageId": "FACEBOOK_38_m_twzI1_jyxOGluQszKFygpqvPon4OcDB9fenOopASnXgOo9wCX5O0Ahn2sIHUZ1-I1PAGzAXE-_EykBn3LcQYfA",
    "permalink": "https://www.facebook.com/SprinklrPaid/inbox/2406487769607913/",
    "message": "Let me verify my HA check",
    "actualText": "Let me verify my HA check",
    "highLightEntities": {},
    "senderProfile": {
        "snType": "FACEBOOK",
        "age": 0,
        "snId": "3436909326380741",
        "name": "San Sandya",
        "firstName": "San",
        "lastName": "Sandya",
        "screenName": "San Sandya",
        "subType": "USER",
        "following": 0,
        "followers": 0,
        "favCount": 0,
        "statusCount": 0,
        "createdTime": "0",
        "profileImgUrl": "https://platform-lookaside.fbsbx.com/platform/profilepic/?psid=3436909326380741&height=50&width=50&ext=1586527220&hash=AeRSFvR30n9jOvgW",
        "profileWorkflowProperties": {
            "tags": [
                {
                    "tagName": "NoRuleTag",
                    "iconUrl": "http://pz.cdata.prod0.sprinklr.com/DAM/9004/11811473_882223838542043_42641-4b00077a-c4d2-4a35-839e-911a3d635739-1583664707.jpg"
                },
                {
                    "tagName": "11.1.0",
                    "iconUrl": "https://sprcdn-prod0-sam.sprinklr.com/9004/Japanese_Tea_Garden_(San_Franc-691060b1-926f-4747-a7d9-98b3eeb4684e-712355925.jpg"
                },
                {
                    "tagName": "34",
                    "iconUrl": ""
                }
            ],
            "comments": [],
            "notifyUserIds": [],
            "partnerProfileLists": [
                4
            ],
            "clientProfileLists": [
                2
            ],
            "partnerCustomProperties": {
                "59943639e4b0ff87a027c7e4": [
                    "Belgium"
                ],
                "57507acee4b02aaccdaf4863": [
                    "dddd"
                ],
                "57e6ab26e4b0d2f9340bbd6c": [
                    "1474309800000"
                ],
                "57507a18e4b02aaccdaf4851": [
                    "Profile Partner Test"
                ],
                "573d9df2e4b08273cf333d0a": [
                    "100000"
                ],
                "57bc5fe6e4b01efb560a73d9": [
                    "w",
                    "t",
                    "e"
                ],
                "575079c3e4b02aaccdaf484d": [
                    "Normal Text Field"
                ]
            },
            "clientCustomProperties": {
                "57e6b019e4b0d2f9340bbda8": [
                    "1475173800000"
                ],
                "57ac0f9fe4b028ae829e3881": [
                    "500000"
                ],
                "57ce8285e4b0c6ed5cf3ece9": [
                    "Detractor"
                ],
                "57da3bbce4b05575029131fc": [
                    "asd",
                    "assd"
                ]
            },
            "spaceCustomProperties": {},
            "userCustomProperties": {},
            "clientTags": [
                "is not_profile"
            ]
        },
        "universalProfileId": "5ce78591e4b0a6ca36a55dac",
        "participationIndex": 0.0,
        "influencerIndex": 0.0,
        "spamIndex": 0.0,
        "accountsFollowedByUser": [],
        "accountsFollowingUser": [],
        "accountsUnFollowingUser": [],
        "accountsUnFollowedByUser": [],
        "accountsBlockingUser": [],
        "accountsSuspendingUser": [],
        "profileTags": [
            {
                "tagName": "NoRuleTag",
                "iconUrl": "http://pz.cdata.prod0.sprinklr.com/DAM/9004/11811473_882223838542043_42641-4b00077a-c4d2-4a35-839e-911a3d635739-1583664707.jpg"
            },
            {
                "tagName": "11.1.0",
                "iconUrl": "https://sprcdn-prod0-sam.sprinklr.com/9004/Japanese_Tea_Garden_(San_Franc-691060b1-926f-4747-a7d9-98b3eeb4684e-712355925.jpg"
            },
            {
                "tagName": "34",
                "iconUrl": ""
            }
        ],
        "externalId": "3436909326380741",
        "accountSpecificInfos": [
            {
                "accountId": 1000067750,
                "externalId": "3436909326380741",
                "hasUserBrandResponse": true,
                "lastFanEngagedTime": 1583935217000,
                "profilePMThreadId": "t_757285288058965",
                "profileLastPMTime": 1583936102000,
                "permalink": "/SprinklrPaid/inbox/2406487769607913/"
            }
        ],
        "accountSpecificInfoMap": {
            "1000067750": {
                "accountId": 1000067750,
                "externalId": "3436909326380741",
                "hasUserBrandResponse": true,
                "lastFanEngagedTime": 1583935217000,
                "profilePMThreadId": "t_757285288058965",
                "profileLastPMTime": 1583936102000,
                "permalink": "/SprinklrPaid/inbox/2406487769607913/"
            }
        }
    },
    "receiverProfile": {
        "snType": "FACEBOOK",
        "age": 0,
        "snId": "1595783670678331",
        "name": "Paid Media Global",
        "firstName": "Paid",
        "lastName": "Global",
        "screenName": "Paid Media Global",
        "bio": "We promote the paid media through our brand sprinklr",
        "subType": "PAGE",
        "following": 0,
        "followers": 3370,
        "favCount": 0,
        "statusCount": 0,
        "permalink": "https://www.facebook.com/SprinklrPaid/",
        "createdTime": "0",
        "profileImgUrl": "https://scontent.xx.fbcdn.net/v/t1.0-1/cp0/p50x50/60871769_2403924643197559_4059654073735970816_n.jpg?_nc_cat=101&_nc_sid=dbb9e7&_nc_ohc=H47En7UUiwoAX9ovtCf&_nc_ht=scontent.xx&oh=606155473b30cf6b40c71a34c5bf98b2&oe=5EA60448",
        "verified": false,
        "profileWorkflowProperties": {
            "tags": [
                {
                    "tagName": "NoRuleTag",
                    "iconUrl": "http://pz.cdata.prod0.sprinklr.com/DAM/9004/11811473_882223838542043_42641-4b00077a-c4d2-4a35-839e-911a3d635739-1583664707.jpg"
                },
                {
                    "tagName": "11.1.0",
                    "iconUrl": "https://sprcdn-prod0-sam.sprinklr.com/9004/Japanese_Tea_Garden_(San_Franc-691060b1-926f-4747-a7d9-98b3eeb4684e-712355925.jpg"
                },
                {
                    "tagName": "34",
                    "iconUrl": ""
                }
            ],
            "comments": [],
            "notifyUserIds": [],
            "partnerProfileLists": [
                40
            ],
            "clientProfileLists": [
                3
            ],
            "partnerCustomProperties": {
                "570de778e4b020af03efb53b": [
                    "24"
                ],
                "5809acb8e4b027d61cf7d4d0": [
                    ""
                ],
                "57baf9f7e4b01efb5609d5dd": [
                    ""
                ],
                "5809af23e4b027d61cf7d526": [
                    "en"
                ],
                "57507a18e4b02aaccdaf4851": [
                    ""
                ],
                "5809b05ee4b027d61cf7d554": [
                    ""
                ],
                "589583f0e4b035a892f57632": [
                    "2"
                ],
                "58e9c13ee4b0d91456ca8ea8": [
                    ""
                ],
                "57e6a963e4b0d2f9340bbd59": [
                    "q"
                ],
                "59943639e4b0ff87a027c7e4": [
                    "Belgium"
                ]
            },
            "clientCustomProperties": {
                "57e35db6e4b0774076ac2d96": [
                    "Available"
                ],
                "591d7c1ce4b0de015d42885f": [
                    "1"
                ],
                "56fce6135f94c60904000001": [
                    "1456876800000"
                ],
                "57e35d6fe4b0774076ac2d93": [
                    "3/5 Stag"
                ],
                "591d7b97e4b0de015d428856": [
                    "1"
                ],
                "58f9e8b4e4b0dc1273e3cb34": [
                    "q"
                ],
                "57ce8285e4b0c6ed5cf3ece9": [
                    "Promoter"
                ],
                "57e35eb5e4b0774076ac2da6": [
                    ""
                ],
                "5663d839f6d7f12f4d000002": [
                    "Cool"
                ],
                "5847b7b2e4b056818a8ebd40": [
                    ""
                ],
                "57bc16f5e4b01efb560a4f1b": [
                    ""
                ],
                "58c78bb0e4b08e7cbb95f37f": [
                    ""
                ],
                "57ce924ee4b0c6ed5cf40bdb": [
                    ""
                ],
                "591d7ab6e4b0de015d428832": [
                    "1"
                ],
                "58f4a65ee4b098dec86c5384": [
                    "100"
                ],
                "5709fbf1e4b0e249972c6e10": [
                    ""
                ],
                "57e35d36e4b0774076ac2d90": [
                    "4.2/5"
                ],
                "57e35cf7e4b0774076ac2d8d": [
                    "7.6"
                ],
                "57e6b065e4b0d2f9340bbdae": [
                    "Test for audience update rule only actions"
                ]
            },
            "spaceCustomProperties": {},
            "userCustomProperties": {},
            "clientTags": [
                "new tag",
                "is not_profile"
            ]
        },
        "universalProfileId": "56546a31e4b07c1872e9cb66",
        "participationIndex": 0.0,
        "influencerIndex": 8.0,
        "spamIndex": 0.0,
        "accountsFollowedByUser": [],
        "accountsFollowingUser": [],
        "accountsUnFollowingUser": [],
        "accountsUnFollowedByUser": [],
        "accountsBlockingUser": [],
        "accountsSuspendingUser": [],
        "profileTags": [
            {
                "tagName": "NoRuleTag",
                "iconUrl": "http://pz.cdata.prod0.sprinklr.com/DAM/9004/11811473_882223838542043_42641-4b00077a-c4d2-4a35-839e-911a3d635739-1583664707.jpg"
            },
            {
                "tagName": "11.1.0",
                "iconUrl": "https://sprcdn-prod0-sam.sprinklr.com/9004/Japanese_Tea_Garden_(San_Franc-691060b1-926f-4747-a7d9-98b3eeb4684e-712355925.jpg"
            },
            {
                "tagName": "34",
                "iconUrl": ""
            }
        ],
        "externalId": "1595783670678331",
        "accountSpecificInfos": [
            {
                "accountId": 1000067750,
                "externalId": "1595783670678331"
            }
        ],
        "accountSpecificInfoMap": {
            "1000067750": {
                "accountId": 1000067750,
                "externalId": "1595783670678331"
            }
        }
    },
    "isSenderFollower": false,
    "createdTime": 1583935220557,
    "modifiedTime": 1583937997550,
    "snCreatedTime": 1583935217000,
    "snCreatedTimeYearMonth": "2020_03",
    "snModifiedTime": 1583935217000,
    "mediaList": [],
    "geoTarget": {
        "countries": [
            "Global"
        ]
    },
    "rawMessage": "Let me verify my HA check",
    "workflowProperties": {
        "sentiment": 0,
        "isSpam": false,
        "isProfane": false,
        "read": false
    },
    "language": "en",
    "conversationId": "t_757285288058965",
    "parentMsgType": 0,
    "deleted": false,
    "archived": false,
    "brandPost": false,
    "parentBrandPost": false,
    "hasBrandComment": true,
    "hasBrandResponded": true,
    "hasScheduledComment": false,
    "hasParentPost": false,
    "hasApplicationConversation": false,
    "rootUniversalMessageId": "FACEBOOK_38_t_757285288058965",
    "isSharedPost": false,
    "hasConversation": true,
    "colorCode": "red",
    "colorDescription": "0-24 hours range",
    "sFCaseCreationEnabled": true,
    "canCreateSFCase": true,
    "sFTaskCreationEnabled": true,
    "canCreateSFTask": false,
    "accountType": "FBPAGE",
    "isSecure": true,
    "isStrictSecure": true,
    "brandResponseByUser": 1000053136,
    "lastRespondedMsgType": 39,
    "hasChildren": false,
    "workflowComments": [],
    "userActions": [],
    "status": "read",
    "detectedSurveyMessage": false,
    "sourceInfos": []
}

## For Facebook Compliance: FB Human Agent Tag

For the [Facebook compliance](https://help.sprinklr.com/Knowledge_Base/Experience_Cloud_User_Guides/Channel_Guides/Facebook_Channel_Overview/Facebook_Messenger_Platform_Policy_for_Replying_to_Customer_Inquiries) regarding the `Facebook Messenger Platform Policy` , you can use the following information from the above response.

## Example - Response




"accountSpecificInfos": [
            {
                "accountId": 1000067750,
                "externalId": "3436909326380741",
                "hasUserBrandResponse": true,
                "lastFanEngagedTime": 1583935217000,
                "profilePMThreadId": "t_757285288058965",
                "profileLastPMTime": 1583936102000,
                "permalink": "/SprinklrPaid/inbox/2406487769607913/"
            }
        ]

[](https://dev.sprinklr.com/read-message-by-umid-v1)
