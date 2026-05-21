---
title: "Create URL Shortener"
slug: create-url-shortener
url: https://dev.sprinklr.com/create-url-shortener
---

# Create URL Shortener

#
POST  Create URL Shortener



You can use this api to create vanity and non vanity short links and in response you will get the shortened URL and other related objects after making the Request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/link/shorten

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

###  Request Parameters



















			[read URL Shorteners API](https://dev.sprinklr.com/read-url-shortener)










| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| link | Required | Refers to the link that needs to be shortened | URL |
| urlShortenerId | Required | Refers to the unique identifier for the url shortener. You can fetch the url shortener Id using | String |
| name | Optional | Refers to the name of the URL shortener | String |

**Note: **
To create a Vanity URL you need to provide `name` in the request body and the `urlShortnerId` should have the capability to create vanity.
You can check for `"canUseForVanityLink": true` in the [Read URL Shortener](https://dev.sprinklr.com/read-url-shortener) api call response and can use the one which have this property true.

## Example - Without Vanity Url















Copy Code



curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/link/shorten' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "link": "https://Sprinklr.com",
    "urlShortenerId": "569a4628e4b0c22f27c8de09"
}'






## Example - Response





{
    "data": {
        "id": 101612830,
        "urlShortenerId": "569a4628e4b0c22f27c8de09",
        "linkHash": "101612830",
        "originalLink": "https://Sprinklr.com",
        "shortLink": "http://spr.ly/101612830",
        "campaignId": -11
    },
    "errors": []
}







## Example - With Vanity Url















Copy Code



curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/link/shorten' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "link": "https://Sprinklr.com",
    "urlShortenerId": "569a4628e4b0c22f27c8de09",
    "name": "Sprinklr"
}'






## Example - Response





{
    "data": {
        "id": 101614388,
        "urlShortenerId": "569a4628e4b0c22f27c8de09",
        "linkHash": "Sprinklr",
        "originalLink": "https://Sprinklr.com",
        "shortLink": "http://spr.ly/Sprinklr",
        "campaignId": -10,
        "domain": "spr.ly"
    },
    "errors": []
}







 [](https://dev.sprinklr.com/create-url-shortener)




[Back to top](https://dev.sprinklr.com/create-url-shortener)
