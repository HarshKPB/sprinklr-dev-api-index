---
title: "Asset Import Async v1"
slug: asset-import-async-v1
url: https://dev.sprinklr.com/asset-import-async-v1
---

# Asset Import Async v1

#  POST & GET  Asset Import Async v1

The asset import async API helps you import an asset via URL. Here, the first step involves importing the asset, which will fetch the task Id in response. Using the task Id, you can use the status check API to fetch the uploaded content Id. Finally, you can use the [SAM asset create](https://dev.sprinklr.com/create-asset)API to create an asset in Sprinklr Asset Manager.

The two steps for asset import async involve:

- [Import via url to get Task Id](https://dev.sprinklr.com/asset-import-async-v1/)

- [Check the status via Task Id](https://dev.sprinklr.com/asset-import-async-v1/)


**Dev Notes: ****Things to know when using the asset import async API:**

- There is no size limitation when using asset import async API

- The processing time for importing the asset depends on its size

- It is recommended to periodically check the status of the import

- The asset import API will continue running until the import is successful

## 1. Import via url to get Task Id

This will provide us the task Id of asset upload task.

## API Endpoint

`POST`
https://api3.sprinklr.com`/{env}/`api/v1/sam/importUrl/async

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

## Query Parameters

The following table describes the Query Parameters in use.







| Query Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| importType | Required | The type of import. | String |
| url | Required | The URL of the content that you want to import. | String |
| uploadTrackerId | Required | The unique id entered by user. | String |

## Example - Request




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/sam/importUrl/async?importType=VIDEO&url=https://storage.googleapis.com/livenew.mp4&uploadTrackerId=1234987872we3235' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'key: {apikey}'



## Example - Response




5efab978baa8317829b91384



### Response Definition







``

| Parameter | Description | Type |
| --- | --- | --- |
| 5efab978baa8317829b91384 | taskId | String |

## 2. Check the status via Task Id

We will use the Task ID from the above call response to check the upload status of the asset and to get uploadedContentId and then we can use uploadedContentId in Asset Create API call to create a SAM asset.

### API Endpoint

`GET`
https://api3.sprinklr.com/{{env}}/api/v1/sam/task/status/{taskId}

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

## Path Parameters

The following table describes the Path Parameters in use.







| Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| taskId | Required | Refers to the task Id that you receive in the response of "import via URL" API call. | String |

## Example




 Copy Code


curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v1/sam/task/status/5efab978baa8317829b91384' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'key: {apikey}'



## Example - Response



{
    "attributes": {
        "width": "0",
        "height": "0"
    },
    "attributeObjects": {},
    "id": "5efabaeee9e5dd0001167f33",
    "contentType": "VIDEO_FROM_URL",
    "contentName": "https___storage.googleapis.com_newlive.mp4",
    "contentUrl": "https://sprcdn-assets.sprinklr.com/1787/https___storage.googleapis.com-e5ab696f-425119.mp4",
    "mimeType": "video/mp4",
    "previewUrl": "",
    "modifiedTime": 1593490158775,
    "sourceUrl": "https://storage.googleapis.com/livenew.mp4",
    "extension": "com&Expires=123&Signature=Q6s4YTXs9KR8gayfXPT1%0FLSpBCBj%2BXHcXc9Fi8bM9Eqj6HznA%3D%3D",
    "sizeInBytes": 391790029,
    "success": true
}



**Dev Notes: **Now you can assign the id ("id": "5efabaeee9e5dd0001167f33") received from the response above to `uploadedContentId` parameter in [Asset Create API call.](https://dev.sprinklr.com/asset-create-v1)

[](https://dev.sprinklr.com/asset-import-async-v1) 

 

 
[Back to top](https://dev.sprinklr.com/asset-import-async-v1)
