---
title: "Media Upload"
slug: media-upload
url: https://dev.sprinklr.com/media-upload
---

# Media Upload

#
  POST Media Upload


You can use this API call to upload multiple media assets as input-stream in the content store. However, uploading media to the content store doesn’t imply that the content is uploaded to Sprinklr Social Asset Manager. After uploading content to the content store, use the [Asset Create](https://dev.sprinklr.com/create-asset) endpoint to create an asset within Sprinklr Asset Manager.

In this documentation, we will explore the following scenarios:

- Upload Media

- Upload Media in Bulk

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
| Content-Type | multipart/form-data; boundary=<calculated when request is sent> | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### 1. Upload Media

This API allows uploading a single media to Sprinklr's content store

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/media/upload

### Query Parameters






****``````






| Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| assetType | Required | The type of asset to be uploadedExample: File, Image, Video | String |
| fileName | Required | The name of the file to upload along with file extension, e.g. new.pdf | String |

### Body - Form-Data Parameters



| File | Value | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| file | Asset source | Required | Source of the uploaded media content | String |

### Example - Request















Copy Code


curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/media/upload?assetType=image&fileName=test' \
  -H 'Authorization: Bearer {token}' \
  -H 'Accept: application/json' \
  -H 'key: {apikey}'
  -F 'file=@"/Users/Desktop/TestImage1"'






### Example - Response





	{
    "data": {
        "id": "608676dbc2952f59abc797af",
        "mimeType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "name": "test-pdf121.xlsx",
        "url": "https://prod2-assets.sprinklr.com/prod2-cdata/DAM/50001/4a60e727-a731-4f66-8e9e-a87a2bbbd03d-1084902514/test-pdf121.xlsx",
        "previewUrl": "",
        "size": 15511
    },
    "errors": []
}







### 2. Uploading Media in Bulk

This API allows uploading media in bulk to Sprinklr's content store

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/media/upload/multiple

### Query Parameters

****``````


| Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| assetType | Required | The type of asset to be uploadedExample: File, Image, Video | String |

### Body - Form-Data Parameters



| File | Value | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| files | Asset Sources | Required | Sources of the uploaded media | String |

### Example - Request















Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/media/upload/multiple?assetType=file' \
  -H 'Authorization: Bearer {token}' \
  -H 'key: {apikey}' \
  -F 'files=@"/Users/Downloads/Screenshot 2022-04-26 at 2.04.01 PM.png"' \
  -F 'files=@"/Users/Downloads/Screenshot 2022-05-12 at 13.26.45.png"' \
  -F 'files=@"/Users/Desktop/Screenshot 2022-06-15 at 15.23.27.png"' \






### Example - Response





    {
   "data": [
       {
           "width": 3584,
           "height": 2240,
           "previewWidth": 720,
           "previewHeight": 450,
           "id": "62b1abe362b4f17bcf95d5c0",
           "mimeType": "image/png",
           "name": "Screenshot 2022-06-20 at 11.51.40.png",
           "url": "https://qa4-cdata-secure.sprinklr.com/DAM/400002/daf90fa6-7459-4d29-b5ce-940e7126b59e-1634145368/Screenshot_2022-06-20_at_11.51.png",
           "previewUrl": "https://qa4-cdata-secure.sprinklr.com/DAM/400002/daf90fa6-7459-4d29-b5ce-940e7126b59e-1634145368/Screenshot_2022-06-20_at_11.51_p.png",
           "size": 1379047
       },
       {
           "width": 3584,
           "height": 2240,
           "previewWidth": 720,
           "previewHeight": 450,
           "id": "62b1abe262b4f17bcf95d5bb",
           "mimeType": "image/png",
           "name": "Screenshot 2022-06-21 at 11.07.51.png",
           "url": "https://qa4-cdata-secure.sprinklr.com/DAM/400002/83e57077-d670-4d05-bad7-8fddc112c4a1-1036305582/Screenshot_2022-06-21_at_11.07.png",
           "previewUrl": "https://qa4-cdata-secure.sprinklr.com/DAM/400002/83e57077-d670-4d05-bad7-8fddc112c4a1-1036305582/Screenshot_2022-06-21_at_11.07_p.png",
           "size": 981542
       }
   ],
   "errors":[]
   }







### Response Parameters









````





````












****


















| Parameter | Description | Type |
| --- | --- | --- |
| width | Width of the uploaded contentApplicable for assetTypes: IMAGE, VIDEO | Integer |
| height | Height of the uploaded contentApplicable for assetTypes: IMAGE, VIDEO | Integer |
| previewWidth | Applicable for image asset type | Integer |
| previewHeight | Applicable for image asset type | Integer |
| id | Unique identifier for the uploaded content | String |
| mimeType | Provides information about the asset type and its respective formatExample: Image/png | String |
| name | Refers to the file name | String |
| url | The url of the uploaded content on the Sprinklr platform | URL |
| previewUrl | The preview url of the uploaded content on the Sprinklr platform | URL |
| size | The size of the uploaded content in bytes | Integer |

[](https://dev.sprinklr.com/media-upload)




[Back to top](https://dev.sprinklr.com/media-upload)
