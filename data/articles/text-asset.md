---
title: "Text Asset"
slug: text-asset
url: https://dev.sprinklr.com/text-asset
---

# Text Asset

# Text Asset

This is used for assetType of TEXT.

| Fields | Type | Description |
| --- | --- | --- |
| text | String | This assetType helps search a text asset |

## Example – TEXT

This is for TEXT asset.

## Example - Request















Copy Code


curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/sam/search' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -d'{
  "filters": {
    "ASSET_TYPE": [
      "TEXT"
    ]
  },
  "sortList": [
    {
      "order": "DESC",
      "key": "createdTime"
    }
  ],
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
  "recordCount": 3265,
  "socialMediaAssets": [
    {
      "id": "54e5bd0ce4b0fc102c0bb604",
      "name": "MyupdateText",
      "description": "Updated from external api__1424348672422",
      "assetStatus": "EXPIRED",
      "assetType": "TEXT",
      "expiryTime": 1424367420000,
      "availableAfterTime": 1424304000000,
      "shareConfigs": [
        {
          "shareLevel": "GLOBAL"
        }
      ],
      "ownerClientId": 186,
      "ownerUserId": 2027,
      "partnerCustomFields": {
      },
      "clientCustomProperties": {
      },
      "assetSource": "SPRINKLR",
      "autoImported": false,
      "restricted": true,
      "deleted": false,
      "createdTime": 1424342284472,
      "updatedTime": 1424417993718,
      "locked": false,
      "textAsset": {
        "text": "that puppy is so cute 2015-02-19 10:37:25.107 ; Now"
      }
    },
    {
      "id": "54e5bd0be4b0fc102c0bb5f9",
      "name": "Plain Text 20150219103727733",
      "description": "Plain Text Description 3728362",
      "assetStatus": "EXPIRED",
      "assetType": "TEXT",
      "expiryTime": 1424367420000,
      "availableAfterTime": 1424304000000,
      "shareConfigs": [
        {
          "shareLevel": "GLOBAL"
        }
      ],
      "ownerClientId": 186,
      "ownerUserId": 2027,
      "partnerCustomFields": {
      },
      "clientCustomProperties": {
      },
      "assetSource": "SPRINKLR",
      "autoImported": false,
      "restricted": false,
      "deleted": false,
      "createdTime": 1424342283832,
      "updatedTime": 1424417993718,
      "locked": false,
      "textAsset": {
        "text": "this is difficult 2015-02-19 10:37:27.31 ; Now"
      }
    }
  ]
}







[](https://dev.sprinklr.com/text-asset) 

 

 
[Back to top](https://dev.sprinklr.com/text-asset)
