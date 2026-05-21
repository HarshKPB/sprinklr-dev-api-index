---
title: "Message Conversation Read v1"
slug: message-conversation-read-v1
url: https://dev.sprinklr.com/message-conversation-read-v1
---

# Message Conversation Read v1

#  POST Message Conversation Read v1

Using this API, you can fetch the children messages that are linked with parent message Id within a conversation.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v1/conversations/new/children

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
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal. |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

## Request Parameters



















		[Channel Type](https://dev.sprinklr.com/channels-v1)






















[MessageType](https://dev.sprinklr.com/message-v1)
















| Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| parentSnMsgId | Required | The unique parent message Identifier received from channel. | String |
| sntype | Required | for the message. | String |
| sourceType | Required | Message SourceType = {ACCOUNT, PERSISTENT_SEARCH, LISTENING, BENCHMARKING, AUDIENCE, AUDIENCE_STUDY}. | String |
| sourceId | Optional | AccountId. | Long |
| messageType | Required | Sprinklr supported message types messages are either inbound (from a channel) or outbound (posts to a channel). | Integer |
| sortOrder | Optional | The order in which you want to sort the response. i.e. ASC or DESC. | Integer |
| upto | Required | The time in Epoch to which you want to fetch messages from parent message. | Epoch |

## Example - Request




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/conversations/new/children' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'key: {apikey}' \
  -d '{
    "parentSnMsgId": "2091657247780860_2605186629761250",
    "snType": "FACEBOOK",
    "sourceType": "ACCOUNT",
    "sourceId": 1000073624,
    "msgType": 14,
    "rows":100,
    "sortOrder": "DESC",
    "upto":"1596099143001"
}'



## Example - Response




{
    "data": [
        {
            "likeFlag": false,
            "hasBrandReply": false,
            "hasCommentReply": false,
            "hidden": false,
            "canRemove": true,
            "canHide": false,
            "canComment": true,
            "canReplyPrivately": false,
            "isShadowPost": false,
            "isReview": false,
            "ageGated": false,
            "canEdit": true,
            "partnerId": 9004,
            "clientId": 1000004509,
            "sourceId": 1000073624,
            "accountId": 1000073624,
            "sourceType": "ACCOUNT",
            "snType": "FACEBOOK",
            "snMsgId": "2605186629761250_2683192528627326",
            "messageType": 14,
            "messageSubType": 257,
            "universalMessageId": "FACEBOOK_14_2605186629761250_2683192528627326",
            "postId": 2016935270,
            "selfPostId": 2066520191,
            "campaignId": 1182,
            "campaignClientId": 1000004509,
            "clientAndCampaignId": "1000004509_1182",
            "isAutoImported": true,
            "permalink": "https://www.facebook.com/2091657247780860/posts/2605186629761250/?comment_id=2683192528627326",
            "message": "How do you like this Traditional Food?",
            "actualText": "How do you like this Traditional Food?",
            "textEntities": {
                "message": [
                    {
                        "indices": [
                            21,
                            37
                        ],
                        "screenName": "Traditional Food",
                        "snUserId": "1172417539573743",
                        "copiableEntity": false,
                        "striked": false
                    }
                ]
            },
            "highLightEntities": {},
            "senderProfile": {
                "snType": "FACEBOOK",
                "age": 0,
                "snId": "2091657247780860",
                "name": "PBot",
                "firstName": "PBot",
                "screenName": "PBot",
                "bio": "This place is for the foodies.This place is for the foodies.This place is for the foodies.",
                "subType": "PAGE",
                "following": 0,
                "followers": 24,
                "favCount": 0,
                "statusCount": 0,
                "permalink": "https://www.facebook.com/2091657247780860",
                "createdTime": "1601318437221",
                "profileImgUrl": "https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-1/p200x200/119556962_2726481864298392_5287330585436753512_n.png?_nc_cat=103&_nc_sid=dbb9e7&_nc_ohc=bL8f0KTz4S0AX-H4Yka&_nc_ht=scontent-iad3-1.xx&oh=39d051a41571f4a22a9932db74334b03&oe=5F9BDAEE",
                "verified": false,
                "profileWorkflowProperties": {
                    "tags": [
                        {
                            "tagName": "34",
                            "iconUrl": ""
                        }
                    ],
                    "comments": [],
                    "notifyUserIds": [],
                    "partnerProfileLists": [
                        2102,
                        2137,
                        2154,
                        2135
                    ],
                    "clientProfileLists": [
                        2568,
                        2548
                    ],
                    "partnerCustomProperties": {
                        "5dd395639c96e811a8e1b4ca": [
                            "Hello"
                        ],
                        "59943639e4b0ff87a027c7e4": [
                            "Germany"
                        ]
                    },
                    "clientCustomProperties": {
                        "5bab707de4b0947df29a41b9": [],
                        "5b1006f1e4b0a54914f86df2": [
                            "France"
                        ]
                    },
                    "spaceCustomProperties": {},
                    "userCustomProperties": {},
                    "clientTags": [
                        "media",
                        "nav1",
                        "follower_count"
                    ]
                },
                "universalProfileId": "5eb50971777cf00001653fc8",
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
                "profileTags": [
                    {
                        "tagName": "34",
                        "iconUrl": ""
                    }
                ],
                "externalId": "2091657247780860",
                "accountSpecificInfos": [
                    {
                        "accountId": 1000073624,
                        "externalId": "2091657247780860"
                    }
                ],
                "accountSpecificInfoMap": {
                    "1000073624": {
                        "accountId": 1000073624,
                        "externalId": "2091657247780860"
                    }
                },
                "additional": {
                    "appIdCPId": [
                        "5ae6c4c9e4b0cde987870359π5edf1eadee49456bd4c8232e",
                        "5ae6c4c9e4b0cde987870359π5edf2340ee49456bd41a093f",
                        "5ae6c4c9e4b0cde987870359π5edf2a29ee49456bd47595bf",
                        "5f5226afdaf49968c82bb0d7πBsonObjectId{value=5f522758268f0fbdb36ec6ec}",
                        "5f5226afdaf49968c82bb0d7πBsonObjectId{value=5f5227da268f0fbdb377a7d7}"
                    ],
                    "profileEngaged": [
                        "true"
                    ],
                    "cCFP": [
                        "true"
                    ],
                    "appId": [
                        "5f0801899c11484bbf470f95",
                        "5ddba8369c96e82af6c57518",
                        "5f5226afdaf49968c82bb0d7"
                    ],
                    "appOrgId": [
                        "00D7F000003fsQsUAI",
                        "00D2w000000lCQnEAM",
                        "00D28000000WlceEAC"
                    ]
                }
            },
            "receiverProfile": {
                "age": 0,
                "following": 0,
                "followers": 0,
                "favCount": 0,
                "statusCount": 0,
                "profileWorkflowProperties": {
                    "tags": [],
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
                "participationIndex": 0.0,
                "influencerIndex": 0.0,
                "spamIndex": 0.0,
                "accountsFollowedByUser": [],
                "accountsFollowingUser": [],
                "accountsUnFollowingUser": [],
                "accountsUnFollowedByUser": [],
                "accountsBlockingUser": [],
                "accountsSuspendingUser": [],
                "accountsDeactivatingUser": []
            },
            "mentionedProfiles": [
                {
                    "snType": "FACEBOOK",
                    "age": 0,
                    "snId": "1172417539573743",
                    "name": "Traditional Food",
                    "screenName": "Traditional Food",
                    "following": 0,
                    "followers": 0,
                    "favCount": 0,
                    "statusCount": 0,
                    "profileImgUrl": "https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-1/c58.0.200.200a/p200x200/41558903_1172418032907027_3657995209024733184_n.png?_nc_cat=108&_nc_sid=dbb9e7&_nc_ohc=7zMOCSRIaTMAX_GsDLb&_nc_ht=scontent-iad3-1.xx&oh=f58bc4b359d41010a9cf512c54f8c684&oe=5F3473CB",
                    "profileWorkflowProperties": {
                        "tags": [],
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
                    "participationIndex": 0.0,
                    "influencerIndex": 0.0,
                    "spamIndex": 0.0,
                    "accountsFollowedByUser": [],
                    "accountsFollowingUser": [],
                    "accountsUnFollowingUser": [],
                    "accountsUnFollowedByUser": [],
                    "accountsBlockingUser": [],
                    "accountsSuspendingUser": [],
                    "accountsDeactivatingUser": []
                }
            ],
            "isSenderFollower": false,
            "createdTime": 1596099148443,
            "modifiedTime": 1596099156068,
            "snCreatedTime": 1596099143000,
            "snCreatedTimeYearMonth": "2020_07",
            "snModifiedTime": 1596099143000,
            "snStats": {
                "nL": 0
            },
            "mediaList": [],
            "geoTarget": {
                "countries": [
                    "Global"
                ]
            },
            "rawMessage": "How do you like this Traditional Food?",
            "workflowProperties": {
                "sentiment": 0,
                "isSpam": false,
                "isProfane": false,
                "tags": [
                    "secure"
                ],
                "clientQueues": [
                    {
                        "clientQueueQueryField": "1000004509_65",
                        "queueId": 65,
                        "queueAssignedTime": 1596099148605
                    }
                ],
                "partnerQueues": [
                    {
                        "queueId": 11,
                        "queueAssignedTime": 1596099148605
                    }
                ],
                "contentLists": [],
                "partnerCustomProperties": {},
                "processingUserDetailsList": [],
                "read": false
            },
            "language": "en",
            "conversationId": "2091657247780860_2605186629761250",
            "parentSnMsgId": "2091657247780860_2605186629761250",
            "parentSnCreatedTimeYearMonth": "2020_04",
            "parentMsgType": 15,
            "deleted": false,
            "archived": false,
            "brandPost": true,
            "parentBrandPost": true,
            "hasBrandComment": true,
            "hasBrandResponded": false,
            "hasScheduledComment": false,
            "hasParentPost": true,
            "hasApplicationConversation": false,
            "rootUniversalMessageId": "FACEBOOK_15_2091657247780860_2605186629761250",
            "isSharedPost": false,
            "numberOfComments": 0,
            "hasConversation": false,
            "colorCode": "green",
            "colorDescription": "20 days - 30 days range",
            "sFCaseCreationEnabled": true,
            "canCreateSFCase": true,
            "sFTaskCreationEnabled": true,
            "canCreateSFTask": false,
            "accountType": "FBPAGE",
            "isSecure": true,
            "isBrandInitiatedConversation": true,
            "audienceTargets": [
                {
                    "targetOptions": {},
                    "placementType": "PAGE",
                    "operator": "OR"
                }
            ],
            "numOfWorkFlowComments": 1,
            "hasWorkFlowComment": true,
            "hasChildren": false,
            "parentUniversalMessageKey": {
                "universalMessageId": "FACEBOOK_15_2091657247780860_2605186629761250",
                "snType": "FACEBOOK",
                "msgType": 15,
                "snMsgId": "2091657247780860_2605186629761250",
                "sourceId": 1000073624,
                "sourceType": "ACCOUNT",
                "snCreatedTimeYearMonth": "2020_04",
                "snCreatedTime": 1588013222000
            },
            "altPUMK": {
                "universalMessageId": "FACEBOOK_15_2091657247780860_2605186629761250",
                "snType": "FACEBOOK",
                "msgType": 15,
                "snMsgId": "2091657247780860_2605186629761250",
                "sourceId": 1000073624,
                "sourceType": "ACCOUNT",
                "snCreatedTimeYearMonth": "2020_04",
                "snCreatedTime": 1588013222000
            },
            "workflowComments": [
                {
                    "id": "5f228a549ce63f1d603fefa3",
                    "comment": "adsf",
                    "commentingUser": -100,
                    "commentedOnDate": 1596099156051,
                    "commentUpdateDate": 1596099156051,
                    "onAsset": "MESSAGE_WORKFLOW",
                    "assetId": "FACEBOOK_14_2605186629761250_2683192528627326",
                    "partnerId": 9004,
                    "clientId": -1,
                    "isEdited": false,
                    "isEditable": false,
                    "deleted": false,
                    "hasConversation": false
                }
            ],
            "userActions": [],
            "detectedSurveyMessage": false,
            "sourceInfos": []
        },
        {
            "likeFlag": false,
            "hasBrandReply": false,
            "hasCommentReply": false,
            "hidden": false,
            "canRemove": true,
            "canHide": false,
            "canComment": true,
            "canReplyPrivately": false,
            "isShadowPost": false,
            "isReview": false,
            "ageGated": false,
            "canEdit": true,
            "partnerId": 9004,
            "clientId": 1000004509,
            "sourceId": 1000073624,
            "accountId": 1000073624,
            "sourceType": "ACCOUNT",
            "snType": "FACEBOOK",
            "snMsgId": "2605186629761250_2683192531960659",
            "messageType": 14,
            "messageSubType": 257,
            "universalMessageId": "FACEBOOK_14_2605186629761250_2683192531960659",
            "postId": 2016935270,
            "selfPostId": 2066520213,
            "campaignId": 1182,
            "campaignClientId": 1000004509,
            "clientAndCampaignId": "1000004509_1182",
            "isAutoImported": true,
            "permalink": "https://www.facebook.com/2091657247780860/posts/2605186629761250/?comment_id=2683192531960659",
            "message": "We will win this time #confident #believe #positive",
            "actualText": "We will win this time #confident #believe #positive",
            "textEntities": {
                "message": [
                    {
                        "indices": [
                            22,
                            32
                        ],
                        "hashtag": "confident",
                        "copiableEntity": false,
                        "striked": false
                    },
                    {
                        "indices": [
                            33,
                            41
                        ],
                        "hashtag": "believe",
                        "copiableEntity": false,
                        "striked": false
                    },
                    {
                        "indices": [
                            42,
                            51
                        ],
                        "hashtag": "positive",
                        "copiableEntity": false,
                        "striked": false
                    }
                ]
            },
            "highLightEntities": {},
            "senderProfile": {
                "snType": "FACEBOOK",
                "age": 0,
                "snId": "2091657247780860",
                "name": "PBot",
                "firstName": "PBot",
                "screenName": "PBot",
                "bio": "This place is for the foodies.This place is for the foodies.This place is for the foodies.",
                "subType": "PAGE",
                "following": 0,
                "followers": 24,
                "favCount": 0,
                "statusCount": 0,
                "permalink": "https://www.facebook.com/2091657247780860",
                "createdTime": "1601318437221",
                "profileImgUrl": "https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-1/p200x200/119556962_2726481864298392_5287330585436753512_n.png?_nc_cat=103&_nc_sid=dbb9e7&_nc_ohc=bL8f0KTz4S0AX-H4Yka&_nc_ht=scontent-iad3-1.xx&oh=39d051a41571f4a22a9932db74334b03&oe=5F9BDAEE",
                "verified": false,
                "profileWorkflowProperties": {
                    "tags": [
                        {
                            "tagName": "34",
                            "iconUrl": ""
                        }
                    ],
                    "comments": [],
                    "notifyUserIds": [],
                    "partnerProfileLists": [
                        2102,
                        2137,
                        2154,
                        2135
                    ],
                    "clientProfileLists": [
                        2568,
                        2548
                    ],
                    "partnerCustomProperties": {
                        "5dd395639c96e811a8e1b4ca": [
                            "Hello"
                        ],
                        "59943639e4b0ff87a027c7e4": [
                            "Germany"
                        ]
                    },
                    "clientCustomProperties": {
                        "5bab707de4b0947df29a41b9": [],
                        "5b1006f1e4b0a54914f86df2": [
                            "France"
                        ]
                    },
                    "spaceCustomProperties": {},
                    "userCustomProperties": {},
                    "clientTags": [
                        "media",
                        "nav1",
                        "follower_count"
                    ]
                },
                "universalProfileId": "5eb50971777cf00001653fc8",
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
                "profileTags": [
                    {
                        "tagName": "34",
                        "iconUrl": ""
                    }
                ],
                "externalId": "2091657247780860",
                "accountSpecificInfos": [
                    {
                        "accountId": 1000073624,
                        "externalId": "2091657247780860"
                    }
                ],
                "accountSpecificInfoMap": {
                    "1000073624": {
                        "accountId": 1000073624,
                        "externalId": "2091657247780860"
                    }
                },
                "additional": {
                    "appIdCPId": [
                        "5ae6c4c9e4b0cde987870359π5edf1eadee49456bd4c8232e",
                        "5ae6c4c9e4b0cde987870359π5edf2340ee49456bd41a093f",
                        "5ae6c4c9e4b0cde987870359π5edf2a29ee49456bd47595bf",
                        "5f5226afdaf49968c82bb0d7πBsonObjectId{value=5f522758268f0fbdb36ec6ec}",
                        "5f5226afdaf49968c82bb0d7πBsonObjectId{value=5f5227da268f0fbdb377a7d7}"
                    ],
                    "profileEngaged": [
                        "true"
                    ],
                    "cCFP": [
                        "true"
                    ],
                    "appId": [
                        "5f0801899c11484bbf470f95",
                        "5ddba8369c96e82af6c57518",
                        "5f5226afdaf49968c82bb0d7"
                    ],
                    "appOrgId": [
                        "00D7F000003fsQsUAI",
                        "00D2w000000lCQnEAM",
                        "00D28000000WlceEAC"
                    ]
                }
            },
            "receiverProfile": {
                "age": 0,
                "following": 0,
                "followers": 0,
                "favCount": 0,
                "statusCount": 0,
                "profileWorkflowProperties": {
                    "tags": [],
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
                "participationIndex": 0.0,
                "influencerIndex": 0.0,
                "spamIndex": 0.0,
                "accountsFollowedByUser": [],
                "accountsFollowingUser": [],
                "accountsUnFollowingUser": [],
                "accountsUnFollowedByUser": [],
                "accountsBlockingUser": [],
                "accountsSuspendingUser": [],
                "accountsDeactivatingUser": []
            },
            "isSenderFollower": false,
            "createdTime": 1596099151243,
            "modifiedTime": 1596099151809,
            "snCreatedTime": 1596099143000,
            "snCreatedTimeYearMonth": "2020_07",
            "snModifiedTime": 1596099143000,
            "snStats": {
                "nL": 0
            },
            "mediaList": [],
            "geoTarget": {
                "countries": [
                    "Global"
                ]
            },
            "rawMessage": "We will win this time #confident #believe #positive",
            "workflowProperties": {
                "sentiment": 1,
                "isSpam": false,
                "isProfane": false,
                "tags": [
                    "secure"
                ],
                "clientQueues": [
                    {
                        "clientQueueQueryField": "1000004509_65",
                        "queueId": 65,
                        "queueAssignedTime": 1596099151676
                    }
                ],
                "partnerQueues": [
                    {
                        "queueId": 11,
                        "queueAssignedTime": 1596099151676
                    }
                ],
                "contentLists": [],
                "partnerCustomProperties": {},
                "processingUserDetailsList": [],
                "read": false
            },
            "language": "en",
            "conversationId": "2091657247780860_2605186629761250",
            "parentSnMsgId": "2091657247780860_2605186629761250",
            "parentSnCreatedTimeYearMonth": "2020_04",
            "parentMsgType": 15,
            "deleted": false,
            "archived": false,
            "brandPost": true,
            "parentBrandPost": true,
            "hasBrandComment": true,
            "hasBrandResponded": false,
            "hasScheduledComment": false,
            "hasParentPost": true,
            "hasApplicationConversation": false,
            "rootUniversalMessageId": "FACEBOOK_15_2091657247780860_2605186629761250",
            "isSharedPost": false,
            "numberOfComments": 0,
            "hasConversation": false,
            "colorCode": "green",
            "colorDescription": "20 days - 30 days range",
            "sFCaseCreationEnabled": true,
            "canCreateSFCase": true,
            "sFTaskCreationEnabled": true,
            "canCreateSFTask": false,
            "accountType": "FBPAGE",
            "isSecure": true,
            "isBrandInitiatedConversation": true,
            "audienceTargets": [
                {
                    "targetOptions": {},
                    "placementType": "PAGE",
                    "operator": "OR"
                }
            ],
            "numOfWorkFlowComments": 1,
            "hasWorkFlowComment": true,
            "hasChildren": false,
            "parentUniversalMessageKey": {
                "universalMessageId": "FACEBOOK_15_2091657247780860_2605186629761250",
                "snType": "FACEBOOK",
                "msgType": 15,
                "snMsgId": "2091657247780860_2605186629761250",
                "sourceId": 1000073624,
                "sourceType": "ACCOUNT",
                "snCreatedTimeYearMonth": "2020_04",
                "snCreatedTime": 1588013222000
            },
            "altPUMK": {
                "universalMessageId": "FACEBOOK_15_2091657247780860_2605186629761250",
                "snType": "FACEBOOK",
                "msgType": 15,
                "snMsgId": "2091657247780860_2605186629761250",
                "sourceId": 1000073624,
                "sourceType": "ACCOUNT",
                "snCreatedTimeYearMonth": "2020_04",
                "snCreatedTime": 1588013222000
            },
            "workflowComments": [
                {
                    "id": "5f228a4f7dbb921fb6e9c752",
                    "comment": "adsf",
                    "commentingUser": -100,
                    "commentedOnDate": 1596099151791,
                    "commentUpdateDate": 1596099151791,
                    "onAsset": "MESSAGE_WORKFLOW",
                    "assetId": "FACEBOOK_14_2605186629761250_2683192531960659",
                    "partnerId": 9004,
                    "clientId": -1,
                    "isEdited": false,
                    "isEditable": false,
                    "deleted": false,
                    "hasConversation": false
                }
            ],
            "userActions": [],
            "detectedSurveyMessage": false,
            "sourceInfos": []
        },
        {
            "likeFlag": false,
            "hasBrandReply": false,
            "hasCommentReply": false,
            "hidden": false,
            "canRemove": true,
            "canHide": false,
            "canComment": true,
            "canReplyPrivately": false,
            "isShadowPost": false,
            "isReview": false,
            "ageGated": false,
            "canEdit": true,
            "partnerId": 9004,
            "clientId": 1000004509,
            "sourceId": 1000073624,
            "accountId": 1000073624,
            "sourceType": "ACCOUNT",
            "snType": "FACEBOOK",
            "snMsgId": "2605186629761250_2681464058800173",
            "messageType": 14,
            "messageSubType": 257,
            "universalMessageId": "FACEBOOK_14_2605186629761250_2681464058800173",
            "postId": 2016935270,
            "selfPostId": 2066495484,
            "campaignId": 1182,
            "campaignClientId": 1000004509,
            "clientAndCampaignId": "1000004509_1182",
            "isAutoImported": true,
            "permalink": "https://www.facebook.com/2091657247780860/posts/2605186629761250/?comment_id=2681464058800173",
            "message": "In this difficult situation we are with you Traditional Food #support #together",
            "actualText": "In this difficult situation we are with you Traditional Food #support #together",
            "textEntities": {
                "message": [
                    {
                        "indices": [
                            44,
                            60
                        ],
                        "screenName": "Traditional Food",
                        "snUserId": "1172417539573743",
                        "copiableEntity": false,
                        "striked": false
                    },
                    {
                        "indices": [
                            61,
                            69
                        ],
                        "hashtag": "support",
                        "copiableEntity": false,
                        "striked": false
                    },
                    {
                        "indices": [
                            70,
                            79
                        ],
                        "hashtag": "together",
                        "copiableEntity": false,
                        "striked": false
                    }
                ]
            },
            "highLightEntities": {},
            "senderProfile": {
                "snType": "FACEBOOK",
                "age": 0,
                "snId": "2091657247780860",
                "name": "PBot",
                "firstName": "PBot",
                "screenName": "PBot",
                "bio": "This place is for the foodies.This place is for the foodies.This place is for the foodies.",
                "subType": "PAGE",
                "following": 0,
                "followers": 24,
                "favCount": 0,
                "statusCount": 0,
                "permalink": "https://www.facebook.com/2091657247780860",
                "createdTime": "1601318437221",
                "profileImgUrl": "https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-1/p200x200/119556962_2726481864298392_5287330585436753512_n.png?_nc_cat=103&_nc_sid=dbb9e7&_nc_ohc=bL8f0KTz4S0AX-H4Yka&_nc_ht=scontent-iad3-1.xx&oh=39d051a41571f4a22a9932db74334b03&oe=5F9BDAEE",
                "verified": false,
                "profileWorkflowProperties": {
                    "tags": [
                        {
                            "tagName": "34",
                            "iconUrl": ""
                        }
                    ],
                    "comments": [],
                    "notifyUserIds": [],
                    "partnerProfileLists": [
                        2102,
                        2137,
                        2154,
                        2135
                    ],
                    "clientProfileLists": [
                        2568,
                        2548
                    ],
                    "partnerCustomProperties": {
                        "5dd395639c96e811a8e1b4ca": [
                            "Hello"
                        ],
                        "59943639e4b0ff87a027c7e4": [
                            "Germany"
                        ]
                    },
                    "clientCustomProperties": {
                        "5bab707de4b0947df29a41b9": [],
                        "5b1006f1e4b0a54914f86df2": [
                            "France"
                        ]
                    },
                    "spaceCustomProperties": {},
                    "userCustomProperties": {},
                    "clientTags": [
                        "media",
                        "nav1",
                        "follower_count"
                    ]
                },
                "universalProfileId": "5eb50971777cf00001653fc8",
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
                "profileTags": [
                    {
                        "tagName": "34",
                        "iconUrl": ""
                    }
                ],
                "externalId": "2091657247780860",
                "accountSpecificInfos": [
                    {
                        "accountId": 1000073624,
                        "externalId": "2091657247780860"
                    }
                ],
                "accountSpecificInfoMap": {
                    "1000073624": {
                        "accountId": 1000073624,
                        "externalId": "2091657247780860"
                    }
                },
                "additional": {
                    "appIdCPId": [
                        "5ae6c4c9e4b0cde987870359π5edf1eadee49456bd4c8232e",
                        "5ae6c4c9e4b0cde987870359π5edf2340ee49456bd41a093f",
                        "5ae6c4c9e4b0cde987870359π5edf2a29ee49456bd47595bf",
                        "5f5226afdaf49968c82bb0d7πBsonObjectId{value=5f522758268f0fbdb36ec6ec}",
                        "5f5226afdaf49968c82bb0d7πBsonObjectId{value=5f5227da268f0fbdb377a7d7}"
                    ],
                    "profileEngaged": [
                        "true"
                    ],
                    "cCFP": [
                        "true"
                    ],
                    "appId": [
                        "5f0801899c11484bbf470f95",
                        "5ddba8369c96e82af6c57518",
                        "5f5226afdaf49968c82bb0d7"
                    ],
                    "appOrgId": [
                        "00D7F000003fsQsUAI",
                        "00D2w000000lCQnEAM",
                        "00D28000000WlceEAC"
                    ]
                }
            },
            "receiverProfile": {
                "age": 0,
                "following": 0,
                "followers": 0,
                "favCount": 0,
                "statusCount": 0,
                "profileWorkflowProperties": {
                    "tags": [],
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
                "participationIndex": 0.0,
                "influencerIndex": 0.0,
                "spamIndex": 0.0,
                "accountsFollowedByUser": [],
                "accountsFollowingUser": [],
                "accountsUnFollowingUser": [],
                "accountsUnFollowedByUser": [],
                "accountsBlockingUser": [],
                "accountsSuspendingUser": [],
                "accountsDeactivatingUser": []
            },
            "mentionedProfiles": [
                {
                    "snType": "FACEBOOK",
                    "age": 0,
                    "snId": "1172417539573743",
                    "name": "Traditional Food",
                    "screenName": "Traditional Food",
                    "following": 0,
                    "followers": 0,
                    "favCount": 0,
                    "statusCount": 0,
                    "profileImgUrl": "https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-1/c58.0.200.200a/p200x200/41558903_1172418032907027_3657995209024733184_n.png?_nc_cat=108&_nc_sid=dbb9e7&_nc_ohc=7zMOCSRIaTMAX_GsDLb&_nc_ht=scontent-iad3-1.xx&oh=f58bc4b359d41010a9cf512c54f8c684&oe=5F3473CB",
                    "profileWorkflowProperties": {
                        "tags": [],
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
                    "participationIndex": 0.0,
                    "influencerIndex": 0.0,
                    "spamIndex": 0.0,
                    "accountsFollowedByUser": [],
                    "accountsFollowingUser": [],
                    "accountsUnFollowingUser": [],
                    "accountsUnFollowedByUser": [],
                    "accountsBlockingUser": [],
                    "accountsSuspendingUser": [],
                    "accountsDeactivatingUser": []
                }
            ],
            "isSenderFollower": false,
            "createdTime": 1595925470602,
            "modifiedTime": 1595925471041,
            "snCreatedTime": 1595925465000,
            "snCreatedTimeYearMonth": "2020_07",
            "snModifiedTime": 1595925465000,
            "snStats": {
                "nL": 0
            },
            "mediaList": [],
            "geoTarget": {
                "countries": [
                    "Global"
                ]
            },
            "rawMessage": "In this difficult situation we are with you Traditional Food #support #together",
            "workflowProperties": {
                "sentiment": 0,
                "isSpam": false,
                "isProfane": false,
                "tags": [
                    "secure"
                ],
                "clientQueues": [
                    {
                        "clientQueueQueryField": "1000004509_65",
                        "queueId": 65,
                        "queueAssignedTime": 1595925470752
                    }
                ],
                "partnerQueues": [
                    {
                        "queueId": 11,
                        "queueAssignedTime": 1595925470752
                    }
                ],
                "contentLists": [],
                "partnerCustomProperties": {},
                "processingUserDetailsList": [],
                "read": false
            },
            "language": "en",
            "conversationId": "2091657247780860_2605186629761250",
            "parentSnMsgId": "2091657247780860_2605186629761250",
            "parentSnCreatedTimeYearMonth": "2020_04",
            "parentMsgType": 15,
            "deleted": false,
            "archived": false,
            "brandPost": true,
            "parentBrandPost": true,
            "hasBrandComment": true,
            "hasBrandResponded": false,
            "hasScheduledComment": false,
            "hasParentPost": true,
            "hasApplicationConversation": false,
            "rootUniversalMessageId": "FACEBOOK_15_2091657247780860_2605186629761250",
            "isSharedPost": false,
            "numberOfComments": 0,
            "hasConversation": false,
            "colorCode": "green",
            "colorDescription": "20 days - 30 days range",
            "sFCaseCreationEnabled": true,
            "canCreateSFCase": true,
            "sFTaskCreationEnabled": true,
            "canCreateSFTask": false,
            "accountType": "FBPAGE",
            "isSecure": true,
            "isBrandInitiatedConversation": true,
            "audienceTargets": [
                {
                    "targetOptions": {},
                    "placementType": "PAGE",
                    "operator": "OR"
                }
            ],
            "numOfWorkFlowComments": 1,
            "hasWorkFlowComment": true,
            "hasChildren": false,
            "parentUniversalMessageKey": {
                "universalMessageId": "FACEBOOK_15_2091657247780860_2605186629761250",
                "snType": "FACEBOOK",
                "msgType": 15,
                "snMsgId": "2091657247780860_2605186629761250",
                "sourceId": 1000073624,
                "sourceType": "ACCOUNT",
                "snCreatedTimeYearMonth": "2020_04",
                "snCreatedTime": 1588013222000
            },
            "altPUMK": {
                "universalMessageId": "FACEBOOK_15_2091657247780860_2605186629761250",
                "snType": "FACEBOOK",
                "msgType": 15,
                "snMsgId": "2091657247780860_2605186629761250",
                "sourceId": 1000073624,
                "sourceType": "ACCOUNT",
                "snCreatedTimeYearMonth": "2020_04",
                "snCreatedTime": 1588013222000
            },
            "workflowComments": [
                {
                    "id": "5f1fe3df65e8d1650ceba961",
                    "comment": "adsf",
                    "commentingUser": -100,
                    "commentedOnDate": 1595925471029,
                    "commentUpdateDate": 1595925471029,
                    "onAsset": "MESSAGE_WORKFLOW",
                    "assetId": "FACEBOOK_14_2605186629761250_2681464058800173",
                    "partnerId": 9004,
                    "clientId": -1,
                    "isEdited": false,
                    "isEditable": false,
                    "deleted": false,
                    "hasConversation": false
                }
            ],
            "userActions": [],
            "detectedSurveyMessage": false,
            "sourceInfos": []
        },
        {
            "likeFlag": false,
            "hasBrandReply": false,
            "hasCommentReply": false,
            "hidden": false,
            "canRemove": true,
            "canHide": false,
            "canComment": true,
            "canReplyPrivately": false,
            "isShadowPost": false,
            "isReview": false,
            "ageGated": false,
            "canEdit": true,
            "partnerId": 9004,
            "clientId": 1000004509,
            "sourceId": 1000073624,
            "accountId": 1000073624,
            "sourceType": "ACCOUNT",
            "snType": "FACEBOOK",
            "snMsgId": "2605186629761250_2681463928800186",
            "messageType": 14,
            "messageSubType": 257,
            "universalMessageId": "FACEBOOK_14_2605186629761250_2681463928800186",
            "postId": 2016935270,
            "selfPostId": 2066495449,
            "campaignId": 1182,
            "campaignClientId": 1000004509,
            "clientAndCampaignId": "1000004509_1182",
            "isAutoImported": true,
            "permalink": "https://www.facebook.com/2091657247780860/posts/2605186629761250/?comment_id=2681463928800186",
            "message": "How do you like this Traditional Food?",
            "actualText": "How do you like this Traditional Food?",
            "textEntities": {
                "message": [
                    {
                        "indices": [
                            21,
                            37
                        ],
                        "screenName": "Traditional Food",
                        "snUserId": "1172417539573743",
                        "copiableEntity": false,
                        "striked": false
                    }
                ]
            },
            "highLightEntities": {},
            "senderProfile": {
                "snType": "FACEBOOK",
                "age": 0,
                "snId": "2091657247780860",
                "name": "PBot",
                "firstName": "PBot",
                "screenName": "PBot",
                "bio": "This place is for the foodies.This place is for the foodies.This place is for the foodies.",
                "subType": "PAGE",
                "following": 0,
                "followers": 24,
                "favCount": 0,
                "statusCount": 0,
                "permalink": "https://www.facebook.com/2091657247780860",
                "createdTime": "1601318437221",
                "profileImgUrl": "https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-1/p200x200/119556962_2726481864298392_5287330585436753512_n.png?_nc_cat=103&_nc_sid=dbb9e7&_nc_ohc=bL8f0KTz4S0AX-H4Yka&_nc_ht=scontent-iad3-1.xx&oh=39d051a41571f4a22a9932db74334b03&oe=5F9BDAEE",
                "verified": false,
                "profileWorkflowProperties": {
                    "tags": [
                        {
                            "tagName": "34",
                            "iconUrl": ""
                        }
                    ],
                    "comments": [],
                    "notifyUserIds": [],
                    "partnerProfileLists": [
                        2102,
                        2137,
                        2154,
                        2135
                    ],
                    "clientProfileLists": [
                        2568,
                        2548
                    ],
                    "partnerCustomProperties": {
                        "5dd395639c96e811a8e1b4ca": [
                            "Hello"
                        ],
                        "59943639e4b0ff87a027c7e4": [
                            "Germany"
                        ]
                    },
                    "clientCustomProperties": {
                        "5bab707de4b0947df29a41b9": [],
                        "5b1006f1e4b0a54914f86df2": [
                            "France"
                        ]
                    },
                    "spaceCustomProperties": {},
                    "userCustomProperties": {},
                    "clientTags": [
                        "media",
                        "nav1",
                        "follower_count"
                    ]
                },
                "universalProfileId": "5eb50971777cf00001653fc8",
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
                "profileTags": [
                    {
                        "tagName": "34",
                        "iconUrl": ""
                    }
                ],
                "externalId": "2091657247780860",
                "accountSpecificInfos": [
                    {
                        "accountId": 1000073624,
                        "externalId": "2091657247780860"
                    }
                ],
                "accountSpecificInfoMap": {
                    "1000073624": {
                        "accountId": 1000073624,
                        "externalId": "2091657247780860"
                    }
                },
                "additional": {
                    "appIdCPId": [
                        "5ae6c4c9e4b0cde987870359π5edf1eadee49456bd4c8232e",
                        "5ae6c4c9e4b0cde987870359π5edf2340ee49456bd41a093f",
                        "5ae6c4c9e4b0cde987870359π5edf2a29ee49456bd47595bf",
                        "5f5226afdaf49968c82bb0d7πBsonObjectId{value=5f522758268f0fbdb36ec6ec}",
                        "5f5226afdaf49968c82bb0d7πBsonObjectId{value=5f5227da268f0fbdb377a7d7}"
                    ],
                    "profileEngaged": [
                        "true"
                    ],
                    "cCFP": [
                        "true"
                    ],
                    "appId": [
                        "5f0801899c11484bbf470f95",
                        "5ddba8369c96e82af6c57518",
                        "5f5226afdaf49968c82bb0d7"
                    ],
                    "appOrgId": [
                        "00D7F000003fsQsUAI",
                        "00D2w000000lCQnEAM",
                        "00D28000000WlceEAC"
                    ]
                }
            },
            "receiverProfile": {
                "age": 0,
                "following": 0,
                "followers": 0,
                "favCount": 0,
                "statusCount": 0,
                "profileWorkflowProperties": {
                    "tags": [],
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
                "participationIndex": 0.0,
                "influencerIndex": 0.0,
                "spamIndex": 0.0,
                "accountsFollowedByUser": [],
                "accountsFollowingUser": [],
                "accountsUnFollowingUser": [],
                "accountsUnFollowedByUser": [],
                "accountsBlockingUser": [],
                "accountsSuspendingUser": [],
                "accountsDeactivatingUser": []
            },
            "mentionedProfiles": [
                {
                    "snType": "FACEBOOK",
                    "age": 0,
                    "snId": "1172417539573743",
                    "name": "Traditional Food",
                    "screenName": "Traditional Food",
                    "following": 0,
                    "followers": 0,
                    "favCount": 0,
                    "statusCount": 0,
                    "profileImgUrl": "https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-1/c58.0.200.200a/p200x200/41558903_1172418032907027_3657995209024733184_n.png?_nc_cat=108&_nc_sid=dbb9e7&_nc_ohc=7zMOCSRIaTMAX_GsDLb&_nc_ht=scontent-iad3-1.xx&oh=f58bc4b359d41010a9cf512c54f8c684&oe=5F3473CB",
                    "profileWorkflowProperties": {
                        "tags": [],
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
                    "participationIndex": 0.0,
                    "influencerIndex": 0.0,
                    "spamIndex": 0.0,
                    "accountsFollowedByUser": [],
                    "accountsFollowingUser": [],
                    "accountsUnFollowingUser": [],
                    "accountsUnFollowedByUser": [],
                    "accountsBlockingUser": [],
                    "accountsSuspendingUser": [],
                    "accountsDeactivatingUser": []
                }
            ],
            "isSenderFollower": false,
            "createdTime": 1595925465833,
            "modifiedTime": 1595925468091,
            "snCreatedTime": 1595925459000,
            "snCreatedTimeYearMonth": "2020_07",
            "snModifiedTime": 1595925459000,
            "snStats": {
                "nL": 0
            },
            "mediaList": [],
            "geoTarget": {
                "countries": [
                    "Global"
                ]
            },
            "rawMessage": "How do you like this Traditional Food?",
            "workflowProperties": {
                "sentiment": 0,
                "isSpam": false,
                "isProfane": false,
                "tags": [
                    "secure"
                ],
                "clientQueues": [
                    {
                        "clientQueueQueryField": "1000004509_65",
                        "queueId": 65,
                        "queueAssignedTime": 1595925466235
                    }
                ],
                "partnerQueues": [
                    {
                        "queueId": 11,
                        "queueAssignedTime": 1595925466235
                    }
                ],
                "contentLists": [],
                "partnerCustomProperties": {},
                "processingUserDetailsList": [],
                "read": false
            },
            "language": "en",
            "conversationId": "2091657247780860_2605186629761250",
            "parentSnMsgId": "2091657247780860_2605186629761250",
            "parentSnCreatedTimeYearMonth": "2020_04",
            "parentMsgType": 15,
            "deleted": false,
            "archived": false,
            "brandPost": true,
            "parentBrandPost": true,
            "hasBrandComment": true,
            "hasBrandResponded": false,
            "hasScheduledComment": false,
            "hasParentPost": true,
            "hasApplicationConversation": false,
            "rootUniversalMessageId": "FACEBOOK_15_2091657247780860_2605186629761250",
            "isSharedPost": false,
            "numberOfComments": 0,
            "hasConversation": false,
            "colorCode": "green",
            "colorDescription": "20 days - 30 days range",
            "sFCaseCreationEnabled": true,
            "canCreateSFCase": true,
            "sFTaskCreationEnabled": true,
            "canCreateSFTask": false,
            "accountType": "FBPAGE",
            "isSecure": true,
            "isBrandInitiatedConversation": true,
            "audienceTargets": [
                {
                    "targetOptions": {},
                    "placementType": "PAGE",
                    "operator": "OR"
                }
            ],
            "numOfWorkFlowComments": 1,
            "hasWorkFlowComment": true,
            "hasChildren": false,
            "parentUniversalMessageKey": {
                "universalMessageId": "FACEBOOK_15_2091657247780860_2605186629761250",
                "snType": "FACEBOOK",
                "msgType": 15,
                "snMsgId": "2091657247780860_2605186629761250",
                "sourceId": 1000073624,
                "sourceType": "ACCOUNT",
                "snCreatedTimeYearMonth": "2020_04",
                "snCreatedTime": 1588013222000
            },
            "altPUMK": {
                "universalMessageId": "FACEBOOK_15_2091657247780860_2605186629761250",
                "snType": "FACEBOOK",
                "msgType": 15,
                "snMsgId": "2091657247780860_2605186629761250",
                "sourceId": 1000073624,
                "sourceType": "ACCOUNT",
                "snCreatedTimeYearMonth": "2020_04",
                "snCreatedTime": 1588013222000
            },
            "workflowComments": [
                {
                    "id": "5f1fe3dc3404374e7e4e0d30",
                    "comment": "adsf",
                    "commentingUser": -100,
                    "commentedOnDate": 1595925468075,
                    "commentUpdateDate": 1595925468075,
                    "onAsset": "MESSAGE_WORKFLOW",
                    "assetId": "FACEBOOK_14_2605186629761250_2681463928800186",
                    "partnerId": 9004,
                    "clientId": -1,
                    "isEdited": false,
                    "isEditable": false,
                    "deleted": false,
                    "hasConversation": false
                }
            ],
            "userActions": [],
            "detectedSurveyMessage": false,
            "sourceInfos": []
        }
 ],
    "hasMore": true,
    "prevCount": 0,
    "nextCount": 0
}



[](https://dev.sprinklr.com/message-conversation-read-v1)
