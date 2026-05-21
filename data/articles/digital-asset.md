---
title: "Digital Asset"
slug: digital-asset
url: https://dev.sprinklr.com/digital-asset
---

# Digital Asset

# Digital Asset

This is used for assetType of PHOTO, VIDEO, DOC, EXCEL, PDF, etc.

| Fields | Type | Description |
| --- | --- | --- |
| mediaUrl | String |  |
| originalMediaUrl | String |  |
| mediaMimeType | String |  |
| previewUrl | String |  |
| imageHightUnit | String |  |
| imageWidthUnit | String |  |
| previewImageHightUnit | String |  |
| previewImageWidthUnit | String |  |
| imageHeight | Integer | For PHOTO assetType |
| imageWidth | Integer | For PHOTO assetType |
| previewImageHeight | Integer | For PHOTO assetType |
| previewImageWidth | Integer | For PHOTO assetType |
| sizeInBytes | Integer |  |
| digitalAssetHash | String |  |

## Example - PHOTO

Search for PHOTO asset type, EXPIRED status and keyword search of “hello”,”post”,”hi”.

## Example - Request















Copy Code



curl -X POST \
  'https://api3.sprinklr.com/api/v1/sam/search' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'key: {apikey}'
  -d'{
  "filters": {
    "ASSET_TYPE": [
      "PHOTO"
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
  "rows": 1
}'






### Example - Response




 {
  "start": 1,
  "recordCount": 107,
  "socialMediaAssets": [
    {
      "id": "54d3a03be4b0dba76ac12755",
      "name": "did you post that? 2015-02-05 22:19:43.591 ; Now",
      "description": "Uploaded through publisher.",
      "assetStatus": "APPROVED",
      "assetType": "PHOTO",
      "expiryTime": 2208988800000,
      "availableAfterTime": 1423157057000,
      "shareConfigs": [
        {
          "shareLevel": "GLOBAL"
        }
      ],
      "reportingStats": {
        "COMMENTS": 0.,
        "ENGAGEMENT_METRICS": 0,
        "FB_COMMENTS": 0,
        "FB_ENGAGEMENT_METRICS": 0,
        "FB_FANS": 6,
        "FB_IMPRESSIONS": 0,
        "FB_LIKES": 0,
        "FB_PEOPLE_TALK_ABOUT_THIS": 0,
        "FB_POST_CONSUMPTIONS": 0,
        "FB_POST_CONSUMPTIONS_UNIQUE": 0,
        "FB_POST_ENGAGED_USERS": 0,
        "FB_POST_IMPRESSIONS_FAN": 0,
        "FB_POST_IMPRESSIONS_FAN_PAID": 0,
        "FB_POST_IMPRESSIONS_FAN_PAID_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_FAN_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_ORGANIC": 0,
        "FB_POST_IMPRESSIONS_ORGANIC_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_PAID": 0,
        "FB_POST_IMPRESSIONS_PAID_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_VIRAL": 0,
        "FB_POST_IMPRESSIONS_VIRAL_UNIQUE": 0,
        "FB_POST_NEGATIVE_FEEDBACK": 0,
        "FB_POST_NEGATIVE_FEEDBACK_UNIQUE": 0,
        "FB_POST_STORIES": 0,
        "FB_REACHES": 0,
        "FB_SHARES": 0,
        "FOLLOWERS": 6,
        "LIKES": 0,
        "REACH": 0,
        "SHARES": 0,
        "TOTAL_ENGAGEMENT": 0
      },
      "clientActionStats": {
        "PUBLISHED_COUNT": 4
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
      "createdTime": 1423155257000,
      "updatedTime": 1424332749046,
      "locked": false,
      "digitalAsset": {
        "mediaUrl": "http://cdata.nqa.sprinklr.com/DAM/45/http___www.jpl.nasa.gov_spacei-20fa230c-0883-4889-937c-a443461e8930-301702548.jpg",
        "originalMediaUrl": "http://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA17011_ip.jpg",
        "mediaMimeType": "image/jpeg",
        "previewUrl": "http://cdata.nqa.sprinklr.com/DAM/45/http___www.jpl.nasa.gov_spacei-20fa230c-0883-4889-937c-a443461e8930-301702548_p.jpg",
        "imageHeight": 600.0,
        "imageHeightUnit": "px",
        "imageWidth": 600.0,
        "imageWidthUnit": "px",
        "previewImageHeight": 600.0,
        "previewImageHeightUnit": "px",
        "previewImageWidth": 600.0,
        "previewImageWidthUnit": "px"
      }
    }
  ]
}






## Example - VIDEO















Copy Code



curl -X POST \
  'https://api3.sprinklr.com/api/v1/sam/search' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'key: {apikey}'
  -d'{
  "filters": {
    "ASSET_TYPE": [
      "VIDEO"
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
  "rows": 4
}'






### Example - Response




 {
  "start": 4,
  "recordCount": 7234,
  "socialMediaAssets": [
    {
      "id": "54e5bc64e4b0fc102c0bac3d",
      "name": "MyUpdated Video",
      "description": "Updated from external api__1424348676329",
      "assetStatus": "APPROVED",
      "assetType": "VIDEO",
      "expiryTime": 2208988800000,
      "availableAfterTime": 1424304000000,
      "shareConfigs": [
        {
          "shareLevel": "GLOBAL"
        }
      ],
      "reportingStats": {
        "COMMENTS": 0,
        "ENGAGEMENT_METRICS": 0,
        "FB_COMMENTS": 0,
        "FB_ENGAGEMENT_METRICS": 0,
        "FB_FANS": 3,
        "FB_IMPRESSIONS": 0,
        "FB_LIKES": 0,
        "FB_PEOPLE_TALK_ABOUT_THIS": 0,
        "FB_POST_CONSUMPTIONS": 0,
        "FB_POST_CONSUMPTIONS_UNIQUE": 0,
        "FB_POST_ENGAGED_USERS": 0,
        "FB_POST_IMPRESSIONS_FAN": 0,
        "FB_POST_IMPRESSIONS_FAN_PAID": 0,
        "FB_POST_IMPRESSIONS_FAN_PAID_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_FAN_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_ORGANIC": 0,
        "FB_POST_IMPRESSIONS_ORGANIC_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_PAID": 0,
        "FB_POST_IMPRESSIONS_PAID_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_VIRAL": 0,
        "FB_POST_IMPRESSIONS_VIRAL_UNIQUE": 0,
        "FB_POST_NEGATIVE_FEEDBACK": 0,
        "FB_POST_NEGATIVE_FEEDBACK_UNIQUE": 0,
        "FB_POST_STORIES": 0,
        "FB_POST_VIDEO_AVG_TIME_WATCHED": 0,
        "FB_POST_VIDEO_COMPLETE_VIEWS_ORGANIC": 0,
        "FB_POST_VIDEO_COMPLETE_VIEWS_ORGANIC_UNIQUE": 0,
        "FB_POST_VIDEO_COMPLETE_VIEWS_PAID": 0,
        "FB_POST_VIDEO_COMPLETE_VIEWS_PAID_UNIQUE": 0,
        "FB_POST_VIDEO_LENGTH": 0,
        "FB_POST_VIDEO_VIEWS_ORGANIC": 0,
        "FB_POST_VIDEO_VIEWS_ORGANIC_UNIQUE": 0,
        "FB_POST_VIDEO_VIEWS_PAID": 0,
        "FB_POST_VIDEO_VIEWS_PAID_UNIQUE": 0,
        "FB_REACHES": 0,
        "FB_SHARES": 0,
        "FOLLOWERS": 3,
        "LIKES": 0,
        "REACH": 0,
        "SHARES": 0,
        "TOTAL_ENGAGEMENT": 0
      },
      "clientActionStats": {
        "PUBLISHED_COUNT": 1
      },
      "ownerClientId": 208,
      "ownerUserId": 2065,
      "partnerCustomFields": {
      },
      "assetSource": "SPRINKLR",
      "autoImported": false,
      "restricted": true,
      "deleted": false,
      "createdTime": 1424342116486,
      "updatedTime": 1424418145586,
      "locked": false,
      "digitalAsset": {
        "mediaUrl": "http://cdata.nqa.sprinklr.com/DAM/45/66958aef-21fc-426b-929d-088c0be76afe-1658720739.mp4",
        "originalMediaUrl": "http://cdata.nqa.sprinklr.com/DAM/45/66958aef-21fc-426b-929d-088c0be76afe-1658720739.mp4",
        "imageHeightUnit": "px",
        "imageWidthUnit": "px",
        "previewImageHeightUnit": "px",
        "previewImageWidthUnit": "px"
      }
    },
    {
      "id": "54e5bc32e4b0fc102c0ba869",
      "name": "Video 20150219103422374",
      "description": "Video Desc 3423361",
      "assetStatus": "APPROVED",
      "assetType": "VIDEO",
      "expiryTime": 2208988800000,
      "availableAfterTime": 1424304000000,
      "shareConfigs": [
        {
          "shareLevel": "GLOBAL"
        }
      ],
      "reportingStats": {
        "COMMENTS": 0,
        "ENGAGEMENT_METRICS": 0,
        "FB_COMMENTS": 0,
        "FB_ENGAGEMENT_METRICS": 0,
        "FB_FANS": 1,
        "FB_IMPRESSIONS": 0,
        "FB_LIKES": 0,
        "FB_PEOPLE_TALK_ABOUT_THIS": 0,
        "FB_POST_CONSUMPTIONS": 0,
        "FB_POST_CONSUMPTIONS_UNIQUE": 0,
        "FB_POST_ENGAGED_USERS": 0,
        "FB_POST_IMPRESSIONS_FAN": 0,
        "FB_POST_IMPRESSIONS_FAN_PAID": 0,
        "FB_POST_IMPRESSIONS_FAN_PAID_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_FAN_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_ORGANIC": 0,
        "FB_POST_IMPRESSIONS_ORGANIC_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_PAID": 0,
        "FB_POST_IMPRESSIONS_PAID_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_VIRAL": 0,
        "FB_POST_IMPRESSIONS_VIRAL_UNIQUE": 0,
        "FB_POST_NEGATIVE_FEEDBACK": 0,
        "FB_POST_NEGATIVE_FEEDBACK_UNIQUE": 0,
        "FB_POST_STORIES": 0,
        "FB_POST_VIDEO_AVG_TIME_WATCHED": 0,
        "FB_POST_VIDEO_COMPLETE_VIEWS_ORGANIC": 0,
        "FB_POST_VIDEO_COMPLETE_VIEWS_ORGANIC_UNIQUE": 0,
        "FB_POST_VIDEO_COMPLETE_VIEWS_PAID": 0,
        "FB_POST_VIDEO_COMPLETE_VIEWS_PAID_UNIQUE": 0,
        "FB_POST_VIDEO_LENGTH": 0,
        "FB_POST_VIDEO_VIEWS_ORGANIC": 0,
        "FB_POST_VIDEO_VIEWS_ORGANIC_UNIQUE": 0,
        "FB_POST_VIDEO_VIEWS_PAID": 0,
        "FB_POST_VIDEO_VIEWS_PAID_UNIQUE": 0,
        "FB_REACHES": 0,
        "FB_SHARES": 0,
        "FOLLOWERS": 1,
        "LIKES": 0,
        "REACH": 0,
        "SHARES": 0,
        "TOTAL_ENGAGEMENT": 0
      },
      "clientActionStats": {
        "PUBLISHED_COUNT": 1
      },
      "ownerClientId": 186,
      "ownerUserId": 2026,
      "partnerCustomFields": {
      },
      "clientCustomProperties": {
      },
      "assetSource": "SPRINKLR",
      "autoImported": false,
      "restricted": false,
      "deleted": false,
      "createdTime": 1424342066988,
      "updatedTime": 1424418145306,
      "locked": false,
      "digitalAsset": {
        "mediaUrl": "http://cdata.nqa.sprinklr.com/DAM/45/c6154dc1-89be-4191-92a9-754c1b730935-1661498087.flv",
        "originalMediaUrl": "http://cdata.nqa.sprinklr.com/DAM/45/c6154dc1-89be-4191-92a9-754c1b730935-1661498087.flv",
        "imageHeightUnit": "px",
        "imageWidthUnit": "px",
        "previewImageHeightUnit": "px",
        "previewImageWidthUnit": "px"
      }
    },
    {
      "id": "54e5bc2de4b0fc102c0ba7d3",
      "name": "Video 20150219103413345",
      "description": "Video Desc 3414649",
      "assetStatus": "APPROVED",
      "assetType": "VIDEO",
      "expiryTime": 2208988800000,
      "availableAfterTime": 1424304000000,
      "shareConfigs": [
        {
          "shareLevel": "GLOBAL"
        }
      ],
      "ownerClientId": 186,
      "ownerUserId": 2026,
      "partnerCustomFields": {
      },
      "clientCustomProperties": {
      },
      "assetSource": "SPRINKLR",
      "autoImported": false,
      "restricted": false,
      "deleted": false,
      "createdTime": 1424342061476,
      "updatedTime": 1424342061476,
      "locked": false,
      "digitalAsset": {
        "mediaUrl": "http://cdata.nqa.sprinklr.com/DAM/45/65b591c2-cbc0-4ff9-b0b6-2a1847e26b88-1658720739.mp4",
        "originalMediaUrl": "http://cdata.nqa.sprinklr.com/DAM/45/65b591c2-cbc0-4ff9-b0b6-2a1847e26b88-1658720739.mp4",
        "imageHeightUnit": "px",
        "imageWidthUnit": "px",
        "previewImageHeightUnit": "px",
        "previewImageWidthUnit": "px"
      }
    },
    {
      "id": "54e5bc2ae4b0fc102c0ba799",
      "name": "Video 20150219103413222",
      "description": "Video Desc 3413786",
      "assetStatus": "APPROVED",
      "assetType": "VIDEO",
      "expiryTime": 2208988800000,
      "availableAfterTime": 1424304000000,
      "shareConfigs": [
        {
          "shareLevel": "GLOBAL"
        }
      ],
      "reportingStats": {
        "COMMENTS": 0,
        "ENGAGEMENT_METRICS": 0,
        "FB_COMMENTS": 0,
        "FB_ENGAGEMENT_METRICS": 0,
        "FB_FANS": 4,
        "FB_IMPRESSIONS": 0,
        "FB_LIKES": 0,
        "FB_PEOPLE_TALK_ABOUT_THIS": 0,
        "FB_POST_CONSUMPTIONS": 0,
        "FB_POST_CONSUMPTIONS_UNIQUE": 0,
        "FB_POST_ENGAGED_USERS": 0,
        "FB_POST_IMPRESSIONS_FAN": 0,
        "FB_POST_IMPRESSIONS_FAN_PAID": 0,
        "FB_POST_IMPRESSIONS_FAN_PAID_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_FAN_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_ORGANIC": 0,
        "FB_POST_IMPRESSIONS_ORGANIC_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_PAID": 0,
        "FB_POST_IMPRESSIONS_PAID_UNIQUE": 0,
        "FB_POST_IMPRESSIONS_VIRAL": 0,
        "FB_POST_IMPRESSIONS_VIRAL_UNIQUE": 0,
        "FB_POST_NEGATIVE_FEEDBACK": 0,
        "FB_POST_NEGATIVE_FEEDBACK_UNIQUE": 0,
        "FB_POST_STORIES": 0,
        "FB_POST_VIDEO_AVG_TIME_WATCHED": 0,
        "FB_POST_VIDEO_COMPLETE_VIEWS_ORGANIC": 0,
        "FB_POST_VIDEO_COMPLETE_VIEWS_ORGANIC_UNIQUE": 0,
        "FB_POST_VIDEO_COMPLETE_VIEWS_PAID": 0,
        "FB_POST_VIDEO_COMPLETE_VIEWS_PAID_UNIQUE": 0,
        "FB_POST_VIDEO_LENGTH": 0,
        "FB_POST_VIDEO_VIEWS_ORGANIC": 0,
        "FB_POST_VIDEO_VIEWS_ORGANIC_UNIQUE": 0,
        "FB_POST_VIDEO_VIEWS_PAID": 0,
        "FB_POST_VIDEO_VIEWS_PAID_UNIQUE": 0,
        "FB_REACHES": 0,
        "FB_SHARES": 0,
        "FOLLOWERS": 4,
        "LIKES": 0,
        "REACH": 0,
        "SHARES": 0,
        "TOTAL_ENGAGEMENT": 0
      },
      "clientActionStats": {
        "PUBLISHED_COUNT": 2
      },
      "ownerClientId": 186,
      "ownerUserId": 2026,
      "partnerCustomFields": {
      },
      "clientCustomProperties": {
      },
      "assetSource": "SPRINKLR",
      "autoImported": false,
      "restricted": false,
      "deleted": false,
      "createdTime": 1424342058113,
      "updatedTime": 1424418145518,
      "locked": false,
      "digitalAsset": {
        "mediaUrl": "http://cdata.nqa.sprinklr.com/DAM/45/8ba97097-7282-4d8a-8154-9baf1d3a3d14-1658720739.mp4",
        "originalMediaUrl": "http://cdata.nqa.sprinklr.com/DAM/45/8ba97097-7282-4d8a-8154-9baf1d3a3d14-1658720739.mp4",
        "imageHeightUnit": "px",
        "imageWidthUnit": "px",
        "previewImageHeightUnit": "px",
        "previewImageWidthUnit": "px"
      }
    }
  ]
}






[](https://dev.sprinklr.com/digital-asset) 

 

 
[Back to top](https://dev.sprinklr.com/digital-asset)
