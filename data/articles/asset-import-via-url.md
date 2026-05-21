---
title: "Asset Import via Url"
slug: asset-import-via-url
url: https://dev.sprinklr.com/asset-import-via-url
---

# Asset Import via Url

#
  POST - Asset Import via Url

Using this API, you can import a media asset to the content store using the media URL. Kindly note that adding the asset to the content store doesn't imply that it is added to the Digital Asset Manager. For adding the asset to the Digital Asset Manager, you can call the [asset create](https://dev.sprinklr.com/create-asset) API.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/media/upload/url

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/getting-started)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Query Parameters

****

****

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| uploadUrl | Required | Refers to the Url of the media asset.Note: The media Url must be URL encoded | String |
| fileName | Required | Refers to the filename of the media asset file | String |
| assetType | Required | Refers to the media asset type you are trying to upload.Supported Media Types: image, video, file | String |

### Example - Request




 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/media/upload/url?uploadUrl=https%3A%2F%2Fmedia.photo.com%2Fid%2F1325772079%2Fphoto%2Fyoung-female-freelancer-works.jpg%3Fs%3D2048x2048%26w%3Dis%26k%3D20%26c%3DboOYBMsN0Yk_3QGcN3FjAYS0JE5VJGt4h3Y-wsCfWyQ%3D&fileName=Girl%20working%20on%20laptop%20and%20making%20notes&assetType=image' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
 

### Example - Response



 
{
    "data": {
        "width": 2048,
        "height": 1366,
        "previewWidth": 720,
        "previewHeight": 480,
        "id": "667e5d015dd2594ed476e521",
        "mimeType": "image/jpeg",
        "name": "Girl working on laptop and making notes.jpg",
        "url": "https://sprcdn-assets.sprinklr.com/787/e1946dc3-c221-47cf-893d-64c67adbb0b1-1406391328/Girl_working_on_laptop_and_mak.jpg",
        "previewUrl": "https://sprcdn-assets.sprinklr.com/787/e1946dc3-c221-47cf-893d-64c67adbb0b1-1406391328/Girl_working_on_laptop_and_mak_p.jpg",
        "size": 244144
    },
    "errors": []
}
 

     
     
   
 
[](https://dev.sprinklr.com/asset-import-via-url) 

 

 
[Back to top](https://dev.sprinklr.com/asset-import-via-url)
