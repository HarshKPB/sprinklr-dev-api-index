---
title: "Create Draft"
slug: create-draft
url: https://dev.sprinklr.com/create-draft
---

# Create Draft

#
POST Create Draft

Creating a draft allows creating an outbound message that can be sent at a later date and time. This API call aims to create a draft, which can then be scheduled for publishing using [schedule draft API](https://dev.sprinklr.com/schedule-draft).

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/publishing/draft

### Headers

HTTP headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			```




			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)


``
[ME API](https://dev.sprinklr.com/me-api)



| Key | Value | Description |
| --- | --- | --- |
| accept | application/json | Determines the acceptable response type from the server |
| Content-Type | application/json | Content-Type is representation header determines the type of data (media/resource) present in the request body. |
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the dev portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  article |
| workspace_id | workspaceId | This field is optional. If your authorization token is associated with multiple workspaces, you'll have to pass workspace_id in the headers for creating a draft. You can use  to check the workspace Id your token is primarily associated with. |

### Request Parameters





















































****






			[channel type](https://dev.sprinklr.com/channels-v1)








****














































































****




| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| accountIds |  | Required | List of account ids you wish to schedule the message to | List [Integer] |
| content |  | Optional | Object defining the content details | Object |
|  | title | Optional | The title of the message. | String |
|  | text | Optional | The text of the draft message. | String |
|  | attachment | Optional | Object defining the attachment detailsRefer to the table below for attachment object details | Object |
| channelOptions |  | Optional | Required when you need to pass options specific to a channel typeNote: Channel options are supported for the following channels: FACEBOOK, INSTAGRAM, EMAIL, SINA WEIBO, TWILIO | Array |
|  | channelType | Optional | Refers to the  for which the draft is being created | String |
|  | accountId | Optional | Refers to the specific account ids w.r.t mentioned channel type, where the draft needs to be created | Integer |
|  | darkPost | Optional | Dark posts allow creating content to target different audiences without publishing the content to the page. These posts are created when you create ads or use paid promotionIn simple words, a dark post is never published but only surfaces as an ad.Note: Dark Posts published natively on a channel will not be pulled into Sprinklr unless a comment is made on the post. A comment action on the Dark Post will cause the Dark Post to be imported into the Sprinklr platform. | Boolean |
| scheduleDate |  | Optional | Schedule date for publishing the drafted message | Epoch (time in milliseconds) |
| taxonomy |  | Required | Taxonomy related to the message | Object |
|  | campaignId | Required | Campaign under which you want to create the draft | String |
|  | clientCustomProperties | Optional | Workspace level custom properties | String |
|  | partnerCustomProperties | Optional | Global level custom properties | String |
|  | tags | Optional | Refers to any tags that need to be added to the draft | String |
|  | urlShortenerId | Optional | URL shortener identifier to be added to the draft | String |
| approval |  | Optional | Object defining approval details for reviewing and approving the draft | Object |
|  | type |  | Type of approval to process. defaults to NONE 				 				Enum: [ ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE | String |
|  | id |  | Value related to the chosen approval type | String |
| version |  | Optional | Current version of the message.Default: 0 | Integer |

### Attachment Object Description Table












****

****

****

****``

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Refers to the type of the attachment.Supported Types:: VIDEO, IMAGE, CAROUSEL, MULTI_MEDIA, POLL (LinkedIn) | String |
| title |  | Optional | Refers to the title of the attachment | String |
| url |  | OptionalRequired when you need to associate an attachment to the post | Refers to the publically accessible url of the attachment | Url |
| alternateText |  | Optional | Refers to the alt text for the image attachment | String |
| previewUrl |  | Optional | Refers to the preview url of the attachment, i.e., the thumbnail of the attachment | Url |
| mediaAttachmentList |  | Optional.Required when scheduling a draft with multiple attachments for instance when creating a carousel draft | Array containing attachment details | Array |
|  | url | Required | Refers to the puiblically accessible url for the attachment | Url |
|  | title | Optional | Refers to the attachment's title | String |
|  | type | Required | Refers to the type of the attachment.Example: IMAGE, VIDEO, etc | String |
| clickThroughUrl |  | Required when publishing a Facebook Carousel Post | Refers to the common Url that will act as the redirect URL for all the items in the carousel | Url |
| attachmentOptions |  | Optional | Object containing the channel specfic attachment details | Object |
|  | category | OptionalRequired for YouTube publishing | Refers to the Youtube video publishing category 					Enum: 					 						[ '22': 'People & Blogs', '23': 'Comedy', '24': 'Entertainment', '25': 'News & Politics', '15': 'Pets & Animals',  '26': 'Howto & Style', '27': 'Education', '17': 'Sports', '28': 'Science & Technology' '29': 'Nonprofits & Activism', '19': 'Travel & Events',  '1': 'Film & Animation',  '2': 'Autos & Vehicles',  '20': 'Gaming', '10': 'Music' ] | String |
|  | channelType | Required | Refers to the channel for which you are scheduling the post | String |
|  | visibility | Optional | Refers to the visibility permisions for the postSupported Values:PUBLIC, PRIVATE | String |
|  | notifySubscribers | Optional | If true, the subscribers will be notified when the post is published | Boolean |
|  | embeddable | Optional | If true, the post will be embeddable | Boolean |
|  | accountId | Optional | If the given attachment options are specfic to an account, account Id can be mentioned | Integer |
| closedCaptions |  | Optional.Required when scheduling a video post with captions | Array containing the details of the captions attachment file | Array |
|  | languageCode | Required | Refers to the language code of the captions file.Example: en for english |  |
|  | title | Optional | Refers to the title of the captions attachment file | String |
|  | url | Required | Refers to the publically accessible url for the captions file | Url |
|  | extension | Required | Refers to the extension format of the captions file | String |

## Example 1: Create Draft for Carousel Post

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
 "accountIds": [
        1000068765
    ],
    "content": {
        "text": "Testing publishing",
        "attachment": {
            "type": "CAROUSEL",
            "mediaAttachmentList": [
                {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg",
                    "title": "New",
                    "type": "IMAGE"
                },
                {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg",
                    "title": "New",
                    "type": "IMAGE"
                },
                {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg",
                    "title": "New",
                    "type": "IMAGE"
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "1000005643_101234"
    }
}'
 

     
     
   

## Example - Response

 
 
     
 
{
"data": "MESSAGE_2045128734",
"errors": []
}
 

     
     
   
 

## Example 2: Create Draft Using Location Id (For Instagram Only)

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
"accountIds": [
        600057261
    ],
    "content": {
        "text": "NEW TEST 2",
        "attachment": {
            "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg",
            "type": "IMAGE",
            "alternateText": "Adding alt text"
            "attachmentOptions": [
                {
                    "locationId": 10813158587386200,
                    "channelType": "INSTAGRAM"
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "7_1"
    }
}'
 

     
     
   

## Example - Response

 
 
     
 
{
"data": "MESSAGE_2045129845",
"errors": []
}
 

     
     
   
 

**Dev Notes: **Refer to [lookupByDimension API](https://dev.sprinklr.com/lookup-by-dimension) for fetching the required locationId

## Example 3: Create Video Draft with Captions

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": ["600055050"],
    "content": {
        "title": "Testing API2 draft",
        "text": "Testing API2 draft",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset Test",
            "type": "VIDEO",
            "previewUrl": "https://qa4-cdata-app.sprinklr.com/DAM/400002/1a30fb97-e7fa-4a34-9f8f-6af4f0d97fac-1686362046/preview_image_0-fd451247-18b1-.png",
            "closedCaptions": [
                {
                    "languageCode": "en",
                    "title": "AnimatedVideo_Captions.vtt",
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/320d9f60-7b4d-4ecc-956a-d2000805bd55-1951371300/AnimatedVideo_Captions.vtt",
                    "extension": "vtt"
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "-1_273"
    },
    "approval": {}
}'
 

     
     
   

### Response Parameters
















| Parameter | Description | Type |
| --- | --- | --- |
| data | Contains the Id of draft message. | String |

**Dev Notes: **For searching the created drafts, you can refer to [Search by Entity (OUTBOUND_MESSAGE)](https://dev.sprinklr.com/search-by-entity) API

	[](https://dev.sprinklr.com/create-draft) 

 

 
[Back to top](https://dev.sprinklr.com/create-draft)
