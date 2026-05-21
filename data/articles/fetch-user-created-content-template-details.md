---
title: "Fetch User-Created Content Template Details"
slug: fetch-user-created-content-template-details
url: https://dev.sprinklr.com/fetch-user-created-content-template-details
---

# Fetch User-Created Content Template Details

#
GET Fetch User-Created Content Template Details

This API helps fetch the user-created content template details using the template Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/contentTemplate/{templateId}

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
  'https://api3.sprinklr.com/{env}/api/v2/contentTemplate/626ea2b03e29aa260a93' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
 

     
     
   

## Example - Response

 
 
     
 
     {
     "data": {
        "id": "626ea2b03e29aa260a93",
        "name": "MessageBrief",
        "content": "Hello World",
        "smartTemplate": true,
        "templateType": "CONTENT_BRIEF",
        "assetClass": "CONTENT_BRIEF",
        "publisherStatus": "completed",
        "version": 0,
        "templateVersionInfo": "0.0.1",
        "editDisabled": false,
        "archived": false,
        "report": "CONTENT_TEMPLATE",
        "governance": {
            "visibility": {
                "shareConfigs": [
                    {
                        "shareLevel": "CLIENT",
                        "sharedWithIds": [
                            "4817"
                        ]
                    },
                    {
                        "shareLevel": "CLIENT_GROUP",
                        "sharedWithIds": []
                    }
                ],
                "globallyVisible": false
            }
        },
        "clientId": 4801,
        "ownerUserId": 96576,
        "createdTime": "May 1, 2022 3:09:36 PM",
        "modifiedTime": "May 1, 2022 3:11:18 PM",
        "lastModifiedUserId": 96576,
        "deleted": false,
        "canEdit": false
    },
    "errors": []
}
 

     
     
   
 

### Response Parameters

























****


| Parameters | Description | Type |
| --- | --- | --- |
| id | The id of the template passed in the request | String |
| name | The name of the template | String |
| content | The content of the template | String |
| templateType | Defines the type of template Example: CONTENT_BRIEF, CARD_ASSET, CONTENT_TEMPLATE, FEEDBACK, FEED_TEMPLATE, IMAGE_EDITOR, MEDIA_ASSET |  |

**Dev Notes: **The other response parameters vary from template to template. The details depend on the template details set in the UI.

	[](https://dev.sprinklr.com/fetch-user-created-content-template-details) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-user-created-content-template-details)
