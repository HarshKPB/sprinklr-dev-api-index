---
title: "Delete Case Using Case Number"
slug: delete-case-using-case-number
url: https://dev.sprinklr.com/delete-case-using-case-number
---

# Delete Case Using Case Number

#
  POST - Delete Case Using Case Number


Using this API, you can delete a case using the case number.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/case/case-numbers/delete

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
















| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| caseNumbers | Required | Refers to the list of case numbers associated with the cases you want to delete | List [String] |

## Example - Request




 Copy Code



curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/case/case-numbers/delete' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
        "7251064"
      ]





## Example - Response




HTTP/1.1 204 (No Content)





**Dev Notes: **204 No Content implies that the case has been deleted successfully. You can validate that the case has been deleted using [Read Case by Case Number API](https://dev.sprinklr.com/read-case-by-case-number), and check if "deleted" field is set to "true" in the API response.

[](https://dev.sprinklr.com/delete-case-using-case-number)




[Back to top](https://dev.sprinklr.com/delete-case-using-case-number)
