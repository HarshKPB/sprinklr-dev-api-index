---
title: "Update Message Properties with Attachement"
slug: update-message-properties-with-attachement
url: https://dev.sprinklr.com/update-message-properties-with-attachement
---

# Update Message Properties with Attachement

#
  PUT Update Message Properties with Attachment




Use this API to update message content and manage photo and video attachments on one or more existing messages.

**What You Can Do**


- Edit message text and replace the current attachment.

- Add image or video attachments.

- Append additional attachments instead of replacing existing ones.

- Clear existing attachments from a message.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/message/workflow-with-attachments

### Headers

API headers include the mandatory information that you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.








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







| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |

## Request Body

















****``**************[channelType](https://dev.sprinklr.com/channels-v1)****[messageType](https://dev.sprinklr.com/message)******




























      ``






      ``



| Parameter | Sub-parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- | --- |
| messageIds |  | Required | Array<string> | One or more message IDs to update. Dev Notes: messageId= sourceType (ACCOUNT, PERSISTENT_SEARCH, LISTENING) + “_”+ sourceId + “_” + channelCreatedTime + “_” + “” + “_” + ” “ +”_” + channelMessageId |
| content |  | Optional* | Object | Content updates, including text and attachment. |
|  | text | Optional | String | Updated message text. |
|  | attachment | Optional | Object | Attachment details (image or video). |
| appendAttachments |  | Optional | Boolean | If true, adds the provided attachment(s) to the message         instead of replacing existing ones. |
| clearAttachments |  | Optional | Boolean | If true, removes existing attachments from the specified         message(s). |

  *
    * `content` is required when you are adding or editing text or
    attachments. When `clearAttachments` is set to `true`,
    you can omit `content`.
  *

### Attachment Object














      ````









| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| type | Required (when attachment is provided) | String | Attachment type. Supported values: IMAGE, VIDEO. |
| url | Required (when attachment is provided) | String | Public or secure URL for the asset to attach. |

## Behavior and Rules

### Replace vs. Append


-
    **Default behavior (no flags):**
    The attachment specified in `content.attachment` is treated as the
    updated attachment payload. This is commonly interpreted as replace behavior.


-
    **Append behavior:**
    Set `appendAttachments: true` to add the attachment to the message
    while keeping existing attachments.


### Clear Attachments


-
    Set `clearAttachments: true` to remove existing attachments from
    the message or messages.


-
    When clearing attachments, do not send `content.attachment` unless
    your platform implementation explicitly supports clearing and adding
    attachments in a single request.


### Flag Interactions (Recommended)

  To avoid ambiguous operations, follow these guidelines:


-
    Do not set `appendAttachments: true` and
    `clearAttachments: true` in the same request.


-
    If you need to clear attachments and then attach new media, perform the
    operation in two calls:


  - Clear attachments

  - Update or add attachments



## Example 1 - Update text and set an IMAGE attachment















Copy Code



curl --location --request PUT 'https://api3.sprinklr.com/{env}/api/v2/message/workflow-with-attachments?accountId=87654321' \
--header 'Authorization: Bearer ' \
--header 'Key: {API_Key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "messageIds": [
        "ACCOUNT_87654321_1774451552605_SOURCE_AGNOSTIC_432_case_054_message_054"
    ],
    "content": {
        "text": "Hi, my name is Shivi. This is a test message image",
        "attachment": {
            "type": "IMAGE",
            "url": "https://space-qa6.sprinklr.com/ui/rest/secure-assets/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3Nwci1xYTYtY2RuLXNlY3VyZS9EQU0vNjYwMDAwMDAvYzliOWM4N2ItYzdjMC00OWE5LWFiYTQtZDViNzIwMTgxNWRmLTg1MzU4OTIwMS9odHRwc19fX3FhNi1tZWRpYS1wcm94eS5zcHJpbmsuanBn"
        }
    }
}'






## Example 2 - Append a VIDEO attachment















Copy Code



curl --location --request PUT 'https://api3.sprinklr.com/{env}/api/v2/message/workflow-with-attachments?accountId=87654321' \
--header 'Authorization: Bearer ' \
--header 'Key: {API_Key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "messageIds": [
        "ACCOUNT_87654321_1774451552605_SOURCE_AGNOSTIC_432_case_054_message_054"
    ],
        "content": {
        "attachment": {
            "type": "VIDEO",
            "url": "https://prod0-secure-content.sprinklr.com/ui/rest/secure-content-redirection/signed/redirect?accessToken=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJBY2Nlc3MgVG9rZW4gR2VuZXJhdGVkIEJ5IFNwcmlua2xyIiwiY2xpZW50QWNjZXNzIjpmYWxzZSwidmFsaWRhdGVVcmwiOnRydWUsImlzcyI6IlNQUklOS0xSIiwidHlwIjoiSldUIiwib3JpZ2luYWxVcmwiOiJodHRwczovL3Byb2QwLWNkYXRhLXNlY3VyZS5zcHJpbmtsci5jb20vREFNLzkwMDQvMDk1YTA0ODMtY2RkZS00MDkxLWJmYzUtZWJlZmExNTAyZWFlLTk2MDAzNDMyMC5tcDQiLCJhdWQiOiJTUFJJTktMUiIsInNjb3BlIjpbIlJFQUQiLCJXUklURSJdLCJleHAiOjE3NjkwNTg5MDksInRva2VuVHlwZSI6IkFDQ0VTUyIsImF1dGhUeXBlIjoiU0VDVVJFX1VQTE9BRF9WMiIsImlhdCI6MTc2ODg4NjEwOSwianRpIjoiMGNkNDQyODItNjY5Yi00NzBmLTlmMzEtZDNlYTNjZTUwNjdiIn0.uIIBA9dbIXNW8YdVuWVwH2_VxzLPnmq_DcwAya3Bjkym2krJkR3kY6gen8Mo5QcpRFux9KZBPmTwKS7x4w9Xm7O83svMzVmyJisjPPbxvjrp6OV7YnEZYuwFWhN-zeDA7yYPZ6y1LXKQhEFDFcPaMgkKAdWChsby62gGDkMmGSNceBZVRGtNlBXeKDGWLpfKrJyx7I9Kneu7sDQRe0Auhkpve5qgGrSWSG_50zzvdvKcfnGhXVSN18v6KN923ppU0T-R2b9NXuvBecdd1hgscs_zduGZxc4TE3QZth1xlLM5Xgf1apz6Hz-eMFMfXl5XTSPZn31liBupHFm5uB7J9A"
        }
    },
    "appendAttachments":true
}'






## Example 3 - Clear Existing Attachments















Copy Code



curl --location --request PUT 'https://api3.sprinklr.com/{env}/api/v2/message/workflow-with-attachments?accountId=87654321' \
--header 'Authorization: Bearer ' \
--header 'Key: {API_Key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data'{
    "messageIds": [
        "ACCOUNT_87654321_1774451552605_SOURCE_AGNOSTIC_432_case_054_message_054"
    ],
    "clearAttachments": true
}'






### Example Response





204 No Content







	[](https://dev.sprinklr.com/update-message-properties-with-attachement)




[Back to top](https://dev.sprinklr.com/update-message-properties-with-attachement)
