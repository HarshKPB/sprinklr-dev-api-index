---
title: "Media Download"
slug: media-download
url: https://dev.sprinklr.com/media-download
---

# Media Download

#
  GET Media Download


The Media Download API allows you to download a media file using a URL. You can obtain this URL from the [Read Message by UMID API](https://dev.sprinklr.com/read-message-by-umid).

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/media/download?url=`url`

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
| Content-Type | multipart/form-data; boundary=<calculated when request is sent> | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Query Parameters

	``[Read Message by UMID API](https://dev.sprinklr.com/read-message-by-umid)



| Parameter | Required | Description | Type |
| --- | --- | --- | --- |
| url | Required | This is the URL for the media file. It is returned in the url parameter in the response of the . | URL |


### Supported Media Types


You can download the following media types using its encrypted URL:









      ``



      ``



      ``



      ``



      ``



      ``



      ``



      ``




| Media Type | Description |
| --- | --- |
| application/octet-stream | Generic binary data used when the file type is unknown. |
| image/ | Image files (for example, JPEG, PNG). |
| audio/ | Audio files (for example, MP3). |
| video/ | Video files (for example, MP4). |
| application/pdf | PDF documents |
| application/zip | ZIP archive files |
| application/x-font-ttf | TrueType Font files |
| application/vnd.ms-excel | Microsoft Excel spreadsheet files |

### Example - Request















Copy Code


curl -X GET 'https://api3.sprinklr.com/{env}/api/v2/media/download?url=' \
-H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \






### Example - Response





200 OK







**Dev Notes: **The media file is included in the response. For example, a video file is returned as shown below:

[](https://dev.sprinklr.com/media-download)




[Back to top](https://dev.sprinklr.com/media-download)
