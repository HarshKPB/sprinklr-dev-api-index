---
title: "Business Hours Webhooks"
slug: business-hours-webhooks
url: https://dev.sprinklr.com/business-hours-webhooks
---

# Business Hours Webhooks

# Business Hours Webhooks

 You can subscribe to the Business Hours webhook from the Sprinklr UI. Whenever a business hours configuration is created or updated, a webhook response is sent to the callback URL specified during the subscription.

	**Business Hours Subscriptions:** Business Hours Created, Business Hours Updated

The following sections describe the webhook responses


- [Business Hours Created Webhook](https://dev.sprinklr.com/business-hours-webhooks#bhCreated)

- [Business Hours Updated Webhook](https://dev.sprinklr.com/business-hours-webhooks#bhUpdated)


## Business Hours Created Webhook


The following response is received when the Business Hours Created webhook is triggered:

### JSON Response




  Copy Code

{
  "id": "685abd8acfd53f0290240c1e",
  "type": "business.hours.created",
  "payload": {
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
    "createdTime": "Jun 24, 2025, 03:00:26 PM",
    "modifiedTime": "Jun 24, 2025, 03:00:26 PM"
  },
  "eventTime": 1750777226890,
  "subscriptionDetails": {
    "subscriptionId": "685abb872600f92e98806390"
  }
}




### Response Parameters
















































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Id of the event | String |
| type |  | Type of the event | String |
| payload |  | Payload of the webhook | Object |
|  | id | Id of the business hours configuration | String |
|  | name | Name of the business hours configuration | String |
|  | timeZone | Time zone of the business hours configuration | String |
|  | daySchedules | List of daily schedulesFor more details, see the Day Schedule Object table below. | Array |
|  | createdTime | Creation timestamp | String |
|  | modifiedTime | Last modification timestamp | String |
| evenTime |  | Timestamp of the event | Epoch (milliseconds) |
| subscriptionDetails | subscriptionId | Subscription identifier | String |

#### Day Schedule Object
















































| Sub-parameter | timeRange Sub-parameter | Description | Type |
| --- | --- | --- | --- |
| schedulingDay |  | Day of the week for which the schedule applies | String |
| timeRange |  | Defines a time range object containing the start and end times. | Array |
|  | from | Start time in minutes from 00:00 (midnight) | Number |
|  | upto | End time in minutes from 00:00 (midnight) | Number |
|  | timeUnit | Unit of time measurement (MINUTES) | String |
| enabled |  | Indicates if the schedule for the day is active or not | Boolean |


## Business Hours Updated Webhook


The following response is received when the Business Hours Updated webhook is triggered:

### JSON Response




  Copy Code

{
  "id": "685ac3a5cfd53f029027558c",
  "type": "business.hours.updated",
  "payload": {
    "oldBusinessHours": {
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
      "createdTime": "Jun 24, 2025, 03:00:26 PM",
      "modifiedTime": "Jun 24, 2025, 03:00:26 PM"
    },
    "newBusinessHours": {
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
  },
  "eventTime": 1750778788809,
  "subscriptionDetails": {
    "subscriptionId": "685abbd7cfd53f029022d312"
  }
}



### Response Parameters
























































| Parameter | Sub-parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Id for the event | String |
| type |  | Type of the event | String |
| payload |  | Payload of the webhook containing old and new business hours | Object |
|  | oldBusinessHours | Previous business hours configurationFor more details, see the Old/New Business Hours Object table | Object |
|  | newBusinessHours | Updated business hours configurationFor more details, see the Old/New Business Hours Object table | Object |
| eventTime |  | Timestamp of the event | Epoch (milliseconds) |
| subscriptionDetails | subscriptionId | Subscription identifier | String |

#### Old/New Business Hours Object










































| Parameter | Description | Type |
| --- | --- | --- |
| id | Id for the business hours | String |
| name | Name of the business hours configuration | String |
| timeZone | Time zone of the business hours | String |
| daySchedules | List of day-wise schedulesFor more details, see the Day Schedule Object table below. | Array |
| createdTime | Timestamp of creation | String |
| modifiedTime | Timestamp of last modification | String |

#### Day Schedule Object
















































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| schedulingDay |  | Day of the week the schedule applies to | String |
| timeRange |  | Defines a time range object containing the start and end times. | Array |
|  | from | Start time in minutes from midnight (00:00) | Number |
|  | upto | End time in minutes from midnight (00:00) | Number |
|  | timeUnit | Unit of time used (MINUTES) | String |
| enabled |  | Indicates whether the schedule is active | Boolean |

	 [](https://dev.sprinklr.com/business-hours-webhooks)

[Back to top](https://dev.sprinklr.com/business-hours-webhooks)
