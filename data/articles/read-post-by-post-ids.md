---
title: "Read Post by Post Ids"
slug: read-post-by-post-ids
url: https://dev.sprinklr.com/read-post-by-post-ids
---

# Read Post by Post Ids

#
GET Read Post by Post IDs

Using this API, you can fetch the outbound post details for the given postIds.

**Use Cases:**

- Validate the details of a scheduled/sent posts such as content, mentions, created time, status, custom properties, campaign, etc.

- Receive up-to-date details on the sent/scheduled posts

**Dev Notes: ** You can also fetch multiple posts by passing comma separated postIds.

Example: postIds=1454030193, 1454030101

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/publishing/posts

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

## Query Parameters

[publishing post API](https://dev.sprinklr.com/publishing-post)

| Query parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| postIds | Required | Refers to the unique identifier for the created post.You can fetch the post Id from  response | String |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X GET \
 https://api3.sprinklr.com/{env}/api/v2/publishing/posts?postIds=9999997,9999996,9999993' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'
 

     
     
   

## Example - Response

 
 
     
 
	[ {
    "data": [
        {
            "id": 9999993,
            "accountId": 600055472,
            "parentMessageId": 9999990,
            "accountType": "WHATSAPP_BUSINESS",
            "channelType": "WHATSAPP_BUSINESS",
            "enrichments": {
                "flaggedWords": {
                    "allFlaggedWords": [],
                    "imageFlaggedWords": [],
                    "messageFlaggedWords": [],
                    "videoFlaggedWords": []
                }
            },
            "content": {
                "text": "",
                "isRichText": false
            },
            "taxonomy": {
                "campaignId": "66000002_469",
                "clientCustomProperties": {},
                "partnerCustomProperties": {
                    "_c_64dc83bf0cfbc0371edd879b": [
                        "default value"
                    ],
                    "_c_64c38c760e8ea978f3f1270d": [
                        "0"
                    ]
                }
            },
            "status": "SUCCESS",
            "autoResponse": false,
            "createdTime": 1697984884078,
            "modifiedTime": 1697984884078,
            "authorId": -100
        },
        {
            "id": 9999996,
            "accountId": 600055472,
            "parentMessageId": 9999994,
            "accountType": "WHATSAPP_BUSINESS",
            "channelType": "WHATSAPP_BUSINESS",
            "enrichments": {
                "flaggedWords": {
                    "allFlaggedWords": [],
                    "imageFlaggedWords": [],
                    "messageFlaggedWords": [],
                    "videoFlaggedWords": []
                }
            },
            "content": {
                "text": "",
                "isRichText": false
            },
            "taxonomy": {
                "campaignId": "66000002_469",
                "clientCustomProperties": {},
                "partnerCustomProperties": {
                    "_c_64dc83bf0cfbc0371edd879b": [
                        "default value"
                    ],
                    "_c_64c38c760e8ea978f3f1270d": [
                        "0"
                    ]
                }
            },
            "status": "SENT",
            "autoResponse": false,
            "createdTime": 1697984884089,
            "modifiedTime": 1697984884089,
            "authorId": -100
        },
        {
            "id": 9999997,
            "accountId": 600055472,
            "parentMessageId": 9999995,
            "accountType": "WHATSAPP_BUSINESS",
            "channelType": "WHATSAPP_BUSINESS",
            "enrichments": {
                "flaggedWords": {
                    "allFlaggedWords": [],
                    "imageFlaggedWords": [],
                    "messageFlaggedWords": [],
                    "videoFlaggedWords": []
                }
            },
            "content": {
                "text": "",
                "isRichText": false
            },
            "taxonomy": {
                "campaignId": "66000002_469",
                "clientCustomProperties": {},
                "partnerCustomProperties": {
                    "_c_64dc83bf0cfbc0371edd879b": [
                        "default value"
                    ],
                    "_c_64c38c760e8ea978f3f1270d": [
                        "0"
                    ]
                }
            },
            "status": "FAILED",
            "autoResponse": false,
            "createdTime": 1697984884088,
            "modifiedTime": 1697984884088,
            "authorId": -100
        }
    ],
    "errors": []
}
 

     
     
   
 

	[](https://dev.sprinklr.com/read-post-by-post-ids) 

 

 
[Back to top](https://dev.sprinklr.com/read-post-by-post-ids)
