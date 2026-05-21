---
title: "Update Keyword List 2.0"
slug: update-keyword-list-2-0
url: https://dev.sprinklr.com/update-keyword-list-2-0
---

# Update Keyword List 2.0

#
  PUT - Update Keyword List


You can update listening keyword list via this API call using keyword list Id and you will get the updated response and other related objects after making the request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/keyword-list/{Id}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/getting-started)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameters



















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Id | Required | The Id of the keyword list. | String |

### Request Parameters






























































****

****

****

































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| name |  | Required | The keyword list name. | String |
| description |  | Optional | The keyword list description. | String |
| conditions |  | Optional | The list containing keyword condition information. | List<Condition> |
|  | term | Optional | The value based on keyword type. | String |
|  | distance | Optional | The distance is used to set the slop value for elastic search. | Integer |
|  | keywordType | Optional | The available keyword types are KEYWORD, PROXIMITY_KEYWORD, PHRASE. | String |
| tags |  | Optional | You can apply tags to Keyword Lists, providing an additional layer of management to your Listening Keyword Lists. | List<String> |
| conditionsUpdateType |  | OptionalRequired when the conditionsUpdateType is "APPEND" | Refers to the type of keyword list updateSupported Values: UPDATE: To add all the keywords in the payload including existing and new ones APPEND: To append only the new keywords and the existing ones will be retained even if excluded in the payload | String |
| shareConfig |  | Optional | The object containing share configurations which authorise users to view keyword list. |  |
|  | userIds | Optional | The list of user Ids, which is a unique identifier of each user. | List<Long> |
|  | userGroupIds | Optional | The list of user group Ids, which is a unique identifier of each user group. | List<String> |
|  | clientIds | Optional | the list of client Ids, which is a unique identifier of client. | List<Long> |
|  | clientGroupIds | Optional | The list of client group Ids, which is unique identifier of client group. | List<String> |
|  | shareWithEveryOne | Optional | Set it to true, if you want to share it with all users. | Boolean |
| permissionEntity |  | Optional | The object containing permission configuration to authorise users to edit and update keyword list. |  |
|  | userIds | Optional | The list of user Ids, which is a unique identifier of each user. | List<Long> |
|  | userGroupIds | Optional | The list of user group Ids, which is a unique identifier of each user group. | List<String> |

## Example - Request for UPDATE Conditions Update Type




 Copy Code


curl -X PUT \
   'https://api3.sprinklr.com/{env}/api/v2/keyword-list/655a0d6002e3356f92599d56' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Test",
  "description":"Testing Update Condition Type",
  "conditions": [
    {
      "term": keyword1,
      "distance": null,
      "keywordType": null
    },
    {
      "term": "keyword2",
      "distance": null,
      "keywordType": "KEYWORD"
    },
   {
      "term": "keyword3",
      "distance": null,
      "keywordType": "KEYWORD"
    }
  ],
  "tags": [],
  "conditionsUpdateType": "UPDATE",
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
        "id": "655a0d6002e3356f92599dcf",
        "name": "Test",
        "description": "Testing Update Condition Type",
        "conditions": [
            {
                "term": "keyword1",
                "distance": 0,
                "keywordType": "KEYWORD"
            },
            {
                "term": "keyword2",
                "distance": 0,
                "keywordType": "KEYWORD"
            },
            {
                "term": "keyword3",
                "distance": 0,
                "keywordType": "KEYWORD"
            }
        ],
        "tags": []
    },
    "errors": []
}



## Example - Request for APPEND Conditions Update Type




 Copy Code


	curl -X PUT \
   'https://api3.sprinklr.com/{env}/api/v2/keyword-list/655a0d6002e3356f92599d56' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Test",
  "description": "Testing Append Condition Type",
  "conditions": [
    {
      "term": "keyword4",
      "distance": 4,
      "keywordType": "KEYWORD"
    }
  ],
  "tags": ["Watch","TimePiece","Handmade","Iconic"],
  "conditionsUpdateType": "APPEND",
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
        "name": "Test",
        "description": "Testing Append Condition Type",
        "conditions": [
            {
                "term": "keyword1",
                "distance": 0,
                "keywordType": "KEYWORD"
            },
            {
                "term": "keyword2",
                "distance": 0,
                "keywordType": "KEYWORD"
            },
            {
                "term": "keyword3",
                "distance": 0,
                "keywordType": "KEYWORD"
            },
            {
                "term": "keyword4",
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


















































































































| Parameters | Sub-Params | Description | Type |
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

[](https://dev.sprinklr.com/update-keyword-list-2-0)




[Back to top](https://dev.sprinklr.com/update-keyword-list-2-0)
