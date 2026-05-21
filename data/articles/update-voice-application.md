---
title: "Update Voice Application"
slug: update-voice-application
url: https://dev.sprinklr.com/update-voice-application
---

# Update Voice Application

#
 POST  Update Voice Application



This API enables you to update an existing Voice Application within your Sprinklr environment. This application defines how incoming and outgoing voice calls are handled for a given account and configuration.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/voice/update-voice-application


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

### Request Body Parameters










































| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| appId | string | Yes | Unique identifier of the Voice Application that you want to update. |
| name | string | No | Name of the voice application |
| provider | string | No | Name of the provider (e.g., SPRINKLR) |
| providerDomain | string | No | Domain of the provider |
| phoneNumber | string | No | Primary phone number in E.164 format |
| voiceAccountId | string | No | Unique Identifier of the associated Voice Account |
| country | string | No | Country code (e.g., US) |
| ivrProcessId | string | No | Associated IVR process ID |
| secondaryPhoneNumbers | string | No | Comma-separated list of backup phone numbers |
| description | string | No | Optional description of the voice app |
| dndCheckRequired | string | No | Enable DND check (true/false or leave empty) |
| dtmfTimeoutSeconds | integer | No | Timeout for DTMF input in seconds |
| speechTimeoutSeconds | integer | No | Timeout for speech input in seconds |
| externalCaseUrlTemplate | string | No | URL template for linking external case |
| callerSipDomain | string | No | Domain used in SIP INVITE for the caller |
| contactSipDomain | string | No | Domain used in SIP INVITE for the contact |
| fromNumberSipHeaderKey | string | No | SIP header key for passing the from number |
| supervisorEligibleForAcwOnBargeIn | boolean | No | Whether supervisor is eligible for ACW after barge-in |
| fallbackAcwId | string | No | ACW (After Call Work) ID to use if no match is found |
| callerIds | string | No | Comma-separated list of caller ID numbers |
| callEventWorkflowIvrId | string | No | ID of the IVR workflow for call events |
| byocTrunkId | string | No | Bring-Your-Own-Carrier trunk ID |
| outboundWaitMessage | string | No | Message to play while outbound call is connecting |
| jitterBufferSize | string | No | Buffer size for handling network jitter |
| locationSipContext | string | No | Context string for SIP-based location routing |

### Steps to Retrieve `voiceAccountId`

To retrieve the `voiceAccountId` required for creating or updating a Voice Application, follow these steps:


-
    **Open the Voice Account Record Manager**

    Navigate to the *Voice Account* section in your Sprinklr environment.


-
    **Inspect the Network Activity**


  - Right-click anywhere on the page and select **Inspect** to open the browser’s Developer Tools.

  - Go to the **Network** tab.



-
    **Filter and Locate the API Call**


  - Refresh the page if needed to populate network requests.

  - Look for the API request named `getPaginatedVoiceAccounts` in the list.



-
    **Copy the Voice Account ID**


  - Click on the `getPaginatedVoiceAccounts` request.

  - In the **Response** section, locate the specific Voice Account entry you want to use.

  - Copy the value of the `id` field. This is your `voiceAccountId`.



## Example - Request















Copy Code



curl --location 'https://api3.sprinklr.com/{env}/api/voice/update-voice-application' \
--header 'Authorization: Bearer {access_token}' \
--header 'Key: {api_key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "appId": "app_66127627_SP",
    "name": "Test Voice App Shivangi",
    "secondaryPhoneNumbers": "+1234,+456,+789",
    "voiceAccountId": "665d604053e7f3411f9b79e7",
    "description": "This is a test voice application updated by Shivangi",
    "country": "US",
    "dndCheckRequired": "",
    "dtmfTimeoutSeconds": 10,
    "speechTimeoutSeconds": 10,
    "supervisorEligibleForAcwOnBargeIn": false,
    "callerIds": "+123,+456,+789"
}'






## Example - Response





200 OK
{
    "errors": []
}








**Dev Note: ** 200 OK in the response implies that the voice application has been successfully updated.

[](https://dev.sprinklr.com/update-voice-application)




[Back to top](https://dev.sprinklr.com/update-voice-application)
