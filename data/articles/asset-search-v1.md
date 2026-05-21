---
title: "Asset Search v1"
slug: asset-search-v1
url: https://dev.sprinklr.com/asset-search-v1
---

# Asset Search v1

#  GET Asset Search v1

Using this API, you can search assets using sorting and filters. As a response, you will get a list of assets that matches you search request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/sam/search

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











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

### Request Parameters

[Media Asset Types](https://dev.sprinklr.com/media-asset-type)

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| filters | Required | See supported  Example: "filters": { "ASSET_TYPE": ["PHOTO"], "CLIENTS": "4"} | Map < Enum, List < String > > |
| sortList | Required | You can sort based on any attribute of the asset object Example: "sortList": { "order": "DESC", "key": "createdTime"} | List < Object > |
| keywordSearch | Optional | Search for assets with certain keywords Use AND, OR, and NOT Example: "keywordSearch": "hello OR post OR hi" | String |
| rangeCondition | Required | You can find Range Condition options in the Range Condition object. Example: "rangeCondition": { "start": 0, "fieldName": "createdTime", "end": 1424363439363} Note: To use custom field in the range condition please add "customFields." before the field name. eg "rangeCondition": {"start": 0,"fieldName": "customFields.{fieldName}","end": 1424363439363} | Object |
| onlyAvailable | Optional | Search for assets that are available (true/false) Default = false Example: "onlyAvailable": "false" | Boolean |
| start | Required | The start offset Start offset example: "A" as an array of characters containing "abcdef", the fourth element containing the character "D" has an offset of three from the start of "A". Default = 0 Example: "start": 0 | Integer |
| rows | Required | The number of rows (assets) to fetch from the start offset Default = 20 rows (assets) Example: "rows": 3 | Integer |

### Example - Request




 Copy Code



curl -X POST \
 'https://api2.sprinklr.com/{env}/api/v1/sam/search' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
   "filters":{
      "ASSET_TYPE":[
         "PHOTO"
      ]
   },
   "sortList":[
      {
         "order":"DESC",
         "key":"createdTime"
      }
   ],
   "keywordSearch":"hello OR post OR hi",
   "rangeCondition":{
      "start":0,
      "fieldName":"createdTime",
      "end":1424363439363
   },
   "onlyAvailable":false,
   "start":0,
   "rows":1
}'



### Example - Response




{
   "start":1,
   "recordCount":3,
   "socialMediaAssets":[
      {
         "id":"553e84e3e4b08aba446da98d",
         "name":"are you segregating your posts? 2015-02-08 13:5...",
         "description":"Uploaded through auto import.",
         "assetStatus":"APPROVED",
         "assetType":"PHOTO",
         "expiryTime":2208988800000,
         "availableAfterTime":1423385800000,
         "shareConfigs":[
            {
               "shareLevel":"GLOBAL"
            }
         ],
         "clientActionStats":{
            "PUBLISHED_COUNT":1
         },
         "ownerClientId":4,
         "ownerUserId":0,
         "campaignIds":[
            "4_2"
         ],
         "assetSource":"SPRINKLR",
         "autoImported":true,
         "restricted":true,
         "deleted":false,
         "createdTime":1423384000000,
         "updatedTime":1430160611653,
         "locked":false,
         "digitalAsset":{
            "mediaUrl":"http://cdata.qa-apple.sprinklr.com/DAM/3/are_you_segregating_your_posts-8cd48041-6148-48aa-8738-349b3ba9a5af-2089373192.jpg",
            "originalMediaUrl":"https://scontent.xx.fbcdn.net/hphotos-xpt1/v/t1.0-9/10920952_545365738939920_5557674369134781996_n.jpg?oh=c882e9b0c3efe66ac54490e1789645cc&oe=55DE60F9",
            "mediaMimeType":"image/jpeg",
            "previewUrl":"http://cdata.qa-apple.sprinklr.com/DAM/3/are_you_segregating_your_posts-8cd48041-6148-48aa-8738-349b3ba9a5af-2089373192_p.jpg",
            "imageHeight":210,
            "imageHeightUnit":"px",
            "imageWidth":240,
            "imageWidthUnit":"px",
            "previewImageHeight":210,
            "previewImageHeightUnit":"px",
            "previewImageWidth":240,
            "previewImageWidthUnit":"px"
         }
      }
   ]
}



[](https://dev.sprinklr.com/asset-search-v1) 

 

 
[Back to top](https://dev.sprinklr.com/asset-search-v1)
