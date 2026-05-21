---
title: "Delete Transaction"
slug: delete-transaction
url: https://dev.sprinklr.com/delete-transaction
---

# Delete Transaction

#   DELETE Delete CFM Transaction

The API deletes a specific transaction using its unique Transaction ID.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/survey-transactions/`{transactionId}`?transactionGroupId={transactionGroupId}

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



















| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| transactionId | string | Yes | The unique identifier of the transaction that needs to be deleted. |

## Query Parameter



















| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| transactionGroupId | string | Yes | The unique identifier of the transaction group that contains the transaction to be deleted. |

## Example Request

Copy Code


curl --location --request DELETE 'https://api3.sprinklr.com/{env}/api/v2/survey-transactions/68b5b00b83f80a7ebcdedfda?transactionGroupId=68adc96c444bb074f1fd28f7' \
--header 'Authorization: Bearer {token}' \
--header 'Key: {api_key}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \

## Example - Response


{
    "data": "Transaction 68b5b00b83f80a7ebcdedfda deleted successfully",
    "errors": []
}



[](https://dev.sprinklr.com/delete-transaction)

[Back to top](https://dev.sprinklr.com/delete-transaction)
