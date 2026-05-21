---
title: "Delete Business Hour"
slug: delete-business-hour
url: https://dev.sprinklr.com/delete-business-hour
---

# Delete Business Hour

#   DELETE Delete Business Hour
 

This API allows you to delete a specific business hours configuration in Sprinklr using its unique Id. This Id is generated when the configuration is created.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/business-hours/`{business_hours_id}`

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













     [Create Business Hour API](https://dev.sprinklr.com/create-business-hour)



| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {business_hours_id} | Required | The Id of the business hours configuration you created. You can obtain this Id from the response of the . | String |

## Example - Request




 Copy Code



curl --location --request DELETE 'https://api3.sprinklr.com/{env}/api/v2/business-hours/685cbc1b8a018e4528962cdb' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data ''



## Example - Response





204
No Content



**Dev Notes:** A `204 No Content` response indicates that the business hours configuration was successfully deleted.

[](https://dev.sprinklr.com/delete-business-hour) 

 

 
[Back to top](https://dev.sprinklr.com/delete-business-hour)
