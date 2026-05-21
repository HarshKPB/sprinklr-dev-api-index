---
title: "Secure Media Download"
slug: secure-media-download
url: https://dev.sprinklr.com/secure-media-download
---

# Secure Media Download

#
  GET  Secure Media Download

	Using this API, you can regenerate time-bound accessible URLs by passing expired URL in the path parameter.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/secure-assets/fetch/{secureUrl}

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

### Path Parameters

****``

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| secureUrl | Required | Refers to the secure url for Sprinklr media asset (image, video, audio, PDFs, etc.)Note: The url should be url-encoded | url |

### Example - Request




 Copy Code



curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/secure-assets/fetch/https%3A%2F%2Fstorage.googleapis.com%2Fspr-qa6-cdn-secure%2FDAM%2F60000%2Fe85230-6404-4d01-a7cd-16b21da894a1-2036103%2F36f1061b-b2da-44f-9598-7628a9.jpg' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
 

### Example - Response




{
    "data": "https://storage.googleapis.com/spr-qa6-cdn-secure/DAM/66000000/e8795230-6404-4d01-a7cd-16b21da894a1-2032016103/36f1061b-b2da-4c4f-9598-7628a9.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=qa6-gcs-sa%40gc-qa6.iam.gserviceaccount.com%2F20250110%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250110T085828Z&X-Goog-Expires=5400&X-Goog-SignedHeaders=host&X-Goog-Signature=73cca131cb1d0d7286dd4a5405d789626f4a8a33ffc883aebfcfafe8acc5dcc81fba587dfc0c8f9b6835b0f92a934b7307be1d547c04f73166016506689a9585e33d743d9e4952b07ffa9777c1b7b1bb1d1c44e9334cec752fbe98e6b702c0d45349e78247d4e6e27bdde1d2dea3a7aef215158a911350ac7d322e5f1d615fe496c81ed5e6dd91bc5c5ca795dbddad455a70bcb30d8f049766180ab1500505441c5e76e8f32c63fac2b50b650d68069c38a88a45203e897329dd0543ae539e510798162271ec229b730f8fda5ad1fd94b2ea3034ef3ab892102fa25eaf35795a0f01d88b2c28deebcc1cf69f93459024bc960a3eefe9",
    "errors": []
}
 

     
     
   

**Dev Notes: **The  accessible url generated in the response will be time-bound. Once the above link expires, you can regenerate the accessible URL by calling the API mentioned above.

[](https://dev.sprinklr.com/secure-media-download) 

 

 
[Back to top](https://dev.sprinklr.com/secure-media-download)
