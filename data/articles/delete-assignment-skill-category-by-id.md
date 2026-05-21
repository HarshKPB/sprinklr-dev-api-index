---
title: "Delete Assignment Skill Category by Id"
slug: delete-assignment-skill-category-by-id
url: https://dev.sprinklr.com/delete-assignment-skill-category-by-id
---

# Delete Assignment Skill Category by Id

#
  DELETE - Delete Assignment Skill Category by Id


Use this API to delete a skill category.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/unified-routing/skill-category/{id}


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
















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | The unique identifier of the skill category. | String |

## Example - Request




 Copy Code



curl -X DELETE \
  'https://api2.sprinklr.com/{env}/api/v2/unified-routing/skill-category/67974809f4185a22aea9fc99' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}'





## Example - Response




{
    "data": true,
    "errors": []
}





The 200 OK response indicates that the skill category has been deleted.

[](https://dev.sprinklr.com/delete-assignment-skill-category-by-id)






[Back to top](https://dev.sprinklr.com/delete-assignment-skill-category-by-id)
