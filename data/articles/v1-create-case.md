---
title: "v1 Create Case"
slug: v1-create-case
url: https://dev.sprinklr.com/v1-create-case
---

# v1 Create Case

#
POST v1 Create Case

A Sprinklr Case can be created with this API call which allows you to track customer interactions as a bundled group of messages. Once a Case has been created, subsequent responses can be kept together, organized as a single Case, which can help streamline workflows, keep messages organized, and simplify reporting on customer interactions.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/case

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

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| fromSnUser | Required | A map containing the details of the social channel user, such as the user's Universal Id, name, handle, etc. | Object |
| messageKey | Required | The Universal Message Key Object, which contains details for the universal message associated with the case. Refer to the table below for object details. | Object |
| brandPost | Optional | Denotes whether or not the post is a brand post. | Boolean |
| conversationId | Optional | The Conversation Id of the social message associated with the case. | String |
| subject | Optional | The subject of the case. | String |
| description | Optional | The description of the case. | Long |
| mediaList | Optional | A list of the attached media components. | List < Media > |
| customProperties | Optional | Custom properties associated with the case. | Map < String>, List < String > |
| assignedTo | Optional | The assigned user for the case. | Long |
| dueDate | Optional | The due date for the case. | Long |
| notifyUsers | Optional | A list of users to notify. | List < Long > |
| comment | Optional | Comments associated with the case. | String |
| queues | Optional | A list of queues to which to send the case. Queues are used to  store cases based on like conditions that can be configured and  automated in the Rule Engine. You can think of queues as invisible folders that house and organise your cases. | List < Long > |
| archived | Optional | The archival state of the case upon creation. | Boolean |
| dissociateCaseIds | Optional | A list of case Ids from which to dissociate the case. When you associate a case, they bundle together, providing your team members with all the information they need on a customer experience and vice-versa. | List < Long > |
| generateNotification | Optional | Denotes whether or not to generate notifications for the case. Default = true | Boolean |

### messageKey Object Description Table

****``````

[channel type](https://dev.sprinklr.com/channels-v1)

[message type code](https://dev.sprinklr.com/message-v1)

****``````

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| universalMessageId | Optional | Unique universal message id.Syntax: snType + msgType + SnMsgId | String |
| snType | Required | Refers to the  where the message exists | String |
| msgType | Required | Refers to the | Long |
| snMsgId | Required | Unique message identifier received from the channel | String |
| sourceId | Required | The sourceId/accountId existing in Sprinklr on which fan replied or from which the brand | String |
| sourceType | Required | Refers to the source type of the message.Supported values: ACCOUNT, PERSISTENT_SEARCH, LISTENING | String |
| snCreatedTimeYearMonth | Optional | Message creation year and month in native | Long |
| snCreatedTime | Optional | Message created time in native | Epoch |

### Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
		curl -X POST \
  https://api3.sprinklr.com/{env}/api/v1/case \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '
{
    "fromSnUser": {
        "n": "Alex Rudd",
        "sN": "AlexRudd5",
        "uI": "1014969314003177472"
    },
    "messageKey": {
        "universalMessageId": "TWITTER_4_1100424712713252865",
        "snType": "TWITTER",
        "msgType": 4,
        "snMsgId": "1100424712713252865",
        "sourceId": 104379,
        "sourceType": "ACCOUNT",
        "snCreatedTimeYearMonth": "2019_02",
        "snCreatedTime": 1551204602111
    },
    "subject": "Case creation via API",
    "description": "Testing the case api endpoint to create a case.",
    "comment": "Comments go here",
    "archived": false
}'
			 

     
     
   

### Example - Response

 
 
     
 
505920
 

     
     
   
 

### Response Definition

| Parameter | Description | Data Type |
| --- | --- | --- |
| {Id} | The {Id} is associated with the case you have created via API call or in the UI. | String |

		[](https://dev.sprinklr.com/v1-create-case) 

 

 
[Back to top](https://dev.sprinklr.com/v1-create-case)
