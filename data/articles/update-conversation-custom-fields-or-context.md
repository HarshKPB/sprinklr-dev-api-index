---
title: "Update Conversation Custom Fields or Context"
slug: update-conversation-custom-fields-or-context
url: https://dev.sprinklr.com/update-conversation-custom-fields-or-context
---

# Update Conversation Custom Fields or Context

# Update Conversation Custom Fields

You can use this method to update the custom fields/context associated with a conversation.

Custom fields are the properties or metadata associated with certain entities in Sprinklr such as message or case. To know more about custom fields, see [Custom Fields.](https://www.sprinklr.com/help/articles/sprinklr-service-glossary/custom-fields/63af40eb3fece76798a35ff2)

**Dev Notes: **To ensure data security of custom fields, Sprinklr offers certain security features. For more information, see [Custom Fields Data Security Features](https://dev.sprinklr.com/update-conversation-custom-fields-or-context#cf_data_security).

## Method

	 `sprChat('updateConversationContext');`

## Parameters







| Parameter | Type | Required/Optional | Description | Default value |
| --- | --- | --- | --- | --- |
| context | StringTMap<string[]> | Required | Map of custom field IDs and their values that you want to update in the conversation. | None |
| conversationId | String | Optional | Sprinklr defined conversation ID. | Latest active and open conversation |

## Examples

**Example 1**: The following example updates the value of the `_c_abcdef123` custom field to `123` in the conversation with ID `conv_1`:




  Copy Code



window.sprChat('updateConversationContext', {
    conversationId: 'conv_1',
    context: {
       '_c_abcdef123': ['123'],
    }
 });





**Example 2**: The following example updates the value of the `_c_abcdef123` custom field to `123` on the latest active and open conversation:




  Copy Code



window.sprChat('updateConversationContext', {
    context: {
       '_c_abcdef123': ['123'],
    }
 });






## Custom Fields Data Security Features


To enhance data security when updating custom fields, brands can use the following features:


### Whitelist Custom Fields


Brands can whitelist custom fields, allowing only whitelisted profile or case-level custom fields to be updated. Any non-whitelisted fields will remain unchanged, even if new values are included in the update SDK method. To enable this feature, contact Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).


### Sending Encrypted Data in Custom Fields


To enhance security and protect sensitive information, brands can send custom field values in an encrypted JSON Web Token (JWT) format instead of plaintext. The JWT will be decrypted using a predefined key, which is configured in the backend during the enablement process. To enable this feature, contact Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

Once enabled, brands can use the following function to decrypt JWT in the conversational AI bot:

`Map<String, Object> map= JWT.validateAndGetJwtClaims("JWT_TOKEN", "KEY_IDENTIFIER");
	return MAP_UTILS.getString(map, "KEY_NAME");`

The following are descriptions of the variables:



- `JWT_TOKEN`: Custom field value in encrypted JWT format.

- `KEY_IDENTIFIER`: A key identifier to pick the correct decryption key.

- `KEY_NAME`: The specific key whose value you want to retrieve.


**How it Works**: The function receives the JWT token and the key identifier. The key identifier is used to fetch the correct decryption key from the backend. Once the key is obtained, the JWT is decrypted and the key-value pairs (claims) are extracted. The function returns the value associated with the specified key name from the extracted claims.



[](https://dev.sprinklr.com/update-conversation-custom-fields-or-context)

[Back to top](https://dev.sprinklr.com/update-conversation-custom-fields-or-context)
