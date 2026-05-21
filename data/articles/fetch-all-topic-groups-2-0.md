---
title: "Fetch All Topic Groups 2.0"
slug: fetch-all-topic-groups-2-0
url: https://dev.sprinklr.com/fetch-all-topic-groups-2-0
---

# Fetch All Topic Groups 2.0

#
  GET - Fetch All Topic Groups


This API enables you to fetch the list of all available configured topic groups and topics.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/listening-topic-group/all

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

## Example - Request




 Copy Code


curl -X GET \
   https://api3.sprinklr.com/{env}/api/v2/listening-topic-group/all \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'



## Example - Response




{
    "data": [
        {
            "id": "64e74dc1004a266a3c077952",
            "name": "test24th aug "
        },
        {
            "id": "65127da25417d02c3492e752",
            "name": "UGC"
        },
{
            "id": "6523a9462c3dab1c757536b5",
            "name": "SPE Stack Exchange"
        },
        {
            "id": "652bc152969f7826ca70983e",
            "name": "Prithvi"
        },
        {
            "id": "652cc111969f7826ca7996b3",
            "name": "World Cup"
        },
        {
            "id": "6549fef1fe9995744504aeee",
            "name": "#coke"
        },
        {
            "id": "654b2a0cbf54f26681aff0ab",
            "name": "Darshil Testing"
        },
        {
            "id": "654b5eb53489437393e51e88",
            "name": "Topic group 1"
        },
        {
            "id": "654b640e6d4442041ba1ba16",
            "name": "11aa"
        },
        {
            "id": "65549e8ffc8b90462e6a1004",
            "name": "testing"
        },
        {
            "id": "655b5e15acd38117ad0094d0",
            "name": "FM test"
        },
  {
            "id": "655b5e9cacd38117ad00f3e3",
            "name": "FM test2"
        },
        {
            "id": "657786e4e804207bc0b50181",
            "name": "Test_HP"
        },
        {
            "id": "657880a2a28d3a2c92dd151c",
            "name": "Anant G 1"
        }
    ],
    "errors": []
}





### Response Schema

A successful API response will return a 200 OK status code along with the following response schema:




































| Parameters | Sub-Parameters | Description | Type |
| --- | --- | --- | --- |
| data |  | Main object containing all the listening topic details. | Array of Objects |
|  | id | Listening Topic Group Id, the unique identifier of the Topic Group. | String |
|  | name | Topic Group name. | String |
| errors |  | Array of error objects, if any | Array of Objects |

[](https://dev.sprinklr.com/fetch-all-topic-groups-2-0)




[Back to top](https://dev.sprinklr.com/fetch-all-topic-groups-2-0)
