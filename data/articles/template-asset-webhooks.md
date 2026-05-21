---
title: "Template Asset Webhooks"
slug: template-asset-webhooks
url: https://dev.sprinklr.com/template-asset-webhooks
---

# Template Asset Webhooks

# Template Asset Webhooks

`Template Asset Webhook Subscriptions:` Create, Update, Delete

This webhook is triggered whenever an omnichannel template is created, updated, or deleted

- [template.asset.created Webhook](https://dev.sprinklr.com/template-asset-webhooks#taCreated)

- [template.asset.updated Webhook](https://dev.sprinklr.com/template-asset-webhooks#taUpdated)

- [template.asset.deleted Webhook](https://dev.sprinklr.com/template-asset-webhooks#taDeleted)


### template.asset.created Webhook - HSM Template




  Copy Code



```

{
    "id": "63ff5af61b00a978efa1ac27",
    "type": "template.asset.created",
    "payload": {
        "assetType": "TEMPLATE_ASSET",
        "templateAsset": {
            "channelType": "WHATSAPP_BUSINESS",
            "templateType": "HSM",
            "elementList": [],
            "buttons": [],
            "attachment": {
                "wabaTemplateId": 592224602777153,
                "namespace": "c361c688_70d9_4f6e_b994_44c19cb9bc1a",
                "wabaId": "1113164986160914",
                "elementName": "elem_name",
                "category": "TRANSACTIONAL",
                "langCode": "bn",
                "buttons": [],
                "wabaTemplateStatus": "PENDING",
                "message": "MSG\n",
                "header": {
                    "headerType": "Text",
                    "message": "HEADER"
                },
                "type": "HSM"
            }
        },
        "id": "63ff5af21b00a978efa1ab3d",
        "name": "Mith-WhatsappBusiness-1March23",
        "description": "Mith-WhatsappBusiness-1March23",
        "status": "Approved",
        "taxonomy": {
            "clientCustomProperties": {},
            "partnerCustomProperties": {
                "62a1cee720e26714e3988dfc": [
                    "Integrated Marketing"
                ],
                "_c_62cec298ee244a614a39c4b4": [
                    "Business_Function TEST"
                ],
                "5ebe4cf68b112133b824f039": [
                    "Test_Sample10"
                ],
                "_c_5fec3ed893f2057f703713b0": [
"
*l3 fix - Updated*
"
                ],
                "62a1cc6e20e26714e3963731": [
                    "N/A"
                ],
                "5ceb7d74e4b01a09536250b4": [
                    "_Ipod"
                ],
                "_c_617d53f013bf364027ffc901": [
                    "Joey"
                ],
                "5ebe4d128b112133b824f079": [
                    "12123"
                ]
            }
        },
        "insights": {},
        "validity": {
            "expiryTime": 1678284120000,
            "availableFrom": 1677678545521,
            "neverExpire": false,
            "visibleFrom": 1677678545521,
            "visibleTill": 2208988800000
        },
        "assetSource": "SPRINKLR",
        "actionStats": {},
        "shareConfigs": [
            {
                "type": "CLIENT",
                "ids": [
                    "2"
                ]
            },
            {
                "type": "CLIENT_GROUP",
                "ids": []
            },
            {
                "type": "USER",
                "ids": []
            },
            {
                "type": "USER_GROUP",
                "ids": []
            }
        ],
        "restricted": false,
        "createdTime": 1677679349978,
        "modifiedTime": 1677679349978,
        "approvedByUser": 600004599,
        "createdByUser": 600004599
    },
    "eventTime": 1677679350016,
    "subscriptionDetails": {
        "subscriptionId": "63fddf5fd7bd390c232decb4"
    }
}





### template.asset.updated Webhook - HSM Template




  Copy Code



{
    "id": "640063c30fffef02c389170b",
    "type": "template.asset.updated",
    "payload": {
        "assetType": "TEMPLATE_ASSET",
        "templateAsset": {
            "channelType": "WHATSAPP_BUSINESS",
            "templateType": "HSM",
            "elementList": [],
            "buttons": [],
            "attachment": {
                "wabaTemplateId": 592224602777153,
                "namespace": "c361c688_70d9_4f6e_b994_44c19cb9bc1a",
                "wabaId": "1113164986160914",
                "elementName": "elem_name",
                "category": "TRANSACTIONAL",
                "langCode": "bn",
                "buttons": [],
                "wabaTemplateStatus": "APPROVED",
                "rejectedReason": "NONE",
                "message": "MSG1\n",
                "header": {
                    "headerType": "Text",
                    "message": "HEADER"
                },
                "type": "HSM"
            }
        },
        "id": "63ff5af21b00a978efa1ab3d",
        "name": "Mith-WhatsappBusiness-1March23-updated22222",
        "description": "Mith-WhatsappBusiness-1March23",
        "status": "Approved",
        "taxonomy": {
            "clientCustomProperties": {},
            "partnerCustomProperties": {
                "62a1cee720e26714e3988dfc": [
                    "Integrated Marketing"
                ],
                "_c_62cec298ee244a614a39c4b4": [
                    "Business_Function TEST"
                ],
                "5ebe4cf68b112133b824f039": [
                    "Test_Sample10"
                ],
                "_c_5fec3ed893f2057f703713b0": [
"
*l3 fix - Updated*
"
                ],
                "62a1cc6e20e26714e3963731": [
                    "N/A"
                ],
                "5ceb7d74e4b01a09536250b4": [
                    "_Ipod"
                ],
                "_c_617d53f013bf364027ffc901": [
                    "Joey"
                ],
                "5ebe4d128b112133b824f079": [
                    "12123"
                ]
            }
        },
        "insights": {},
        "validity": {
            "expiryTime": 1678284120000,
            "availableFrom": 1677678545521,
            "neverExpire": false,
            "visibleFrom": 1677678545521,
            "visibleTill": 2208988800000
        },
        "assetSource": "SPRINKLR",
        "actionStats": {},
        "shareConfigs": [
            {
                "type": "CLIENT",
                "ids": [
                    "2"
                ]
            },
            {
                "type": "CLIENT_GROUP",
                "ids": []
            },
            {
                "type": "USER",
                "ids": []
            },
            {
                "type": "USER_GROUP",
                "ids": []
            }
        ],
        "restricted": false,
        "createdTime": 1677679349978,
        "modifiedTime": 1677747139250,
        "approvedByUser": 600004599,
        "createdByUser": 600004599
    },
    "eventTime": 1677747139465,
    "subscriptionDetails": {
        "subscriptionId": "63fddf5fd7bd390c232decb4"
    }
}





### template.asset.deleted Webhook - HSM Template





  Copy Code



{
    "id": "640063d00fffef02c38919b3",
    "type": "template.asset.deleted",
    "payload": {
        "assetType": "TEMPLATE_ASSET",
        "templateAsset": {
            "channelType": "WHATSAPP_BUSINESS",
            "templateType": "HSM",
            "elementList": [],
            "buttons": [],
            "attachment": {
                "wabaTemplateId": 592224602777153,
                "namespace": "c361c688_70d9_4f6e_b994_44c19cb9bc1a",
                "wabaId": "1113164986160914",
                "elementName": "elem_name",
                "category": "TRANSACTIONAL",
                "langCode": "bn",
                "buttons": [],
                "wabaTemplateStatus": "APPROVED",
                "rejectedReason": "NONE",
                "message": "MSG1\n",
                "header": {
                    "headerType": "Text",
                    "message": "HEADER"
                },
                "type": "HSM"
            }
        },
        "id": "63ff5af21b00a978efa1ab3d",
        "name": "Mith-WhatsappBusiness-1March23-updated22222",
        "description": "Mith-WhatsappBusiness-1March23",
        "status": "Approved",
        "taxonomy": {
            "clientCustomProperties": {},
            "partnerCustomProperties": {
                "62a1cee720e26714e3988dfc": [
                    "Integrated Marketing"
                ],
                "_c_62cec298ee244a614a39c4b4": [
                    "Business_Function TEST"
                ],
                "5ebe4cf68b112133b824f039": [
                    "Test_Sample10"
                ],
                "_c_5fec3ed893f2057f703713b0": [
"
*l3 fix - Updated*
"
                ],
                "62a1cc6e20e26714e3963731": [
                    "N/A"
                ],
                "5ceb7d74e4b01a09536250b4": [
                    "_Ipod"
                ],
                "_c_617d53f013bf364027ffc901": [
                    "Joey"
                ],
                "5ebe4d128b112133b824f079": [
                    "12123"
                ]
            }
        },
        "insights": {},
        "validity": {
            "expiryTime": 1678284120000,
            "availableFrom": 1677678545521,
            "neverExpire": false,
            "visibleFrom": 1677678545521,
            "visibleTill": 2208988800000
        },
        "assetSource": "SPRINKLR",
        "actionStats": {},
        "shareConfigs": [
            {
                "type": "CLIENT",
                "ids": [
                    "2"
                ]
            },
            {
                "type": "CLIENT_GROUP",
                "ids": []
            },
            {
                "type": "USER",
                "ids": []
            },
            {
                "type": "USER_GROUP",
                "ids": []
            }
        ],
        "restricted": false,
        "createdTime": 1677679349978,
        "modifiedTime": 1677747139250,
        "approvedByUser": 600004599,
        "createdByUser": 600004599
    },
    "eventTime": 1677747152243,
    "subscriptionDetails": {
        "subscriptionId": "63fddf5fd7bd390c232decb4"
    }
}





**Dev Notes: **The webhook response payload can vary based on the channel type and template type

### Response Parameters
























-
-
-




****

****

****

| Parameter | Sub-Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- | --- |
| id |  |  | Refers to the unique identifier for the webhook | String |
| type |  |  | Refers to the webhook type.Examples:template.asset.createdtemplate.asset.updatedtemplate.asset.deleted | String |
| payload |  |  | Object containing the case details details | Object |
|  | assetType |  | Refers to the type of the assetExample:TEMPLATE_ASSET | String |
|  | templateAsset |  | Refers to the object containing the asset details | Object |
|  |  | channelType | Refers to the channel type for the template | String |
|  |  | templateType | Refers to type of template for the respective channel type | String |
|  |  | elementList | Refers to the list of items in the template | Array |
|  |  | buttons | Refers to the array containing the button details if any | Array |
|  |  | attachment | Refers to object containing the attachment details for the templateThe attachment details are channel and template specific | Object |
|  | id |  | Refers to the unique identifier for the template | String |
|  | name |  | Refers to the name of the template | String |
|  | description |  | Refers to the description of the template | String |
|  | status |  | Refers to the status of the templateExample:Approved, Pending, etc. | String |
|  | taxonomy |  | Refers to the object containing the taxonomy details | Object |
|  |  | clientCustomProperties | Refers to the object containing the key and value pairs for workspace level custom properties | Object |
|  |  | partnerCustomProperties | Refers to the object containing the key and value pairs for global level custom properties | Object |
|  | insights |  | Object containing the additional insights for the template if any | Object |
|  | validity |  | Object containing the asset validity details | Object |
|  |  | expiryTime | Refers to the time at which the template asset will expire | Epoch |
|  |  | availableFrom | Refers to the time from which the asset will be available for use | Epoch |
|  |  | neverExpire | If true, the asset will be valid forever and won't expire | Boolean |
|  |  | visibleFrom | Refers to the time from which the asset will be visible | Epoch |
|  |  | visibleTill | Refers to the time until when the template asset will be visible | Epoch |
|  | assetSource |  | Refers to the source of the assetDefault: Sprinklr | String |
|  | actionStats |  | Object defining the actions taken on the asset (if any) | Object |
|  | shareConfigs |  | Array containing the asset visibility permissions | Array |
|  |  | type | Refers to the user type having the permissions | String |
|  |  | id | Refers to the list of corresponding Ids for client groups, workspaces, users, and user groups having the permissions to view the asset | List [String] |
|  | restricted |  | If true, the asset is restricted to be used | Boolean |
|  | createdTime |  | Refers to the time at which the asset was created | Epoch |
|  | modifiedTime |  | Refers to the time at which the asset was last modified | Epoch |
|  | approvedByUser |  | Refers to the user id associated with the user who approved the asset | Integer |
|  | createdByUser |  | Refers to the user id associated with the user who created the asset | Integer |
| eventTime |  |  | Refers to the time at which the event took place | Epoch |
| subscriptionDetails |  |  | Refers to the object containing the webhook subscription details | Object |
|  | subscriptionId |  | refers to the unique identifier for the webhook subscription | String |

[](https://dev.sprinklr.com/template-asset-webhooks)

[Back to top](https://dev.sprinklr.com/template-asset-webhooks)
