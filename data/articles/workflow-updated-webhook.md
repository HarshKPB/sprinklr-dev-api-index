---
title: "Workflow Updated Webhook"
slug: workflow-updated-webhook
url: https://dev.sprinklr.com/workflow-updated-webhook
---

# Workflow Updated Webhook

# Workflow Updated Webhook

**Workflow Webhook Subscriptions:**
 Workflow Updated

Whenever the message queue gets updated, the webhook notification is triggered with the details that are described in the following documents:

**Dev Notes: **Workflow updated webhook triggers whenever there are custom property or queues level changes at message level.

### Workflow Updated Webhook





  Copy Code



{
  "id": "5f60729e203e4c2f85f04ac8",
  "type": "workflow.updated",
  "payload": {
    "sourceType": "PERSISTENT_SEARCH",
    "sourceId": 431176,
    "content": {
      "text": "Ready for watching. 🙂👍",
      "richText": "Ready for watching. 🙂👍",
      "attachment": {
        "url": "https://video.twimg.com/ext_tw_video/1294516335361/pu/vid/864x480/oXtU3obf_Sn12.mp4?tag=10",
        "previewUrl": "https://pbs.twimg.com/ext_tw_video_thumb/129451635361/pu/img/sjY8TLYozEtFZ.jpg",
        "type": "VIDEO"
      }
    },
    "channelMessageId": "1294718074654875648",
    "channelType": "TWITTER",
    "channelCreatedTime": 1597519818353,
    "senderProfile": {
      "name": "covidkalang",
      "channelType": "TWITTER",
      "channelId": "1241023158859096064",
      "permalink": "https://twitter.com/covidlang",
      "avatarUrl": "https://twitter.com/covidlang/profile_image?size=original",
      "followers": 21,
      "username": "covidkalang",
      "verified": false,
      "unSubscribed": false,
      "deleted": false,
      "snCreatedTime": 0,
      "snModifiedTime": 0
    },
    "permalink": "https://www.twitter.com/covidlang/status/1294718074654875648",
    "language": "tl",
    "messageId": "PERSISTENT_SEARCH_431176_1597519818353_TWITTER_8_1294718074654875648",
    "brandPost": false,
    "createdTime": 1597519852923,
    "modifiedTime": 1597519853397,
    "textEntities": {
      "message": [
        {
          "indices": [
            232,
            255
          ],
          "url": "https://t.co/AvEtp98d73"
        }
      ]
    },
    "insights": {
      "FOLLOWER_COUNT_AT_POST": 21,
      "POST_REACH_COUNT": 21
    },
    "workflow": {
      "modifiedTime": 1600156318356,
      "customProperties": {},
      "queues": [],
      "spaceWorkflows": []
    },
    "enrichments": {
      "sentiment": 1
    },
    "conversationId": "1294718074654875648",
    "autoImported": false
  },
  "eventTime": 1600156318374,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf57e0a2"
  }
}





### Response Definitions







[Here](https://dev.sprinklr.com/webhook-types)

[Click here](https://dev.sprinklr.com/channels-v1)

| Parameters | Description | Type |
| --- | --- | --- |
| id | Id of the webhook triggered event that contains all information related to occurred events. | String |
| type | Type of event.  you can find the type of webhook events | String |
| payload | The payload contains the details of the field related to the triggered event. |  |
| sourceType | Source of the “type” of event.Message SourceType = {ACCOUNT, PERSISTENT_SEARCH, LISTENING} | String |
| sourceId | Source Id based on the source type. | String |
| content | It contains details related to the message. | String |
| text | Text present in the message. | String |
| richText | Message in the rich text format | String |
| attachment | Attachment information. |  |
| url | Url of attachment. | URL |
| previewUrl | To preview the attachment. | URL |
| title | The title has written by a user based on the message attachment type. | String |
| type | Type of attachment i.e. Link, Text, Image, Video, etc. | String |
| channelMessageId | Id of the message on Native. | String |
| channelType | Native social channel.  to view the supported channel type. | String |
| accountType | Type of account in the native. | String |
| senderProfile | Details are given in Sender Profile Definitions Table. |  |
| permalink | Native URL of the message. | URL |
| language | The language used in the native channel. | String |
| messageId | Message id in Sprinklr. | String |
| postId | Post id of the message. | String |
| brandPost | If true, It is a brand post. | Boolean |
| createdTime | Message creation time. | Unix Epoch |
| modifiedTime | Time at which the message is modified. | Unix Epoch |
| textEntities | Text entities if any in the message. | String |
| insights | Insights related to message.Example:"insights": { 				      "POST_LIKE_COUNT": 1, 				      "POST_FB_IMPRESSIONS": 2 				    } | Integer |
| workflow | Custom properties of the message. | String |
| enrichments | It shows the sentiment of the message.Example:"enrichments": { 				      "sentiment": 0 				    } | Positive, Negative,Neutral |
| eventTime | The event occurred time. When the webhook was triggered. | Unix Epoch |
| subscriptionDetails | It contains the details of the subscription.Example:"subscriptionDetails": { 				    "subscriptionId": "5dd7b694a468895c581087c6" 				  } |  |

#### Sender Profile Definitions







| Parameters | Description | Type |
| --- | --- | --- |
| name | Name of the profile from which message is sent. | String |
| channelType | Native social channel.Message SourceType = {ACCOUNT, PERSISTENT_SEARCH, LISTENING} | String |
| channeld | Channel id in native. | String |
| permalink | Native profile URL. | URL |
| avatarUrl | Url to profile picture. | URL |
| followers | Followers count of the profile. | Integer |
| username | Username of the profile. | String |
| verified | If true, the profile is verified. | Boolean |
| unSubscribed | If true, the profile gets unsubscribed. | Boolean |
| deleted | If true, deleted. | Boolean |
| snCreatedTime | Profile creation time in Native. | Unix Epoch |
| snModifiedTime | Profile modification time in Native. | Unix Epoch |

[](https://dev.sprinklr.com/reporting-blueprints)

[Back to top](https://dev.sprinklr.com/reporting-blueprints)
