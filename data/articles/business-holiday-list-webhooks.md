---
title: "Business Holiday List Webhooks"
slug: business-holiday-list-webhooks
url: https://dev.sprinklr.com/business-holiday-list-webhooks
---

# Business Holiday List Webhooks

# Business Holiday List Webhooks

You can subscribe to the Business Holiday List webhook from the Sprinklr UI. Whenever a business holiday list is created or updated, the webhook response is sent to the callback URL mentioned in the subscription.

	**Business Holiday List Webhooks:** Business Holiday List Created, Business Holiday List Updated

The following sections describe the Business Holiday List Webhooks response:


- [Business Holiday List Created Webhook](https://dev.sprinklr.com/business-holiday-list-webhooks#business_holiday_list_created)

- [Business Holiday List Updated Webhook](https://dev.sprinklr.com/business-holiday-list-webhooks#business_holiday_list_updated)


## Business Holiday List Created Webhook


The following response is received when the Business Holiday List Created webhook is triggered:

### JSON Response




  Copy Code

{
  "id": "685ae4bb58a2030ff973a665",
  "type": "business.holidays.list.created",
  "payload": {
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
      }
    ],
    "createdTime": "Jun 24, 2025, 05:47:39 PM",
    "modifiedTime": "Jun 24, 2025, 05:47:39 PM"
  },
  "eventTime": 1750787259143,
  "subscriptionDetails": {
    "subscriptionId": "685abbfccfd53f029022f068"
  }
}




### Response Parameters






















































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Id of the event | String |
| type |  | Type of event triggered | String |
| payload |  | Payload of the webhook | Object |
|  | id | Id of the holiday list | String |
|  | name | Name of the holiday list | String |
|  | timeZone | Time zone used for the holiday list | String |
|  | businessHolidays | Array containing the business holidays. For more details, see the Business Holiday Lists object table below. | String |
|  | createdTime | Time when the list was created | String |
|  | modifiedTime | Time when the list was last modified | String |
| eventTime |  | Epoch timestamp of the event | Number (Epoch Time) |
| subscriptionDetails |  |  |  |
|  | subscriptionId | Id for the subscription related to this event | String |

#### Business Holidays List






















































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| date |  | Epoch timestamp of the holiday | Number (Epoch Time) |
| title |  | Name or title of the holiday | String |
| allDay |  | Indicates whether the holiday is a full-day event | Boolean |
| timeRange |  | Defines a time range object containing the start and end times. | Array |
|  | from | Start time in minutes after midnight (00:00). For example, 210 means 3:30 AM. | String |
|  | upto | End time in minutes after midnight (00:00). For example, 450 means 7:30 AM. | String |
|  | timeUnit | Unit of time measurement (MINUTES). | String |


## Business Holiday List Updated Webhook


The following response is received when the Business Holiday List Updated webhook is triggered:

### JSON Response




  Copy Code

{
  "id": "685ae51858a2030ff973f75c",
  "type": "business.holidays.list.updated",
  "payload": {
    "oldBusinessHolidayList": {
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
        }
      ],
      "createdTime": "Jun 24, 2025, 05:47:39 PM",
      "modifiedTime": "Jun 24, 2025, 05:47:39 PM"
    },
    "newBusinessHolidayList": {
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
    }
  },
  "eventTime": 1750787352658,
  "subscriptionDetails": {
    "subscriptionId": "685abc27cfd53f0290231201"
  }
}



### Response Parameters






























































| Parameter | Sub-Parameters | Description | Type |
| --- | --- | --- | --- |
| id |  | Id of the event | String |
| type |  | Type of event triggered | String |
| payload |  |  |  |
|  | oldBusinessHolidayList | Details of the holiday list before the updateFor more details, see the Old/New Business Holiday List object table below | Object |
|  | newBusinessHolidayList | Details of the holiday list after the updateFor more details, see the Old/New Business Holiday List object table below | Object |
| eventTime |  | Epoch timestamp of the event | Number (Epoch Time) |
| subscriptionDetails |  |  |  |
|  | subscriptionId | Identifier for the related subscription | String |


#### Old/New Business Holiday List











































| Parameter | Description | Type |
| --- | --- | --- |
| id | ID of the previous holiday list | String |
| name | Name of the previous holiday list | String |
| timeZone | Time zone of the holiday list | String |
| createdTime | Creation time of the holiday list | String (DateTime) |
| modifiedTime | Last modified time of the holiday list | String (DateTime) |
| businessHolidays | Array of holiday objectsFor more details, see the Business Holidays List object table below. | Array |

#### Business Holidays List






















































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| date |  | Epoch timestamp of the holiday | Number (Epoch Time) |
| title |  | Name or title of the holiday | String |
| allDay |  | Indicates whether the holiday is a full-day event | Boolean |
| timeRange |  | Defines a time range object containing the start and end times. | Array |
|  | from | Start time in minutes after midnight (00:00). For example, 210 means 3:30 AM. | String |
|  | upto | End time in minutes after midnight (00:00). For example, 450 means 7:30 AM. | String |
|  | timeUnit | Unit of time measurement (MINUTES). | String |

	 [](https://dev.sprinklr.com/business-holiday-list-webhooks)

[Back to top](https://dev.sprinklr.com/business-holiday-list-webhooks)
