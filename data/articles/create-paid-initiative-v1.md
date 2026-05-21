---
title: "Create Paid Initiative v1"
slug: create-paid-initiative-v1
url: https://dev.sprinklr.com/create-paid-initiative-v1
---

# Create Paid Initiative v1

#
  POST - Create Paid Initiative

Sprinklr's Paid Media Advertising solution makes it easy to maximize the effectiveness of your advertising program. With this API call, you can create a Sprinklr Paid Initiative and, you will get the Id as a response after making a request. Users will be able to use all the supported social channel specific objectives through this API.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v1/paid/entity/paidinitiative/create

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

### Request Parameters

[https://en.wikipedia.org/wiki/ISO_4217#Active_codes](https://en.wikipedia.org/wiki/ISO_4217#Active_codes)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| channel | Required | Name of the Social Channe | Enum {FACEBOOK, TWITTER, LINKEDIN, PINTEREST, SNAPCHAT, LINE} |
| objective | Required | Campaign objective, specific to social channel. | Enum |
| name | Required | Name of the Paid Initiative. | String |
| startDate | Required | Start Date of the Paid Initiative in epoch millis. | Long |
| endDate | Optional | End Date of the Paid Initiative in epoch millis. | Long |
| spendCap | Optional | Spend Cap or Lifetime budget of the Paid Initiative. Currency would be that of the social account. If it cannot be determined by the social account, then it would be taken from the currency field mentioned below. This could happen in case of channel like Twitter. | Float |
| currency | Optional | Currency like USD, etc.  This field would be used only if the currency cannot be determined by the ad account. But a validation would be thrown in case the currency provided doesn’t match with that of ad account.  This is mandatory for cases when currency cannot be determined from ad account. | Enum  ISO currency codes  Reference: |
| accountUserId | Required | Account Id of the social account in the channel. | String |
| workSpaceId | Required | Workspace id of the channel. | Long |

## Example - Request




 Copy Code


curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v1/paid/entity/paidinitiative/create' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
	"name":"My campaign",
	"channel":"FACEBOOK",
	"objective":"CLICKS_TO_WEBSITE",
	"startDate":1551385726000,
	"endDate":1551385726000,
	"spendCap":100.45,
	"accountUserId":"10045ad",
	"workSpaceId":100,
}'



## Response Examples

### Case: Successful Response




{
	"id":"12345abcde"
}





### Case: Unsuccessful Response




{
	"error":[
		{
			"code":"MANDATORY_FIELD_MISSING",
			"message":"Name field cannot be blank"
		},
		{
			"code":"MANDATORY_FIELD_MISSING",
			"message":"Name field cannot be blank"
		}
	]
}





## Response Parameters

| Field | Description | Type |
| --- | --- | --- |
| id | Id of the Paid Initiative if successfully created. | String |
| error | Code: Code and Description table for Error Codes are given below.Message: User facing error message with localization. | Array of Objects |

## Error Codes

| Code | Description |
| --- | --- |
| MANDATORY_FIELD_MISSING | When mandatory fields are left blank or not provided. |
| ENUM_VALUE_INCORRECT | Enum value is wrong for example for currency if the value provided is USDA instead of USD. |
| CURRENCY_INCORRECT | Currency doesn’t match with Ad account currency. |
| WORKSPACE_NOT_FOUND | Workspace specified doesn’t exist. |
| ACCOUNT_NOT_FOUND | Ad Account specified doesn’t exist in the workspace. |
| OBJECTIVE_INCORRECT | Objective mentioned isn’t supported for the social channel chosen. |
| INCORRECT_DATE | Start or End date provided is in the past or End Date < Start Date. |
| CHANNEL_NOT_SUPPORTED | The channel for the account mentioned is not supported by the API. |
| UNKNOWN_ERROR | Unknown Error - please contact Sprinklr Support. |

[](https://dev.sprinklr.com/create-paid-initiative-v1)




[Back to top](https://dev.sprinklr.com/create-paid-initiative-v1)
