---
title: "Apply Macro (v1)"
slug: v1-apply-macro
url: https://dev.sprinklr.com/v1-apply-macro
---

# Apply Macro (v1)

# POST Apply Macro (v1)

Using this API you can apply Macros to execute multiple actions on a message, asset, or profile to have workflow efficiencies. Using [Bootstrap](https://dev.sprinklr.com/v1-bootstrap-resources) you can fetch all the available macros and their configuration information.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/macro/apply

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/'/api-key-and-secret-generation)



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

| Key | Value | Description |  |
| --- | --- | --- | --- |
| assetClass | Required | Refers to the asset type on which the macro needs to be appliedExample: UNIVERSAL_CASE for case asset typeEnum: 					 						[ UNIVERSAL_CASE, MESSAGE, OUTBOUND_MESSAGE, USER_GENERATED_CONTENT, SPR_TASK, PROFILE, CAMPAIGN, SUB_CAMPAIGN, MEDIA_ASSET, ACCOUNT ] | String |
| entityKeys | Required | Refers to the unique identifier for the entity on which the macro needs to be applied | List [String] |
| macroIds | Required | Refers to the unique identifier for the macros to be applied | List [String] |

### Steps to Extract Request Payload from UI

- Open an Asset Class in Sprinklr UI on which you want to apply Macro.

- Open Inspect Element and click Network tab.

- Manually apply the Macro to the case within Sprinklr UI.

- In the Network tab locate under Name "apply".

- Scroll down to "Request Payload" section within Headers.

- Click view source to view the payload

- Copy the payload and use it as your request body to make an API call.

## Example - Request




 Copy Code



curl -X POST \
'https://api2.sprinklr.com/{env}/api/v1/macro/apply' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "assetClass": "UNIVERSAL_CASE",
    "entityKeys": [
        "25355193"
    ],
    "macroIds": [
        "5d22fc06e4b01f1d357ed8b7"
    ]
}'



## Example - Response





204 No Content



[](https://dev.sprinklr.com/v1-apply-macro) 

 

 
[Back to top](https://dev.sprinklr.com/v1-apply-macro)
