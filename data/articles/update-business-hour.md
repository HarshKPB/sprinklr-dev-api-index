---
title: "Update Business Hour"
slug: update-business-hour
url: https://dev.sprinklr.com/update-business-hour
---

# Update Business Hour

#   POST Update Business Hour
 

This API allows you to update an existing business hours configuration in Sprinklr.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/business-hours

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

## Request Parameters













     [Create Business Hour API](https://dev.sprinklr.com/create-business-hour)























       [Create Business Holiday List API](https://dev.sprinklr.com/create-business-holiday-list)










| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | Id of the business hours configuration. You can obtain this Id from the response of the . | String |
| name | Required | Name of the business hours configuration. | String |
| description | Optional | The description of the business hours configuration. | String |
| timeZone | Required | The time zone of the business hours configuration. | String |
| businessHolidayLists | Optional | An array of business holiday list Ids. You can retrieve these Ids from the response of the . | Array |
| daySchedules | Required | An array specifying work time slots for each day of the week. Each entry includes the day, a time range (from, upto, and timeUnit). For detailed structure, refer to the Day Schedule table. | Array |

### Day Schedule
















****




























****



| Parameters | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| schedulingDay |  | Required | Day of the week you are scheduling the business hours and holidays for. 			 Supported Values: MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY | String |
| timeRange |  | Optional | Defines a time range object containing the start and end times. | String |
|  | from | Optional | Start time in minutes after midnight (00:00). For example, "210" means 3:30 AM. | String |
|  | upto | Optional | End time in minutes after midnight (00:00). For example, "450" means 7:30 AM. | String |
|  | timeUnit | Optional | Unit of time measurement.  				 Supported Value: MINUTES | String |

## Example - Request




 Copy Code



curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/business-hours' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Cookie: JSESSIONID=6621EE4034EC0C37EB1B0BA2EC406ABD' \
--data '{
    "id": "686648f50791710f2810df19",
    "name":"BR New Business Hours 3",
    "description":"This configuration is for business hours",
    "timeZone":"Asia/Kabul",
    "daySchedules":[
  {
    "schedulingDay": "MONDAY",
    "timeRange": [
      {
        "timeUnit": "MINUTES"
      }
    ]
  },
  {
    "schedulingDay": "TUESDAY",
    "timeRange": [
      {
        "timeUnit": "MINUTES"
      }
    ]
  },
  {
    "schedulingDay": "WEDNESDAY",
    "timeRange": [
      {
        "timeUnit": "MINUTES"
      }
    ]
  },
  {
    "schedulingDay": "THURSDAY",
    "timeRange": [
      {
        "timeUnit": "MINUTES"
      }
    ]
  },
  {
    "schedulingDay": "FRIDAY",
    "timeRange": [
      {
        "from": 210,
        "upto": 420,
        "timeUnit": "MINUTES"
      }
    ]
  },
  {
    "schedulingDay": "SATURDAY",
    "timeRange": [
      {
        "from": 210,
        "upto": 420,
        "timeUnit": "MINUTES"
      }
    ]
  }
]
}'



## Example - Response





 {
    "data": {
        "id": "686648f50791710f2810df19",
        "name": "BR New Business Hours 3",
        "description": "This configuration is for business hours",
        "timeZone": "Asia/Kabul",
        "daySchedules": [
            {
                "schedulingDay": "MONDAY",
                "timeRange": [
                    {
                        "timeUnit": "MINUTES"
                    }
                ],
                "enabled": false
            },
            {
                "schedulingDay": "TUESDAY",
                "timeRange": [
                    {
                        "timeUnit": "MINUTES"
                    }
                ],
                "enabled": false
            },
            {
                "schedulingDay": "WEDNESDAY",
                "timeRange": [
                    {
                        "timeUnit": "MINUTES"
                    }
                ],
                "enabled": false
            },
            {
                "schedulingDay": "THURSDAY",
                "timeRange": [
                    {
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
        ]
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












``






``




| Parameter | Subparameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Id of the business hours configuration. | String |
| name |  | Name of the business hours configuration. | String |
| description |  | Description of the configuration. | String |
| timeZone |  | Time zone for the schedule. Example: Asia/Kabul | String |
| daySchedules |  | Array of daily schedules. Contains day, time ranges, and status. | Array |
|  | schedulingDay | Day of the week for the schedule. Example: MONDAY | String |
|  | timeRange | Array of time ranges defining work intervals. | Array |
|  |  | from: Start time in minutes after midnight. Example: 210 (3:30 AM) | Integer |
|  |  | upto:  End time in minutes after midnight. Example: 420 (7:00 AM) | Integer |
|  |  | timeUnit: Unit for the time range. Example: MINUTES | String |
|  | enabled | Indicates whether the schedule for the day is active. Example: false | Boolean |
| businessHolidayLists |  | An array of business holiday list Ids. | Array |
| createdTime |  | Timestamp when the configuration was created. Example: Jun 26, 2025, 03:18:51 AM | String |
| modifiedTime |  | Timestamp when the configuration was last modified. Example: Jun 26, 2025, 03:18:51 AM | String |

[](https://dev.sprinklr.com/update-business-hour) 

 

 
[Back to top](https://dev.sprinklr.com/update-business-hour)
