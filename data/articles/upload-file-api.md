---
title: "Upload File API"
slug: upload-file-api
url: https://dev.sprinklr.com/upload-file-api
---

# Upload File API

# Upload File API



This API helps upload the file to server and returns the fileToken in return, which then can be passed in the [Conversation Send API](https://dev.sprinklr.com/conversation-send-api).

## API Endpoint

https://{env}-live-chat.sprinklr.com/api/livechat/v1/upload/file

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			``



| Key | Value | Description |
| --- | --- | --- |
| x-chat-token | The token you received in the App Handshake API response | The token for authenticating the live chat session |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

### Request Parameters (form-data)











****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| file | Required | Refers to source of the file from your local | String |
| url | OptionalRequired if you want to pass the already created publicaly accessible url instead of the file token | Refers to the publicaly accessible url for the attachment file you want send in the conversation | String |
| fileName | Required | Refers to the unique name of the fileNote: The filename should also have the format in the suffix. Example, imagefile.png or videofile.mov, or audiofile.wav, etc. | String |

**Dev Notes: **Supported file formats include:

- **Image:** ` jpg`, `jpeg`, `jfif`, `png`, `gif`

- **Video:**` mov`, `mp4`, `mpg`, `mpeg`

## Example - Request




  Copy Code



curl -X POST \
 https://{env}-live-chat.sprinklr.com/api/livechat/v1/conversation//6513d21819a98b52f41801df/messageRead' \
  -H 'x-chat-token: {chat token}' \
  -H 'Content-Type: application/json' \
  -F 'file=@"/Users/Desktop/TestImage1 '\
  -F 'fileName="Test"'\





### Example - Response



{
"fileToken": " "6516b27e2ce93949915cd6e7"
}





**Dev Notes: **You can use this file token in the [Conversation Send API](https://dev.sprinklr.com/conversation-send-api) attachment payload to send the file with the message. Also note that the fileToken is only valid for 1.5 days, i.e., 36 hours post which you'll have to regenerate the fileToken before you pass it in the conversation send API.

[](https://dev.sprinklr.com/upload-file-api)

[Back to top](https://dev.sprinklr.com/upload-file-api)
