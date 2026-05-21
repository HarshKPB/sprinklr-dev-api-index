---
title: "Add Comment"
slug: add-comment
url: https://dev.sprinklr.com/add-comment
---

# Add Comment

#
  POST - Add Comment


You can use the Add Comment API to add comment in different entity types with and without attachment. To add comment with attachments like Image, Video and file, you need to use another API to first upload the attachment on cloud and then use it in Add Comment API. Below are the steps you need to follow:

- Create Comment without Attachment

- Create Comment with Attachments

**Dev Note: ** Supported entity types: `MESSAGE, OUTBOUND_MESSAGE, CASE, CAMPAIGN, PROFILE.`

## Create Comment without Attachment

You can use the Add Comment API to add comment in different entity types.

### API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/comment/`{entityType}`/`{entityId}`

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

























| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityType | Required | Entity type can be MESSAGE, OUTBOUND_MESSAGE, CASE, CAMPAIGN and PROFILE. | String |
| entityId | Required | Entity id with respect to entity types. e.g  MESSAGE - Message Id , CASE - Case Number, OUTBOUND_MESSAGE - The unique outbound message Id, CAMPAIGN - Campaign Id and PROFILE - Profile Id. | String |

## Example - Create Case Comment




 Copy Code



curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/comment/CASE/25253550  \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -H 'accept: application/json' \
  -d  '{
        "text": "comment test"
       }'





## Example - Response



{
    "data": {
        "id": "5ef9bed9401d6d4d17232a8c",
        "text": "comment test",
        "commentingUser": 200551,
        "createdTime": 1593425624890,
        "modifiedTime": 1593425624890,
        "entityType": "CASE",
        "entityId": "25253550"
    },
    "errors": []
}





### API Endpoint for PROFILE, MESSAGE and CAMPAIGN:

























| Entity Type | Endpoint |
| --- | --- |
| PROFILE | https://api3.sprinklr.com/{env}/api/v2/comment/PROFILE/{profileId} |
| MESSAGE | https://api3.sprinklr.com/{env}/api/v2/comment/MESSAGE/{messageId} |
| CAMPAIGN | https://api3.sprinklr.com/{env}/api/v2/comment/CAMPAIGN/{campaignId} |
| OUTBOUND_MESSAGE | https://api3.sprinklr.com/{env}/api/v2/comment/OUTBOUND_MESSAGE/{postId} |

## Create Comment with Attachment

You can use the Add Comment API to add comment in different entity types with attachment. To add comment with attachments like Image, Video and file, you need to first use the `Media Upload API` to upload the attachment on cloud and then use the response of Media Upload API in Add Comment API. Below are the steps:

### Step 1:
 Use Media Upload api to upload the attachment on cloud.

### API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/media/upload

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






























| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| assetType | Required | Asset type can be Image, video and file. | String |
| fileName | Required | Enter a file name. | String |
| uploadTrackerId | Required | A unique identifier from the client. This id is any string as long as it is unique each time.The uploadTrackerId cannot be used again once you have uploaded an asset to the content store. | String |

## Example - Upload Attachment




 Copy Code



curl --location --request POST
  'https://api3.sprinklr.com/{env}/api/v2/media/upload?assetType=image&fileName=test_image&uploadTrackerId=dfghj567890cfghvb567890' \
--header 'Key: {Enter your API KEY}' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Content-Type: application/json' \
--form 'file=@/Sumit/test Data/Test_image.jpg'





## Example - Response



{
    "data": {
        "width": 1036,
        "height": 688,
        "previewWidth": 720,
        "previewHeight": 478,
        "id": "5f8965815edbb80d687e298e",
        "mimeType": "image/png",
        "name": "test_image.png",
        "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
        "previewUrl": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image_p.png",
        "size": 47991
    },
    "errors": []
}





**Dev Note: ** From the above response we will use `url` and `previewUrl` in the next step.

### Step 2:

Create comment with attachment using the response parameters form step 1 in Add Comment api.

### API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/comment/`{entityType}`/`{entityId}`

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

























| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityType | Required | Entity type can be MESSAGE, OUTBOUND_MESSAGE, CASE, CAMPAIGN and PROFILE. | String |
| entityId | Required | Entity id with respect to entity types. e.g  MESSAGE - Message Id , CASE - Case Number, CAMPAIGN - Campaign Id and PROFILE - Profile Id. | String |

## Request Parameters

















































| Parameters | Sub - Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| text |  | Required | The comment the you need to update. | String |
| attachment |  | Required | The object containing attachment information. | String |
|  | url | Required | The url you get in the response of Media API call. | String |
|  | previewUrl | Optional | The previewUrl you get in the response of Media API call. | String |
|  | type | Required | Type of attachmentEnum:  						[ IMAGE, DOC, VIDEO, AUDIO ] | String |

## Example - Create Case Comment




 Copy Code



curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/comment/CASE/25253550  \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -H 'accept: application/json' \
  -d  '{
    "text": "Comment Create on Case with Attachment",
    "attachment":{
        "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
        "previewUrl": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image_p.png",
    "type":"IMAGE"
    }
}'





## Example - Response




{
    "data": {
        "id": "5f89660aa6b62573fe7e6a6b",
        "text": "Comment Create with Attachment",
        "attachment": {
            "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
            "previewUrl": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image_p.png",
            "type": "IMAGE"
        },
        "commentingUser": 200551,
        "createdTime": 1602840074151,
        "modifiedTime": 1602840074151,
        "entityType": "CASE",
        "entityId": "25356250"
    },
    "errors": []
}





## Response Parameters









































| Parameters | Description | Type |
| --- | --- | --- |
| id | Unique Id of the comment. | String |
| text | Text of the comment. | String |
| createdTime | Time when the comment was made. | Epoch |
| modifiedTime | Time when the comment was modified. | Epoch |
| entityType | Entity type on which the asset was created. | String |
| entityId | Id of the entity on which the comment was created. | String |

[](https://dev.sprinklr.com/add-comment)




[Back to top](https://dev.sprinklr.com/add-comment)
