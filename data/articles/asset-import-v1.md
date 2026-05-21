---
title: "Asset Import v1"
slug: asset-import-v1
url: https://dev.sprinklr.com/asset-import-v1
---

# Asset Import v1

#  POST  Asset Import v1

You can use this API call to import an asset to the content store from an external link. You can import the following content types, IMAGE, VIDEO and LINK. But uploading content to the content store does not mean that you have uploaded your content into the Sprinklr Asset Manager. After uploading content to the content store, use the [Asset Create API](https://dev.sprinklr.com/asset-create-v1) to create an asset in the Sprinklr Asset Manager.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/sam/importUrl

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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Query Parameters












| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| importType | Required | Available content types: IMAGE, VIDEO, LINK, FILE If IMAGE or VIDEO is used, the content from the URL is imported. Example: contentType=IMAGE | String |
| url | Required | The URL of the asset you want to import.  This id is any string that you make up. The uploadTrackerId cannot be used again once you have uploaded an asset to the content store. Example: uploadTrackerId=anyStringThatYouMakeUp123 | String |
| uploadTrackerId | Required | A unique identifier from the client.  This id is any string that you make up. The uploadTrackerId cannot be used again once you have uploaded an asset to the content store. Example: uploadTrackerId=anyStringThatYouMakeUp123 | String |

## Example - Request




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/sam/importUrl?importType=IMAGE&url=http://www.webdesignmash.com/trial/wp-content/uploads/2012/12/christmas-wallpaper-81.jpg&uploadTrackerId=1234987872we3235' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'key: {apikey}'



## Example - Response



{
   "originalUrl":"http://www.sprinklr.com",
   "title":"Customer Experience Management (CEM) - Sprinklr",
   "description":"Sprinklr offers the only social media management system that enables global scale of social customer experience management (CEM) for the social enterprise.",
   "providerUrl":"https://www.sprinklr.com",
   "providerName":"www.sprinklr.com",
   "thumbnails":[
      {
         "url":"https://www.sprinklr.com/wp-content/uploads/2016/03/facebook_img_sprinklr_v3.png",
         "width":486,
         "height":256,
         "size":13904
      }
   ],
   "type":"html",
   "oEmbed":{
      "type":"link",
      "embedCode":""
   },
   "destinationUrl":"https://www.sprinklr.com/"
}



[](https://dev.sprinklr.com/asset-import-v1) 

 

 
[Back to top](https://dev.sprinklr.com/asset-import-v1)
