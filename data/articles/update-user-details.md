---
title: "Update User Details"
slug: update-user-details
url: https://dev.sprinklr.com/update-user-details
---

# Update User Details

# Update User Details

This method is used to update the current user and their details. With this method, you can update user details, authenticate the current anonymous user, log out the current authenticated user, or update the custom fields/context for the current user.

**Dev Notes: **To ensure data security of custom fields, Sprinklr offers certain security features. For more information, see [Custom Fields Data Security Features](https://dev.sprinklr.com/update-user-details#cf_data_security).

## Method

	 `sprChat('updateUserSettings');`

## Parameters







| Name | Type | Required/Optional | Description | Default value |
| --- | --- | --- | --- | --- |
| userContext | StringTMap<string[]> | Optional | Map of custom field IDs and their values associated with the user that you want to update. | None |
| user | {       id: string;       hash: string;       email?: string;       firstName?: string;       lastName?: string;       profileImageUrl?: string;       phoneNo?: string;  } | Optional | Details of the user you want to update. | None |

## Examples

**Example 1**: The following example updates the value of the `_p_abcdef123` custom field to `123` for the current user.




  Copy Code



window.sprChat('updateUserSettings', {
  userContext: {
       '_p_abcdef123': ['123'],
   }
 });





**Example 2**: The following example updates user details for the current anonymous user:




  Copy Code



window.sprChat('updateUserSettings', {
    user: {
      firstName: 'live',
      lastName: 'chat',
      email: 'live-chat@sprinklr.com'
    },
 });





**Example 3**: The following example updates user details for the currently authenticated user:




  Copy Code



window.sprChat('updateUserSettings', {
    user: {
      id: '123',
      hash: '12adsfasdf1231sadasfasfas1231dgfggf',
      firstName: 'live'
      lastName: 'chat',
      email: 'live-chat@sprinklr.com'
    },
 });





**Example 4**: If your current user is anonymous, calling the following method updates the session by merging the current user and their history with the authenticated user and their history:




  Copy Code



window.sprChat('updateUserSettings', {
    user: {
      id: '123',
      hash: '12adsfasdf1231sadasfasfas1231dgfggf',
      firstName: 'live'
      lastName: 'chat',
      email: 'live-chat@sprinklr.com'
    },
 });






**Example 5**: If your current user is authenticated, calling the following method changes the session by logging out the authenticated user and clearing their history, creating a new anonymous user.




  Copy Code



window.sprChat('updateUserSettings', {
    user: {},
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



[](https://dev.sprinklr.com/update-user-details)

[Back to top](https://dev.sprinklr.com/update-user-details)
