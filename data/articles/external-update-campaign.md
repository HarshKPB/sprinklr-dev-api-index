---
title: "External Update Campaign"
slug: external-update-campaign
url: https://dev.sprinklr.com/external-update-campaign
---

# External Update Campaign

#
  PUT - External Update Campaign


You can Update an external Campaign with this API call using the Campaign{Id}.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/campaign/{externalSource}/{externalId}

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
| externalSource | Required | Name of extenal source. | String |
| externalSourceId | Required | Id of the external source. | String |

## Request Parameters
















































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



curl -X PUT \
  https://api3.sprinklr.com/{env}/api/v2/campaign/{externalSource}/{externalId} \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Auto Camp 02",
        "description": "Verify the campaign",
        "startDate": 1560159652000,
        "externalSource": "CAMPAIGN_PORTAL",
        "externalSourceId": "dgsg3456y45tygvcd3456tyhgfde3456yhfgfd_01",
        "tags": [
            "Int Tag_02",
            "Campaign Tag_02"
        ],
     "status": "APPROVED"
    }'



## Example - Response




{
        "id": "2_1481",
        "name": "Auto Camp 02",
        "description": "Verify the campaign",
        "createdTime": 1576595206438,
        "modifiedTime": 1576595645051,
        "startDate": 1560159652000,
        "tags": [
            "Int Tag_02",
            "Campaign Tag_02"
        ],
        "owner": 600000788,
        "clientCustomProperties": {},
        "status": "APPROVED",
        "archived": false,
        "externalSource": "CAMPAIGN_PORTAL",
        "externalSourceId": "dgsg3456y45tygvcd3456tyhgfde3456yhfgfd_01"
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
| tags | Tags on the campaign. | String |
| owner | Owner of the campaign. | Integer |
| status | Status of the campaign. e.g. Draft, Approved. | String |
| archived | True if campaign is archived.default: false | Boolean |
| clientCustomFields | Partner level custom fields on the campaign. | String |
| externalSource | Name of extenal source. | String |
| externalSourceId | Id of the external source. | String |

 [](https://dev.sprinklr.com/external-update-campaign)






[Back to top](https://dev.sprinklr.com/external-update-campaign)
