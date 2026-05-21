---
title: "Create Case Via Associated Messages"
slug: create-case-via-associated-messages
url: https://dev.sprinklr.com/create-case-via-associated-messages
---

# Create Case Via Associated Messages

#
  POST  Create Case Via Associated Messages


The Create Case with Associated Messages API enables the creation of a new case in Sprinklr while simultaneously attaching relevant messages—such as transcripts or conversation logs—to the case.
This functionality is designed to support integrations with third-party systems like External Bots, where customer interactions are captured in real-time and need to be contextualized within a case for downstream processing.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/case/create-with-messages

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

## Request Body Parameters















































****``````


























































      ``






      ``






      ``






      ``






      ````








****

- ****``
- ****
  -
  - ``
``








****

- ****``
- ****
  - ``
  -






      ``




















      ``






      ``



| Parameter | Sub-Parameter | Optional/Required | Type | Description |
| --- | --- | --- | --- | --- |
| subject |  | Optional | String | Subject of the case. |
| description |  | Optional | String | Description of the case. |
| workflow |  | Optional | Object | The object containing the workflow details. |
|  | customProperties | Optional | String | Custom property object containing metadata such as Ressort ID, priority, calling reason, location, etc., in key-value format. |
| channelType |  | Required | String | The channel type associated with the profile.         Note: This value is case-sensitive. Use uppercase values like SMS or EMAIL. Example: SPRINKLR_VOICE. |
| channelId |  | OptionalRequired for all channels except EMAIL and SMS | String | Unique identifier for the customer profile.         Acts as the primary key for the profile in Sprinklr.         Example: Reusing the same channelId in multiple API calls associates the new case with the existing customer profile. |
| contactInfo |  | Required | Object | The object containing contact details associated with the profile. |
|  | firstName | Optional | String | First name of the profile. |
|  | lastName | Optional | String | Last name of the profile. |
|  | fullName | Optional | String | Full name of the profile. |
|  | phoneNo | Required for SMSOptional for EMAIL | String | Phone number associated with the profile. |
| associatedMessages |  | Required | Array of Objects | List of messages to be associated with the case. |
|  | messageId | Required | String | Unique message ID in the format: ACCOUNT_<sourceId>_<channelCreatedTime>_SOURCE_AGNOSTIC_432_<channelMessageId>. |
|  | sourceType | Required | String | Hardcoded value: ACCOUNT. |
|  | sourceId | Required | String | Hardcoded value (e.g., 66000030). |
|  | content | Required | Object | Transcript content. Example: { "text": "customer message" } |
|  | channelMessageId | Required | String | Genesys-generated unique message ID (e.g., c1, c2). Must match the suffix in messageId. |
|  | senderProfile | Required | Object | Provides metadata about the originator of the message (customer or brand/bot).         Attributes:                    channelType: Hardcoded value: SOURCE_AGNOSTIC           channelId:                            If customer message – use customer's phone number.               If brand message – use hardcoded ID: 66c895e5f780694bbb0837b1                                          Example:         "senderProfile": { "channelType": "SOURCE_AGNOSTIC", "channelId": "+19172034633" } |
|  | receiverProfile | Required | Object | Provides metadata about the recipient of the message (brand/bot or customer).         Attributes:                    channelType: Hardcoded value: SOURCE_AGNOSTIC           channelId:                            If customer message – use hardcoded ID: 66c895e5f780694bbb0837b1               If brand message – use customer's phone number |
|  | channelCreatedTime | Required | String | Epoch timestamp of message creation in external bot (e.g., 1724333771000). |
|  | createdTime | Required | String | Epoch timestamp when the message was created in Sprinklr (same as channelCreatedTime in this use case). |
|  | modifiedTime | Required | String | Epoch timestamp when the message was last modified. |
|  | brandPost | Required | String | true if message is posted by external bot (typically for bot/brand messages). |
|  | autoResponse | Required | String | true if the message is an automatic response generated by external bot. |


## Example - Request




 Copy Code



