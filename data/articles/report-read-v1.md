---
title: "Report Read v1"
slug: report-read-v1
url: https://dev.sprinklr.com/report-read-v1
---

# Report Read v1

#
  POST - Report Read

Using this API, you can fetch the reporting data from a tabular widget.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/reports/query

**Best Practice: ** While making Reporting API call, time range should be less than 15 days and page size should be less than 50000. If you cross that limit, the API will give 400 bad request.

**Dev Notes: ** To get the response without any error use this formula: {(page -1)*pagesize} < 50000.

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

### Request Parameters


































































































``

















``












| Parameter | Type | Description | Requierd/Optional |
| --- | --- | --- | --- |
| reportingEngine | String | Supported engines are: 				PLATFORM, 				INBOUND_MESSAGE | Required |
| report | String | Name of the predefined report | Required |
| startTime | long | start time of the report; it’s in Unix time in ms | Required |
| endTime | long | end time of the report; it’s in Unix time in ms | Required |
| timeZone | String | default is UTC | Optional |
| page | int | starting page number; default=0 | Optional |
| pageSize | int | max number of items in the page; default=10, max=2000 | Optional |
| filters | List<ExternalFIlter> | filter information | Optional |
| groupBys | List<ExternalGroup> | group-by information | Optional |
| projections | List<ExternalProjection> | metrics information | Required |
| sorts | List<ExternalSort> | sorting information, ASC orDESC. Example:  "sorts":{ "heading":"", "order":"ASC" } | Optional |
| projectionDecorations | List<String> | CHANGE, PERCENTAGE_CHANGE, PERCENTAGE | Optional |
| jsonResponse | Boolean | true, to get the industry standard structured response. "jsonResponse":true | Required |
| additional | Map<String, Boolean> | Report dimensions are automatically resolved to include additional information: 					CASE or ASSOCIATED_CASE: Case description will be added. 					Adding "SKIP_RESOLVER":true will suppress the said resolution. | Optional |

**Dev Notes: **Initially the document will cover only a subset of available engines PLATFORM and INBOUND_MESSAGE.

### ExternalFIlter Definitions












































| Parameter | Type | Description | Required/Optional |
| --- | --- | --- | --- |
| dimensionName | String | attribute getting filtered | Required |
| filterType | String | Supported filterTypes are: 				IN, GT, GTE, LT, LTE, NIN, BETWEEN, STARTS_WITH, CONTAINS, EQUALS , FILTER, EXISTS | Required |
| values | List<Object> | values getting compared against | Optional |
| details | Map<String, Object> | additional information as required | Optional |

### ExternalGroup Definitions












































| Parameter | type | Description | Required/Optional |
| --- | --- | --- | --- |
| heading | String | string value to be used as the key in the response | Required |
| dimensionName | String | attribute used for groupBy | Required |
| groupType | List<Object> | Supported groupTypes are: 				DATE_HISTOGRAM, 				TIME_OF_DAY, 				DAY_OF_WEEK, MONTH_OF_YEAR, 				FIELD | Required |
| details | Map<String, Object> | additional information as required | Optional |

### ExternalProjection Definitions












































| Parameter | Type | Description | Required/Optional |
| --- | --- | --- | --- |
| heading | String | string value to be used as the key in the response | Required |
| measurementName | String | measurement for the report | Required |
| aggregateFunction | String | Supported functions are: 				SUM, AVG, MIN, MAX, STATS | Required |
| details | Map<String, Object> | additional information as required | Optional |

## Example - Request




 Copy Code



curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v1/reports/query' \
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
        ]
    },
    "errors": []
}





### Response Parameters



























| Parameter | Type | Description |
| --- | --- | --- |
| headings | List<String> | Each string value was provided as the key in the request; groupBys followed by projections. |
| rows | List<List<Object>> | N-th List<Object> is the value corresponding to the n-th heading |

**Dev Notes: **The next part of this document will show how various reports can be obtained using this API.

[](https://dev.sprinklr.com/report-read-v1)




[Back to top](https://dev.sprinklr.com/report-read-v1)
