---
title: "Generate Knowledge Base Sitemap"
slug: generate-knowledge-base-sitemap
url: https://dev.sprinklr.com/generate-knowledge-base-sitemap
---

# Generate Knowledge Base Sitemap

#
  GET - Generate Knowledge Base Sitemap



The Generate Knowledge Base Sitemap API generates and returns the sitemap for the articles matching with the specified request.

## API Endpoint


https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/generate-sitemap

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

### Query Parameters

























- ********
- ****
- ****
[Search by Entity](https://dev.sprinklr.com/search-by-entity)








``














****
****







****
****




| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| searchRequest |  | Optional | An object used to specify criteria for searching articles. It contains a list of filters to narrow down the articles you want to add to the sitemap. | Object |
|  | filters | Optional | An array containing the list of nested filters based on which you want to search and add the articles to the sitemap.   filterType: The type of filter you want to apply. For supported filter types, see the Filter Types table below.   field: The field based on which you want to filter the list of articles. Supported fields:    values: The values of the field based on which you want to filter the articles.  The filter format is the same as the format used in the  endpoint. | Object |
| baseUrl |  | Required | Specify the domain. All articles matching the request must have the same domain in their external permalink as the domain defined in baseUrl. Example: https://sprinklr.com/help | String |
| modelId |  | Optional | If specified, only the articles matching the filters from the modelIds will be considered for generating the sitemap. |  |
| changeFrequency |  | Optional | Indicates how frequently the content is likely to change.         Possible values: ALWAYS, HOURLY, DAILY, WEEKLY, MONTHLY, YEARLY, NEVER.         Default value: MONTHLY | String |
| priority |  | Optional | Priority of the article in the sitemap relative to other URLs.         Possible values: 0.0 to 1.0 (in 0.1 increments).         Default value: 1.0 | Number |

### Filter Types - Description







| Filter Type | Description |
| --- | --- |
| AND | Similar to boolean AND. It is added where more than one filter exists and returns values that meet all filter conditions. |
| OR | Similar to boolean OR. It is added where more than one filter exists and returns values that meet at least one filter condition. |
| NOT | Similar to boolean NOT, i.e., it returns values where that do not match the applied filter conditions. |
| IN | Returns resources where the key matches with any of the values mentioned in the list of values |
| GT (greater than) | Returns resources where the key is greater than the value/s mentioned in the list of values |
| GTE (Greater than equal to) | Returns resources where the key is greater than equal to the value/s mentioned in the list of values |
| LT (Less than) | Returns resources where the key is less than the value/s mentioned in the list of values |
| LTE (Less than equal to) | Returns resources where the key is less than equal to the value/s mentioned in the list of values |
| NIN (Not In) | Returns resources where the key does not match with the values mentioned in the list of values |
| EQUALS | Returns resources where the given key is equal to the value/s mentioned in the list of values |
| NOT_EQUALS | Returns resources where the given key is not equal to the value/s mentioned in the list of values |
| CONTAINS | Returns resources where the given key contains the values mentioned in the list of values |

**Dev Notes: **Only articles that match the specified request and have an external permalink will be included in the sitemap. Articles that meet the criteria but do not have an external permalink will be excluded from the sitemap.

### Example - Request




 Copy Code



curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/generate-sitemap' \
--header 'Authorization: Bearer ' \
--header 'Key: ' \
--header 'Content-Type: application/json'
--data-raw '{
    "searchRequest": {
        "filters": [
            {
                "filterType": "IN",
                "field": "KB_CONTENT_ID",
                "values": [
                    "6560dfd8304efa11575fe3d7"
                ]
            }
        ]
    },
    “modelId”:””,
    "baseUrl": "https://help.sprinklr.com",
    "changeFrequency": "MONTHLY",
    "priority": 1
}'
 

     
     
   

### Example - Response




{
"data": {
"URL": "https://storage.googleapis.com/spr-qa6-cdn/KNOWLEDGE_BASE_SITEMAP_66000000_1702124035731.xml",
"errors": [
"[KNOWLEDGE_BASE_SITEMAP] Error while generating sitemap for kb content: 657459822448a75527347bcc, Reason : Domain of URL https://help.dd.com/with-externa-permalink-55555 doesn't match base URL https://help.sprinklr.com"
]
},
"errors": []
}
 

     
     
   


### Response Parameters































| Parameter | Sub-Parameter | Description |
| --- | --- | --- |
| data |  | The object containing the sitemap URL and any errors that might have occurred. |
|  | URL | The URL of the generated sitemap XML file. |
|  | errors | Errors that occurred while generating the sitemap. |
| errors |  | Errors that might have occurred other than the errors related to the sitemap. |

[](https://dev.sprinklr.com/generate-knowledge-base-sitemap) 

 

 
[Back to top](https://dev.sprinklr.com/generate-knowledge-base-sitemap)
