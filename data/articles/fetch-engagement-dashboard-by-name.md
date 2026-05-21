---
title: "Fetch Engagement Dashboard by Name"
slug: fetch-engagement-dashboard-by-name
url: https://dev.sprinklr.com/fetch-engagement-dashboard-by-name
---

# Fetch Engagement Dashboard by Name

#
  GET Fetch Engagement Dashboard by Name



Using this API, you can fetch the engagement dashboard details using the given name.

**Use Cases:**

- Fetch the names and column ids of all the engagement dashboards available in the Sprinklr environment

- Fetch column Ids, which then can be used in stream read API

- Fetch up-to-date information on all the engagement dashboards existing in the environment

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/monitoring/dashboard/find/name/{dashbaordName}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.














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

## Path Parameter












| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| dashboardName | Required | Refers to the name of the dashboard. Kindly note that the dashboard name should be URL-encoded | String |

	**Note:**Using this API, you can fetch the stream Id of the engagement dashboard column, which can then be used to fetch the column details from the [Outbound](https://dev.sprinklr.com/outbound-column-stream) or [Inbound](https://dev.sprinklr.com/inbound-column-stream) Stream Read API.

## Example - Request















Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/monitoring/dashboard/find/name/Sanity' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}'






## Example - Response





{
    "data": [
        {
            "id": "6639fe152e0b880f6ecc5213",
            "name": "Sanity",
            "columnOrder": [
                "6639fe3d2e0b880f6ecc6374"
            ],
            "columns": [
                {
                    "id": "6639fe3d2e0b880f6ecc6374",
                    "name": "Test API",
                    "dashboardId": "6639fe152e0b880f6ecc5213",
                    "channel": "FACEBOOK",
                    "type": "REPLIES",
                    "properties": {
                        "SORT_ENABLED": [
                            "true"
                        ],
                        "ACCOUNT": [
                            "600044038",
                            "600002748",
                            "66004907",
                            "600029918",
                            "66002003",
                            "600037467",
                            "600012352",
                            "600040986",
                            "600011034",
                            "600012345",
                            "600039666"
                        ],
                        "SOURCE_ID": [
                            "600044038",
                            "600002748",
                            "66004907",
                            "600029918",
                            "66002003",
                            "600037467",
                            "600012352",
                            "600040986",
                            "600011034",
                            "600012345",
                            "600039666"
                        ],
                        "SHOW_COUNT": [
                            "true"
                        ],
                        "CATEGORY": [
                            "7"
                        ],
                        "POST_TYPE": [
                            "all"
                        ],
                        "TIME_RANGE_FILTER_KEY": [
                            "LIFETIME"
                        ],
                        "SPONSORED_POST_TYPE": [
                            "all"
                        ],
                        "SEARCH_ENABLED": [
                            "true"
                        ]
                    },
                    "clientCustomProperties": {},
                    "partnerCustomProperties": {},
                    "upfrontFilterKeys": [],
                    "sourceType": "ACCOUNT",
                    "clientQueues": [],
                    "partnerQueues": [],
                    "sortField": "snCreatedTime",
                    "columnColor": "#ccc",
                    "autoRender": true,
                    "locked": false,
                    "order": 0.0,
                    "versionId": 0
                }
            ],
            "tags": [],
            "locked": false,
            "shared": true
        }
    ],
    "errors": []
}







[](https://dev.sprinklr.com/fetch-engagement-dashboard-by-name)




[Back to top](https://dev.sprinklr.com/fetch-engagement-dashboard-by-name)
