---
title: "Create v3"
slug: create-v3
url: https://dev.sprinklr.com/create-v3
---

# Create v3

#
POST Create API

The Create v3 API allows you to create various entities within Sprinklr, including cases, comments, custom fields, messages, and more. This unified endpoint simplifies and streamlines the process of entity creation.

## API Endpoint

	https://`{env}`-api2-v3.sprinklr.com/v3/api/entities/create/CASE

## Headers

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

## Request Parameters

[Request Types](https://dev.sprinklr.com/create-v3#request-type)

	[Payload Format](https://dev.sprinklr.com/create-v3#payload-format)

| Parameter | Required/Optional | Description | Type | Possible Values |
| --- | --- | --- | --- | --- |
| requestType | Required | The type of entity you want to create. | String | CASE, PROFILE, CUSTOM_FIELD, SAM, PROFILE_CASE. For more details, see the  section. |
| payload | Required | Contains the details of the entity you want to create. | Object | For the payload format, see the  section for the respective entity. |

## Request Types


The following table lists the supported values for the `requestType` parameter:




























| Request Type | Description |
| --- | --- |
| CASE | Creates a case. |
| PROFILE_CASE | Creates a case associated with a specific profile. |
| PROFILE_CASE_WITH_MESSAGES | Creates a profile-linked case that includes related messages. |
| CAMPAIGN | Creates a new marketing or advertising campaign. |
| CUSTOM_FIELD | Creates a custom field. |
| PROFILE | Creates a new user or customer profile. |
| SAM | Creates a social media asset such as a post, image, or ad. |
| USER | Creates a new user account in the platform. |
| DRAFT_MESSAGE | Creates a draft message for review or later sending. |
| REPLY_DM | Replies to a direct message. |
| REPLY_MESSAGE | Replies to a public or thread message. |
| SCHEDULE_MESSAGE | Schedules a message to be posted at a specific time. |
| COMMENT | Creates a basic comment on a post or thread. |
| COMMENT_WITH_MULTIPLE_ATTACHMENTS | Posts a comment with multiple attachments. |
| TASK | Creates a task. |
| LISTENING_TOPIC | Creates a listening topic for monitoring social mentions or trends. |
| KEYWORD_GROUP | Creates a group of keywords for tracking or analytics purposes. |


## Payload Format


The value of the `payload` parameter varies depending on the request type. For example, the payload for CASE request type would be different from the payload for COMMENT.


For the description of each parameter, see the [Payload Parameters](https://dev.sprinklr.com/create-v3#payload-parameters) section. You can also refer to the [Examples](https://dev.sprinklr.com/create-v3#examples) section for request and response examples.

The following table lists the example payload for each request type:


























| Request Type | Payload |
| --- | --- |
| CASE | Copy Code      			      "payload": {         "subject": "API Case creation",         "description": "This case is created with API.012",         "firstMessageId": "ACCOUNT_600056911_1742986039000_FACEBOOK_470_600275313172150",         "priority": "high",         "summary": "Urgent Case",         "dueDate": 0,         "workflow": {             "customProperties": {                 "spr_uc_status": [                     "New"                 ],                 "spr_uc_priority": [                     "High"                 ],                 "spr_uc_type": [                     "Complaint"                 ]             }         },         "contact": {         "id": "TWITTER_1619985399673421826",         "name": "ABC"     }     } |
| PROFILE_CASE | Copy Code      			      "payload": {     "subject": "External Profile Case creation",     "description": "Description of the case",     "workflow": {         "customProperties": {             "spr_uc_status": [                 "New"             ],             "spr_uc_priority": [                 "High"             ],             "spr_uc_type": [                 "Complaint"             ]         },         "queues": []     },     "channelType": "SMS",     "channelId": "919370333926",     "contactInfo": {         "email": "",         "firstName": "John",         "lastName": "Doe",         "fullName": "John Doe",         "phoneNo":"919370333926",         "website":["www.sprinklr.com","www.facebook.com"]    },     "commentDTO": {         "attachments": [             {                 "type": "IMAGE",                 "title": "Sample Image",                 "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg",                 "mimeType": "images/jpg"            }         ],         "comment" : "Testing Comment Here"     } } |
| PROFILE_CASE_WITH_MESSAGES | Copy Code      			      "payload": {         "subject": "API Case creation",         "description": "This case is created with API.012",         "firstMessageId": "ACCOUNT_600056911_1742986039000_FACEBOOK_470_600275313172150",         "priority": "high",         "summary": "Urgent Case",         "dueDate": 0,         "workflow": {             "customProperties": {                 "spr_uc_status": [                     "New"                 ],                 "spr_uc_priority": [                     "High"                 ],                 "spr_uc_type": [                     "Complaint"                 ]             }         },         "contact": {         "id": "TWITTER_1619985399673421826",         "name": "ABC"     }     } |
| CAMPAIGN | Copy Code      			      "payload": {         "name": "Campaign-BR",         "description": "Testing06",         "tags": [             "Int Tag",             "Campaign Tag"         ],         "status": "APPROVED",         "partnerCustomFields": {             "5c35cbf2e4b0e1b05edd1b01": [                 "1"             ]         },         "clientCustomFields": {             "5ad59e6fe4b024f15e8384ef": [                 "ABC"             ]         }     } |
| CUSTOM_FIELD | Copy Code      			      "payload": {     "label": "api 2 test-b",     "assetTypes": [         "UNIVERSAL_CASE",         "SPR_TASK"     ],     "type": "TEXT",     "visibility": {         "globallyVisible": false,         "visibilityConfig": [             {                 "type": "CLIENT",                 "ids": [                     "2",                     "4"                 ]             }         ]     },     "category": "API2",     "enabled": false,     "permissions": [         {             "spaceType": "CLIENT",             "spaceId": 2,             "permissionConfigs": [                 {                     "permissions": [                         "ALL"                     ],                     "type": "USER_GROUP",                     "ids": [                         "5f2933921a761e2bdfe7b5bc"                     ]                 },                 {                     "permissions": [                         "ALL"                     ],                     "type": "USER",                     "ids": [                         "600040226",                         "600030703"                     ]                 }             ]         }     ] } |
| PROFILE | Copy Code      			     "payload": {         "id": "Shelton_external_CRMID",         "contact": {             "firstName": "Test",             "lastName": "AB",             "fullName": "User User",             "email": "Test@sprinklr.com",             "phoneNo": "217-555-5555",             "address": {                 "street1": "123 Main St.",                 "city": "Austin",                 "state": "Texas",                 "country": "US",                 "postalCode": "78749"             },             "website": [                 "http://onsite.com"             ]         },         "profiles": [             {                 "name": "thamee_thammu",                 "channelType": "TWITTER",                 "channelId": "33",                 "permalink": "http://crmsite.com/Test"             }         ],         "profileWorkflow": {             "profileLists": [                 0             ],             "customProperties": {                 "additionalProp1": [                     "string"                 ],                 "additionalProp2": [                     "string"                 ],                 "additionalProp3": [                     "string"                 ]             },             "profileSpaceWorkflows": [                 {                     "spaceId": "8033"                 }             ]         }     } |
| SAM | Copy Code      			      "payload": {         "name": "Testing SAM API",         "description": "Sample Description from API",         "assetType": "PHOTO",         "status": "DRAFT",         "taxonomy": {             "campaignId": "",                   "partnerCustomProperties": {}         },         "attachment": {             "type": "IMAGE",             "url": "https://sprcdn-prod0-sam.sprinklr.com/9004/Image_Asset_1-e7d4785d-0b47-4818-ab65-11e093394057-1529617391_p.jpg",             "previewUrl": "https://sprcdn-prod0-sam.sprinklr.com/9004/Image_Asset_1-e7d4785d-0b47-4818-ab65-11e093394057-1529617391_p.jpg",             "mimeType": "image/jpg"         },         "validity": {             "expiryTime": 1695219326000,             "availableFrom": 1695132926000,             "neverExpire": false,             "visibleFrom": 1695132926000         },         "assetSource": "SPRINKLR",         "restricted": false     } |
| USER | Copy Code      			      "payload": {        "userName": "bhagyashree.rai+newtest+qa6@sprinklr.com",         "name": {             "familyName": "John",             "givenName": "Doe"         },         "locale": "EN_US",         "clientAttributes": [             {                 "clientId": 66000002,                 "userType": "CLIENT_ADMIN",                 "phoneNumbers": [                     {                         "value": "+919123456789"                     }                 ]             },             {                 "clientId": 66000002,                 "userType": "CLIENT_ADMIN",                 "phoneNumbers": [                     {                         "value": "+919123456789"                     }                 ],                 "businessCategory": "CORPORATE",                 "userGroupIds": [],                 "clientCustomProperties": {},                 "designation": "test",                 "department": "test"             }         ]     } |
| DRAFT_MESSAGE | Copy Code      			      "payload": {         "accountIds": [             66085334         ],         "content": {             "title": "Testing API2 publishing",             "text": "Testing API2 publishing",             "attachment": {                 "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",                 "title": "Video Asset",                 "type": "VIDEO",                 "previewUrl": "https://qa4-cdata-app.sprinklr.com/DAM/400002/1a30fb97-e7fa-4a34-9f8f-6af4f0d97fac-1686362046/preview_image_0-fd451247-18b1-.png",                 "closedCaptions": [                     {                         "languageCode": "en",                         "title": "AnimatedVideo_Captions.en.srt",                         "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/747948f1-d93b-4938-bb88-b12a07f74a5f-2843360148.srt",                         "extension": "srt"                     }                 ]             }         },         "taxonomy": {             "campaignId": "66000002_1"         }     } |
| REPLY_DM | Copy Code      			      "payload": {         "accountId": 600050101,         "content": {             "text": "New test message from api asasa asa",             "attachment": {                 "type": "IMAGE",                 "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg"             }         },         "taxonomy": {             "campaignId": "66000002_3287"         },         "inReplyToMessageId": "ACCOUNT_600050101_1743147159000_FACEBOOK_38_m_X3kdV5GQMqia5Cxi3Uhk5B5AlbOXAPgFKKHUVFqxv84sJT3QN3ZYi2XX1obr5u8zHGsid-xVDLhGYFbA3nhFvA",         "toProfile": {             "channelType": "FACEBOOK",             "channelId": "4854526314645371"         },         "approval": {}     } |
| REPLY_MESSAGE | Copy Code      			      "payload": {         "accountId": 600038198,         "content": {             "text": "New test message from api as",             "attachment": {                 "type": "IMAGE",                 "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg"             }         },         "taxonomy": {             "campaignId": "66000002_3287"         },         "inReplyToMessageId": "ACCOUNT_600002748_1695565012562_TWITTER_7_1705949424906625102",         "toProfile": {             "channelType": "TWITTER",             "channelId": "1619985399673421826"         },         "approval": {}     } |
| SCHEDULE_MESSAGE | Copy Code      			      "payload": {         "id": 260528845,         "accountIds": [             66085334         ],         "content": {             "title": "Testing API2 publishing",             "text": "Testing API2 publishing",             "attachment": {                 "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",                 "title": "Video Asset",                 "type": "VIDEO",                 "previewUrl": "https://qa4-cdata-app.sprinklr.com/DAM/400002/1a30fb97-e7fa-4a34-9f8f-6af4f0d97fac-1686362046/preview_image_0-fd451247-18b1-.png",                 "closedCaptions": [                     {                         "languageCode": "en",                         "title": "AnimatedVideo_Captions.en.srt",                         "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/747948f1-d93b-4938-bb88-b12a07f74a5f-2843360148.srt",                         "extension": "srt"                     }                 ]             }         },          "scheduleDate": 1744794000000,         "taxonomy": {             "campaignId": "66000002_1"         },         "approval": {}     } |
| COMMENT | Copy Code      			      "payload": {         "entityId": "123",         "entityType": "CASE",         "text": "hi",         "attachment": {             "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",             "previewUrl": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image_p.png",             "type": "VIDEO"         }     } |
| COMMENT_WITH_MULTIPLE_ATTACHMENTS | Copy Code      			      "payload": {         "entityId": "12232",         "entityType": "CASE",         "comment": "Add Comment Attachments on Case",         "attachments": [             {                 "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",                 "previewUrl": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",                 "type": "IMAGE"             },             {                 "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",                 "previewUrl": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",                 "type": "IMAGE"             }         ]     } |
| TASK | Copy Code      			      "payload": {         "taskType": "Design Task",         "title": "SAM TASK via API2.02025-03-25 11:46:56.035",         "description": "SAM TASK description via API2.0",         "dueDate": 1594642560000,         "taskStatus": "New",         "assignment": {             "assigneeId": "66000149",             "assigneeType": "USER"         },         "assetId": "67e4d18d2caa57607600a975",         "assetType": "MEDIA_ASSET"     } |
| LISTENING_TOPIC | Copy Code      			      "payload": {         "name": "Customer Support",         "displayName": "Api Topic44",         "topicType": "QUERY_LISTENING",         "description": "Created via Listening API",         "topicGroupId": "67fe670fb0cde13474489bf6",         "startDate": 1615140543000,         "endDate": 1680065287000,         "tags": [             "API"         ],         "sources": [             "TWITTER"         ],         "enabled": false,         "query": "message: hello",         "excludeRetweets": false,         "matchQuotedRetweets": false,         "excludePossiblySensitiveContent": false,         "excludeUrlsInSearch": false,         "onlyVerifiedUser": false,         "clientId": 1,         "partnerCustomProperties": {}     } |
| KEYWORD_GROUP | Copy Code      			      "payload": {         "name": "Deepak Api Testing v1",         "description": "Testing new Keyword API",         "conditions": [             {                 "term": "Rolex",                 "distance": 4,                 "keywordType": "KEYWORD"             }         ],         "tags": [             "Watch",             "TimePiece",             "Handmade",             "Iconic"         ],         "shareConfig": {             "shareWithEveryOne": true         },         "permissionEntity": {             "userIds": [                 66000101             ],             "userGroupIds": []         }     } |


### Payload Parameters


For the description of each payload parameter,  refer to the table for the respective request type



- [CASE](https://dev.sprinklr.com/create-v3#case-payload-table)

- [PROFILE_CASE](https://dev.sprinklr.com/create-v3#profile-case-payload-table)

- [CAMPAIGN](https://dev.sprinklr.com/create-v3#campaign-payload-table)

- [CUSTOM_FIELD](https://dev.sprinklr.com/create-v3#custom-field-payload-table)

- [PROFILE](https://dev.sprinklr.com/create-v3#profile-payload-table)

- [SAM](https://dev.sprinklr.com/create-v3#sam-payload-table)

- [USER](https://dev.sprinklr.com/create-v3#user-payload-table)

- [DRAFT_MESSAGE](https://dev.sprinklr.com/create-v3#draft-message-payload-table)

- [REPLY_DM and REPLY_MESSAGE](https://dev.sprinklr.com/create-v3#reply-payload-table)

- [SCHEDULE_MESSAGE](https://dev.sprinklr.com/create-v3#schedule-message-payload-table)

- [COMMENT](https://dev.sprinklr.com/create-v3#comment-payload-table)

- [COMMENT_WITH_MULTIPLE_ATTACHMENTS](https://dev.sprinklr.com/create-v3#comment-with-multiple-attachments-payload-table)

- [TASK](https://dev.sprinklr.com/create-v3#task-payload-table)

- [LISTENING_TOPIC](https://dev.sprinklr.com/create-v3#listening-topic-payload-table)

- [KEYWORD_GROUP](https://dev.sprinklr.com/create-v3#keyword-group-payload-table)

### CASE

**Dev Notes: **The format of firstMessageId is `sourceType (ACCOUNT, PERSISTENT_SEARCH, LISTENING) + “_”+ sourceId + “_” + channelCreatedTime + “_” + “channelType” + “_” + ” messageType“ +”_” + channelMessageId`. For example, ACCOUNT_600056911_1742986039000_FACEBOOK_470_600275313172150.


You can get these details for the first message using the Read Message by UMID API. UMID of a message can be retrieved from the Sprinklr UI.



























































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| firstMessageId |  | Required | The Id of the first message to be associated with the case. For example, ACCOUNT_600056911_1742986039000_FACEBOOK_470_60027531317215 | String |
| subject |  | Optional | The subject of the case. | String |
| description |  | Optional | The desription of the case. | String |
| priority |  | Optional | The urgency of the case with which case should be addressed. | String |
| summary |  | Optional | The summary of the case. | String |
| dueDate |  | Optional | Timestamp by when the case must be resolved. | Epoch |
| workflow |  | Optional | Object describing the workflow schema for the case. | Object |
|  | customProperties | Optional | Refers to the custom properties of the case. | Object |
| contact |  | Optional | Object containing the contact details. | Object |
|  | id | Required | The unique id of the contact. | String |
|  | name | Optional | Name of the contact. | String |

### PROFILE_CASE



























































































































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| subject |  | Optional | The subject of the case. | String |
| description |  | Optional | The desription of the case. | String |
| workflow |  | Optional | Object describing the workflow schema for the case. | Object |
|  | customProperties | Optional | Refers to the custom properties of the case. | Object |
|  | queues | Optional | A list of queues to which the case is added. | List [Long] |
| channelType |  | Required | The channel type associated with profile. | String |
| channelId |  | Optional for EMAIL and SMS channelsRequired for all other channels | Refers to the unique identifier for the customer profile. | String |
| contactInfo |  | Required | The object contaning detailed contact information associated with the profile. | Object |
|  | email | Required for EMAIL channel type. Optional for SMS channel type. | Email Id of the profile. | String |
|  | firstName | Optional | First name of the profile. | String |
|  | lastName | Optional | Last name of the profile. | String |
|  | fullName | Optional | Full name of the profile. | String |
|  | phoneNo | Required for SMS channel type. Optional for EMAIL channel type. | The phone number associated with the profile. | String |
|  | website | Optional | The list of websites associated with the profile. | Array |
| commentDTO |  | Optional | Object containing the comment details (if any). | Object |
|  | attachments | Optional | Array containing the attachment details. | Array |
|  | attachments.type | Required | Refers to the type of attachment. Supported Attachment Types: IMAGE, VIDEO, LINK, DOC, AUDIO | String |
|  | attachments.title | Optional | Refers to the title of the attachment. | String |
|  | attachments.url | Required | Refers to the url of the attachment | String |
|  | attachments.mimeType | Optional | Refers to attachment type and its format. For example, image/jpg | String |

### CAMPAIGN

















































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| name | Required | Name of the campaign. | String |
| status | Required | Status of the campaign. For example, DRAFT, APPROVED | String |
| description | Optional | Description of the campaign. | String |
| tags | Optional | Tags associated with the campaign. | Array of Strings |
| partnerCustomFields | Optional | Partner level custom fields of the campaign. | Object |
| clientCustomFields | Optional | Client level custom fields of the campaign. | Object |

### CUSTOM_FIELD























































****````













































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| label |  | Required | Label or tag that you want to add to the custom field. | String |
| assetTypes |  | Required | The asset type to which you want to associate the custom field. Supported Asset Types: Account, Outbound Message, Message, Profile, Media Asset, User, Campaign, Sub-Campaign, Community Product, Paid Initiative, Ad Set, Ad Variant, Case, Universal Case, Survey, Task. | Array of Strings |
| type |  | Required | Refers to the data type of the custom field. Supported Data Types: TEXT, PICKLIST, MULTISELECT PICKLIST, NUMBER, DATE, TEXT MULTI, TEXTAREA. | String |
| visibility |  | Optional | Object defining the visibility of the custom field. | Object |
|  | globallyVisible | Optional | Indicates whether the field is visible globally. Supported values: true, false | Boolean |
|  | visibilityConfig | Optional | Array defining the visibility configuration for the custom field.  				Dev Notes: If visibilityConfig is defined, globallyVisible needs to be false. | String |
|  | visibilityConfig.type | Required | Refers to the type of client/user you want to share the custom field with. Supported Values: CLIENT, CLIENT_GROUP, USER, USER_GROUP. | String |
|  | visibilityConfig.ids | Optional | IDs of entities (like clients or partners) with visibility access. | List [String, Integer] |
| category |  | Optional | The category of the custom field. | String |
| enabled |  | Optional | Indicates whether the field is active/enabled. Possible values are true or false. | Boolean |
| permissions |  | Optional | Array defining the permission levels for the custom field. | String |
|  | spaceType | Optional | The space type to which you want to add the custom field. | String |
|  | spaceId | Optional | The space Id where to add the custom field. | Number |
|  | permissionConfigs.permissions | Optional | Refers to the permissions you want to give to the custom field. Select “ALL” to give all the permissions to the selected group. | List [String] |
|  | permissionConfigs.type | Optional | Refers to the type of group you want to give permission to. Supported Values: CLIENT, CLIENT_GROUP, USER, USER_GROUP. | String |
|  | permissionConfigs.ids | Optional | The Ids with respect to the type defined. | List [String, Integer] |

### PROFILE





























































































































****




























      [profile list](https://www.sprinklr.com/help/articles/sprinklr-service-glossary/universal-profile/640905717517d84a3aaf398d)



























      [profile list](https://www.sprinklr.com/help/articles/sprinklr-service-glossary/universal-profile/640905717517d84a3aaf398d)




| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| id |  | Required | Id of the user profile. | String |
| contact |  | Required | Refers to the object containing the contact details of the customer. | Object |
|  | firstName | Optional | First name of the user. It is recommended to specify first name as it acts as an unique identifier for the customer profile. | String |
|  | lastName | Optional | Last name of the user.It is recommended to specify last name as it acts as an unique identifier for the customer profile. | String |
|  | fullName | Optional | Refers to the full name of the customer. It is recommended to pass full name as it acts as an unique identifier for the customer profile. | String |
|  | email | Optional | Refers to the email Id of the customer | String |
|  | phoneNo | Optional | Refers to the contact number of the customer. | String |
|  | address | Optional | Object containing the address of the user. | Object |
|  | address.street1 | Optional | Enter the street details. | String |
|  | address.city | Optional | Enter the city. | String |
|  | address.state | Optional | Enter the state. | String |
|  | address.country | Optional | Enter the country. | String |
|  | website | Optional | List of websites associated with the customer. Example, [                 "http://onsite.com", "https://youtube.com"             ] | Array |
| profiles |  | Required | Object containing social profile details of the customer. | Object |
|  | name | Required | Refers to the full name of the customer. | String |
|  | channelType | Required | Refers to the channel type you want to associate with the profile. Dev Notes: The channel type is case sensitive and must be passed in uppercase. For example, SMS for SMS channel, EMAIL for email channel, WHATSAPP for WhatsApp social channel, and so on. | String |
|  | permalink | Optional | Refers to the link to the social profile the customer is associated with. | String |
|  | channelId | Required | Refers to the channel Id. That is, native channel user Id of the customer | String |
| profileWorkflow |  |  | Refers to the object containing the profile workflow properties such as profile list details, custom properties, and workspace level details. | Object |
|  | profileLists | Optional | List containing the  Ids on the global level. You can fetch the existing profile list name and Id using Bootstrap API. | List [Integer] |
|  | customProperties | Optional | Refers to the global level custom properties you want to associate with the profile. | Object |
|  | profileSpaceWorkflows | Optional | Refers to the array containing the workspace level properties associated with the profile. | Array |
|  | profileSpaceWorkflows.spaceId | Optional | Refers to the workspace Id where the customer needs to be added. | String |
|  | profileSpaceWorkflows.profileLists | Optional | List containing the  Ids on the global level. You can fetch the existing profile list name and Id using Bootstrap API. | List [Integer] |

### SPRINKLR ASSET MANAGER (SAM)

































































































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| name |  | Required | Name of the asset. | String |
| assetType |  | Required | The type of asset. Supported values: PRESENTATION, PHOTO, VIDEO, AUDIO, FLASH, HTML, PDF, DOC, DOCX, EXCEL, ZIP, PSD, SKETCH, FONT | String |
| status |  | Required | Refers to the status of the asset. Supported Values: APPROVED, DRAFT, EXPIRED | String |
| description |  | Optional | Description of the asset. | String |
| taxonomy |  | Required | Taxonomy details of the asset. | Object |
|  | campaignId | Required | Campaign identifier to associate the asset with. |  |
|  | partnerCustomProperties | Optional | Refers to the object containing custom fields and their values. | Object |
| attachment |  | Required | Object defining the attachment details. | Object |
|  | type | Required | Refers to the type of attachment. Supported values: AUDIO, VIDEO, IMAGE. | String |
|  | url | Required | Refers to the URL of the attachment. | String |
|  | previewUrl | Optional | Refers to the preview URL of the attachment. | String |
|  | mimeType | Optional | Refers to the combination of attachment type and format. For example, image/jpg. | String |
| validity |  | Optional | Refers to the object containing the asset validity details. | Object |
|  | expiryTime | Optional | Refers to the expiry time of the asset. | Epoch |
|  | availableFrom | Optional | Refers to the time from when the asset will be available for use. | Epoch |
|  | neverExpire | Optional | Indicates whether the asset will never expire. Supported values: true, false | Epoch |

### USER

























































































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| userName |  | Required | The email Id of the user. The email Id of the user must be unique every time you hit the Create API. | String |
| name |  | Required | Object that specifies the familyName and givenName. | Object |
|  | familyName | Required | Refers to the last name of the user | String |
|  | givenName | Required | Refers to the first name of the user | String |
| locale |  | Optional | Refers to the language code of the user. | String |
| clientAttributes |  |  | The client-level attributes of the user. | Array |
|  | clientId | Required | Refers to the workspace Id where you want to add the user. | Integer |
|  | userType | Required | The type of user you want to create. Supported values: PARTNER_ADMIN, PARTNER_USER, CLIENT_ADMIN, CLIENT_USER | String |
|  | phoneNumbers | Optional | Array containing phone details. | String |
|  | phoneNumbers.value | Optional | Refers to the phone number of the user. | String |
|  | businessCategory | Optional | The category of business. Supported values: CORPORATE or DISTRIBUTED. | String |
|  | userGroupIds | Optional | The user group Ids where you want to add the user. | List[String] |
|  | clientCustomProperties | Optional | The workspace level custom properties. | Object |
|  | department | Optional | Refers to the user department. | String |
|  | designation | Optional | Refers to the user designation. | String |

### DRAFT_MESSAGE































































































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| accountIds |  | Required | The list of account Ids from which the message is created. | Array |
| content |  | Required | The object containing message content details. | Object |
|  | title | Optional | Title of the message to be published. | String |
|  | text | Required | Text of the message to be published. | String |
|  | attachment | Optional | Object containing the attachment details. | Object |
|  | attachment.url | Optional | URL of the attachment (media file). | String |
|  | attachment.title | Optional | Title of the attachment. | String |
|  | attachment.type | Required | Type of attachment. Supported values: VIDEO, IMAGE, CAROUSEL, MULTI_MEDIA, POLL (LinkedIn) | String |
|  | attachment.previewUrl | Optional | Preview URL for the attachment. | String |
|  | attachment.closedCaptions | Optional | List of closed captions for the media. | Array (Object) |
|  | attachment.closedCaptions.languageCode | Required | Language code for the closed caption file. | String |
|  | attachment.closedCaptions.title | Required | Title of the closed caption file. | String |
|  | attachment.closedCaptions.url | Required | URL to the closed caption file. | String |
|  | attachment.closedCaptions.extension | Required | Extension of the closed caption file. For example, srt. | String |
| taxonomy |  | Required | Object containing the taxonomy details. | String |
|  | campaignId | Required | Campaign under which you want to create the draft. | String |

### REPLY_DM and REPLY_MESSAGE
































































































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| accountId |  | Required | Account Id from which you want to create the message. | String |
| content |  | Required | The object containing message content details. | Object |
|  | title | Optional | Title of the message to be published. | String |
|  | text | Required | Text of the message to be published. | String |
|  | attachment | Optional | Object containing the attachment details. | Object |
|  | attachment.url | Optional | URL of the attachment (media file). | String |
|  | attachment.type | Required | Type of attachment. Supported values: VIDEO, IMAGE, CAROUSEL, MULTI_MEDIA, POLL (LinkedIn) | String |
| taxonomy |  | Required | Object containing the taxonomy details. | String |
|  | campaignId | Required | Campaign under which you want to create the draft. | String |
| inReplyToMessageId |  | Required | Message Id of the message you want to send the reply for. | String |
| toProfile |  | Required | The object containing customer profile details. | String |
|  | channelType | Required | Channel type of the profile. | String |
|  | channelId | Required | Channel Id of the profile. | String |
| approval |  | Optional | The object containing approval details. | String |
|  | type | Required | Type of approval to process. Default value is NONE.  Supported values: ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE | String |
|  | id | Required | Value for the chosen approval type. | String |

### SCHEDULE_MESSAGE




































































































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| accountIds |  | Required | The account Ids from which the message is created. | Array |
| content |  | Required | The object containing message content details. | Object |
|  | title | Optional | Title of the message to be published. | String |
|  | text | Required | Text of the message to be published. | String |
|  | attachment | Optional | Attachment object containing details of the media. | Object |
|  | attachment.url | Optional | URL of the attachment (media file). | String |
|  | attachment.type | Required | Type of attachment. For example, VIDEO, IMAGE. | String |
| scheduleDate |  | Required | Schedule date for the message. | Epoch |
| taxonomy |  | Required | Campaign ID associated with the content. | String |
|  | campaignId | Required | Campaign ID associated with the content. | String |
| inReplyToMessageId |  | Required | Message Id of the message you want to send the reply for. | String |
| toProfile |  | Required | The object containing the user profile details. | Object |
|  | channelType | Required | Channel Type of the user profile. For example, Facebook. |  |
|  | channelId | Required | Channel Id of the profile. | String |
| approval |  | Optional | The object containing approval details. | Object |
|  | type | Optional | Type of approval to process. Default value is NONE. Supported values: ACCOUNT_OWNER, USER, APPROVAL_PATH, NONE. | String |
|  | id | Required | Value for the chosen approval type. | String |

### COMMENT
































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| entityType |  | Required | Entity type can be MESSAGE, OUTBOUND_MESSAGE, CASE, CAMPAIGN and PROFILE. | String |
| entityId |  | Required | Entity Id of the entity type specified. For example, if the entity type is MESSAGE, specify the message Id. Similarly, for CASE - Case Number, OUTBOUND_MESSAGE - The unique outbound message Id, CAMPAIGN - Campaign Id and PROFILE - Profile Id. | String |
| text |  | Required | The comment the you want to publish. | String |
| attachment |  | Optional | The object containing attachment information. | Object |
|  | url | Optional | The URL of the attachment. | String |
|  | previewUrl | Optional | The URL of the attachment's preview. | String |
|  | type | Optional | The type of the attachment. Supported values: IMAGE, DOC, VIDEO, AUDIO. | String |

### COMMENT_WITH_MULTIPLE_ATTACHMENTS































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| entityType |  | Required | Entity type can be MESSAGE, OUTBOUND_MESSAGE, CASE, CAMPAIGN and PROFILE. | String |
| entityId |  | Required | Entity Id of the entity type specified. For example, if the entity type is MESSAGE, specify the message Id. Similarly, for CASE - Case Number, OUTBOUND_MESSAGE - The unique outbound message Id, CAMPAIGN - Campaign Id and PROFILE - Profile Id. | String |
| comment |  | Optional | The comment associated with the entity. | String |
| attachments |  | Optional | An array containing the attachment details. | Array |
|  | url | Optional | The URL of the attachment. | String |
|  | previewUrl | Optional | The URL of the attachment's preview. | String |
|  | type | Optional | The type of the attachment. Supported values: IMAGE, DOC, VIDEO, AUDIO. | String |

### TASK



















































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| taskType |  | Required | The type of the task. | String |
| title |  | Required | The title of the task. | String |
| description |  | Optional | A description of the task. | String |
| dueDate |  | Required | The due date of the task in milliseconds. | Epoch |
| taskStatus |  | Required | The current status of the task. | String |
| assignment |  | Required | The object containing task assignment details. | String |
|  | assigneeId | Required | The Id of the user to whom the task is assigned. | String |
|  | assigneeType | Required | The type of user. | String |
| assetId |  | Required | The Id of the entity for which the task is created. | String |
| assetType |  | Required | The type of entity for which the task is created. | String |

### LISTENING_TOPIC













































































































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| name |  | Required | The name of the listening topic. | String |
| displayName |  | Optional | The display name of the listening topic. | String |
| topicType |  | Required | The type of the listening topic. Supported values: ACCOUNT_LISTENING, PROFILE_LISTENING, QUERY_LISTENING, GEO_LOCATION. | String |
| description |  | Optional | A description of the listening topic. | String |
| topicGroupId |  | Required | Topic Group ID to which this Listening Topic belongs. | String |
| startDate |  | Required | Start date for Listening Topic to become active. | Epoch |
| endDate |  | Required | End date for Listening Topic to become in-active | Epoch |
| tags |  | Optional | Tags to group Listening Topic based on use case. | List |
| sources |  | Optional | Sources to grab data from. | List |
| enabled |  | Optional | Enable live data fetching. | Boolean |
| query |  | Required | Keyword query to grab messages. | String |
| excludeRetweets |  | Optional | Indicates whether to exclude all retweets. Supported values: true or false. | Boolean |
| matchQuotedRetweets |  | Optional | Indicates whether to match quoted retweets. Supported values: true or false. | Boolean |
| excludePossiblySensitiveContent |  | Optional | Indicates whether to exclude possibly sensitive content. Supported values: true or false. | Boolean |
| excludeUrlsInSearch |  | Optional | Indicates whether to exclude URLs in search.  Supported values: true or false. | Boolean |
| onlyVerifiedUser |  | Optional | Indicates whether to include only verified users. Supported values: true or false. | Boolean |
| clientId |  | Optional | The client ID associated with the topic. | Long |
| partnerCustomProperties |  | Optional | Object defining the key-value pair for global level custom properties that needs to be applied on the listening topic. | Object |


### Keyword Group





























































































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| name |  | Required | The Keyword Group name. | String |
| description |  | Optional | The Keyword Group description. | String |
| conditions |  | Required | The Keyword Group conditions list. | List<Condition> |
|  | term | Required | The value based on keyword type. | String |
|  | distance | Required | The distance is used to set the slop value for elastic search. | Integer |
|  | keywordType | Required | The available keyword types are KEYWORD, PROXIMITY_KEYWORD, PHRASE. | String |
| tags |  | Optional | Keyword List tags list. | List<String> |
| shareConfig |  | Optional | The object containing share configurations which authorise users to view Keyword List. |  |
|  | userIds | Optional | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | Optional | List of User Group IDs, which is unique identifier for each User Group. | List<String> |
|  | clientIds | Optional | List of Client IDs, which is unique identifier for Client. | List<Long> |
|  | clientGroupIds | Optional | List of Client Group IDs, which is unique identifier for Client Group. | List<String> |
|  | shareWithEveryOne | Optional | Set it to true, if you want to share it with all users. | Boolean |
| permissionEntity |  | Optional | The object containing permission configuration to authorise users to edit or update Keyword List. |  |
|  | userIds | Optional | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | Optional | List of User Group IDs, which is unique identifier for each User Group. | List<String> |


## Examples


The following section includes the example requests and responses for each entity:



- [CASE](https://dev.sprinklr.com/create-v3#case-example)

- [PROFILE_CASE](https://dev.sprinklr.com/create-v3#profile-case-example)

- [CAMPAIGN](https://dev.sprinklr.com/create-v3#campaign-example)

- [CUSTOM_FIELD](https://dev.sprinklr.com/create-v3#custom-field-example)

- [PROFILE](https://dev.sprinklr.com/create-v3#profile-example)

- [SAM](https://dev.sprinklr.com/create-v3#sam-example)

- [USER](https://dev.sprinklr.com/create-v3#user-example)

- [DRAFT_MESSAGE](https://dev.sprinklr.com/create-v3#draft-message-example)

- [REPLY_DM](https://dev.sprinklr.com/create-v3#reply-dm-example)

- [REPLY_MESSAGE](https://dev.sprinklr.com/create-v3#reply-message-example)

- [SCHEDULE_MESSAGE](https://dev.sprinklr.com/create-v3#schedule-message-example)

- [COMMENT](https://dev.sprinklr.com/create-v3#comment-example)

- [COMMENT_WITH_MULTIPLE_ATTACHMENTS](https://dev.sprinklr.com/create-v3#comment-with-multiple-attachments-example)

- [TASK](https://dev.sprinklr.com/create-v3#task-example)

- [LISTENING_TOPIC](https://dev.sprinklr.com/create-v3#listening-topic-example)

- [KEYWORD_GROUP](https://dev.sprinklr.com/create-v3#keyword-group-example)


### CASE


#### Request





  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/CASE' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Content-Type: application/json' \
--header 'Cookie: JSESSIONID=B0710AA6671C4F42EEDB8622D00A548E' \
--data '{
    "requestType": "CASE",
    "payload": {
        "subject": "API Case creation",
        "description": "This case is created with API.012",
        "firstMessageId": "ACCOUNT_600056911_1742986039000_FACEBOOK_470_600275313172150",
        "priority": "high",
        "summary": "Urgent Case",
        "dueDate": 0,
        "workflow": {
            "customProperties": {
                "spr_uc_status": [
                    "New"
                ],
                "spr_uc_priority": [
                    "High"
                ],
                "spr_uc_type": [
                    "Complaint"
                ]
            }
        },
        "contact": {
        "id": "TWITTER_1619985399673421826",
        "name": "ABC"
    }
    }
}'





#### Response

      

{
    "id": "67f61359d92cf915b0ae45fc",
    "caseNumber": 6842917,
    "subject": "#6842917 Facebook API Case creation",
    "description": "This case is created with API.012",
    "version": 0,
    "status": "New",
    "priority": "high",
    "caseType": "Complaint",
    "externalCase": null,
    "externalCaseInfo": {
        "externalCases": []
    },
    "workflow": {
        "assignment": null,
        "modifiedTime": null,
        "customProperties": {
            "spr_uc_type": [
                "Complaint"
            ],
            "spr_uc_priority": [
                "high"
            ],
            "spr_uc_status": [
                "New"
            ],
            "spr_uc_eng_score": [
                "0"
            ]
        },
        "queues": [],
        "spaceWorkflows": null,
        "campaignId": null
    },
    "channelCustomProperties": [],
    "contact": {
        "id": "FACEBOOK_1619985399673421826",
        "name": "Sikander Singh",
        "channelType": "FACEBOOK",
        "channelId": "1619985399673421826",
        "fromSnUserId": "1619985399673421826"
    },
    "attachment": null,
    "dueDate": 0,
    "summary": "Urgent Case",
    "smartSummary": null,
    "createdTime": 1744180057370,
    "modifiedTime": 1744180057644,
    "firstMessageId": "ACCOUNT_600056911_1742986039000_FACEBOOK_470_600275313172150",
    "sentiment": null,
    "latestProfileMessageAssociatedTime": 1742986039000,
    "conversationId": null,
    "firstMessageAssociatedTime": 1742986039000,
    "latestMessageAssociatedTime": 1742986039000,
    "firstUserBrandResponseCreationTime": null,
    "avgCaseResponseSLA": null,
    "totalProcessingClockTime": 0,
    "allEngagedUsersList": [],
    "associatedFanMessageCount": 1,
    "associatedBrandMessageCount": 0,
    "associatedUserBrandMessageCount": 0,
    "deleted": false,
    "latestMessageId": null
}





### Example - Request (PROFILE_CASE)


#### Request




  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/CASE' \
--header 'key: {Enter your API Key}' \
--header 'Authorization: Bearer {Enter your Access Tokey}' \
--header 'Content-Type: application/json' \
--header 'Cookie: JSESSIONID=04A3822D631AF6E13748A9C59AFC1F23; JSESSIONID=D6605664A6605E54E8331F6413B69425' \
--data '{
    "requestType": "PROFILE_CASE",
    "payload": {
    "subject": "External Profile Case creation",
    "description": "Description of the case",
    "workflow": {
        "customProperties": {
            "spr_uc_status": [
                "New"
            ],
            "spr_uc_priority": [
                "High"
            ],
            "spr_uc_type": [
                "Complaint"
            ]
        },
        "queues": []
    },
    "channelType": "SMS",
    "channelId": "919370333926",
    "contactInfo": {
        "email": "",
        "firstName": "John",
        "lastName": "Doe",
        "fullName": "John Doe",
        "phoneNo":"919370333926",
        "website":["www.sprinklr.com","www.facebook.com"]
   },
    "commentDTO": {
        "attachments": [
            {
                "type": "IMAGE",
                "title": "Sample Image",
                "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg",
                "mimeType": "images/jpg"
           }
        ],
        "comment" : "Testing Comment Here"
    }
}
}'






#### Response

      

{
    "id": "67f89bddade7f94977b40d6c",
    "caseNumber": 6919657,
    "subject": "#6919657 Sms External Profile Case creation",
    "description": "Description of the case",
    "version": 0,
    "status": "New",
    "priority": "High",
    "caseType": "Complaint",
    "externalCase": null,
    "externalCaseInfo": {
        "externalCases": []
    },
    "workflow": {
        "assignment": null,
        "modifiedTime": null,
        "customProperties": {
            "spr_uc_type": [
                "Complaint"
            ],
            "spr_uc_priority": [
                "High"
            ],
            "spr_uc_status": [
                "New"
            ],
            "spr_is_profile_case": [
                "true"
            ]
        },
        "queues": [],
        "spaceWorkflows": null,
        "campaignId": null
    },
    "channelCustomProperties": [],
    "contact": {
        "id": "SMS_919370333926",
        "name": null,
        "channelType": "SMS",
        "channelId": "919370333926",
        "fromSnUserId": "919370333926"
    },
    "attachment": null,
    "dueDate": null,
    "summary": null,
    "smartSummary": null,
    "createdTime": 1744346076383,
    "modifiedTime": 1744346077543,
    "firstMessageId": null,
    "sentiment": null,
    "latestProfileMessageAssociatedTime": null,
    "conversationId": null,
    "firstMessageAssociatedTime": null,
    "latestMessageAssociatedTime": 1744346076383,
    "firstUserBrandResponseCreationTime": null,
    "avgCaseResponseSLA": null,
    "totalProcessingClockTime": 0,
    "allEngagedUsersList": [],
    "associatedFanMessageCount": 0,
    "associatedBrandMessageCount": 0,
    "associatedUserBrandMessageCount": 0,
    "deleted": false,
    "latestMessageId": null
}





### CAMPAIGN


#### Request




  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/CAMPAIGN' \
--header 'Authorization: Bearer nKNILl4utxEkXao4jjE9N4xJXS1tnhdHvAhXIRXjMzw3ODJjNWJkZS1kOTViLTMxY2ItYWM1My1kMzU3YzIzMzA1NmQ=' \
--header 'Content-Type: application/json' \
--header 'Cookie: JSESSIONID=E33FB25BD6157C7981C559BD332F73A2' \
--data '{
    "requestType": "CAMPAIGN",
    "payload": {
        "name": "Campaign-BR",
        "description": "Testing06",
        "tags": [
            "Int Tag",
            "Campaign Tag"
        ],
        "status": "APPROVED",
        "partnerCustomFields": {
            "5c35cbf2e4b0e1b05edd1b01": [
                "1"
            ]
        },
        "clientCustomFields": {
            "5ad59e6fe4b024f15e8384ef": [
                "ABC"
            ]
        }
    }
}'





#### Response

      

{
    "id": "66000002_4813",
    "name": "Campaign-BR",
    "displayId": null,
    "parentCampaignId": null,
    "description": "Testing06",
    "createdTime": 1744183405820,
    "modifiedTime": 1744183405819,
    "startDate": null,
    "endDate": null,
    "tags": [
        "Int Tag",
        "Campaign Tag"
    ],
    "owner": 66014658,
    "partnerCustomProperties": {
        "5c35cbf2e4b0e1b05edd1b01": [
            "1"
        ]
    },
    "clientCustomProperties": {
        "5ad59e6fe4b024f15e8384ef": [
            "ABC"
        ]
    },
    "status": "APPROVED",
    "visibility": null,
    "archived": false,
    "externalSource": null,
    "externalSourceId": null,
    "deleted": false
}





### CUSTOM_FIELD


#### Request




  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/CUSTOM_FIELD' \
--header 'key: {Enter your API key}' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Content-Type: application/json' \
--data '{
    "requestType": "CUSTOM_FIELD",
    "payload": {
    "label": "api 2 test-b",
    "assetTypes": [
        "UNIVERSAL_CASE",
        "SPR_TASK"
    ],
    "type": "TEXT",
    "visibility": {
        "globallyVisible": false,
        "visibilityConfig": [
            {
                "type": "CLIENT",
                "ids": [
                    "2",
                    "4"
                ]
            }
        ]
    },
    "category": "API2",
    "enabled": false,
    "permissions": [
        {
            "spaceType": "CLIENT",
            "spaceId": 2,
            "permissionConfigs": [
                {
                    "permissions": [
                        "ALL"
                    ],
                    "type": "USER_GROUP",
                    "ids": [
                        "5f2933921a761e2bdfe7b5bc"
                    ]
                },
                {
                    "permissions": [
                        "ALL"
                    ],
                    "type": "USER",
                    "ids": [
                        "600040226",
                        "600030703"
                    ]
                }
            ]
        }
    ]
}
}'





#### Response

      

{
    "id": "67f7d5a7ade7f94977b38b56",
    "fieldName": "_c_67f7d5a2ade7f94977b38b4e",
    "label": "api 2 test-b",
    "description": null,
    "assetTypes": [
        "CASE",
        "TASK"
    ],
    "type": "TEXT",
    "values": [],
    "valuesOptions": null,
    "category": "API2",
    "enabled": false,
    "visibility": {
        "globallyVisible": false,
        "visibilityConfig": [
            {
                "type": "CLIENT",
                "ids": [
                    "2",
                    "4"
                ]
            }
        ]
    },
    "permissions": [
        {
            "spaceType": "CLIENT",
            "spaceId": "2",
            "permissionConfigs": [
                {
                    "type": "USER_GROUP",
                    "ids": [
                        "5f2933921a761e2bdfe7b5bc"
                    ],
                    "permissions": [
                        "ALL"
                    ]
                },
                {
                    "type": "USER",
                    "ids": [
                        "600030703",
                        "600040226"
                    ],
                    "permissions": [
                        "ALL"
                    ]
                }
            ]
        }
    ],
    "optionType": "GENERAL",
    "optionKey": null,
    "accessibleClientIds": [
        2,
        4
    ],
    "createdTime": 1744295334197,
    "modifiedTime": 1744295334197,
    "customFieldControllerById": null,
    "langVsTranslatedFieldValues": null
}





### PROFILE


#### Request




  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/PROFILE' \
--header 'key: {Enter your API key}' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Content-Type: application/json' \
--header 'Cookie: JSESSIONID=04A3822D631AF6E13748A9C59AFC1F23; JSESSIONID=D6605664A6605E54E8331F6413B69425' \
--data-raw '{
    "requestType": "PROFILE",
    "payload": {
        "id": "Shelton_external_CRMID",
        "contact": {
            "firstName": "Test",
            "lastName": "AB",
            "fullName": "User User",
            "email": "Test@sprinklr.com",
            "phoneNo": "217-555-5555",
            "address": {
                "street1": "123 Main St.",
                "city": "Austin",
                "state": "Texas",
                "country": "US",
                "postalCode": "78749"
            },
            "website": [
                "http://onsite.com"
            ]
        },
        "profiles": [
            {
                "name": "thamee_thammu",
                "channelType": "TWITTER",
                "channelId": "33",
                "permalink": "http://crmsite.com/Test"
            }
        ],
        "profileWorkflow": {
            "profileLists": [
                0
            ],
            "customProperties": {
                "additionalProp1": [
                    "string"
                ],
                "additionalProp2": [
                    "string"
                ],
                "additionalProp3": [
                    "string"
                ]
            },
            "profileSpaceWorkflows": [
                {
                    "spaceId": "8033"
                }
            ]
        }
    }
}'





#### Response

      

{
    "id": "67e529ec7085764e3ed1a32d",
    "contact": {
        "firstName": "Test",
        "maidenName": null,
        "lastName": "AB",
        "fullName": "User User",
        "email": "Test@sprinklr.com",
        "username": null,
        "phoneNo": "217-555-5555",
        "address": null,
        "website": [
            "http://onsite.com"
        ],
        "phoneDetails": [],
        "emailDetails": []
    },
    "demographics": null,
    "works": null,
    "profiles": [
        {
            "name": "thamee_thammu",
            "channelType": "TWITTER",
            "channelId": "33",
            "permalink": "http://crmsite.com/Test",
            "avatarUrl": null,
            "profileImageUrl": null,
            "coverImageUrl": null,
            "bio": null,
            "followers": 0,
            "following": 0,
            "username": null,
            "verified": null,
            "unSubscribed": false,
            "deleted": false,
            "snCreatedTime": 0,
            "snModifiedTime": 1744295669044,
            "statusCount": 0,
            "accountSpecificInfos": [],
            "additional": {},
            "birthDate": null,
            "url": "http://crmsite.com/Test",
            "maritalStatus": null
        }
    ],
    "profileWorkflow": {
        "profileLists": [
            0
        ],
        "customProperties": {
            "additionalProp1": [
                "string"
            ],
            "additionalProp2": [
                "string"
            ],
            "additionalProp3": [
                "string"
            ]
        },
        "profileSpaceWorkflows": [
            {
                "spaceId": "8033",
                "modifiedTime": null,
                "customProperties": null,
                "queues": null,
                "profileLists": [],
                "tags": []
            }
        ]
    },
    "createdTime": 1743071724791,
    "modifiedTime": 1744295674392,
    "organizations": null,
    "certificates": null,
    "recommendations": null,
    "educations": null,
    "languages": null,
    "skills": null,
    "courses": null,
    "honors": null,
    "patents": null,
    "projects": null,
    "publications": null,
    "testScores": null,
    "voluntaryExp": null,
    "operatingHours": null,
    "restricted": false
}





### SAM


#### Request




  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/SOCIAL_ASSET' \
--header 'Accept-Encoding: gzip' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Content-Type: application/json' \
--data '{
    "requestType": "SAM",
    "payload": {
        "name": "Testing SAM API",
        "description": "Sample Description from API",
        "assetType": "PHOTO",
        "status": "DRAFT",
        "taxonomy": {
            "campaignId": "",
            "partnerCustomProperties": {}
        },
        "attachment": {
            "type": "IMAGE",
            "url": "https://sprcdn-prod0-sam.sprinklr.com/9004/Image_Asset_1-e7d4785d-0b47-4818-ab65-11e093394057-1529617391_p.jpg",
            "previewUrl": "https://sprcdn-prod0-sam.sprinklr.com/9004/Image_Asset_1-e7d4785d-0b47-4818-ab65-11e093394057-1529617391_p.jpg",
            "mimeType": "image/jpg"
        },
        "validity": {
            "expiryTime": 1695219326000,
            "availableFrom": 1695132926000,
            "neverExpire": false,
            "visibleFrom": 1695132926000
        },
        "assetSource": "SPRINKLR",
        "restricted": false
    }
}'





#### Response

      

{
    "id": "67f7ddc0ade7f94977b39149",
    "name": "Testing SAM API",
    "description": "Sample Description from API",
    "status": "Expired",
    "taxonomy": {
        "name": null,
        "campaignId": null,
        "subCampaignId": null,
        "clientCustomProperties": null,
        "partnerCustomProperties": {},
        "tags": null,
        "urlShortenerId": null
    },
    "insights": {},
    "validity": {
        "expiryTime": 1695219326000,
        "availableFrom": 1695132926000,
        "neverExpire": false,
        "visibleFrom": 1695132926000,
        "visibleTill": null
    },
    "parentId": null,
    "assetSource": "SPRINKLR",
    "sourceId": null,
    "externalMediaId": null,
    "actionStats": {},
    "shareConfigs": [],
    "restricted": false,
    "locked": false,
    "createdTime": 1744297408404,
    "modifiedTime": 1744297408404,
    "defaultLocale": null,
    "langVsTranslatedFieldValues": {},
    "approvedByUser": null,
    "createdByUser": 66014658,
    "versionId": 0,
    "assetType": "PHOTO",
    "attachment": {
        "type": "IMAGE",
        "assetId": null,
        "attachmentOptions": null,
        "url": "https://sprcdn-prod0-sam.sprinklr.com/9004/Image_Asset_1-e7d4785d-0b47-4818-ab65-11e093394057-1529617391_p.jpg",
        "urlHash": null,
        "title": null,
        "description": null,
        "previewUrl": "https://sprcdn-prod0-sam.sprinklr.com/9004/Image_Asset_1-e7d4785d-0b47-4818-ab65-11e093394057-1529617391_p.jpg",
        "hashedPreviewUrl": null,
        "mimeType": "image/jpg",
        "alternateText": null,
        "height": null,
        "width": null
    }
}





### USER

#### Request




  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/USER' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Content-Type: application/scim+json' \
--data-raw '{
    "requestType": "USER",
    "payload": {
       "userName": "bhagyashree.rai+newtest+qa6@sprinklr.com",
        "name": {
            "familyName": "John",
            "givenName": "Doe"
        },
        "locale": "EN_US",
        "clientAttributes": [
            {
                "clientId": 66000002,
                "userType": "CLIENT_ADMIN",
                "phoneNumbers": [
                    {
                        "value": "+919123456789"
                    }
                ]
            },
            {
                "clientId": 66000002,
                "userType": "CLIENT_ADMIN",
                "phoneNumbers": [
                    {
                        "value": "+919123456789"
                    }
                ],
                "businessCategory": "CORPORATE",
                "userGroupIds": [],
                "clientCustomProperties": {},
                "designation": "test",
                "department": "test"
            }
        ]
    }
}'





#### Response

      

{
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:scim:schemas:extension:sprinklrGlobalAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrClientAttributes:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserAssignmentConfig:2.0:User",
        "urn:scim:schemas:extension:sprinklrUserVoiceConfig:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
    ],
    "id": "66062296",
    "externalId": null,
    "lyearnId": null,
    "userPermissions": null,
    "accessibleClientIds": null,
    "userName": "bhagyashree.rai+newtest+qa6@sprinklr.com",
    "name": {
        "familyName": "John",
        "givenName": "Doe"
    },
    "photos": [],
    "phoneNumbers": null,
    "active": false,
    "locale": "EN_US",
    "globalAttributes": null,
    "clientAttributes": [
        {
            "clientId": 66000002,
            "userType": "CLIENT_ADMIN",
            "phoneNumbers": [
                {
                    "value": "+919123456789",
                    "type": null,
                    "primary": null
                }
            ],
            "businessCategory": null,
            "primaryUserGroupId": null,
            "userGroupIds": null,
            "clientCustomProperties": null,
            "designation": null,
            "department": null,
            "managerId": null,
            "managerEmailAddress": null,
            "managerFederationId": null,
            "approvalMandatory": null
        },
        {
            "clientId": 66000002,
            "userType": "CLIENT_ADMIN",
            "phoneNumbers": [
                {
                    "value": "+919123456789",
                    "type": null,
                    "primary": null
                }
            ],
            "businessCategory": "CORPORATE",
            "primaryUserGroupId": null,
            "userGroupIds": [],
            "clientCustomProperties": {},
            "designation": "test",
            "department": "test",
            "managerId": null,
            "managerEmailAddress": null,
            "managerFederationId": null,
            "approvalMandatory": null
        }
    ],
    "isSpaceUser": null,
    "meta": {
        "resourceType": "User",
        "createdTime": null,
        "lastModified": "2025-04-11 09:43:46",
        "location": "/v3/api/entities/create/USER66062296"
    },
    "emails": [
        {
            "value": "bhagyashree.rai+newtest+qa6@sprinklr.com",
            "type": null,
            "primary": true
        }
    ],
    "userAssignmentConfig": null,
    "userVoiceConfig": null,
    "currentLoginStatus": null,
    "upcomingStatus": null,
    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": null
}






### DRAFT_MESSAGE


#### Request




  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/OUTBOUND_MESSAGE' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--data '{
    "requestType": "DRAFT_MESSAGE",
    "payload": {
        "accountIds": [
            66085334
        ],
        "content": {
            "title": "Testing API2 publishing",
            "text": "Testing API2 publishing",
            "attachment": {
                "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
                "title": "Video Asset",
                "type": "VIDEO",
                "previewUrl": "https://qa4-cdata-app.sprinklr.com/DAM/400002/1a30fb97-e7fa-4a34-9f8f-6af4f0d97fac-1686362046/preview_image_0-fd451247-18b1-.png",
                "closedCaptions": [
                    {
                        "languageCode": "en",
                        "title": "AnimatedVideo_Captions.en.srt",
                        "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/747948f1-d93b-4938-bb88-b12a07f74a5f-2843360148.srt",
                        "extension": "srt"
                    }
                ]
            }
        },
        "taxonomy": {
            "campaignId": "66000002_1"
        }
    }
}'





#### Response

      

[
    "MESSAGE_272845063"
]





### REPLY_DM


#### Request





  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/OUTBOUND_MESSAGE' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Enter you Access Token}' \
--data '{
    "requestType": "REPLY_DM",
    "payload": {
        "accountId": 600050101,
        "content": {
            "text": "New test message from api asasa asa",
            "attachment": {
                "type": "IMAGE",
                "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg"
            }
        },
        "taxonomy": {
            "campaignId": "66000002_3287"
        },
        "inReplyToMessageId": "ACCOUNT_600050101_1743147159000_FACEBOOK_38_m_X3kdV5GQMqia5Cxi3Uhk5B5AlbOXAPgFKKHUVFqxv84sJT3QN3ZYi2XX1obr5u8zHGsid-xVDLhGYFbA3nhFvA",
        "toProfile": {
            "channelType": "FACEBOOK",
            "channelId": "4854526314645371"
        },
        "approval": {}
    }
}'





#### Response

      

[
    "POST_272845918",
    "POST_272845919"
]






### REPLY_MESSAGE


#### Request





  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/OUTBOUND_MESSAGE' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer abnQ+7DK1gauzRr8ce/KAx++Xf24GBMSR32dgY9+svI5Mzc3YzI1Ny02NWZhLTMxNTgtOWEyNi0zYTFlYTkwODE4NWI=' \
--header 'Cookie: JSESSIONID=D6605664A6605E54E8331F6413B69425' \
--data '{
    "requestType": "REPLY_MESSAGE",
    "payload": {
        "accountId": 600038198,
        "content": {
            "text": "New test message from api as",
            "attachment": {
                "type": "IMAGE",
                "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/c536c5dd-9ddc-47e4-8916-05b291637ec8-637631488.jpg"
            }
        },
        "taxonomy": {
            "campaignId": "66000002_3287"
        },
        "inReplyToMessageId": "ACCOUNT_600002748_1695565012562_TWITTER_7_1705949424906625102",
        "toProfile": {
            "channelType": "TWITTER",
            "channelId": "1619985399673421826"
        },
        "approval": {}
    }
}'





#### Response

      

[
    "POST_272845968"
]





### SCHEDULE_MESSAGE


#### Request





  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/OUTBOUND_MESSAGE' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--data '{
    "requestType": "SCHEDULE_MESSAGE",
    "payload": {
        "id": 260528845,
        "accountIds": [
            66085334
        ],
        "content": {
            "title": "Testing API2 publishing",
            "text": "Testing API2 publishing",
            "attachment": {
                "url": "https://qa4-cdata-app.sprinklr.com/DAM/400002/75107996-023c-4b23-b48c-f1e3dc9ef174-1188660913/Video_3.mp4",
                "title": "Video Asset",
                "type": "VIDEO",
                "previewUrl": "https://qa4-cdata-app.sprinklr.com/DAM/400002/1a30fb97-e7fa-4a34-9f8f-6af4f0d97fac-1686362046/preview_image_0-fd451247-18b1-.png",
                "closedCaptions": [
                    {
                        "languageCode": "en",
                        "title": "AnimatedVideo_Captions.en.srt",
                        "url": "https://qa4-sprcdn-assets.sprinklr.com/400002/747948f1-d93b-4938-bb88-b12a07f74a5f-2843360148.srt",
                        "extension": "srt"
                    }
                ]
            }
        },
         "scheduleDate": 1744794000000,
        "taxonomy": {
            "campaignId": "66000002_1"
        },
        "approval": {}
    }
}'





### COMMENT


#### Request





  Copy Code



curl --location --request POST 'https://qa6-api2-v3.sprinklr.com/v3/api/entities/create/COMMENT' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Content-Type: application/json' \
--header 'Cookie: JSESSIONID=D6605664A6605E54E8331F6413B69425' \
--data '{
    "requestType": "COMMENT",
    "payload": {
        "entityId": "123",
        "entityType": "CASE",
        "text": "hi",
        "attachment": {
            "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
            "previewUrl": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image_p.png",
            "type": "VIDEO"
        }
    }
}'





#### Response

      

{
    "id": "67fe6429b588615185ee6ac3",
    "text": "hi",
    "attachment": {
        "type": "VIDEO",
        "assetId": null,
        "attachmentOptions": null,
        "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
        "urlHash": null,
        "previewUrl": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image_p.png",
        "hashedPreviewUrl": null,
        "title": null,
        "description": null,
        "mimeType": null,
        "closedCaptions": [],
        "thumbnails": null,
        "rate": null,
        "duration": null
    },
    "commentingUser": 66014658,
    "createdTime": 1744725033255,
    "modifiedTime": 1744725033255,
    "entityType": "CASE",
    "entityId": "123",
    "conversationId": null,
    "externalComment": null,
    "inReplyToCommentId": null,
    "private": null
}





### COMMENT_WITH_MULTIPLE_ATTACHMENTS


#### Request





  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/COMMENT' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Content-Type: application/json' \
--header 'Cookie: JSESSIONID=D6605664A6605E54E8331F6413B69425' \
--data '{
    "requestType": "COMMENT_WITH_MULTIPLE_ATTACHMENTS",
    "payload": {
        "entityId": "12232",
        "entityType": "CASE",
        "comment": "Add Comment Attachments on Case",
        "attachments": [
            {
                "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
                "previewUrl": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
                "type": "IMAGE"
            },
            {
                "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
                "previewUrl": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
                "type": "IMAGE"
            }
        ]
    }
}'





#### Response

      

{
    "id": "67fe64f1b588615185ee6b22",
    "text": "Add Comment Attachments on Case",
    "attachment": {
        "type": "MULTI_MEDIA",
        "assetId": null,
        "attachmentOptions": null,
        "attachments": [
            {
                "type": "IMAGE",
                "assetId": null,
                "attachmentOptions": null,
                "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
                "urlHash": null,
                "title": null,
                "description": null,
                "previewUrl": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
                "hashedPreviewUrl": null,
                "mimeType": null,
                "alternateText": null,
                "height": null,
                "width": null
            },
            {
                "type": "IMAGE",
                "assetId": null,
                "attachmentOptions": null,
                "url": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
                "urlHash": null,
                "title": null,
                "description": null,
                "previewUrl": "https://sprcdn-assets.sprinklr.com/787/aee8ce95-ef25-4365-a9d4-717a8a9f458e-780709975/test_image.png",
                "hashedPreviewUrl": null,
                "mimeType": null,
                "alternateText": null,
                "height": null,
                "width": null
            }
        ]
    },
    "commentingUser": 66014658,
    "createdTime": 1744725233883,
    "modifiedTime": 1744725233883,
    "entityType": "CASE",
    "entityId": "12232",
    "conversationId": null,
    "externalComment": null,
    "inReplyToCommentId": null,
    "private": null
}





### TASK


#### Request





  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/TASK' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Content-Type: application/json' \
--data '{
    "requestType": "TASK",
    "payload": {
        "taskType": "Design Task",
        "title": "SAM TASK via API2.02025-03-25 11:46:56.035",
        "description": "SAM TASK description via API2.0",
        "dueDate": 1594642560000,
        "taskStatus": "New",
        "assignment": {
            "assigneeId": "66000149",
            "assigneeType": "USER"
        },
        "assetId": "67e4d18d2caa57607600a975",
        "assetType": "MEDIA_ASSET"
    }
}'





#### Response

      

{
    "id": "67fe6560b588615185ee6b5e",
    "assignment": {
        "assigneeId": "66000149",
        "assigneeType": "USER",
        "assignedById": 66014658,
        "assignmentTime": null
    },
    "taskType": "Design Task",
    "taskStatus": "New",
    "title": "SAM TASK via API2.02025-03-25 11:46:56.035",
    "description": "SAM TASK description via API2.0",
    "assetId": "67e4d18d2caa57607600a975",
    "assetType": "SOCIAL_ASSET",
    "parentTaskId": null,
    "completionDate": null,
    "dueDate": 1594642560000,
    "customProperties": {
        "spr_task_status": [
            "New"
        ],
        "spr_task_type": [
            "Design Task"
        ]
    },
    "inactive": false,
    "nextTaskId": null,
    "attachment": null,
    "subscribers": null,
    "queueDetails": [],
    "createdTime": 1744725344190,
    "modifiedTime": 1744725344190,
    "workFlowState": null,
    "externalCases": []
}





### LISTENING_TOPIC


#### Request





  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/LISTENING_TOPIC' \
--header 'Accept-Encoding: gzip' \
--header 'Authorization: Bearer abnQ+7DK1gauzRr8ce/KAx++Xf24GBMSR32dgY9+svI5Mzc3YzI1Ny02NWZhLTMxNTgtOWEyNi0zYTFlYTkwODE4NWI=' \
--header 'Content-Type: application/json' \
--header 'Cookie: JSESSIONID=D6605664A6605E54E8331F6413B69425' \
--data '{
    "requestType": "LISTENING_TOPIC",
    "payload": {
        "name": "Customer Support",
        "displayName": "Api Topic44",
        "topicType": "QUERY_LISTENING",
        "description": "Created via Listening API",
        "topicGroupId": "67fe670fb0cde13474489bf6",
        "startDate": 1615140543000,
        "endDate": 1680065287000,
        "tags": [
            "API"
        ],
        "sources": [
            "TWITTER"
        ],
        "enabled": false,
        "query": "message: hello",
        "excludeRetweets": false,
        "matchQuotedRetweets": false,
        "excludePossiblySensitiveContent": false,
        "excludeUrlsInSearch": false,
        "onlyVerifiedUser": false,
        "clientId": 1,
        "partnerCustomProperties": {}
    }
}'





#### Response

      

{
    "id": "67fe6829b588615185ee6c50",
    "name": "Customer Support",
    "displayName": "Api Topic44",
    "topicType": "QUERY_LISTENING",
    "iconUrl": null,
    "imageUrl": null,
    "color": null,
    "description": "Created via Listening API",
    "topicGroupId": "67fe670fb0cde13474489bf6",
    "startDate": 1615140543000,
    "endDate": 1680065287000,
    "tags": [
        "API"
    ],
    "sources": [
        "TWITTER"
    ],
    "enabled": false,
    "query": "message: hello",
    "languageCodes": null,
    "countryCodes": null,
    "locations": null,
    "blockLocations": null,
    "blockedDomains": null,
    "blockedDomainsListIds": null,
    "blockedClientProfileLists": null,
    "blockedPartnerProfileLists": null,
    "blockedCountryCodes": null,
    "blockedLanguageCodes": null,
    "generatingSourceList": null,
    "generatingSources": null,
    "blockedGeneratingSourceList": null,
    "blockedGeneratingSources": null,
    "inclusiveDomains": null,
    "inclusiveDomainsListIds": null,
    "inclusiveClientProfileLists": null,
    "inclusivePartnerProfileLists": null,
    "accountIds": null,
    "accountGroupIds": null,
    "excludeRetweets": false,
    "matchQuotedRetweets": false,
    "excludePossiblySensitiveContent": false,
    "excludeUrlsInSearch": false,
    "excludeRevItemName": false,
    "onlyVerifiedUser": false,
    "minimumFollowerCount": null,
    "minimumMozRank": null,
    "maximumMozSpamScore": null,
    "maximumAlexaRank": null,
    "createdTime": 1744726056671,
    "modifiedTime": 1744726056671,
    "ownerUserId": 66014658,
    "lastModifiedUserId": 66014658,
    "clientId": 66000002,
    "dataVolumeThresholdApiConfig": null,
    "partnerCustomProperties": {},
    "clientCustomProperties": null,
    "customEntityTypeVsCustomEntityIds": null,
    "autoBackfill": false
}





### KEYWORD_GROUP


#### Request





  Copy Code



curl --location --request POST 'https://{env}-api2-v3.sprinklr.com/v3/api/entities/create/KEYWORD_GROUP' \
--header 'Accept-Encoding: gzip' \
--header 'Authorization: Bearer abnQ+7DK1gauzRr8ce/KAx++Xf24GBMSR32dgY9+svI5Mzc3YzI1Ny02NWZhLTMxNTgtOWEyNi0zYTFlYTkwODE4NWI=' \
--header 'Content-Type: application/json' \
--header 'Cookie: JSESSIONID=D6605664A6605E54E8331F6413B69425' \
--data '{
    "requestType": "KEYWORD_GROUP",
    "payload": {
        "name": "Deepak Api Testing v1",
        "description": "Testing new Keyword API",
        "conditions": [
            {
                "term": "Rolex",
                "distance": 4,
                "keywordType": "KEYWORD"
            }
        ],
        "tags": [
            "Watch",
            "TimePiece",
            "Handmade",
            "Iconic"
        ],
        "shareConfig": {
            "shareWithEveryOne": true
        },
        "permissionEntity": {
            "userIds": [
                66000101
            ],
            "userGroupIds": []
        }
    }
}'





#### Response

      

{
    "id": "67fe6d9bb588615185ee6de0",
    "name": "Deepak Api Testing v1",
    "description": "Testing new Keyword API",
    "conditions": [
        {
            "term": "Rolex",
            "distance": 0,
            "keywordType": "KEYWORD"
        }
    ],
    "conditionsUpdateType": null,
    "tags": [
        "Watch",
        "TimePiece",
        "Handmade",
        "Iconic"
    ],
    "shareConfig": {
        "userIds": null,
        "userGroupIds": null,
        "clientIds": null,
        "clientGroupIds": null,
        "shareWithEveryOne": true
    },
    "permissionEntity": {
        "userIds": [
            66000101
        ],
        "userGroupIds": null
    },
    "autoBackfillTopics": false
}





	 [](https://dev.sprinklr.com/create-v3)

[Back to top](https://dev.sprinklr.com/create-v3)
