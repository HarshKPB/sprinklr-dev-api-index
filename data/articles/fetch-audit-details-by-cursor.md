---
title: "Fetch Audit Details by Cursor"
slug: fetch-audit-details-by-cursor
url: https://dev.sprinklr.com/fetch-audit-details-by-cursor
---

# Fetch Audit Details by Cursor

#
  GET Fetch Audit Details by Cursor

If the [audit API](https://dev.sprinklr.com/audit-api) response has additional details that exceed the limit in the request, you can fetch them using cursor ID.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/audit?id={cursorId}

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

## Example - Request














Copy Code




curl -X GET \
  https://api3.sprinklr.com/{env}/api/v2/audit?id=629e3336dd414169dc5af161 \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \





## Example - Response





{
     "data": {
       "results": [
           {
               "assetClass": "UNIVERSAL_CASE",
               "assetId": "10520954",
               "auditDate": 1650452106126,
               "userId": 0,
               "changes": [
                   {
                       "fieldName": "Messages",
                       "oldValues": [],
                       "newValues": [
                           "Test1"
                       ]
                   }
               ]
           },
           {
               "assetClass": "UNIVERSAL_CASE",
               "assetId": "10520954",
               "auditDate": 1650452106118,
               "userId": 0,
               "changes": [
                   {
                       "fieldName": "Message Sentiment",
                       "oldValues": [],
                       "newValues": [
                           "0"
                       ]
                   }
               ]
           }
     ],
    "cursor": "627e334a25033713a3cb8887"
},
 "errors": []
}





### Response Parameters




















































































| Parameters | Sub-Params | Sub-Params | Description | Type |
| --- | --- | --- | --- | --- |
| Results |  |  | Array listing the details of the response | Array |
|  | assetClass |  | assetClass for which the request is made | String |
|  | assetId |  | The assetId mentioned in the request | String |
|  | auditDate |  | The date on which the asset was analyzed | Epoch |
|  | userId |  | The Id of the user who made the changes | Integer |
|  | changes |  | Lists the change details | Array |
|  |  | fieldName | The name of the field that was modified | String |
|  |  | oldValues | The old value of the field | String |
|  |  | newValues | The new or the changed value of the field | String |
| cursor |  |  | If the API response has additional data that exceeds the mentioned limit in the request, a cursor Id is returnedYou can use this cursor Id to fetch the next set of data | String |

	 [](https://dev.sprinklr.com/fetch-audit-details-by-cursor)




[Back to top](https://dev.sprinklr.com/fetch-audit-details-by-cursor)
