---
title: "Asset Create v1"
slug: asset-create-v1
url: https://dev.sprinklr.com/asset-create-v1
---

# Asset Create v1

#  POST Asset Create v1

The Asset Manager provides a centralized repository for all media assets, documents, templates, and more. You can use this API call to create a content asset within Sprinklr Asset Manager.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v1/sam

**Please Note:**


- Before creating a Digital Asset, you must first upload or [import the asset](https://dev.sprinklr.com/asset-import-v1) into the content store.

- Before creating a Link Asset, you must first [import the asset](https://dev.sprinklr.com/asset-import-v1) into the content store.

- You do not need to upload or import a Text Asset before creating it.

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













``







``







``







``







``







``







``





			[Bootstrap:](https://dev.sprinklr.com/bootstrap-resources-v1)

``





			[Bootstrap](https://dev.sprinklr.com/bootstrap-resources-v1)

``







``







``





			[Bootstrap](https://dev.sprinklr.com/bootstrap-resources-v1)

``







``





			``





			``







``





			[Link Asset](https://dev.sprinklr.com/link-asset)[Asset Import](https://dev.sprinklr.com/asset-import-v1)``





			[Text Asset](https://dev.sprinklr.com/text-asset)``





| Query Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| name | Required | The name of the asset. 				Example: 				 "name": "My Asset's New Name" | String |
| description | Optional | The description of the asset. 				Example: 				 "description": "My asset's new description" | String |
| assetType | Required | The media asset type: PHOTO, VIDEO, AUDIO, PRESENTATION, HTML, PDF, DOC, DOCX, EXCEL, ZIP, PSD, SKETCH, FONT, BENEFIT, SWOOSH_BENEFIT, LINK, TEXT, RTFD, RICH_TEXT, POST, CARD_ASSET, FEEDBACK, POLL, FORM, SURVEY, TEMPLATE_ASSET, REVIEW, CANVAS, DYNAMIC_IMAGE_TEMPLATE 				Example: 				 "assetType": "PHOTO" | Media Asset Type Object |
| assetStatus | Required | The status of the asset: DRAFT, APPROVED, EXPIRED. 				Example: 				 "assetStatus": "APPROVED" | Asset Status Object |
| expiryTime | Optional | The date in milliseconds since Unix Epoch to have the asset expire (Unix Time * 1000). Default = infinity. 				Example: 				 "expiryTime": 1471842000000 | Long |
| availableAfterTime | Required | The date in milliseconds since Unix Epoch to make the asset available (Unix Time * 1000). Default = current time. 				Example: 			 "availableAfterTime": 1471842000000 | Long |
| tags | Optional | A list of tags to assign to the asset. 				Example: 			 "tags": ["animals", "horses", "fish"] | Set < String > |
| shareConfig | Required | Who to share the asset with and at which permission levels. shareLevel: GLOBAL, LOCAL, USER, CLIENT_GROUP, USER_GROUP. shareWithIds: You can find ids relevant to the share level by using the  endpoint using types=CLIENTS. 				Example: 				 "shareConfigs":[    {       "shareLevel":"USER",       "sharedWithIds":[          "181"       ]    },    {       "shareLevel":"USER_GROUP",       "sharedWithIds":[          "54ff27cde4b0459cff2ab78b"       ]    },    {       "shareLevel":"CLIENT",       "sharedWithIds":[          "4"       ]    } ] | Set < String > |
| campaignIds | Required | The campaign id for the asset. You can find the campaign id using the  endpoint using types=CLIENT_CAMPAIGNS. 				Example: 				 "campaignIds": [ "1236_717" ] | Set < String > |
| assetSource | Required | Defines the source of the asset. Default = SPRINKLR. 				Example: 				 "assetSource": "STOCK PHOTO COMPANY" | String |
| partnerCustomFields | Required | The partner custom fields to associate with that asset using key/value pair combination. 				The partner custom fields to associate with that asset using key/value pair combination. You can find the partner custom fields using the Bootstrap endpoint using types=MEDIA_ASSET_CUSTOM_FIELDS.Example: 				 "partnerCustomFields": {   "5515eddf6687eb2d72000001": ["Copyright Restricted"] } | Map < String, List < String > > |
| clientCustomProperties | Required | The client custom properties to associate with that asset using key/value pair combination. You can find the client custom properties using the  endpoint using types=MEDIA_ASSET_CUSTOM_FIELDS. 				Example: 				 "clientCustomProperties":{    "5515eddf6687eb2d72000001":[       "Copyright Restricted"    ] } | Map < String, List < String > > |
| autoImported | Optional | Defines whether or not the asset was auto-imported into Sprinklr. Hint: If you are creating it, auto-importation is not likely. Default = false. 				Example: 				 "autoImported": false | Boolean |
| restricted | Optional | The restricted state of the asset. Default = false. Example: 				 "restricted": false | Boolean |
| restricted | Optional | The restricted state of the asset. Example: 				 "restricted": true | Boolean |
| uploadedContentId | Required | Required for Digital Asset creation. The uploadedContentId is the "id" string of the response when you add a Digital Asset to the content store using the Asset Upload and Asset Import endpoints.Example: 				 "uploadedContentId": "54e6f378e4b0a53788412491" | String |
| linkAsset | Required | Required for  creation. The linkAsset.linkDetails is the full response when you add a Link Asset to the content store using the  endpoint. Example: 				"linkAsset":{    "linkDetails":{       "originalUrl":"http://www.sprinklr.com",       "title":"Customer Experience Management (CEM) - Sprinklr",       "description":"Sprinklr offers the only social media management system that enables global scale of social customer experience management (CEM) for the social enterprise.",       "providerUrl":"https://www.sprinklr.com",       "providerName":"www.sprinklr.com",       "thumbnails":[          {             "url":"https://www.sprinklr.com/wp-content/uploads/2016/03/facebook_img_sprinklr_v3.png",             "width":486,             "height":256,             "size":13904          }       ],       "type":"html",       "oEmbed":{          "type":"link",          "embedCode":""       },       "destinationUrl":"https://www.sprinklr.com/"    } } } | Link Asset Object |
| textAsset | Required | Required for  creation. Example:  "textAsset":{    "text":"I am creating a text asset using the Sprinklr API" } | Text Asset Object |

###  Example - TEXT Asset




 Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v1/sam' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
   "name":"Create Asset - TEXT",
   "assetType":"TEXT",
   "description":"Create a text asset with Sprinklr's API",
   "textAsset":{
      "text":"This is a text asset!"
   }
}'



## Example - Response



[
   {
      "id":"57bc817ce4b0a2507ad66720",
      "name":"Create Asset - TEXT",
      "description":"Create a text asset with Sprinklr’s API",
      "assetStatus":"APPROVED",
      "assetType":"TEXT",
      "expiryTime":2208988800000,
      "availableAfterTime":1471910400000,
      "shareConfigs":[
         {
            "shareLevel":"GLOBAL"
         }
      ],
      "ownerClientId":4,
      "ownerUserId":181,
      "autoImported":false,
      "restricted":false,
      "deleted":false,
      "createdTime":1471971708622,
      "updatedTime":1471971708622,
      "locked":false,
      "textAsset":{
         "text":"This is a text asset!"
      }
   }
]



###  Example - PHOTO Asset




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/sam' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
   "name":"Create Asset - PHOTO",
   "assetType":"PHOTO",
   "description":"Create a photo asset with Sprinklr's API",
   "uploadedContentId":"57bc7feae4b0a2507ad6671f"
}'



## Example - Response



[
   {
      "id":"57bc82d6e4b0a2507ad66723",
      "name":"Create Asset - PHOTO",
      "description":"Create a photo asset with Sprinklr's API",
      "assetStatus":"APPROVED",
      "assetType":"PHOTO",
      "expiryTime":2208988800000,
      "availableAfterTime":1471910400000,
      "shareConfigs":[
         {
            "shareLevel":"GLOBAL"
         }
      ],
      "ownerClientId":4,
      "ownerUserId":181,
      "autoImported":false,
      "restricted":false,
      "deleted":false,
      "createdTime":1471972054183,
      "updatedTime":1471972054183,
      "locked":false,
      "digitalAsset":{
         "mediaUrl":"http://cdata.qa-apple.sprinklr.com/DAM/3/Screen_Shot_2016-05-23_at_11.3-bb83c3d2-812e-422c-b38e-819bff5fe1f5-2062056546.png",
         "originalMediaUrl":"",
         "mediaMimeType":"image/png",
         "previewUrl":"http://cdata.qa-apple.sprinklr.com/DAM/3/Screen_Shot_2016-05-23_at_11.3-bb83c3d2-812e-422c-b38e-819bff5fe1f5-2062056546_p.png",
         "imageHeight":402,
         "imageHeightUnit":"px",
         "imageWidth":404,
         "aspectRatio":1.0049751243781095,
         "imageWidthUnit":"px",
         "previewImageHeight":402,
         "previewImageHeightUnit":"px",
         "previewImageWidth":404,
         "previewImageWidthUnit":"px",
         "thumbnailUrl":"http://cdata.qa-apple.sprinklr.com/DAM/3/Screen_Shot_2016-05-23_at_11.3-bb83c3d2-812e-422c-b38e-819bff5fe1f5-2062056546_t.png",
         "thumbnailHeight":72,
         "thumbnailWidth":72
      }
   }
]



###  Example - LINK Asset




 Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v1/sam' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
  "name": "Create Asset - LINK",
  "assetType": "LINK",
  "description": "Create a link asset with Sprinklr's API",
  "linkAsset": {
    "linkDetails": {
      "originalUrl": "http://www.sprinklr.com",
      "title": "Customer Experience Management (CEM) - Sprinklr",
      "description": "Sprinklr offers the only social media management system that enables global scale of social customer experience management (CEM) for the social enterprise.",
      "providerUrl": "https://www.sprinklr.com",
      "providerName": "www.sprinklr.com",
      "thumbnails": [{
        "url": "https://www.sprinklr.com/wp-content/uploads/2016/03/facebook_img_sprinklr_v3.png",
        "width": 486,
        "height": 256,
        "size": 13904
      }],
      "type": "html",
      "oEmbed": {
        "type": "link",
        "embedCode": ""
      },
      "destinationUrl": "https://www.sprinklr.com/"
    }
  }
}'



## Example - Response



[
   {
      "id":"57bc8723e4b0a2507ad66726",
      "name":"Create Asset - LINK",
      "description":"Create a link asset with Sprinklr's API",
      "assetStatus":"APPROVED",
      "assetType":"LINK",
      "expiryTime":2208988800000,
      "availableAfterTime":1471910400000,
      "shareConfigs":[
         {
            "shareLevel":"GLOBAL"
         }
      ],
      "ownerClientId":4,
      "ownerUserId":181,
      "autoImported":false,
      "restricted":false,
      "deleted":false,
      "createdTime":1471973155972,
      "updatedTime":1471973155972,
      "locked":false,
      "linkAsset":{
         "linkDetails":{
            "originalUrl":"http://www.sprinklr.com",
            "title":"Customer Experience Management (CEM) - Sprinklr",
            "description":"Sprinklr offers the only social media management system that enables global scale of social customer experience management (CEM) for the social enterprise.",
            "providerUrl":"https://www.sprinklr.com",
            "providerName":"www.sprinklr.com",
            "thumbnails":[
               {
                  "url":"https://www.sprinklr.com/wp-content/uploads/2016/03/facebook_img_sprinklr_v3.png",
                  "width":486,
                  "height":256,
                  "size":13904
               }
            ],
            "type":"html",
            "oEmbed":{
               "type":"link",
               "embedCode":""
            },
            "destinationUrl":"https://www.sprinklr.com/"
         },
         "linkType":"link"
      }
   }
]



###  Example - POST Asset




 Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v1/sam' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "assetType": "POST",
    "expiryTime": 2208988800000,
    "name": "Post Asset Test",
    "availableAfterTime": 1678783560000,
    "visibleFromTime": 1678783560000,
    "visibleTillTime": 2208988800000,
    "campaignIds": [
        "0"
    ],
    "shareConfigs": [
        {
            "shareLevel": "CLIENT",
            "sharedWithIds": []
        },
        {
            "shareLevel": "CLIENT_GROUP",
            "sharedWithIds": []
        },
        {
            "shareLevel": "USER",
            "sharedWithIds": []
        },
        {
            "shareLevel": "USER_GROUP",
            "sharedWithIds": []
        }
    ],
    "tags": [],
    "assetStatus": "APPROVED",
    "restricted": false,
    "postAsset": {
        "channelSpecificDetails": [],
        "postAssetChannelContent": [
            {
                "postChannelType": "EMAIL",
                "postAccountType": "EMAIL",
                "postContent": "Hello Team",
                "postAdditional": {
                    "TO_EMAIL_ADDRESS": [],
                    "CC_EMAIL_ADDRESS": [],
                    "BCC_EMAIL_ADDRESS": [],
                    "CONTENT_TEMPLATE_TYPE": [
                        "STANDARD"
                    ],
                    "title": [
                        null
                    ],
                    "subject": [
                        null
                    ],
                    "templateContent": [
                        null
                    ]
                }
	}]
}
}'

## Example - Response



[
    {
        "id": "64108753a19e0e0eed122e47",
        "name": "Post Asset Test",
        "assetStatus": "APPROVED",
        "assetType": "POST",
        "expiryTime": 2208988800000,
        "availableAfterTime": 1678783560000,
        "visibleFromTime": 1678783560000,
        "visibleTillTime": 2208988800000,
        "tags": [],
        "shareConfigs": [
            {
                "shareLevel": "CLIENT",
                "sharedWithIds": []
            },
            {
                "shareLevel": "CLIENT_GROUP",
                "sharedWithIds": []
            },
            {
                "shareLevel": "USER",
                "sharedWithIds": []
            },
            {
                "shareLevel": "USER_GROUP",
                "sharedWithIds": []
            }
        ],
        "ownerClientId": 1,
        "ownerUserId": 600000003,
        "campaignIds": [
            "0"
        ],
        "autoImported": false,
        "restricted": false,
        "deleted": false,
        "createdTime": 1678804819771,
        "updatedTime": 1678804819771,
        "locked": false,
        "postAsset": {
            "postPublishedTime": 0,
            "postAssetChannelContent": [
                {
                    "postChannelType": "EMAIL",
                    "postAccountType": "EMAIL",
                    "postContent": "Hello There",
                    "postAdditional": {
                        "TO_EMAIL_ADDRESS": [],
                        "CC_EMAIL_ADDRESS": [],
                        "BCC_EMAIL_ADDRESS": [],
                        "CONTENT_TEMPLATE_TYPE": [
                            "STANDARD"
                        ],
                        "title": [
                            null
                        ],
                        "subject": [
                            null
                        ],
                        "templateContent": [
                            null
                        ]
                    }
                }
            ],
            "postAssetChannels": [
                "EMAIL"
            ],
            "channelSpecificDetails": [],
            "childPostAsset": false,
            "enabled": true
        },
        "favorite": false
    }
]



[](https://dev.sprinklr.com/asset-create-v1) 

 

 
[Back to top](https://dev.sprinklr.com/asset-create-v1)
