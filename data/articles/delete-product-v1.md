---
title: "Delete Product v1"
slug: delete-product-v1
url: https://dev.sprinklr.com/delete-product-v1
---

# Delete Product v1

#
  DELETE - Delete Product

Using this API, you can delete a product from the product catalog.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/universal-commerce/product/{productId}

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

## Path Parameter







| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| productId | Required | Refers to the unique identifier for the product you want to delete | String |

## Example - Request




 Copy Code



curl -X DELETE \
  'https://api3.sprinklr.com/{env}/api/v1/universal-commerce/product/65deed0978b4b5414e722622' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \





## Example - Response




204 No Content





**Dev Notes: **204 No Content implies that the product has been deleted successfully

[](https://dev.sprinklr.com/delete-product-v1)




[Back to top](https://dev.sprinklr.com/delete-product-v1)
