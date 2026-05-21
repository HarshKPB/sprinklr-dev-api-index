---
title: "Publishing Post"
slug: publishing-post
url: https://dev.sprinklr.com/publishing-post
---

# Publishing Post

#
POST Publishing Post


You can publish a new post across social media channels using this API call.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/publishing/post

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
| workspace_id | workspaceId | This field is optional. If your authorization token is associated with multiple workspaces, you'll have to pass workspace_id in the headers for publishing a post. You can use  to check the workspace Id your token is primarily associated with. |

### Request Parameters

This document covers four types of post publishing (*find the quick links below*). The request parameters for different post types will mostly remain the same, except for the attachment object.


- [Create New Social Media Post (All Channels)](https://dev.sprinklr.com/publishing-post#create-new-social-media-post-all-channels)

- [Create New Social Media Post With Attachment (All Channels)](https://dev.sprinklr.com/publishing-post#create-new-social-media-post-with-attachment-all-channels)

- [Create New Social Media Post With Multiple Attachments](https://dev.sprinklr.com/publishing-post#create-new-social-media-post-with-multiple-attachments)

- [Create New Carousel Post](https://dev.sprinklr.com/publishing-post#create-new-carousel-post)

- [Tag People/Accounts on Instagram Images](https://dev.sprinklr.com/publishing-post#tag-people-accounts-on-instagram-images)

- [Create New Email Post](https://dev.sprinklr.com/publishing-post#create-new-email-post)

- [Create a Video Post with Captions](https://dev.sprinklr.com/publishing-post#create-a-video-post-with-captions)

- [Create an Instagram Reel](https://dev.sprinklr.com/publishing-post#create-instagram-reel)


















































````

































``````



















[Supported Channels](https://dev.sprinklr.com/channels-v1)


















****











[segment audience](https://www.sprinklr.com/help/articles/segment-manager/segment-manager/64920b8d723d925979dec013)

****``







































































****












| Parameters | Sub Parameters | Sub-Param objects | Required/Optional | Description | Type |  |
| --- | --- | --- | --- | --- | --- | --- |
| accountIds |  |  | Required | array of account ids from where you want to publish the post | Integer |  |
| content |  |  | Required | The object containing Content details. |  |  |
|  | title |  | Optional | Title of the post, if any. | String |  |
|  | text |  | Required | The text you want to publish. | String |  |
|  | attachment |  | Optional | The attachment object contains the details of the attachments.For the Instagram carousel and multiple attachments post, refer to the description tables below | Object |  |
|  |  | type | Optional | Type of attachment. VIDEO, IMAGE, CAROUSEL, MULTI_MEDIA | String |  |
|  |  | url | Optional | The url of attachment. |  |  |
|  |  | alternateText | Optional | Refers to the alt text for the IMAGE attachment | String |  |
|  |  | attachmentOptions{ 				channelType 				accountId                                 locationId                                 } | OptionalattachmentOptions is currently supported for only 3 channel types, i.e., INSTAGRAM, FACEBOOK, and TWITTER | Array of attachment properties per channel and/or account.{ChannelType for media options.If the properties are specific to an account in addition to channelType, accountId can be specified and the properties would then only be used for the given accountlocationId is valid for Instagram channels only} | Array |  |
| channelOptions |  |  | Optional | Channel specific options, if any |  |  |
|  | channelType |  | Optional | ChannelType for the options.Enum: [ FACEBOOK ] Refer to  for more details. | String |  |
|  | accountId |  | Optional | If the option is specific to an account in addition to channelType, accountId can be specified and the options would then only be used for the given account | Integer |  |
|  | darkPost |  | Optional | Dark posts allows creating content to target different audiences without publishing the content to the page. These posts are created when you create ads or use paid promotionIn simple words, a dark post is never published but is only surfaced as an ad.Note: Dark Posts published natively on a channel will not be pulled into Sprinklr unless a comment is made on the post. A comment action on the Dark Post will cause the Dark Post to be imported into the Sprinklr platform. | Boolean |  |
| scheduleDate |  |  | Optional | Schedule date for the post | Integer |  |
| audienceId |  |  | Optional | Refers to the audience Id you want to restrict the post from. You can setup  within Sprinklr that share common properties. If you want to restrict a particular audience from seeing the post, you can add the audience's unique identifier in the payloadNote: This feature is only applicable to Facebook posts | String |  |
|  | taxonomy |  |  |  | Object containing taxonomy details. |  |
|  | campaignId |  | Required | Campaign identifier to associate the post with. | String |  |
|  | clientCustomProperties |  | Optional | client custom properties for the post | String |  |
|  | partnerCustomProperties |  | Optional | partner custom properties for the post | String |  |
|  | tags |  | Optional | Tags to be added to the post | String |  |
|  | urlShortenerId |  | Optional | Url shortner identifier to apply to the post | String |  |
| approval |  |  |  | Object containing Approval details. |  |  |
|  | type |  | Optional | Type of approval to process. defaults to NONE 				 				Enum: [ ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE | String |  |
|  | id |  | Optional | Required when the approval type chosen is:“Follows an approval path”. | String |  |
| version |  |  | Optional | Current version of the message. | Integer |  |



**Dev Notes: **The `locationId` field is available only for Instagram. You can find the locationId using the [lookup API.](https://dev.sprinklr.com/lookup)

### Example: Create New Social Media Post (All Channels)

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
  "id": 0,
  "accountIds": [
    0
  ],
  "content": {
    "title": "string",
    "text": "string",
    "attachment": {
      "type": "IMAGE",
      "url":"{The Url of the image or video that you want to Post}",
      "attachmentOptions": [
        {
          "channelType": "FACEBOOK",
          "accountId": 0
        }
      ]
    }
  },
  "channelOptions": [
    {
      "channelType": "FACEBOOK",
      "accountId": 0,
      "darkPost": false
    }
  ],
  "scheduleDate": 0,
  "taxonomy": {
    "campaignId": "string",
    "clientCustomProperties": {
      "additionalProp1": [
        "string"
      ],
      "additionalProp2": [
        "string"
      ],
      "additionalProp3": [
        "string"
      ]
    },
    "partnerCustomProperties": {
      "additionalProp1": [
        "string"
      ],
      "additionalProp2": [
        "string"
      ],
      "additionalProp3": [
        "string"
      ]
    },
    "tags": [
      "string"
    ],
    "urlShortenerId": "string"
  },
  "approval": {
    "type": "ACCOUNT_OWNER",
    "id": "string"
  },
  "version": 0
}'
 

     
     
   

### Example - Response

 
 
     
 
{
    "data": [],
    "errors": [
    ]
}
 

     
     
   
 

### Example: Create new Social Media Post With Attachment (All Channels)

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
    "accountIds": [
        229835
    ],
    "content": {
    "title": "sample",
    "text": "NEW TEST",
    "attachment": {
        "url": "https://sprcdn-assets.sprinklr.com/787/Check-312bdd6b-c33e-40e2-b041-6de8b805aec-189354701.mp4",
        "type": "VIDEO"
      }
  },
    "taxonomy": {
        "campaignId": "4483_206"
    }
}'
 

     
     
   

## Example - Response

 
 
     

{
    "data": [
        "POST_3630973254"
    ],
    "errors": []
}
 

     
     
   
 

### Example: Create new Social Media Post With Multiple Attachments

**Attachment  Object Description Table for Multiple Attachments**













| Parameters | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Refers to the type of the attachment"MULTI_MEDIA" in this case | String |
| attachments |  | Required | Array containing the attachment details | Array |
|  | type | Required | Refers to the type of the attachmentExample: VIDEO, IMAGE | String |
|  | url | Required | Refers to the publically accessible url for the attachment | String |

### Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [
        1000069117
    ],
    "content": {
        "text": "Publishing API2 POST on twitter Page with multiple images attached 2023-05-25 22:44:40.926",
        "attachment": {
            "type": "MULTI_MEDIA",
            "attachments": [
                {
                    "type": "IMAGE",
                    "url": "https://sprcdn-prod0-sam.sprinklr.com/9004/Image_Asset_1-e7d4785d-0b47-4818-ab65-11e093394057-1529617391_p.jpg",
                    "alternateText": "Adding alt text for image"
                },
                {
                    "type": "IMAGE",
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg",
                    "alternateText": "Adding alt text for image"
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "1000004509_1594"
    }
}'
 

     
     
 

## Example - Response

 
 
     

{
    "data": [
        "POST_3630973258"
    ],
    "errors": []
}
 

     
     
   
 

### Example: Create New Carousel Post

**Attachment Object Description Table for Carousel Post**






















































| Parameters | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | The type of attachment i.e. CAROUSEL | String |
| mediaAttachmentList |  | Required | The list of images/videos in a carousel. You can add at max 10 attachments | Array |
|  | type | Required | The type of attachment | String |
|  | title | Required | The title of the attachment | String |
|  | description | Required | The description of the attachment | String |
|  | url | Required | The URL of the attachment | String |
| clickThroughUrl |  | Required when publishing a Facebook Carousel Post | Refers to the common Url that will act as the redirect URL for all the items in the carousel | Url |

### Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
"accountIds": 600045231,
    "content": {
        "attachment": {
            "type": "CAROUSEL",
            "mediaAttachmentList": [
                {
                    "type": "IMAGE",
                    "title": "IMAGE 1",
                    "description": "Media Asset Description 1",
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg"
                },
                {
                    "type": "IMAGE",
                    "title": "IMAGE 2",
                    "description": "Media Asset Description 2",
                    "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg"
                }
            ]
        }
    },
    "taxonomy": {
        "campaignId": "23_453"
    },
  "approval": { }
}'
 

     
     
   

### Example - Response

 
 
     
 
{
    "data": [
        "POST_600000009736513"
    ],
    "errors": []
}
 

     
     
   
 

### Example: Tag People/Accounts on Instagram Images

**Attachment Object Description Table for Tagging People on Instagram**










































``````





















| Parameters | Sub-Param | Sub-Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- | --- |
| Type |  |  | Required | The type of attachment. For example: IMAGE | String |
| URL |  |  | Required | The URL of the attachment type | URL |
| previewUrl |  |  | Optional | The preview URL of the image | URL |
| attachmentOptions |  |  | RequiredattachmentOptions is currently supported for only 3 channel types, i.e., INSTAGRAM, FACEBOOK, and TWITTER | Array describing the attachment details | Array |
|  | channelType |  | Required | Channel type for the attachmentchannelType will be "INSTAGRAM" for tagging images | String |
|  | userTags |  | Required | The array defining the tagging details | Array |
|  |  | username | Required | The Instagram username of the person you want to tag | String |
|  |  | x | Required | The longitude coordinate where you want to add the tag on the image | String |
|  |  | y | Required | The latitude coordinate where you want to add the tag on the image | String |
|  |  | url | Required | The URL of the user account you want to tag | URL |

### Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
  "accountIds": [
       1000069270
   ],
   "content": {
       "text": "test tag",
       "attachment": {
           "type": "IMAGE",
           "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg",
           "attachmentOptions": [
               {
                   "channelType": "INSTAGRAM",
                   "userTags": [
                       {
                           "username": "elena.js",
                           "x": "0.4961829811476927",
                           "y": "0.19380626634165207",
                           "url": "https://www.instagram.com/elena.js/"
                       },
                       {
                           "username": "frooto_in",
                           "x": "0.8778626",
                           "y": "0.19297405",
                           "url": "https://www.instagram.com/elenasalvatore.js/"
                       }
                   ]
               }
           ]
       }
   },
   "taxonomy": {
       "campaignId": "1000006709_1932"
   },
   "approval": {}
}'
 

     
     
   

### Example - Response

 
 
     
 
{
    "data": [
        "POST_2165857003"
    ],
    "errors": []
}
 

     
     
   
 

### Response Parameters















| Parameters | Description | Type |
| --- | --- | --- |
| Post_Id | The Id of the newly created social media post | String |

### Example: Create New Email Post

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [
        1000136963
    ],
    "accountGroupIds": [],
    "content": {
        "title": "test",
        "text": "email"
    },
    "channelOptions": [
        {
            "toEmailAddress": [
                "john.doe@sprinklr.com"
            ],
            "channelType": "EMAIL"
        }
    ],
    "scheduleDate": 0,
    "taxonomy": {
        "campaignId": "4509_1"
    }
}'
 

     
     
   

### Example - Response

 
 
     
 
{
    "data": [
        "POST_2165857004"
    ],
    "errors": []
}
 

     
     
   
 

### Example: Create a Video Post with Captions

**Attachment  Object Description Table for Attaching Video with captions**












****

****``

| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Refers to the type of the attachment, i.e., VIDEO in this case. | String |
| title |  | Optional | Refers to the title of the attachment | String |
| url |  | OptionalRequired when you need to associate an attachment to the post | Refers to the publically accessible url of the attachment | Url |
| previewUrl |  | Optional | Refers to the preview url of the attachment, i.e., the thumbnail for the attachment | Url |
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
|  | url | Required | Refers to the publicly accessible url for the captions file | Url |
|  | extension | Required | Refers to the extension format of the captions file | String |

 
 
       
 
 
 
 
 
 
 
 
 
 
 
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
        "title": "Testing API2 publishing",
        "text": "Testing API2 publishing",
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
 

     
     
 

## Example - Response

 
 
     
 
{
    "data": [
        "POST_2165857005"
    ],
    "errors": []
}
 

     
     
   
 

### Response Parameters















| Parameters | Description | Type |
| --- | --- | --- |
| Post_Id | The Id of the newly created social media post | String |

### Example: Create Instagram Reel

**Request Body Description Table for Instagram Reel**


















































     ``













   ``













  ``














| Parameter | Sub-Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- | --- |
| accountIds |  | Required | List of Sprinklr account IDs to which the Instagram Reel will be published. Must contain at least one Instagram Business account ID. | Array<Number> |
| content |  | Required | Contains the core content details for the Instagram Reel. | Object |
|  | title | Optional | Internal title for the post. Used for identification in Sprinklr and not published to Instagram. | String |
|  | text | Required | Caption text for the Instagram Reel. This text appears as the Reel caption on Instagram. | String |
|  | attachment | Required | Media attachment details for the Reel. Instagram Reels require a single video attachment. | Object |
| scheduleDate |  | Required | Unix timestamp (in milliseconds) for scheduled publishing. Use 0 to publish immediately. | Number |
| channelOptions |  | Required | Channel-specific publishing options. | Array<Object> |
|  | channelType | Required | Social media channel for publishing. Set this value to INSTAGRAM. | String |
|  | accountId | Required | Instagram Business account ID where the Reel will be published. | Number |
|  | mediaType | Required | Type of Instagram content being published. Must be set to REEL. | String |
| taxonomy |  | Optional | Metadata used for campaign tracking and reporting. | Object |
|  | campaignId | Optional | Campaign identifier used to associate the Reel with a specific marketing campaign in Sprinklr. | String |

**Attachment Object**










   ``
















``

| Parameter | Sub-Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- | --- |
| type |  | Required | Type of media attached. Must be set to VIDEO for Instagram Reels. | String |
| url |  | Required | Publicly accessible URL of the video file to be published as a Reel. | String |
| previewUrl |  | Optional | URL of the preview image or thumbnail for the video. If not provided, Instagram selects a default frame. | String |
| attachmentOptions |  | Required | Channel-specific attachment configuration. | Array<Object> |
|  | channelType | Required | Social media channel for the attachment. Set this value to INSTAGRAM. | String |
|  | accountId | Required | Instagram Business account ID associated with the video attachment. | Number |

### Example Request - Publish Instagram Reel

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/publishing/post' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "accountIds": [
        66073052
    ],
    "content": {
        "title": "Test publishing reel3",
        "text": "Test publishing reel4",
        "attachment": {
            "type": "VIDEO",
            "url": "https://storage.googleapis.com/spr-qa6-cdn-secure/DAM/66000000/ee658421-f85f-4b07-95ff-43b4c80ced4c-1043006613/file_example_MP4_480_1_5MG_(1).mp4",
            "previewUrl": "https://storage.googleapis.com/spr-qa6-cdn-secure/DAM/66000000/3942a906-53c4-43a5-b00c-fc5ed566ac03-387636868/preview_image_0-file_example_M.png",
            "attachmentOptions": [
                {
                    "channelType": "INSTAGRAM",
                    "accountId": 66073052
                }
            ]
        }
    },
    "scheduleDate": 0,
    "channelOptions": [
        {
            "channelType": "INSTAGRAM",
            "accountId": 66073052,
            "mediaType":"REEL"
        }
    ],
    "taxonomy": {
        "campaignId": "66000002_6883"
    }
}'
 

     
     
 

### Example - Response

 
 
     
 
{
    "data": [
        "POST_546651018"
    ],
    "errors": []
}
 

     
     
   
 

### Response Parameters
















| Parameters | Description | Type |
| --- | --- | --- |
| Post_Id | The Id of the newly instagram reel | String |

[](https://dev.sprinklr.com/publishing-post) 

 

 
[Back to top](https://dev.sprinklr.com/publishing-post)
