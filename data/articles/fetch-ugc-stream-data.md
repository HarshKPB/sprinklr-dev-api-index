---
title: "Fetch UGC Stream Data"
slug: fetch-ugc-stream-data
url: https://dev.sprinklr.com/fetch-ugc-stream-data
---

# Fetch UGC Stream Data

#
  POST Fetch UGC Stream Data




UGC, i.e., [user-generated content](https://www.sprinklr.com/help/articles/getting-started/about-user-generated-content/633c5eed59534970b26f9a84) refers to the messages and media content posted by your audience/fans. Once the content is UGC approved, a [UGC asset](https://www.sprinklr.com/help/articles/getting-started/about-user-generated-content/633c5eed59534970b26f9a84#50c002a2-c291-4dfb-a41e-b9c319569236) is created , which can then be republished by the brand. Using this API, you can fetch UGC stream data from the respective dashboard using the column stream Id.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/stream/{streamId}/feed


### Headers

API headers include the mandatory information that you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


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













[Dashboard Read API](https://dev.sprinklr.com/fetch-engagement-dashboards)




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
| sortField | Optional | The field by which to sort the records. | String |
| sortOrder | Optional | The order in which to sort the records (e.g., ASC for ascending, DESC for descending) | String |

## Example - Request















Copy Code



	curl -X POST \
 'https://api3.sprinklr.com/`{env}`/api/v2/stream/66d03a2c3bd87c362c151945/feed' \
 -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
    "start": 0,
    "rows": 2,
    "sortField": "CREATED_TIME",
    "sortOrder": "DESC"
} '






## Example - Response





{
    "data": {
        "entities": [
            {
                "assetType": "POST",
                "universalProfileId": "65cca18f8283a8d966391ff3",
                "profileSNId": "7606804795998691",
                "profileScreenName": "cartier",
                "channelType": "INSTAGRAM",
                "sourceAccountId": 600056637,
                "universalMessageKeyStr": "INSTAGRAMπ320πaWdfZAG1faXRlbToxOklHTWVzc2FnZAUlEOjE3ODQxNDUxNjYxNDQ5NzU0OjM0MDI4MjM2Njg0MTcxMDMwMTI0NDI1OTUyNzc3NDcxOTg3MjU1MTozMTU0MjExNjQzNjE5Mzk1MjQwNjM2NzY5NDQwOTk1NzM3NgZDZDπACCOUNTπ600056637π1709901558000π2024_03",
                "clientToUserLike": {},
                "statusChangedBy": "SPR_-100",
                "statusChangedTime": 1723114792114,
                "snCreatedTime": 1709901558000,
                "nativeFanMessageId": "aWdfZAG1faXRlbToxOklHTWVzc2FnZAUlEOjE3ODQxNDUxNjYxNDQ5NzU0OjM0MDI4MjM2Njg0MTcxMDMwMTI0NDI1OTUyNzc3NDcxOTg3MjU1MTozMTU0MjExNjQzNjE5Mzk1MjQwNjM2NzY5NDQwOTk1NzM3NgZDZD",
                "totalHashTagsUsed": 0,
                "profileFollowerCount": 0,
                "totalLikes": 0,
                "ownerClientId": 66000002,
                "ugcStats": {
                    "LIKES": 1.0,
                    "INSTAGRAM_POST_LIKES": 1.0
                },
                "id": "66b4a52731a99312322c75a6",
                "name": "2024-08-08.8430667.151318255590085",
                "description": "UGC Asset",
                "status": "Approved",
                "taxonomy": {},
                "insights": {},
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "GLOBAL"
                    }
                ],
                "restricted": false,
                "locked": false,
                "createdTime": 1723114791717,
                "modifiedTime": 1723114792136,
                "createdByUser": 66000035
            },
            {
                "assetType": "POST",
                "universalProfileId": "6603dd69e2a3fdcbbd7bde39",
                "profileSNId": "25046866234929031",
                "profileScreenName": "rome.shaw",
                "channelType": "INSTAGRAM",
                "sourceAccountId": 600055190,
                "universalMessageKeyStr": "INSTAGRAMπ303π18037055531310281πACCOUNTπ600055190π1720681361000π2024_07",
                "clientToUserLike": {},
                "statusChangedBy": "SPR_-100",
                "statusChangedTime": 1723041661154,
                "snCreatedTime": 1720681361000,
                "totalHashTagsUsed": 0,
                "profileFollowerCount": 0,
                "totalLikes": 0,
                "ownerClientId": 66000437,
                "ugcStats": {
                    "REACH": 0.0,
                    "INSTAGRAM_POST_COMMENTS": 0.0,
                    "COMMENTS": 0.0,
                    "FOLLOWERS": 0.0,
                    "LIKES": 0.0,
                    "INSTAGRAM_POST_LIKES": 0.0
                },
                "id": "668f9eea1cbb777b0b2e0a62",
                "name": "2024-07-11.3855980.7637116395960",
                "description": "UGC Asset",
                "status": "Approved",
                "taxonomy": {},
                "insights": {},
                "assetSource": "SPRINKLR",
                "actionStats": {},
                "shareConfigs": [
                    {
                        "type": "GLOBAL"
                    }
                ],
                "restricted": false,
                "locked": false,
                "createdTime": 1720688361096,
                "modifiedTime": 1723041661249,
                "createdByUser": 66004971
            }
        ],
        "hasMore": true,
        "nextPageCursor": "6704ebff109f2d50aa695d5a"
    },
    "errors": []
}







 [](https://dev.sprinklr.com/fetch-ugc-stream-data)




[Back to top](https://dev.sprinklr.com/fetch-ugc-stream-data)
