---
title: "Update Proficiency or Remove Skills"
slug: update-proficiency-or-remove-skills
url: https://dev.sprinklr.com/update-proficiency-or-remove-skills
---

# Update Proficiency or Remove Skills

# PUT Update Proficiency or Remove Skills

This API call is related to modern care’s [skills based routing](https://www.sprinklr.com/help/articles/setting-up-assignment-engine-legacy/skill-based-routing/64045b5b32d12b63c5f5674f), which is an assignment strategy to assign messages/cases to the most suitable user/agent, based on their respective proficiency score. Through this API call, you will be able to:

- [Update the proficiency score of the user/agent](https://dev.sprinklr.com/update-proficiency-or-remove-skills/)

- [Remove the skills of the user/agent](https://dev.sprinklr.com/update-proficiency-or-remove-skills/)

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/user-settings/assignment-config/{userId}

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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Parameters











****

| Parameter | Sub-Param | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| capacities |  | Optional | Array defining the capacity of work an agent can handle (new and active conversations) in a given time | Array |
|  | id |  | Refers to the capacity name | String |
|  | capacity |  | Capacity of new cases/messages an agent can handle w.r.t new conversationsExample:If the capacity is 5, agent can handle 5 cases at max for new conversations | Integer |
|  | activeConversationCapacity |  | Refers to the capacity for the assignment of active conversations | Integer |
| capacitiesToRemove |  | Optional | Refers to the object defining the capacities you want to update/remove | Object |
| proficiencies |  | Required | Object defining the proficiency details | Object |
|  | skillVsProficiency | Required | Object defining the updated proficiency score for a particular skill id | Object |
|  | languageVsProficiency | Optional | Object defining the updated proficiency score w.r.t language | Object |
|  | channelVsProficiency | Optional | Object defining the updated proficiency score w.r.t channel | Object |
| skillsToRemove |  | Required for removing skillsOptional for updating skills | List with details of skill ids you want to remove | List [String] |
| languagesToRemove |  | Optional | List with details of languages to remove | List [String] |
| channelsToRemove |  | Optional | List with details of channels to remove | List [String] |

## Example - Request for Updating Proficiency Score



 Copy Code


curl -X PUT \
 'https://api3.sprinklr.com/{env}/api/v2/user-settings/assignment-config/600001230' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
{
   "capacities": [
{
               "id": "default",
               "capacity": 2,
               "activeConversationCapacity": 2
           }
],
   "capacitiesToRemove":["default"],
   "proficiencies":{
       "skillVsProficiency":{
                      "5ede78c522098613e5dfd9c9":56,
                      "5ee78b36861c7b3cc829b706":25,
                      "5fbfc48accb38e37b031cb65":42
                   },
       "languageVsProficiency":{},
       "channelVsProficiency":{}
   },
   "skillsToRemove":[""],
   "languagesToRemove":[""],
   "channelsToRemove":[""]
}'



## Example - Response for Updating Proficiency Score





{
    "data": {
        "userId": "6000001230",
        "capacities": [],
        "proficiencies": {
            "skillVsProficiency": {
                "5f6992783f0c3d580df821b4": 40,
                "5eaff2c302ec853f2150258f": 100,
                "5fbfc48accb38e37b031cb65": 42,
                "5eaff2cb02ec853f21502568": 100,
                "5ede78c522098613e5dfd9c9": 56,
                "5ee78b36861c7b3cc829b706": 25
 }
        }
    },
    "errors": []
}



## Example - Request for Removing Skills



 Copy Code


curl -X PUT \
 'https://api3.sprinklr.com/{env}/api/v2/user-settings/assignment-config/600001230' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
{
   "capacities":
[
{
               "id": "default",
               "capacity": 2,
               "activeConversationCapacity": 2
           }],
   "capacitiesToRemove":["default"],
   "proficiencies":{
       "skillVsProficiency":{},
       "languageVsProficiency":{},
       "channelVsProficiency":{}
   },
   "skillsToRemove":["5ede78c522098613e5dfd9c9","5ee78b36861c7b3cc829b706","5fbfc48accb38e37b031cb65"],
   "languagesToRemove":[""],
   "channelsToRemove":[""]
}'



## Example - Response for Removing Skills





{
    "data": {
        "userId": "600000003",
        "capacities": [],
        "proficiencies": {
            "skillVsProficiency": {
                "5f6992783f0c3d580df821b3": 40,
                "5eaff2c302ec853f2150258f": 100,
                "5e9fdead02ec853ab5c73c78": 100,
                "5eaff2cb02ec853f21502679": 100
              }
        }
    },
    "errors": []
}



**Dev Notes:**To view the particular skill associated with the Skill Id in the response, refer to [lookup by Id](https://dev.sprinklr.com/lookup-by-id) API documentation. Use `ASSIGNMENT_SKILL` as the lookup type.

### Response Parameters












****

****

| Parameter | Sub-Param | Description | Type |
| --- | --- | --- | --- |
| userId |  | The user id used in the request URI | Integer |
| capacities |  | Object defining the capacity of new cases/messages an agent can handle in a given timeInference: If the capacity is 5, agent cannot handle more than 5 cases | Object |
| proficiencies |  | Object with information on skill ids and the respective proficiency score | Object |
|  | skillvsProficiency | List of skill ids along with its respective proficiency scoreSkill Id refers to the unique identifier for a particular skillProficiency score refers to the proficiency level of the user in a particular skillProficiency score range: 1-100 | String, Integer |

[](https://dev.sprinklr.com/update-proficiency-or-remove-skills) 

 

 
[Back to top](https://dev.sprinklr.com/update-proficiency-or-remove-skills)
