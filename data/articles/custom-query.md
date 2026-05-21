---
title: "Custom Query"
slug: custom-query
url: https://dev.sprinklr.com/custom-query
---

# Custom Query

#
POST Custom Query

Reporting API helps you in getting the reporting data which will help you analyze your business on the web. You can use the data to understand traffic, analyze patterns, find out how popular a specific content is, or compile information to make future strategies for the business.

**Help Resource:** **[Reporting Blueprint](https://dev.sprinklr.com/reporting-blueprints)**

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/reports/query

### Headers

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

**Dev Notes: **You can extract the API request payload from the reporting widget in the UI, using "[Generate API v2 Payload](https://help.sprinklr.com/articles/integration-guides/generate-api-v2-payload/613767325f2e7c0c9ed36f2b)" option. Once extracted, copy the payload and use it in the request body of the API call as is.

### Request Parameters







-
-
-

-
-
-

-
-
-

-
-
-

-
-
-

-
-
-

``

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| reportingEngine | Required | Copy exact value from the UI payload. | String |
| report | Required | This defines the type of the report, copy the value from the UI payload. | String |
| startTime | Required | This should be in milliseconds format. e.g 1541529000000 | Integer,  UNIX timestamp (milliseconds) |
| endTime | Required | This should be in milliseconds format. e.g 1544120999999 | Integer,  UNIX timestamp (milliseconds) |
| timeZone | Required | Copy exact value from the UI payload. | String |
| pageSize | Required | Specifies the number of rows to be pull in the single API call, it matches the numbers of rows visible in the widget for each page. | Integer |
| page | Required | Specifies the page number, if total records are 100 & pageSize is 20, to pull the complete data through API make five API call with different page numbers. | Integer |
| groupBys  Heading dimensionName groupType | Required | Any value which defines the data. Name of the dimension, this should match exactly “group by” field from UI payload e.g "field": "SN_CREATED_TIME" will change to    "dimensionName": "SN_CREATED_TIME". Defines the type of group, copy value exactly from the UI Payload | Array |
| projections  Heading measurementName aggregateFunction | Required | Any string value which defines the data.  Contains exact value for measurement field from UI payload e.g "measurement": "MENTIONS_COUNT" will change to    "measurementName": "MENTIONS_COUNT".  Copy exactly from the UI payload. | Array |
| Filters  dimensionName filterType Values:[] | Required | Copy exact value of UI filter “fields”e.g   "field": "LST_THEME_TAG"  will change to "dimensionName": "LST_THEME_TAG". Defines the type of the filter applied, the value should match exactly the UI payload filterType. These are filter values, copy them exactly from UI payload. | Array |
| sorts | Optional | sorting information | List<ExternalSort> |
| projectionDecorations | Optional | CHANGE, PERCENTAGE_CHANGE, PERCENTAGE | List<String> |
| jsonResponse | Required | true, to get the industry standard structured response. "jsonResponse":true | Boolean |
| additional | Optional | Report dimensions are automatically resolved to include additional information: 					CASE or ASSOCIATED_CASE: Case description will be added. 					Adding "SKIP_RESOLVER":true will suppress the said resolution. | Object |

**External Filter:**







| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| dimensionName | Required | attribute getting filtered | String |
| filterType | Required | Supported filterTypes are: IN, GT, GTE, LT, LTE, NIN, BETWEEN, STARTS_WITH, CONTAINS, EQUALS , FILTER, EXISTS | String |
| values | Optional | values getting compared against | List<Object> |
| details | Optional | additional information as required | Object |

**External Group:**







| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| heading | Required | string value to be used as the key in the response | String |
| dimensionName | Required | attribute used for groupBy | String |
| groupType | Required | Supported groupTypes are: DATE_HISTOGRAM, TIME_OF_DAY, DAY_OF_WEEK, MONTH_OF_YEAR, FIELD | List<Object> |
| details | Optional | additional information as required | Object |

**External Projection:**







| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| heading | Required | string value to be used as the key in the response | String |
| mesurementName | Required | measurement for the report | String |
| aggregateFunction | Required | Supported functions are: SUM, AVG, MIN, MAX, STATS | String |
| details | Optional | additional information as required | Object |

**Dev Notes: ** To get response as per industry standards, please keep the value of `"jsonResponse"`:`true`


## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/reports/query' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
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
    "filters": [
        {
            "filterType": "IN",
            "dimensionName": "CLIENT_ID",
            "values": [
                5,
                19,
                14,
                34,
                6,
                27,
                7,
                2,
                8,
                23,
                4,
                20,
                1,
                3,
                9,
                "-1",
                "-1"
            ],
            "details": {
                "accessible": true
            }
        },
        {
            "filterType": "IN",
            "dimensionName": "ACCOUNT_ID",
            "values": [
                999998,
                999988,
                600001371,
                600001518,
                600001103,
                600001111,
                600001522,
                600001701,
                600001376,
                600002030,
                600001112,
                "978657890",
                "999998",
                "999999",
                "-65537",
                "-10",
                "978657890"
            ],
            "details": {
                "accessible": true
            }
        }
    ],
    "additional":{
    	"RESOLVER_SKIP_FIELDS":"POST_ID"
    },
    "jsonResponse":true
}'
 

     
     
   

