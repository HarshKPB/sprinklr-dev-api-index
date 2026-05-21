---
title: "Fetch Voice Recording"
slug: fetch-voice-recording
url: https://dev.sprinklr.com/fetch-voice-recording
---

# Fetch Voice Recording

#
 GET  Fetch Voice Recording



Voice recording URLs received from APIs will no longer be publicly accessible. To download the voice recording, you can call this API using the recording Id received in the restricted voice recording URLs.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/voice/recording


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

### Query Parameters

















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| recordingId | Required | Refers to the unique identifier for the voice recording.For example, read message by Id API returns "https://api2.sprinklr.com/{env}/api/v2/voice/recording?recordingId=000001904430ddb4e4b03149fc92eded" as the recording URL.In this case, the recording Id needed to access the recording will be:  000001904430ddb4e4b03149fc92eded | String |

## Example - Request















Copy Code



curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/voice/recording?recordingId=000001904430ddb4e4b03149fc92eded'\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






## Example - Response





200 OK








**Dev Note: ** 200 OK in the response implies that the recording has been successfully downloaded

[](https://dev.sprinklr.com/fetch-voice-recording)




[Back to top](https://dev.sprinklr.com/fetch-voice-recording)
