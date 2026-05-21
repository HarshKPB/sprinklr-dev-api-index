---
title: "Create Campaign v1"
slug: create-campaign-v1
url: https://dev.sprinklr.com/create-campaign-v1
---

# Create Campaign v1

#
  POST Create Campaign v1




Campaigns are used in Sprinklr as primary tags to categorize outbound messages for Reporting. When you create a new campaign using this API call, those campaigns will be available to select when publishing content from Sprinklr.

Use [Bootstrap](https://dev.sprinklr.com/bootstrap-resources-v1) for configuration information.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v1/campaign/create

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














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







| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| name | Required | Name of the Campaign. | String |
| description | Optional | Description of the Campaign. Not exceeding 500 characters. | String |
| startDate | Required | Campaign Start date in the epoch. | Long |
| endDate | Optional | Campaign End date in the epoch. | Long |
| CampaignStatus | Required | Status of the campaign (DRAFT, APPROVED, EXPIRED). | String |
| tags | Optional | List of tags. | List<String> |
| clientCustomProperties | Optional | You can customize Client custom properties in a Campaign as per your need. | Map<String>,List<String> |
| partnerCustomProperties | Optional | Partner custom properties can be customized and configured per your need. | Map<String>,List<String> |
| campaignOwnerId | Optional | Campaign owner Id. | Long |
| color | Optional | Color to be set for the campaign. Will be displayed in the UI. | String |
| shareConfigs | Optional | List of asset share configs. | List<AssetShareConfig> |

## Example - Request















Copy Code


 curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/campaign/create' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
    "name": "Campaign Name 3",
    "color": "#eadef0",
    "description": "Description of the Campaign",
    "campaignOwnerId": 1000061632,
    "startDate": "1513596840000",
    "endDate": "1513769640000",
    "campaignStatus": "DRAFT",
    "tags": [],
    "visibility": {
        "shareConfigs": [{
            "shareLevel": "CLIENT",
            "sharedWithIds": ["1000004845"]
        }, {
            "shareLevel": "CLIENT_GROUP",
            "sharedWithIds": []
        }]
    },
    "shareConfigs": [{
        "shareLevel": "USER",
        "sharedWithIds": ["1000004845"]
    }, {
        "shareLevel": "USER_GROUP",
        "sharedWithIds": []
    }],
    "partnerCustomProperties": {
        "spr_campaign_goal": ["Goal 1", "Goal 2"],
        "customPropertyFieldName": ["Value 1"]
    },
    "clientCustomProperties": {
        "1000004845": {
            "customPropertyFieldName": ["Value 1"]
        }
    }
}'






## Example - Response




 {
   "data":[
      {
    "id": "1_11394",
    "name": "Campaign Name 3",
    "description": "Description of the Campaign",
    "archived": false,
    "hasSubCampaign": false,
    "hasContentBrief": false,
    "campaignStatus": "DRAFT",
    "startDate": 1513596840000,
    "endDate": 1513769640000,
    "allDay": false,
    "tags": [],
    "clientCustomProperties": {
        "1000004845": {
            "customPropertyFieldName": [
                "Value 1"
            ]
        }
    },
    "partnerCustomProperties": {
        "spr_campaign_goal": [
            "Goal 1",
            "Goal 2"
        ],
        "customPropertyFieldName": [
            "Value 1"
        ]
    },
    "campaignOwnerId": 600000001,
    "eventType": false,
    "gmcEnabled": false,
    "color": "#eadef0",
    "autoImportCampaign": false,
    "external": false,
    "phaseList": [],
    "additional": {},
    "privateCampaign": false,
    "locked": false,
    "processInitiated": false,
    "influencerCampaign": false,
    "favoritedForCurrentUser": false,
    "flattenedShareConfig": [
        "USER/1000004845"
    ],
    "flavours": [],
    "campaignFlavourDetailsMap": {},
    "searchSummary": "Campaign Name 3 Description of the Campaign",
    "additionalInformation": {
        "ownerNameLC": "chandrashekharma jinka(su) ",
        "campaignDescriptionLC": "description of the campaign",
        "ownerName": "Chandrashekharma Jinka(SU) ",
        "campaignNameLC": "campaign name 3",
        "rCP": {
            "flatCustomProperties": [
                "ALLµcustomPropertyFieldNameµValue 1",
                "ALL",
                "ALLµspr_campaign_goalµGoal 1",
                "ALLµspr_campaign_goalµGoal 2",
                "ALLµspr_campaign_goal",
                "ALLµcustomPropertyFieldName"
            ],
            "customPropertyNames": [
                "spr_campaign_goal",
                "customPropertyFieldName"
            ],
            "mappedCustomProperties": {
                "spr_campaign_goal": [
                    "Goal 1",
                    "Goal 2"
                ],
                "customPropertyFieldName": [
                    "Value 1",
                    "Value 1"
                ]
            },
            "mappedControllingCustomPropertyList": [
                {
                    "fields": [
                        "5f6b9df191de3028c4c7e5f8",
                        "5f6b9df191de3028c4c7e5f2"
                    ],
                    "properties": {}
                },
                {
                    "fields": [
                        "_c_60ed815aff3b6d13b4c78ac1",
                        "5f6b9df191de3028c4c7e5e0"
                    ],
                    "properties": {}
                },
                {
                    "fields": [
                        "_c_60ed9174ff3b6d13b4c7d5b2",
                        "5f6b9df191de3028c4c7e5e0"
                    ],
                    "properties": {}
                },
                {
                    "fields": [
                        "_c_6194d1866317ad7b91e6701c",
                        "_c_622af6d206c315679d108956"
                    ],
                    "properties": {}
                },
                {
                    "fields": [
                        "_c_6316f79f3cd19c6584c941f7",
                        "_c_6311e57408d19414ad819b77"
                    ],
                    "properties": {}
                }
            ],
            "customProperties": [
                {
                    "key": "spr_campaign_goal",
                    "values": [
                        "Goal 1",
                        "Goal 2"
                    ]
                },
                {
                    "key": "customPropertyFieldName",
                    "values": [
                        "Value 1",
                        "Value 1"
                    ]
                }
            ]
        }
    },
    "userAccessible": true,
    "versionId": 0,
    "shareConfigs": [
        {
            "shareLevel": "USER",
            "sharedWithIds": [
                "1000004845"
            ]
        },
        {
            "shareLevel": "USER_GROUP",
            "sharedWithIds": []
        }
    ],
    "grants": [
        "CLIENT/1/OWNERSHIP",
        "USER/600000001/OWNERSHIP"
    ],
    "clientId": 1,
    "ownerUserId": 600000001,
    "createdTime": 1663603974122,
    "modifiedTime": 1663603974120,
    "deleted": false,
    "canEdit": true
}





	[](https://dev.sprinklr.com/create-campaign-v1)






[Back to top](https://dev.sprinklr.com/create-campaign-v1)
