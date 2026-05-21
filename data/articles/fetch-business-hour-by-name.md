---
title: "Fetch Business Hour by Name"
slug: fetch-business-hour-by-name
url: https://dev.sprinklr.com/fetch-business-hour-by-name
---

# Fetch Business Hour by Name

#   GET Fetch Business Hour by Name
 

This API allows you to fetch a specific business hours configuration in Sprinklr using its name.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/business-hours/by-name?name=`{business_hour_name}`

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

## Query Parameter

















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| name | Required | Name of the business hours configuration to retrieve. Provide the exact name used during its creation. The name can include spaces. | String |

## Example - Request




 Copy Code



curl --location --request GET 'https://api3.sprinklr.com/{env}/api/v2/business-hours/by-name?name=Bangalore%20Team%20Business%20Hours' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data ''



## Example - Response





 {
    "data": [
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
        }
    ],
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

[](https://dev.sprinklr.com/fetch-business-hour-by-name) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-business-hour-by-name)
