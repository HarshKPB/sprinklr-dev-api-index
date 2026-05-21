---
title: "Fetch Accessible Workspaces"
slug: fetch-accessible-workspaces
url: https://dev.sprinklr.com/fetch-accessible-workspaces
---

# Fetch Accessible Workspaces

#
  GET - Fetch Accessible Workspaces


Using this API, you can fetch the details of all the workspaces the user has access to, with respect to the partner Id for which the token was generated.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/client/accessible-clients


### Headers

API headers include the mandatory information that you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











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
 'https://api3.sprinklr.com/{env}/api/v2/client/accessible-clients' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'



## Example - Response




{
    "data": [
        {
            "id": "4706",
            "name": "App_Client1"
        },
        {
            "id": "4707",
            "name": "App_Client2"
        },
        {
            "id": "4708",
            "name": "App_Client3"
        },
        {
            "id": "7019",
            "name": "App_Client4"
        }
    ],
    "errors": []
}



### Response Parameters





























| Parameter | Sub-Param | Definition | Type |
| --- | --- | --- | --- |
| data |  | Array describing the id and the name of the user in the respective workspace environment | Array |
|  | id | Refers to the respective workspace id | Integer |
|  | name | Refers to the respective workspace name | String |

[](https://dev.sprinklr.com/fetch-accessible-workspaces)




[Back to top](https://dev.sprinklr.com/fetch-accessible-workspaces)
