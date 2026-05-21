---
title: "Fetch Assignment Skill by Name"
slug: fetch-assignment-skill-by-name
url: https://dev.sprinklr.com/fetch-assignment-skill-by-name
---

# Fetch Assignment Skill by Name

#
  GET - Fetch Assignment Skill by Name

Use this API to get the details of an assignment skill by its name.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/unified-routing/skill?name={skill_name}


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
| {skill_name} | Required | Name of the skill for which you want to fetch details. You can get the skill name from the Sprinklr UI. | String |

## Example - Request




 Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/unified-routing/skill?name=English' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Accept: application/json'





## Example - Response




{
    "data": {
        "id": "64f055a22e9f7a0625dc5b03",
	      "skill": "English",
	      "skillCategory": "64f055a22e9f7a0625dc5b02",
	      "createdTime": 1712053089874,
	      "modifiedTime": 1736059969057
    },
    "errors": []
}





## Response Parameters



| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the skill. | String |
| skill | Name of the skill. | String |
| skillCategory | The Id of the skill category to which the skill belongs. | String |
| createdTime | Timestamp of when the skill was created. | Epoch |
| modifiedTime | Timestamp of when the skill was last modified. | Epoch |

[](https://dev.sprinklr.com/fetch-assignment-skill-by-name)






[Back to top](https://dev.sprinklr.com/fetch-assignment-skill-by-name)
