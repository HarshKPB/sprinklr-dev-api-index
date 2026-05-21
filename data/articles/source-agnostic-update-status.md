---
title: "Source Agnostic - Update Status"
slug: source-agnostic-update-status
url: https://dev.sprinklr.com/source-agnostic-update-status
---

# Source Agnostic - Update Status

#
POST Source Agnostic - Update Status


This API allows you to update the status of a message that has already been imported in Sprinklr.



**Dev Notes: **Status updates apply only to existing brand messages and are limited to a single message per request.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/source-agnostic/`{accountId}`/updateStatus

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

## Query Parameter


















| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| accountId | Required | Refers to the unique identifier for the Source Agnostic account. | String |

**Steps to Extract Account Id from UI: **


- In the Sprinklr UI, click the **New Page** icon and search for All Settings.
- Navigate to **All Settings**.
- In **Manage Workspace**, click **Accounts**.
- In the **Accounts** page, click the three dots icon placed alongside the respective account name.
- Click **Details** option from the drop-down menu.
- In the **Details** window, click the Copy URL icon on the top-right corner.
- Use any encoder-decoder tool and paste the copied URL.
- The account id will be the part of the decoded URL. For example, if you get `/ACCOUNT/100426226/OVERVIEW` in the decoded URL, your account id is 100426226.

## Request Parameters





















****







- ``
- ``
- ``
- ``
****










| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| conversationId | Required | The unique identifier that the brand generates each time a new conversation (composed of several messages) is created within Sprinklr. When sending messages within the same conversation within Sprinklr, the conversationId should remain the same. If a new conversationId will be passed, a new case will be created. | String |
| messageId | Required | The unique identifier of the message whose status you want to update.  	 Dev Notes: messageId= sourceType + “_”+ sourceId + “_” + ChannelCreatedTime + “_” + “ChannelType” + “_” + ” MessageType“ +”_” + channelMessageId. | String |
| errorMessage | Optional | A brief description explaining the reason for the message failure. | String |


**Dev Notes:** To find the message ID in the Sprinklr UI:



- In Care Console, open the relevant case.

- Double-click the message whose status you want to update.

- Click on **Properties**.

- In the **ID** field, the message ID is the value following the prefix `PID_`.



## Example - Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/source-agnostic/66122694/updateStatus?conversationId=test_test&messageId=68944a63104d823fdeeb43ab&status=read' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'key: {Enter Your API Key}'


 

## Example - Response



{"data":true,"errors":[]}



 

### Response Parameters





















| Parameter | Description | Type |
| --- | --- | --- |
| data | True indicates that the status of the message has been updated successfully | boolean |
| errors | List of errors, if any | array |

	[](https://dev.sprinklr.com/source-agnostic-update-status) 

 

 
[Back to top](https://dev.sprinklr.com/source-agnostic-update-status)
