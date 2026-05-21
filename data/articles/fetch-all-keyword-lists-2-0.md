---
title: "Fetch All Keyword Lists 2.0"
slug: fetch-all-keyword-lists-2-0
url: https://dev.sprinklr.com/fetch-all-keyword-lists-2-0
---

# Fetch All Keyword Lists 2.0

#
  GET - Fetch All Keyword Lists


Using this API, you can fetch all keyword lists available within a workspace.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/keyword-list/fetchKeywordListsNameIdMapping

**Dev Notes:**If your authorization token is associated with multiple workspaces, you'll have to pass your `workspace_id` in the headers for fetching all keyword lists. You can use [Fetch Accessible Clients API](https://dev.sprinklr.com/fetch-accessible-workspaces) to check the workspaces Ids your token is associated with.

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



``

``

[Fetch Accessible Clients API](https://dev.sprinklr.com/fetch-accessible-workspaces)

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |
| workspace_id | your workspace_idYou can use  to check the workspaces Ids your token is associated with | workspace_id is only required when your token is associated with multiple workspaces |

## Example -Request




 Copy Code


curl -X GET \
   'https://api3.sprinklr.com/{env}/api/v2/keyword-list/fetchKeywordListsNameIdMapping' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'



## Example - Response




{
    "data": {
        "Test1": "627a4265f701733135886fb7",
        "Test2": "627cb60ab63b08670be7ee02",
        "Test3": "623191d3d31232194d07296d",
        "Test4": "626bd67318e10738333fc439",
        "TEST5": "6233358754393860c8743347"
    },
    "errors": []
}



### Response Parameters: Key and Value Mapping


















[Read Keyword List API](https://dev.sprinklr.com/read-keyword-list-2-0)




| Parameters | Description | Type |
| --- | --- | --- |
| name | Refers to the keyword list name | String |
| id | Refers to the unique identifier for the keyword list. For the given id, you can fetch the keyword list details using the | String |

[](https://dev.sprinklr.com/fetch-all-keyword-lists-2-0)




[Back to top](https://dev.sprinklr.com/fetch-all-keyword-lists-2-0)
