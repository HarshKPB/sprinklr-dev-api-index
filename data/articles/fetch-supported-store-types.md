---
title: "Fetch Supported Store Types "
slug: fetch-supported-store-types
url: https://dev.sprinklr.com/fetch-supported-store-types
---

# Fetch Supported Store Types 

#   GET Fetch Supported Store Types
 

While creating Facebook Ads, for the App Promotion Objective, you can send people to the store where they can purchase your app. This endpoint fetches the supported Store Types.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/supportedStoreTypes

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

### Query Parameters













     ``





     ``



| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| adObjective | Optional | It is the specific Objective of the Paid Initiative. It must be set to OUTCOME_TRAFFIC. | String |
| channelType | Optional | It is the channel for which the Paid Initiative has been created. It must be set to FACEBOOK. | String |

## Example - Request




 Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/supportedStoreTypes?adObjective=OUTCOME_TRAFFIC&channelType=FACEBOOK' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Token}’ \
--header 'Key: {API_Key}’



## Example - Response





{
  "data": {
    "google_play": "Google Play",
    "itunes": "App Store",
    "fb_canvas": "Facebook Canvas",
    "itunes_ipad": "App Store for iPad",
    "instant_game": "Instant Games"
  },
  "errors": []
}




### Response Parameters






















































| Parameter | Sub-Parameter | Type | Description |
| --- | --- | --- | --- |
| data |  | Object | Details on the supported store types. |
|  | google_play | String | Display name for the Google Play platform. |
|  | itunes | String | Display name for the Apple App Store platform. |
|  | fb_canvas | String | Display name for the Facebook Canvas platform. |
|  | itunes_ipad | String | Display name for the Apple App Store platform specific to iPad. |
|  | instant_game | String | Display name for the Instant Games platform. |
| errors |  | Array | An array containing error messages or objects, if any. |

[](https://dev.sprinklr.com/fetch-supported-store-types) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-supported-store-types)
