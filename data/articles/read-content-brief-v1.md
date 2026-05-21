---
title: "Read Content Brief v1"
slug: read-content-brief-v1
url: https://dev.sprinklr.com/read-content-brief-v1
---

# Read Content Brief v1

#
GET - Read Content Brief


Using this API, you can fetch the Content Brief details using the unique content brief Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/content/brief/{Id}

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

### Path Parameters


















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Id | Required | The unique content brief Id. | String |

### Example - Request

 Copy Code



curl -X GET \
'https://api3.sprinklr.com/{env}/api/v1/content/brief/5fc8ea7d83bb3e1bf9b2d27e' \
-H 'Authorization: Bearer {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'accept: application/json'




### Example - Response




{
    "id": "5fc8ea7d83bb3e1bf9b2d27e",
    "name": "Content Brief Example",
    "assetClass": "CAMPAIGN",
    "assetId": "4_3373",
    "templateId": "5cb6e7cde4b0e0f3e9ac9bf0",
    "data": "{\"object\":\"value\",\"document\":{\"object\":\"document\",\"data\":{},\"nodes\":[{\"object\":\"block\",\"type\":\"heading-one\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"This is smart editor test 123\",\"marks\":[{\"object\":\"mark\",\"type\":\"fontfamily\",\"data\":{\"value\":\"Times\"}},{\"object\":\"mark\",\"type\":\"fontsize\",\"data\":{\"value\":48}}]},{\"object\":\"leaf\",\"text\":\"ccs \",\"marks\":[]}]}]},{\"object\":\"block\",\"type\":\"paragraph\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"This is smart editor test\",\"marks\":[{\"object\":\"mark\",\"type\":\"fontfamily\",\"data\":{\"value\":\"Times New Roman\"}}]}]}]},{\"object\":\"block\",\"type\":\"paragraph\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"this is \",\"marks\":[]}]},{\"object\":\"inline\",\"type\":\"link\",\"data\":{\"href\":\"https://google.com/\"},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"content\",\"marks\":[]}]}]},{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"\",\"marks\":[]}]}]},{\"object\":\"block\",\"type\":\"paragraph\",\"data\":{},\"nodes\":[{\"object\":\"text\",\"leaves\":[{\"object\":\"leaf\",\"text\":\"\",\"marks\":[]}]}]}}",
    "type": "CAMPAIGN",
    "clientId": 4,
    "ownerUserId": 600000359,
    "createdTime": 1607002749248,
    "modifiedTime": 1641970868342,
    "lastModifiedUserId": 600000034,
    "dueDate": 1608817149248,
    "shareConfigs": [
        {
            "shareLevel": "GLOBAL"
        }
    ],
    "smartBrief": true,
    "version": 18,
    "locked": false,
    "canEdit": false,
    "canCollaborate": false
}








**Need assistance? Fill out our [feedback form](https://forms.office.com/r/5wTBFPQ7DC) and we’ll get back to you. **

[](https://dev.sprinklr.com/read-content-brief-v1)




[Back to top](https://dev.sprinklr.com/read-content-brief-v1)
