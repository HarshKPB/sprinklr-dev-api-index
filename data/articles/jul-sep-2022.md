---
title: "Jul - Sep, 2022"
slug: jul-sep-2022
url: https://dev.sprinklr.com/jul-sep-2022
---

# Jul - Sep, 2022

# Jul - Sep, 2022

**Developer Note:**
We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.
Please note that the API base endpoint has changed from `api2` to `api3`.
For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## ****Fetch Report Names -  Sep  21st, 2022

Using this API, you can fetch the report names associated with the given reporting engine Id.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/reports/reports/{reportingEngineId}

## **BETA** - Create Knowledge Base Article -  Sep 9th, 2022

Using this API, you can create a knowledge base article within Sprinklr.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/knowledgebase/create


## ****BETA - Update Knowledge Base Article -  Sep 9th, 2022

Using this API, you can update a knowledge base article within Sprinklr.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/knowledgebase/update


## ****BETA - Delete Knowledge Base Article -  Sep 9th, 2022

Using this API, you can delete a knowledge base article within Sprinklr.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/knowledgebase/delete


## ****BETA - Create Support Ticket -  Sep 2nd, 2022

Using this API, you can create support tickets and register cases in Sprinklr Care Lite.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/support-ticket/create-case


## ****BETA - Fetch Support Case Custom Fields -  Sep 2nd, 2022

Using this API, you can fetch the custom fields defined for an existing support case.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/support-ticket/case-custom-fields

## ****Fetch Accessible Workspaces -  Sep 1st, 2022

Using this API, you can fetch the details of all the workspaces the user has access to, with respect to the partner Id for which the token was generated.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/client/accessible-clients


## ****BETA - Advocacy Community - Fetch Project Id -  Aug 31st, 2022

Using this API, you can find the project Id for the advocacy community instance using the unique project key.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/xb-community/projectId/{projectKey}


## ****BETA - Advocacy Community - Fetch Screener Questions -  Aug 31st, 2022

Using this API, you can find all the screener questions defined for a community project.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/xb-community/screener/{projectId}



## ****BETA - Advocacy Community - Fetch Screener Answers -  Aug 31st, 2022

Using this API, you can find the answers for the screener questions using the unique screen question Ids.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/xb-community/screener-answer



## ****BETA - Advocacy Community - Find Users Using Project Id -  Aug 31st, 2022

Using this API, you can find advocacy community users using the unique projectId.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/xb-community/find/users/{projectId}


## ****BETA - Advocacy Community - Update User -  Aug 31st, 2022

Using this API, you can update information for the given community user Id.

**API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/xb-community/update/user/{communityUserId}


## ****Create Custom Entity Trigger - Aug 26th, 2022

Using this API, you can create a trigger configuration for a custom entity.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/custom-entity/trigger


## ****Fetch Custom Entity Trigger - Aug 26th, 2022

Using this API, you can fetch the custom entity trigger details using the unique reference id for the trigger.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/custom-entity/trigger/{Id}



## ****Fetch All Custom Entity Triggers - Aug 26th, 2022

Using this API, you can fetch all the configured custom entity triggers for a given trigger type.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/custom-entity/triggers/{entityType}/{triggerType}



## ****Enable Custom Entity Trigger - Aug 26th, 2022

Using this API, you can enable the custom entity trigger for the given trigger id.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/custom-entity/trigger/{id}/enable



## ****Disable Custom Entity Trigger - Aug 26th, 2022

Using this API, you can disable the custom entity trigger for the given trigger id.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/custom-entity/trigger/{id}/disable



## ****Update Custom Entity Trigger - Aug 26th, 2022

Using this API, you can update the trigger configuration for a given trigger id.

**API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/custom-entity/trigger/{id}



## ****Delete Custom Entity Trigger - Aug 26th, 2022

Using this API, you can delete the trigger configuration of a custom entity for the given trigger id.

**API Endpoint**

DELETE https://api2.sprinklr.com/{env}/api/v2/custom-entity/trigger/{id}



## ****Fetch Custom Entity - Aug 26th, 2022

Using this API, you can fetch the custom entity details using the entity type and the entity id.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/custom-entity/entity/{entityType}/{entityId}



## ****Delete Custom Entity - Aug 26th, 2022

Using this API, you can delete the created custom entity details using the entity type and the entity id.

**API Endpoint**

DELETE https://api2.sprinklr.com/{env}/api/v2/custom-entity/entity/{entityType}/{entityId}



## ****Fetch Reporting Engines - Aug 25th, 2022

With this API, you can fetch all the supported reporting engines for reporting insights.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/reports/engines



## ****BETA - Source Agnostic - Send Message - Aug 24th, 2022

