---
title: "Asset Read v1"
slug: asset-read-v1
url: https://dev.sprinklr.com/asset-read-v1
---

# Asset Read v1

#  GET Asset Read v1

Using this API, you retrieve the details of an existing asset from the Sprinklr Asset Manager using the unique asset Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/sam/{asset id}

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

### Path Parameters

[asset search API documentation](https://dev.sprinklr.com/asset-search-v1)

-
-
-
-

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| assetId | Required | The Id of the Asset on which you want to make a Read API call.To fetch asset Id, refer to .Alternatively, you can fetch asset Id from the UI using the following steps:Navigate to Digital Asset Manager on Sprinklr platform.Hover over to the asset you want to fetch the details for and click on the three dots in the bottom right corner.Click on "Details" from the drop down menu. A window will appear.You'll be able to see the assetId in the overview section. | List<String> |

### Example - Request




 Copy Code


curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/sam/{asset id}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'



### Example - Response



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



[](https://dev.sprinklr.com/asset-read-v1) 

 

 
[Back to top](https://dev.sprinklr.com/asset-read-v1)