curl --location 'https://api3.sprinklr.com/{env}/api/v2/case/create-with-messages' \
--header 'Authorization: Bearer {token}’ \
--header 'Content-Type: application/json' \
--header 'Cookie: user.env.type=ENTERPRISE' \
--data '{
    "subject": "SM Case creation",
    "description": "Description of the case",
    "workflow": {
        "customProperties": {
            "ressortID": [
                "1234"
            ],
            "spr_uc_priority": [
                "High"
            ],
            "_c_66c466b44ee87b14829998ed": [
                "Billing"
            ],
            "_c_66c2ece58c7d8703b61b4d6a": [
                "INDIA"
            ],
            "_c_66c2ece58c7d8703b61b4d6a": [
                "INDIA"
            ],
            "_c_66c4bedfdb55fe51a39aa277": [
                "Yes"
            ]
        }
    },
    "channelType": "SPRINKLR_VOICE",
    "channelId": "+19172034633",
    "contactInfo": {
        "firstName": "Dheeraj",
        "lastName": "Y",
        "fullName": "Dheeraj Y",
        "phoneNo": "+19172034633"
    },
    "associatedMessages": [
        {
            "messageId": "ACCOUNT_66000030_1723099052000_SOURCE_AGNOSTIC_432_c111111_unm1_saat121111111111122asa",
            "sourceType": "ACCOUNT",
            "sourceId": 66000030,
            "content": {
                "text": "customer message"
            },
            "channelMessageId": "c1",
            "channelType": "SOURCE_AGNOSTIC",
            "accountType": "SOURCE_AGNOSTIC",
            "senderProfile": {
                "channelType": "SOURCE_AGNOSTIC",
                "channelId": "+19172034633"
            },
            "receiverProfile": {
                "channelType": "SOURCE_AGNOSTIC",
                "channelId": "663caccd472e572a74286325"
            },
            "channelCreatedTime": 1724333771000,
            "createdTime": 1724333771000,
            "modifiedTime": 1724333771000
        },
        {
            "messageId": "ACCOUNT_66000030_1723099052000_SOURCE_AGNOSTIC_432_c10111111_unm2_saat2211111111111122asasa",
            "sourceType": "ACCOUNT",
            "sourceId": "66000030",
            "content": {
                "text": "brand message"
            },
            "channelMessageId": "c2",
            "channelType": "SOURCE_AGNOSTIC",
            "accountType": "SOURCE_AGNOSTIC",
            "senderProfile": {
                "channelType": "SOURCE_AGNOSTIC",
                "channelId": "663caccd472e572a74286325"
            },
            "receiverProfile": {
                "channelType": "SOURCE_AGNOSTIC",
                "channelId": "+19172034633"
            },
            "channelCreatedTime": 1724333771000,
            "createdTime": 1724333771000,
            "modifiedTime": 1724333771000,
            "brandPost": true,
            "autoResponse": true
        }
    ]
}'





## Example - Response




	{
    "data": {
        "id": "67b32dfba735514b4a315123",
        "caseNumber": 6734261,
        "subject": "SM Case creation",
        "description": "Description of the case",
        "version": 0,
        "priority": "High",
        "externalCaseInfo": {
            "externalCases": []
        },
        "workflow": {
            "customProperties": {
                "_c_66c4bedfdb55fe51a39aa277": [
                    "Yes"
                ],
                "_c_66c466b44ee87b14829998ed": [
                    "Billing"
                ],
                "ressortID": [
                    "1234"
                ],
                "spr_uc_priority": [
                    "High"
                ],
                "_c_66c2ece58c7d8703b61b4d6a": [
                    "INDIA"
                ],
                "spr_is_profile_case": [
                    "true"
                ]
            },
            "queues": []
        },
        "channelCustomProperties": [],
        "contact": {
            "id": "SPRINKLR_VOICE_+19172034633",
            "channelType": "SPRINKLR_VOICE",
            "channelId": "+19172034633",
            "fromSnUserId": "+19172034633"
        },
        "createdTime": 1739795963572,
        "modifiedTime": 1739795963578,
        "latestMessageAssociatedTime": 1739795963572,
        "totalProcessingClockTime": 0,
        "allEngagedUsersList": [],
        "associatedFanMessageCount": 0,
        "associatedBrandMessageCount": 0,
        "associatedUserBrandMessageCount": 0,
        "deleted": false
    },
    "errors": []
}





[](https://dev.sprinklr.com/create-case-via-associated-messages)




[Back to top](https://dev.sprinklr.com/create-case-via-associated-messages)
