---
title: "Fetch Skills and Proficiency"
slug: fetch-skills-and-proficiency
url: https://dev.sprinklr.com/fetch-skills-and-proficiency
---

# Fetch Skills and Proficiency

# GET Fetch Skills and Proficiency

This API call is related to modern care’s [skills based routing](https://www.sprinklr.com/help/articles/setting-up-assignment-engine-legacy/skill-based-routing/64045b5b32d12b63c5f5674f), which is an assignment strategy to assign messages/cases to the most suitable agent, instead of simply choosing the next available agent. Through this API call, you will be able to fetch the skill id and proficiency score of an agent.


## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/user-settings/assignment-config/{userId}

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











			[user search API](https://dev.sprinklr.com/v1-user-search)





| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {userId} | Required | The user id you receive in the response of .Alternatively, you can also retrieve user id from Sprinklr's UI platform | Integer |

### Example - Request



 Copy Code


curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/user-settings/assignment-config/600001230' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'



### Example - Response





{
    "data": {
        "userId": "600001230",
        "capacities": [],
        "proficiencies": {
            "skillVsProficiency": {
                "5f6992783f0c3d580df820b4": 40,
                "5eaff2c302ec853f2150258f": 100,
                "5fbfc48accb38e37b031cb65": 42,
                "5e9fdead02ec853ab5c73c78": 100,
                "5eaff2cb02ec853f21502679": 100,
                "5ede78c522098613e5dfd9c8": 56,
                "6194d2696317ad7b91e67c5g": 10,
                "5ee78b36861c7b3cc829b706": 25,
                "5ee78b9a861c7b3cc829bfgd": 100
            }
        }
    },
    "errors": []
}



### Response Parameters












****

****

| Parameter | Sub-Param | Description | Type |
| --- | --- | --- | --- |
| userId |  | The user id used in the request URI | Integer |
| capacities |  | Object defining the capacity of new cases/messages an agent can handle in a given timeInference: If the capacity is 5, agent cannot handle more than 5 cases | Object |
| proficiencies |  | Object with information on skill ids and the respective proficiency score | Object |
|  | skillvsProficiency | List of skill ids along with its respective proficiency scoreSkill Id refers to the unique identifier for a particular skillProficiency score refers to the proficiency level of the user in a particular skillProficiency score range: 1 - 100 | String, Integer |

**Dev Notes:**To view the particular skill associated with the Skill Id in the response, refer to [lookup by Id](https://dev.sprinklr.com/lookup-by-id) API documentation. Use `ASSIGNMENT_SKILL` as the lookup type.

[](https://dev.sprinklr.com/fetch-skills-and-proficiencyl) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-skills-and-proficiency)
