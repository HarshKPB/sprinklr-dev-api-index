---
title: "Update Campaign"
slug: update-campaign
url: https://dev.sprinklr.com/update-campaign
---

# Update Campaign

#
  PUT - Update Campaign

You can Update a Campaign with this API call using the  external source and source{Id}.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/campaign/{campaignId}

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

### Path Parameter
















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {campaignId} | Required | Campaign Id of the campaign that needs to be updated. | String |

## Request Parameters








































































































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



curl -X PUT \
  https://api3.sprinklr.com/{env}/api/v2/campaign/{campaignId} \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
  "name": "string",
  "description": "string",
  "startDate": 0,
  "endDate": 0,
  "tags": [
    "string"
  ],
  "status": "string",
  "archived": false,
  "partnerCustomFields": {
    "additionalProp1": [
      "string"
    ],
    "additionalProp2": [
      "string"
    ],
    "additionalProp3": [
      "string"
    ]
  },
  "clientCustomFields": {
    "additionalProp1": [
      "string"
    ],
    "additionalProp2": [
      "string"
    ],
    "additionalProp3": [
      "string"
    ]
  }
}'





## Example - Response




{
   "id":"string",
   "name":"string",
   "description":"string",
   "createdTime":0,
   "modifiedTime":0,
   "startDate":0,
   "endDate":0,
   "tags":[
      "string"
   ],
   "owner":0,
   "partnerCustomFields":{
      "additionalProp1":[
         "string"
      ],
      "additionalProp2":[
         "string"
      ],
      "additionalProp3":[
         "string"
      ]
   },
   "clientCustomFields":{
      "additionalProp1":[
         "string"
      ],
      "additionalProp2":[
         "string"
      ],
      "additionalProp3":[
         "string"
      ]
   },
   "status":"string",
   "archived":false
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
| owner | Owner of the campaign. | Integer |
| status | Status of the campaign. e.g. Draft, Approved. | String |
| archived | True if campaign is archived.default: false | Boolean |
| partnerCustomFields | Partner level custom fields on the campaign. | String |
| clientCustomFields | Partner level custom fields on the campaign. | String |

 [](https://dev.sprinklr.com/update-campaign)




[Back to top](https://dev.sprinklr.com/update-campaign)
