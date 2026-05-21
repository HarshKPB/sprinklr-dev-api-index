---
title: "Post Publishing v1"
slug: post-publishing-v1
url: https://dev.sprinklr.com/post-publishing-v1
---

# Post Publishing v1

#
POST Post Publishing v1

Using this API, you can schedule a Post across social media and messaging channels.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v1/publishing/post

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



















[MessageType](https://dev.sprinklr.com/message-v1)






















































































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| messageType | Required | . Set this to 2 for original post for all channels. | Enum |
| accountId | Required | AccountId is a unique Id of the social channel account where a post will be published. | Long |
| taxonomy | Required | Taxonomy of the message. & Taxonomy.campaignId (and therefore taxonomy) must be populated, unless the post asset is used and if the asset.campaignId is not null. Taxonomy description table given below. | Taxonomy Object |
| content | Required | The content of the message. One of the postAssetId and content attributes must be populated. Content description table given below. | Content Object |
| scheduledDate | Optional | datetime value in milliseconds. It is (UNIX time in UTC)*1000. | Long |
| approval | Optional | Approval details of the post. | Approval Object |
| audienceTarget | Optional | Map 				List | Map> |
| parentUniversalMessageKey | Optional | UniversalMessageKey: If this post is in reply to a message like comment/reply to a post, then this field is the reference to the parent message | UniversalMessageKey Object |
| inReplyToUniversalMessageKey | Optional | This uniquely identifies the message this post is replying to. 				It’s different from parentUniversalMessageKey. 				E.g., Client choose to reply to a comment on brand post. The parentUniversalMessageKey points to the brandPost and inReplyToUniversalMessageKey points to the comment to reply. | UniversalMessageKey Object |
| originalPostId | Optional | if this message is a republish message, then originalPostId = the post to be republished | String |
| fullResponse | Optional | True for receiving full Post object. False for receiving postId only. Default is false. | Boolean |

### Taxonomy Field Descriptions Table






























































| Parameter | Sub Parameter | Required | Description | Type |
| --- | --- | --- | --- | --- |
| taxonomy |  | Required | The object that contains the taxonomy details. | Object |
|  | campaignId | Required | The id of the campaign which you want to attach with the post or draft. | String |
|  | clientCustomProperties | Optional | The custom properties with respect to draft ot post. | String |
|  | partnerCustomProperties | Optional | The partner properties with respect to draft ot post. | String |
|  | tags | Optional | The tags with respect to draft ot post. | String |
|  | campaignStartDate | Optional | The campaign start date. | Long |
|  | campaignEndDate | Optional | The campaign end date. | Long |

### Content Field Descriptions Table




























``







| Parameter | Sub Parameter | Required | Description | Type |
| --- | --- | --- | --- | --- |
| content |  | Required | The object that contains the content details. | Object |
|  | message | Required | The message you want to post on social. | String |
|  | attachment  				 				"attachment": { 				"type": "PHOTO", 				"mediaList": [ 				{ 				"type": "PHOTO", 				"source": " ", 				"previewImageUrl": " " 				} 				] 				} | Optional | The attachment object contains the details of attachment.  				type: the type of attachment. 				source: the image source url 				previewImageUrl: the image preview url. | Object |

### Example 1: Schedule Post for Image Asset

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v1/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
"messageType":2,
    "accountId": 315665,
    "content": {
        "message": "testing",
        "attachment": {
            "type": "PHOTO",
            "mediaList": [
                {
                    "type": "PHOTO",
                    "source": "https://sprdn-assets.sprinklr.com/738/78f58316-256a-44c4-8ffe-b730c593cfb1-71568467.gif",
                    "imageUrl": "https://sprdn-assets.sprinklr.com/738/78f58316-256a-44c4-8ffe-b730c593cfb1-71568467.gif",
                     "mediaMimeType": "image/gif"
                }
            ]
        }
    },
   "taxonomy":{
      "campaignId":"4_11"
   },
   "approval":{
      "approvalOption":"APPROVAL_PATH",
      "approvalPathId":"58e13874e4b0814cd7553ecc"
   },
   "scheduledDate":1490993400000
}'
 

     
     
   

### Example - Response

 
 
     
 
"postId": 78327876
 

     
     
   
 

### Example 2: Schedule Post for Multiple Images

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v1/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
 "messageType":2,
    "accountId": 315665,
    "content": {
        "message": "testing",
        "attachment": {
            "type": "PHOTO",
            "mediaList": [
                {
                    "type": "PHOTO",
                    "source": "https://sprdn-assets.sprinklr.com/738/78f58316-256a-44c4-8ffe-b730c593cfb1-71568467.gif",
                    "imageUrl": "https://sprdn-assets.sprinklr.com/738/78f58316-256a-44c4-8ffe-b730c593cfb1-71568467.gif",
                     "mediaMimeType": "image/gif"
                },
                {
                    "type": "PHOTO",
                    "source": "https://sprdn-assets.sprinklr.com/738/78f58316-256a-44c4-8ffe-b730c593cfb1-71568467.gif",
                    "imageUrl": "https://sprdn-assets.sprinklr.com/738/78f58316-256a-44c4-8ffe-b730c593cfb1-71568467.gif",
                     "mediaMimeType": "image/gif"
                }
            ]
        }
    },
   "taxonomy":{
      "campaignId":"4_11"
   },
   "approval":{
      "approvalOption":"APPROVAL_PATH",
      "approvalPathId":"58e13874e4b0814cd7553ecc"
   },
   "scheduledDate":1490993400000
}'
 

     
     
   

### Example - Response

 
 
     
 
"postId": 78327987
 

     
     
   
 

### Response Parameters





















| Parameter | Description | Type |
| --- | --- | --- |
| postId | The {Id} is associated with the message you have posted or created via API call or in the UI. | Integer |

	[](https://dev.sprinklr.com/post-publishing-v1) 

 

 
[Back to top](https://dev.sprinklr.com/post-publishing-v1)
