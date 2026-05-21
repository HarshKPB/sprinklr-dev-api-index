---
title: "Fetch All Business Hours"
slug: fetch-all-business-hours
url: https://dev.sprinklr.com/fetch-all-business-hours
---

# Fetch All Business Hours

#   GET Fetch All Business Hours

 

This API allows you to retrieve details of all business hours configurations created in Sprinklr.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/business-hours?page=0&size=10

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



curl --location --request GET 'https://api3.sprinklr.com/{env}/api/v2/business-hours?page=1&size=10' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Cookie: user.env.type=ENTERPRISE; user.env.type=ENTERPRISE'



## Example - Response





  {
    "data": {
        "results": [
            {
                "id": "66ed5616c41bfd533a8bfa08",
                "name": "AK 9to6",
                "timeZone": "Asia/Kolkata",
                "daySchedules": [
                    {
                        "schedulingDay": "MONDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1080,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "TUESDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1080,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "WEDNESDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1080,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "THURSDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1080,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "FRIDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1080,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SATURDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1080,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    }
                ],
                "businessHolidayLists": [
                    "66ed55c8c41bfd533a8bd584"
                ],
                "createdTime": "Sep 20, 2024, 11:01:42 AM",
                "modifiedTime": "Sep 20, 2024, 11:01:42 AM"
            },
            {
                "id": "6840371b434395122a481765",
                "name": "AkhilTest",
                "timeZone": "Asia/Kabul",
                "daySchedules": [
                    {
                        "schedulingDay": "MONDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 600,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "TUESDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 600,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "WEDNESDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 600,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "THURSDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 600,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "FRIDAY",
                        "timeRange": [],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SATURDAY",
                        "timeRange": [],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SUNDAY",
                        "timeRange": [],
                        "enabled": false
                    }
                ],
                "businessHolidayLists": [
                    "683ee63b1c303b3055f7dc20"
                ],
                "createdTime": "Jun 04, 2025, 12:07:55 PM",
                "modifiedTime": "Jun 04, 2025, 12:07:55 PM"
            },
            {
                "id": "65eb08921bf0c21d2050c5d9",
                "name": "Auto_BH_For_Suppression_List_Testd",
                "timeZone": "Asia/Kolkata",
                "daySchedules": [
                    {
                        "schedulingDay": "MONDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "TUESDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "WEDNESDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "THURSDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "FRIDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SATURDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SUNDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    }
                ],
                "createdTime": "Mar 08, 2024, 12:46:10 PM",
                "modifiedTime": "Dec 03, 2024, 07:32:34 AM"
            },
            {
                "id": "654f5939a6e4cd6e5d0d549e",
                "name": "Automation_Business_Hour_0_1440_ASIA_KOLKATA",
                "description": "Business Hour For Asia/Kolkata Timezone (540-1020)",
                "timeZone": "Asia/Kolkata",
                "daySchedules": [
                    {
                        "schedulingDay": "MONDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "TUESDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "WEDNESDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "THURSDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "FRIDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1080,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SATURDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SUNDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    }
                ],
                "createdTime": "Mar 19, 2025, 07:21:46 AM",
                "modifiedTime": "Jun 24, 2025, 05:48:03 PM"
            },
            {
                "id": "685cbc1b8a018e4528962cdb",
                "name": "BR Business Hours",
                "description": "This configuration is for business hours",
                "timeZone": "Asia/Kabul",
                "daySchedules": [
                    {
                        "schedulingDay": "MONDAY",
                        "timeRange": [
                            {
                                "from": 210,
                                "upto": 420,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "TUESDAY",
                        "timeRange": [
                            {
                                "from": 210,
                                "upto": 420,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "WEDNESDAY",
                        "timeRange": [
                            {
                                "from": 210,
                                "upto": 420,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "THURSDAY",
                        "timeRange": [
                            {
                                "from": 210,
                                "upto": 420,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "FRIDAY",
                        "timeRange": [
                            {
                                "from": 210,
                                "upto": 420,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SATURDAY",
                        "timeRange": [
                            {
                                "from": 210,
                                "upto": 420,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    }
                ],
                "createdTime": "Jun 26, 2025, 03:18:51 AM",
                "modifiedTime": "Jun 26, 2025, 03:18:51 AM"
            },
            {
                "id": "685abd8acfd53f0290240c19",
                "name": "Bangalore Team Business Hours",
                "timeZone": "Asia/Kolkata",
                "daySchedules": [
                    {
                        "schedulingDay": "MONDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "TUESDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "WEDNESDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "THURSDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "FRIDAY",
                        "timeRange": [],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SATURDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SUNDAY",
                        "timeRange": [],
                        "enabled": false
                    }
                ],
                "createdTime": "Jun 24, 2025, 03:00:26 PM",
                "modifiedTime": "Jun 24, 2025, 03:26:28 PM"
            },
            {
                "id": "6548d40b016df675d87730b2",
                "name": "Bhanu_BH(6-9, 12-3, 6-9)",
                "timeZone": "Asia/Kolkata",
                "daySchedules": [
                    {
                        "schedulingDay": "WEDNESDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 540,
                                "timeUnit": "MINUTES"
                            },
                            {
                                "from": 720,
                                "upto": 900,
                                "timeUnit": "MINUTES"
                            },
                            {
                                "from": 1080,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "THURSDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 540,
                                "timeUnit": "MINUTES"
                            },
                            {
                                "from": 720,
                                "upto": 900,
                                "timeUnit": "MINUTES"
                            },
                            {
                                "from": 1080,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "FRIDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 540,
                                "timeUnit": "MINUTES"
                            },
                            {
                                "from": 720,
                                "upto": 900,
                                "timeUnit": "MINUTES"
                            },
                            {
                                "from": 1080,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SATURDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 540,
                                "timeUnit": "MINUTES"
                            },
                            {
                                "from": 720,
                                "upto": 900,
                                "timeUnit": "MINUTES"
                            },
                            {
                                "from": 1080,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SUNDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 540,
                                "timeUnit": "MINUTES"
                            },
                            {
                                "from": 720,
                                "upto": 900,
                                "timeUnit": "MINUTES"
                            },
                            {
                                "from": 1080,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    }
                ],
                "createdTime": "Nov 06, 2023, 11:54:51 AM",
                "modifiedTime": "Jul 15, 2024, 01:14:43 PM"
            },
            {
                "id": "655e11bbe9abbe37dd2f3ce6",
                "name": "Business Hour Ticket Testing",
                "timeZone": "Asia/Kolkata",
                "daySchedules": [
                    {
                        "schedulingDay": "MONDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "TUESDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "WEDNESDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "THURSDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "FRIDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SATURDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SUNDAY",
                        "timeRange": [
                            {
                                "from": 0,
                                "upto": 1440,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    }
                ],
                "createdTime": "Nov 22, 2023, 02:35:39 PM",
                "modifiedTime": "Jul 15, 2024, 01:14:47 PM"
            },
            {
                "id": "655b42243b0b642534f97e15",
                "name": "Business hours Changes testing",
                "timeZone": "Asia/Kolkata",
                "daySchedules": [
                    {
                        "schedulingDay": "MONDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 900,
                                "timeUnit": "MINUTES"
                            },
                            {
                                "from": 1080,
                                "upto": 1140,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "TUESDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 900,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "WEDNESDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 900,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "THURSDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 900,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "FRIDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 900,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SATURDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 900,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SUNDAY",
                        "timeRange": [
                            {
                                "from": 360,
                                "upto": 900,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    }
                ],
                "createdTime": "Nov 20, 2023, 11:25:24 AM",
                "modifiedTime": "Jul 15, 2024, 01:14:47 PM"
            },
            {
                "id": "67aed975c9fe1f1b12408853",
                "name": "Business hours by ritam",
                "timeZone": "Asia/Kolkata",
                "daySchedules": [
                    {
                        "schedulingDay": "MONDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "TUESDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "WEDNESDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "THURSDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "FRIDAY",
                        "timeRange": [
                            {
                                "from": 540,
                                "upto": 1260,
                                "timeUnit": "MINUTES"
                            }
                        ],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SATURDAY",
                        "timeRange": [],
                        "enabled": false
                    },
                    {
                        "schedulingDay": "SUNDAY",
                        "timeRange": [],
                        "enabled": false
                    }
                ],
                "businessHolidayLists": [
                    "677fcb464aa4f00faaf675d1"
                ],
                "createdTime": "Feb 14, 2025, 05:49:41 AM",
                "modifiedTime": "Feb 18, 2025, 08:06:27 AM"
            }
        ],
        "count": 304
    },
    "errors": []
}



## Response Parameters























































      ``
``





      ``
``





      ``
``






``






``






``




| Parameter | Subparameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Id of the business hours configuration. | String |
| name |  | Name of the business hours configuration. | String |
| description |  | Description of the configuration. | String |
| timeZone |  | Time zone for the schedule. | String |
| daySchedules |  | Array of daily schedules. Contains day, time ranges, and status. | Array |
|  | schedulingDay | Day of the week for the schedule. | String |
|  | timeRange | Array of time ranges defining work intervals. | Array |
|  |  | from: Start time in minutes after midnight. Example: 210 (3:30 AM) | Integer |
|  |  | upto:  End time in minutes after midnight. Example: 420 (7:00 AM) | Integer |
|  |  | timeUnit: Unit for the time range. Example: MINUTES | String |
|  | enabled | Indicates whether the schedule for the day is active. Example: false | Boolean |
| createdTime |  | Timestamp when the configuration was created. Example: Jun 26, 2025, 03:18:51 AM | String |
| modifiedTime |  | Timestamp when the configuration was last modified. Example: Jun 26, 2025, 03:18:51 AM | String |

[](https://dev.sprinklr.com/fetch-all-business-hours) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-all-business-hours)
