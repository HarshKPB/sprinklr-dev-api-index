---
title: "Bulk-Translate Articles"
slug: bulk-translate-articles
url: https://dev.sprinklr.com/bulk-translate-articles
---

# Bulk-Translate Articles

#  POST  Bulk-Translate Articles

The Knowledge Base Translation API enables you to trigger translations of Knowledge Base articles into one or more target languages. You can use this API to translate a specific article or bulk‑translate content across all supported languages, helping you keep localized content up to date at scale. This API is designed for automation scenarios, such as integrating translation workflows into publishing pipelines or synchronizing multilingual content across regions.

**Note:** Before triggering the Bulk Translate API, ensure that language variants of the base article exist for the required languages. You can create or update these variants by using the [Update Knowledge Base Articles API](https://dev.sprinklr.com/update-knowledge-base-articles) with the `lngVariants` request parameter.

## Prerequisites

- You must have **Edit** permission under the **Knowledge Base** section of the **Service Cloud** module.

## API Endpoint


https://api3.sprinklr.com/`{env}`/api/v2/knowledgebase/bulk-translate

## Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allow access to protected resources.

``

[Authorize](https://dev.sprinklr.com/authorize)

``

[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)

``

``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the server.For generating authorization token, refer to  section on the developer portal. |
| Key | api-key | API key helps authenticate the application with the server.For generating API key, refer to  guide. |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body. |
| Accept | application/json | Determines the acceptable response type from the server. |

## Request Parameters

[Create Knowledge Base Article API](https://dev.sprinklr.com/create-knowledge-base-articles)

[this link](https://www.sprinklr.com/help/articles/translating-content/autotranslate-an-article/641adba2a1367f1be7db82d4)
****``

****``
****************

| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| contentIds | Required | String | Refers to the content IDs of the base articles you want to translate, which you can obtain from the  response or from the article URL when accessing the article from the Knowledge Base homepage. |
| locales | Optional | String |  |
| status | Optional | String | Specifies the status that articles will have after translation. Available options are DRAFT, APPROVED, and READY TO PUBLISH.  Note: If the status parameter is not provided in the payload, all articles will be saved in the DRAFT state by default.  Note: To set the status to APPROVED or READY TO PUBLISH, you must have Approve permission under the Knowledge Base section of the Service Cloud module. |

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/knowledgebase/bulk-translate' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Access_Token}' \
--header 'Key: {API_Key}' \
--data '{
  "contentIds": ["69bc0a51d3d3e04dfcfb4641", “69bc0a51d3d3e04dfcfb3628”],
  "locales": ["ar", "hi_IN"],
  "status": "APPROVED"
}'

## Example Response

{
    "data": "Your request to translate articles has been submitted",
    "errors": []
}

**Note:** The submitted request is processed asynchronously. After all auto‑translations are completed, Sprinklr sends a webhook indicating that the article auto‑translation was successful. In addition, each successful auto‑translation of a language variant triggers an update webhook.
