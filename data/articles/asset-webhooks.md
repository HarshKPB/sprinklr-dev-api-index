---
title: "Asset Webhooks"
slug: asset-webhooks
url: https://dev.sprinklr.com/asset-webhooks
---

# Asset Webhooks

# Asset Webhooks

**Asset Webhook Subscriptions:**
 Asset Created, Asset Updated and Asset Deleted

Whenever an action is performed on Assets either via Sprinklr UI or API, the webhook notification are triggered with the details that are described in the following documents:


- [Asset.Created Webhook](https://dev.sprinklr.com/asset-webhooks#assetCreate)

- [Asset.Updated Webhook](https://dev.sprinklr.com/asset-webhooks#assetUpdate)

- [Asset.Deleted Webhook](https://dev.sprinklr.com/asset-webhooks#assetDelete)

### Asset.Created Webhook




  Copy Code



{
  "id": "5f61ebe4b28a0d05d53b2573",
  "type": "asset.created",
  "payload": {
    "id": "5f61ebe4b28a0d05d53b2570",
    "name": "Publishing API2 POST on Facebook Page with video attachment",
    "description": "",
    "assetType": "VIDEO",
    "status": "Approved",
    "attachment": {
      "url": "https://sprcdn-assets.sprinklr.com/787/f415961c-9929-45a0-8dc6-8724f9784723-2085827763/https___prod-media-proxy.sprin.mp4",
      "previewUrl": "https://prod-media.sprinklr.com/channel/data/media/787/0089a882-3e1c-4128-93ce-7f7573dfecdc.jpg",
      "type": "VIDEO"
    },
    "taxonomy": {
      "campaignId": "4700_2"
    },
    "insights": {},
    "validity": {
      "expiryTime": 2208988800000,
      "availableFrom": 1600254677000,
      "neverExpire": false
    },
    "assetSource": "SPRINKLR",
    "actionStats": {},
    "shareConfigs": [
      {
        "type": "CLIENT",
        "ids": [
          "4700"
        ]
      }
    ],
    "restricted": false
  },
  "eventTime": 1600252900271,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf57e0a2"
  }
}





### Asset.Updated Webhook




  Copy Code



{
  "id": "5f61ead1dfe835394cd69950",
  "type": "asset.updated",
  "payload": {
    "id": "5f61ead018df7c62259d5de7",
    "name": "Publishing API2 POST on Facebook Page with video attachment",
    "description": "",
    "assetType": "VIDEO",
    "status": "Approved",
    "attachment": {
      "url": "https://sprcdn-assets.sprinklr.com/787/3895ca8e-a564-4017-a5a3-5cbecd46abc4-1795648788/https___prod-media-proxy.sprin.mp4",
      "previewUrl": "https://prod-media.sprinklr.com/channel/data/media/787/91401d80-60f2-47e4-b869-b84a070e7813.jpg",
      "type": "VIDEO"
    },
    "taxonomy": {
      "campaignId": "4700_2"
    },
    "insights": {},
    "validity": {
      "expiryTime": 2208988800000,
      "availableFrom": 1600254403000,
      "neverExpire": false
    },
    "assetSource": "SPRINKLR",
    "actionStats": {},
    "shareConfigs": [
      {
        "type": "CLIENT",
        "ids": [
          "4700"
        ]
      }
    ],
    "restricted": false
  },
  "eventTime": 1600252625976,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf57e0a2"
  }
}





### Asset.Deleted Webhook




  Copy Code



{
  "id": "5f6b230bc2bf3170009bda5f",
  "type": "asset.deleted",
  "payload": {
    "id": "5f6b225b1e627b218f7fd73d",
    "name": "Video post ",
    "description": "",
    "assetType": "VIDEO",
    "status": "Approved",
    "attachment": {
      "url": "https://sprcdn-assets.sprinklr.com/787/b5328ee1-b3b0-46bd-a426-8bb0a3fa3248-346148661.mp4",
      "previewUrl": "https://sprcdn-assets.sprinklr.com/787/c7fab287-8f50-4124-8b0a-f054ff4cafdf-1669757000/preview_image_0-b5328ee1-b3b0-.png",
      "type": "VIDEO"
    },
    "taxonomy": {
      "campaignId": "4706_623",
      "clientCustomProperties": { },
      "partnerCustomProperties": {
        "5e9677d8044204326c0fa736": [],
        "5e967841044204326c0fb327": [],
      },
      "tags": [
        "noo"
      ]
    },
    "insights": {},
    "validity": {
      "expiryTime": 2208988800000,
      "availableFrom": 1600858465925,
      "neverExpire": false
    },
    "assetSource": "SPRINKLR",
    "actionStats": {},
    "shareConfigs": [
      {
        "type": "CLIENT",
        "ids": [
          "4700"
        ]
      }
    ],
    "restricted": false
  },
  "eventTime": 1600856843406,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf57e0a2"
  }
}





### Response Definition


























































































































































































| Parameter | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Id of the asset. | String |
| name |  | Name of the asset. | String |
| description |  | Description of asset. | String |
| assetType |  | The type of asset.ENUM:[PRESENTATION, PHOTO, VIDEO, AUDIO, FLASH, HTML, PDF, DOC, DOCX, EXCEL, ZIP, PSD, SKETCH, FONT] | String |
| status |  | Status of the asset. | String |
| attachment |  | The object containing details about the attachment. |  |
|  | type | The type of attachment.ENUM:[Audio, Video] | String |
|  | attachmentOptions | Array of attachment properties per channel and/or account.ChannelSpecificMediaProperties. |  |
|  | channelType | ChannelType for media options. Enum:[ FACEBOOK, TWITTER ] | String |
|  | accountId | If the properties are specific to an account inaddition to channelType, accountId can be specified and the properties would then only be used for the given account. | Integer |
| taxonomy |  | The object containing details related to asset taxonomy |  |
|  | campaignId | Campaign identifier to associate the message to. | String |
|  | clientCustomProperties | Client custom properties for the message. | String |
|  | partnerCustomProperties | Partner custom properties for the message. | String |
|  | tags | Tags to be added to the message. | String |
|  | urlShortnerId | Url shortner identifier to apply to the message. | String |
| insights |  | Collective insights of the posts on social channels. e.g. likes, comments, shares. | Double |
| validity |  | This object contains Information regarding the validity of an asset. |  |
|  | expiryTime | Asset expiry time. This option is not valid if neverExpire is true. | Integer |
|  | availableFrom | Asset is available from time. | Integer |
|  | neverExpire | If True, asset will never expire. | Boolean |
| parentId |  | Parent Asset Id. | String |
| assetSource |  | Source of the Asset. e.g. SPRINKLR, GETTY, SHUTTERSTOCK. | String |
| actionStats |  | Stats of the asset actions. e.g Download, Published. | Double |
| shareConfigs |  | The object containing details of Asset share confinguration. |  |
|  | shareLevel | Asset share level. e.g. USER, GLOBAL, CLIENT. | String |
|  | sharedWithIds | Id based on shareLevel. | String |
| restricted |  | If True, asset is restricted from publishing. | Boolean |

[](https://dev.sprinklr.com/asset-webhooks)

[Back to top](https://dev.sprinklr.com/asset-webhooks)
