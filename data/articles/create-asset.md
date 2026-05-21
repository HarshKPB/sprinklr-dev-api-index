---
title: "Create Asset"
slug: create-asset
url: https://dev.sprinklr.com/create-asset
---

# Create Asset

#
  POST - Create Asset

	Using this API, you can create a media asset within Sprinklr. You can track and manage multiple versions of assets.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/sam

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







































``````





































****






























































| Parameter | Sub Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| name |  | Required | Refers to the name that you want to assign to the asset | String |
| description |  | Optional | Refers to the description of the asset | String |
| assetType |  | Required | Refers to the type of asset.Enum: 					 						[ PRESENTATION, SUBTITLE, PHOTO, VIDEO, AUDIO, FLASH, HTML, PDF, DOC, DOCX, EXCEL, ZIP, PSD, SKETCH, FONT ] | String |
| status |  | Required | Refers to the status of the asset.Supported Values: APPROVED, DRAFT, EXPIRED | String |
| attachment |  | Required | Object defining the attachment details | Object |
|  | type | Required | Refers to the type of attachment.ENUM:[AUDIO, VIDEO, IMAGE] | String |
|  | url | Required | Refers to the url of the attachment | Url |
|  | previewUrl | Optional | Refers to the preview url of the attachment | Url |
|  | mimeType | Optional | Refers to the combination of attachment type and format.Example: image/jpg | String |
| validity |  | Optional | Refers to the object containing the asset validity details | Object |
|  | expiryTime | Optional | Refers to the expiry time of the asset | Epoch (milliseconds) |
|  | availableFrom | Optional | Refers to the time from when the asset will be available for use | Epoch (milliseconds) |
|  | neverExpire | Optional | If true, the asset will never expire | Boolean |
|  | visibleFrom | Optional | Refers to time since when the asset will be visible on the Sprinklr's platform | Epoch (milliseconds) |
| taxonomy |  | Required | Taxonomy related to an asset | Object |
|  | campaignId | Required | Campaign identifier to associate the asset with. | String |
|  | partnerCustomProperties | Optional | Refers to the object containing key and value pairs for custom field and its respective values | Object |
|  | tags | Optional | The tags you want to set for the asset | List[String] |
| assetSource |  | Optional | Refers to the source of the Asset. e.g. SPRINKLR, GETTY, SHUTTERSTOCK. | String |
| actionStats |  | Optional | Stats of the asset actions. e.g Download, Published. | Double |
| shareConfigs |  | Optional | Array defining the asset share confinguration. | Array |
|  | shareLevel | Optional | Asset share level. e.g. USER, GLOBAL, CLIENT. | String |
|  | sharedWithIds | Optional | Id based on shareLevel. | String |
| restricted |  | Optional | If True, asset is restricted for publishing | Boolean |

## Example - Request




 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/sam' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "API check part 2",
    "description": "Sample Description from Asset again",
    "assetType": "PHOTO",
    "status": "DRAFT",
    "attachment": {
        "type": "IMAGE",
        "url": "https://sprcdn-assets.sprinklr.com/787/8ec5ebf9-8c31-4884-b5e1-ba15aa2e1728-1737311220/APIImage.jpg",
        "previewUrl": "https://sprcdn-assets.sprinklr.com/787/8ec5ebf9-8c31-4884-b5e1-ba15aa2e1728-1737311220/APIImage_p.jpg",
        "mimeType": "image/jpeg"
    },
    "assetSource": "SPRINKLR",
    "restricted": false
}'
 

     
     
 

## Example - Response




{
    "data": {
        "assetType": "PHOTO",
        "attachment": {
            "url": "https://sprcdn-assets.sprinklr.com/787/8ec5ebf9-8c31-4884-b5e1-ba15aa2e1728-1737311220/APIImage.jpg",
            "previewUrl": "https://sprcdn-assets.sprinklr.com/787/8ec5ebf9-8c31-4884-b5e1-ba15aa2e1728-1737311220/APIImage_p.jpg",
            "mimeType": "image/jpeg",
            "type": "IMAGE"
        },
        "id": "6798dd077b60507fc0a5dd98",
        "name": "API check part 2",
        "description": "Sample Description from Asset again",
        "status": "Draft",
        "taxonomy": {},
        "insights": {},
        "validity": {
            "expiryTime": 2208988800000,
            "availableFrom": 1738022400000,
            "neverExpire": false,
            "visibleFrom": 1738022400000
        },
        "actionStats": {},
        "shareConfigs": [],
        "restricted": false,
        "locked": false,
        "createdTime": 1738071303688,
        "modifiedTime": 1738071303688,
        "langVsTranslatedFieldValues": {},
        "createdByUser": 66014640,
        "versionId": 0
    },
    "errors": []
}
 

     
     
   

### Response Parameters

















































































































































































































| Parameter | Sub-Parameter |  | Type | Description |
| --- | --- | --- | --- | --- |
| data |  |  | Object | Contains details about the created asset. |
|  | assetType |  | String | The type of asset created (e.g., PHOTO). |
|  | attachment |  | Object | Details of the asset attachment. |
|  |  | url | String (URL) | The URL of the attached asset. |
|  |  | previewUrl | String (URL) | The URL of the preview version of the asset. |
|  |  | mimeType | String | The MIME type of the asset (e.g., image/jpeg). |
|  |  | type | String | The type of attachment (e.g., IMAGE). |
|  | id |  | String | The unique identifier of the asset. |
|  | name |  | String | The name of the asset. |
|  | description |  | String | A brief description of the asset. |
|  | status |  | String | The status of the asset (e.g., Draft). |
|  | taxonomy |  | Object | Reserved for taxonomy details. |
|  | insights |  | Object | Reserved for asset insights (currently empty in the response). |
|  | validity |  | Object | Contains details about the asset's validity. |
|  |  | expiryTime | Number (Epoch) | The time (in milliseconds) when the asset will expire. |
|  |  | availableFrom | Number (Epoch) | The time (in milliseconds) when the asset becomes available. |
|  |  | neverExpire | Boolean | Indicates whether the asset is set to never expire. |
|  |  | visibleFrom | Number (Epoch) | The time (in milliseconds) when the asset becomes visible. |
|  | actionStats |  | Object | Reserved for action statistics (currently empty in the response). |
|  | shareConfigs |  | Array | Contains sharing configurations. |
|  | restricted |  | Boolean | Indicates if the asset is restricted (e.g., false). |
|  | locked |  | Boolean | Indicates if the asset is locked (e.g., false). |
|  | createdTime |  | Number (Epoch) | The time (in milliseconds) when the asset was created. |
|  | modifiedTime |  | Number (Epoch) | The time (in milliseconds) when the asset was last modified. |
|  | langVsTranslatedFieldValues |  | Object | Reserved for language-specific translated fields. |
|  | createdByUser |  | Number | The ID of the user who created the asset. |
|  | versionId |  | Number | The version ID of the asset. |
| errors |  |  | Array | Contains a list of errors, if any occurred during the creation process (e.g., empty array if no errors). |

[](https://dev.sprinklr.com/create-asset) 

 

 
[Back to top](https://dev.sprinklr.com/create-asset)
