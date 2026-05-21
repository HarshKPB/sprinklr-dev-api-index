---
title: "Fetch Standard Content Template Details"
slug: fetch-standard-content-template-details
url: https://dev.sprinklr.com/fetch-standard-content-template-details
---

# Fetch Standard Content Template Details

#
GET Fetch Standard Content Template Details

This API helps fetch standard content template details using the template Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/contentTemplate/{templateId}?fromGlobal=true

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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/contentTemplate/{templateId}?fromGlobal=true' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
 

     
     
   

## Example - Response

 
 
     
 
{
   "data": {
       "id": "626ea2b03e29aa260a93",
       "name": "Test Standard Template",
       "channelType": "TWITTER",
       "templateType": "CARD_ASSET",
       "height": 480,
       "width": 960,
       "assetClass": "MEDIA_ASSET",
       "locationUrl": "https://qa4-spx-components.cdn.sprinklr.com/components/twitter/multiDestinationWebsite/0.0.12",
       "publisherStatus": "standard_template",
       "contentType": "MULTI_DESTINATION_WEBSITE",
       "additional": {
           "TEMPLATE_CATEGORY": [
               "MULTI_DESTINATION_WEBSITE"
           ]
       },
       "guid": "15cbb0ba-7edb-40b4-b66c-647fb8231fe6",
       "version": 11,
       "templateVersionInfo": "0.0.12",
       "editDisabled": false,
       "filterDisplayName": "Twitter Multi Destination Image Carousel Card",
       "archived": false,
       "report": "CONTENT_TEMPLATE",
       "governance": {
           "visibility": {
               "globallyVisible": true
           }
       },
       "clientId": 0,
       "ownerUserId": 0,
       "createdTime": "Apr 13, 2022 7:28:28 AM",
       "modifiedTime": "Apr 13, 2022 7:28:28 AM",
       "deleted": false,
       "canEdit": false
   },
   "errors": []
}
 

     
     
   
 

**Dev Notes: **The response parameters vary from template to template. The details depend on the template details present on the backend

	[](https://dev.sprinklr.com/fetch-standard-content-template-details) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-standard-content-template-details)
