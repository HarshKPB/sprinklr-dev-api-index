---
title: "Update Account Custom Properties - Partial"
slug: update-account-custom-properties-partial
url: https://dev.sprinklr.com/update-account-custom-properties-partial
---

# Update Account Custom Properties - Partial

#
  POST Update Account Custom Properties (Partial)

Using this API, you can partially update partner/client custom properties for the given account Id. The API will only update the custom properties that are passed in the request body.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/account/update/{accountId}/customProperties

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

### Path Parameter















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| accountId | Required | Unique Id of the account. | String |

### Request Parameters





















****







****





| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| spaceId | Optional | Refers to the workspace id where the account exists | Integer |
| partnerCustomProperties | Optional | Refers to the custom properties you want to update at global level.Syntax:"Custom field name": [ {List of custom field values separated by comma}]Example:"_c_5f635d84ddef993f24577401": [             "text123"], | Object |
| clientCustomProperties | Optional | Refers to the custom properties you want to update at workspace level.Syntax:"Custom field name": [ {List of custom field values separated by comma}]Example:"_c_5f635d84ddef993f24577401": [             "text123"], | Object |

## Example - Request




 Copy Code



curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/account/update/600000132/customProperties' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "spaceId": 0,
    "partnerCustomProperties": {
        "_c_5f635d84ddef993f24577401": [
            "text123"
        ],
        "_c_6059873a178b014f558c1742": [
            "Hyderabad"
        ]
    },
    "clientCustomProperties": {
        "_c_617693a7a762962f80a32404": [
            "10"
        ],
        "_c_619246fe5f0ec3151749fb54": [
            "5"
        ]
    }
}



## Example - Response




204 No Content





**Dev Notes: **204 No Content implies that the account custom properties have been successfully updated.

[](https://dev.sprinklr.com/reporting-blueprints)




[Back to top](https://dev.sprinklr.com/reporting-blueprints)
