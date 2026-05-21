---
title: "Jul - Sep, 2024"
slug: jul-sep-2024
url: https://dev.sprinklr.com/jul-sep-2024
---

# Jul - Sep, 2024

#
Jul - Sep, 2024

**Developer Note:**
We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.
Please note that the API base endpoint has changed from `api2` to `api3`.
For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## ****Create Email API - 2nd Sept, 2024

Introducing Email API to ingest data within Sprinklr as both fan and brand message. You can create email with attachments from URL as well as local device.

* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/email/create?aId={emailId}

## ****Read Dashboard List API - 2nd Sept, 2024

Introducing Read Dashboard List API to retrieve a list of Sprinklr reporting and listening dashboards along with detailed metadata.

* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/entity/{entityType}/filter

## ****Macro API - 2nd Sept, 2024

Introducing Macro API to automate the application of macros on various Entities, including Cases, Outbound Messages, User-Generated Content, Profiles, Campaigns, and more.

* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/macro/apply

## ****Update Agent Status API - 2nd Sept, 2024

Introducing Update Agent Status API to update an agent's availability status, which will be stored in the `spr_user_availability_status` custom field.

* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/user/update-user-status

## ****Read Draft API - 2nd Sept, 2024

Introducing Read Draft API to retrieve a message draft by using message id.

* ***API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/publishing/drafts?messageids={message_id}/filter

## ****Fetch Metrics and Dimensions API - 2nd Sept, 2024

Introducing Fetch Metrics and Dimensions API to retrieve metadata for specific reports within the specified platform.

* ***API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/reports/metadata/PLATFORM?reportNames={reportName}

## ****Fetch Custom Metrics API - 2nd Sept, 2024

Introducing Fetch Custom Metrics API to retrieve custom metrics associated with the given report name.

* ***API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/reports/customMetric/PLATFORM?reportNames={reportName}

## ****Asset Import Async API - 2nd Sept, 2024

Introducing Asset Import Async API to import an asset using URL and check the import status by using the Task Id.

* ***API Endpoint for Asset Import**

POST https://api2.sprinklr.com/{env}/api/v2/sam/importUrl/async?importType={type}&url={valid_url_address}&uploadTrackerId={tracker_id}

* ***API Endpoint for Checking the Status via Task Id**

GET https://api2.sprinklr.com/{env}/api/v2/sam/task/status/{taskId}

## ****Update Message Properties API - 2nd Sept, 2024

Introducing Update Message Properties API to update the custom properties of a message in the workflow.

* ***API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/message/workflow

## ****Update Profile Lists -  7th Aug, 2024

Introducing Profile List Update endpoint that allows you to update client and partner profile lists across a universal profile categorized under audience profiles module.

* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/profile/workflow/profile-list



## ****Search Custom Fields -  30th July, 2024

Search by Entity API now supports CUSTOM_FIELD entity. You can search for custom fields based on the given filter types and corresponding values.

* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/search/CUSTOM_FIELD



## ****Fetch CRM User Mapping -  20th July, 2024

* ***API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/crm-user-mapping/{InstalledAppId}



## ****Fetch and Download CRM User Mapping -  20th July, 2024

* ***API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/crm-user-mapping/{InstalledAppId}/export

## ****Fetch CRM User Mapping Using CRM User Ids -  20th July, 2024

* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/crm-user-mapping/{installedAppId}/by-crm-users



## ****Fetch CRM User Mapping Using SPR User Ids -  20th July, 2024

* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/crm-user-mapping/{installedAppId}/by-spr-users



## ****Add CRM User Mapping -  20th July, 2024

* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/crm-user-mapping/{installedAppId}

## ****Add CRM User Mapping -  20th July, 2024

* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/crm-user-mapping/{installedAppId}

## ****Create/Update CRM User Mappings -  20th July, 2024

* ***API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/crm-user-mapping/{installedAppId}

## ****Create/Update User Mapping - Bulk -  20th July, 2024

* ***API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/crm-user-mapping/{installedAppId}/bulk-upsert



## ****Create/Update User Mapping - From File -  20th July, 2024

* ***API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/crm-user-mapping/{installedAppId}/import

## ****Delete CRM User Mapping -  20th July, 2024

* ***API Endpoint**

DELETE https://api2.sprinklr.com/{env}/api/v2/crm-user-mapping/{installedAppId}

## ****Trigger Customer Journeys in Bulk -  15th July, 2024

* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/marketing-journey/bulk-trigger



## ****Search Entity -  15th July, 2024

Search by entity API (SOCIAL ASSETS) now supported three additional key filters, i.e., templateType, channels, and name.
* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/search/SOCIAL_ASSET



## ****Search Customer Journeys -  15th July, 2024

Using this API, you can search for existing customer journeys based on the given filters.

* ***API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/marketing-journey/search

## ****Fetch All Work Queues -  14th July, 2024

Using this API, you can fetch the details for all the work queues existing within the unified routing module.

* ***API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/work-queue/getAllWorkQueues



## ****Read Post by Post Ids (v1 to v2 Transition)  -  14th July, 2024

Using this API, you can fetch the details of the outbound posts such as created time, published time, status, tagged custom properties, campaigns, etc.

* ***API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/publishing/posts



## ****Fetch Engagement Dashboard by Name (v1 to v2 Transition)  -  14th July, 2024

Using this API, you can fetch the engagement dashboard details using the given name.

* ***API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/monitoring/dashboard/find/name/{dashbaordName}



## ****Fetch All Engagement Dashboards(v1 to v2 Transition)  -  14th July, 2024

Using this API, you can fetch all the existing engagement dashboards available in the partner environment/workspace.

* ***API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/monitoring/dashboard

[](https://dev.sprinklr.com/jul-sep-2024)

[Back to top](https://dev.sprinklr.com/jul-sep-2024)
