---
title: "Read Post by Post ID v1"
slug: read-post-by-post-id-v1
url: https://dev.sprinklr.com/read-post-by-post-id-v1
---

# Read Post by Post ID v1

#
GET Read Post by Post ID v1

Using this API, you can fetch the outbound post details for the given postIds.

**Dev Notes: ** You can also fetch multiple post by passing comma separated postIds.

Example: postIds=1454030193, 1454030101

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/outbound/posts

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

## Query Parameters

| Query parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| postIds | Required | The id of the Post that you want to fetch. You can also fetch multiple post by passing comma separated postIds. Example: postIds=1454030193,1454030101. | String |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X GET \
 https://api3.sprinklr.com/{env}/api/v1/outbound/posts?postIds=1454030193 \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'
 

     
     
   

## Example - Response

 
 
     
 
[
   [
    {
        "messageId": 2683242132,
        "postId": 1454030193,
        "accountId": 111727,
        "channelType": "FACEBOOK",
        "accountType": "FBPAGE",
        "additional": {
            "dirty": [
                "true"
            ],
            "CAN_EDIT": [
                "true"
            ],
            "SOURCE_ID": [
                "MESSAGE_2683242132"
            ],
            "IS_BRANDED": [
                "false"
            ],
            "RETRY_COUNT": [
                "1"
            ],
            "CLIENT_IP_ADDRESS": [
                "27.34.246.122"
            ],
            "CAN_DELETE": [
                "true"
            ],
            "X_VERSION_ID": [
                "96065298-f3bb-40f2-9ee3-ef44189c1696"
            ],
            "CLIENT_REF": [
                "QUICK_PUBLISHER"
            ],
            "CONTENT_TYPES": [
                "POST"
            ],
            "CONTENT_TEMPLATE_ID": [
                "59687731e4b0de173f6f3eac"
            ],
            "X_LAST_VERSION_ID": [
                "c9f4516a-15a4-4446-a146-175bd7a479f3"
            ],
            "PUBLISH_GIF_AS_VIDEO": [
                "false"
            ],
            "MESSAGE_CREATED_TIME": [
                "1569560854090"
            ],
            "REQUEST_SOURCE": [
                "UI"
            ],
            "RELATED_ENTITIES": [
                "MESSAGE_2683242132"
            ],
            "PUBLISHED_BY": [
                "96287"
            ],
            "ADDITIONAL_SAM_IDS": [
                "5d8d9a2a8dbefe4b0f9e8d92"
            ],
            "LINK_DETAILS_ADDED": [
                "true"
            ],
            "CUSTOMER_JOURNEY_STAGE": [
                "Others"
            ]
        },
        "publishedDate": 1569560882000,
        "publishedTime": 1569560882720,
        "statusID": "1585249011738379_2351054305157842",
        "postStatistics": {
            "channelInsights": {
                "FB_POST_IMPRESSIONS_FAN": 0.0,
                "FB_POST_NEGATIVE_FEEDBACK": 0.0
            }
        },
        "permalink": "https://www.facebook.com/1585249011738379/posts/2351054305157842",
        "processedContent": {
            "message": "http://spr.ly/74354509 checking",
            "attachment": {
                "type": "LINK",
                "mediaList": [
                    {
                        "type": "LINK",
                        "previewImageUrl": "https://www.gsk.com/media/4191/phonconsumer.jpg?center=0.31%2C0.38166666666666665&mode=crop&quality=90&width=600&height=315&rnd=131548058740000000",
                        "title": "Apprentices, students and graduates | GSK",
                        "description": "Student and graduate opportunities with one of the world's leading global healthcare companies.",
                        "source": "http://spr.ly/74354509",
                        "additional": {
                            "thumbnails": [
                                "{\"url\":\"https://www.gsk.com/media/4191/phonconsumer.jpg?center=0.31%2C0.38166666666666665&mode=crop&quality=90&width=600&height=315&rnd=131548058740000000\",\"width\":400,\"height\":300}"
                            ],
                            "providerName": [
                                "www.gsk.com"
                            ],
                            "currIndex": [
                                "0"
                            ],
                            "originalThumbs": [
                                "5"
                            ]
                        }
                    }
                ],
                "title": "Apprentices, students and graduates | GSK",
                "description": "Student and graduate opportunities with one of the world's leading global healthcare companies."
            },
            "languageCode": "en",
            "textEntities": {
                "message": [
                    {
                        "indices": [
                            0,
                            22
                        ],
                        "url": "http://spr.ly/74354509",
                        "copiableEntity": false
                    }
                ]
            },
            "channelCustomProperties": {},
            "hasContentVariants": false,
            "additional": {
                "CONTENT_TEMPLATE_NAME": [
                    "Post"
                ],
                "rawContent": [
                    "https://www.gsk.com/en-gb/careers/apprentices-students-and-graduates/ checking"
                ]
            }
        },
        "autoImported": false,
        "ruleEngineExecuted": true,
        "parentPostId": 2683242140,
        "childPost": false,
        "messageSubType": 0,
        "hasAccountAccess": false,
        "rePublishable": true,
        "reCallable": false,
        "reSchedulable": false,
        "documentType": "POST",
        "fbPostId": "2351054305157842",
        "recommendationScore": 0.0,
        "universalId": "POST_2683242140",
        "authorId": 96287,
        "clientId": 4706,
        "messageType": 2,
        "content": {
            "message": "https://www.gsk.com/en-gb/careers/apprentices-students-and-graduates/ checking",
            "attachment": {
                "type": "LINK",
                "mediaList": [
                    {
                        "type": "LINK",
                        "previewImageUrl": "https://www.gsk.com/media/4191/phonconsumer.jpg?center=0.31%2C0.38166666666666665&mode=crop&quality=90&width=600&height=315&rnd=131548058740000000",
                        "title": "Apprentices, students and graduates | GSK",
                        "description": "Student and graduate opportunities with one of the world's leading global healthcare companies.",
                        "source": "https://www.gsk.com/en-gb/careers/apprentices-students-and-graduates/",
                        "additional": {
                            "thumbnails": [
                                "{\"url\":\"https://www.gsk.com/media/4191/phonconsumer.jpg?center=0.31%2C0.38166666666666665&mode=crop&quality=90&width=600&height=315&rnd=131548058740000000\",\"width\":400,\"height\":300}"
                            ],
                            "providerName": [
                                "www.gsk.com"
                            ],
                            "currIndex": [
                                "0"
                            ],
                            "originalThumbs": [
                                "5"
                            ]
                        },
                        "mediaDetails": {
                            "imageDetails": {
                                "width": 600,
                                "height": 315,
                                "aspectRatio": 1.9047619047619047
                            }
                        }
                    }
                ],
                "title": "Apprentices, students and graduates | GSK",
                "description": "Student and graduate opportunities with one of the world's leading global healthcare companies."
            },
            "linkDetails": [
                {
                    "link": "http://spr.ly/74354509",
                    "queryParams": {},
                    "twitterCardLink": false,
                    "isShortLink": false,
                    "redirectedLink": false,
                    "isFinalLink": false,
                    "domain": "spr.ly",
                    "retried": false
                },
                {
                    "link": "https://www.gsk.com/en-gb/careers/apprentices-students-and-graduates/?details=607&tag=non_updated,ContentNotUpdated,noooo,twitter",
                    "queryParams": {
                        "details": "607",
                        "tag": "non_updated,ContentNotUpdated,noooo,twitter"
                    },
                    "originalLink": "http://spr.ly/74354509",
                    "twitterCardLink": false,
                    "isShortLink": false,
                    "redirectedLink": true,
                    "isFinalLink": true,
                    "domain": "www.gsk.com",
                    "retried": false
                }
            ],
            "languageCode": "en",
            "textEntities": {
                "message": [
                    {
                        "indices": [
                            0,
                            69
                        ],
                        "url": "https://www.gsk.com/en-gb/careers/apprentices-students-and-graduates/",
                        "copiableEntity": false
                    }
                ]
            },
            "hasContentVariants": false,
            "additional": {
                "CONTENT_TEMPLATE_NAME": [
                    "Post"
                ],
                "rawContent": [
                    "https://www.gsk.com/en-gb/careers/apprentices-students-and-graduates/ checking"
                ]
            }
        },
        "taxonomy": {
            "campaignId": "4706_607",
            "clientCustomProperties": {
                "5c0f7c02e4b0d9e0bba2f436": [
                    "India"
                ],
                "58524c4de4b03f06ce0a428d": [
                    "140375"
                ],
                "57d062a8e4b0c8a8083a78df": [
                    "o"
                ],
                "5aaf81d7e4b0aa440986bd63": [
                    "Kakinada"
                ]
            },
            "partnerCustomProperties": {
                "5c8901ece4b004f181e91cf0": [
                    "1569560820000"
                ],
                "5cf8c4e9e4b080d87ad4d7b7": [
                    "Approval Pending"
                ],
                "5d5a7776294c262585c1f89c": [
                    "opt s",
                    "opt a",
                    "opt m"
                ],
                "5a787be9e4b0dc241f89c4c5": [
                    "ok"
                ],
                "5d383940e4b09b5e2561a4da": [
                    "87"
                ]
            },
            "tags": [
                "non_updated",
                "Content Not Updated",
                "noooo",
                "twitter"
            ],
            "urlShortnerDomain": "597ebd17e4b0ea2738d98242",
            "campaignStartDate": 0,
            "campaignEndDate": 0
        },
        "approval": {
            "approvalOption": "NONE"
        },
        "createdDate": 1569560854000,
        "createdTime": 1569560854262,
        "modifiedDate": 1575481634000,
        "modifiedTime": 1575481634066,
        "scheduleDate": 1569560853000,
        "scheduledTime": 1569560853874,
        "status": "SENT",
        "version": 2,
        "deleted": false,
        "category": "UPDATE",
        "postAssetId": "5d8d9a2a8dbefe4b0f9e8d92",
        "hasConversation": false,
        "lockedUntil": 0
    }
]
 

     
     
   
 

	[](https://dev.sprinklr.com/read-post-by-post-id-v1) 

 

 
[Back to top](https://dev.sprinklr.com/read-post-by-post-id-v1)