## Example - Response

 
 
     
 
{
    "data": {
        "data": [
            {
                "POST_ID": "700000000495980",
                "CAMPAIGN_ID": "Action test 3 long HJGFjkhjh jhklalkfjkljklj kjHFKLKLJSKLJKJFLJFLJFLFL khjfhjkaskljf jhfkakljsfkljf jhfjkkflajklj jhfjkkljlkajfkl hfjkhkjhkjf jkahfjkhkjh jfhjk (Core & Social Cloud)",
                "ACCOUNT_ID": "Air Max",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000507467",
                "CAMPAIGN_ID": "005 (Core & Social Cloud)",
                "ACCOUNT_ID": "eriksenchristian332",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000558343",
                "CAMPAIGN_ID": "We Are Here Campaign (Core & Social Cloud)",
                "ACCOUNT_ID": "Sprinklr - HSBC",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000580319",
                "CAMPAIGN_ID": "005 (Core & Social Cloud)",
                "ACCOUNT_ID": "Air Max",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000713861",
                "CAMPAIGN_ID": "Bayer Organic Farming Campaign (Marketing Cloud)",
                "ACCOUNT_ID": "mikejening",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000730562",
                "CAMPAIGN_ID": "[Auto Import] (Core & Social Cloud)",
                "ACCOUNT_ID": "PBot",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000789435",
                "CAMPAIGN_ID": "Email Nurture Campaign (Core & Social Cloud)",
                "ACCOUNT_ID": "Bahubali",
                "TOTAL_ENGAGEMENT": 2.0
            },
            {
                "POST_ID": "700000000789477",
                "CAMPAIGN_ID": "Evergreen Campaign (Marketing Cloud)",
                "ACCOUNT_ID": "Access Denied",
                "TOTAL_ENGAGEMENT": 1.0
            },
            {
                "POST_ID": "700000000884018",
                "CAMPAIGN_ID": "Vibha Analytics Tab Test Data (System Client)",
                "ACCOUNT_ID": "NikeApp",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000937590",
                "CAMPAIGN_ID": "0001 (Core & Social Cloud)",
                "ACCOUNT_ID": "maruthitestuser",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000938291",
                "CAMPAIGN_ID": "002 (Core & Social Cloud)",
                "ACCOUNT_ID": "Air Max",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000938293",
                "CAMPAIGN_ID": "002 (Core & Social Cloud)",
                "ACCOUNT_ID": "01010101",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000946198",
                "CAMPAIGN_ID": "002 (Core & Social Cloud)",
                "ACCOUNT_ID": "Test AH",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000946199",
                "CAMPAIGN_ID": "002 (Core & Social Cloud)",
                "ACCOUNT_ID": "Test AH",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000946228",
                "CAMPAIGN_ID": "002 (Core & Social Cloud)",
                "ACCOUNT_ID": "Test AH",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000946229",
                "CAMPAIGN_ID": "002 (Core & Social Cloud)",
                "ACCOUNT_ID": "Test AH",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000948105",
                "CAMPAIGN_ID": "0001 (Core & Social Cloud)",
                "ACCOUNT_ID": "Wordpress VIP",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000949155",
                "CAMPAIGN_ID": "Action test 3 long HJGFjkhjh jhklalkfjkljklj kjHFKLKLJSKLJKJFLJFLJFLFL khjfhjkaskljf jhfkakljsfkljf jhfjkkflajklj jhfjkkljlkajfkl hfjkhkjhkjf jkahfjkhkjh jfhjk (Core & Social Cloud)",
                "ACCOUNT_ID": "01010101",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000951619",
                "CAMPAIGN_ID": "0001 (Core & Social Cloud)",
                "ACCOUNT_ID": "Wordpress VIP",
                "TOTAL_ENGAGEMENT": 0.0
            },
            {
                "POST_ID": "700000000951638",
                "CAMPAIGN_ID": "0001 (Core & Social Cloud)",
                "ACCOUNT_ID": "Wordpress VIP",
                "TOTAL_ENGAGEMENT": 0.0
            }
        ],
        "hasMore": false
    },
    "errors": []
}
 

     
     
   
 

	[](https://dev.sprinklr.com/custom-query) 

 

 
[Back to top](https://dev.sprinklr.com/custom-query)
