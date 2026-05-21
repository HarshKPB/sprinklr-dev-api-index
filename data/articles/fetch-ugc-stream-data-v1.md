---
title: "Fetch UGC Stream Data v1"
slug: fetch-ugc-stream-data-v1
url: https://dev.sprinklr.com/fetch-ugc-stream-data-v1
---

# Fetch UGC Stream Data v1

#
  POST Fetch UGC Stream Data




UGC, i.e., [user-generated content](https://www.sprinklr.com/help/articles/getting-started/about-user-generated-content/633c5eed59534970b26f9a84) refers to the messages and media content posted by your audience/fans. Once the content is UGC approved, a [UGC asset](https://www.sprinklr.com/help/articles/getting-started/about-user-generated-content/633c5eed59534970b26f9a84#50c002a2-c291-4dfb-a41e-b9c319569236) is created , which can then be republished by the brand. Using this API, you can fetch UGC stream data from the respective dashboard using the column stream Id.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v1/ugc/stream/{streamId}/feed


### Headers

API headers include the mandatory information that you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameter













[Dashboard Read API](https://dev.sprinklr.com/fetch-engagement-dashboard-v1)



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {streamId} | Required | Stream Id of the column to fetch data fromYou can fetch the stream id using the | String |

### Request Parameters













****

****







****




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| start | Optional | The start offset that specifies the starting point for fetching the dataIf there is an array of characters containing "ABCDEF" — Then the character “A” would have an offset of 0, “B” would be 1 and so on.Example: If you set the start to 3 — the data will be pulled from 4th post onwards in the respective dashboard columnDefault = 0 | Integer |
| rows | Optional | The number of rows (assets) to fetch from the start offsetDefault = 20 | Integer |

## Example - Request















Copy Code


 curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/ugc/stream/62c65f59341788006966eb8e/feed' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
   "start": 0,
   "rows": 1
}'






## Example - Response





{
    "start": 1,
    "recordCount": 898563,
    "ugcAssets": [
        {
            "ugcAsset": {
                "universalProfileId": "56383b48e4b05859b41f5687",
                "profileSNId": "588615567",
                "profileScreenName": "manjea",
                "ugcStatus": "PENDING_APPROVAL_REQUEST",
                "channelType": "TWITTER",
                "sourceAccountId": 1000067673,
                "universalMessageKeyStr": "TWITTERπ2π661402520082907136πPERSISTENT_SEARCHπ-1π1446525623000π2015_11",
                "ugcStats": {},
                "clientToUserLike": {
                    "1000005610": [
                        1000054124
                    ]
                },
                "totalHashTagsUsed": 0,
                "profileFollowerCount": 0,
                "totalLikes": 1,
                "id": "56383b59e4b05859b41f5701",
                "name": "Something new! https://t.co/5EKsGgmjX7 https://...",
                "description": "UGC Asset",
                "assetType": "PHOTO",
                "socialAsset": {
                    "mediaUrl": "http://pz.cdata.prod0.sprinklr.com/DAM/9004/https___pbs.twimg.com_media_CS-f847cc60-d7fa-4a71-972b-5c8225f6f7e2-1593538410.jpg",
                    "originalMediaUrl": "https://pbs.twimg.com/media/CS3GFmHXAAEzqSQ.jpg",
                    "mediaMimeType": "image/jpeg",
                    "previewUrl": "http://pz.cdata.prod0.sprinklr.com/DAM/9004/https___pbs.twimg.com_media_CS-f847cc60-d7fa-4a71-972b-5c8225f6f7e2-1593538410_p.jpg",
                    "imageHeight": 322.0,
                    "imageHeightUnit": "px",
                    "imageWidth": 599.0,
                    "aspectRatio": 1.860248447204969,
                    "imageWidthUnit": "px",
                    "previewImageHeight": 322.0,
                    "previewImageHeightUnit": "px",
                    "previewImageWidth": 599.0,
                    "previewImageWidthUnit": "px"
                },
                "shareConfigs": [
                    {
                        "shareLevel": "GLOBAL"
                    }
                ],
                "ownerClientId": 1000005610,
                "clientDetails": [
                    {
                        "clientId": "1000005610"
                    },
                    {
                        "clientId": "1000005622"
                    }
                ],
                "assetSource": "SPRINKLR",
                "totalDownloadCount": 0.0,
                "totalPublishedCount": 0.0,
                "totalLikeCount": 0.0,
                "customProperties": {
                    "flatCustomProperties": [
                        "ALL"
                    ],
                    "customPropertyNames": [],
                    "mappedCustomProperties": {},
                    "mappedControllingCustomPropertyList": [],
                    "customProperties": []
                },
                "isPrivate": false,
                "ownerUserId": 1000053013,
                "createdTime": 1446525785022,
                "modifiedTime": 1449208862972,
                "lastModifiedUserId": 1000054124,
                "deleted": false,
                "canEdit": false
            }
        }
    ],
    "hasMore": true
}







	[](https://dev.sprinklr.com/fetch-ugc-stream-data-v1)






[Back to top](https://dev.sprinklr.com/fetch-ugc-stream-data-v1)
