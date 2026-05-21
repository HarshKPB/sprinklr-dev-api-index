---
title: "Read Campaign"
slug: read-campaign
url: https://dev.sprinklr.com/read-campaign
---

# Read Campaign

#
  GET Read Campaign

You can fetch Campaign via this API call and you will get the data corresponds a Campaign {Id} and other related objects as Response after making the Request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/campaign/{campaignId}

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

### Request Parameter















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {campaignId} | Required | Campaign Id for which you want to fetch details. | String |

## Example - Request














Copy Code




curl -X GET \
  https://api3.sprinklr.com/{env}/api/v2/campaign/{campaignId} \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'





## Example - Response





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
}





### Response Parameters


































































































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

 [](https://dev.sprinklr.com/read-campaign)




[Back to top](https://dev.sprinklr.com/read-campaign)
