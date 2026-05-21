---
title: "Delete User (SCIM)"
slug: delete-user-scim
url: https://dev.sprinklr.com/delete-user-scim
---

# Delete User (SCIM)

#  DELETE  Delete User (SCIM)


Using this API, you can delete/deprovision a user from the Sprinklr platform.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/scim/Users/{userId}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/scim+json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

## Path Paramenter
















[search by entity](https://dev.sprinklr.com/search-by-entity)[read user by User Name](https://dev.sprinklr.com/fetch-user-by-email-id)[bootstrap API](https://dev.sprinklr.com/v1-bootstrap-resources/)

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| userId | Required | Refers to the unique identifier for the user whose details need to be deleted.You can use ,  API, or  to fetch the user Id details | Integer |

## Example - Request



 Copy Code



curl -X DELETE \
  'https://api3.sprinklr.com/{env}/api/v1/scim/v2/Users/66009014' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/scim+json' \
  -H 'key: {apikey}'



## Example - Response




>204 No Content



**Dev Notes: **`204 No Content` implies that the user has been successfully deleted.

[](https://dev.sprinklr.com/delete-user-scim) 

 

 
[Back to top](https://dev.sprinklr.com/delete-user-scim)
