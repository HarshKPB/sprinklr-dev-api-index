---
title: "Preview Outbound Post"
slug: preview-outbound-post
url: https://dev.sprinklr.com/preview-outbound-post
---

# Preview Outbound Post

#  POST & GET  Preview Outbound Post

The Preview Outbound Post API allows you to generate and download previews of outbound posts before publishing. This API is useful for validating post formatting, appearance, and export output.

The workflow consists of two endpoints:

-  [Generate Outbound Post Preview API Endpoint](https://dev.sprinklr.com/preview-outbound-post#Generate-Outbound-Post-Preview-API)

-  [Outbound Post Preview Status API Endpoint](https://dev.sprinklr.com/preview-outbound-post#Outbound-Post-Preview-Status)

##  Generate Outbound Post Preview API Endpoint

This endpoint initiates the generation of a preview for the specified outbound post.

### API Endpoint

https://api3.sprinklr.com/{env}/api/v2/publishing/preview/generate?messageId={messageId}&exportType={exportType}&name={name}

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




















      ``









| Name | Type | Required | Description |
| --- | --- | --- | --- |
| messageId | string | Yes | Unique identifier of the outbound message to preview. |
| exportType | string | Yes | Export file format. Supported value: PNG. |
| name | string | No | Custom name for the exported preview file. The default name is auto-generated. |

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/publishing/preview/generate?messageId=359114819&exportType=PNG&name=New_report' \
--header 'Authorization: Bearer {token}' \
--header 'Key: {API_Key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \

## Example - Response


{
  "data": "68c2a81f25d19c07e1489c4b",
  "errors": []
}

### Response Schema





















| Field | Type | Description |
| --- | --- | --- |
| data | string | Unique identifier of the generated preview job. |
| errors | array | List of errors, if any. Returns empty if the request is successful. |

## Outbound Post Preview Status API Endpoint

This endpoint retrieves the status of the preview generation and provides a download URL if successful.

### API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/publishing/preview/status/{previewId}

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


















| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| previewId | string | Required | Unique identifier returned from the preview generation API. |

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/publishing/preview/status/68c2a81f25d19c07e1489c4b' \
--header 'Authorization: Bearer {token}' \
--header 'Key: {API_Key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \

## Example - Response


{
  "data": {
    "id": "68c2a81f25d19c07e1489c4b",
    "url": "https://storage.com/spn-qa6-cdn-secure/EXPORT/2025/09/11/10-46/66000000/b3826b52-5b57-4f35-9de8-2c5f9f3ae2d7-851742598/New_report.zip?X-Goog",
    "status": "SUCCESS"
  },
  "errors": []
}

### Response Schema

















      ````




      ``````








| Parameter | Type | Description |
| --- | --- | --- |
| id | string | Preview job ID. |
| url | string | Download link for the preview. The URL points to a .zip file.The .zip file contains the outbound post preview in the requested export format. |
| status | string | Current status of the preview job. Possible values:          IN_PROGRESS, SUCCESS, FAILED. |
| errors | array | List of errors, if any. Returns empty if the request is successful. |

[](https://dev.sprinklr.com/preview-outbound-post)

[Back to top](https://dev.sprinklr.com/preview-outbound-post)
