---
title: "Listening Topics v1"
slug: listening-topics-v1
url: https://dev.sprinklr.com/listening-topics-v1
---

# Listening Topics v1

#
  GET Listening Topics



Get the list of all available configured topic groups and topics. The API returns the minimal information on topic groups and topics along with the keywords used while creating the topic id in query param.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v1/listening/topics

**Dev Notes: **Topic description in available in API response but when description is empty for a Topic, you will not get "description" key in the response

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.















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


## Example















Copy Code



curl -X GET \
  'https://api3.sprinklr.com{env}api/v1/listening/topics' \
  -H 'Authorization: Bearer {token}' \
  -H 'cache-control: no-cache' \
  -H 'key: {apikey}'






### Example - Response





	{
   "status":"SUCCESS",
   "response":{
      "topicGroups":[
         {
            "id":"brands",
            "name":"Brands"
         },
         {
            "id":"products",
            "name":"Products"
         },
	{
            "id":"5818dcd1e4b0eb64147912a0",
            "name":"Hospitality"
         },
         {
            "id":"595c5073e4b064e21f85cf64",
            "name":"Sprinklr"
         }
      ],
      "topics":[
         {
            "id":"595b8b78e4b00bd3a9a9c30a",
            "name":"Hashtag Inquiry",
            "topicGroup":"595b89fde4b00bd3a9a9be00",
            "tags":[
            ],
            "enabled":false,
            "displayName":""
         },
         {
                "id": "5d5be5c68a479852475771e9",
                "name": "Topic_Volumetric_Rule_Tarun",
                "topicGroup": "5d53d9dc8a479814d0f6455f",
                "description": "This topic is created to test the volumetric rule.",
                "tags": [],
                "enabled": true
          },
	  {
                "id": "5f9beabd6fcf2b678hg4fefe",
                "name": "locationBased",
                "topicGroup": "5f9beabd6fcf2b678hg4fefe",
                "tags": [],
                "modifiedTime": 1604050813052,
                "createdTime": 1604053034382,
                "enabled": false,
                "query": “((\”new\” OR (\”brand\” AND \”bikes\” AND \”launch\”) AND  NOT \"asfsdv\")",
                "dataSources": [
                    "TWITTER",
                    "FACEBOOK",
                    "INSTAGRAM",
                    "YOUTUBE
                ],
                "languageCodes": [],
                "countryCodes": []
            }
      ]
   }
}






	[](https://dev.sprinklr.com/listening-topics-v1)






[Back to top](https://dev.sprinklr.com/listening-topics-v1)
