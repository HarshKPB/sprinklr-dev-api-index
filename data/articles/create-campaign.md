---
title: "Create Campaign"
slug: create-campaign
url: https://dev.sprinklr.com/create-campaign
---

# Create Campaign

#
  POST Create Campaign


Campaigns are used in Sprinklr as primary tags to categorize outbound messages for Reporting. When you create a new campaign using this API call, those campaigns will be available to select when publishing content from Sprinklr.

Use [Bootstrap](https://dev.sprinklr.com/bootstrap-resources-v1) for configuration information.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/campaign

**Dev Notes: **In case of Sub-Campaign creation you need to pass the "parentCampaignId" in the request payload after description.

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

- [Create Campaign](https://dev.sprinklr.com/create-campaign#CC)

- [Create External Campaign](https://dev.sprinklr.com/create-campaign#CEC)

## Create Campaign

You can create a completely new campaign via this API call and will get a Create Campaign {Id} and other related information related to the campaign in response.

### Request Parameters








































































































| Parameter | Sub-Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- | --- |
| name |  | Required | Name of the campaign. | String |
| description |  | Optional | Description of campaign. | String |
| parentCampaignId |  | Optional | Parent campaign Id in case of sub-campaign. | String |
| startDate |  | Optional | Start date of campaign. | Integer |
| endDate |  | Optional | End date of campaign. | Integer |
| tags |  | Optional | Tags on the campaign. | String |
| status |  | Required | Status of the campaign. e.g. Draft, Approved. | String |
| archived |  | Optional | True if campaign is archived. 			default: false | Boolean |
| partnerCustomFields |  | Optional | Partner level custom fields on the campaign. | Map<String, List<String>> |
| clientCustomFields |  | Optional | Partner level custom fields on the campaign. | Map<String, List<String>> |
| visibility |  | Optional | The object containing campaign sharing details. | Object |
|  | globallyVisible | Optional | Accepts true / false, based on this campaign visibility controls globally visible or not. | Boolean |
|  | visibilityConfig | Optional | To define the sharing configuration based on CLIENT,  CLIENT_GROUP, USER, USER_GROUP. All the fields are optional and can be used as per the use case. | <List<String> |

**visibilityConfig Sample: **

```
"visibilityConfig": [
                {
                    "type": "CLIENT",
                    "ids": [ "2" ]
                },
                {
                    "type": "CLIENT_GROUP",
                    "ids": [ "60740690d4644c337059b7a1"]
                },
                {
                    "type": "USER",
                    "ids": [ "600000003" ]
                },
                {
                    "type": "USER_GROUP",
                    "ids": [  "61923d665f0ec3151749d108" ]
                }
            ]

```

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
     
 curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/campaign \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Test Campaign",
    "description": "Testing06",
    "startDate": 1560159652000,
    "endDate": 2209563421000,
    "tags": [
        "Int Tag",
        "Campaign Tag"
    ],
    "status": "APPROVED",
    "partnerCustomFields": {
        "5c35cbf2e4b0e1b05edd1b01": [
            "1"
        ]
    },
    "clientCustomFields": {
        "5ad59e6fe4b024f15e8384ef": [
            "ABC"
        ]
    },
    "visibility": {
        "globallyVisible": "false",
        "visibilityConfig": [
            {
                "type": "CLIENT",
                "ids": ["2"]
            },
            {
                "type": "CLIENT_GROUP",
                "ids": ["60740690d4644c337059b7a1"]
            },
            {
                "type": "USER",
                "ids": ["600000003"]
            },
            {
                "type": "USER_GROUP",
                "ids": ["61923d665f0ec3151749d108"]
            }
        ]
    }
}'
 

     
     
   

## Example - Response





{
    "data": {
        "id": "1_7714",
        "name": "Test Campaign",
        "description": "Testing06",
        "createdTime": 1644921826572,
        "modifiedTime": 1644921826570,
        "startDate": 1560159652000,
        "endDate": 2209563421000,
        "tags": [
            "Int Tag",
            "Campaign Tag"
        ],
        "owner": 600004599,
        "partnerCustomProperties": {
            "5c35cbf2e4b0e1b05edd1b01": [
                "1"
            ]
        },
        "clientCustomProperties": {
            "5ad59e6fe4b024f15e8384ef": [
                "ABC"
            ]
        },
        "status": "APPROVED",
        "visibility": {
            "globallyVisible": false,
            "visibilityConfig": [
                {
                    "type": "CLIENT",
                    "ids": [
                        "2"
                    ]
                },
                {
                    "type": "CLIENT_GROUP",
                    "ids": [
                        "60740690d4644c337059b7a1"
                    ]
                },
                {
                    "type": "USER",
                    "ids": [
                        "600000003"
                    ]
                },
                {
                    "type": "USER_GROUP",
                    "ids": [
                        "61923d665f0ec3151749d108"
                    ]
                }
            ]
        },
        "archived": false,
        "deleted": false
    },
    "errors": []
}







### Response Definition


















































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Id of the campaign. | String |
| name | Name of the campaign. | String |
| description | Description of campaign. | String |
| createdTime | Campaign created time in Sprinklr. | Integer |
| modifiedTime | last modified time of campaign in Sprinklr. | Integer |
| startDate | Start date of campaign. | integer |
| endDate | End date of campaign. | integer |
| tags | Tags on the campaign. | String |
| owner | User Id of the campaign owner. | Integer |
| status | Status of the campaign. e.g. Draft, Approved. | String |
| archived | True if campaign is archived. 			default: false | Boolean |
| partnerCustomFields | Partner level custom fields on the campaign. | String |
| clientCustomFields | Partner level custom fields on the campaign. | String |
| visibility | The object containing the sharing configuration of campaign. | Object |

## Create External Campaign

This call helps create a new campaign on Sprinklr's platform, while it also stores the details of any external campaign, created on a third-party system.

### Request Parameters















































| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| name | Required | Name of the campaign. | String |
| startDate | Optional | Start date of campaign. | Integer |
| externalSource | Required | Name of external source. | String |
| externalSourceId | Required | Id of external source. | String |
| tags | Optional | Tags on the campaign. | String |
| status | Required | Status of the campaign. e.g. Draft, Approved. | String |


## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
     
curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/campaign \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Auto Camp 01",
        "startDate": 1560159652000,
        "externalSource" : "CAMPAIGN_PORTAL",
        "externalSourceId" : "dgsg3456y45tygvcd3456tyhgfde3456yhfgfd_02",
        "tags": [
            "Int Tag01",
            "Campaign Tag01"
        ],
     "status": "APPROVED"
    }'






## Example - Response





{
"data": {
"id": "2_1482",
"name": "Auto Camp 01",
"createdTime": 1576595532163,
"modifiedTime": 1576595532162,
"startDate": 1560159652000,
"tags": [
"Int Tag01",
"Campaign Tag01"
],
"owner": 600000788,
"status": "APPROVED",
"archived": false,
"externalSource": "CAMPAIGN_PORTAL",
"externalSourceId": "dgsg3456y45tygvcd3456tyhgfde3456yhfgfd_02"
},
"errors": []
}
"additionalProp3": [
"string"
]
},
"status": "string",
"archived": false
}





Campaign with already existing "externalSourceId", you will receive error message







"errors": [
        {
            "id": "5df8fcdec6e1aa000166cc8c",
            "code": 400,
            "message": "Campaign already exists with external details : CAMPAIGN_PORTAL - dgsg3456y45tygvcd3456tyhgfde3456yhfgfd_02"
        }
    ]







### Response Definition



































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Id of the campaign. | String |
| name | Name of the campaign. | String |
| createdTime | Campaign created time in Sprinklr. | Integer |
| modifiedTime | last modified time of campaign in Sprinklr. | Integer |
| startDate | Start date of campaign. | integer |
| tags | Tags on the campaign. | String |
| owner | Owner of the campaign. | Integer |
| status | Status of the campaign. e.g. Draft, Approved. | String |
| archived | True if campaign is archived. default: false | Boolean |
| externalSource | Name of external source. | String |
| externalSourceId | Id of external source. | String |

 [](https://dev.sprinklr.com/create-campaign)




[Back to top](https://dev.sprinklr.com/create-campaign)
