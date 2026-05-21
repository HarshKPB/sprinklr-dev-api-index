---
title: "Comment Webhooks"
slug: comment-webhooks
url: https://dev.sprinklr.com/comment-webhooks
---

# Comment Webhooks

# Comment Webhooks

	**Comment Webhook Subscriptions:**
 Comment Created and Comment Updated

Whenever an action is performed regarding creation or updation of comment either via Sprinklr UI or API, the webhook notification are triggered with the details that are described in the following documents:


- [Comment.Created Webhook](https://dev.sprinklr.com/comment-webhooks#commentCreate)

- [Comment.Updated Webhook](https://dev.sprinklr.com/comment-webhooks#commentUpdate)

### Comment.Created Webhook




  Copy Code



	{
  "id": "5f61e87c0431b12a3f64597f",
  "type": "comment.created",
  "payload": {
    "id": "5f61e87c0431b12a3f64597e",
    "text": "lax_inbound_verizon",
    "commentingUser": -100,
    "createdTime": 1600252028737,
    "modifiedTime": 1600252028737,
    "entityType": "MESSAGE",
    "entityId": "PERSISTENT_SEARCH_214437_1600251542000_YOUTUBE_45_LJwodn5mJ58"
  },
  "eventTime": 1600252028745,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf57e0a2"
  }
}





### Comment.Updated Webhook




  Copy Code



{
  "id": "5f61e87c0431b12a3f64597f",
  "type": "comment.updated",
  "payload": {
    "id": "5f61e87c0431b12a3f64597e",
    "text": "New Comment updated",
    "commentingUser": -100,
    "createdTime": 1600252028737,
    "modifiedTime": 1603274798396,
    "entityType": "MESSAGE",
    "entityId": "PERSISTENT_SEARCH_214437_1600251542000_YOUTUBE_45_LJwodn5mJ58"
  },
  "eventTime": 1603274798398,
  "subscriptionDetails": {
    "subscriptionId": "5efd98dbaaa2ac56bf57e0a2"
  }
}





### Response definitions









































| Parameters | Description | Type |
| --- | --- | --- |
| id | Unique Id of the comment. | String |
| text | Text of the comment. | String |
| createdTime | Time when the comment was made. | Epoch |
| modifiedTime | Time when the comment was modified. | Epoch |
| entityType | Entity type on which the asset was created. | String |
| entityId | Id of the entity on which the comment was created. | String |

[](https://dev.sprinklr.com/comment-webhooks)

[Back to top](https://dev.sprinklr.com/reporting-blueprints)
