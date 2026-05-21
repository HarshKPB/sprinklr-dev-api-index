---
title: "Asset Import Async"
slug: asset-import-async
url: https://dev.sprinklr.com/asset-import-async
---

# Asset Import Async

#
  POST & GET Asset Import Async


The asset import async API helps you import an asset via URL. Here, the first step involves importing the asset, which will fetch the task Id in response. Using the task Id, you can use the status check API to fetch the uploaded content Id. Finally, you can use the [SAM asset create](https://dev.sprinklr.com/create-asset)API to create an asset in Sprinklr Asset Manager.

The two steps for asset import async involve:

- Import via URL to get Task Id.

- Check the status via Task Id.

**Dev Notes: **
**Things to know when using the Asset Import Async API:**

- There is no size limitation when using asset import async API.

- The processing time for importing the asset depends on its size.

- It is recommended to periodically check the status of the import.

- The asset import API will continue running until the import is successful.

## 1. Import via URL to get Task Id

This will provide us the task Id of asset upload task.

## API Endpoint

`POST`
https://api3.sprinklr.com`/{env}/`api/v2/sam/importUrl/async?importType={type}&url={valid_url_address}&uploadTrackerId={tracker_id}

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

The following table describes the Query Parameters in use.







| Query Parameter | Required | Type | Description |
| --- | --- | --- | --- |
| importType | Required | String | The file type of asset that you want to import.The supported formats are:   [ PRESENTATION, SUBTITLE, PHOTO, VIDEO, AUDIO, FLASH, HTML, PDF, DOC, DOCX, EXCEL, ZIP, PSD, SKETCH, FONT ] |
| url | Required | String | The URL of the content that you want to import. |
| uploadTrackerId | Required | String | The unique id entered by user. |

## Example - Request














Copy Code




curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/sam/importUrl/async?importType=IMAGE&url=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1711476926632-53026474fe1a&uploadTrackerId=567783456782440' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'key: {apikey}'






## Sample - Response





{
    "data": "66c8970682fba20e63411816",
    "errors": []
}





### Response Schema





``

| Parameter | Type | Description |
| --- | --- | --- |
| data | String | The data returned as response will serve as 'task ID'. This unique 'task ID' will be used to fetch the status of the asset. |
| error | String | This represents the error message, if any. |

## 2. Check the Status via Task Id

We will use the Task ID from the above call response to check the upload status of the asset.

### API Endpoint

`GET`
https://api3.sprinklr.com/{env}/api/v2/sam/task/status/{taskId}

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

## Path Parameters

The following table describes the Path Parameters in use.







| Parameter | Required | Type | Description |
| --- | --- | --- | --- |
| taskId | Required | String | Refers to the task Id that you receive in the response of "Import via URL" API call. |

## Example














Copy Code




curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/sam/task/status/66c8970682fba20e63411816' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'key: {apikey}'





## Sample - Response





{
    "data": {
        "uploadTaskStatus": "Completed",
        "uploadedContent": {
            "width": 5399,
            "height": 8095,
            "previewWidth": 480,
            "previewHeight": 720,
            "id": "66c897155c165d4a555fb2d3",
            "mimeType": "image/jpeg",
            "name": "https___images.unsplash.com_photo-1711476926632-53026474fe1a.jpg",
            "url": "https://qa6-secure-content.sprinklr.com/ui/rest/secure-content-redirection/encrypted/redirect/SPRC_VM_5BCmsF4XcVnvVq4bCA3bXp0SzJmms%2Bqw9KZZUFfNPDCoeqzNpU18eI5%2FqE4cgAfeYmJpAfPO4PHSdGP2jm0WEMFRwcC2cpdnxNcZ50RmQvzz2B%2FnhP6IeFfhVwe6IBELx74rUbVn5%2FcS%2FOhVmfHkD0wD70BGLFK2kW9jw81caekD%2FedZSGuYPsYxebp33yfauArCoFxXgtTcv0fIj%2Fv0nS9juPP8kKcRDNvofE3pG0ASNc5Qn4OLEDVO%2FDcmsTO3.jpg",
            "previewUrl": "https://qa6-secure-content.sprinklr.com/ui/rest/secure-content-redirection/encrypted/redirect/SPRC_VM_B65PdhI47t4NGbTdjgUPG0PKTrcLbdm8owzbo0LARPazi3%2B5ZEpBDY8k6NX0YiGRXKkELMxUw3IveRfUJ3cR%2B7FzmlQfdpyfL6yiWSwZa5Gm7RTfQE7Fr%2BTn6Bw4e6i12Q%2BQUYtGH5ua2ncF6ZXPnH9sha5BCSR8zi3hOLG9UEzccSzfsOJVaq12Ko3jE9p9Ll3klQ3yc12YEIWk0JTH43yJwaotydOM7OSomYQm6XRZ0EoZEHhggoReA%2BaSXnUb.jpg",
            "size": 6069196
        }
    },
    "errors": []
}





[](https://dev.sprinklr.com/asset-import-async) 

 

 
[Back to top](https://dev.sprinklr.com/asset-import-async)
