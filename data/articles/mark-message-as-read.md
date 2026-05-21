---
title: "Mark Message as Read"
slug: mark-message-as-read
url: https://dev.sprinklr.com/mark-message-as-read
---

# Mark Message as Read

#
  POST Mark Message as Read




This API helps validate that the customer message has been read by the brand. When you receive a message within Sprinklr using the message received webhook, you can use the messageId from the webhook response in the query parameters of this API for marking that message as read.

**Dev Notes: **Currently, the API only supports WhatsApp Business Channel

## Examples

### Customer Sends a Whatsapp Message

### Customer Message is Marked as Read Using API

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/message/notify-read

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)


``



| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Accept | application/json | Determines the acceptable response type from the server |

### Query Parameters


















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| MessageId | Required | The Id of the customer's message you want to be validated as read | String |

**Dev Notes: **`messageId`= sourceType + “_”+ sourceId + “_” + ChannelCreatedTime + “_” + “[ChannelType](https://dev.sprinklr.com/channels-v1)” + “_” + ” [MessageType](https://dev.sprinklr.com/message-v1)“ +”_” + channelMessageId.

### Example - Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/message/notify-read?messageId=ACCOUNT_600044439_1707827235000_WHATSAPP_BUSINESS_316_wamid.HBgMOTE5NDE4NTg2MTA2FQIAEhggNThGQTY5QjFBMDU5MTdFNkNFMzVBRDgyRDlFRTg4RDkA' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \






### Example - Response





200 OK






	[](https://dev.sprinklr.com/mark-message-as-read)




[Back to top](https://dev.sprinklr.com/mark-message-as-read)
