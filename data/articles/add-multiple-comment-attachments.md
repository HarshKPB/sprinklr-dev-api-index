---
title: "Add Multiple Comment Attachments"
slug: add-multiple-comment-attachments
url: https://dev.sprinklr.com/add-multiple-comment-attachments
---

# Add Multiple Comment Attachments

#
  POST - Add Multiple Comment Attachments


Using this API, you can add multiple attachments on a comment (note).

**Dev Note: ** Supported entity types: `MESSAGE, OUTBOUND_MESSAGE, CASE, CAMPAIGN, PROFILE.`

### API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/comment/`{entityType}`/`{entityId}`/multiple-attachment

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


## Request Parameters













****

| Parameters | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| comment |  | Required | Refers to the text of the comment | String |
| attachments |  | Required | Refers to the array containing the comments' details | Array |
|  | url | Required | Refers to the url of the attachment | String |
|  | previewUrl | Optional | Refers to the preview Url of the attachment | String |
|  | type | Required | Refers to the type of the attachmentSupported Attachment Types: IMAGE, VIDEO, DOC | String |

**Dev Note: **Prior to adding an attachment on a comment, use `[Media upload API](https://dev.sprinklr.com/media-upload)` to upload the attachment on the Sprinklr's server.

## Example - Add Note Attachments on Case




 Copy Code



curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/comment/CASE/25253550/multiple-attachment' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -H 'accept: application/json' \
  -d  '{
    "comment": "Add Comment Attachments on Case",
    "attachments": [
        {
            "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image_p.png",
            "previewUrl": "https: //sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image_p.png",
            "type": "IMAGE"
        },
        {
            "url": "https://pz.cdata.prod0.sprinklr.com/DAM/9004/71221cd8-a9f7-4179-b6ca-3273e07a3c7c-1284685191/https___pbs.twimg.com_media_GG.jpg",
            "previewUrl": "https: //pz.cdata.prod0.sprinklr.com/DAM/9004/71221cd8-a9f7-4179-b6ca-3273e07a3c7c-1284685191/https___pbs.twimg.com_media_GG_p.jpg",
            "type": "IMAGE"
        }
    ]
}'





## Example - Response




{
    "data": {
        "id": "65d5acd6dff20160fd4ac551",
        "text": "Add Comment Attachments on Case",
        "attachment": {
            "attachments": [
                {
                    "url": "https: //sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image_p.png",
                    "previewUrl": "https: //sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image_p.png",
                    "type": "IMAGE"
                },
                {
                    "url": "https: //pz.cdata.prod0.sprinklr.com/DAM/9004/71221cd8-a9f7-4179-b6ca-3273e07a3c7c-1284685191/https___pbs.twimg.com_media_GG.jpg",
                    "previewUrl": "https: //pz.cdata.prod0.sprinklr.com/DAM/9004/71221cd8-a9f7-4179-b6ca-3273e07a3c7c-1284685191/https___pbs.twimg.com_media_GG_p.jpg",
                    "type": "IMAGE"
                }
            ],
            "type": "MULTI_MEDIA"
        },
        "commentingUser": 1000157828,
        "createdTime": 1708502226669,
        "modifiedTime": 1708502226669,
        "entityType": "CASE",
        "entityId": "7252751",
        "conversationId": "65c664c1fedc2955e850f969",
        "externalComment": {
            "channelType": "EMAIL"
        }
    },
    "errors": []
}





[](https://dev.sprinklr.com/add-multiple-comment-attachments)




[Back to top](https://dev.sprinklr.com/add-multiple-comment-attachments)
