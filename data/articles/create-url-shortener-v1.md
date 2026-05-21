---
title: "Create URL Shortener - v1"
slug: create-url-shortener-v1
url: https://dev.sprinklr.com/create-url-shortener-v1
---

# Create URL Shortener - v1

#
  POST - Create URL Shortener

Using this API, you can shorten the given long URL.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/link/shorten

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



















			[Bootstrap resources](https://dev.sprinklr.com/bootstrap-resources-v1)

[Read URL Shorteners API](https://dev.sprinklr.com/read-url-shortener)




| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| link | Required | The link to shorten | String |
| urlShortnerId | Required | You can fetch the shortnerId from  (type: PARTNER_URL_SHORTNERS [global-level] or CLIENT_URL_SHORTNERS [workspace-level] ).Alternatively, you can use  to fetch the urlShortnerId | String |

## Example

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
	'https://api3.sprinklr.com/{env}/api/v1/link/shorten' \
	-H 'Authorization: Bearer {token}' \
	-H 'Content-Type: application/json' \
	-H 'cache-control: no-cache' \
	-H 'key: {apikey}' \
	-d '{
		"link": "https://dev.sprinklr.com",
		"urlShortnerId": "5547_spr.ly"
	}'
 

     
     
   
 
 
     

"http://spr.ly/6002Ez4Wa"
 

     
     
   
 
[](https://dev.sprinklr.com/create-url-shortener-v1) 

 

 
[Back to top](https://dev.sprinklr.com/create-url-shortener-v1)
