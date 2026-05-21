---
title: "Jan - Mar 2025"
slug: jan-mar-2025
url: https://dev.sprinklr.com/jan-mar-2025
---

# Jan - Mar 2025

# Jan - Mar, 2025

## Sprinklr API Updates

Sprinklr is implementing the infrastructure updates as listed below:

**Important:**

These updates will only impact you if you are using Sprinklr APIs in your environment. If you are using standard Sprinklr connectors or integrations, there will be no impact, and no action is required on your part.

If you are using Sprinklr APIs, take note of the following updates:

### 1. API Domain Change

The current API domain (`api2.sprinklr.com`) is being updated to `api3.sprinklr.com`.

****
****

``
``

| Current Domain | New Domain |
| --- | --- |
| api2.sprinklr.com | api3.sprinklr.com |

**Action Required**: Update the domain in your API calls to `api3.sprinklr.com`.

**Note:** All paths and endpoints will remain the same. Therefore, no other changes are required apart from the domain update.

### 2. Authentication and Security Existing Credentials

Your current credentials (API keys, tokens, client IDs/secrets) will continue to work without modification.

**Action Recommended**: While existing credentials will remain valid, we recommend updating your token generation endpoints and respective authorization tokens as well

**Authentication Process**: The authentication process will remain unchanged.

### 3. Developer Portal

A new Developer Portal will be available starting December 7, 2024. You can access the new developer portal from [here](https://dev.sprinklr.com/)

**Action Required**: You will need to re-register using the same email address associated with the current portal.

**Note:** All your existing applications will be accessible in the new portal.

## Partial Updates for Universal Profile Fields

You can now partially update Universal Profile fields through the Sprinklr API, allowing more flexibility in managing data.


New Capabilities:


- **Partial Updates**: Update specific native or custom fields without overwriting all data.

- **Multi-Value Picklists**: Add or remove specific values from multi-value picklist fields.

Example: If a field contains X, Y, Z, you can add R, S or remove Z.

## Expanded Support for Missing Stream Types in Dashboard Read API


The [Dashboard Stream Read v2 API](https://dev.sprinklr.com/fetch-engagement-dashboards) now supports additional stream types to provide comprehensive access to data.

New Stream Types Added:


- MESSAGES

- BENCHMARKING_CONVERSATIONS

- INBOX Channels: APPLE_APP_STORE, ZENDESK, YOUTUBE, EMAIL, YELP

- GPLUS_BUSINESS_LOCATION_REVIEW

- LINKED_IN_COMPANY_INBOX


## Versioning Support in Asset APIs


Asset [Create](https://dev.sprinklr.com/create-asset), [Read](https://dev.sprinklr.com/read-asset), and [Update](https://dev.sprinklr.com/update-asset) APIs now support versioning to enhance content management. You can track and manage multiple versions of assets.

## Introducing Skill and Skill Category APIs

The new Skill and Skill Category APIs are introduced to manage agent skills and categories. With these APIs, you can get skills and skill categories details, create skills, create skill categories, and more.


### Endpoint Details:



- [Fetch Assignment Skill by Id](https://dev.sprinklr.com/fetch-assignment-skill-by-id)

- [Fetch Assignment Skill by Name](https://dev.sprinklr.com/fetch-assignment-skill-by-name)

- [Create Assignment Skill](https://dev.sprinklr.com/create-assignment-skill)

- [Update Assignment Skill](https://dev.sprinklr.com/update-assignment-skill)

- [Delete Assignment Skill](https://dev.sprinklr.com/delete-assignment-skill-by-id)

- [Fetch Assignment Skill Category by Id](https://dev.sprinklr.com/fetch-assignment-skill-category-by-id)

- [Fetch Assignment Skill Category by Name](https://dev.sprinklr.com/fetch-assignment-skill-category-by-name)

- [Create Assignment Skill Category](https://dev.sprinklr.com/create-assignment-skill-category)

- [Update Assignment Skill Category](https://dev.sprinklr.com/update-assignment-skill-category)

- [Delete Assignment Skill Category by Id](https://dev.sprinklr.com/delete-assignment-skill-category-by-id)



## Introducing Knowledge Base Webhooks

You can subscribe to the new Knowledge Base Webhooks to receive response when any content is created, updated, or deleted in the Knowledge Base. For more details, see [Knowledge Base Webhooks](https://dev.sprinklr.com/knowledge-base-webhooks).

## Introducing External Authentication Credential APIs

The External Authentication Credential APIs allow you to seamlessly create and delete external API credentials within Sprinklr, enabling secure integrations with third-party applications.


### Endpoint Details:



- [Create Basic Authentication Credentials](https://dev.sprinklr.com/create-basic-authentication-credentials)

- [Create OAuth Refresh Token Credentials](https://dev.sprinklr.com/create-oauth-refresh-token-credentials)

- [Create Password Authentication Credentials](https://dev.sprinklr.com/create-password-authentication-credentials)

- [Create Client Credentials](https://dev.sprinklr.com/create-client-credentials)

- [Create OAuth 1.0 Credentials](https://dev.sprinklr.com/create-oauth-1-0-credentials)

- [Create JWT Credentials](https://dev.sprinklr.com/create-jwt-credentials)

- [Create Custom Authentication Credentials](https://dev.sprinklr.com/create-custom-authentication-credentials)

- [Create API Key Credentials](https://dev.sprinklr.com/create-api-key-credentials)

- [Delete External Authentication Credentials](https://dev.sprinklr.com/delete-external-authentication-credentials)



## Introducing CFM Workflow API


The CFM Workflow API allows you to create or update customer profiles and utilize the provided parameters to trigger personalized survey distributions via Email, SMS, or WhatsApp. This enables seamless and targeted customer feedback collection based on specific events.


### Endpoint Details:

	[CFM Workflow API](https://dev.sprinklr.com/cfm-workflow-api)

[](https://dev.sprinklr.com/jan-mar-2025)

[Back to top](https://dev.sprinklr.com/jan-mar-2025)
