---
title: "Schedule Draft"
slug: schedule-draft
url: https://dev.sprinklr.com/schedule-draft
---

# Schedule Draft

# POST Schedule Draft

Using this API, you can schedule an existing draft message for publishing across channels.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/publishing/draft/schedule

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
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the dev portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  article |
| workspace_id | workspaceId | This field is optional. If your authorization token is associated with multiple workspaces, you'll have to pass workspace_id in the headers for scheduling a draft. You can use  to check the workspace Id your token is primarily associated with. |

## Request Parameters














[documentation](https://dev.sprinklr.com/read-account)

[Bootstrap Resources - Partner Campaigns API](https://dev.sprinklr.com/bootstrap-resources-v1)

[read URl Shortners API](https://dev.sprinklr.com/read-url-shortener)

****

****

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| id |  | Required | Refers to the unique identifier of the draft postThis is the id you receive in the create draft API response | Integer |
| accountIds |  | Required | Refers to the list of account Ids you want to schedule the post fromRefer to this  for steps on how how to extract account Id from the UI |  |
| content |  | Required | Refers to the object containing the post details | Object |
|  | title | Optional | Refers to the title of the post | String |
|  | text | Optional | Refers to the text of the post | String |
|  | attachment | Required | Object containing the post attachment details | Object |
| scheduleDate |  | Required | Refers to the time at which you want to schedule the post for publishing. | Epoch (milliseconds) |
| taxonomy |  | Required | Object containing additional details required for scheduling the post | Object |
|  | campaignId | Required | Refers to the campaign Id under which you want to scheule the post.You can fetch all the campaigns present on the Sprinklr platform using | String |
|  | clientCustomProperties | Optional | Refers to the workspace level custom properties that you want to append to the post | List of custom property name and value pair |
|  | partnerCustomProperties | Optional | Refers to the global (partner) level custom properties that you want to append to the post | List of custom property name and value pair |
|  | tags | Optional | Refers to the tags that you want to append to the post | List [String] |
|  | urlShortenerId | Optional | Refers to the Url shortener Id to associate to the post.You can fetch the existing Url shorteners using | String |
| approval |  | Required | Object containing the approval details for scheduling the draft | Object |
|  | type | Optional | Refers to the type of approval required.Supported Types:ACCOUNT_OWNER, USER, APPROVAL_PATH, NONEDefault: NONE | String |
|  | id | Optional | Refers to the unique identifier for the approval depending on the chosen approval type | String |
| version |  | Optional | Refers to the current version of the post. For example, version 0 would mean the initial version of the draft message.Required when publishing for Instagram and Youtube | Integer |

### Attachment Object Description Table












****

****

[Channels](https://dev.sprinklr.com/channels-v1)

****

****``

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Refers to the type of the attachment.Supported Types:: VIDEO, IMAGE, CAROUSEL, MULTI_MEDIA | String |
| title |  | Optional | Refers to the title of the attachment | String |
| url |  | OptionalRequired when you need to associate an attachment to the post | Refers to the publically accessible url of the attachment | Url |
| previewUrl |  | Optional | Refers to the preview url of the attachment, i.e., the thumbnail of the attachment | Url |
| mediaAttachmentList |  | Optional.Required when scheduling a draft with multiple attachments such as when publishing a carousel post | Array containing attachment details | Array |
|  | url | Required | Refers to the puiblically accessible url for the attachment | Url |
|  | title | Optional | Refers to the attachment's title | String |
|  | type | Required | Refers to the type of the attachment.Example: IMAGE, VIDEO, etc | String |
| clickThroughUrl |  | Required when publishing a Facebook Carousel Post | Refers to the common Url that will act as the redirect URL for all the items in the carousel | Url |
| attachmentOptions |  | Optional | Object containing the channel specfic attachment details | Object |
|  | category | OptionalRequired for YouTube publishing | Refers to the Youtube video publishing category 					Enum: 					 						[ '22': 'People & Blogs', '23': 'Comedy', '24': 'Entertainment', '25': 'News & Politics', '15': 'Pets & Animals',  '26': 'Howto & Style', '27': 'Education', '17': 'Sports', '28': 'Science & Technology' '29': 'Nonprofits & Activism', '19': 'Travel & Events',  '1': 'Film & Animation',  '2': 'Autos & Vehicles',  '20': 'Gaming', '10': 'Music' ] | String |
|  | channelType | Required | Refers to the channel for which you are scheduling the post. Refer to  for more details. | String |
|  | visibility | Optional | Refers to the visibility permisions for the postSupported Values:PUBLIC, PRIVATE | String |
|  | notifySubscribers | Optional | If true, the subscribers will be notified when the post is published | Boolean |
|  | embeddable | Optional | If true, the post will be embeddable | Boolean |
|  | accountId | Optional | If the given attachment options are specfic to an account, account Id can be mentioned | Integer |
| closedCaptions |  | Optional.Required when scheduling a video post with captions | Array containing the details of the captions attachment file | Array |
|  | languageCode | Required | Refers to the language code of the captions file.Example: en for english |  |
|  | title | Optional | Refers to the title of the captions attachment file | String |
|  | url | Required | Refers to the publically accessible url for the captions file | Url |
|  | extension | Required | Refers to the extension format of the captions file | String |

## Example 1: Schedule Draft with Multiple Attachments

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [
        600001490,
        600001719
    ],
    "content": {
        "text": "Testing publishing with twitter channel",
        "attachment": {
            "type": "MULTI_MEDIA",
            "attachments": [
                {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/13977851-c5b6-40c3-83a3-aaa9972c8daf-33859841.mp4",
                    "type": "VIDEO"
                },
                {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/13977851-c5b6-40c3-83a3-aaa9972c8daf-33859841.mp4",
                    "type": "VIDEO"
                },
                {
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/13977851-c5b6-40c3-83a3-aaa9972c8daf-33859841.mp4",
                    "type": "VIDEO"
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "2_402"
    },
    "scheduleDate": 1650371400000,
    "id": 600000009739494,
    "version": 1
}'
 

     
     
   

## Example 2: Schedule a Carousel Post

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
"accountIds": [
        1000069482
    ],
    "content": {
        "text": "Testing schedule draft with multiple attachments",
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
        "campaignId": "1000004785_102763"
    },
    "id": 2091203996,
    "scheduleDate": 1611554041000,
    "version": 0
}'
 

     
     
   

## Example 3: Schedule a Video Post with Captions

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 10978107753,
    "accountIds": [1598083],
    "content": {
        "title": "Testing API2 publishing",
        "text": "Testing API2 publishing",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset",
            "type": "VIDEO",
            "previewUrl": "https://qa4-cdata-app.sprinklr.com/DAM/400002/1a30fb97-e7fa-4a34-9f8f-6af4f0d97fac-1686362046/preview_image_0-fd451247-18b1-.png",
            "closedCaptions": [
                {
                    "languageCode": "en",
                    "title": "AnimatedVideo_Captions.en.srt",
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/747948f1-d93b-4938-bb88-b12a07f74a5f-2843360148.srt",
                    "extension": "srt"
                }
            ]
        }
    },
    "scheduleDate": 1691750660000,
    "taxonomy": {
        "campaignId": "4706_11490"
    },
    "approval": {}
}'
 

     
     
   

	[](https://dev.sprinklr.com/schedule-draft) 

 

 
[Back to top](https://dev.sprinklr.com/schedule-draft)
