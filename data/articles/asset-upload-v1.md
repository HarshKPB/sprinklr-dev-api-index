---
title: "Asset Upload v1"
slug: asset-upload-v1
url: https://dev.sprinklr.com/asset-upload-v1
---

# Asset Upload v1

#  POST Asset Upload v1

You can use this API call to upload content in the content store. But uploading content to the content store does not mean that you have uploaded your content into the Sprinklr Asset Manager. After uploading content to the content store, use the [Asset Create API](https://dev.sprinklr.com/asset-create-v1) to create an asset in the Sprinklr Asset Manager.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/sam/upload

**Dev Notes: **This API has a 120-second (2 minutes) hard limit. Please reach out to the Integrations Support team for large-sized assets that could take longer than 120 seconds to upload.

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

## Query Parameters















****










| Parameter | Required | Type | Description |
| --- | --- | --- | --- |
| contentType | Required | String | Avalaible content types are IMAGE, VIDEO, FILE.Example: contentType = IMAGE |
| uploadTrackerId | Required | String | A unique identifier from the client. This id is any string as long as it is unique each time.The uploadTrackerId cannot be used again once you have uploaded an asset to the content store. |

## Example - Request




 Copy Code



curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v1/sam/upload?contentType=IMAGE&uploadTrackerId=HotelPool1562034506566' \
--header 'Authorization: {Bearer token}' \
--header 'key: {API key}' \
--header 'Cookie: user.env.type=ENTERPRISE' \
--form 'file=@"/C:/Users/Sprinklr/Downloads/image.png'



## Example - Response



{
    "width": 6720,
    "height": 4480,
    "previewWidth": 720,
    "previewHeight": 480,
    "thumbnailImageWidth": 72,
    "thumbnailImageHeight": 48,
    "lowQualityImageUrl": "https://sprcdn-assets.sprinklr.com/787/C98A0320-9fcad5ab-0aa6-4e70-8d4b-3bed6bbdb369-1677822253_l_q.jpg",
    "id": "5ee9022b716f263825f0c443",
    "contentType": "IMAGE",
    "contentName": "C98A0320.jpg",
    "contentUrl": "https://sprcdn-assets.sprinklr.com/787/C98A0320-9fcad5ab-0aa6-4e70-8d4b-3bed6bbdb369-1677822253.jpg",
    "mimeType": "image/jpeg",
    "previewUrl": "https://sprcdn-assets.sprinklr.com/787/C98A0320-9fcad5ab-0aa6-4e70-8d4b-3bed6bbdb369-1677822253_p.jpg",
    "thumbnailUrl": "https://sprcdn-assets.sprinklr.com/787/C98A0320-9fcad5ab-0aa6-4e70-8d4b-3bed6bbdb369-1677822253_t.jpg",
    "modifiedTime": 1592328747942,
    "sourceUrl": "",
    "extension": "jpg",
    "sizeInBytes": 817388,
    "success": true
}



[](https://dev.sprinklr.com/asset-upload-v1) 

 

 
[Back to top](https://dev.sprinklr.com/asset-upload-v1)
