---
title: "Apply Macro"
slug: apply-macro
url: https://dev.sprinklr.com/apply-macro
---

# Apply Macro

#
  POST Apply Macro




This API allows you to automate the application of macros on various Entities, including Cases, Outbound Messages, User-Generated Content, Profiles, Campaigns, and more.

### Use Cases:

- **Automate Macro Application:** Streamline the process by automatically applying macros to Cases, Profiles, UGC, Campaigns, Outbound Messages, Tasks, Sub-Campaigns, Media Assets, and Social Accounts.

- **Boost Productivity:** Reduce manual effort and enhance agent productivity by automating macro application.

- **Enable Complex Automation:** Facilitate the automation of complex actions across the supported entity types.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/macro/apply

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.







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

## Request Parameters







****

| Key | Value | Type | Description |
| --- | --- | --- | --- |
| assetClass | Required | String | Refers to the asset type on which the macro needs to be appliedExample: UNIVERSAL_CASE for case asset typeEnum: [ UNIVERSAL_CASE, MESSAGE, OUTBOUND_MESSAGE, USER_GENERATED_CONTENT, SPR_TASK, PROFILE, CAMPAIGN, SUB_CAMPAIGN, MEDIA_ASSET, ACCOUNT ] |
| entityKeys | Required | List [String] | Refers to the unique identifier for the entity on which the macro needs to be applied |
| macroIds | Required | List [String] | Refers to the unique identifier for the macros to be applied |

## Example - Request















Copy Code



curl -X POST \
'https://api3.sprinklr.com/{env}/api/v2/macro/apply' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{"assetClass": "UNIVERSAL_CASE",
       "entityKeys": [
        "1724559"
                    ],
        "macroIds": [
          "667bf9b8b9d50132d01cfd5d"
                   ]
      }'






## Example - Response





204 No Content







[](https://dev.sprinklr.com/apply-macro)




[Back to top](https://dev.sprinklr.com/apply-macro)
