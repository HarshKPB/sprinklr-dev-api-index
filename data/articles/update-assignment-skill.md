---
title: "Update Assignment Skill"
slug: update-assignment-skill
url: https://dev.sprinklr.com/update-assignment-skill
---

# Update Assignment Skill

#
  PUT - Update Assignment Skill

Use this API to update an assignment skill.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/unified-routing/skill


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

### Request Parameters




























| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| skill | Required | Name of the skill. | String |
| description | Optional | The description of the skill. | String |
| skillCategory | Optional | The category of the skill. | String |

## Example - Request




 Copy Code



curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/unified-routing/skill' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'\
  -d '{
        "skill": "Voice Skill",
        "description": "This is a new description.",
        "skillCategory": "64df382ecf307e061ae6b824"
    }'





## Example - Response




{
    "data": {
        "id": "679724accced544cfa9e2d02",
        "skill": "Voice Skill",
        "description": "This is a new description.",
        "skillCategory": "64df382ecf307e061ae6b824",
        "createdTime": 1737958572032,
        "modifiedTime": 1737958572032
    },
    "errors": []
}





## Response Parameters



| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the skill. | String |
| skill | Name of the skill. | String |
| description | Description of the skill. | String |
| skillCategory | The Id of the skill category to which the skill belongs. | String |
| createdTime | Timestamp of when the skill was created. | Epoch |
| modifiedTime | Timestamp of when the skill was last modified. | Epoch |

[](https://dev.sprinklr.com/update-assignment-skill)






[Back to top](https://dev.sprinklr.com/update-assignment-skill)
