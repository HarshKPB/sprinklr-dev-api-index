---
title: "SAM Webhooks"
slug: sam-webhooks
url: https://dev.sprinklr.com/sam-webhooks
---

# SAM Webhooks

#
  SAM Webhooks

	**SAM Webhook Subscriptions:**
 Asset Created, Asset Updated, Asset Deleted

Whenever an action is performed in Sprinklr Asset Manager either via Sprinklr UI or API, the webhook notification are triggered with the details that are described in the following documents:


- [Asset.Created Webhook](https://dev.sprinklr.com/sam-webhooks#samCreate)

- [Asset.Updated Webhook](https://dev.sprinklr.com/sam-webhooks#samUpdate)

- [Asset.Deleted Webhook](https://dev.sprinklr.com/sam-webhooks#samDelete)

### Asset.Created Webhook




  Copy Code

{
  "id": "5eb422c5231b0905b88e1e0e",
  "type": "asset.created",
  "payload": {
    "id": "5eb422c5231b0905b88e1e0a",
    "name": "button asset",
    "description": "button asset",
    "assetType": "PHOTO",
    "status": "Approved",
    "attachment": {
      "url": "https://sprcdn-assets.sprinklr.com/787/acf5745d-b83b-4ad9-9db4-73f2988cba21-1150920941.png",
      "previewUrl": "https://sprcdn-assets.sprinklr.com/787/Screenshot_2020-05-04_at_8.40.-2e18d388-d602-4c04-91c9-aceaa7535616-2042906844_p.png",
      "type": "IMAGE"
    },
    "taxonomy": {
      "campaignId": "4706_750",
      "clientCustomProperties": {
      },
      "partnerCustomProperties": {
      }
    },
    "insights": {},
    "validity": {
      "expiryTime": 2208988800000,
      "availableFrom": 1588863649481,
      "neverExpire": false
    },
    "assetSource": "SPRINKLR",
    "actionStats": {},
    "shareConfigs": [
      {
        "type": "GLOBAL"
      }
    ],
    "restricted": false
  },
  "eventTime": 1588863685839,
  "subscriptionDetails": {
    "subscriptionId": "5e50dae460b4d41b5270ac8a"
  }
}



### Asset.Updated Webhook




  Copy Code

{
  "id": "5eb422df9dd9b4324f48244c",
  "type": "asset.updated",
  "payload": {
    "id": "5eb422c5231b0905b88e1e0a",
    "name": "button asset",
    "description": "button asset",
    "assetType": "PHOTO",
    "status": "Approved",
    "attachment": {
      "url": "https://sprcdn-assets.sprinklr.com/787/acf5745d-b83b-4ad9-9db4-73f2988cba21-1150920941.png",
      "previewUrl": "https://sprcdn-assets.sprinklr.com/787/Screenshot_2020-05-04_at_8.40.-2e18d388-d602-4c04-91c9-aceaa7535616-2042906844_p.png",
      "type": "IMAGE"
    },
    "taxonomy": {
      "campaignId": "4706_750",
      "clientCustomProperties": {
      },
      "partnerCustomProperties": {
    },
    "insights": {},
    "validity": {
      "expiryTime": 2208988800000,
      "availableFrom": 1588863649481,
      "neverExpire": false
    },
    "assetSource": "SPRINKLR",
    "actionStats": {},
    "shareConfigs": [
      {
        "type": "GLOBAL"
      }
    ],
    "restricted": false
  },
  "eventTime": 1588863711625,
  "subscriptionDetails": {
    "subscriptionId": "5e50dae460b4d41b5270ac8a"
  }
}



### Asset.Deleted Webhook




  Copy Code

{
  "id": "5eb42303231b0905b88e327b",
  "type": "asset.deleted",
  "payload": {
    "id": "5eb422c5231b0905b88e1e0a",
    "name": "button asset",
    "description": "button asset",
    "assetType": "PHOTO",
    "status": "Approved",
    "attachment": {
      "url": "https://sprcdn-assets.sprinklr.com/787/acf5745d-b83b-4ad9-9db4-73f2988cba21-1150920941.png",
      "previewUrl": "https://sprcdn-assets.sprinklr.com/787/Screenshot_2020-05-04_at_8.40.-2e18d388-d602-4c04-91c9-aceaa7535616-2042906844_p.png",
      "type": "IMAGE"
    },
    "taxonomy": {
      "campaignId": "4706_750",
      "clientCustomProperties": {
      },
      "partnerCustomProperties": {    },
    "insights": {},
    "validity": {
      "expiryTime": 2208988800000,
      "availableFrom": 1588863649481,
      "neverExpire": false
    },
    "assetSource": "SPRINKLR",
    "actionStats": {},
    "shareConfigs": [
      {
        "type": "GLOBAL"
      }
    ],
    "restricted": false
  },
  "eventTime": 1588863747228,
  "subscriptionDetails": {
    "subscriptionId": "5e50dae460b4d41b5270ac8a"
  }
}



### Description of Response Object




































































































































































































































| Parameter | Sub Param | Description | Type |
| --- | --- | --- | --- |
| id |  | Unique webhookId. | String |
| type |  | Id of the asset. | String |
| payload |  | Payload Object | String |
| id |  | Id of the asset. | String |
| name |  | Name of the asset. | String |
| description |  | Description of the asset. | String |
| assetType |  | The type of asset. 				ENUM:[PRESENTATION, PHOTO, VIDEO, AUDIO, FLASH, HTML, 				PDF, DOC, DOCX, EXCEL, ZIP, PSD, SKETCH, FONT] | String |
| status |  | Status of the asset. | String |
| attachment |  | Information about the attachment. |  |
|  | type | The type of attachment. 				ENUM:[Audio, Video] | String |
|  | url | Url of asset | String |
|  | previewUrl | Preview Url of the asset. | String |
| taxonomy |  | Taxonomy related to an asset |  |
|  | campaignId | Campaign identifier to associate the message to. | String |
|  | clientCustomProperties | Client custom properties for the message. | String |
|  | partnerCustomProperties | Partner custom properties for the message. | String |
| insights |  | Collective insights of the posts on social channels. e.g. likes, 				comments, shares. | Double |
| validity |  | Information regarding the validity of an asset. |  |
|  | expiryTime | Asset expiry time. This option is not valid if neverExpire is true. | Epoch |
|  | availableFrom | The asset is available from time. | Epoch |
|  | neverExpire | If True, the asset will never expire. | Boolean |
| assetSource |  | Source of the Asset. e.g. SPRINKLR, GETTY, SHUTTERSTOCK. | String |
| actionStats |  | Stats of the asset actions. e.g Download, Published. | Double |
| shareConfigs |  | Asset share configuration. |  |
|  | shareLevel | Asset share level. e.g. USER, GLOBAL, CLIENT. | String |
|  | sharedWithIds | Id based on the share-level. | String |
| restricted |  | If True, the asset is restricted from publishing. | Boolean |
| eventTime |  | Event occurring time. | Epoch |
| subscriptionDetails |  | Details about subscription |  |
|  | SubscriptionId | Webhook subscription Id. | String |

### Attachment Option Description























| Parameter | Description | Type |
| --- | --- | --- |
| channelType | ChannelType for media options. Enum:[ FACEBOOK, TWITTER ] | String |
| accountId | If the properties are specific to an account inaddition to channelType, accountId can be specified and the properties would then only be used for the given account. | Integer |

 [](https://dev.sprinklr.com/sam-webhooks)

[Back to top](https://dev.sprinklr.com/sam-webhooks)
