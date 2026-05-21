---
title: "CFM Workflow API"
slug: cfm-workflow-api
url: https://dev.sprinklr.com/cfm-workflow-api
---

# CFM Workflow API

# POST CFM Workflow API


The CFM Workflow API allows you to create or update customer profiles and utilize the provided parameters to trigger personalized survey distributions via Email, SMS, or WhatsApp. This enables seamless and targeted customer feedback collection based on specific events.

##  API Endpoint

https://api3.sprinklr.com/{env}/api/v2/cfm-workflow/triggerWithNewProfile

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














[create/update universal profile](https://dev.sprinklr.com/create-update-universal-profile)

| Parameters | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| workflowId | Required | String | Unique identifier of the workflow to be triggered. |
| contextParams | Optional | Object | Key and value pair that provides additional information about the customer and their journey |
| unifiedProfile | Required | Object | Refer to the  API documentation for understanding profile creation object parameters The tables below describe the request parameters for creating unified profile |

### unifiedProfile Parameters Description Table






























































































































































































			x
























































































































| Parameter | Sub Parameters | Required/Optional | Type | Description |
| --- | --- | --- | --- | --- |
| id |  | Optional | String | Unique identifier of the unified profile. |
| contact |  | Optional |  | Contact information of the profile. |
|  | firstName | Optional | String | First name of the profile. |
|  | maidenName | Optional | String | Maiden name of the profile. |
|  | lastName | Optional | String | Last Name of the profile. |
|  | fullName | Optional | String | Full name of the profile. |
|  | email | Optional | String | Email id of the profile. |
|  | phoneNo | Optional | String | Phone number of the profile. |
|  | address | Optional | String | Address of the profile.Schema for Address Table given below. |
|  | website | Optional | String | List of websites for the profile. |
| demographics |  | Optional |  | Demographic Information of the client. |
|  | age | Optional | Integer | Age of the profile. |
|  | location | Optional | String | Location of the profile. |
|  | gender | Optional | String | Gender of the profile. |
|  | language | Optional | String | Language of the profile. |
| profiles |  |  |  | List of social identities linked to the profile. |
|  | name | Required | String | Name of the person. |
|  | channelType | Required | String | Channel type of the profile. e.g. facebook. |
|  | channelId | Required | String | Refers to the unique identifier for the customer profile. If the channelId is unique, a new profile will be created and a journey will be associated with it, else the journey will be associated with the existing profile. |
|  | permalink | Optional | String | Link of the profile on social channel. |
|  | avatarUrl | Optional | String | Profile image link. |
|  | bio | Optional | String | Detailed description about the user. |
|  | followers | Optional | Integer | Followers count of the user. |
|  | username | Optional | String | Unique identifier of the user. |
|  | verified | Optional | Boolean | True if the user is verified by the channel. 				default: false |
|  | unSubscribed | Optional | Boolean | True if the user is subscribed for email and other activities.default: false |
|  | deleted | Optional | Boolean | True if profile is deleted natively.default: false |
|  | snCreatedTime | Optional | Integer | Social Channel created time. |
|  | snModifiedTime | Optional | Integer | Social Channel modified time. |
|  | accountSpecificInfos | Optional |  | Account Specific Info like accountId, externalId, etc.Account Specific Info Table given below. |
| profileWorkflow |  |  |  |  |
|  | profileLists | Optional | Integer | Partner profile lists on the profile, if any. |
|  | customProperties | Optional | String | Partner custom properties on the profile, if any.  Profile Level Custom Fields are not supported currently. |
|  | profileSpaceWorkflows | Optional |  | List of client level workflows on the profile, if any.ProfileSpaceWorkflow Table given below. |
| createdTime |  | Optional | Integer | Created time of the profile in sprinklr. |
| modifiedTime |  | Optional | Integer | Last modified time of the profile in sprinklr. |

### Address Parameter Description Table

















































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| street1 | Optional | First line of the user's address. | String |
| street2 | Optional | Second line of the user's address. | String |
| city | Optional | The city of the user's address to help identify the location. | String |
| state | Optional | The state of the user's address. | String |
| country | Optional | The country of the user's address. | String |
| postalCode | Optional | ZIP Code of the address. | String |

### Account Specific Info Parameter Description Table































































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| accountId | Optional | Account id of the profile. | Integer |
| externalId | Optional | External id of the profile. | String |
| lastBrandEngagedTime | Optional | Last brand engagement time. | Integer |
| lastFanEngagedTime | Optional | Last fan engagement time. | Integer |
| optIn | Optional | If True, optin.default: false | Boolean |
| fanSubscriptionState | Optional | Subscription state of fan. | String |
| activeUser | Optional | If True, user id active.default: false | Boolean |
| invited | Optional | If True, invited.default: false | Boolean |

### Profile Space Workflow Parameter Description Table































































| Parameter | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| spaceId |  | Required | Client Id. | String |
| modifiedTime |  | Optional | Last modified time of the space workflow | Integer |
| customFields |  | Optional | Client custom properties on the asset, if any. | String |
| queues |  | Optional | Client queue details of the message, if any. | Integer |
|  | queueId | Optional | Queue identifier to add the message to queue. | Integer |
|  | assignmentTime | Optional | Assignment time of the queue to the message. | Integer |
| profileLists |  | Optional | Client profile lists on the profile, if any. | Integer |


### Example - API Request















Copy Code



curl --request POST \
 --url 'https://api3.sprinklr.com/{env}/api/v2/cfm-workflow/triggerWithNewProfile' \
  --header 'Authorization: Bearer {Access_Token}' \
  --header 'Key: {API_Key}'\
 --header 'Content-Type: application/json' \
 --header 'Accept: application/json' \
  --data '{
	"workflowId":"6df11e44-72ba-46ac-a5a4-aad1d1ee4255",
	"contextParams": {
		"IGNORE_DEDUP": true,
		"lang":"ar",
		"country":"Jordan",
		"countryCode": "SA",
		"surveyFilled": "true"
	},
	"unifiedProfile": {
		"contact": {
			"firstName": "John Doe"
		},
		"profiles": [
			{
				"channelType": "WHATSAPP_BUSINESS",
				"channelId": "9174628306756",
				"name": "John Doe"
			},
			{
				"channelType": "SMS",
				"channelId": "9174628306756",
				"name": "John Doe"
			},
			{
				"channelType": "EMAIL",
				"channelId": "test@sprinklr.com",
				"name": "John Doe"
			}
		]
	}
}'






### Example - Response





	{
    "data": "\"Success\"",
    "errors": []
}







**Dev Notes: **A "Success" status indicates that the API Endpoint was successful in trigerring the CFM Workflow for the Profile.

	[](https://dev.sprinklr.com/cfm-workflow-api)




[Back to top](https://dev.sprinklr.com/cfm-workflow-api)
