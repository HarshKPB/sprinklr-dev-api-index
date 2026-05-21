---
title: "Draft Webhooks"
slug: draft-webhooks
url: https://dev.sprinklr.com/draft-webhooks
---

# Draft Webhooks

# Draft Webhooks

**Draft Webhook Subscriptions:**
 Draft Create, Draft Updated and Draft Scheduled

Whenever a draft message is created or scheduled within Sprinklr via UI or API, the following webhook notification are triggered with the details that are described in the following documents:


- [Draft.Created Webhook](https://dev.sprinklr.com/draft-webhooks#draftCreate)

- [Draft.Updated Webhook](https://dev.sprinklr.com/draft-webhooks#draftUpdate)

- [Draft.Scheduled Webhook](https://dev.sprinklr.com/draft-webhooks#draftSchedule)

### Draft.Created Webhook




  Copy Code



{
  "id": "64882ad56bae815253176488",
  "type": "draft.created",
  "payload": {
    "id": 10324861151,
    "accountIds": [
      1360918
    ],
    "version": 0,
    "contentTemplateIds": [],
    "accountTypes": [
      "FACEBOOK"
    ],
    "variantDetails": {
      "variant": false,
      "variantParentMessageId": "MESSAGE_10324861156",
      "hasVariants": false
    },
    "content": {
     "text": "Create Draft Webhook Test",
      "attachment": {
      "url": "https://sprcdn-assets.sprinklr.com/787/08ce3d34-bf14-4be7-97be-f8a44d2b4898-637631488.jpg",
      "title": "Image Asset 1",
      "previewUrl": "https://sprcdn-assets.sprinklr.com/787/9ba11b21-00b3-48c0-a20c-40c74c80a4b3-1529617391/Image_Asset_1_p.jpg",
      "type": "IMAGE",
      "assetId": "647deb715c034a2fc33f4c41"
      }
    },
    "channelOptions": [],
    "scheduleDate": 1686645460952,
    "taxonomy": {
      "campaignId": "4706_205"
    },
    "status": "DRAFT",
    "autoResponse": false,
    "createdTime": 1686645460952,
    "modifiedTime": 1686645460952,
    "authorId": 429501
  },
  "eventTime": 1686645461307,
  "subscriptionDetails": {
    "subscriptionId": "64882a6fee94e20971539991"
  }
}





### Draft.Updated Webhook




  Copy Code



{
  "id": "602cfc7e8446b6208d939d2a",
  "type": "draft.updated",
  "payload": {
    "id": 4497935072,
    "accountIds": [
      230338
    ],
    "accountGroupIds": [],
    "version": 2,
    "contentTemplateIds": [
      "599a9f3fe4b035f0b2040994"
    ],
    "accountTypes": [
      "LINKEDIN_COMPANY"
    ],
    "variantDetails": {
      "variant": false,
      "variantParentMessageId": "MESSAGE_10325017518",
      "hasVariants": false
    },
    "content": {
      "text": "Hello There",
      "attachment": {
        "url": "https://sprcdn-assets.sprinklr.com/787/08ce3d34-bf14-4be7-97be-f8a44d2b4898-637631488.jpg",
        "title": "Image Asset",
        "previewUrl": "https://sprcdn-assets.sprinklr.com/787/9ba11b21-00b3-48c0-a20c-40c74c80a4b3-1529617391/Image_Asset_1_p.jpg",
        "type": "IMAGE",
        "assetId": "647deb715c034a2fc33f4c41"
      }
    },
    "channelOptions": [],
    "scheduleDate": 1686646604726,
    "taxonomy": {
    "campaignId": "4706_767",
    "clientCustomProperties":{},
    "partnerCustomProperties":{},
    "tags": [
        "`1234"
      ],
      "urlShortenerId": "6486f3143c9e4007418233eb"
    },
    "status": "DRAFT",
    "autoResponse": false,
    "createdTime": 1686646604726,
    "modifiedTime": 1686646940468,
    "authorId": 62379
  },
  "eventTime": 1686646940656,
  "subscriptionDetails": {
    "subscriptionId": "64882a6fee94e20971539991"
  }
}





### Draft.Scheduled Webhook




  Copy Code



{
  "id": "602d03971b04ed2a6fd1750e",
  "type": "draft.scheduled",
  "payload": {
    "draftId": 4497935072,
    "postIds": [
      4498588827
    ]
  },
  "eventTime": 1613562775274,
  "subscriptionDetails": {
    "subscriptionId": "602c9c2671d9215e2f67e0b6"
  }
}





[](https://dev.sprinklr.com/draft-webhooks)

[Back to top](https://dev.sprinklr.com/draft-webhooks)
