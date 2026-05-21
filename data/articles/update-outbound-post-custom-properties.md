---
title: "Update Outbound Post Custom Properties"
slug: update-outbound-post-custom-properties
url: https://dev.sprinklr.com/update-outbound-post-custom-properties
---

# Update Outbound Post Custom Properties

#
PUT Update Outbound Post Custom Properties

This API allows updating partner and client custom properties for an outbound post for the given channel and account Id. You can also use this API to update the inbound copy and comments of the corresponding outbound post by using the optional query parameters.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/publishing/outbound/workflow-properties/`{accountId}`/`{channelId}`

### Headers

HTTP headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.










			``




			```




			``


[Authorize](https://dev.sprinklr.com/suthorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)


``
[ME API](https://dev.sprinklr.com/me-api)

| Key | Value | Description |
| --- | --- | --- |
| accept | application/json | Determines the acceptable response type from the server |
| Content-Type | application/json | Content-Type is representation header determines the type of data (media/resource) present in the request body. |
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the dev portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  article |
| workspace_id | workspaceId | This field is optional. If your authorization token is associated with multiple workspaces, you'll have to pass workspace_id in the headers for updating a draft. You can use  to check the workspace Id your token is primarily associated with. |

### Path Parameters








[Bootstrap API](https://dev.sprinklr.com/bootstrap-api-v1)

``

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| accountId | Required | Refers to the unique identifier for the account from where the post was published.You can extract the account Id from Sprinklr’s UI using the steps mentioned below.Alternatively, you can also use the  to fetch all the accounts and associated data. | Integer |
| channelId | Required | Refers to the unique identifier for the native channel post Id.channelId will be received from channel. This is stored within “statusID” parameter in Sprinklr | String |

**Steps to Extract Account Id from UI: **

- Click on the hamburger menu on the top left corner on Sprinklr platform's homepage
- Navigate to All Settings Options
- Click on Accounts Icon within "Manage Workspace" module
- Click on the three dots placed alongside the respective account name
- Click on "Details" option from the drop down menu
- Click on copy url icon on the top right corner from the window that appears
- Use any encoder-decoder tool and paste the copied URL
- The account id will be the part of the decoded URL, i.e., if you get `/ACCOUNT/100426226/OVERVIEW` in the decoded URL, your account id is 100426226.

### Query Parameters

``
``

``

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| updateRelatedInboundMessages | Optional | Indicates whether the API should also update related inbound messages that are connected to the outbound post. When set to true, the API updates the inbound copy of the outbound post (channel copy)and all inbound comments on that post.  When set to false only the outbound post is updated. | Boolean |
| inboundMessagePropertiesToUpdate | Optional | Specifies which custom properties should be applied to inbound messages when updateRelatedInboundMessages=true.This ID corresponds to a configured custom property within Sprinklr. | String |

## Understanding Different Custom Property Update Operations

| Update Type | Description |
| --- | --- |
| selectivePartnerCustomProperties | The partner custom properties that are added in the payload will be appended to the outbound post.Please note that it will reset the existing custom property if not added in the API request |
| partnerCustomPropertiesAdded | It will associate the new partner custom property to the outbound post |
| partnerCustomPropertiesRemoved | It will remove the partner custom properties that are added in the payload |

## Example 1: Update Outbound Post Custom Properties Only

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/publishing/outbound/workflow-properties/{accountId}/{channelId}' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "tags": [
        "test",
        "api12121"
    ],
    "selectivePartnerCustomProperties": {
        "_c_646c35d81098132552c6eaa3": [
            "645b6702c9bf716545609cfc"
        ]
    }
}'
 

     
     
   

## Example - Response

 
 
     
 
{
    "data": [
        "POST_600000023528578"
    ],
    "errors": []
}
 

     
     
   

## Example 2: Update Outbound and Inbound Post Custom Properties with Inbound Comments

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X PUT \'https://api3.sprinklr.com/{env}/api/v2/publishing/outbound/workflow-properties/66073052/3779997641183388850_62647274115?updateRelatedInboundMessages=true&inboundMessagePropertiesToUpdate=_c_6960fc9d53519d3ad3abea0d' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "tags": [
        "test",
        "api12121"
    ],
    "selectivePartnerCustomProperties": {
        "_c_6960fc9d53519d3ad3abea0d": [
            "Stanger"
        ]
    }
}'
 

     
     
   

## Example - Response

 
 
     
 
{
    "data": [
        "POST_537727193"
    ],
    "errors": []
}
 

     
     
   

**Dev Notes: **To validate the modified custom properties, you can call “[Read Post by Post Id](https://dev.sprinklr.com/read-post-by-post-id-v1)” API. You can configure Post Id received in the API response above (i.e., 600000023528578)  in the path parameter to fetch the updated client and partner custom properties.

## API Success and Error Responses









| API Status Code | Description |
| --- | --- |
| 200 OK | The custom properties have been successfully updated |
| 400 Bad Request | Account Id or channel Id is incorrect |

	[](https://dev.sprinklr.com/update-outbound-post-custom-properties) 

 

 
[Back to top](https://dev.sprinklr.com/update-outbound-post-custom-properties)
