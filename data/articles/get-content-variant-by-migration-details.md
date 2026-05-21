---
title: "Get Content Variant by Migration Details"
slug: get-content-variant-by-migration-details
url: https://dev.sprinklr.com/get-content-variant-by-migration-details
---

# Get Content Variant by Migration Details

#
  GET - Get Content Variant by Migration Details



The Get Content Variant by Migration Details API retrieves the details of an article and its language variants based on specified migration details, country code, and locale. The response includes the matched article details along with its available country and language variants.


If the requested country-specific variant does not exist, the API fall backs to global country variant using the `fallbackToGlobalVariant` flag.

**Dev Notes: **You can use [Create Knowledge Base API](https://dev.sprinklr.com/create-knowledge-base-article) to set migration details for an article.

## API Endpoint


https://api3.sprinklr.com`/{env}/`api/v2/knowledgebase/find-variant-by-migration-details

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












****



[Create Knowledge Base Article](https://dev.sprinklr.com/create-knowledge-base-article)

[Create Knowledge Base Article](https://dev.sprinklr.com/create-knowledge-base-article)



****



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| resolveLinkedAssets | Required | Indicates whether to retrieve content along with its associated linked assets.Possible values: true, false | Boolean |
| migratedId | Required | Refers to the migration Id configured while creating the article using the  API. | String |
| migratedFrom | Required | Refers to the source from where the article is migrated and is configured while creating the article using the  API. | String |
| countryCode | Required | The country code of the country this article is created for. | String |
| locale | Required | The locale code of the language this article is created in. | String |
| fallbackToGlobalVariant | Required | Indicates whether to retrieve the global version of the content if the specified country or language variant is unavailable. Possible Values: true, false | Boolean |

### Example - Request




 Copy Code



curl -X GET \
  https://api3.sprinklr.com/{env}/api/v2/knowledgebase/find-content-by-migration-details?migratedId=hi_IN_test_migrated_id_api3&migratedFrom=SPRINKLR' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'
 

     
     
   

### Example - Response




{
{
  "data": {
    "mainBaseContent": {},
    "mainBaseLngVariants": {},
    "knowledgeBaseContent": {},
    "isFallbackResponse": false,
    "countryLngVariants": {},
    "countryVariants": {},
    "countryVariant": {},
    "errorMessage": "",
    “redirectAssetId” : ""
  }
},
    "errors": []
}
 

     
     
   


### Response Parameters























      ``











      ``````



| Field | Description |
| --- | --- |
| mainBaseContent | The main base content found for the specified migration details. |
| mainBaseLngVariants | A map of locale codes to corresponding language variant article Ids for different language translations of the main base content. |
| knowledgeBaseContent | The required article matching the specified country and locale in the API request. |
| isFallbackResponse | This is set to true if the country variant for the specified country code was not found and a fallback to the global country variant occurred. |
| lngVariants | A map of locale codes to corresponding language variant article Ids for other language translations. |
| countryVariants | A map of country codes to corresponding article IDs for other country variants. |
| errorMessage | Set when fallbackToGlobalVariant is enabled and a required country or language variant (including fallback) is not found.         If this occurs, mainBaseContent and mainBaseLngVariants may still be populated if available. |

[](https://dev.sprinklr.com/get-content-variant-by-migration-details) 

 

 
[Back to top](https://dev.sprinklr.com/get-content-variant-by-migration-details)
