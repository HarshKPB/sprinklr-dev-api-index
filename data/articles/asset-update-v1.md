---
title: "Asset Update v1"
slug: asset-update-v1
url: https://dev.sprinklr.com/asset-update-v1
---

# Asset Update v1

#  PUT Asset Update v1

Using this API, you can update an asset existing within Sprinklr Asset Manager. The API only supports updating Digital Assets, Link Assets, and Text Assets.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v1/sam/{assetId}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/getting-started)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameter


















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| assetId | Required | The unique identifier for the asset | String |

### Request Parameters


























































[Bootstrap](https://dev.sprinklr.com/bootstrap-resources-v1)









[](https://dev.sprinklr.com/)[Bootstrap](https://dev.sprinklr.com/bootstrap-resources-v1)








[Bootstrap](https://dev.sprinklr.com/bootstrap-resources-v1)








[Bootstrap](https://dev.sprinklr.com/bootstrap-resources-v1)












| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| name | Optional | The name of the asset | String |
| description | Optional | The description of the asset | String |
| assetStatus | Optional | The status of the asset: DRAFT, APPROVED, EXPIRED 						Example: 						"assetStatus": "APPROVED" | Asset Status Object |
| expiryTime | Optional | The date in milliseconds since Unix Epoch to have the asset expire. 						Example: 						"assetStatus": 1471842000000 | Long |
| availableAfterTime | Optional | The date in milliseconds since Unix Epoch to make the asset available. 						Example: 						"assetStatus": 1471842000000 | Long |
| tags | Optional | A list of tags to assign to the asset. 						Example: 						"tags": ["animals", "horses", "fish"] | Set < String > |
| shareConfig | Optional | Who to share the asset with and at which permission levels 						shareLevel: GLOBAL, LOCAL, USER, CLIENT_GROUP, USER_GROUP 						shareWithIds: You can find ids relevant to the share level by using the  : endpoint using types=CLIENTS | Set < String > |
| campaignId | Optional | The campaign id for the asset 						You can find the campaign id using the  endpoint using types=CLIENT_CAMPAIGNS 						Example: 						"campaignId": "8" | String |
| partnerCustomFields | Optional | The partner custom fields to associate with that asset using key/value pair combination 						You can find the partner custom fields using the  endpoint using types=MEDIA_ASSET_CUSTOM_FIELDS | Map < String>, List < String > |
| clientCustomProperties | Optional | The client custom properties to associate with that asset using key/value pair combination 						You can find the partner custom fields using the   endpoint using types=MEDIA_ASSET_CUSTOM_FIELDS | Map < String>, List < String > |
| restricted | Optional | The restricted state of the asset 						Example: 						"restricted": true | Boolean |

### Example - Request




 Copy Code



curl --location --request PUT 'https://api3.sprinklr.com/{env}/api/v1/sam/570e127fe4b0efc7492279d3'
--header 'key: {Api Key}'
--header 'Authorization: Bearer {Access Token}'
--header 'Content-Type: application/json'
--data-raw '{
  "name": "sumittesting",
  "description": "Updated via API test.",
  "tags": ["new"]
}'



**Dev Notes: **You may only update the attributes above. They system will ignore all other attributes. As an example, if you attempt to update assetType from PHOTO to VIDEO, the assetType will not change.The API only supports updating [Digital Assets](https://dev.sprinklr.com/digital-asset), [Link Assets](https://dev.sprinklr.com/link-asset), and [Text Assets](https://dev.sprinklr.com/text-asset). It does not support updating Post Assets at this time.

### Example - Response



{
    "id": "5fbe4b634243e53430b674fa",
    "name": "sumittesting",
    "description": "Updated via API test.",
    "assetStatus": "APPROVED",
    "assetType": "TEMPLATE_ASSET",
    "expiryTime": 2208988800000,
    "availableAfterTime": 1606306532868,
    "visibleFromTime": 1606306532868,
    "visibleTillTime": 2208988800000,
    "tags": [
        "new"
    ],
    "shareConfigs": [
        {
            "shareLevel": "GLOBAL"
        }
    ],
    "ownerClientId": 4706,
    "ownerUserId": 242077,
    "partnerCustomFields": {
        "5f5f660090dc844f8163a8d0": [],
        "5e9677d8044204326c0fa736": [],
        "5e967841044204326c0fb327": [],
        "5f2561bb2fcd3d02a6e9a24c": [],
        "5e967827044204326c0fb074": [],
        "5ee9abedb57ccf7e498de46a": [
            "4706"
        ],
        "5f48f892b3802c3df6ba3cb6": [],
        "5cc69310e4b09bbb0df1376c": [],
        "5cc44946e4b09f74916db841": [],
        "5f4e249b13a44358662d0e9d": [],
        "59da2c02e4b0ebae64f837c3": [],
        "wh_bu_hsm_lan_code": [],
        "5cb87468e4b02199d74408d7": [],
        "5e967816044204326c0fae1d": [],
        "wh_bu_hsm_element": [],
        "5cb874cde4b02199d744162c": [],
        "wh_bu_hsm_namespace": [],
        "wh_bu_hsm_lan_pol": [],
        "5f2561ce2fcd3d02a6e9a42f": [],
        "5e9677a9044204326c0fa07d": [],
        "5e967854044204326c0fb584": []
    },
    "clientCustomProperties": {
        "570a4c11e4b0b75893b7a119": [],
        "5acb507ee4b0defd28291c7f": [
            "55"
        ],
        "5f4e28ca5c151768a52f7f79": [],
        "59f02e57e4b0d671007ce978": [],
        "5acb5124e4b0defd28292e65": [
            "00"
        ]
    },
    "campaignIds": [
        "4706_750"
    ],
    "assetSource": "SPRINKLR",
    "autoImported": false,
    "restricted": false,
    "deleted": false,
    "createdTime": 1606306659316,
    "updatedTime": 1608210972192,
    "locked": false,
    "templateAsset": {
        "channelType": "FACEBOOK",
        "templateType": "CAROUSEL",
        "elementList": [
            {
                "id": "5fbe4b634243e53430b674f5",
                "title": "new",
                "elementList": [
                    {
                        "id": "5fbe4b634243e53430b674f6",
                        "title": "new",
                        "url": "www.google.com",
                        "quantity": 0,
                        "price": 0,
                        "type": "text",
                        "actionType": "web_url",
                        "langVsTranslatedFieldValues": {}
                    }
                ],
                "attachedAssets": [
                    {
                        "previewUrl": "https://sprcdn-assets.sprinklr.com/787/7f5bbaea-19fa-4e96-8e3c-c325fbf52ff0-836545904/https___prod-media-proxy.sprin_p.jpg",
                        "mediaUrl": "https://sprcdn-assets.sprinklr.com/787/7f5bbaea-19fa-4e96-8e3c-c325fbf52ff0-836545904/https___prod-media-proxy.sprin.jpg",
                        "mediaMimeType": "image/jpeg",
                        "title": "11",
                        "description": "",
                        "attachedSAMId": "5fbe4209aa0b7d6cfbc31563",
                        "mediaAssetType": "PHOTO"
                    }
                ],
                "quantity": 0,
                "price": 0,
                "langVsTranslatedFieldValues": {}
            },
            {
                "id": "5fbe4b634243e53430b674f7",
                "title": "new2",
                "elementList": [
                    {
                        "id": "5fbe4b634243e53430b674f8",
                        "title": "new",
                        "quantity": 0,
                        "price": 0,
                        "type": "text",
                        "actionType": "no_action",
                        "langVsTranslatedFieldValues": {}
                    }
                ],
                "attachedAssets": [
                    {
                        "previewUrl": "https://sprcdn-assets.sprinklr.com/787/c22c20f4-3789-4852-9680-ab59f3c9e2c3-1899917651/https___prod-media-proxy.sprin_p.jpg",
                        "mediaUrl": "https://sprcdn-assets.sprinklr.com/787/c22c20f4-3789-4852-9680-ab59f3c9e2c3-1899917651/https___prod-media-proxy.sprin.jpg",
                        "mediaMimeType": "image/jpeg",
                        "title": "2020-11-25.8830315.6666977400828518",
                        "description": "",
                        "attachedSAMId": "5fbe1b7ca125a60d7a504984",
                        "mediaAssetType": "PHOTO"
                    }
                ],
                "quantity": 0,
                "price": 0,
                "langVsTranslatedFieldValues": {}
            }
        ],
        "omniChannelTemplate": false,
        "translatedLanguages": []
    }
}



[](https://dev.sprinklr.com/asset-update-v1) 

 

 
[Back to top](https://dev.sprinklr.com/asset-update-v1)
