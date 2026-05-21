---
title: "Fetch Business Holiday List by Id"
slug: fetch-business-holiday-list-by-id
url: https://dev.sprinklr.com/fetch-business-holiday-list-by-id
---

# Fetch Business Holiday List by Id

#   GET Fetch Business Holiday List by Id
 

This API allows you to fetch a business holiday list by its Id. This Id is generated when you create the business holiday list.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/business-holidays/id/`{business_holiday_list_id}`

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













     [Create Business Holiday List API](https://dev.sprinklr.com/create-business-holiday-list)



| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {business_holiday_list_id} | Required | The Id of the business holiday list you want to retrieve. You can obtain this Id from the response of the . | String |

## Example - Request




 Copy Code



curl -X GET 'https://api3.sprinklr.com/{env}/api/v2/business-holidays/id/6596671c867650463571e705' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Cookie: user.env.type=ENTERPRISE; JSESSIONID=6381C49DC321AF0D8743CEF1B75D1452'



## Example - Response





{
    "data": {
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

[](https://dev.sprinklr.com/fetch-business-holiday-list-by-id) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-business-holiday-list-by-id)
