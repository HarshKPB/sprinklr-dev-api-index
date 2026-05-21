---
title: "Get Version History by Id"
slug: get-version-history-by-id
url: https://dev.sprinklr.com/get-version-history-by-id
---

# Get Version History by Id

#
  GET - Get Version History by Id



Using this API, you can fetch the version details for the given article version Id

## API Endpoint


https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/version-history/{versionHistoryId}

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












[search version history API](https://dev.sprinklr.com/search-version-history)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| versionHistoryId | Required | Refers to the unique identifier for the article's version.You can find version history Id using | String |

## Example - Request




 Copy Code



curl -X GET \
  https://api3.sprinklr.com/{env}/api/v2/knowledgebase/version-history/641d87c1ff740f7620c78f62' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
   

## Example - Response




{
    "data": {
        "id": "641d87c1ff740f7620c78f51",
        "contentId": "6419d62ec6599e702070acef",
        "version": 3,
        "title": "some title",
        "markUpText": "
hello

there
",
        "status": "APPROVED",
        "publicContent": true,
        "ownerUserId": 600000218,
        "createdTime": "Mar 24, 2023, 11:21:37 AM"
    },
    "errors": []
}
 

     
     
   
 

[](https://dev.sprinklr.com/get-version-history-by-id) 

 

 
[Back to top](https://dev.sprinklr.com/get-version-history-by-id)
