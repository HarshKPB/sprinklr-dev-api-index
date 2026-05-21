---
title: "Case Management Stream "
slug: case-management-stream
url: https://dev.sprinklr.com/case-management-stream
---

# Case Management Stream 

#
  POST Case Management Stream



Using this API, you can fetch the case details from the case management stream column.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/stream/{streamId}/feed

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













[Read Dashboard API](https://dev.sprinklr.com/fetch-engagement-dashboard-v1)




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| streamId | Required | Stream Id of the column to fetch data.You can fetch the stream Id using | String |

## Request Parameters



























****
****











| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| start | Required | The start offset to tell the client where to begin pulling data.The default is 0. | Integer |
| rows | Required | The number of rows to be fetched, starting from the start. | Integer |
| sortField | Required | Key on the basis of which you want to sort the data.Supported sortField include:CASE_MODIFICATION_TIMECASE_CREATION_TIME | String |
| sortOrder | Optional | Short in ascending or descending order.i.e. ASC and DESC. | String |

## Example - Request















Copy Code



	curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/stream/65c604a1bbd6d649d85d1e98/feed' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "start" : 0,
    "rows" :1,
    "sortField" : "CASE_MODIFICATION_TIME",
    "sortOrder": "DESC"
}






## Example - Response





{
    "data": {
        "entities": [
            {
                "id": "65ec0cd8af85261213e08375",
                "caseNumber": 25415471,
                "subject": "Test Subject",
                "description": "Test Description",
                "version": 4331,
                "externalCase": {
                    "id": "500F900001cPSEGIA4",
                    "caseNumber": "00001119",
                    "channelType": "SALESFORCE",
                    "permalink": "https://test-org4-dev-ed.develop.my.salesforce.com/500F900001cPSEGIA4",
                    "createdTime": 1709968602000,
                    "modifiedTime": 1709968604000
                },
                "externalCaseInfo": {
                    "externalCases": []
                },
                "workflow": {
                    "customProperties": {
                        "spr_uc_predicted_csat_rating": [
                            "50"
                        ],
                        "SALESFORCE_UNIVERSAL_CASE_CONTACT_ID": [
                            "003F900001grcJhIAI"
                        ],
                        "spr_uc_eng_score": [
                            "0"
                        ],
                        "_c_65c4c1d5dc61983762389934": [
                            "New"
                        ],
                        "spr_uc_initial_csat_rating": [
                            "50"
                        ],
                        "SALESFORCE_UNIVERSAL_CASE_CONTACT_Name": [
                            "Tony"
                        ]
                    },
                    "queues": []
                },
                "channelCustomProperties": [],
                "contact": {
                    "id": "TWITTER_134480496",
                    "name": "Aashitagupta",
                    "channelType": "TWITTER",
                    "channelId": "134480496",
                    "fromSnUserId": "134480496"
                },
                "createdTime": 1709968600700,
                "modifiedTime": 1711427462329,
                "firstMessageId": "ACCOUNT_74143_1709818327114_TWITTER_7_1765732159145365664",
                "sentiment": 0,
                "latestProfileMessageAssociatedTime": 1709818327114,
                "conversationId": "392248399183237120",
                "firstMessageAssociatedTime": 1709818327114,
                "latestMessageAssociatedTime": 1709818327114,
                "totalProcessingClockTime": 9017,
                "allEngagedUsersList": [],
                "associatedFanMessageCount": 1,
                "associatedBrandMessageCount": 0,
                "associatedUserBrandMessageCount": 0,
                "deleted": false
            }
],
        "hasMore": true,
        "nextPageCursor": "66025e042419fd1cb63ae670"
    },
    "errors": []
}







**Dev Notes: **For fetching the next set of results, you can use the [stream cursor API](https://dev.sprinklr.com/stream-cursor-api) where you need to pass the Id received in the nextPageCursor response field

[](https://dev.sprinklr.com/case-management-streams)




[Back to top](https://dev.sprinklr.com/case-management-streams)
