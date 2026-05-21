---
title: "Jul - Sep, 2023"
slug: jul-sep-2023
url: https://dev.sprinklr.com/jul-sep-2023
---

# Jul - Sep, 2023

# Jul - Sep, 2023

**Developer Note:**
We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.
Please note that the API base endpoint has changed from `api2` to `api3`.
For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## ****Publishing Post API -  Sep 25th, 2023

Publishing Post API now supports publishing post for LinkedIn Poll, Updating Facebook Album, creating Twitter Thread, and adding Instagram Story.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/post



## ****Schedule Draft API -  Sep 25th, 2023

Schedule Draft API now supports scheduling post for LinkedIn Poll, Updating Facebook Album, creating Twitter Thread, and adding Instagram Story.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/draft/schedule



## ****Create Draft API -  Sep 25th, 2023

Create Draft API now supports creating LinkedIn Poll, Updating Facebook Album, creating Twitter Thread, and adding Instagram Story.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/draft



## ****Email Create API -  Sep 15th, 2023

Email Create API now supports adding HEIC,HEIF,TIFF, and JFIF format images as attachments.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/email/create



## ****Search Comment API -  Sep 8th, 2023

This API now allows searching comments on case, message, and profile level using filters and sorting conditions.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/search/COMMENT



## ****Merge Cases -  Sep 7th, 2023

This API allows merging one or more cases where one case is the parent case and the merged cases are the child cases.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/case/merge-cases



## ****Remove Contact from Suppression List -  Sep 5th, 2023

This API allows removing a contact from an existing suppression list.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/suppressionList/removeContact/{suppressionListId}/{contactValue}



## ****Add Bulk Contacts to Suppression List -  Sep 5th, 2023

This API allows adding multiple contacts to a suppression list so that they aren't contacted again.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/suppressionList/addContacts



## ****Add Contacts to Suppression List -  Sep 4th, 2023

This API allows adding contacts to a suppression list so that they aren't contacted again.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/suppressionList/addContact



## ****Update Outbound Post Custom Properties -  Sep 1st, 2023

This API allows updating partner and client custom properties for an outbound post for the given channel and account Id.

**API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/publishing/outbound/workflow-properties/{accountId}/{channelId}



## ****Search User -  July 20th, 2023

Using this API, you can search user by passing filters and sorting details

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/scim/Users

 [](https://dev.sprinklr.com/jul-sep-2023)

[Back to top](https://dev.sprinklr.com/jul-sep-2023)
