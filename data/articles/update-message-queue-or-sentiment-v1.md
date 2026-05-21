---
title: "Update Message Queue or Sentiment v1"
slug: update-message-queue-or-sentiment-v1
url: https://dev.sprinklr.com/update-message-queue-or-sentiment-v1
---

# Update Message Queue or Sentiment v1

# POST  Update Message Queue or Sentiment v1

Using this API, you can update partner queue details and sentiment for the given message

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/message/workflow/sentiment-queue/update

**Dev Notes: **For updating the message custom properties, kindly refer to [Message Properties Update](https://dev.sprinklr.com/message-properties-update-v1) API documentation

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

















****

****
****
****

****[How is Customer Sentiment Detected?](https://www.sprinklr.com/help/articles/sentiment-and-csat-scores/how-is-customer-sentiment-detected/65ae2127ab59de79d2a156e8)








****[Queues](https://www.sprinklr.com/help/articles/sprinklr-service-glossary/queues/640907fe7517d84a3aaf398e)

[Bootstrap Resources](https://dev.sprinklr.com/bootstrap-resources-v1)














			[channel type](https://dev.sprinklr.com/channels-v1)






			[message type code](https://dev.sprinklr.com/message-v1)




















            ``````











| Parameter | Sub-Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- | --- |
| sentiment |  | Optional | Refers to the sentiment you want to assign to the messageSentiment Scales: -1 or lower:  Negative Sentiment0 - Neutral Sentiment1 or higher - Positive SentimentRelated Article: | String |
| PartnerQueues |  | Optional | Refers to the partner/customer queue that you want to add the message toRelated Article:  For fetching all the existing partner queues, you can call  (PARTNER_QUEUES) API | List [Integer] |
| universalMessageWorkflowKey |  | Required | Refers to the object containing the message detailsThe object parameters are different parameters that help construct the  unique message Id | Object |
|  | snType | Required | Refers to the  associated with the message | String |
|  | msgType | Required | Refers to the  with respect to the given channel | String |
|  | snMsgId | Required | Refers to the unique identifier for the message on the native channel | String |
|  | sourceId | Required | Refers to the unique identifier for the given source type | String |
|  | sourceType | Required | Refers to the message's SourceType = {ACCOUNT, PERSISTENT_SEARCH, LISTENING} | String |
|  | snCreatedTime | Required | Refers to the time at which the message was created on the social native channel | Integer (Epoch) |

**Dev Notes:** Kindly note that the queue updates will override the existing queues, i.e., the pre-existing queue won't be synced

## Example - Request




 Copy Code


curl -X POST \
  https://api3.sprinklr.com/{env}/api/v1/message/workflow/sentiment-queue/update' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "sentiment": "-1",
    "partnerQueues": [
            100080
        ],
    "universalMessageWorkflowKey": [
        {
            "snType": "TWITTER",
            "msgType": "7",
            "snMsgId": "1749372031106224488",
            "sourceId": "1600046533",
            "sourceType": "ACCOUNT",
            "snCreatedTime": 1705917768000
        }
    ]
}'



## Example - Response




true



**Dev Notes: **`true` implies that the message's sentiment/queue details have been updated successfully

[](https://dev.sprinklr.com/update-message-queue-or-sentiment-v1)
