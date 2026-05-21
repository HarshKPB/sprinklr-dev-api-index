---
title: "Comment Search - v1"
slug: comment-search-v1
url: https://dev.sprinklr.com/comment-search-v1
---

# Comment Search - v1

#
  POST - Comment Search

Using this API, you can search for comments for a given asset class and asset Id.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v1/generic/comment/search/{assetClass}/{assetId}

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

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| assetClass | Required | Asset class string ={ 				UNIVERSAL_CASE, 				MESSAGE_WORKFLOW, 				PROFILE_WORKFLOW, 				MEDIA_ASSET 				} | String |
| assetId | Required | The unique identifier for the asset where the comment exists | String |

### Request Parameters

















****

| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| commentPaginationInfo |  | Optional | Object containing the pagination details | Object |
|  | sinceDate | Optional | The starting time from when you want to fetch comments | Epoch |
|  | untilDate | Optional | The ending time till when you want to fetch comments | Epoch |
|  | start | Optional | Refers to the start offsetDefault=0 | Integer |
|  | rows | Optional | The number of rows (assets) to fetch from the start offset | Integer |
|  | sortKey | Optional | Refers to how you want to sort the results in the responseExample: commentCreationTime | String |
|  | sortDirection | Optional | Indicates whether you want the results in ascending order or descending order | String |

### Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      

curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/generic/comment/search/UNIVERSAL_CASE/15359604' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}' \
  -d '{
    "assetClass": "UNIVERSAL_CASE",
    "assetId": "15359604",
    "commentPaginationInfo":{
    "sinceDate":1607342601118,
    "untilDate":1607342644675,
    "start":0,
    "rows":10,
    "sortKey":"commentCreationTime",
    "sortDirection":"DESC"
    }
}'
 

     
     
   

### Example - Response

 
 
     
 
{
    "data": [
        {
            "id": "5fce1a349bce40767bb8ab6e",
            "comment": "
post test
",
            "commentingUser": 242077,
            "commentedOnDate": 1607342644673,
            "commentUpdateDate": 1607342644673,
            "onAsset": "UNIVERSAL_CASE",
            "assetId": "25359684",
            "partnerId": 787,
            "mediaList": [],
            "isEdited": false,
            "isEditable": false,
            "deleted": false,
            "hasConversation": false
        },
        {
            "id": "5fce1a2f9bce40767bb8aab8",
            "comment": "
neww
",
            "commentingUser": 242077,
            "commentedOnDate": 1607342639658,
            "commentUpdateDate": 1607342639658,
            "onAsset": "UNIVERSAL_CASE",
            "assetId": "25359684",
            "partnerId": 787,
            "mediaList": [],
            "isEdited": false,
            "isEditable": false,
            "deleted": false,
            "hasConversation": false
        },
        {
            "id": "5fce1a119bce40767bb8a728",
            "comment": "
make new test noe

​
",
            "commentingUser": 242077,
            "commentedOnDate": 1607342609018,
            "commentUpdateDate": 1607342609018,
            "onAsset": "UNIVERSAL_CASE",
            "assetId": "25359684",
            "partnerId": 787,
            "mediaList": [],
            "isEdited": false,
            "isEditable": false,
            "deleted": false,
            "hasConversation": false
        },
        {
            "id": "5fce1a099bce40767bb8a5fd",
            "comment": "
new test comment
",
            "commentingUser": 242077,
            "commentedOnDate": 1607342601118,
            "commentUpdateDate": 1607342601118,
            "onAsset": "UNIVERSAL_CASE",
            "assetId": "25359684",
            "partnerId": 787,
            "mediaList": [],
            "isEdited": false,
            "isEditable": false,
            "deleted": false,
            "hasConversation": false
        }
    ],
    "lastProcessedCommentTime": 1607342601118,
    "hasMore": false,
    "totalComments": 4
}
 

     
     
   
 
[](https://dev.sprinklr.com/comment-search-v1) 

 

 
[Back to top](https://dev.sprinklr.com/comment-search-v1)
