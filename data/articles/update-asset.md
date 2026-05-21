---
title: "Update Asset"
slug: update-asset
url: https://dev.sprinklr.com/update-asset
---

# Update Asset

#
  PUT  Update Asset

You can update a Sprinklr asset via this API call.

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


































































































































			``********
****

- ``
-
- ````
- ``
```

```
****
- ``
- ``
-






			****``


















| Parameter | Sub Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| id |  | Required | Id of the asset. | String |
| name |  | Required | Name of the asset. | String |
| description |  | Required | Description of asset. | String |
| assetType |  | Required | The type of asset.ENUM:[PRESENTATION, PHOTO, VIDEO, AUDIO, FLASH, HTML, PDF, DOC, DOCX, EXCEL, ZIP, PSD, SKETCH, FONT] | String |
| status |  | Required | Status of the asset.Supported Values: APPROVED, DRAFT, EXPIRED | String |
| attachment |  | Required | Information about the attachment. | String |
|  | type | Required | The type of attachment.ENUM:[Audio, Video] | String |
|  | attachmentOptions | Optional | Array of attachment properties per channel and/or account.ChannelSpecificMediaProperties are given below in Attachment Option Table. |  |
| taxonomy |  | Required | Taxonomy related to an asset |  |
|  | campaignId | Required | Campaign identifier to associate the message to. | String |
|  | clientCustomProperties | Optional | Client custom properties for the message. | String |
|  | partnerCustomProperties | Optional | Partner custom properties for the message. | String |
|  | tags | Optional | Tags to be added to the message. | String |
|  | urlShortnerId | Optional | Url shortner identifier to apply to the message. | String |
| insights |  | Optional | Collective insights of the posts on social channels. e.g. likes, comments, shares. | Double |
| validity |  | Optional | Information regarding the validity of an asset. |  |
|  | expiryTime | Optional | Asset expiry time. This option is not valid if neverExpire is true. | Integer |
|  | availableFrom | Optional | Asset is available from time. | Integer |
|  | neverExpire | Optional | If True, asset will never expire. | Boolean |
| parentId |  | Optional | Parent Asset Id. | String |
| assetSource |  | Optional | Source of the Asset. e.g. SPRINKLR, GETTY, SHUTTERSTOCK. | String |
| actionStats |  | Optional | Stats of the asset actions. e.g Download, Published. | Double |
| shareConfigs |  | Optional | The shareConfigs parameter defines the visibility configuration of an asset in      Asset Manager. It determines which clients, client groups, users, or user groups can access a specific asset. This parameter is used when updating an asset’s sharing and access settings.       Example Configuration        The following example shares an asset with:           One client (1000004509)     No client groups     Two users (1000063395, 1000059523)     One user group (66bf4770d6907b378599e534)      "shareConfigs": [   {     "type": "CLIENT",     "ids": ["1000004509"]   },   {     "type": "CLIENT_GROUP",     "ids": []   },   {     "type": "USER",     "ids": ["1000063395", "1000059523"]   },   {     "type": "USER_GROUP",     "ids": ["66bf4770d6907b378599e534"]   } ]   Notes        You can combine multiple type entries in the same configuration.     Empty ids arrays mean no entities of that type are included.     Ensure that IDs are valid and correspond to entities configured in your Sprinklr environment. | Array of Object |
|  | type | Optional | Specifies the entity type to which the asset is shared. Supported Values: USER, USER_GROUP, GLOBAL, CLIENT, CLIENT_GROUP . | String |
|  | id | Optional | A list of unique identifiers for the specified entity type. | String |
| restricted |  | Optional | If True, asset is restricted from publishing. | Boolean |

### Attachment Option Description Table


























| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| channelType | Required | ChannelType for media options. Enum:[ FACEBOOK, TWITTER ] | String |
| accountId | Optional | If the properties are specific to an account inaddition to channelType, accountId can be specified and the properties would then only be used for the given account. | Integer |


## Example - Request




 Copy Code



curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/sam' \
  -H 'Authorization:Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
    "id": "6798dd077b60507fc0a5dd98",
    "name": "API check part 2",
    "description": "Asset is updated now-3",
    "assetType": "PHOTO",
    "status": "Draft",
    "attachment": {
        "url": "https://space-qa6.sprinklr.com/ui/rest/secure-assets/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3Nwci1xYTYtY2RhdGEvREFNLzY2MDAwMDAwLzRkMWU3NDc1LWVkMDItNDUyYy1iY2NkLTNjYzFmMzlkZWI2Ny0xOTc4Mzc3NzgzL2h0dHBzX19fcWE2LW1lZGlhLXByb3h5LnNwcmluay5qcGc%3D1",
            "previewUrl": "https://space-qa6.sprinklr.com/ui/rest/secure-assets/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3Nwci1xYTYtY2RhdGEvREFNLzY2MDAwMDAwLzRkMWU3NDc1LWVkMDItNDUyYy1iY2NkLTNjYzFmMzlkZWI2Ny0xOTc4Mzc3NzgzL2h0dHBzX19fcWE2LW1lZGlhLXByb3h5LnNwcmluay5qcGc%3D1",
            "mimeType": "image/jpeg",
            "type": "IMAGE"
    },
    "assetSource": "SPRINKLR",
    "restricted": false
}'
 

     
     
 