Source agnostic import message API allows importing third-party bot messages to Sprinklr.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/source-agnostic/{accountId}/send



## ****BETA - Source Agnostic - Close Conversation - Aug 24th, 2022

Source Agnostic close conversation API allows closing the conversation using the unique conversation Id.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/source-agnostic/closeConversation?conversationId={conversationId}



## ****Fetch Custom Field Using Field Name- Aug 22nd, 2022

This API call helps in fetching the custom field details using the corresponding field name.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/custom-field/{customFieldName}



## ****Update Custom Field- Aug 22nd, 2022

This API call helps update the custom field using the unique field id.

**API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/custom-field/{customFieldId}



## **Recommendation Webhooks**- Aug 12th, 2022

Recommendation webhooks subscription allows receiving nudges for Agent Assist widget in real-time. By subscribing to a recommendation webhook, you ensure reminders are sent to the agents that help them resolve customer queries effectively and in a timely manner.

**Payload Details**

Refer to [Recommendation Webhooks](https://developer.sprinklr.com/docs/read/webhooks/webhook_response_payload/Recommendation_Webhook) documentation



## **Create/Update Lead Event**- Aug 1st, 2022

This API call helps create and update lead events.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/dmp/lead/{sourceId}



## **Create/Update Bulk Lead Events**- Aug 1st, 2022

This API call helps create and update bulk lead events.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/dmp/lead/{sourceId}/bulk



## **Create/Update Lead**- Aug 1st, 2022

This API call helps create lead based on the information passed in the request payload.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/dmp/audience-lead



## **Update Agent Status**- Aug 1st, 2022

This API call helps update the availability status of the customer service agent.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v1/user/update/user/status



## **Journey Facilitator - For Existing Profile** - Aug 1st, 2022

With this API, you can trigger customer journey for an existing customer profile.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/marketing-journey/trigger



## **Journey Facilitator - For New Profile**- Aug 1st, 2022

This API helps create a new profile and triggers the customer journey based on given information.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/marketing-journey/triggerWithNewProfile



## **Create Custom Entity Definition** - July 25th, 2022

Using this API call, you will be able to create a custom entity definition.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/custom-entity/definition



## **Fetch Custom Entity Definition** - July 25th, 2022

This API call helps in fetching the configured definition for the given entity Id.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/custom-entity/definition/{entityDefinitionId}



## **Update Custom Entity Definition**- July 25th, 2022

This API call will help you update an existing custom entity definition using the entity definition Id.

**API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/custom-entity/definition/{entityDefinitionId}



## **Create Custom Entity Field** - July 25th, 2022

This API call helps create the corresponding fields for the created custom entity definition.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/custom-entity/field



## **Fetch Custom Entity Fields** - July 25th, 2022

This API call helps in fetching all the fields for the given entity definition Id.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/custom-entity/fields/{entityType}



## **Update Custom Entity Fields**- July 25th, 2022

Using this API, you can update a particular field within the custom entity

**API Endpoint**

PATCH https://api2.sprinklr.com/{env}/api/v2/custom-entity/entity/{entityType}/{entityId}



## **Create Custom Entity** - July 25th, 2022

This API helps create the values for the different fields of the custom entity i.e., it helps store the data that is being collected for different custom entity fields.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/custom-entity/entity



## **Update Custom Entity**- July 25th, 2022

This API helps update the values for the different fields of the custom entity i.e., it helps update the stored data for different custom entity fields.

**API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/custom-entity/entity/{entityId}



## **Bulk Media Upload** - July 15th, 2022

This API allows uploading media in bulk to Sprinklr's content store.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/media/upload/multiple

## **Dark Post Support in Publishing API** - July 15th, 2022

Support for dark post has been added to the Publishing Post API. By setting `darkPost=True`, you can create ads to target different audiences without publishing the content to the page.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/post

## **Fetch Skills and Proficiency** - July 15th, 2022

This API call allows you to fetch the skill id and proficiency score of an agent.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/user-settings/assignment-config/{userId}

## **Update Proficiency/Remove Skills** - July 15th, 2022

Uisng this API, you will be able to update the proficiency score of the user/agent and remove the skills of the user/agent.

**API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/user-settings/assignment-config/{userId}

## **Tag People on Instagram Images** - July 15th, 2022

Using this API call, you will be able to tag people/accounts on Instagram images while publishing a post.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/post

## **User Search by Custom Field**- July 15th, 2022

You can now use this API to search users based on the given custom field values. Support for using "USER" as an entity type has also been made available.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/search/{entityType}

[](https://dev.sprinklr.com/jul-sep-2022)

[Back to top](https://dev.sprinklr.com/jul-sep-2022)
