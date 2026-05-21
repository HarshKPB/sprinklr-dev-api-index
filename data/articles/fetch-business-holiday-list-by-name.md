---
title: "Fetch Business Holiday List by Name"
slug: fetch-business-holiday-list-by-name
url: https://dev.sprinklr.com/fetch-business-holiday-list-by-name
---

# Fetch Business Holiday List by Name

#   GET Fetch Business Holiday List by Name
 

This API allows you to fetch a business holiday list configuration from Sprinklr by specifying its name.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/business-holidays/by-name?name=`{business_holiday_list_name}`

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

















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| name | Required | Name of the business holiday list to retrieve. Use the exact name provided during creation. The name may include spaces. | String |

## Example - Request




 Copy Code



curl -X GET 'https://api3.sprinklr.com/{env}/api/v2/business-holidays/by-name?name=MR%20WFM%20Business%20holidays' \
--header 'Authorization: Bearer  {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Cookie: user.env.type=ENTERPRISE; user.env.type=ENTERPRISE; JSESSIONID=3443381B169E05A5AF8FCEC08C395D49'



## Example - Response





{
    "data": [
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
        }
    ],
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

[](https://dev.sprinklr.com/fetch-business-holiday-list-by-name) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-business-holiday-list-by-name)
