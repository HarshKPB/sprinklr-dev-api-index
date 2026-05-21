---
title: "Message Webhooks"
slug: message-webhooks
url: https://dev.sprinklr.com/message-webhooks
---

# Message Webhooks

#
  Message Webhooks

		**Message Webhook Subscriptions:**
 Updated, Received, Deleted, Message Engagement Updated, Message Read, Message Delivered, Published, Publish Failed, Message Publish Failed

Whenever user sends a message or an action is performed on message either via Sprinklr UI or API, webhook notification are triggered with the details that are described in the following documents:

- [Message.Created Webhook](https://dev.sprinklr.com/message-webhooks#MR)

- [Message.Updated Webhook](https://dev.sprinklr.com/message-webhooks#MU)

- [Message.Deleted Webhook](https://dev.sprinklr.com/message-webhooks#MD)

- [Message.Engagement.Updated Webhook](https://dev.sprinklr.com/message-webhooks#MEU)

- [Message.Published Webhook](https://dev.sprinklr.com/message-webhooks#MP)

- [Message.Read Webhook](https://dev.sprinklr.com/message-webhooks#MRW)

- [Message.Delivered Webhook](https://dev.sprinklr.com/message-webhooks#MDW)

- [Message.Publish.Failed Webhook](https://dev.sprinklr.com/message-webhooks#MPF)

- [Message.Sent.For.Approval Webhook](https://dev.sprinklr.com/message-webhooks#MSFA)

- [Post.Trend.Metrics.Change Webhook](https://dev.sprinklr.com/message-webhooks#post-trend)

### Message.Created Webhook

#### JSON Response




  Copy Code

{
   "id": "624d13cce13f043114f1204d",
   "type": "message.created",
   "payload": {
       "draftId": 600000009172522,
       "sourceType": "ACCOUNT",
       "sourceId": 600039142,
       "content": {
               "text": "@abc_test @xyz_test",
               "richText": "@abc_test @xyz_test"
      },
      "channelMessageId": "1511558084136685272",
      "channelType": "TWITTER",
      "accountType": "TWITTER",
      "channelCreatedTime": 1649218505306,
      "senderProfile": {
               "name": "Ray",
               "channelType": "TWITTER",
               "channelId": "1062932421388132151",
               "permalink": "https://twitter.com/Ray12",
               "avatarUrl": "https://abs.twimg.com/sticky/default_profile_images/default_profile.png",
               "bio": "",
               "followers": 2,
               "following": 38,
               "username": "Ray12",
               "verified": false,
               "unSubscribed": false,
               "deleted": false,
               "snCreatedTime": 0,
               "snModifiedTime": 0,
               "statusCount": 93
      },
      "receiverProfile": {
              "name": "abc",
              "channelType": "TWITTER",
              "channelId": "859271710",
              "permalink": "https://twitter.com/abc_test",
              "avatarUrl": "https://pbs.twimg.com/profile_images/478429801032597504/ihdJNAtu.jpeg",
              "bio": "Programming, Hacking, Security Vulnerability, Distributed and Cloud Computing, Massive Parallel Computing, Natural Language Processing, Artificial Intelligence",
              "followers": 107,
              "following": 88,
              "username": "abc_test",
              "verified": false,
              "unSubscribed": false,
              "deleted": false,
              "snCreatedTime": 0,
              "snModifiedTime": 0,
              "statusCount": 14551
      },
      "mentionedProfiles": [
        {
              "name": "xyz",
              "channelType": "TWITTER",
              "channelId": "1422199331818409188",
              "followers": 0,
              "following": 0,
              "username": "xyz_test",
              "deleted": false,
              "snCreatedTime": 0,
              "snModifiedTime": 0,
              "statusCount": 0
        },
        {
              "name": "abc",
              "channelType": "TWITTER",
              "channelId": "859271710",
              "followers": 0,
              "following": 0,
              "username": "abc_test",
              "deleted": false,
              "snCreatedTime": 0,
              "snModifiedTime": 0,
              "statusCount": 0
        }
      ],
      "permalink": "https://twitter.com/Rrathore19/status/1511558084136685272",
      "language": "fr",
      "messageId": "ACCOUNT_600039142_1649218505306_TWITTER_7_1511558084136685272",
      "postId": 600000006735715,
      "brandPost": false,
      "createdTime": 1649218507139,
      "modifiedTime": 1649218507567,
      "textEntities": {
        "message": [
          {
            "indices": [
              0,
              11
            ],
            "screenName": "abc"
          },
          {
            "indices": [
              12,
              26
            ],
            "screenName": "xyz"
          }
        ]
      },
      "location": {
        "lat": 0,
        "lon": 0
      },
      "insights": {
        "POST_REACH_COUNT": 2
      },
      "workflow": {
        "modifiedTime": 1649218507879,
        "customProperties": {},
        "queues": [
          {
            "queueId": 101416,
            "assignmentTime": 1649218507840
          }
        ],
        "spaceWorkflows": [],
        "campaignId": "2_11"
      },
      "enrichments": {
        "sentiment": 0
      },
      "conversationId": "1443895480526591149",
      "parentMessageId": "ACCOUNT_600039142_1634191118951_TWITTER_7_1448528657438359554",
      "autoImported": true,
      "autoResponse": false
    },
    "eventTime": 1649218507139,
    "subscriptionDetails": {
      "subscriptionId": "624d139f24327f30d640b6ee"
    }
  }


















		[Here](https://dev.sprinklr.com/webhook-types)















































































		[Click here](https://dev.sprinklr.com/channels-v1)




































































































| Parameters | Description | Type |
| --- | --- | --- |
| id | Id of the webhook triggered event that contains all information related to occurred events. | String |
| type | Type of event.  you can find the type of webhook events | String |
| payload | The payload contains the details of the field related to the triggered event. |  |
| draftId | The Id of the created draft | Integer |
| sourceType | Source of the “type” of event.Message SourceType = {ACCOUNT, PERSISTENT_SEARCH, LISTENING} | String |
| sourceId | Source Id based on the source type. | String |
| content | It contains details related to the message. | String |
| text | Text present in the message. | String |
| attachment | Attachment information. |  |
| url | Url of attachment. | URL |
| previewUrl | To preview the attachment. | URL |
| title | The title has written by a user based on the message attachment type. | String |
| type | Type of attachment i.e. Link, Text, Image, Video, etc. | String |
| channelMessageId | Id of the message on Native. | String |
| channelType | Native social channel.  to view the supported channel type. | String |
| accountType | Type of account in the native. | String |
| senderProfile/receiverProfile | Details are given in Sender and Receiver Profile Definitions Table. |  |
| permalink | Native URL of the message. | URL |
| language | The language used in the native channel. | String |
| messageId | Message id in Sprinklr. | String |
| postId | Post id of the message. | String |
| brandPost | If true, It is a brand post. | Boolean |
| createdTime | Message creation time. | Unix Epoch |
| modifiedTime | Time at which the message is modified. | Unix Epoch |
| textEntities | Text entities if any in the message. | String |
| insights | Insights related to message.Example:"insights": { 			      "POST_LIKE_COUNT": 1, 			      "POST_FB_IMPRESSIONS": 2 			    } | Integer |
| workflow | Custom properties of the message. | String |
| enrichments | It shows the sentiment of the message.Example:"enrichments": { 			      "sentiment": 0 			    } | Positive, Negative,Neutral |
| eventTime | The event occurred time. When the webhook was triggered. | Unix Epoch |
| subscriptionDetails | It contains the details of the subscription.Example:"subscriptionDetails": { 			    "subscriptionId": "5dd7b694a468895c581087c6" 			  } |  |


### Sender and Receiver Profile Definitions

















































































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

### Message.Updated Webhook


#### JSON Response




  Copy Code

{
  "id": "5ed5d336a335617905d38176",
  "type": "message.updated",
  "payload": {
    "sourceType": "ACCOUNT",
    "sourceId": -14,
    "content": {
      "title": "Account Engagement Alert",
      "text": "We have noticed high engagement on Account: **Louis Vuitton** on Twitter.\nExpected Engagements: 45, Actual Engagements: 184.\n"
    },
    "channelMessageId": "9993342_24060bd293362f592525932f3f9cc9e3_1590914700000",
    "channelType": "SPRINKLR_ALERT",
    "channelCreatedTime": 1590914700000,
    "senderProfile": {
      "name": "Sprinklr Platform",
      "channelType": "SPRINKLR_ALERT",
      "channelId": "sprinklr_platform",
      "followers": 0,
      "username": "sprinklr platform",
      "unSubscribed": false,
      "deleted": false,
      "snCreatedTime": 0,
      "snModifiedTime": 0
    },
    "language": "en",
    "messageId": "ACCOUNT_-14_1590914700000_SPRINKLR_ALERT_239_9993342_24060bd293362f592525932f3f9cc9e3_1590914700000",
    "brandPost": false,
    "createdTime": 1590915924047,
    "modifiedTime": 1591071542825,
    "textEntities": {},
    "insights": {},
    "workflow": {
      "modifiedTime": 1590917142569,
      "customProperties": {},
      "queues": [
        {
          "queueId": 4,
          "assignmentTime": 1590915924351
        }
      ],
      "spaceWorkflows": []
    },
    "enrichments": {
      "sentiment": 0
    }
  },
  "eventTime": 1591071542852,
  "subscriptionDetails": {
    "subscriptionId": "5e5d0302a468896782356d8f"
  }
}


















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
| attachment | Attachment information. |  |
| url | Url of attachment. | URL |
| previewUrl | To preview the attachment. | URL |
| title | The title has written by a user based on the message attachment type. | String |
| type | Type of attachment i.e. Link, Text, Image, Video, etc. | String |
| channelMessageId | Id of the message on Native. | String |
| channelType | Native social channel.  to view the supported channel type. | String |
| accountType | Type of account in the native. | String |
| senderProfile | Details are given in Sender and Receiver Profile Definitions Table. |  |
| permalink | Native URL of the message. | URL |
| language | The language used in the native channel. | String |
| messageId | Message id in Sprinklr. | String |
| postId | Post id of the message. | String |
| brandPost | If true, It is a brand post. | Boolean |
| createdTime | Message creation time. | Unix Epoch |
| modifiedTime | Time at which the message is modified. | Unix Epoch |
| textEntities | Text entities if any in the message. | String |
| insights | Insights related to message.Example:"insights": { 			      "POST_LIKE_COUNT": 1, 			      "POST_FB_IMPRESSIONS": 2 			    } | Integer |
| workflow | Custom properties of the message. | String |
| enrichments | It shows the sentiment of the message.Example:"enrichments": { 			      "sentiment": 0 			    } | Positive, Negative,Neutral |
| eventTime | The event occurred time. When the webhook was triggered. | Unix Epoch |
| subscriptionDetails | It contains the details of the subscription.Example:"subscriptionDetails": { 			    "subscriptionId": "5dd7b694a468895c581087c6" 			  } |  |

Sender Profile Definitions

















































































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

### Message.Deleted Webhook

#### JSON Response




  Copy Code

{
  "id": "5ed5d5f9267e4300013a9dfb",
  "type": "message.deleted",
  "payload": {
    "universalMessageId": "TWITTER_8_1246733320140083200",
    "snType": "TWITTER",
    "msgType": 8,
    "snMsgId": "1246733320140083200",
    "sourceId": 431176,
    "sourceType": "PERSISTENT_SEARCH",
    "snCreatedTimeYearMonth": "2020_04",
    "snCreatedTime": 1586079361363
  },
  "eventTime": 1591072249789,
  "subscriptionDetails": {
    "subscriptionId": "5e5d0302a468896782356d8f"
  }
}



### Message.Engagement Updated Webhook


#### JSON Response




  Copy Code

{
  "id": "5ece4fa5094fa40001f95e25",
  "type": "message.engagement.updated",
  "payload": {
    "channelMessageId": "1265561296960921604",
    "channelType": "TWITTER",
    "quotedStatusCount": 0,
    "replyCount": 6,
    "reachCount": 0,
    "totalLikes": 228,
    "retweetCount": 9,
    "totalComments": 0,
    "totalShares": 0,
    "totalLoveReactions": 0,
    "totalWowReactions": 0,
    "totalHahaReactions": 0
  },
  "eventTime": 1590568300844,
  "subscriptionDetails": {
    "subscriptionId": "5e50dae460b4d41b5270ac8a"
  }
}



### Message.Published Webhook

#### JSON Response




  Copy Code

{
  "id": "5ed5dcbde23c5c524f4ec3be",
  "type": "message.published",
  "payload": {
    "draftId": 600000009177522,
    "sourceType": "ACCOUNT",
    "sourceId": 269798,
    "content": {
      "text": "hiii"
    },
    "channelMessageId": "gBEGkXl0AndQAgmhWI4OK1_yQek",
    "channelType": "WHATSAPP_BUSINESS",
    "accountType": "WHATSAPP_BUSINESS",
    "channelCreatedTime": 1591073978000,
    "senderProfile": {
      "channelType": "WHATSAPP_BUSINESS",
      "channelId": "919591170985",
      "avatarUrl": "https://sprcdn-assets.sprinklr.com/787/Screen_Shot_2019-11-21_at_4.19-89f73560-06ab-4aef-87c7-02f9d50e9b30-2078293042.png_p.png",
      "followers": 0,
      "username": "Sprinklr Test",
      "unSubscribed": false,
      "deleted": false,
      "snCreatedTime": 0,
      "snModifiedTime": 0
    },
    "receiverProfile": {
      "name": "Sumit Kaushik",
      "channelType": "WHATSAPP_BUSINESS",
      "channelId": "917974027750",
      "followers": 0,
      "username": "Sumit Kaushik",
      "unSubscribed": false,
      "deleted": false,
      "snCreatedTime": 0,
      "snModifiedTime": 0
    },
    "language": "en",
    "messageId": "ACCOUNT_269798_1591073978000_WHATSAPP_BUSINESS_316_gBEGkXl0AndQAgmhWI4OK1_yQek",
    "postId": 3388935980,
    "brandPost": true,
    "createdTime": 1591073979098,
    "modifiedTime": 1591073979599,
    "textEntities": {},
    "insights": {},
    "workflow": {
      "campaignId": "4706_750"
    },
    "enrichments": {
      "sentiment": 0
    }
  },
  "eventTime": 1591073978784,
  "subscriptionDetails": {
    "subscriptionId": "5e5d0302a468896782356d8f"
  }
}



### Message.Read Webhook

#### JSON Response




  Copy Code



{
  "id": "5ed5ddf2542d0e4b82325462",
  "type": "message.read",
  "payload": {
    "senderId": "919591170985",
    "receiverId": "917974027750",
    "timestamp": 1591074290276,
    "messageId": "ACCOUNT_269798_1591073978000_WHATSAPP_BUSINESS_316_gBEGkXl0AndQAgmhWI4OK1_yQek"
  },
  "eventTime": 1591074290276,
  "subscriptionDetails": {
    "subscriptionId": "5e5d0302a468896782356d8f"
  }
}



### Message.Delivered Webhook

#### JSON Response




  Copy Code



{
  "id": "5ed5ddd5542d0e4b82324fef",
  "type": "message.delivered",
  "payload": {
    "senderId": "919591170985",
    "receiverId": "917974027750",
    "timestamp": 1591074261431,
    "messageId": "ACCOUNT_269798_1591074259000_WHATSAPP_BUSINESS_316_gBEGkXl0AndQAgktF1dMgI8t9w8"
  },
  "eventTime": 1591074261431,
  "subscriptionDetails": {
    "subscriptionId": "5e5d0302a468896782356d8f"
  }
}



### Message.Publish.Failed Webhook

#### JSON Response




  Copy Code



{
  "id": "5ed5e0847934090383426ad5",
  "type": "message.publish.failed",
  "payload": {
    "postId": 3388956607,
    "error": "Media File Size is not valid"
  },
  "eventTime": 1591074948709,
  "subscriptionDetails": {
    "subscriptionId": "5e5d0302a468896782356d8f"
  }
}



### Message.Sent.For.Approval Webhook

#### JSON Response




  Copy Code



{
  "id": "5ed5fdadd2236f18f02bef28",
  "type": "message.sent.for.approval",
  "payload": {
    "id": 3389139555,
    "accountId": 328753,
    "parentMessageId": 3389139545,
    "content": {
      "text": "Quote tweet \n\nhttps://www.medium.com ",
      "attachment": {
        "url": "https://storage.googleapis.com/spr-qa6-cdn-secure/DAM/66000000/92512d8f-5b58-42b8-9c18-89526b51f0cb-246366665/SampleJPGImage_10mbmb.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gke-worker%40gc-qa6.iam.gserviceaccount.com%2F20240522%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240522T133200Z&X-Goog-Expires=5400&X-Goog-SignedHeaders=host&X-Goog-Signature=341097bc3c0a7bf65a92096e5ffd8ffa113ac066f3467e9cfd45b5d95c1afa62afeb2fc0a93b9f25622c7e45992ed279057c433016b396f38f8b226a5db54debade867934fc32cd386405d5a9d2973668d8da399e226c23e1b0da015306e4da0fb4befd091bd175d7b006988067a0ed1ee1caf46f810bf3f12d0150dcec2f16f93f08c47ea0fb7343563da5d5acb202645e39ccc692fca05b4e12322e0025dc23dd7becc7376a2029c62a008485bdcfb087aaa35ea70be78dde2a5b643a799a9bcc612633a1017aa4458c3c3fe7dce29c31d15e6275d30c99ad6e9989913fd22d71ae4370a52decb82ea22375b972f5555671e86a95581dd68588f24f5aa93af",
        "title": "Medium – Get smarter about what matters to you.",
        "description": "Medium is not like any other platform on the internet.",
        "previewImageUrl": ""https://storage.googleapis.com/spr-qa6-cdn-secure/DAM/66000000/c34134b1-148e-4376-b779-1a73d7b65ad6-246366665/SampleJPGImage_10mbmb_p.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gke-worker%40gc-qa6.iam.gserviceaccount.com%2F20240522%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240522T133200Z&X-Goog-Expires=5400&X-Goog-SignedHeaders=host&X-Goog-Signature=87dc6d84986f8c986947e3841cc54de0a1afd076b2da518b1f1351eb38138b4fef1ccafe224a82d27f9c94b2006df6689a580e0a05b8bb7178687fc249f7b5a55afa9837e404de1564f3ad8ae861423b72286eb52e020c9bdc914016b3f94f42e0e3ab06617e3b590ce8925ca2d7d8d893aacd064b7b47b318ea0a844255e4cb4f6306b345af23fbb698e09aa4b13d25e65900d102defc32d63d1e590d615394e5b6657b5b95c9ec9e7dfc060f1fa72f90326a8c687b5037b289de6e62ce57c9e077582279a0b440afe8c88f76cbc1f88ba7e39e58dc6da4eab3c7f8ff750d99877fce11d9e283e99efd15e804b7da7def69dced1e9d86bc5271c1cea7fb28f2"",
        "type": "IMAGE"
      }
    },
    "scheduleDate": 1591082410798,
    "taxonomy": {
      "campaignId": "4706_727",
      "clientCustomProperties": {  },
      "partnerCustomProperties": {  },
      "tags": [],
      "urlShortenerId": "573c40c4e4b044151f684057"
    },
    "approval": {
      "type": "APPROVAL_PATH",
      "id": "5ec81e95b4141b6c9b70e8e5"
    },
    "status": "APPROVAL"
  },
  "eventTime": 1591082412989,
  "subscriptionDetails": {
    "subscriptionId": "5e5d0302a468896782356d8f"
  }
}



### Post.Trend.Metrics.Change Webhook

To get real-time post trend updates from Sprinklr via webhook whenever the trend metrics gets updated. This would help in getting the post stats in realtime.

#### JSON Response




  Copy Code



{
  "id": "6062fcbfeab2773b84b61f17",
  "type": "post.trend.metrics.change",
  "payload": {
    "id": "POST_INSIGHTS_TREND_1617062400000_4632636223",
    "postId": 4632636223,
    "date": 1617062400000,
    "measurements": {
      "POST_REACH_COUNT_CUMULATIVE": 137,
      "TWITTER_HASHTAG_CLICKS": 0,
      "POST_COMMENT_COUNT_CUMULATIVE": 0,
      "TWITTER_UNIQUE_IMPRESSIONS": 0,
      "TWITTER_APP_INSTALL_ATTEMPTS": 0,
      "POST_SHARE_COUNT_CUMULATIVE": 0,
      "POST_REACH_COUNT": 0,
      "TWITTER_PERMALINK_CLICKS": 0,
      "TWITTER_APP_OPENS": 0,
      "TWITTER_URL_CLICKS": 0,
      "FOLLOWER_COUNT_AT_POST": 137,
      "POST_REAL_CLICK_COUNT": 0,
      "TWITTER_IMPRESSIONS": 0,
      "POST_TWITTER_REACH1_COUNT": 0,
      "TWITTER_TOTAL_ENGAGEMENTS": 0,
      "POST_TWITTER_REACH_COUNT": 0,
      "POST_TWITTER_FAVORITES_COUNT": 0,
      "TWITTER_VIDEO_VIEWS": 0,
      "POST_TWITTER_REPLIES_COUNT": 0,
      "TWITTER_EMAIL_TWEET": 0,
      "TWITTER_MEDIA_ENGAGEMENTS": 0,
      "NEUTRAL_SENTIMENT_COMMENT_COUNT": 0,
      "POST_LIKE_COUNT": 0,
      "TWITTER_DETAIL_EXPANDS": 0,
      "POSITIVE_SENTIMENT_COMMENT_COUNT": 0,
      "TWITTER_MEDIA_CLICKS": 0,
      "TWITTER_PROFILE_CLICKS": 0,
      "POST_COMMENT_COUNT": 0,
      "POST_TWITTER_RETWEETS_COUNT": 0,
      "TWITTER_USER_FOLLOWS": 0,
      "TWITTER_IMPRESSIONS_CUMULATIVE": 16,
      "POST_TWITTER_REACH2_COUNT": 0,
      "POST_SHARE_COUNT": 0,
      "TWITTER_MEDIA_VIEWS": 0,
      "NEGATIVE_SENTIMENT_COMMENT_COUNT": 0,
      "POST_LIKE_COUNT_CUMULATIVE": 0
    }
  },
  "eventTime": 1617099967735,
  "subscriptionDetails": {
    "subscriptionId": "60531af11a77607f117546cc"
  }
}




	 [](https://dev.sprinklr.com/message-webhooks)

[Back to top](https://dev.sprinklr.com/message-webhooks)
