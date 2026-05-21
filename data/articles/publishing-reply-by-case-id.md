---
title: "Publishing Reply by Case Id"
slug: publishing-reply-by-case-id
url: https://dev.sprinklr.com/publishing-reply-by-case-id
---

# Publishing Reply by Case Id

#
  POST Publishing Reply by Case Id



Use this API to publish a reply to a case by using the case ID. The response is published as a reply to the customer's most recent message in the case, on the same channel where that message was received.

**Dev Notes: **Ensure the message for which you are publishing a reply is a customer message. If the message is a brand message, the reply will not be published.

## API Endpoint

	https://api3.sprinklr.com/{env}/api/v2/publishing/reply-on-case/{case-id}

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
| case-id | Required | The unique identifier of the case you want to respond to. You can get the case Id from the Sprinklr UI. | String |

### Request Parameters




































































- ****
[list of supported channels](https://dev.sprinklr.com/publishing-reply-by-case-id#supported-channels)

- ****
[list of supported channels](https://dev.sprinklr.com/publishing-reply-by-case-id#supported-channels)






-
-






























| Parameter | Sub-Parameter | Required/Optional | Description | Type | Possible Values |
| --- | --- | --- | --- | --- | --- |
| accountId |  | Optional | The Id of the account from which the reply will be posted. | String |  |
| approval |  | Optional | The object containing approval details. If not provided, it defaults to "NONE". | String |  |
| channelOptions |  | Optional | Channel-specific properties that include case and channel details. For example, toEmail address added in case of EMAIL channel type | Array |  |
| content |  | Required | The content of the message, including text and additional elements. | Object |  |
|  | text | Required | The text of the message to be published. | String | "New Message" |
|  | title | Optional | The title of the message to be published. | String | "Answer to your query" |
| messageCategory |  | Required | Specifies the message type. Indicates whether it is a private message or a public reply. | String | PRIVATE_MESSAGE: Indicates that the message is a private message.  Some of the channels that support private messaging are WhatsApp, Twitter Direct Message, Email, Apple Business Chat Message.       See the complete .           REPLY: Indicates that the message is a reply to a public comment. Some of the channels that support replies are Facebook Comment, LinkedIn Company Comment, Twitter Reply, YouTube Comment. 		  See the complete . |
| taxonomy |  | Optional if a default campaign Id is configured.Required if specifying a campaign Id other than the default campaign Id. | Contains customProperties for publishing, including campaignId and urlShortnerDomain. If not provided, default values will be filled. | Object |  |
|  | partnerCustomProperties |  | The partner custom properties associated with the post. | Object |  |
|  | campaignId |  | The Id of the campaign associated with the reply. | String |  |
| scheduleDate |  | Optional | Unix timestamp indicating when the reply should be published. | Epoch |  |


## Supported Channels


Below is a list of channels currently supported:



- [All supported channels](https://dev.sprinklr.com/publishing-reply-by-case-id#all-supported-channels)

- [Channels that support the PRIVATE_MESSAGE category](https://dev.sprinklr.com/publishing-reply-by-case-id#private-message)

- [Channels that support the REPLY category](https://dev.sprinklr.com/publishing-reply-by-case-id#reply)


### All Supported Channels



- KAKAO_TALK_MESSAGE

- WHATSAPP_MESSAGE

- WHATSAPP_BUSINESS_MESSAGE

- GOOGLE_CHAT_REPLY

- VIBER_MESSAGE

- VIBER_SERVICE_MESSAGE

- VIBER_POST

- NEXMO_MESSAGE

- NEXTDOOR_PRIVATE_MESSAGE

- NEXTDOOR_REPLY

- REDDIT_PRIVATE_MESSAGE

- REDDIT_COMMENT

- LIVECHAT_POST

- WECHAT_CONVERSATION

- TWITTER_DIRECT_MESSAGE

- TWITTER_REPLY

- ZIMBRA_PRIVATE_MESSAGE

- ZIMBRA_REPLY

- FACEBOOK_PRIVATE_MESSAGE

- FACEBOOK_COMMENT

- INSTAGRAM_DIRECT_MESSAGE

- INSTAGRAM_COMMENT

- TWILIO_DIRECT_MESSAGE

- AVAYA_SMS

- SIGNAL_WIRE

- SIGNAL_WIRE_MESSAGE

- INFOBIP

- SODIC

- AWS_PINPOINT_SMS

- VECTRAMIND

- SMS_HUB

- ESENDEX

- ITS

- NETCORE

- CMP

- SPRINKLR_LIVE_CHAT

- LINE_MESSAGE

- LINKEDIN_PROFILE_PRIVATE_MESSAGE

- LINKEDIN_PROFILE_COMMENT

- LINKEDIN_GROUP_COMMENT

- LINKEDIN_COMPANY_COMMENT

- VK_GROUP_BUSINESS_MESSAGE_TYPE

- VK_PROXY_BUSINESS_MESSAGE_TYPE

- VK_PAGE_BUSINESS_MESSAGE_TYPE

- APPLE_BUSINESS_CHAT_MESSAGE

- EMAIL_REPLY

- GMAIL_REPLY

- BULK_EMAIL_REPLY

- SMS_GLOBAL_MESSAGE

- GOOGLE_BUSINESS_MESSAGE

- YEXT_REVIEW

- MICROSOFT_EXCHANGE_REPLY

- NIKE_FEED_COMMENT

- YOUTUBE_COMMENT

- PLUCK_REPLY

- WEIBO_COMMENT

- YELP_LOCATION_REVIEW_REPLY


### messageCategory: PRIVATE_MESSAGE



- KAKAO_TALK_MESSAGE

- WHATSAPP_MESSAGE

- WHATSAPP_BUSINESS_MESSAGE

- GOOGLE_CHAT_REPLY

- VIBER_MESSAGE

- VIBER_SERVICE_MESSAGE

- NEXMO_MESSAGE

- NEXTDOOR_PRIVATE_MESSAGE

- REDDIT_PRIVATE_MESSAGE

- LIVECHAT_POST

- WECHAT_CONVERSATION

- TWITTER_DIRECT_MESSAGE

- ZIMBRA_PRIVATE_MESSAGE

- FACEBOOK_PRIVATE_MESSAGE

- INSTAGRAM_DIRECT_MESSAGE

- TWILIO_DIRECT_MESSAGE

- AVAYA_SMS

- SIGNAL_WIRE

- INFOBIP

- SODIC

- AWS_PINPOINT_SMS

- VECTRAMIND

- SMS_HUB

- ESENDEX

- ITS

- NETCORE

- CMP

- SPRINKLR_LIVE_CHAT

- LINE_MESSAGE

- LINKEDIN_PROFILE_PRIVATE_MESSAGE

- VK_GROUP_BUSINESS_MESSAGE_TYPE

- VK_PROXY_BUSINESS_MESSAGE_TYPE

- VK_PAGE_BUSINESS_MESSAGE_TYPE

- APPLE_BUSINESS_CHAT_MESSAGE

- EMAIL_REPLY

- GMAIL_REPLY

- BULK_EMAIL_REPLY

- SIGNAL_WIRE_MESSAGE

- SMS_GLOBAL_MESSAGE

- GOOGLE_BUSINESS_MESSAGE


### messageCategory: REPLY



- VIBER_POST

- YEXT_REVIEW

- NEXTDOOR_REPLY

- REDDIT_COMMENT

- MICROSOFT_EXCHANGE_REPLY

- NIKE_FEED_COMMENT

- YOUTUBE_COMMENT

- TWITTER_REPLY

- ZIMBRA_REPLY

- PLUCK_REPLY

- LINKEDIN_PROFILE_COMMENT

- LINKEDIN_GROUP_COMMENT

- LINKEDIN_COMPANY_COMMENT

- FACEBOOK_COMMENT

- INSTAGRAM_COMMENT

- WEIBO_COMMENT

- YELP_LOCATION_REVIEW_REPLY


## Example - Request















Copy Code



curl -X POST 'https://api3.sprinklr.com/{env}/api/v2/publishing/reply-on-case/6833536' \
-H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
--data '{
    "messageCategory": "PRIVATE_MESSAGE",
    "content": {
        "text": "New Message",
        "title": "Answer to your query"
    }
}'






## Example - Response





{
    "data": [
        "POST_262002438"
    ],
    "errors": []
}







### Response Parameters






















| Parameter | Description | Type |
| --- | --- | --- |
| data | The unique identifier of the posted reply. | Array |
| errors | Contains error messages if any issues occur. | Array |

[](https://dev.sprinklr.com/publishing-reply-by-case-id)






[Back to top](https://dev.sprinklr.com/publishing-reply-by-case-id)
