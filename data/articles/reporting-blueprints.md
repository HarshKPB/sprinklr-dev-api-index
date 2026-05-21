---
title: "Reporting Blueprints"
slug: reporting-blueprints
url: https://dev.sprinklr.com/reporting-blueprints
---

# Reporting Blueprints

#
  Reporting Blueprint

Reporting is a fundamental feature available across all Sprinklr products that help visualize data through standard and custom dashboards. These dashboards provide a birds-eye view of data collected from social media and messaging accounts such as mentions, followers, comments, shares, messages, etc.

By leveraging reporting data sourced from Sprinklr, you can store, centralize, and visualize data, which, in turn, helps make informed decisions.

One of the most common methods for exporting data from within dashboard and widgets is through Reporting APIs. The objective of this article is to walk you through the process and best practices for using Reporting APIs.

## Reporting: Basics

Before getting started with Reporting APIs, let's discuss reporting dashboards and widgets.

### What is a Reporting Dashboard?

Reporting dashboards are a collection of widgets that helps centralize and visualize trends/insights across digital channels. The visualization of data makes it easy to analyze data and gather insights that are critical for improving your bottom line.

**Related Article**: [How to Create a Reporting Dahboard?](https://www.sprinklr.com/help/articles/configure-reporting/widget-configuration-in-reporting/63d4ce252c015d03d4e7fe37)

### What is a Widget?

Widgets are building blocks of a dashboard that visualize data based on the selected metrics and dimensions. For instance, you could create one widget for mentions, one for post likes, or one for engagement by media type. The visualization of every widget depends on the filters applied to it.

**Related Article**: [How to Create a Reporting Widget?](https://www.sprinklr.com/help/articles/configure-reporting/widget-configuration-in-reporting/63d4ce252c015d03d4e7fe37)

### Getting Started With Reporting APIs

Here’s what to know in advance when getting started with reporting APIs:

- To export data using Reporting API, you may require use case approval from social providers.

- You will require the right permissions to view and access reporting dashboards. Refer to Reporting Permissions knowledge base article for more information.

- Before exporting data through APIs, it is essential to create a dashboard and respective widgets on the Sprinklr platform UI. This will give you direct access to the request necessary to make the API call and allow you to validate the exported data

- Next, [register](https://dev.sprinklr.com/create) on the Sprinklr Developer Portal to generate an application. This will create an API key that can be used to generate an authorization token used to make reporting API calls. Refer to [Getting Started](https://dev.sprinklr.com/getting-started) and [Oauth 2.0 for Customers](https://dev.sprinklr.com/oauth-2-0-for-customers) to create application and generate token, respectively.

- Once the key and authorization token are generated, make a call using the “ME” endpoint. This helps validate that the key and token works as expected.

- The next step is to retrieve the request payload for the widgets created in step 3. The payload will be used in the Reporting API request body. The request payload can be generated from the UI if the correct permissions are assigned to the logged-in user. The steps to add the permissions needed to retrieve the payload are detailed in the next section.

- Once the key, token, and request payload are in place, you can make your first reporting API call. There are a few options that can be modified as well in the request payload that will alter the response. These are also documented below.

### Reporting API Workflow

Follow the steps listed below for running a successful reporting API call:

#### 1. Create Dashboard and Widget

Create a reporting dashboard and respective widgets. Configure the widgets using the right filters for dimensions and metrics

#### 2. Enable Generate API Payload Permission

The steps to accomplish this are listed below. Please skip this if you already have the necessary permissions.

- Navigate to the Governance Console and click All Settings within Platform Modules/Listen.

- In the Platform Settings window, select Workspace Roles or Global Roles within Manage Workspace or Manage Customer, respectively.

- In the top right corner of the Roles (Settings) window, click Create Role.

- Provide the basic information such as the name and description of the role. Add the users or user groups you want to provide access to.

- Under Role Permissions, search and select 'Generate Widget API Payload' and click Save in the bottom right corner

#### 3. Copy API Payload

- On the Reporting Home window, select the desired dashboard you wish to generate the API Payload from

- Click on three dots placed in the top right corner of the widget

- Select Generate API v2 Payload from the drop-down menu

- Click on copy code from the pop-up window that appears

#### 4. Make your First API Call

- Use the Reporting API endpoint and paste the copied payload into the body

- Configure the API key and the authorization token in the headers

- You can modify the startTime, endTime, pageSize, and page parameters based on your requirements

- Once configured, make the API call to fetch the desired response

### Sample API Request




  Copy Code



curl -X POST \\
  'https://api3.sprinklr.com/{{env}}/api/v2/reports/query' \
  -H 'Authorization: Bearer {{Enter your Access Token}}' \
  -H 'Key: {{Enter your API KEY}}' \
  -H 'Content-Type: application/json' \
  -d '{
    "reportingEngine": "OUTBOUND_MESSAGE",
    "report": "OUTBOUND_MESSAGE",
    "startTime": "1569436200000",
    "endTime": "1572028199999",
    "timeZone": "Asia/Kolkata",
    "pageSize": "20",
    "page": "0",
    "groupBys": [
        {
            "heading": "POST_ID",
            "dimensionName": "POST_ID",
            "groupType": "FIELD",
            "details": null
        },
        {
            "heading": "CAMPAIGN_ID",
            "dimensionName": "CAMPAIGN_ID",
            "groupType": "FIELD",
            "details": null
        },
        {
            "heading": "ACCOUNT_ID",
            "dimensionName": "ACCOUNT_ID",
            "groupType": "FIELD",
            "details": null
        }
    ],
    "projections": [
        {
            "heading": "TOTAL_ENGAGEMENT",
            "measurementName": "TOTAL_ENGAGEMENT",
            "aggregateFunction": "SUM"
        }
    ],
   "projectionDecorations": [],
    "additional": {
        "dashboardWidget": "true",
        "moduleType": "LISTENING",
        "widgetId": "63484770884c47394c33cac5",
        "exportInfo": "false",
        "dashboardId": "6348476e884c47394c33c979",
        "engine": "LISTENING",
        "showTotal": "true",
        "chartType": "TABLE",
        "showRolloverTrends": "true",
        "TABULAR": "true",
        "option": "CUSTOM"
    },
    "skipResolve": false,
    "jsonResponse": false
}'




## Reporting APIs: Frequently Asked Questions (FAQs)

### 1. Do you have to generate API v2 payload for every widget within a dashboard?

Yes, a separate API payload needs to be generated for every widget within the dashboard.

### 2. Are There any Limitations on page size and page number?

The page size limitations vary from partner to partner. Exceeding the maximum page size will throw a “400 Bad request” error.

It is recommended to try and keep the pageSize and Page details constant when fetching large volumes of data. To fetch the next page details, you can play with startTime and endTime. For accuracy and to prevent duplicate or missing records, keep the startTime and endTime gap minimal, i.e., 5 hours, or even one day, i.e., 24 hours.

### 3. Are There Alternatives for Exporting Data?

You can also export reporting data using one of the following methods:


- Direct exports from the widget using “Export Widget” option from the drop-down menu

- Business intelligence tools such as Power BI or Tableau

- Dump large-scale historical data, using CSV or Excel file in FTP or S3 buckets, which gets automatically executed on a scheduled basis. However, it might require a week’s time to execute the export successfully. Note that `100M messages` is the maximum limit for exporting data through S3 buckets.

### 4. How Do you Know How Many Times to Call the API to Fetch All the Data?

Check for the "hasMore" flag at the end of every response. If hasMore is true, it implies that more data rows are present; if false, it means the end of results.

### 5. Can you Use UI Generated API payload for both the v1 and v2 Reporting endpoint?

You can certainly use the UI-generated API payload for both the v1 and v2 reporting endpoints. However, we’d recommend you use the latest version v2 endpoint.

- Reporting API - v1 endpoint

- Reporting API - v2 endpoint

### 6. What are Some Reasons for Data Mismatches on UI and Reporting API Responses?


-

There can be cases where the authorization token generated might not have access to all the clients (workspaces). So, when a user makes an API call for a dashboard existing in an unauthorized workspace, they might be unable to pull accurate data.

    **Resolution:** Give permission to the right clients (workspaces) that have the required access to pull data from dashboards.


-

The pageSize configuration might be lower than required to pull the entire dashboard data. For instance, if the pageSize is set at 20, you’ll be able to fetch 20 rows of data from the widget.

    **Resolution:** Ensure that the pageSize is increased based on the rows of data you want to fetch. However, the pageSize should not be greater than 1000 as this might lead to frequent gateway timeout errors due to the load on the server.


### 7. What is Twitter Syndication and how Does it Relate With Reporting APIs?

To export Twitter data through Reporting APIs, customers require to seek use-case approval from Twitter. Once you have the approval, raise the request with your success manager to get “Twitter Resyndication” enabled for your environment. If the approval is missing, the API response will reflect incomplete or no data at all and you are likely to see the following error in the response: `"apiStatus": "Removed fields because of resyndication policy"`

**Dev Notes: **
Kindly note that Twitter syndication approval is on hold as Twitter (X) isn't accepting any approval requests currently.
 Additionally, X does not allow redistribution of content via automated means.

### 8. What is the Epoch Format for startTime and endTime Fields?

The epoch timestamp for startTime and endTime needs to be in milliseconds.

### 9. How to do Mapping for Custom Properties in the API Response Against the UI Column Names?

Copy the custom property field name from the API request and use "fetch custom field using field name" API to fetch the label for that custom field.

### Sample API Request



 Copy Code

        "heading": "UNIVERSAL_CASE_CUSTOM_PROPERTY_1",
        "dimensionName": "UNIVERSAL_CASE_CUSTOM_PROPERTY",
        "groupType": "FIELD",
        "details": '{
            "srcType": "CUSTOM",
            "fieldName": "5de864ab7c30ea309500d73c",
            "isSecureField": false }'


### Sample API Request




 Copy Code



curl -X GET \
 'https://api3.sprinklr.com/{{env}}/api/v2/custom-field/5de864ab7c30ea309500d73c' \
  -H 'Authorization: {{Bearer Enter your Access Token}}' \
  -H 'Key: {{Enter your API KEY}}' \
  -H 'accept: application/json'



### 10. What Does skipResolve Field Imply?

skipResolve is a boolean parameter available in the request payload and can be modified based on one's requirements. This field controls if certain fields are expanded into objects or are displayed as references to the respective objects.

### 11. What does jsonResponse Field Imply?

jsonResponse is a boolean parameter available in the request payload and can be modified based on one's requirements. This field controls if the data is returned in as an array of values or an array of JSON objects.

### 12. What is the Difference between projections and groupBys in the Reporting Request Payload?

Projections refer to the configured metrics in the widget. On the other hand, groupBys refer to the configured dimensions.

### 13. Do you Have to Update the Payload If you Modify any Metric/Dimension on the Widget?

Yes, you'll have to update the widget if any changes are made to the metrics/dimensions on the widget. This ensures that the API returns the updated data.
However, if you do not want to go through the hassle of updating the payload every time any metrics/dimensions are modified, you can use "Custom Query Using Widget Id" endpoint. This API makes the query using widget Id and eliminates the need to update the payload every time any changes are made to the widget.

### Sample API Request




  Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{{env}}/api/v2/reports/query/{{widgetId}}' \
  -H 'Authorization: Bearer {{Enter your Access Token}}' \
  -H 'Key: {{Enter your API KEY}}' \
  -H 'Content-Type: application/json' \
  -d '{
    "startTime": 1684261800000,
    "endTime": 1684348199999,
    "page": 0,
    "pageSize": 10,
    "skipResolve": false,
    "jsonResponse": true,
    "interval": "5d",
    "timeZone": "Asia/Kolkata"
}'




### 14. What are Batch Queries?

Batch query implies pulling dimensions and metrics from more than one report types. Request payload fro batch query will have a “collate” field at the top.


### Sample API Request




 Copy Code



curl -X POST \
   'https://api3.sprinklr.com/{{env}}/api/v2/reports/batchQuery' \
  -H 'Authorization: Bearer {{Enter your Access Token}}' \
  -H 'Key: {{Enter your API KEY}}' \
  -H 'Content-Type: application/json' \
  -d '{
    "collate": false,
    "requests": {
        "req2": {
            "report": "POST_INSIGHTS",
            "reportingEngine": "PLATFORM",
            "timeField": null,
            "startTime": 1648665000000,
            "endTime": 1651256999999,
            "timeZone": "Asia/Kolkata",
            "page": 0,
            "pageSize": 20,
            "filters": null,
            "groupBys": null,
            "projections": [
                {
                    "heading": "M_POST_INSIGHTS_TWITTER_IMPRESSIONS_0",
                    "measurementName": "TWITTER_IMPRESSIONS",
                    "aggregateFunction": "SUM",
                    "details": {}
                }
            ],
            "projectionDecorations": [],
            "projectionFilters": null,
            "sorts": [
                {
                    "heading": "TWITTER_MENTIONS__SUM__ACCOUNT_INSIGHTS",
                    "order": "DESC"
                }
            ],
            "streamRequestInfo": null,
            "additional": {
                "translateResponse": "false",
                "dashboardId": "623df6a297ce7f74aa32d143",
                "engine": "PLATFORM",
                "widgetId": "6256a8b9c5cf6913875f45a0",
                "showTotal": "false",
                "Currency": "DEFAULT",
                "chartType": "TABLE",
                "showRolloverTrends": "true",
                "TABULAR": "true"
            },
            "skipResolve": false,
            "jsonResponse": false
        },
        "req1": {
            "report": "ACCOUNT_INSIGHTS",
            "reportingEngine": "PLATFORM",
            "timeField": null,
            "startTime": 1648665000000,
            "endTime": 1651256999999,
            "timeZone": "Asia/Kolkata",
            "page": 0,
            "pageSize": 20,
            "filters": null,
            "groupBys": null,
            "projections": [
                {
                    "heading": "M_ACCOUNT_INSIGHTS_TWITTER_MENTIONS_0",
                    "measurementName": "TWITTER_MENTIONS",
                    "aggregateFunction": "SUM",
                    "details": {}
                }
            ],
            "projectionDecorations": [],
            "projectionFilters": null,
            "sorts": [
                {
                    "heading": "TWITTER_MENTIONS__SUM__ACCOUNT_INSIGHTS",
                    "order": "DESC"
                }
            ],
            "streamRequestInfo": null,
            "additional": {
                "translateResponse": "false",
                "dashboardId": "623df6a297ce7f74aa32d143",
                "engine": "PLATFORM",
                "widgetId": "6256a8b9c5cf6913875f45a0",
                "showTotal": "false",
                "Currency": "DEFAULT",
                "chartType": "TABLE",
                "showRolloverTrends": "true",
                "TABULAR": "true"
            },
            "skipResolve": false,
            "jsonResponse": false
        }
    }
}'




