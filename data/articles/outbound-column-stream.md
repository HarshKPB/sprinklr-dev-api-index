---
title: "Outbound Column Stream"
slug: outbound-column-stream
url: https://dev.sprinklr.com/outbound-column-stream
---

# Outbound Column Stream

#
  POST Outbound Column Stream




Use this API to fetch stream data for outbound columns available in engagement dashboards with Sprinklr Modern Engagement.

Note: In the response of this API call, if there is more data then you will receive a cursor as `"nextPageCursor": "602cbe27efb9i0o345s2fc85"`which can be used in the [Stream Cursor API](https://dev.sprinklr.com/stream-cursor-api) to fetch the next set of data.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/stream/{streamId}/feed

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














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













[Read Dashboard API](https://dev.sprinklr.com/fetch-engagement-dashboard-by-name)




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| streamId | Required | Stream Id of the column to fetch data.You can fetch the stream Id using | String |

## Request Parameters





































| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| start | Required | The start offset to tell the client where to begin pulling data. The default is 0. | Integer |
| rows | Required | The number of rows to be fetched, starting from the start. | Integer |
| sortField | Required | Key on the basis of which you want to sort the data. | String |
| sortOrder | Optional | Short in ascending or descending order.i.e. ASC and DESC. | String |

###  Supported sort Field









			``



			``



			``



			``



			``



			``



			``



			``



| sortField | Description |
| --- | --- |
| MODIFIED_TIME, SCHEDULED_TIME | For scheduled messages. |
| PUBLISHED_TIME | Supported only for sent messages column |
| MODIFIED_TIME | For drafts. |
| MODIFIED_TIME | For group messages. |
| MODIFIED_TIME, SCHEDULED_TIME | For approval queues. |
| MODIFIED_TIME, SCHEDULED_TIME | For approval required. |
| MODIFIED_TIME, SCHEDULED_TIME | For approval sent. |
| MODIFIED_TIME, SCHEDULED_TIME | For rejected messages. |

## Example - Request















Copy Code



	curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/stream/{streamId}/feed' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "start" : 0,
    "rows" :2,
    "sortField" : "SCHEDULED_TIME",
    "sortOrder" : "ASC"
    }'






## Example - Response





{
    "data": {
        "entities": [
{
                "inReplyToMessageId": "ACCOUNT_209928_1551092853000_WHATSAPP_BUSINESS_316_ABEGkYiSaRKXAhCngjk45X78LbQsKlOY--uI",
                "allowDuplicateMessages": false,
                "id": 2157944935,
                "accountId": 209928,
                "publishedDate": 1551092916000,
                "parentMessageId": 2007900936,
                "content": {
                    "text": "This is a survey "
                },
                "scheduleDate": 1551092916000,
                "taxonomy": {
                    "campaignId": "4706_2"
                },
                "status": "SENT"
            },
                "inReplyToMessageId": "ACCOUNT_200008_1551092853000_WHATSAPP_BUSINESS_316_ABEGkYiSaRKXAhC39jgd57jk2bQsKlOY--uI",
                "toProfile": {
                    "screenName": "Name",
                    "channelType": "WHATSAPP_BUSINESS",
                    "channelId": "{phone number}"
                },
                "allowDuplicateMessages": false,
                "id": 2160975399,
                "accountId": 200008,
                "publishedDate": 1551359341000,
                "parentMessageId": 2160975399,
                "content": {
                    "text": "Exel ",
                    "attachment": { }
                },
                "scheduleDate": 1551359327000,
                "taxonomy": {
                    "campaignId": "4706_658",
                    "clientCustomProperties": {
                    },
                    "partnerCustomProperties": {
                    },
                    "tags": [],
                    "urlShortenerId": "5acdb221e4b0226890cfa1c3"
                },
                "status": "SENT"
            }
],
"hasMore": true,
        "nextPageCursor": "602cbe27efb9i0o345s2fc85"
    },
    "errors": []
}






**Response Parameters**

[Click here](https://dev.sprinklr.com/read-message-by-id) to check the response definitions of **MESSAGE**.









			********




| Parameter | Description | Type |
| --- | --- | --- |
| nextPageCursor | The nextPageCursor you get in the response will be used in the Stream Cursor API to fetch next set of data. | String |

	[](https://dev.sprinklr.com/outbound-column-stream)




[Back to top](https://dev.sprinklr.com/outbound-column-stream)
