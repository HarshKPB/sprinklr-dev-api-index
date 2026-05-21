---
title: "Lookup By Id"
slug: lookup-by-id
url: https://dev.sprinklr.com/lookup-by-id
---

# Lookup By Id

#
  POST Lookup By Id



Lookup API helps find details of different entities based on the lookup type and respective Ids present within the keys parameter.


**Dev Note: ** Supported lookup types: `ACCOUNT_ID`, `USER_ID`, `CASE_ID`, `CUSTOM_FIELD`, `FACEBOOK_PLACES_LOOKUP` (for Instagram), `ASSIGNMENT_SKILL, LOCATION_IDS`

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/lookup

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


### Request Parameters
















****






****




| Parameters | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| lookupType |  | Required | Required for lookup endpoint requestsSupported lookup types: ACCOUNT_ID, USER_ID, CASE_ID, CUSTOM_FIELD, and FACEBOOK_PLACES_LOOKUP (for Instagram), ASSIGNMENT_SKILL | String |
| extraParams |  | OptionalRequired when lookupType is CUSTOM_FIELD | Refers to the object containing any additional required parameters for the given lookup type | Object |
|  | assetType | Required | Refers to the asset type associated with the custom fieldIf there are multiple asset types, you can either of the asset types that are applicable on the custom field | String |
| Keys |  | Required | Parameters related to the lookupTypeExample: If ACCOUNT_ID is the lookupType; keys would include Account Ids | String, Integer |

**Dev Note:**lookupType differs from use case to use case. For instance, the lookup type is ASSIGNMENT_SKILL, it helps fetch all the skills associated with the skill ids (that you can fetch using [this API)](https://dev.sprinklr.com/fetch-skills-and-proficiency) provided under the “keys” parameter.


### Request Example Where lookupType = ACCOUNT_ID















Copy Code



curl -X POST \
 https://api3.sprinklr.com/{env}/api/v2/lookup\
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
	"lookupType": "ACCOUNT_ID",
    "keys": [
        "600044848"
    ]
}'






### Example - Response





{
    "data": {},
   "errors": []
}







### Request Example Where lookupType = ASSIGNMENT_SKILL















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/lookup' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
   "lookupType": "ASSIGNMENT_SKILL",
   "keys": [
       "5fbfc48accb38e37b031cb65",
       "5e9fdead02ec853ab5c73c78",
       "5eaff2c302ec853f2150258f",
       "5eaff2cb02ec853f21502679",
       "5ede78c522098613e5dfd9c9",
      ]
}'






### Example - Response





{
   "data": {
      "5fbfc48accb38e37b031cb65": "skill 1"
      "5e9fdead02ec853ab5c73c78": "skill 2",
      "5eaff2c302ec853f2150258f": "skill 3",
      "5eaff2cb02ec853f21502679": "skill 4",
      "5ede78c522098613e5dfd9c9": "skill 5",
},
   "errors": []
}






	[](https://dev.sprinklr.com/lookup-by-id)






[Back to top](https://dev.sprinklr.com/lookup-by-id)
