---
title: "Read Keyword List 2.0"
slug: read-keyword-list-2-0
url: https://dev.sprinklr.com/read-keyword-list-2-0
---

# Read Keyword List 2.0

#
  GET - Read Keyword List


You can fetch the complete Keyword List objects via this api using Keyword List Id.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/keyword-list/{Id}

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

###  Path Parameters



















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Id | Required | The unique Id of the Keyword List. | String |

## Example -Request




 Copy Code


curl -X GET \
   hhttps://api3.sprinklr.com/{env}/api/v2/keyword-list/6040e3d6df5d0f43bf6c0473 \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'





## Example - Response




{
    "data": {
        "id": "6040e3d6df5d0f43bf6c0473",
        "name": "Sumit Testing",
        "description": "Testing new Keyword API",
        "conditions": [
            {
                "term": "Rolex",
                "distance": 0,
                "keywordType": "KEYWORD"
            }
        ],
        "tags": [
            "Watch",
            "TimePiece",
            "Handmade",
            "Iconic"
        ],
        "shareConfig": {
            "shareWithEveryOne": true
        },
        "permissionEntity": {
            "userIds": [
                600001767
            ]
        }
    },
    "errors": []
}





### Response Parameters


















































































































| Parameters | Sub-Parameters | Description | Type |
| --- | --- | --- | --- |
| id |  | The unique identifier of the Keyword List in Listening. | String |
| name |  | The Keyword List name. | String |
| description |  | The Keyword List description. | String |
| conditions |  | The Keyword List keyword conditions list. | List<Condition> |
|  | term | The value based on keyword type. | String |
|  | distance | The distance is used to set the slop value for elastic search. | Integer |
|  | keywordType | The available keyword types are KEYWORD, PROXIMITY_KEYWORD, PHRASE. | String |
| tags |  | Keyword List tags list. | List<String> |
| shareConfig |  | The object containing share configurations which authorise users to view Keyword List. |  |
|  | userIds | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | List of User Group IDs, which is unique identifier for each User Group. | List<String> |
|  | clientIds | List of Client IDs, which is unique identifier for Client. | List<Long> |
|  | clientGroupIds | List of Client Group IDs, which is unique identifier for Client Group. | List<String> |
|  | shareWithEveryOne | Set it to true, if you want to share it with all users. | Boolean |
| permissionEntity |  | The object containing permission configuration to authorise users to edit or update Keyword List. |  |
|  | userIds | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | List of User Group IDs, which is unique identifier for each User Group. | List<String> |

[](https://dev.sprinklr.com/read-keyword-list-2-0)




[Back to top](https://dev.sprinklr.com/read-keyword-list-2-0)
