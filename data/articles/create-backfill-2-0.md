---
title: "Create Backfill 2.0"
slug: create-backfill-2-0
url: https://dev.sprinklr.com/create-backfill-2-0
---

# Create Backfill 2.0

#
  POST - Create Backfill

You can create historical Listening Topic Backfill request via this API call and you will get the backfill Id and other related objects as response after making the request.

	****Note**: **Reach out to your Success Manager to get the Backfill APIs enabled for your environment.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/listening-topic-backfill

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

### Request Parameters




















































































| Parameters | Sub-Params | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| topicId |  | Required | Listening Topic Unique identifier, for which Backfill need to be triggered. | String |
| fromTimeEpochMillis |  | Required | Backfill start time in epoch millis. | Epoch |
| toTimeEpochMillis |  | Required | Backfill end time in epoch millis. | Epoch |
| sources |  | Required | Backfill data sources list. | List<String> |
| shareConfig |  | Optional | The object containing share configurations which authorise users to view Backfill. |  |
|  | userIds | Optional | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | Optional | List of User Group IDs, which is unique identifier for each User Group. | List<String> |
|  | clientIds | Optional | List of Client IDs, which is unique identifier for Client. | List<Long> |
|  | clientGroupIds | Optional | List of Client Group IDs, which is unique identifier for Client Group. | List<String> |
|  | shareWithEveryOne | Optional | Set it to true, if you want to share it with all users. | Boolean |

## Example - Request




 Copy Code


curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/listening-topic-backfill' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "topicId": "5f98178dee90e7688ea2e938",
    "fromTimeEpochMillis": 1613538000000,
    "toTimeEpochMillis": 1614516540000,
     "sources": [
            "TWITTER",
            "FACEBOOK"
        ],
    "shareConfig": {
        "shareWithEveryOne": true
    }
}'





## Example - Response




{
    "data": {
        "id": "6048bcca626a361cc11e954e",
        "topicId": "5f98178dee90e7688ea2e938",
        "fromTimeEpochMillis": 1613538000000,
        "toTimeEpochMillis": 1614513600000,
        "sources": [
            "TWITTER",
            "FACEBOOK"
        ],
        "shareConfig": {
            "shareWithEveryOne": true
        },
        "userId": 600004599,
        "status": "Estimate Requested"
    },
    "errors": []
}





### Response Parameters

























































































































| Parameters | Sub-Params | Description | Type |
| --- | --- | --- | --- |
| id |  | Unique identifier of the Listening Topic Backfill. | String |
| topicId |  | Listening Topic Unique identifier, for which Backfill need to be triggered. | String |
| fromTimeEpochMillis |  | Backfill start time in epoch millis. | Epoch |
| toTimeEpochMillis |  | Backfill end time in epoch millis. | Epoch |
| sources |  | Backfill data sources list. | List<String> |
| shareConfig |  | Backfill Share Config details. |  |
|  | userIds | The list of user Ids, which is a unique identifier of each user. | List<Long> |
|  | userGroupIds | The list of user group Ids, which is a unique identifier of each user group. | List<String> |
|  | clientIds | the list of client Ids, which is a unique identifier of client. | List<Long> |
|  | clientGroupIds | The list of client group Ids, which is unique identifier of client group. | List<String> |
|  | shareWithEveryOne | Set it to true, if you want to share it with all users. | Boolean |
| estimatedSourceVsCount |  | Backfill Estimate details at source level. | Map<String, Long> |
| backfilledSourceVsCount |  | Backfilled data count at source level. | Map<String, Long> |
| userId |  | Backfilled user id. | Long |
| status |  | Backfill current status. | String |
| backfilledDataCount |  | Over all Backfilled data count | Long |
| estimatedDataCount |  | Over all Estimated data count | Long |

[](https://dev.sprinklr.com/create-backfill-2-0)




[Back to top](https://dev.sprinklr.com/create-backfill-2-0)
