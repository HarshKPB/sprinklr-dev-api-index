---
title: "Webhook Types"
slug: webhook-types
url: https://dev.sprinklr.com/webhook-types
---

# Webhook Types

#
		 Webhook Types


You can fetch all the available webhook subscription types with this API call. In response, you will get all the webhook types in JSON format.


### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/webhook-subscriptions/webhook-types

## Header

The following set of HTTP header fields provide required information about the request or response, or about the object sent in the message body. Both request headers and response headers can be controlled using these endpoints.











			``




			``




			``




| Key | Value | Description |
| --- | --- | --- |
| Content-Type | application/json | Request format should be JSON as the endpoint expects a JSON body. |
| Authorization | Bearer {{token}} | Credential used by an application to access an API. |
| Key | api-key | The API key acts as both a unique identifier and a secret token for authentication to a set of access rights. |

## Example - Request




  Copy Code



	curl -X GET \
https://api2.sprinklr.com/{env}/api/v2/webhook-subscriptions/webhook-types \
-H 'Authorization: {Enter your Access Token}' \
-H 'Key: {Enter your API KEY}' \
-H 'accept: application/json'





## Example - Response




  Copy Code



{
    "data": [
        {
            "type": "AUDIENCE_ACTIVITY_CREATED",
            "label": "Audience Activity",
            "category": "Activity"
        },
        {
            "type": "CAMPAIGN_CREATED",
            "label": "Campaign Created",
            "category": "Campaign"
        },
        {
            "type": "CAMPAIGN_DELETED",
            "label": "Campaign Deleted",
            "category": "Campaign"
        },
        {
            "type": "CAMPAIGN_UPDATED",
            "label": "Campaign Updated",
            "category": "Campaign"
        },
        {
            "type": "CASE_CREATED",
            "label": "Case Created",
            "category": "Case"
        },
        {
            "type": "CASE_DELETED",
            "label": "Case Deleted",
            "category": "Case"
        },
        {
            "type": "CASE_UPDATED",
            "label": "Case Updated",
            "category": "Case"
        },
        {
            "type": "MESSAGE_ASSOCIATION_CHANGE",
            "label": "Message Association Change",
            "category": "Case"
        },
        {
            "type": "COMMENT_CREATED",
            "label": "Comment Created",
            "category": "Comment"
        },
        {
            "type": "COMMENT_UPDATED",
            "label": "Comment Updated",
            "category": "Comment"
        },
        {
            "type": "DRAFT_CREATED",
            "label": "Draft Created",
            "category": "Draft"
        },
        {
            "type": "DRAFT_SCHEDULED",
            "label": "Draft Scheduled",
            "category": "Draft"
        },
        {
            "type": "DRAFT_UPDATED",
            "label": "Draft Updated",
            "category": "Draft"
        },
        {
            "type": "MESSAGE_DELETED",
            "label": "Message Deleted",
            "category": "Message"
        },
        {
            "type": "MESSAGE_DELIVERED",
            "label": "Message Delivered",
            "category": "Message"
        },
        {
            "type": "MESSAGE_PUBLISH_FAILED",
            "label": "Message Publish Failed",
            "category": "Message"
        },
        {
            "type": "MESSAGE_PUBLISHED",
            "label": "Message Published",
            "category": "Message"
        },
        {
            "type": "MESSAGE_READ",
            "label": "Message Read",
            "category": "Message"
        },
        {
            "type": "MESSAGE_CREATED",
            "label": "Message Received",
            "category": "Message"
        },
        {
            "type": "MESSAGE_UPDATED",
            "label": "Message Updated",
            "category": "Message"
        },
        {
            "type": "PROFILE_CREATED",
            "label": "Profile Created",
            "category": "Profile"
        },
        {
            "type": "PROFILE_DELETED",
            "label": "Profile Deleted",
            "category": "Profile"
        },
        {
            "type": "PROFILE_UPDATED",
            "label": "Profile Updated",
            "category": "Profile"
        },
        {
            "type": "PROFILES_MERGED",
            "label": "Profiles Merged",
            "category": "Profile"
        },
        {
            "type": "DIGITAL_ASSET_CREATED",
            "label": "Asset Created",
            "category": "Sam"
        },
        {
            "type": "DIGITAL_ASSET_DELETED",
            "label": "Asset Deleted",
            "category": "Sam"
        },
        {
            "type": "DIGITAL_ASSET_UPDATED",
            "label": "Asset Updated",
            "category": "Sam"
        },
        {
            "type": "TASK_CREATE",
            "label": "Task Create",
            "category": "Task"
        },
        {
            "type": "TASK_DELETE",
            "label": "Task Delete",
            "category": "Task"
        },
        {
            "type": "TASK_UPDATE",
            "label": "Task Update",
            "category": "Task"
        },
        {
            "type": "WORKFLOW_UPDATED",
            "label": "Workflow Updated",
            "category": "Workflow"
        }
    ],
    "errors": []
}





**Note: **From here you can check the type of webhook and can use the same type in the request body of Create Webhook to create a subscription of that type.

	For example, ff you want to create a webhook for task delete than use "TASK_DELETE" in subscriptions ("subscriptions":[ "TASK_DELETE" ] ) under the request body of Create Webhook API call.

[](https://dev.sprinklr.com/webhook-types)

[Back to top](https://dev.sprinklr.com/webhook-types)
