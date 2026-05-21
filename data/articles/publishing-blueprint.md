---
title: "Publishing - Blueprint"
slug: publishing-blueprint
url: https://dev.sprinklr.com/publishing-blueprint
---

# Publishing - Blueprint

# Publishing - Blueprint

This article walks you through the API payloads for creating a draft post, scheduling a draft post, and publishing different types of posts across channels.

## Channels and Capabilities Covered

- [Facebook Video: Create Draft, Schedule Draft, Publish Post](https://dev.sprinklr.com/publishing-blueprint#facebook)

- [LinkedIn Video: Create Draft, Schedule Draft, Publish Post](https://dev.sprinklr.com/publishing-blueprint#linkedin)

- [Twitter Video: Create Draft, Schedule Draft, Publish Post](https://dev.sprinklr.com/publishing-blueprint#twitter)

- [YouTube Video: Create Draft, Schedule Draft, Publish Post](https://dev.sprinklr.com/publishing-blueprint#youtube)

- [Instagram Video: Create Draft, Schedule Draft, Publish Post](https://dev.sprinklr.com/publishing-blueprint#insta)

- [Facebook Carousel: Create Draft, Schedule Draft, Publish Post](https://dev.sprinklr.com/publishing-blueprint#fbcarousel)

- [LinkedIn Poll: Create Draft, Schedule Draft, Publish Post](https://dev.sprinklr.com/publishing-blueprint#linkedinpoll)

- [Facebook Album: Create Draft, Schedule Draft, Publish Post](https://dev.sprinklr.com/publishing-blueprint#fbalbum)

- [Instagram Story: Create Draft, Schedule Draft, Publish Post](https://dev.sprinklr.com/publishing-blueprint#instastory)

- [Twitter Thread: Create Draft, Schedule Draft, Publish Post](https://dev.sprinklr.com/publishing-blueprint#twitterthread)

## Headers

HTTP headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources. Please note that the headers will be consistent across APIs.











			``




			```




			``





			``




``



| Key | Value | Description |
| --- | --- | --- |
| accept | application/json | Determines the acceptable response type from the server |
| Content-Type | application/json | Content-Type is representation header determines the type of data (media/resource) present in the request body. |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to Authorize section on the dev portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to Getting Started article |
| workspace_id | workspaceId | This field is optional. If your authorization token is associated with multiple workspaces, you'll have to pass workspace_id in the headers for creating a draft. You can use ME API to check the workspace Id your token is primarily associated with. |

## Common Request Parameters























































****















****






































































| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| accountIds |  | Required | List of social channel account ids you want to draft, schedule, or publish post forYou can use Bootstrap API to fetch all the existing social accounts in the partner/global environment | List [String] |
| id |  | Required when scheduling a draft, i.e., when using Schedule Draft API | Refers to the message Id received in the response of create Draft API | String |
| version |  | OptionalRequired when scheduling draft for Instagram and Youtube channels | Refers to the current version of the post. For example, version 0 would mean the initial version of the draft message | Integer |
| content |  | Required | Object defining the content details | Object |
|  | title | Optional | The title of the post | String |
|  | text | Optional | The text of the post | String |
|  | attachment | Optional | Object defining the attachment detailsRefer to the respective sections for attachment object details | Object |
| channelOptions |  | Optional | Required when you need to pass options specific to a channel typeNote: Channel options are supported for the following channels: FACEBOOK, INSTAGRAM | Array |
|  | channelType | Optional | Refers to the channel type for which the post is being created | String |
|  | accountId | Optional | Refers to the specific account ids w.r.t mentioned channel type, where the post needs to be created | Integer |
|  | darkPost | Optional | Dark posts allow creating content to target different audiences without publishing the content to the page. These posts are created when you create ads or use paid promotionSimply put, a dark post is never published but only surfaces as an ad.Note: Dark Posts published natively on a channel will not be pulled into Sprinklr unless a comment is made on the post. A comment action on the Dark Post will cause the Dark Post to be imported into the Sprinklr platform. | Boolean |
| scheduleDate |  | Optional | Schedule date for publishing the post | Epoch (time in milliseconds) |
| taxonomy |  | Required | Refers to the object containing additional details to be associated with the post such as campaign, tags, custom properties, etc. | Object |
|  | campaignId | Required | Campaign under which you want to publish the postYou can use Bootstrap API to fetch all existing partner level campaign Ids present on the Sprinklr platform | String |
|  | partnerCustomProperties | Optional | Refers to the global level custom properties | Object |
|  | tags | Optional | Refers to any tags that you want to associate with the post | List [String] |
|  | urlShortenerId | Optional | Refers to the Url shortener identifier for the postYou can use Read All URL Shorteners API to fetch the existing URL shorteners and the associated Ids on the Sprinklr platform | String |
| approval |  | Optional | Refers to the object containing the approval details required to publish the post | Object |
|  | type | Optional | Type of approval you want to queue the post to before it gets published. Defaults to NONE 				 				Enum: [ ACCOUNT_OWNER, APPROVAL_PATH, NONE | String |
|  | id | OptionalRequired when the approval type is "APPROVAL_PATH" | Refers to the unique identifier associated with the approval type | String |

## 1. Facebook Video: Create Draft, Schedule Draft, Publish Post

This section will cover APIs for creating a draft, scheduling an existing draft, and publishing video post with captions for Facebook channel.

### Attachment Object Parameters













****``

****

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| url |  | Required | Refers to the url of the video | String |
| title |  | Optional | Refers to the title of the video attachment | String |
| type |  | Required | Refers to the type of the attachment, i.e., VIDEO in this case | String |
| previewUrl |  | Optional | Refers to the preview url for the attachment, i.e, thumbnail for the video | String |
| closedCaptions |  | Required | Refers to the array defining the captions' details for the draft/post | Array |
|  | languageCode | Required | Refers to the language code for the captions file.Example:  en  for English | String |
|  | title | Optional | Refers to the title for the captions' attachment fileThe suffix of the title field value should contain the combination of language, country, and file caption extension format.Example: en_US.srt | String |
|  | url | Required | Refers to the URL containing the captions file | String |
|  | extension | Required | Refers to the extension format of the captions file | String |

### 1.1 Create Draft


Using this API, you can create a draft post for publishing video with captions for Facebook.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft

**Dev Notes: **The suffix of the title field value should contain the combination of language, country, and file caption extension format. Example: en_US.srt

#### Sample API Request: Create Draft for Facebook




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [
        314040
    ],
    "content": {
        "title": "Testing Facebook API3 publishing",
        "text": "Testing Facebook API3 publishing",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID",
            "type": "VIDEO",
            "previewUrl": "https://qa4-cdata-app.sprinklr.com/DAM/400002/1a30fb97-e7fa-4a34-9f8f-6af4f0d97fac-1686362046/preview_image_0-fd451247-18b1-.png",
            "closedCaptions": [
                {
                    "languageCode": "en",
                    "title": "AnimatedVideo_Captions.en_US.srt",
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/747948f1-d93b-4938-bb88-b12a07f74a5f-2843360148.srt",
                    "extension": "srt"
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "4706_11490"
    },
    "approval": {}
}'





#### Example - Response




  Copy Code



{
"data": "MESSAGE_2045129888",
"errors": []
}





### 1.2 Schedule Draft


Using this API, you can schedule an existing draft for publishing video with captions for Facebook.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule

**Dev Notes: **The suffix of the title field value should contain the combination of language, country, and file caption extension format. Example: en_US.srt

#### Sample API Request: Schedule Draft for Facebook




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 10970992771,
    "accountIds": [314040],
    "content": {
        "title": "Testing API3 publishing",
        "text": "Testing API3 publishing",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID",
            "type": "VIDEO",
            "previewUrl": "https://qa4-cdata-app.sprinklr.com/DAM/400002/1a30fb97-e7fa-4a34-9f8f-6af4f0d97fac-1686362046/preview_image_0-fd451247-18b1-.png",
            "closedCaptions": [
                {
                    "languageCode": "en",
                    "title": "AnimatedVideo_Captions.en_US.srt",
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/747948f1-d93b-4938-bb88-b12a07f74a5f-2843360148.srt",
                    "extension": "srt"
                }
            ]
        }
    },
    "scheduleDate": 1691451013000,
    "taxonomy": {
        "campaignId": "4706_11490"
    },
    "approval": {}
}'





#### Example - Response




  Copy Code



{
"data": "POST_2045129097",
"errors": []
}





### 1.3 Publish Post


Using this API, you can publish video with captions for Facebook.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/post

**Dev Notes: **The suffix of the title field value should contain the combination of language, country, and file caption extension format. Example: en_US.srt

#### Sample API Request: Publish Post for Facebook




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [314040],
    "content": {
        "title": "Testing API3 publishing",
        "text": "Testing API3 publishing",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID",
            "type": "VIDEO",
            "previewUrl": "https://qa4-cdata-app.sprinklr.com/DAM/400002/1a30fb97-e7fa-4a34-9f8f-6af4f0d97fac-1686362046/preview_image_0-fd451247-18b1-.png",
            "closedCaptions": [
                {
                    "languageCode": "en",
                    "title": "AnimatedVideo_Captions.en_US.srt",
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/747948f1-d93b-4938-bb88-b12a07f74a5f-2843360148.srt",
                    "extension": "srt"
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "4706_11490"
    },
    "approval": {}
}'





#### Example - Response




  Copy Code



{
"data": "POST_2045129876",
"errors": []
}





## 2. LinkedIn Video: Create Draft, Schedule Draft, Publish Post

This section covers creating a draft, scheduling a draft, and publishing a video post with captions for LinkedIn channel

### Attachment Object Parameters













****``

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| url |  | Required | Refers to the url of the video | String |
| title |  | Optional | Refers to the title of the video attachment | String |
| type |  | Required | Refers to the type of the attachment, i.e., VIDEO in this case | String |
| previewUrl |  | Optional | Refers to the preview url for the attachment, i.e, thumbnail for the video | String |
| closedCaptions |  | Required | Refers to the array defining the captions' details for the draft/post | Array |
|  | languageCode | Required | Refers to the language code for the captions file.Example: en  for English | String |
|  | title | Optional | Refers to the title for the captions' attachment file | String |
|  | url | Required | Refers to the URL containing the captions file | String |
|  | extension | Required | Refers to the extension format of the captions file | String |

### 2.1 Create Draft

Using this API, you can create a draft post for publishing video with captions for LinkedIn channel.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft

#### Sample API Request: Create Draft for LinkedIn




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
        "title": "Testing API3 publishing LinkedIn",
        "text": "Testing API3 publishing LinkedIn",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID and correct Folder Path 8th Jun 2023",
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





#### Example - Response




  Copy Code



{
"data": "MESSAGE_2045129001",
"errors": []
}





### 2.2 Schedule Draft

Using this API, you can schedule an existing draft for publishing video with captions for LinkedIn.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft

#### Sample API Request: Create Draft for LinkedIn




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token{' \
  -H 'Key: {Enter your API KEY{' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": ["600055050"],
    "content": {
        "title": "Testing API3 publishing LinkedIn",
        "text": "Testing API3 publishing LinkedIn",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID and correct Folder Path 8th Jun 2023",
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





#### Example - Response




  Copy Code



{
"data": "MESSAGE_2045129001",
"errors": []
}





### 2.2 Schedule Draft

Using this API, you can schedule an existing draft for publishing video with captions for LinkedIn.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule

#### Sample API Request: Schedule Draft for LinkedIn




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY{' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 600000037228245,
    "accountIds": [
        "600055050"
    ],
    "content": {
        "title": "Testing API3 publishing LinkedIn",
        "text": "Testing API3 publishing LinkedIn",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID and correct Folder Path 8th Jun 2023",
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
    "scheduleDate": 1691398813000,
    "taxonomy": {
        "campaignId": "-1_273"
    },
    "approval": {}
}'





#### Example - Response




  Copy Code



{
"data": "POST_2045129002",
"errors": []
}





### 2.3 Publish Post


Using this API, you can publish video with captions for LinkedIn.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/post

#### Sample API Request: Publish Post for LinkedIn




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY{' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": ["600055050"],
    "content": {
        "title": "Testing API3 publishing LinkedIn",
        "text": "Testing API3 publishing LinkedIn",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID and correct Folder Path 8th Jun 2023",
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





## Example - Response




  Copy Code



{
"data": "POST_2045129003",
"errors": []
}





## 3. Twitter Video: Create Draft, Schedule Draft, Publish Post

This section covers creating a draft, scheduling a draft, and publishing a video post with captions for Twitter channel

### Attachment Object Parameters













****``

****``

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| url |  | Required | Refers to the url of the video | String |
| title |  | Optional | Refers to the title of the video attachment | String |
| type |  | Required | Refers to the type of the attachment, i.e., VIDEO in this case | String |
| previewUrl |  | Optional | Refers to the preview url for the attachment, i.e, thumbnail for the video | String |
| closedCaptions |  | Required | Refers to the array defining the captions' details for the draft/post | Array |
|  | languageCode | Required | Refers to the language code for the captions file.Example:enfor English | String |
|  | title | Optional | Refers to the title for the captions' attachment file | String |
|  | url | Required | Refers to the URL containing the captions file | String |
|  | extension | Required | Refers to the extension format of the captions fileNote: Twitter only supports srt caption files | String |

### 3.1 Create Draft


Using this API, you can create a draft post for publishing video with captions for Twitter.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft

#### Sample API Request: Create Draft for Twitter




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token} \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [1598083],
    "content": {
        "title": "Testing API3 publishing",
        "text": "Testing API3 publishing",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID",
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
    "taxonomy": {
        "campaignId": "4706_11490"
    },
    "approval": {}
}'





#### Example - Response




  Copy Code



{
"data": "MESSAGE_2045129005",
"errors": []
}





### 3.2 Schedule Draft

Using this API, you can schedule an existing draft for publishing video with captions for Twitter.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule

#### Sample API Request: Schedule Draft for LinkedIn




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 10989418657,
    "accountIds": [1598083],
    "content": {
        "title": "Testing API3 publishing",
        "text": "Testing API3 publishing",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID",
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





#### Example - Response




  Copy Code



{
"data": "POST_2045129006",
"errors": []
}





### 3.3 Publish Post

Using this API, you can publish video with captions for Twitter.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/post

#### Sample API Request: Publish Post for Twitter




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [1598083],
    "content": {
        "title": "Testing API3 publishing",
        "text": "Testing API3 publishing",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID",
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
    "taxonomy": {
        "campaignId": "4706_11490"
    },
    "approval": {}
}'









  Copy Code



{
"data": "POST_2045129007",
"errors": []
}





## 4. YouTube Video: Create Draft, Schedule Draft, Publish Post

This section covers creating a draft, scheduling a draft, and publishing a video post with captions for YouTube channel

### Attachment Object Parameters













****

****

- ****[YouTube's Creative Common help article](https://support.google.com/youtube/answer/2797468?hl=en)
- ****[Youtube's terms of services](https://www.youtube.com/static?template=terms)

****``

****``

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| url |  | Required | Refers to the url of the video | String |
| type |  | Required | Refers to the type of the attachment, i.e., VIDEO in this case | String |
| previewUrl |  | Optional | Refers to the preview url for the attachment, i.e, thumbnail for the video | String |
| attachmentOptions |  | Optional | Object containing the channel specific attachment details | Object |
|  | category | Required | Refers to the Youtube video publishing category 					Enum: 					 						[ '22': 'People & Blogs', '23': 'Comedy', '24': 'Entertainment', '25': 'News & Politics', '15': 'Pets & Animals',  '26': 'Howto & Style', '27': 'Education', '17': 'Sports', '28': 'Science & Technology' '29': 'Nonprofits & Activism', '19': 'Travel & Events',  '1': 'Film & Animation',  '2': 'Autos & Vehicles',  '20': 'Gaming', '10': 'Music' ] | String |
|  | channelType | Required | Refers to the channel for which you are scheduling the post."YOUTUBE" in this case | String |
|  | visibility | Optional | Refers to the visibility permissions for the draft/postSupported Values: PUBLIC, PRIVATE | String |
|  | notifySubscribers | Optional | If true, the subscribers will be notified when the post is published | Boolean |
|  | embeddable | Optional | If true, the video will be embeddable | Boolean |
|  | license | Optional | Refers to the Youtube license under which the video will be publishedSupported Values:CREATIVE_COMMON: The creators' work is protected by a copyright and other creators can reuse the video subject to the terms mentioned in the license. You can refer to  for more detailsYOUTUBE: This is the standard YouTube license that allows creators to share videos. You can refer to  for more details | String |
|  | playlistInfo | Optional | Refers to the object containing the playlist details under which the video will be publishedRefer to the table below for playlistInfo parameters' description | Object |
| closedCaptions |  | Required | Refers to the array defining the captions' details for the draft/post | Array |
|  | languageCode | Required | Refers to the language code for the captions file.Example:enfor English | String |
|  | title | Optional | Refers to the title for the captions' attachment file | String |
|  | url | Required | Refers to the URL containing the captions file | String |
|  | extension | Required | Refers to the extension format of the captions fileNote: Twitter only supports srt caption files | String |

## playlistInfo Object Description Table












| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| playlistId | OptionalRequired when adding the video to an existing playlist | Refers to the unique identifier for the playlist. You can pass existing playlist Id to append the video to existing playlist | String |
| playlistName | OptionalRequired when creating a new playlist | Refers to the name for the playlistYou can ignore passing this parameter if you are passing the playlistId for existing playlist | String |

### 4.1 Create Draft


Using this API, you can create a draft post for publishing video with captions for YouTube.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft

#### Sample API Request: Create Draft for YouTube




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [
        "600046991"
    ],
    "content": {
        "title": "Testing API3 publishing YT verification 01",
        "text": "Test publishing YT 01",
        "attachment": {
            "type": "VIDEO",
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/fc331aaf-906d-4e6f-9bd7-765143238959-1188660913/Video_3.mp4",
            "attachmentOptions": {
                "category": "26",
                "channelType": "YOUTUBE",
                "visibility": "PUBLIC",
                "notifySubscribers": false,
                "embeddable": true
            },
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
        "campaignId": "2_13756"
    }
}'





#### Example - Response




  Copy Code



{
"data": "MESSAGE_2045129011",
"errors": []
}





### 4.2 Schedule Draft

Using this API, you can schedule an existing draft for publishing video with captions for YouTube.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule

#### Sample API Request: Schedule Draft for YouTube




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 600000037228277,
    "accountIds": [
        "600046991"
    ],
    "content": {
        "title": "Testing API3 publishing YT verification 01",
        "text": "Test publishing YT 01",
        "attachment": {
            "type": "VIDEO",
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/fc331aaf-906d-4e6f-9bd7-765143238959-1188660913/Video_3.mp4",
            "attachmentOptions": {
                "category": "26",
                "channelType": "YOUTUBE",
                "visibility": "PUBLIC",
                "notifySubscribers": false,
                "embeddable": true
            },
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
    "version": 1,
    "scheduleDate": 1691402413000,
    "taxonomy": {
        "campaignId": "2_13756"
    }
}'





#### Example - Response




  Copy Code



{
"data": "POST_20451290012",
"errors": []
}





### 4.3 Publish Post


Using this API, you can publish video with captions for YouTube.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/post

#### Sample API Request: Publish Post for YouTube




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [
        "600046991"
    ],
    "content": {
        "title": "Testing API3 publishing YT verification 01",
        "text": "Test publishing YT 01",
        "attachment": {
            "type": "VIDEO",
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/fc331aaf-906d-4e6f-9bd7-765143238959-1188660913/Video_3.mp4",
            "attachmentOptions": {
                "category": "26",
                "channelType": "YOUTUBE",
                "visibility": "PUBLIC",
                "notifySubscribers": false,
                "embeddable": true
            },
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
        "campaignId": "2_13756"
    },
    "id":"10555528948",
    "scheduleDate": 1690711153000,
    "version": 0
}'





#### Example - Response




  Copy Code



{
"data": "POST_2045129009",
"errors": []
}





## 5. Instagram Video: Create Draft, Schedule Draft, Publish Post

This section covers APIs for creating a draft, scheduling a draft, and publishing video (reel) for Instagram channel. Please note that the API **doesn't support creating a video posts with captions**.

**Dev Notes: **

- Kindly note that publishing Instagram video (reels) can be achieved only if you have Instagram business account.
- All single feed videos published on Instagram will be shared as reels as per [Meta's update](https://developers.facebook.com/docs/instagram-api/guides/content-publishing/).

### Attachment Object Parameters













| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| url |  | Required | Refers to the url of the video | String |
| title |  | Optional | Refers to the title of the video attachment | String |
| type |  | Required | Refers to the type of the attachment, i.e., VIDEO in this case | String |
| previewUrl |  | Optional | Refers to the preview url for the attachment, i.e, thumbnail for the video | String |

### 5.1 Create Draft

Using this API, you can create a draft post for publishing video (reel) for Instagram channel.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft

#### Sample API Request: Create Draft for Instagram




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [1557236],
    "content": {
        "title": "Testing API3 publishing",
        "text": "Testing API3 publishing",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID",
            "type": "VIDEO",
            "previewUrl": "https://qa4-cdata-app.sprinklr.com/DAM/400002/1a30fb97-e7fa-4a34-9f8f-6af4f0d97fac-1686362046/preview_image_0-fd451247-18b1-.png"
        }
    },
    "taxonomy": {
        "campaignId": "4706_11490"
    },
    "approval": {}
}'





#### Example - Response




  Copy Code



{
"data": "MESSAGE_2045129015",
"errors": []
}





### 5.2 Schedule Draft

Using this API, you can schedule an existing draft for publishing video (reel) on Instagram account.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule

#### Sample API Request: Schedule Draft for Instagram




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 10991401559,
    "accountIds": [1557236],
    "content": {
        "title": "Testing API3 publishing",
        "text": "Testing API3 publishing",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID",
            "type": "VIDEO",
            "previewUrl": "https://qa4-cdata-app.sprinklr.com/DAM/400002/1a30fb97-e7fa-4a34-9f8f-6af4f0d97fac-1686362046/preview_image_0-fd451247-18b1-.png"
        }
    },
    "version": 1,
    "scheduleDate": 1691750660000,
    "taxonomy": {
        "campaignId": "4706_11490"
    },
    "approval": {}
}'





#### Example - Response




  Copy Code



{
"data": "POST_20451290019",
"errors": []
}





### 5.3 Publish Post


Using this API, you can publish video (reel) on Instagram account.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/post

#### Sample API Request: Publish Post for Instagram




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [1557236],
    "content": {
        "title": "Testing API3 publishing",
        "text": "Testing API3 publishing",
        "attachment": {
            "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
            "title": "Video Asset for incorrect Folder ID",
            "type": "VIDEO",
            "previewUrl": "https://qa4-cdata-app.sprinklr.com/DAM/400002/1a30fb97-e7fa-4a34-9f8f-6af4f0d97fac-1686362046/preview_image_0-fd451247-18b1-.png"
        }
    },
    "taxonomy": {
        "campaignId": "4706_11490"
    },
    "approval": {}
}'






#### Example - Response




  Copy Code



{
"data": "POST_2045129134",
"errors": []
}





## 6. Facebook Carousel: Create Draft, Schedule Draft, Publish Post

This section covers APIs for creating a draft, scheduling a draft, and publishing carousel for Facebook channel.

**Dev Notes: **An end card will be appended to the carousel post by default. This end card will have the image of the Facebook display picture and will redirect to the URL configured in the clickThroughUrl field.

## Attachment Object Parameters












****

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Refers to the type of the attachment, i.e., CAROUSEL in this case | String |
| mediaAttachmentList |  | Required | Array containing attachment details | Array |
|  | url | Required | Refers to the url of the attachment | String |
|  | title | Optional | Refers to the title of the carousel's item | String |
|  | type | Required | Refers to the type of the attachmentSupported Values: IMAGE, VIDEO | String |
| clickThroughUrl |  | Required | Refers to the common Url that will act as the redirect URL for all the items in the carousel | String |

### 6.1 Create Draft


Using this API, you can create a draft for publishing Carousel post for Facebook channel.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft

#### Sample API Request: Create Facebook Carousel Draft




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [
        1000073624
    ],
    "approval": {},
    "content": {
        "title": "Sprinklr Social Media Post Title",
        "text": "Sprinklr social media post content",
        "attachment": {
            "type": "CAROUSEL",
            "mediaAttachmentList": [
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/fe0a8af4-ad82-445b-94a8-bde6c9fe350d-870645516/Ferrari_p.jpg",
                    "type": "IMAGE",
                    "title": "Image description"
                },
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/fe0a8af4-ad82-445b-94a8-bde6c9fe350d-870645516/Ferrari_p.jpg",
                    "type": "IMAGE",
                    "title": "Image description"
                }
            ],
            "clickThroughUrl": "https://www.google.com"
        }
    },
    "taxonomy": {
        "campaignId": "1000004509_131997"
    }
}'





#### Example - Response




  Copy Code



{
"data": "MESSAGE_2045129876",
"errors": []
}





### 6.2 Schedule Draft


Using this API, you can schedule a Facebook carousel post.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule

#### Sample API Request: Schedule Facebook Carousel Post




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [
        1000073624
    ],
    "id": 2151937570,
    "version": "2",
    "approval": {},
    "content": {
        "title": "Sprinklr Social Media Post Title",
        "text": "Sprinklr social media post content",
        "attachment": {
            "type": "CAROUSEL",
            "mediaAttachmentList": [
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/fe0a8af4-ad82-445b-94a8-bde6c9fe350d-870645516/Ferrari_p.jpg",
                    "type": "IMAGE",
                    "title": "Image description"
                },
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/fe0a8af4-ad82-445b-94a8-bde6c9fe350d-870645516/Ferrari_p.jpg",
                    "type": "IMAGE",
                    "title": "Image description"
                }
            ],
            "clickThroughUrl": "https://www.google.com"
        }
    },
    "scheduleDate": "1693555650000",
    "taxonomy": {
        "campaignId": "1000004509_131997"
    }
}'





#### Example - Response




  Copy Code



{
"data": "POST_204512900210",
"errors": []
}





### 6.3 Publish Post


Using this API, you can publish carousel post on Facebook.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/post

#### Sample API Request: Publish Facebook Carousel Post




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [
        1000073624
    ],
    "approval": {},
    "content": {
        "title": "Sprinklr Social Media Post Title",
        "text": "Sprinklr social media post content",
        "attachment": {
            "type": "CAROUSEL",
            "mediaAttachmentList": [
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/fe0a8af4-ad82-445b-94a8-bde6c9fe350d-870645516/Ferrari_p.jpg",
                    "type": "IMAGE",
                    "title": "Image description"
                },
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/fe0a8af4-ad82-445b-94a8-bde6c9fe350d-870645516/Ferrari_p.jpg",
                    "type": "IMAGE",
                    "title": "Image description"
                }
            ],
            "clickThroughUrl": "https://www.google.com"
        }
    },
    "taxonomy": {
        "campaignId": "1000004509_131997"
    }
}'





#### Example - Response




  Copy Code



{
"data": "POST_2045129861",
"errors": []
}





## 7. LinkedIn Poll: Create Draft, Schedule Draft, Publish Post

This section will cover APIs for creating a draft, scheduling an existing draft, and publishing LinkedIn Poll.

### Attachment Parameters

****

****

| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Refers to the type of the attachmentType will be "POLL" in this case | String |
| visibility |  | Optional | Defines the visibility of the post, i.e., whether this will be visible globally or only to the LinkedIn connections.Supported values:CONNECTIONS_ONLY, ANYONE | String |
| postDetails |  | Required | Refers to the object containing the poll details | Object |
|  | pollQuestion | Required | Refers to the question of the poll | String |
|  | duration | Optional | Defines the duration of the pollSupported Values: FOURTEEN_DAYS, ONE_DAY, THREE_DAYS, SEVEN_DAYS | String |
|  | pollOptions | Required | Array defining the poll questions.Refer to the table below for pollOptions array fields | Array |

### 7.1 Create Draft


Using this API, you can create a draft post for publishing Poll on Linkedin.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft

#### Sample API Request: Create Draft for LinkedIn




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": 1740171,
    "content": {
        "text": "test message",
        "attachment": {
            "type": "POLL",
            "visibility": "ANYONE",
            "pollsDetails": {
                "pollQuestion": "What is Your Favorite Food?",
                "duration": "FOURTEEN_DAYS",
                "pollOptions": [
                    {
                        "text": "Chinese"
                    },
                    {
                        "text": "Italian"
                    },
                    {
                        "text": "Mexican"
                    }
                ]
            }
        }
    },
    "taxonomy": {
        "campaignId": "4706_11490"
    }
}'





### Example - Response




  Copy Code



{
"data": "MESSAGE_20451298999",
"errors": []
}





### 7.2 Schedule Draft


Using this API, you can schedule an existing draft for publishing LinkedIn Poll.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule

#### Sample API Request: Schedule Draft for LinkedIn




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": 600058041,
    "id":9650461,
    "version": 2,
    "content": {
        "text": "test message",
        "attachment": {
            "type": "POLL",
            "visibility": "ANYONE",
            "pollsDetails": {
                "pollQuestion": "What is Your Favorite Food?",
                "duration": "FOURTEEN_DAYS",
                "pollOptions": [
                    {
                        "text": "Chinese"
                    },
                    {
                        "text": "Italian"
                    },
                    {
                        "text": "Mexican"
                    }
                ]
            }
        }
    },
    "taxonomy": {
        "campaignId": "66000002_14"
    },
    "scheduleDate": 1697611061000
}'






#### Example - Response




  Copy Code



{
"data": "POST_2045129087",
"errors": []
}





### 7.3 Publish Post


Using this API, you can publish LinkedIn Poll.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/post

**Dev Notes: **The suffix of the title field value should contain the combination of language, country, and file caption extension format. Example: en_US.srt

#### Sample API Request: Publish Post for LinkedIn




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": 1740171,
    "content": {
        "text": "test message",
        "attachment": {
            "type": "POLL",
            "visibility": "ANYONE",
            "pollsDetails": {
                "pollQuestion": "What is Your Favorite Food?",
                "duration": "FOURTEEN_DAYS",
                "pollOptions": [
                    {
                        "text": "Chinese"
                    },
                    {
                        "text": "Italian"
                    },
                    {
                        "text": "Mexican"
                    }
                ]
            }
        }
    },
    "taxonomy": {
        "campaignId": "4706_11490"
    }
}'





#### Example - Response




  Copy Code



{
"data": "POST_2045129777",
"errors": []
}





## 8. Facebook Album: Create Draft, Schedule Draft, Publish Post

This section will cover APIs for creating a draft, scheduling an existing draft, and publishing Facebook Album.

### Attachment Parameters

****

| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| attachments |  | Required | Refers to the array containing the Facebook album's content | Array |
|  | url | Required | Refers to the url for the image you want to add to the album | String |
|  | title | Optional | Refers to the title for the image attachment | String |
|  | previewUrl | Optional | Refers to the preview Url for the image attachment |  |
|  | type | Required | Refers to the type of attachment, i.e., IMAGE in this case | String |
|  | description | Optional | Refers to the description of the image | String |
| title |  | Optional | Refers to the title of the album | String |
| type |  | Required | Refers to the type of the post, i.e., ALBUM in this case | String |
| existingAlbumId |  | Required | Refers to the unique identifier for the existing albumNote: You can only create draft/publish pictures to existing Facebook Album | String |

### 8.1 Create Draft

Using this API, you can create a draft post for publishing pictures to existing Facebook album.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft

#### Sample API Request: Create Draft for Facebook




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": 66000038,
    "content": {
        "title": "title 2",
        "text": "text 2",
        "attachment": {
            "attachments": [
                {
                    "url": "https://pz.cdata.prod0.sprinklr.com/DAM/9004/0513f60f-88bf-482e-b081-5c12de3511cb-1763777752/https___pbs.twimg.com_media_F6.jpg",
                    "previewUrl": "https://pz.cdata.prod0.sprinklr.com/DAM/9004/0513f60f-88bf-482e-b081-5c12de3511cb-1763777752/https___pbs.twimg.com_media_F6.jpg",
                    "type": "IMAGE",
                    "description": "desc"
                },
                {
                    "url": "https://pz.cdata.prod0.sprinklr.com/DAM/9004/0513f60f-88bf-482e-b081-5c12de3511cb-1763777752/https___pbs.twimg.com_media_F6.jpg",
                    "previewUrl": "https://pz.cdata.prod0.sprinklr.com/DAM/9004/0513f60f-88bf-482e-b081-5c12de3511cb-1763777752/https___pbs.twimg.com_media_F6.jpg",
                    "type": "IMAGE",
                    "description": "desc1"
                }
            ],
            "title": "Test_Album_Title",
            "existingAlbumId": "120309614415221",
            "type": "ALBUM"
        }
    },
    "taxonomy": {
        "campaignId": "66000002_14"
    }
}'





## Example - Response




  Copy Code



{
"data": "MESSAGE_20451298091",
"errors": []
}





### 8.2 Schedule Draft


Using this API, you can schedule an existing draft for publishing pictures to Facebook album.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule

#### Sample API Request: Schedule Draft for Facebook




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": 66000050,
    "id": 9650893,
    "content": {
        "title": "title 2",
        "text": "text 2",
        "attachment": {
            "attachments": [
                {
                    "url": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                    "title": "Timeline photos",
                    "previewUrl": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                    "type": "IMAGE",
                    "description": "desc"
                },
                {
                    "url": "https://pz.cdata.prod0.sprinklr.com/DAM/9004/0513f60f-88bf-482e-b081-5c12de3511cb-1763777752/https___pbs.twimg.com_media_F6.jpg",
                    "previewUrl": "https://pz.cdata.prod0.sprinklr.com/DAM/9004/0513f60f-88bf-482e-b081-5c12de3511cb-1763777752/https___pbs.twimg.com_media_F6.jpg",
                    "title": "Timeline photos",
                    "type": "IMAGE",
                    "description": "desc1"
                }
            ],
            "title": "Test_Album_Title",
            "existingAlbumId": "120309614415221",
            "type": "ALBUM"
        }
    },
    "taxonomy": {
        "campaignId": "66000002_14"
    },
    "scheduleDate": 1697611061000,
    "version": 2.0
}'





#### Example - Response





  Copy Code



{
"data": "POST_2045129097",
"errors": []
}





### 8.3 Publish Post


Using this API, you can publish pictures to Facebook album.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/post

#### Sample API Request: Publish Post for Facebook




  Copy Code



curl -X POST \
  'https://api2.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": 66000038,
    "content": {
        "title": "title 2",
        "text": "text 2",
        "attachment": {
            "attachments": [
                {
                    "url": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                    "previewUrl": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                    "type": "IMAGE",
                    "description": "desc"
                },
                {
                    "url": "https://pz.cdata.prod0.sprinklr.com/DAM/9004/0513f60f-88bf-482e-b081-5c12de3511cb-1763777752/https___pbs.twimg.com_media_F6.jpg",
                    "previewUrl": "https://pz.cdata.prod0.sprinklr.com/DAM/9004/0513f60f-88bf-482e-b081-5c12de3511cb-1763777752/https___pbs.twimg.com_media_F6.jpg",
                    "type": "IMAGE",
                    "description": "desc1"
                }
            ],
            "title": "Test_Album_Title",
            "existingAlbumId": "120309614415221",
            "type": "ALBUM"
        }
    },
    "taxonomy": {
        "campaignId": "66000002_14"
    }
}'





#### Example - Response




  Copy Code



{
"data": "POST_2045129123",
"errors": []
}





## 9. Instagram Story: Create Draft, Schedule Draft, Publish Post

This section will cover APIs for creating a draft, scheduling an existing draft, and publishing Instagram Story.

**Dev Notes: **Direct publishing is only supported for Instagram business accounts. For other accounts, the post will be queued for manual publishing.

### Attachment Parameters

****

| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Refers to type of the draft/post that you are creating, i.e., STORY in this case | String |
| attachments |  | Required | Refers to the array containing content details for publishing Instagram Story | Array |
|  | url | Required | Refers to the url for the media content you want to add to the Instagram story | String |
|  | previewUrl | Optional | Refers to the preview Url for the media attachment |  |
|  | type | Required | Refers to the type of attachment.Supported Types:: IMAGE, VIDEO | String |

### 9.1 Create Draft

Using this API, you can create a draft post for publishing Instagram Story.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft

#### Sample API Request: Create Draft for Instagram




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": 600057978,
    "content": {
        "title": "Insta story",
        "text": "Insta story",
        "attachment": {
            "type": "STORY",
            "attachments": [
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/e50a2071-bb89-4871-8acf-8eb02b33e7ac-214222129/pink-324175_1280.jpeg",
                    "previewUrl": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/e50a2071-bb89-4871-8acf-8eb02b33e7ac-214222129/pink-324175_1280.jpeg",
                    "type": "IMAGE"
                },
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/099a5fbb-15e5-4a81-afb9-85d14b888a71-534090421/giphy.gif",
                    "previewUrl": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/099a5fbb-15e5-4a81-afb9-85d14b888a71-534090421/giphy.gif",
                    "type": "IMAGE"
                },
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/2c57893c-7d25-40e3-af2b-6a92b5a4b5c8-1422094165/toy-3_qTc2egoH.mp4",
                    "previewUrl": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/cde2de2d-d93e-4fb3-b1dd-55dae65e63c2-1362205659/preview_image_0-toy-3_qTc2egoH.png",
                    "type": "VIDEO"
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "66000002_14"
    }
}





#### Example - Response




  Copy Code



{
"data": "MESSAGE_20451298074",
"errors": []
}





### 9.2 Schedule Draft


Using this API, you can schedule an existing draft for publishing Instagram Story.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule

#### Sample API Request: Schedule Draft for Instagram




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": 600057978,
    "id": 9658984,
    "content": {
        "title": "Insta Story Draft Schedule",
        "text": "Insta Story Draft Schedule",
        "attachment": {
            "attachments": [
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/e50a2071-bb89-4871-8acf-8eb02b33e7ac-214222129/pink-324175_1280.jpeg",
                    "title": "Timeline photos",
                    "previewUrl": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/e50a2071-bb89-4871-8acf-8eb02b33e7ac-214222129/pink-324175_1280.jpeg",
                    "type": "IMAGE"
                },
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/099a5fbb-15e5-4a81-afb9-85d14b888a71-534090421/giphy.gif",
                    "title": "Timeline photos",
                    "previewUrl": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/099a5fbb-15e5-4a81-afb9-85d14b888a71-534090421/giphy.gif",
                    "type": "IMAGE"
                },
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/2c57893c-7d25-40e3-af2b-6a92b5a4b5c8-1422094165/toy-3_qTc2egoH.mp4",
                    "title": "Timeline photos",
                    "previewUrl": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/cde2de2d-d93e-4fb3-b1dd-55dae65e63c2-1362205659/preview_image_0-toy-3_qTc2egoH.png",
                    "type": "VIDEO"
                }
            ],
            "type": "STORY"
        }
    },
    "taxonomy": {
        "campaignId": "66000002_14"
    },
    "version": 2.0,
    "scheduleDate": 1697785591000
}'





#### Example - Response




  Copy Code



{
"data": "POST_2045129032",
"errors": []
}





### 9.3 Publish Post

Using this API, you can directly publish Instagram story using Instagram business account. For other accounts, the post will be added to manual publishing queue.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/post

#### Sample API Request: Publish Post for Instagram




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": 600057978,
    "content": {
        "attachment": {
            "type": "STORY",
            "attachments": [
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/e50a2071-bb89-4871-8acf-8eb02b33e7ac-214222129/pink-324175_1280.jpeg",
                    "previewUrl": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/e50a2071-bb89-4871-8acf-8eb02b33e7ac-214222129/pink-324175_1280.jpeg",
                    "type": "IMAGE"
                },
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/099a5fbb-15e5-4a81-afb9-85d14b888a71-534090421/giphy.gif",
                    "previewUrl": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/099a5fbb-15e5-4a81-afb9-85d14b888a71-534090421/giphy.gif",
                    "type": "IMAGE"
                },
                {
                    "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/2c57893c-7d25-40e3-af2b-6a92b5a4b5c8-1422094165/toy-3_qTc2egoH.mp4",
                    "previewUrl": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/cde2de2d-d93e-4fb3-b1dd-55dae65e63c2-1362205659/preview_image_0-toy-3_qTc2egoH.png",
                    "type": "VIDEO"
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "66000002_14"
    }
}'





#### Example - Response




  Copy Code



{
"data": "POST_2045129126",
"errors": []
}





## 10. Twitter Thread: Create Draft, Schedule Draft, Publish Post

This section will cover APIs for creating a draft, scheduling an existing draft, and publishing Twitter Thread.

### Attachment Parameters

| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Refers to the type of Twitter post, i.e., THREAD in this case | String |
| threads |  | Required | Refers to array containing Twitter thread details | Array |
|  | title | Optional | Refers to the title of the Twitter thread post | String |
|  | text | Required | Refers to the textual content of the Twitter thread post | String |
|  | attachment | Optional | Refers to the object containing the attachment details for parent and the consecutive threads (if any)Refer to the table below for attachment object parameters' description | Object |

### Attachment Object Parameters' Description

****

| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| attachments |  | OptionalRequired when attachment type is "MULTI_MEDIA" | Refers to the array containing the attachment details when the attaching multiple images to a single threadPlease note that the attachment array is only needed when the type of attachment is "MULTI_MEDIA" | Array |
|  | url | Required | Refers to the url of the attachment | String |
|  | title | Optional | Refers to the title of the attachment | String |
|  | previewUrl | Optional | Refers to the preview Url of the attachment | String |
|  | type | Required | Refers to the type of the attachmentSupported Types: IMAGE | String |
| type |  | Required | Refers to the type of the attachmentSupported Types: IMAGE, VIDEO, MULTI_MEDIA | String |
| url |  | Required | Refers to the url of the attachment | String |
| previewurl |  | Optional | Refers to the preview url of the attachment | String |
| title |  | Optional | Refers to the title of the attachment | String |

### 10.1 Create Draft

Using this API, you can create a draft post for publishing Twitter Thread.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft

#### Sample API Request: Create Draft for Twitter




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": 66000401,
    "content": {
        "title": "title 2",
        "text": "text 2",
        "attachment": {
            "threads": [
                {
                    "title": "My Message4",
                    "text": "my text1",
                    "attachment": {
                        "attachments": [
                            {
                                "url": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                                "title": "Timeline photos",
                                "previewUrl": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                                "type": "IMAGE"
                            },
                            {
                                "url": "https://sprcdn-prod0-sam.sprinklr.com/9004/Image_Asset_1-e7d4785d-0b47-4818-ab65-11e093394057-1529617391_p.jpg",
                                "type": "IMAGE"
                            }
                        ],
                        "type": "MULTI_MEDIA"
                    }
                },
                {
                    "title": "My Message2",
                    "text": "my text2",
                    "attachment": {
                        "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/88ab6d42-dcfa-4ff7-83a2-c553fa55d66e-528060825/background_-_16224_(1080p).mp4",
                        "type": "VIDEO"
                    }
                },
                {
                    "title": "My Message",
                    "text": "my text3",
                    "attachment": {
                        "url": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                        "title": "Timeline photos",
                        "previewUrl": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                        "type": "IMAGE"
                    }
                }
            ],
            "type": "THREAD"
        }
    },
    "taxonomy": {
        "campaignId": "66000002_14"
    }
}'





### Example - Response




  Copy Code



{
"data": "MESSAGE_20451298065",
"errors": []
}





### 10.2 Schedule Draft

Using this API, you can schedule an existing draft for publishing Twitter Thread.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule

#### Sample API Request: Schedule Draft for Twitter




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/draft/schedule' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": 66000401,
    "id": 9659750,
    "content": {
        "title": "title 2",
        "text": "text 2",
        "attachment": {
            "threads": [
                {
                    "title": "My Message4",
                    "text": "my text",
                    "attachment": {
                        "attachments": [
                            {
                                "url": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                                "title": "Timeline photos",
                                "previewUrl": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                                "type": "IMAGE"
                            },
                            {
                                "url": "https://sprcdn-prod0-sam.sprinklr.com/9004/Image_Asset_1-e7d4785d-0b47-4818-ab65-11e093394057-1529617391_p.jpg",
                                "type": "IMAGE"
                            }
                        ],
                        "type": "MULTI_MEDIA"
                    }
                },
                {
                    "title": "My Message2",
                    "text": "my text2",
                    "attachment": {
                        "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/88ab6d42-dcfa-4ff7-83a2-c553fa55d66e-528060825/background_-_16224_(1080p).mp4",
                        "type": "VIDEO"
                    }
                },
                {
                    "title": "My Message",
                    "text": "my text3",
                    "attachment": {
                        "url": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                        "title": "Timeline photos",
                        "previewUrl": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                        "type": "IMAGE"
                    }
                }
            ],
            "type": "THREAD"
        }
    },
    "taxonomy": {
        "campaignId": "66000002_14"
    },
    "version": 1,
    "scheduleDate": 1697785591000
}'





#### Example - Response




  Copy Code



{
"data": "POST_2045129031",
"errors": []
}





### 10.3 Publish Post


Using this API, you can publish Twitter thread post.

#### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/post

#### Sample API Request: Publish Post for Twitter




  Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": 66000401,
    "content": {
        "title": "title 2",
        "text": "text 2",
        "attachment": {
            "threads": [
                {
                    "title": "My Message4",
                    "text": "my text1",
                    "attachment": {
                        "attachments": [
                            {
                                "url": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                                "title": "Timeline photos",
                                "previewUrl": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                                "type": "IMAGE"
                            },
                            {
                                "url": "https://sprcdn-prod0-sam.sprinklr.com/9004/Image_Asset_1-e7d4785d-0b47-4818-ab65-11e093394057-1529617391_p.jpg",
                                "type": "IMAGE"
                            }
                        ],
                        "type": "MULTI_MEDIA"
                    }
                },
                {
                    "title": "My Message2",
                    "text": "my text2",
                    "attachment": {
                        "url": "https://storage.googleapis.com/spr-qa6-cdn/DAM/66000000/88ab6d42-dcfa-4ff7-83a2-c553fa55d66e-528060825/background_-_16224_(1080p).mp4",
                        "type": "VIDEO"
                    }
                },
                {
                    "title": "My Message",
                    "text": "my text3",
                    "attachment": {
                        "url": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                        "title": "Timeline photos",
                        "previewUrl": "https://fastly.picsum.photos/id/311/200/300.jpg?hmac=ltcRErkHQZRTlJl3xZ_6HSzWzco1GSU3zbZhA12WvJw",
                        "type": "IMAGE"
                    }
                }
            ],
            "type": "THREAD"
        }
    },
    "taxonomy": {
        "campaignId": "66000002_14"
    }
}'





#### Example - Response




  Copy Code



{
"data": "POST_2045129098",
"errors": []
}





[](https://dev.sprinklr.com/publishing-blueprint)

[Back to top](https://dev.sprinklr.com/publishing-blueprint)
