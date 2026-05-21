---
title: "Update Message Properties"
slug: update-message-properties
url: https://dev.sprinklr.com/update-message-properties
---

# Update Message Properties

#
  PUT Update Message Properties




This API helps update the custom properties of the message in the workflow.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/message/workflow

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

### Request Body Parameters







****
- ****
- ****
- ****[Custom Properties Actions](https://dev.sprinklr.com/update-message-properties#custom-property-actions)

````

- ****
- ****
- ****
- ****

[Example 2](https://dev.sprinklr.com/update-message-properties#example2)

| Parameter | Required/Optional | Type | Description |  |
| --- | --- | --- | --- | --- |
| Custom Property Action | Optional(include when updating custom properties) | Object | This parameter specifies the execution action on messages.Supported Values:    customProperties   customPropertiesToAdd   customPropertiesToRemove  For more information, see  table below. |  |
|  | "fieldName": ["value"] | Optional(include when updating custom properties) | String | It contains key-value pairs where each key represents the fieldName and each value is an array of property values that need to be added, merged or removed. |
| messageIds | Required | Array of Strings | Message identifiers for which the custom properties actions (merge, remove, or replace) will be applied. Each messageId is structured as account_accountId_createdTimestamp_umid where:  account represents the platform (e.g., FACEBOOK, TWITTER). accountId is the unique identifier for the account. createdTimestamp is the UNIX timestamp of the message creation. umid (Universal Message ID) is a unique identifier for the message. |  |
| message | Optional(include when updating message content) | String | The new message content to replace the current text of the specified message IDs. See . |  |


**Dev Notes:** Custom property actions and field names are optional and required only when updating properties. To update just the `message` content, omit these actions and include only the `message` and `messageIds` fields in your request.

### Custom Properties Actions

There are three types of custom properties actions available as listed in the table below:







| Custom Property Action | Description |
| --- | --- |
| customProperties | This action is used to replace existing custom properties in the specified messages with the provided ones. It completely overwrites any current values of the custom properties with the new values provided in the request. |
| customPropertiesToAdd | This action is used to merge specific custom properties into the existing properties of the specified messages. The provided properties will be added to the current set, allowing for the inclusion of additional values without removing existing ones. |
| customPropertiesToRemove | This action is used to remove specific custom properties from the specified messages. The provided properties will be deleted from the existing set, ensuring that only the desired properties remain. |

## Example 1 - Remove Custom Property















Copy Code



curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/message/workflow' \
  -H 'Authorization: Bearer {token}' \
  -H 'key: {apikey}' \
  -H 'Content-Type: application/json' \
  -data' {
    "customPropertiesToRemove": {
        "_c_64e2fba8c4002661cafec06a": [
            "3"
        ]
    },
    "messageIds": [
        "ACCOUNT_600029426_1724753200206_FACEBOOK_38_m_cyNlSvWi8VnI_nZiiTys9N-O6gf0cPA5wbfoCZdjKl8d7fLnSxaIPM4AGXs4dhrk6X1f8hNXokAoM4OrhJWOxg"
    ]
}'






## Example 2 - Update Message Content















Copy Code


curl --location --request PUT 'https://api3.sprinklr.com/{env}/api/v2/message/workflow' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
  "messageIds": [
    "ACCOUNT_66125927_1758891128000_FACEBOOK_97_122148485282565734_1456861735581080"
  ],
  "message": "edited via API"
}'






#### Example Response





204 No Content







	[](https://dev.sprinklr.com/update-message-properties)




[Back to top](https://dev.sprinklr.com/update-message-properties)
