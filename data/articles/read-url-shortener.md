---
title: "Read URL Shortener"
slug: read-url-shortener
url: https://dev.sprinklr.com/read-url-shortener
---

# Read URL Shortener

#
GET Read URL Shortener



You can use this api to read the available URL Shorteners and their Ids and can check the availability of VanityUrl for an Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/link/shorteners

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

## Example - Request















Copy Code



curl -X GET \
   'https://api3.sprinklr.com/{env}/api/v2/link/shorteners' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json'






## Example - Response





{
    "data": [
        {
            "id": "569a4628e4b0cuh98ns1de00",
            "name": "sari",
            "provider": "ARIBE",
            "canUseForVanityLink": false
        },
        {
            "id": "57970f45e4b07auhg45be563",
            "name": "brio_Spr",
            "provider": "Sprinklr",
            "canUseForVanityLink": true
        }
             ],
    "errors": []
}







## Response Parameters











         ``[Shorten Link](https://dev.sprinklr.com/read-url-shortener)


















| Parameter | Description | Type |
| --- | --- | --- |
| id | The id of the shortener provider. You need to use this Id as  urlShortnerId  while using the  api. | String |
| name | The name of the shortener. | String |
| provider | The domain name of the shortener service provider. | String |
| canUseForVanityLink | If true, can be used for vanity url creation. | Boolean |

	[](https://dev.sprinklr.com/read-url-shortener)




[Back to top](https://dev.sprinklr.com/read-url-shortener)
