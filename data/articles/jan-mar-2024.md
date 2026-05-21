---
title: "Jan - Mar, 2024"
slug: jan-mar-2024
url: https://dev.sprinklr.com/jan-mar-2024
---

# Jan - Mar, 2024

#
Jan - Mar, 2024

**Developer Note:**
We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.
Please note that the API base endpoint has changed from `api2` to `api3`.
For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## ****Update User/Partial Update User-  24th March, 2024

Using this API, you can now remove a user from the assigned user group.

**API Endpoint**

PUT  https://api2.sprinklr.com/{env}/api/v2/scim/{userId}

PUT https://api2.sprinklr.com/{env}/api/v2/scim/update/{userId}



## ****Case Management Stream -  24th March, 2024

	Using this API, you can now fetch case details from case management stream column.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/stream/{streamId}/feed



## ****Add Multiple Comment Attachments -  24th February, 2024

You can now add comment with multiple attachments on a given entity.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/comment/{entityType}/{entityId}/multiple-attachment



## ****Mark Message as Read -  24th February, 2024

You can now mark incoming WhatsApp messages as read using this API.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/message/notify-read



## ****Create/Update Bulk Users -  5th February, 2024

You can now create/update users in bulk using both sync and async method.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/scim/bulk-upsert



## ****Delete Case Using Case Number -  2nd February, 2024

You can now delete cases by passing the list of case numbers in the request body.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/case/case-numbers/delete



## ****Update Message Queue/Sentiment -  22nd January, 2024

You can now update the sentiment and partner queue details for the given message.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v1/message/workflow/sentiment-queue/update



## ****Update Keyword List API -  17th Jan, 2024

Update keyword list API now supports partially updating the keyword list, that is, new keywords passed in the payload will be added while the pre-existing keywords will be retained.

**API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/keyword-list/{Id}

[](https://dev.sprinklr.com/jan-mar-2024)

[Back to top](https://dev.sprinklr.com/jan-mar-2024)
