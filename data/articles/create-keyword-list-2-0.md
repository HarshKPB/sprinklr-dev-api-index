---
title: "Create Keyword List 2.0"
slug: create-keyword-list-2-0
url: https://dev.sprinklr.com/create-keyword-list-2-0
---

# Create Keyword List 2.0

#
  POST - Create Keyword List


You can create Listening Keyword List via this API call and in response you will get the Keyword List Id and other related objects after making the request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/keyword-list

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

### Request Body






























































































































| Fields | Sub-Fields | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| name |  | Required | The Keyword List name. | String |
| description |  | Optional | The Keyword List description. | String |
| conditions |  | Required | The Keyword List keyword conditions list. | List<Condition> |
|  | term | Optional | The value based on keyword type. | String |
|  | distance | Optional | The distance is used to set the slop value for elastic search. | Integer |
|  | keywordType | Optional | The available keyword types are KEYWORD, PROXIMITY_KEYWORD, PHRASE. | String |
| tags |  | Optional | Keyword List tags list. | List<String> |
| shareConfig |  | Optional | The object containing share configurations which authorise users to view Keyword List. |  |
|  | userIds | Optional | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | Optional | List of User Group IDs, which is unique identifier for each User Group. | List<String> |
|  | clientIds | Optional | List of Client IDs, which is unique identifier for Client. | List<Long> |
|  | clientGroupIds | Optional | List of Client Group IDs, which is unique identifier for Client Group. | List<String> |
|  | shareWithEveryOne | Optional | Set it to true, if you want to share it with all users. | Boolean |
| permissionEntity |  | Optional | The object containing permission configuration to authorise users to edit or update Keyword List. |  |
|  | userIds | Optional | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | Optional | List of User Group IDs, which is unique identifier for each User Group. | List<String> |

## Example - Request




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/keyword-list' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": null,
  "description":" ",
  "conditions": [
    {
      "term": null,
      "distance": null,
      "keywordType": null
    }
  ],
  "tags": [],
  "shareConfig": {
    "userIds": [],
    "userGroupIds": [],
    "clientIds": [],
    "clientGroupIds": [],
    "shareWithEveryOne": false
  },
  "permissionEntity": {
    "userIds": [],
    "userGroupIds": []
  }
}'



## Example - Response




{
    "data": {
        "id": " ",
        "name": " ",
        "conditions": [
            {
                "term": "Price",
                "distance": 5,
                "keywordType": "KEYWORD"
            }
        ],
        "tags": [
            "Listening",
            "Spam",
            "Profanity",
            "Issues",
            "Suppliers",
            "Testing"
        ]
    },
    "errors": []
}





## Example - Request




 Copy Code


curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/keyword-list' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Sumit Testing",
  "description": "Testing new Keyword API",
  "conditions": [
    {
      "term": "Rolex",
      "distance": 4,
      "keywordType": "KEYWORD"
    }
  ],
  "tags": ["Watch","TimePiece","Handmade","Iconic"],
  "shareConfig": {
    "shareWithEveryOne": true
  },
  "permissionEntity": {
    "userIds": [600001767],
    "userGroupIds": []
  }
}'



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



### Response Definitions


















































































































| Fields | Sub-Fields | Description | Type |
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

[](https://dev.sprinklr.com/create-keyword-list-2-0)




[Back to top](https://dev.sprinklr.com/create-keyword-list-2-0)
