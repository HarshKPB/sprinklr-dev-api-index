---
title: "Merge Cases"
slug: merge-cases
url: https://dev.sprinklr.com/merge-cases
---

# Merge Cases

#
  POST - Merge Cases


Often, customers raise multiple tickets for similar issues. To make agents work efficiently, these similar cases can be merged so that only one agent can handle the case end-to-end and provide faster resolution.


Using this API, you can merge cases where one of the cases would be the parent case and the merged ones would be the child cases. The conversations of the child cases would be visible on the parent case as agent notes.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/case/merge-cases

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












****

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| parentCaseNumber | Required | Refers to the case number in which you want to merge other cases | Integer |
| childCaseNumbers | Required | Refers to the list of cases numbers that need to be merged to the parent caseNote: You can merge one or more cases without any limitation | List [Integer] |

## Example - Request




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/case/merge-cases' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "parentCaseNumber": 6998806,
    "childCaseNumbers": [
        7000547
    ]
}'





## Example - Response




204 No Content





**Dev Notes: **204 No Content Implies that the cases have been successfully merged.

[](https://dev.sprinklr.com/merge-cases)




[Back to top](https://dev.sprinklr.com/merge-cases)
