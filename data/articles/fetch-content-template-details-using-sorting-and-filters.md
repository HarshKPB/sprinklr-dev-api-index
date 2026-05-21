---
title: "Fetch Content Template Details Using Sorting and Filters"
slug: fetch-content-template-details-using-sorting-and-filters
url: https://dev.sprinklr.com/fetch-content-template-details-using-sorting-and-filters
---

# Fetch Content Template Details Using Sorting and Filters

#
	 POST Fetch Content Template Details Using Sorting and Filters

This API helps fetch content template id and name details using sorting and filter values.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/contentTemplate/searchContentTemplates

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

****

****

| Parameters | Sub-Params | Required/Optional | Definition | Type |
| --- | --- | --- | --- | --- |
| sorts |  | Optional | Sorting filter that specifies the arrangement of data in response | Array |
|  | key |  | Defines the filter for sorting the dataExample: MODIFIED_TIME will help you sort the response for templates w.r.t the respective modified time | String |
|  | order |  | The order of data in the responseExample: ASC for ascending and DESC for descending | String |
| page |  | Optional | If the response size is large, page parameters helps limit the number of items in the response | Object |
|  | page |  | Helps specify the page number you want in the responseIf the field has no value, the first page results are gathered in the response | Integer |
|  | size |  | Specifies the number of results in the response | Integer |
| filters |  | Required | Specifies the information for filtering the data in the response | List[String] |
|  | field | Optional | Specifies the fields you want the data filtered forExample: TEMPLATE_TYPE, PUBLISHER_STATUS | String |
|  | filterType | Optional | Defines the type of filter appliedSupported Filter Types: IN, GT, GTE, LT, LTE, NIN, BETWEEN, STARTS_WITH, CONTAINS, EQUALS , FILTER, EXISTS | String |
|  | values | Optional | Specifies the values the data is getting compared against | List [String, Integer] |

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
      
 
curl -X POST\
   'https://api3.sprinklr.com/{env}/api/v2/contentTemplate/searchContentTemplates' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
{
"sorts": [
   {
       "key":"MODIFIED_TIME",
       "order":"DESC"
   }
            ],
"page":
  {
        "page":0,
        "size":5
  },
"filters": [
  {
        "field":"TEMPLATE_TYPE",
        "filterType":"IN",
        "values":["CONTENT_TEMPLATE"]
   },
             ]
}'
 

     
     
   

## Example - Response

 
 
     
 
 {
    "data": {
        "searchResults": [
            {
                "id": "628c7e112bd3813141428b48",
                "name": "TemplateTest1"
            },
            {
                "id": "628b5fc8e105dd4d8f769e0b",
                "name": "TemplateTest2"
            },
            {
                "id": "6287479f2bd38131412b3aff",
                "name": "TemplateTest3"
            },
            {
                "id": "62836448931f3177715c2ef5",
                "name": "TemplateTest4"
            },
            {
                "id": "6283478be105dd4d8f97ef8e",
                "name": "TemplateTest5"
            }
],
    "hasMore": true,
    "totalHits": 320
    },
    "errors": []
}
 

     
     
   
 

### Response Parameters






















| Parameters | Sub-Params | Definition | Type |
| --- | --- | --- | --- |
| searchResults |  | Array that holds the details such as id and name of the content templates | Array |
|  | id | Id of the content template | String |
|  | name | The name of the content template | String |
| hasMore |  | If true, it implies that there are more content templates than that displayed in the result | Boolean |
| totalHits |  | Specifies the total number of content templates present that can be fetched using this request | Integer |

**Dev Notes: **If the request has no sorting or filters applied and has a pair of empty curly brackets, i.e., `**{}**`, then the response will show details for all the content templates available on a single page. By default, the size of response per page is equal to 100.

	[](https://dev.sprinklr.com/fetch-content-template-details-using-sorting-and-filters) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-content-template-details-using-sorting-and-filters)
