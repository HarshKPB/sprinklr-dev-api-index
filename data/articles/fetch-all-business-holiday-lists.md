---
title: "Fetch All Business Holiday Lists"
slug: fetch-all-business-holiday-lists
url: https://dev.sprinklr.com/fetch-all-business-holiday-lists
---

# Fetch All Business Holiday Lists

#   GET Fetch All Business Holiday Lists
 

This API allows you to fetch all business holiday list configurations created in Sprinklr.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/business-holidays?page=0&size=10

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

### Query Parameters




















****



| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| page | Optional | Specifies the page number of the results to retrieve in a paginated response. | Number |
| size | Required | Specifies the maximum number of items to return per page in the response. Maximum Supported Value: 100 | Number |

## Example - Request




 Copy Code



curl --location --request GET 'https://api3.sprinklr.com/{env}/api/v2/business-holidays?page=2&size=10' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \



## Example - Response





{
    "data": {
        "results": [
            {
                "id": "685ae4bb58a2030ff973a642",
                "name": "India Holiday List",
                "timeZone": "Asia/Kolkata",
                "businessHolidays": [
                    {
                        "date": 1755216000000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "Independence Day"
                    },
                    {
                        "date": 1759363200000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "Gandhi Jayanti"
                    },
                    {
                        "date": 1766620800000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "Christmas"
                    },
                    {
                        "date": 1761091200000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "Diwali"
                    }
                ],
                "createdTime": "Jun 24, 2025, 05:47:39 PM",
                "modifiedTime": "Jun 24, 2025, 05:49:12 PM"
            },
            {
                "id": "663c9b109d4237193a783ac1",
                "name": "MAQ_BH",
                "timeZone": "Asia/Kolkata",
                "businessHolidays": [
                    {
                        "date": 1715299200000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "MAQ_DAY"
                    },
                    {
                        "date": 1716422400000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "Alpha_DAY"
                    }
                ],
                "createdTime": "May 09, 2024, 09:44:48 AM",
                "modifiedTime": "May 09, 2024, 09:48:54 AM"
            },
            {
                "id": "6634940ec624331a65bcf743",
                "name": "MR",
                "timeZone": "Asia/Kolkata",
                "businessHolidays": [
                    {
                        "date": 1714780800000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "MR Holiday-1"
                    },
                    {
                        "date": 1714867200000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "MR Holiday-2"
                    },
                    {
                        "date": 1714953600000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "MR Holiday-3"
                    },
                    {
                        "date": 1715040000000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "MR Holiday-4"
                    }
                ],
                "createdTime": "May 03, 2024, 07:36:46 AM",
                "modifiedTime": "May 09, 2024, 10:55:02 AM"
            },
            {
                "id": "6596e52823db9a0a4169271a",
                "name": "MR Business Holiday",
                "timeZone": "Asia/Kolkata",
                "businessHolidays": [
                    {
                        "date": 1717200000000,
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 720,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "allDay": false,
                        "title": "June1 ( 9am-12pm)"
                    },
                    {
                        "date": 1746057600000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "yo"
                    }
                ],
                "createdTime": "Jan 04, 2024, 05:04:40 PM",
                "modifiedTime": "Apr 22, 2025, 08:17:29 AM"
            },
            {
                "id": "65966f6f867650463578de17",
                "name": "MR Dubai Business Holiday",
                "timeZone": "Asia/Dubai",
                "businessHolidays": [
                    {
                        "date": 1712880000000,
                        "timeRange": [
                            {
                                "from": 600,
                                "upto": 780,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "allDay": false,
                        "title": "Dubai Business Holiday(10am-13pm)"
                    }
                ],
                "createdTime": "Jan 04, 2024, 08:42:23 AM",
                "modifiedTime": "Jan 04, 2024, 02:11:23 PM"
            },
            {
                "id": "66baefcd62ff98069eafe62e",
                "name": "MR KT Business List",
                "timeZone": "Asia/Kolkata",
                "businessHolidays": [
                    {
                        "date": 1723680000000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "Independence Day"
                    }
                ],
                "createdTime": "Aug 13, 2024, 05:31:57 AM",
                "modifiedTime": "Aug 13, 2024, 05:31:57 AM"
            },
            {
                "id": "6596671c867650463571e705",
                "name": "MR WFM Business holidays",
                "timeZone": "Asia/Kolkata",
                "businessHolidays": [
                    {
                        "date": 1711238400000,
                        "timeRange": [
                            {
                                "from": 600,
                                "upto": 720,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "allDay": false,
                        "title": "March 24-Business Holiday"
                    }
                ],
                "createdTime": "Jan 04, 2024, 08:06:52 AM",
                "modifiedTime": "Jan 04, 2024, 04:57:36 PM"
            },
            {
                "id": "67d57b7523e0ec3ad023a696",
                "name": "Manasa Holiday list",
                "timeZone": "Asia/Kolkata",
                "businessHolidays": [
                    {
                        "date": 1745712000000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "Manasa Holiday"
                    }
                ],
                "createdTime": "Mar 15, 2025, 01:07:01 PM",
                "modifiedTime": "Mar 15, 2025, 01:07:01 PM"
            },
            {
                "id": "67cffee6e80f920da0b13100",
                "name": "RKP Test",
                "timeZone": "Asia/Kolkata",
                "businessHolidays": [
                    {
                        "date": 1762128000000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "Birthday"
                    },
                    {
                        "date": 1755216000000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "Independence Day"
                    },
                    {
                        "date": 1766016000000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "Birthday"
                    },
                    {
                        "date": 1735689600000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "New Year"
                    }
                ],
                "createdTime": "Mar 11, 2025, 09:14:14 AM",
                "modifiedTime": "Mar 11, 2025, 09:14:52 AM"
            },
            {
                "id": "65f0193db230995b84ec5812",
                "name": "Rahul Holiday List",
                "timeZone": "UTC",
                "businessHolidays": [
                    {
                        "date": 1717545600000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "Holiday 1"
                    },
                    {
                        "date": 1717632000000,
                        "timeRange": [],
                        "allDay": true,
                        "title": "Holiday 2"
                    }
                ],
                "createdTime": "Mar 12, 2024, 08:58:37 AM",
                "modifiedTime": "Jun 05, 2024, 04:57:55 AM"
            }
        ],
        "count": 49
    },
    "errors": []
}



### Response Parameters













































- ****
- ****
- ****


































| Parameter | Subparameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Id of the holiday list configuration | String |
| name |  | Name of the holiday list | String |
| timeZone |  | Time zone used for the configuration | String |
| businessHolidays |  | Array of holiday entries | Array |
|  | date | Timestamp of the holiday in milliseconds (Epoch) | Number |
|  | timeRange | Array of specific time ranges for partial-day holidays (empty for all-day)   from: Start time in minutes after midnight (00:00)   upto: End time in minutes after midnight (00:00)   timeUnit: Unit of time measurement ( MINUTES) | Array |
|  | allDay | Indicates if the holiday spans the entire day | Boolean |
|  | title | Name or label for the holiday | String |
| createdTime |  | Timestamp when the configuration was created | String |
| modifiedTime |  | Timestamp when the configuration was last modified | String |
| errors |  | Array containing any errors from the API response | Array |

[](https://dev.sprinklr.com/fetch-all-business-holiday-lists) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-all-business-holiday-lists)
