---
title: "Post Asset"
slug: post-asset
url: https://dev.sprinklr.com/post-asset
---

# Post Asset

# Post Asset

This is used for assetType of POST.

From Web UI, POST asset can be defined with more than one channel type.  The asset content for different channels is kept separately since each channel has different characteristics, such as different max message length or number of attachments allowed.  For this reason, POST asset contains a set of attributes independent of the channels selected and then a separate set of attributes for each selected channel.  

In addition, POST asset can be created in two different ways.  It can be created from SAM or it can be from auto-imported posts from the channel.  

 

[PostAssetChannelContent](https://dev.sprinklr.com/post-asset#post_asset_channel_content)

| Fields | Type | Description |
| --- | --- | --- |
| postCommonAttachmentType | Enum | AttachmentType; this is for the post attachment independent of channels. |
| postCommonSAMIds | Set of Objects | List of AttachedMiniAsset objects which are SAM assets used as attachment to this post asset |
| postCommonContent | String | Post text content common to all channels selected |
| postAssetChannelContent | Set of Objects | for each channel selected. |
| postId | String | Applicable for auto-imported posts ; Internal postId |
| snMsgId | String | Applicable for auto-imported posts; msg Id from channel |
| postPermalink | String | Applicable for auto-imported posts; msg permalink  to channel |
| postType | Enum | STATUS, LINK, PHOTO, VIDEO, ALBUM |
| postPublishedTime | Long | Applicable for auto-imported posts; (Unix time of post published) * 1000 |
| postAccountId | Long | Applicable for auto-imported posts; the account the post was published |
| parentPostAssetId | String |  |
| textEntities | List<TextEntity> |  |
| urlEntities | List<URLEntity> |  |

## PostAssetChannelContent Object Description

****

****

****

[ChannelType](https://dev.sprinklr.com/channels-v1)

[AttachedMiniAsset](https://dev.sprinklr.com/post-asset#attached_mini_asset)

[AttachmentType](https://dev.sprinklr.com/post-asset#attachment_type)

| Fields | Type | Description |
| --- | --- | --- |
| postChannelType | Enum |  |
| postContent | String | Copyright of the post |
| postSAMAssets | Set of Objects | List of objects which are SAM assets used as attachment to this post asset |
| postAttachmentType | Enum |  |
| postAttditional | Map<String, List<String>> | Anything additional |

## AttachedMiniAsset



****

****

****

| Fields | Type | Description |
| --- | --- | --- |
| attachedSAMId | String | SAM assetId |
| mediaAssetType | Enum | MediaAssetType |
| mediaUrl | String | For Digital Asset attachment |
| mediaMimeType | String | For Digital Asset attachment |
| previewUrl | String | For Digital Asset attachment |
| imageHeight | Integer | For PHOTO Asset attachment |
| imageHightUnit | String | For PHOTO & VIDEO Asset attachment |
| imageWidth | Integer | For PHOTO Asset attachment |
| imageWidthUnit | String | For PHOTO & VIDEO Asset attachment |

## AttachmentType

This is used for the attachments for POST assets.

- PHOTO

- VIDEO

- LINK

- ALBUM

- PDF

- DOCUMENT

- PRESENTATION

- MIXED

- AUDIO

## Example - POST

Search for POST asset.

### Example - Request















Copy Code


 curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v1/sam/search'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
  -d'{
  "filters": {
    "ASSET_TYPE": [
      "POST"
    ]
  },
  "sortList": [
    {
      "order": "DESC",
      "key": "createdTime"
    }
  ],
  "keywordSearch": "hello OR post OR hi",
  "rangeCondition": {
    "start": 0,
    "fieldName": "createdTime",
    "end": 1424363439363
  },
  "onlyAvailable": false,
  "start": 0,
  "rows": 2
}'






### Example - Response





{
"start": 2,
  "recordCount": 151659,
  "socialMediaAssets": [
    {
      "id": "54e60fade4b02c476fcb7411",
      "name": "works well 2015-02-19 21:58:36.584 ; Now",
      "description": "Uploaded through publisher.",
      "assetStatus": "APPROVED",
      "assetType": "POST",
      "expiryTime": 2208988800000,
      "availableAfterTime": 1424365237000,
      "shareConfigs": [
        {
          "shareLevel": "GLOBAL"
        }
      ],
      "clientActionStats": {
        "PUBLISHED_COUNT": 1.0
      },
      "ownerClientId": 186,
      "ownerUserId": 2026,
      "campaignIds": [
        "186_2"
      ],
      "assetSource": "SPRINKLR",
      "autoImported": true,
      "restricted": false,
      "deleted": false,
      "createdTime": 1424363437000,
      "updatedTime": 1424363437491,
      "locked": false,
      "postAsset": {
        "postId": "3998015",
        "snMsgId": "550325261777301",
        "postType": "PHOTO",
        "postPermalink": "https://www.facebook.com/photo.php?fbid\u003d550325261777301",
        "postPublishedTime": 1424363437000,
        "postAssetChannelContent": [
          {
            "postChannelType": "FACEBOOK",
            "postContent": "works well 2015-02-19 21:58:36.584 ; Now",
            "postSAMAssets": [
            ],
            "postAttachmentType": "PHOTO",
            "postAdditional": {
              "REQUEST_SOURCE": [
                "UI"
              ],
              "RETRY_COUNT": [
                "1"
              ],
              "dirty": [
                "true"
              ],
              "CLIENT_IP_ADDRESS": [
                "10.0.0.195"
              ]
            }
          }
        ],
        "postAccountId": 2616
      }
    },
    {
      "id": "54e60fa7e4b02c476fcb7238",
      "name": "her faith upheld her in that time of sadness 20...",
      "description": "Uploaded through publisher.",
      "assetStatus": "APPROVED",
      "assetType": "POST",
      "expiryTime": 2208988800000,
      "availableAfterTime": 1424365231000,
      "shareConfigs": [
        {
          "shareLevel": "GLOBAL"
        }
      ],
      "clientActionStats": {
        "PUBLISHED_COUNT": 1.0
      },
      "ownerClientId": 186,
      "ownerUserId": 2026,
      "campaignIds": [
        "186_2"
      ],
      "assetSource": "SPRINKLR",
      "autoImported": true,
      "restricted": false,
      "deleted": false,
      "createdTime": 1424363431000,
      "updatedTime": 1424363431870,
      "locked": false,
      "postAsset": {
        "postId": "3998009",
        "snMsgId": "215244391952058_550325241777303",
        "postType": "STATUS",
        "postPermalink": "https://www.facebook.com/215244391952058/posts/550325241777303",
        "postPublishedTime": 1424363431000,
        "postAssetChannelContent": [
          {
            "postChannelType": "FACEBOOK",
            "postContent": "her faith upheld her in that time of sadness 2015-02-19 21:59:23.658 ; Now",
            "postSAMAssets": [
            ],
            "postAdditional": {
              "REQUEST_SOURCE": [
                "UI"
              ],
              "RETRY_COUNT": [
                "1"
              ],
              "dirty": [
                "true"
              ],
              "CLIENT_IP_ADDRESS": [
                "10.0.0.132"
              ]
            }
          }
        ],
        "postAccountId": 2616
      }
    }
  ]
}







[](https://dev.sprinklr.com/post-asset) 

 

 
[Back to top](https://dev.sprinklr.com/post-asset)
