---
title: "Update Business Holiday List"
slug: update-business-holiday-list
url: https://dev.sprinklr.com/update-business-holiday-list
---

# Update Business Holiday List

#   POST Update Business Holiday List
 

This API allows you to update a business holiday list in Sprinklr.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/business-holidays

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













     [Create Business Holiday List API](https://dev.sprinklr.com/create-business-holiday-list)






















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | Id of the business holiday list you want to update. You can obtain this Id from the response of the . | String |
| name | Required | Name of the business holiday list configuration. | String |
| timeZone | Required | The time zone of the business holiday list configuration. | String |
| businessHolidays | Required | List of business holidays. At least one business holiday must be mentioned. For more details, see the Business Holidays Object table below. | String |

#### Business Holidays



















































****











| Parameters | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| title |  | Optional | Name or title of the holiday. | String |
| allDay |  | Optional | Indicates whether the holiday lasts all day. | String |
| timeRange |  | Optional | Specify the time range. | String |
|  | from | Optional | Start time in minutes after midnight (00:00). For example, 210 means 3:30 AM. | String |
|  | upto | Optional | End time in minutes after midnight (00:00). For example, 450 means 7:30 AM. | String |
|  | timeUnit | Optional | Unit of time measurement. 				 Supported Value: MINUTES | String |
| date |  | Required | Date of the holiday. The date must be in epoch timestamp format (milliseconds). For example, for date 2025-04-18, enter 1744934400000. You can use any epoch converter tool to convert the date to epoch timestamp. | String |

## Example - Request




 Copy Code



curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/business-holidays' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "id":"686776a97deb6d4ca465a956",
    "name": "BR Business Holiday List 2",
    "timeZone": "Asia/Dhaka",
    "businessHolidays": [
        {
            "title": "Good Friday",
            "allDay": true,
            "timeRange": [],
            "date": 1744934400000
        },
        {
            "title": "May Day",
            "allDay": true,
            "timeRange": [],
            "date": 1746345600000
        },
        {
            "title": "Muharram",
            "allDay": true,
            "timeRange": [],
            "date": 1752067200000
        },
        {
            "title": "Independence day",
            "allDay": true,
            "timeRange": [],
            "date": 1755523200000
        },
        {
            "title": "New Holiday",
            "allDay": true,
            "timeRange": [],
            "date": 1755523200000
        }
    ]
}'



## Example - Response





{
    "data": {
        "id": "686776a97deb6d4ca465a956",
        "name": "BR Business Holiday List 2",
        "timeZone": "Asia/Dhaka",
        "businessHolidays": [
            {
                "date": 1744934400000,
                "timeRange": [],
                "allDay": true,
                "title": "Good Friday"
            },
            {
                "date": 1746345600000,
                "timeRange": [],
                "allDay": true,
                "title": "May Day"
            },
            {
                "date": 1752067200000,
                "timeRange": [],
                "allDay": true,
                "title": "Muharram"
            },
            {
                "date": 1755523200000,
                "timeRange": [],
                "allDay": true,
                "title": "Independence day"
            },
            {
                "date": 1755523200000,
                "timeRange": [],
                "allDay": true,
                "title": "New Holiday"
            }
        ]
    },
    "errors": []
}



### Response Parameters













































- ****
- ****
- ****


































| Parameter | Subparameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Id for the holiday list configuration | String |
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

[](https://dev.sprinklr.com/update-business-holiday-list) 

 

 
[Back to top](https://dev.sprinklr.com/update-business-holiday-list)
