---
title: "Trigger Customer Journey"
slug: trigger-customer-journey
url: https://dev.sprinklr.com/trigger-customer-journey
---

# Trigger Customer Journey

# POST Trigger Customer Journey

Sprinklr allows running automated customer journeys that are based on external events, such as a customer filling up a form, completing an online purchase, abandoning cart, etc. This API helps create a new profile and [triggers the customer journey](https://www.sprinklr.com/help/categories/journey-trigger-settings/648703c2560f6d375397656a) based on given information. If the profile already exists, the API will associate the journey with it.

## Updated API Endpoint

https://api3.sprinklr.com/{env}/api/v2/marketing-journey/triggerJourney

## Old API Endpoint

https://api3.sprinklr.com/{env}/api/v2/marketing-journey/triggerWithNewProfile

**Dev Notes: **The old endpoint https://api3.sprinklr.com/{{env}}/api/v2/marketing-journey/triggerWithNewProfile will continue to be supported until it is officially deprecated.

We recommend using the new endpoint for all future integrations to ensure compatibility with the latest features and improvements.

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











[journey](https://help.sprinklr.com/articles/journey-facilitator/triggersegment-based-audience-journey/613767265f2e7c0c9ed36ef4#To_Select_Journey_Audience)

[create/update universal profile](https://dev.sprinklr.com/create-update-universal-profile)

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| journeyId | Required | The unique identifier for the  that needs to be triggered | String |
| contextParams | Optional | Key and value pair that provides additional information about the customer and their journey | Object |
| unifiedProfile | Required | Refer to the  API documentation for understanding profile creation object parameters The tables below describe the request parameters for creating unified profile | Object |

### unifiedProfile Parameters Description Table






















































































































































































































































































| Parameter | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| id |  | Optional | Unique identifier of the unified profile. | String |
| contact |  |  | Contact information of the profile. |  |
|  | firstName | Optional | First name of the profile. | String |
|  | maidenName | Optional | Maiden name of the profile. | String |
|  | lastName | Optional | Last Name of the profile. | String |
|  | fullName | Optional | Full name of the profile. | String |
|  | email | Optional | Email id of the profile. | String |
|  | phoneNo | Optional | Phone number of the profile. | String |
|  | address | Optional | Address of the profile.Schema for Address Table given below. | String |
|  | website | Optional | List of websites for the profile. | String |
| demographics |  |  | Demographic Information of the client. |  |
|  | age | Optional | Age of the profile. | Integer |
|  | location | Optional | Location of the profile. | String |
|  | gender | Optional | Gender of the profile. | String |
|  | language | Optional | Language of the profile. | String |
| profiles |  |  | List of social identities linked to the profile. |  |
|  | name | Required | Name of the person. | String |
|  | channelType | Required | Channel type of the profile. e.g. facebook. | String |
|  | channelId | Required | Refers to the unique identifier for the customer profile. If the channelId is unique, a new profile will be created and a journey will be associated with it, else the journey will be associated with the existing profile. | String |
|  | permalink | Optional | Link of the profile on social channel. | String |
|  | avatarUrl | Optional | Profile image link. | String |
|  | bio | Optional | Detailed description about the user. | String |
|  | followers | Optional | Followers count of the user. | Integer |
|  | username | Optional | Unique identifier of the user. | String |
|  | verified | Optional | True if the user is verified by the channel. 					default: false | Boolean |
|  | unSubscribed | Optional | True if the user is subscribed for email and other activities.default: false | Boolean |
|  | deleted | Optional | True if profile is deleted natively.default: false | Boolean |
|  | snCreatedTime | Optional | Social Channel created time. | Integer |
|  | snModifiedTime | Optional | Social Channel modified time. | Integer |
|  | accountSpecificInfos | Optional | Account Specific Info like accountId, externalId, etc.Account Specific Info Table given below. |  |
| profileWorkflow |  |  |  |  |
|  | profileLists | Optional | Partner profile lists on the profile, if any. | Integer |
|  | customProperties | Optional | Partner custom properties on the profile, if any.  Profile Level Custom Fields are not supported currently. | String |
|  | profileSpaceWorkflows | Optional | List of client level workflows on the profile, if any.ProfileSpaceWorkflow Table given below. |  |
| createdTime |  | Optional | Created time of the profile in sprinklr. | Integer |
| modifiedTime |  | Optional | Last modified time of the profile in sprinklr. | Integer |

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



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/marketing-journey/triggerJourney' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
   "journeyId": "62f37039a638d31f03122c9e",
   "contextParams": {
       "lang":"ar",
       "user_phone_number": "971501800350",
       "guid":"e18d7683-e699-421b-b7f9-62c1dacc00af",
       "country":"Jordan",
       "countryCode": "SA"
                 },
   "unifiedProfile": {
       "contact": {
           "firstName": "Von"
       },
       "profiles": [
           {
               "channelType": "WHATSAPP_BUSINESS",
               "channelId": "91675834897",
               "name": "Von Test"
           }
       ],
       "createdTime": 1655650673
   }
}'






### Example - Response





{
	"data":
	{
	"status": "SUCCESS",
	"message": "Triggered Successfully",
	"trackingId": "673b4d5120594a5352f27b40_668692ffc118f93091bbc9c3_673b52d0a596900be7001f97"
	},
	"errors": []
	}







**Dev Notes: **A "SUCCESS" status only indicates that the API Endpoint was successful in trigerring the Journey Facilitator for the Profile, NOT the successful completion of execution of the Journey Facilitator Workflow.

	[](https://dev.sprinklr.com/trigger-customer-journey)




[Back to top](https://dev.sprinklr.com/trigger-customer-journey)
