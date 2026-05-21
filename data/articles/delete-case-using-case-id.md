---
title: "Delete Case Using Case Id"
slug: delete-case-using-case-id
url: https://dev.sprinklr.com/delete-case-using-case-id
---

# Delete Case Using Case Id

#
  POST - Delete Case Using Case Id


Using this API, you can delete a case using the case Id, i.e., the unique identifier for the case.

## API Endpoint

	https://api3.sprinklr.com`/{env}/`api/v2/case/delete

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
| caseIds | Required | Refers to the list of case Ids associated with the cases you want to delete | List [String] |

## Example - Request

Copy Code


curl -X POST \
   'https://api3.sprinklr.com/{env}/api/v2/case/delete' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
        "65bca12b3c4a8a365471a6d5"
      ]



## Example - Response




HTTP/1.1 204 (No Content)



[](https://dev.sprinklr.com/delete-case-using-case-id)




[Back to top](https://dev.sprinklr.com/delete-case-using-case-id)