#### Best Practices

- Register for the Developer Portal, and authorization tokens using a service user which is not tied to a particular user. Contact the Success Manager for support in creating a “Service Account” user. Note that a working email address is required.

- Ensure that the Generate API v2 payload permission is enabled for the logged-in / service account Sprinklr user.

- Ensure that the change permissions on a dashboard are limited to prevent any unintended changes to the widgets.

- Use table or postcard type of visualization for insights into numeric and textual data as it helps validate the exported data through Reporting API.

- Ensure the right filters, i.e., metrics and dimensions, are chosen while configuring the dashboard. This is because the API will only return the data configured in the widget you generate the API payload for. Note that dashboard level filters will not be reflected in the payload that is generated.

### Appendix: Reporting APIs

- **Reporting Overview**: Provides an overview of what reporting is and how it works

- **Custom Query**: This helps fetch data available in the widget you generate the API payload for

- **Custom Query Using Widget Id**: This helps fetch data available in the widget for the given widget Id. You do not have to update the widget every time any metric/dimension is changed when using this API.

- **Batch Query**: This helps pull data from widgets that support metrics and dimensions coming from multiple reports.

- **Fetch Reporting Engines**: This helps fetch all the supported reporting data sources for reporting insights

- **Fetch Report Names**: This helps fetch the report name associated with the given reporting engine Id.

- **Read Dashboard List**: This gives the list of Sprinklr reporting and listening dashboards along with the associated metadata
 [](https://dev.sprinklr.com/reporting-blueprints)




[Back to top](https://dev.sprinklr.com/reporting-blueprints)
