---
title: "GDPR - Privacy"
slug: v1-gdpr-apis
url: https://dev.sprinklr.com/v1-gdpr-apis
---

# GDPR - Privacy

#
GDPR (Privacy)

The EU General Data Protection Regulation (GDPR) was designed to protect and empower all EU citizens data privacy and to reshape the way organizations across the region approach data privacy. With this, end user is granted rights around how their personal data is used, collected, processed and protected. This requires corporates doing business in EU to have processes to enable end users for such rights.  Sprinklr being a data processor for its clients, is making sure to empower all its clients to comply with GDPR laws in both automated and manual ways. This document covers the API approach of Sprinklr to help clients automate the GDPR requests on their end.

The following API endpoints need to be called in the given order to perform the intended actions on the profile:

- **[Create View Request](https://dev.sprinklr.com/v1-gdpr-create-view-request)**: Using this API, you can submit a request to view the profile data

- **[Fetch Request Status](https://dev.sprinklr.com/v1-gdpr-fetch-request-status)**: Using this API, you can fetch the status of the view request. It is recommended to proceed with “Fetch Profile Data” API only after the fetch request Status API returns “SUCCESS” response

- **[Fetch Profile Data](https://dev.sprinklr.com/v1-gdpr-fetch-profile-data)**: Using this API, you can fetch the profile data associated with the user profile passed in the view request API payload

- **[Create Edit Request](https://dev.sprinklr.com/v1-gdpr-create-edit-request)**: Using this API, you can submit a request to edit the profile

- **[Create Delete Request](https://dev.sprinklr.com/v1-gdpr-create-delete-request)**: Using this API, you can submit the request to delete the profile. This API will delete the profile and the cases associated with the profile. The delete type determines what is deleted using this API


**Dev Note: ** If you want to delete the audience profile, you will need to call all the API in the order given above. If you skip calling any of the above APIs, the profile won't be deleted

## POST `/gdpr/view`

Returns a status id associated with the given request
**Request Parameters**
















































| Param Name | Description | Param Type | Example |
| --- | --- | --- | --- |
| profileKey | Profile Identifier | ProfileKey | See below |
| endTime | Activity till that | Long(Optional) | 1520580721 |
| startTime | Activity from | Long(Optional) | 1510580721 |
| callBackUrl | Success callback | String(Optional) | https://callback.com/qw2345 |
| referenceId | Unique identifier from client side | String | qw2345 |
| reason | Request Reason from client side | String(Optional) | Request raised from end user through Microsoft Privacy Console |

### ProfileKey





















[here](https://dev.sprinklr.com/channels-v1)



| Param Name | Description | Field Type | Example Value |
| --- | --- | --- | --- |
| id | UserId | String | taylorswift13 |
| type | Id Type | Enum | TWITTER 			Complete list |

## POST `/gdpr/:statusid`

Returns a status id associated with the given request
**Response Parameters**













			******




| Param Name | Description | Field Type | Example Value |
| --- | --- | --- | --- |
| status | Status | Enum:NEW,IN_PROCESS, SUCCESS,FAILED | SUCCESS |

## GET `/gdpr/view/:statusid` (Without query params)

Returns a status id associated with the given request
**Response Parameters**


















| Param Name | Description | Field Type | Example Value |
| --- | --- | --- | --- |
| profileActivity | Profile Activity | ProfileActivity | See below |

### ProfileKey




















			[Check here](https://dev.sprinklr.com/profile-v1)















| Param Name | Description | Field Type | Example Value |
| --- | --- | --- | --- |
| metaData | The metadata for request | Object(MetaData) | See below |
| profile | The associated audience profile in sprinklr | Object(AudienceProfile) |  |
| activities | List of activities | List<Activity> | See below |
| cursor | Optional cursor associated with profile activity | String | qwerty |

### MetaData
























| Param Name | Description | Field Type | Example Value |
| --- | --- | --- | --- |
| total | Total profile activities | Integer | 159 |
| countByActivityType | Activities count by activity type | Map<String,Integer> | {“total” : 159,“countByActivityType”: {“SOCIAL” : 49, “AUDIENCE”: 45, “LISTENING”:65}} |

### Activity




















			**









| Param Name | Description | Field Type | Example Value |
| --- | --- | --- | --- |
| id | Id for the event | String | qwqe345gh |
| activityType | Activity Type | String | SOCIAL |
| time | Activity Time | Long | 234567 |

Depending upon the activity type we will have different activity classes.
Activity with activityType as *Social Activity* will comprise of fields from [Inbound Message](https://dev.sprinklr.com/inbound-messages-v1) in addition to three primary attributes mentioned above.

## GET `/gdpr/view/:statusid` (With query params)

Returns a status id associated with the given request
**Response Parameters**

### Request Query Parameters


















| Param Name | Description | Field Type | Example Value |
| --- | --- | --- | --- |
| cursor | Cursor for pagination | String | 58e72d9d9e5978a1ff128417 |

### Response

Response to this call will be an object of ProfileActivity.

## POST `/gdpr/edit`

Returns a status id associated with the given request.

### Request Query Parameters










































| Param Name | Description | Param Type | Example |
| --- | --- | --- | --- |
| requestId | The view request id for the profile to be updated | String | 5afd31ba60b2c6d0dd7f3cb2 |
| updateRequest | Update Request | Object | See below |
| callBackUrl | Success callback | String(Optional) | https://callback.com/qw2345 |
| referenceId | Unique identifier from client side. | String(Optional) | qw2345 |
| reason | Reason for submitting the request. | String(Optional) | “User requested through Privacy Console” |

Currently, we support edit of only the following fields:


- *contactInfo*

- *manualContactInfo*

- *demographics*

- *works*

- *skills*

- *education**s*

- *profileWorkflowProperties*

## POST `/gdpr/delete`

Returns a status id associated with the given request

### Request Query Parameters


































































| Param Name | Description | Param Type | Example |
| --- | --- | --- | --- |
| requestId | The id for the view request used to generate activitiyIds | String | 48e72d9d9e5978a1ff128427 |
| endTime | Activity till that | UTC time in millis | 1520580721 |
| startTime | Activity starting from | UTC time in millis | 1510580721 |
| activityType | activityType | String(Optional) | SOCIAL |
| activityId | activityId | String(Optional) | “qwqe345gh” |
| deleteType | Type of delete : selective vs complete. When the deleteType is EVERYTHING, other filter fields (activityId, time, etc) are ignored. | Enum: CUSTOM, EVERYTHING | CUSTOM |
| callBackUrl | Success callback | String(Optional) | https://callback.com/qw2345 |
| referenceId | Unique identifier from client side. | String(Optional) | qw2345 |
| reason | Include deleted results for your request. Defaults to false. | String(Optional) | “User request through Privacy Console” |
