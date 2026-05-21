---
title: "Fetch All Campaign"
slug: fetch-all-campaign
url: https://dev.sprinklr.com/fetch-all-campaign
---

# Fetch All Campaign

#
  GET Fetch All Campaign

You can use this API to fetch all Campaign.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/campaign

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)


``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Accept | application/json | Determines the acceptable response type from the server |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
     
 
curl -X GET \
  https://api3.sprinklr.com/{env}/api/v2/campaign \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






## Example - Response





{
    "data": [
        {
            "id": "string",
            "name": "string",
            "displayId": "string",
            "parentCampaignId": "string",
            "description": "string",
            "startDate": 0,
            "endDate": 0,
            "createdTime": 0,
            "modifiedTime": 0,
            "tags": [
                "string"
            ],
            "owner": "string",
            "status": "string",
            "archived": false,
            "deleted": false,
            "partnerCustomProperties": {
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
            "clientCustomProperties": {
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
            "externalSource": "string",
            "externalSourceId": "string"
        }
    ],
    "errors": []
}







### Response Definition
























































































































| Parameter | Description | Type |
| --- | --- | --- |
| id | Id of the campaign. | String |
| name | Name of the campaign. | String |
| displayId | The Display Id in case of sub campaign. | String |
| parentCampaignId | The Parent campaign Id in case of sub campaign. | String |
| description | Description of campaign. | String |
| createdTime | Campaign created time in Sprinklr. | Integer |
| modifiedTime | last modified time of campaign in Sprinklr. | Integer |
| startDate | Start date of campaign. | integer |
| endDate | End date of campaign. | integer |
| tags | Tags on the campaign. | String |
| owner | Owner of the campaign. | Integer |
| status | Status of the campaign. e.g. Draft, Approved. | String |
| archived | True if campaign is archived.default: false | Boolean |
| partnerCustomFields | Partner level custom fields on the campaign. | Map<String, List<String>> |
| clientCustomFields | Partner level custom fields on the campaign. | Map<String, List<String>> |
| externalSource | The External system name. | String |
| externalSourceId | The External system Id. | String |

 [](https://dev.sprinklr.com/fetch-all-campaign)






[Back to top](https://dev.sprinklr.com/fetch-all-campaign)
