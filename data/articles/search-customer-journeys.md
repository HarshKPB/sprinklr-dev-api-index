---
title: "Search Customer Journeys"
slug: search-customer-journeys
url: https://dev.sprinklr.com/search-customer-journeys
---

# Search Customer Journeys

#
  POST  Search Customer Journeys


Using this API you can search for existing customer journeys based on the given filters.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/marketing-journey/search

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

## Request Parameters












****

****

****

****

****

| Parameter | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| query |  | Optional | Refers to the search keyword for the journey name | String |
| sorts |  | Optional | Refers to the array containing the sorting information based on which you want to sort the response | Array |
|  | key | Required | Refers to the key (unique identifier) on which you want to sort the resultsSupported keys: name, tags, createdAt, modifiedTime | String |
|  | order | Optional | Refers to the order based on which you want to sort the resultsSupported orders: ASC, DESC | String |
| page |  | Required | Refers to the object containing the pagination information | Object |
|  | size | Required | Refers to the number of response you wish to receive per API hit | Integer |
|  | page | Optional | Refers to the page number you want the results fromDefault Page Size: 0 | Integer |
| filters |  | Optional | Refers to the array containing the filtering details | Array |
|  | filterType | Required | Refers to the filter operator typeSupported values:IN | String |
|  | field | Required | Refers to the journey field based on which you want to filter the dataSupported fields: name, campaignId, createdAt, modifiedTime, ownerUserId, status, smartSegmentId |  |
|  | values | Required | Refers to the list of values matching the value passed in the field parameter | List [String, Integer] |

**Dev Notes: **For fetching all the existing customer journeys at once, send empty curly brackets `{ }` in the API request.

## Example - Request















Copy Code



	curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/marketing-journey/search' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
	"sorts": [
		{
			"key": "name",
			"order": "DESC"
		}
	],
	"query": "",
	"page": {
		"size": 5,
		"page": 0
	},
	"filters": [
		{
			"filterType": "IN",
			"field": "ownerUserId",
			"values": [
				1000101995
			]
		}
	]
}'






## Example - Response





{
    "data": {
        "data": [
            {
                "id": "60485dbaa1e3cd322760084a",
                "name": "ss",
                "campaignId": "EXCLUDED_EXPIRED_CAMPAIGN_ID",
                "createdAt": 1615355322284,
                "modifiedTime": 1615355322284,
                "ownerUserId": 1000101995,
                "status": "ACTIVE",
                "deliverSettings": {},
                "journeyEntryPoint": {
                    "entryPointDetails": {
                        "smartSegmentId": "6045cbdd7bede32995d87e0c"
                    },
                    "entryType": "SMART_SEGMENT"
                },
                "oneTimeJourney": false,
                "processDefinitionId": "60485dbaa1e3cd322760084b",
                "processDefinitionFlavour": "MARKETING_JOURNEY",
                "shareConfigs": [
                    {
                        "shareLevel": "GLOBAL"
                    }
                ]
            },
            {
                "id": "60472603e9681c2bee77673b",
                "name": "saurav_agent",
                "campaignId": "EXCLUDED_EXPIRED_CAMPAIGN_ID",
                "createdAt": 1615275523875,
                "modifiedTime": 1615275523875,
                "ownerUserId": 1000101995,
                "status": "ACTIVE",
                "deliverSettings": {},
                "journeyEntryPoint": {
                    "entryPointDetails": {
                        "smartSegmentId": "6045cbdd7bede32995d87e0c"
                    },
                    "entryType": "SMART_SEGMENT"
                },
                "oneTimeJourney": false,
                "processDefinitionId": "60472603e9681c2bee77673c",
                "processDefinitionFlavour": "MARKETING_JOURNEY",
                "shareConfigs": [
                    {
                        "shareLevel": "GLOBAL"
                    }
                ]
            }
        ],
        "count": 52,
        "hasMore": true
    },
    "errors": []
}






	[](https://dev.sprinklr.com/search-customer-journeys)




[Back to top](https://dev.sprinklr.com/search-customer-journeys)
