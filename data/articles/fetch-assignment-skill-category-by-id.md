---
title: "Fetch Assignment Skill Category by Id"
slug: fetch-assignment-skill-category-by-id
url: https://dev.sprinklr.com/fetch-assignment-skill-category-by-id
---

# Fetch Assignment Skill Category by Id

#
  GET - Fetch Assignment Skill Category by Id


Use this API to fetch the details of a skill category.


## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/unified-routing/skill-category/{skill_category_id}


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












[Fetch Assignment Skill Category by Name](https://dev.sprinklr.com/fetch-assignment-skill-category-by-name)




| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {skill_category_id} | Required | The Id of the skill category for which you want to retrieve the details.  				You can use the  API to retrieve the skill category ID. The name of the skill category can be found in the Sprinklr UI. | String |

## Example - Request




 Copy Code



curl -X GET \
  'https://api3.sprinklr.com/{env}/api/v2/unified-routing/skill-category/64df382ecf307e061ae6b824' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Accept: application/json'





## Example - Response




{
    "data": {
        "id": "64df382ecf307e061ae6b824",
        "name": "test",
        "description": "te",
        "skills": [
            {
                "id": "65c5b9b3e3277779b28b9e4d",
                "skill": "new skill vp",
                "skillCategory": "64df382ecf307e061ae6b824",
                "createdTime": 1722514751893,
                "modifiedTime": 1736059969115
            },
            {
                "id": "676293dfceeb6d36a05d90eb",
                "skill": "hello, hi",
                "skillCategory": "64df382ecf307e061ae6b824",
                "createdTime": 1734513631534,
                "modifiedTime": 1734513631534
            },
            {
                "id": "676295f078314077fc93ac29",
                "skill": "hello test skill",
                "description": "dummy 2 desc",
                "skillCategory": "64df382ecf307e061ae6b824",
                "createdTime": 1734514160380,
                "modifiedTime": 1734960401889
            },
            {
                "id": "6790df41e225ac6b5bca2f76",
                "skill": "High-A_English",
                "skillCategory": "64df382ecf307e061ae6b824",
                "createdTime": 1737547585564,
                "modifiedTime": 1737547585564
            },
            {
                "id": "6790df86e225ac6b5bca36c6",
                "skill": "A_English",
                "skillCategory": "64df382ecf307e061ae6b824",
                "createdTime": 1737547654122,
                "modifiedTime": 1737547654122
            },
            {
                "id": "6790df8c1747217be3a0da74",
                "skill": "A_Hindi",
                "skillCategory": "64df382ecf307e061ae6b824",
                "createdTime": 1737547660662,
                "modifiedTime": 1737547660662
            },
            {
                "id": "679722c8f4185a22aea6cd45",
                "skill": "Voice Call",
                "description": "This is for voice call skill.",
                "skillCategory": "64df382ecf307e061ae6b824",
                "createdTime": 1737958088782,
                "modifiedTime": 1737958088782
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
| skills | List of skills associated with this category. Each skill has its own object with details. For the skill description, refer to the skills table. | Array of Objects |
| shareConfigs | Array for share configurations. | Array |


The following table describes the `skills` object parameters.



| Parameter | Description | Type |
| --- | --- | --- |
| id | Unique identifier for the skill. | String |
| skill | Name of the skill. | String |
| description | Description of the skill. | String |
| skillCategory | The Id of the skill category to which the skill belongs. | String |
| createdTime | Timestamp of when the skill was created. | Epoch |
| modifiedTime | Timestamp of when the skill was last modified. | Epoch |

[](https://dev.sprinklr.com/fetch-assignment-skill-category-by-id)






[Back to top](https://dev.sprinklr.com/fetch-assignment-skill-category-by-id)
