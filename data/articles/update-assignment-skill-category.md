---
title: "Update Assignment Skill Category"
slug: update-assignment-skill-category
url: https://dev.sprinklr.com/update-assignment-skill-category
---

# Update Assignment Skill Category

#
  PUT - Update Assignment Skill Category

Use this API to update a skill category.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/unified-routing/skill-category


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































****
****




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| id | Required | Unique identifier for the skill category. | String |
| name | Required | The name of the skill category. | String |
| description | Optional | A description of the skill category. | String |
| skills | Optional | A list of skills that you want to add to the skill category. Each object in the array represents an individual skill.For each skill, mention these details: 				skill: The name of a specific skill. 				description: A description of the skill. | String |

## Example - Request




 Copy Code



curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/unified-routing/skill-category' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json'\
  -d '{
        "id": "67974809f4185a22aea9fc99",
        "name": "Live Chat Skills",
        "description": "This is the category for Live Chat skills.",
        "skills": [
          {
            "skill": "Enable attachments capability",
            "description": "This the skill for enabling attachments capability within Live Chat."
          },
          {
            "skill": "Customize Live Chat",
            "description": "Customize Live Chat according to customer requirements."
          },
          {
            "skill": "Configure Guided Flow",
            "description": "This the skill for configuring guided flow in Live Chat."
          }
        ]
    }'





## Example - Response




{
    "data": {
        "id": "67974809f4185a22aea9fc99",
        "name": "Live Chat Skills",
        "description": "This is the category for Live Chat skills.",
        "skills": [
            {
                "skill": "Enable attachments capability",
                "description": "This the skill for enabling attachments capability within Live Chat.",
                "skillCategory": "67974809f4185a22aea9fc99",
                "createdTime": 0,
                "modifiedTime": 0
            },
            {
                "skill": "Customize Live Chat",
                "description": "Customize Live Chat according to customer requirements.",
                "skillCategory": "67974809f4185a22aea9fc99",
                "createdTime": 0,
                "modifiedTime": 0
            },
            {
                "skill": "Configure Guided Flow",
                "description": "This the skill for configuring guided flow in Live Chat.",
                "skillCategory": "67974809f4185a22aea9fc99",
                "createdTime": 0,
                "modifiedTime": 0
            }
        ],
        "shareConfigs": []
    },
    "errors": []
}





## Response Parameters





| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the skill category. | String |
| name | Name of the skill category. | String |
| description | Description of the skill category. | String |
| skills | List of skills associated with this category. Each skill has its own object with details. | Array of Objects |
| shareConfigs | Array for share configurations. | Array |


The following tabe describes the `skills` object parameters:



| Parameter | Description | Type |
| --- | --- | --- |
| skill | Name of the skill. | String |
| description | Description of the skill. | String |
| skillCategory | The Id of the skill category to which the skill belongs. | String |
| createdTime | Timestamp of when the skill was created. | Epoch |
| modifiedTime | Timestamp of when the skill was last modified. | Epoch |

[](https://dev.sprinklr.com/update-assignment-skill-category)






[Back to top](https://dev.sprinklr.com/update-assignment-skill-category)
