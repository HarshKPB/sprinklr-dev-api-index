---
title: "Delete Business Holiday List"
slug: delete-business-holiday-list
url: https://dev.sprinklr.com/delete-business-holiday-list
---

# Delete Business Holiday List

#   DELETE Delete Business Holiday List
 

This API allows you to delete a business holiday list from Sprinklr.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/business-holidays/`{business_holiday_list_id}`

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














[Create Business Holiday List](https://dev.sprinklr.com/create-business-holiday-list)



| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {business_holiday_list_id} | Required | Id of the business holiday list that you want to delete. You can get this Id from the response of the  API. | String |

## Example - Request




 Copy Code


curl -X DELETE 'https://api3.sprinklr.com/{env}/api/v2/business-holidays/686610af0791710f2810c945' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json'



## Example - Response





204
No Content



**Dev Notes: **A `204 No Content` response indicates that the holiday list was successfully deleted.

[](https://dev.sprinklr.com/delete-business-holiday-list) 

 

 
[Back to top](https://dev.sprinklr.com/delete-business-holiday-list)
