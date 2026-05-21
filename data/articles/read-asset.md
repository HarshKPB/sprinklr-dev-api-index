---
title: "Read Asset"
slug: read-asset
url: https://dev.sprinklr.com/read-asset
---

# Read Asset

#
  GET - Read Asset

You can fetch details of an existing Sprinklr asset via this API call using the asset Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/sam/{assetId}

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

### Path Parameters







[create asset API](https://dev.sprinklr.com/create-asset)[asset search API](https://dev.sprinklr.com/asset-search-v1)

-
-
-
- ****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| assetId | Required | Asset id of the existing Sprinklr asset. You can extract the asset Id from the  response or you can use the .Alternatively, you can fetch the asset id from the UI too. Steps for UI extract:    Navigate to asset manager Hover over to the desired asset Click on the three dots on the right and click on details You will be able to find the asset id under the properties section  Note: Ensure that the type of asset you want to read is supported. The following note lists the supported asset types. | String |

**Dev Notes: **The API supports reading the following asset types:

PRESENTATION, PHOTO, VIDEO, AUDIO, FLASH, HTML, PDF, DOC, DOCX, EXCEL, ZIP, PSD, SKETCH, FONT, SUBTITLE, TEMPLATE_ASSET, RAR, SVG, EML, MSG, EDB, ICS, EPS, INDD, LINK, POST, RICH_TEXT, TEXT, POLL, GEO_LOCATION

## Example - Request




 Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/sam/6798dd077b60507fc0a5dd98' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
 

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
        "assetSource": "SPRINKLR",
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
			 

     
     
   

**Dev Notes: **If your token is associated with multiple workspaces, kindly pass "workspace_id" in the headers to access the asset details.

[](https://dev.sprinklr.com/read-asset) 

 

 
[Back to top](https://dev.sprinklr.com/read-asset)