## Example - Response



 
{
    "data": {
        "assetType": "PHOTO",
        "attachment": {
            "url": "https://space-qa6.sprinklr.com/ui/rest/secure-assets/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3Nwci1xYTYtY2RhdGEvREFNLzY2MDAwMDAwLzRkMWU3NDc1LWVkMDItNDUyYy1iY2NkLTNjYzFmMzlkZWI2Ny0xOTc4Mzc3NzgzL2h0dHBzX19fcWE2LW1lZGlhLXByb3h5LnNwcmluay5qcGc%3D1",
            "previewUrl": "https://space-qa6.sprinklr.com/ui/rest/secure-assets/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3Nwci1xYTYtY2RhdGEvREFNLzY2MDAwMDAwLzRkMWU3NDc1LWVkMDItNDUyYy1iY2NkLTNjYzFmMzlkZWI2Ny0xOTc4Mzc3NzgzL2h0dHBzX19fcWE2LW1lZGlhLXByb3h5LnNwcmluay5qcGc%3D1",
            "mimeType": "image/jpeg",
            "type": "IMAGE"
        },
        "id": "6798dd077b60507fc0a5dd98",
        "name": "API check part 2",
        "description": "Asset is updated now-3",
        "status": "Draft",
        "taxonomy": {},
        "insights": {},
        "validity": {
            "expiryTime": 2208988800000,
            "availableFrom": 1738022400000,
            "neverExpire": false,
            "visibleFrom": 1738022400000
        },
        "assetSource": "SPRINKLR",
        "actionStats": {},
        "shareConfigs": [],
        "restricted": false,
        "locked": false,
        "createdTime": 1738071303688,
        "modifiedTime": 1738075557706,
        "langVsTranslatedFieldValues": {},
        "createdByUser": 66014640,
        "versionId": 1
    },
    "errors": []
}
 

     
     
   
 

### Response Parameters
























































































``````

































































































































| Parameter | Sub-Parameter |  | Type | Description |
| --- | --- | --- | --- | --- |
| data |  |  | Object | Contains details about the updated asset. |
|  | assetType |  | String | The type of asset updated (e.g., PHOTO)ENUM:[PRESENTATION, PHOTO, VIDEO, AUDIO, FLASH, HTML, PDF, DOC, DOCX, EXCEL, ZIP, PSD, SKETCH, FONT] |
|  | attachment |  | Object | Details of the updated asset attachment. |
|  |  | url | String (URL) | The URL of the attached asset. |
|  |  | previewUrl | String (URL) | The URL of the preview version of the asset. |
|  |  | mimeType | String | The MIME type of the asset (e.g., image/jpeg). |
|  |  | type | String | The type of attachment (e.g., IMAGE). |
|  | id |  | String | The unique identifier of the updated asset. |
|  | name |  | String | The name of the updated asset. |
|  | description |  | String | A brief description of the updated asset. |
|  | status |  | String | The status of the updated asset (e.g., Draft). Supported Values: APPROVED, DRAFT, EXPIRED |
|  | taxonomy |  | Object | Reserved for taxonomy details. |
|  | insights |  | Object | Reserved for asset insights. |
|  | validity |  | Object | Contains details about the asset's validity. |
|  |  | expiryTime | Number (Epoch) | The time (in milliseconds) when the asset will expire. |
|  |  | availableFrom | Number (Epoch) | The time (in milliseconds) when the asset becomes available. |
|  |  | neverExpire | Boolean | Indicates whether the asset is set to never expire. |
|  |  | visibleFrom | Number (Epoch) | The time (in milliseconds) when the asset becomes visible. |
|  | assetSource |  | String | The source of the asset (e.g., SPRINKLR). |
|  | actionStats |  | Object | Reserved for action statistics (currently empty in the response). |
|  | shareConfigs |  | Array | Contains sharing configurations (currently empty in the response). |
|  | restricted |  | Boolean | Indicates if the asset is restricted (e.g., false). |
|  | locked |  | Boolean | Indicates if the asset is locked (e.g., false). |
|  | createdTime |  | Number (Epoch) | The time (in milliseconds) when the asset was created. |
|  | modifiedTime |  | Number (Epoch) | The time (in milliseconds) when the asset was last updated. |
|  | langVsTranslatedFieldValues |  | Object | Reserved for language-specific translated fields. |
|  | createdByUser |  | Number | The ID of the user who created the asset. |
|  | versionId |  | Number | The version ID of the asset (e.g., 1 for the updated version). |
| errors |  |  | Array | Contains a list of errors, if any occurred during the update process (e.g., empty array if no errors). |

[](https://dev.sprinklr.com/update-asset) 

 

 
[Back to top](https://dev.sprinklr.com/update-asset)
