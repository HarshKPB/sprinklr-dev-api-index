---
title: "Message Properties Update v1"
slug: message-properties-update-v1
url: https://dev.sprinklr.com/message-properties-update-v1
---

# Message Properties Update v1

#  POST Message Properties Update v1

You can use this API to update the message workflow properties.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/message/workflow/properties/update

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

### Request Body Parameter












			[Custom Property Action](https://dev.sprinklr.com/message-properties-update-v1#init)



























































| Parameter | Sub Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
|  |  | Required | Object containing custom properties details. | Object |
|  | "fieldName": ["value"] | Required | The custom properties containing fieldName and value | String |
| universalMessageWorkflowKey |  | Required | The universal message object containing message details. | Object |
|  | snType | Required | The social network type. e.g. TWITTER | String |
|  | msgType | Required | The socail message type like Post or Reply etc. | String |
|  | snMsgId | Required | The social network message Id. | String |
|  | sourceId | Required | The sourceId of the account. | String |
|  | sourceType | Required | The source type of the message. | String |
|  | snCreatedTime | Required | The message created time. | Epoch |

**Dev Notes: **Steps to extract custom field name from the UI:

- Click to add a new tab on platform's homepage
- Navigate to All Settings Options in the Platform Modules section
- Click on Custom Fields Icon under "Manage Workspace" section
- Click on the three dots placed alongside the custom field you want the fetch the name for
- Select "Copy Field name" from the drop down menu
- Use this field name in the API request payload

## Custom Properties Actions and Description




























| Action | Description |
| --- | --- |
| selectivePartnerCustomProperties | Replaces the values with the ones present in the API request.For instance, “a” and “b” were existing values for the custom property and only “c” and “d” are added in new API request, in this case the new value would be “c” and “d” |
| partnerCustomPropertiesAdded | Adds a new value to the list of existing values.For instance, “a” and “b” were existing values for the custom property and only “c” is added in the new API request, in this case the new value will be “a”, “b” and “c”.That is, it will retain the existing values and append the new one to the already existing list |
| partnerCustomPropertiesRemoved | To remove custom properties |

## Example




 Copy Code



	curl -X POST \
  https://api3.sprinklr.com/{env}/api/v1/message/workflow/properties/update \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
-d'{
	"partnerCustomPropertiesRemoved": {
		"spr_uc_tag": [
			"Tag A"]
	},
	"partnerCustomPropertiesAdded": {
		"spr_uc_tag": [
			"Tag B"
		]
	},
	"selectivePartnerCustomProperties": {
		"5a81c6ebe4b0142c7eee5696": [
			"yes"
		]
	},
	"universalMessageWorkflowKey": [
		{
	    "snType": "TWITTER",
        "msgType": "7",
        "snMsgId": "1307953838494593024",
        "sourceId": "77338",
        "sourceType": "ACCOUNT",
        "snCreatedTime": 1600675470361
		}
	]
}'



## Example - Response



true

**Dev Notes: ****true** in the response implies that the message properties have been successfully updated.

[](https://dev.sprinklr.com/message-properties-update-v1) 

 

 
[Back to top](https://dev.sprinklr.com/message-properties-update-v1)
