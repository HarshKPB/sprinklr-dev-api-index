---
title: "Post Draft Update v1"
slug: post-draft-update-v1
url: https://dev.sprinklr.com/post-draft-update-v1
---

# Post Draft Update v1

#
PUT Post Draft Create v1

You can update an existing draft post in the UI via this API call. It can either be an original post or a reply.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/publishing/draft/{messageId}

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

### Path Parameters

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| messageId | Required | The id of the drafted post | Integer |

### Request Parameters

****

****

****

****

[MessageType](https://dev.sprinklr.com/message-v1)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| messageType | Required | . Set this to 2 for an update (new post). | Long |
| messageId | Optional | The id of the draft message. | Long |
| accountIds | Required | List of unique Ids for the channel account added in the system. | List <Long> |
| taxonomy | Required | Taxonomy of the message. Taxonomy.campaignId (and therefore taxonomy) must be populated, unless the post asset is used and if the asset.campaignId is not null. Taxonomy description table given below. | Taxonomy Object |
| content | Required | The content of the message. One of the postAssetId and content attributes must be populated.Content description table given below. | Content Object |
| scheduledDate | Optional | Datetime value in milliseconds. It is (UNIX time in UTC)*1000. | Long |
| channelSpecificContentList | Optional | Content for each channel. Unique channels are determined by the provided account Ids. Content can be same or overridden for each channel. For each account provided, content is searched in this list and applied. | Array |
| channelSpecificAudienceTargetList | Optional | Target Audience for each channel. | List[String] |

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
|  | attachment                 "attachment": {             "type": "PHOTO",             "mediaList": [                 {                     "type": "PHOTO",                     "source": " ",                     "previewImageUrl": " "                 }             ]         } | Optional | The attachment object contains the details of attachment.                type: the type of attachment.               source: the image source url               previewImageUrl: the image preview url. | Object |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X PUT \
 'https://api3.sprinklr.com/{env}/api/v1/publishing/draft/78377' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
  -d'{
  "messageType":2,
   "taxonomy":{
      "campaignId":"62_-98",
      "urlShortnerDomain":null,
      "tags":[
      ],
      "socialBarId":null,
      "clientCustomProperties":{
      },
      "partnerCustomProperties":{
         "ExpiresOn":[
            "1391126400000"
         ],
         "Country":[
            "us"
         ],
         "testing_text_ob":[
            "123456",
            "09876",
            "Check"
         ],
         "AvailableFrom":[
            "1385596800000"
         ],
         "CampaignName":[
            "camp1"
         ],
         "name":[
            "a"
         ]
      }
   },
   "approval":{
      "approvalOption":"NONE",
      "comment":""
   },
   "scheduledDate":1397134963000,
   "accountIds":[
      "3036"
   ],
   "accountGroupIds":[
   ],
   "content":{
      "message":"Test Update Draft Post"
   },
   "channelSpecificContentList":[
      {
         "data":{
            "message":"Test Update Draft Post"
         },
         "channelInfo":{
            "channelType":"FACEBOOK"
         }
      }
   ],
   "channelSpecificAudienceTargetList":[
   ],
   "channelSpecificAdditionalProperties":[
      {
         "data":{
            "dirty":[
               true
            ]
         },
         "channelInfo":{
            "channelType":"FACEBOOK"
         }
      }
   ],
   "messageId":3170357,
   "version":0
}'
 

     
     
 

## Example - Response

 
 
     
 
204 No Content
 

     
     
   
 

## Response Parameters



| Parameter | Description | Type |
| --- | --- | --- |
| 204 (No Content) | It indicates that the server has successfully fulfilled the request and there is no content to send in the response payload body. |  |

	[](https://dev.sprinklr.com/post-draft-update-v1) 

 

 
[Back to top](https://dev.sprinklr.com/post-draft-update-v1)
