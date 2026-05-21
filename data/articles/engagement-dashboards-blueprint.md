---
title: "Engagement Dashboards - Blueprint"
slug: engagement-dashboards-blueprint
url: https://dev.sprinklr.com/engagement-dashboards-blueprint
---

# Engagement Dashboards - Blueprint

# Engagement Dashboards - Blueprint

	Engagement or monitoring dashboards offer a customized view of inbound and outbound messages across social channels and the associated metadata. This data is organized into columns where you can view, edit, export, share, respond and perform other supported actions.

## Engagement Dashboard - Basics

### What is a Column?

[Engagement dashboard](https://www.sprinklr.com/help/articles/getting-started-with-social-engagement/create-a-workflow-column/641beadf55c4c33ae8b81420) content is organized and displayed in the form of columns. Each column's content depends on its configuration and the selected source. Two types of columns are supported within Sprinklr, i.e., an outbound and an inbound column.

### What is a Stream?

Stream refers to the data that resides within each of the columns. These data streams reside within the configured columns and can be fetched using the unique stream Id associated with the column.

## Things to Know in Advance

- Engagement dashboards are distinguishable based on one or more columns of data

- Each column offers a visualization of channel-based messages and their metadata

- Every engagement dashboard has its unique name and id to help differentiate it from others

- The engagement dashboard offer loosely coupled integration, i.e., any change in the column filter would reflect in the exported dashboard data

- Dashboard and column Ids are consistent across production and Sandbox environments

## Pulling Engagement Dashboard Data Using APIs

- Registering on Sprinklr’s [developer portal](https://dev.sprinklr.com/developer-portal-registration) is the first step toward establishing an API connection

- You can generate an API key using the steps mentioned in the [Getting Started guide](https://dev.sprinklr.com/getting-started)

- For authentication token generation, use either of the following methods:

- [OAuth 2.0 for Customers](https://dev.sprinklr.com/oauth-2-0-for-customers)

- [Client Credentials Grant Type](https://dev.sprinklr.com/client-credentials-get)

- [Certificate-Based Token Generation](https://dev.sprinklr.com/jwt-token-generation)

## Engagement Dashboard: Workflow

### 1. Configure Engagement Dashboard

Creating an engagement dashboard and configuring the columns within the dashboard is the first step for visualizing the messages on Sprinklr's platform.

### 1.1 Create Engagement Dashboard

You can create an engagement dashboard from the Modern Engagement module within the Sprinklr platform.

**Related Knowledgebase Article**: [How to Create an Engagement Dashboard](https://www.sprinklr.com/help/articles/getting-started-with-social-engagement/what-can-you-do-with-engagement-dashboards/6450dc2fd85662201933c821)?

### 1.2 Create Engagement Dashboard Column

Once the engagement dashboard is created, you can add a column based on the desired source.

**Related Knowledgebase Article**: [How to Add an Engagement Dashboard Column](https://www.sprinklr.com/help/articles/getting-started-with-social-engagement/create-a-workflow-column/641beadf55c4c33ae8b81420)?

## 2. Fetch Engagement Dashboard Details

You can fetch the engagement dashboard details using the following APIs:

### 2.1 Fetch All Engagement Dashboards

Using this API, you can fetch details for all the engagement dashboards configured in your Sprinklr environment.

**Related Dev Portal Documentation**: Fetch All Engagement Dashboards

### 2.2 Fetch Engagement Dashboard

Using this API, you can fetch the details for a specific engagement dashboard using the dashboard name.

**Dev Notes: **The dashboard name should be `URL-encoded`.

**Related Dev Portal Documentation**: Fetch Engagement Dashboard

### 3. Fetch Column Stream

Once you have the engagement dashboard details, you can fetch the column data using stream Id.

### 3.1 Fetch Outbound Column

Using this API, you can fetch the data from within an outbound column for the given stream Id. For fetching the stream Id, refer to Read Dashboard API.

**Related Dev Portal Documentation**: Fetch Outbound Column Stream

### 3.2 Fetch Inbound Column

Using this API, you can fetch the data within an inbound column for the given stream Id. For fetching the stream Id, Read Dashboard API.

**Related Dev Portal Documentation**: Fetch Inbound Column Stream

### 3.3 Fetch Stream Using Cursor

Using this API, you can fetch the next set of results for both the inbound and outbound column responses. To obtain a successful response, you can pass the “nextPageCursor” field value as a path parameter in this API call.

**Related Dev portal Documentation**: Stream Cursor API

### 3.4 Fetch Case Stream

Using this API, you can fetch the messages associated with a case from an engagement dashboard for the given streamId. You can refer to Read Dashboard API for fetching the stream Id.

**Related Dev Portal Documentation**: Fetch Case Stream

Dev Note: This will return all the case-level stream data where the selected column source is “`Case Management`.”

## FAQs - Engagement Dashboards

### 1. How to Identify Stream Id from the Read Dashboard API Response?

Look for the following parameters in the read dashboard by name API response:

- **columnOrder**: List of all stream Ids for the columns in the dashboard

- **columns**: Array containing the individual stream Ids under the “Id” field

### 2. What is the Flow of APIs for Extracting Engagement Dashboard Data?

The complete flow for extracting engagement dashboard data includes calling the following APIs:

- **Fetch Engagement Dashboards**: for extracting names for all the dashboards configured in the Sprinklr environment

- **Fetch Engagement Dashboard Using Dashboard Name**: for fetching all the details of an engagement dashboard using its name

- **Fetch Outbound Stream**: for fetching the message metadata for an outbound column using stream Id

- **Fetch Inbound Stream**: for fetching the message metadata for an inbound column using stream Id

- **Fetch Case Stream**: for fetching the message metadata for columns where the configured source is "case management."
[](https://dev.sprinklr.com/engagement-dashboards-blueprint)

[Back to top](https://dev.sprinklr.com/engagement-dashboards-blueprint)
