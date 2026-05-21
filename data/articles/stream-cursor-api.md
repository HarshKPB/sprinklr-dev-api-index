---
title: "Stream Cursor API"
slug: stream-cursor-api
url: https://dev.sprinklr.com/stream-cursor-api
---

# Stream Cursor API

#
  GET Stream Cursor API



You can fetch the next set of available data with this API call.

### API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/stream/cursor/`{nextPageCursor}`

 Note: The above ` {nextPageCursor}` is the one you receive in the response from either the Outbound or Inbound API. So before using this API call, you should use the Outbound/Inbound API to receive the nextPageCursor in the response.

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












``




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| nextPageCursor | Required | The cursor you received in response of the Outbound/Inbound API call. Example:  "nextPageCursor": "602cc4ngh67dg345tnb703fe" | String |

## Example - Request















Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/stream/cursor/{nextPageCursor}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'






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







**Note: ** You will receive another cursor if more data is available to fetch. You can use the id given in nextPageCursor to make another GET call.

## Response Parameters

[Click here](https://dev.sprinklr.com/read-message-by-id) to check the response definitions of **MESSAGE**.









			********




| Parameter | Description | Type |
| --- | --- | --- |
| nextPageCursor | The nextPageCursor you get in the response will be used in the Stream Cursor API to fetch next set of data. | String |

[](https://dev.sprinklr.com/stream-cursor-api)




[Back to top](https://dev.sprinklr.com/stream-cursor-api)
