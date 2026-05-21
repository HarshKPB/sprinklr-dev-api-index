---
title: "Lookup By Dimension"
slug: lookup-by-dimension
url: https://dev.sprinklr.com/lookup-by-dimension
---

# Lookup By Dimension

#
  POST Lookup By Dimension




Lookup API helps find details of different entities based on the lookup type. For example, you can search for locations Ids using `FACEBOOK_PLACES_LOOKUP` as lookup type will get a unique location ID for every location.


**Dev Note: ** Supported lookup types: `ACCOUNT_ID`, `PARTNER_USERS`, `USER`, `CASE_ID`, `CUSTOM_FIELD`, `FACEBOOK_PLACES_LOOKUP` (only for Instagram), `SMART_SEGMENT_ID`, `CATALOG`

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/lookup/byDimensions

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





















































| Parameters | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| Filters |  | Required | Creates a new array of elements that pass the test implemented within the provided function | Array |
| dimensionLookups |  | Required | The array of objects that contain the query details. | Array |
|  | LookupType | Required | Required for lookup endpoint requestsKindly refer to the table below for supported lookup types | String |
|  | Query | Required | The first four letters of the location you are looking for | String |
|  | Page{                         page                         size                         } | Page: Optional                                                  Size: Required | When the number of responses are large, page request helps limit the number of items in the response{Page helps specify the page number you want in the response. If                           no page number is provided, the first page results are displayed by default.Size helps specify the maximum number of results that will be shown in a response.} | Integer |

### Example for lookupType: FACEBOOK_PLACES_LOOKUP















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/lookup/byDimensions' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
	"filters": [],
	"dimensionLookups": [
		{
			"lookupType": "FACEBOOK_PLACES_LOOKUP",
			"query": "cali",
			"page": {
				"page": 0,
				"size": 1
			}
		}
	]
}'






**Dev Notes: **For Instagram the lookup type will be:

"lookupType": `"FACEBOOK_PLACES_LOOKUP"`





{
        "FACEBOOK_PLACES_LOOKUP": {
            "hasMore": true,
            "result": [
                {
                    "id": "84115026000887",
                    "name": "ABC",
                    "address": "United States",
                    "location": {
                        "city": "Denver",
                        "state": "CO",
                        "country": "United States",
                        "zip": "80219",
                        "latitude": 39.71184,
                        "longitude": -105.02464,
                        "street": "253 S Federal Blvd"
                    }
                }
            ]
        }
    },
    "errors": []
}







Once you have the locationId, the next step is to publish a post by passing the locationId in the request payload. Here’s a document for [publishing a post](https://dev.sprinklr.com/publishing-post).

### Example for lookupType: ACCOUNT_ID















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/lookup/byDimensions' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "filters": [],
    "dimensionLookups": [
        {
            "lookupType": "ACCOUNT_ID",
            "query": "Twitter",
            "page": {
                "page": 0,
                "size": 1
            }
        }
    ]
}'










{
    "data": {
        "ACCOUNT_ID": {
            "hasMore": true,
            "result": [
                {
                    "id": "1000069394",
                    "type": "TWITTER",
                    "displayName": "1kg12cs0351",
                    "channelId": "788251714138669056",
                    "owner": 1000055211,
                    "properties": "{\"orgProfImgUrl\":\"https:\/\/abs.twimg.com\/sticky\/default_profile_images\/default_profile_normal.png\",\"relayEnabled\":\"true\",\"coverImageUrl\":\"https:\/\/pbs.twimg.com\/profile_banners\/788251714138669056\/1534852880\/1500x500\"}",
                    "channelType": "TWITTER",
                    "spaceId": 1000004509,
                    "partnerCustomProperties": {
                        "_c_61a5c6b1637af95d68d8cf21": [
                            "Testing 123"
                        ],
                        "_c_61968f6f92d9691cfc2c5fb0": [
                            "Joey"
                        ]
                    },
                    "permalink": "https://twitter.com/1kg12cs0351",
                    "active": true,
                    "deactivationReason": "",
                    "deleted": false,
                    "createdTime": "2016-10-24 09:47:03.0",
                    "modifiedTime": "2023-04-11 09:53:12"
                }
            ]
        }
    },
    "errors": []
}






[](https://dev.sprinklr.com/lookup-by-dimension)
