---
title: "Delete Survey Response"
slug: delete-survey-response
url: https://dev.sprinklr.com/delete-survey-response
---

# Delete Survey Response

#
  DELETE Delete Survey Response

This API allows you to delete a specific survey response using its unique ID.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/survey-response/`{survey-response-id}`

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

### Path Parameters



















| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| {survey-response-id} | Required | String | Unique identifier of the survey response. |



**Steps to Retrieve Survey Response Id from Sprinklr UI**


- Open Customer Feedback Management (CFM) persona app in Sprinklr.

- In the **Programs** tab, locate the survey of which you want to fetch the responses.

- Hover over the survey. A **View** button is displayed.

- Click **View**.

- On the top bar, click **Responses**.

The **Response Id** column values correspond to `survey-response-id`.

## Example - Request




 Copy Code


curl --location --request DELETE 'https://api3.sprinklr.com/{env}/api/v2/survey-response/68b6bd55ccda6f5475acf933' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Enter Your Access Token}'



## Example - Response




{
    "data": "Survey response deleted successfully.",
    "errors": []
}





  [](https://dev.sprinklr.com/delete-survey-response)




[Back to top](https://dev.sprinklr.com/delete-survey-response)
