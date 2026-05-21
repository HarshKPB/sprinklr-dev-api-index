---
title: "Create Custom Entity - Bulk"
slug: create-custom-entity-bulk
url: https://dev.sprinklr.com/create-custom-entity-bulk
---

# Create Custom Entity - Bulk

#   POST Create Custom Entity - Bulk
 

This API allows you to bulk insert multiple records for a custom entity in one request. For example, you can define a custom entity for a product and insert several product records at once.

**Dev Notes: **Before using the Custom Entity APIs, this feature must be enabled for your Sprinklr instance. To enable it, contact your Success Manager or reach out to Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/custom-entity/entity/bulk-upsert/`{entity-type}`

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

## Path Parameter












-
- ****
- ****
- ****



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| {entity-type} | Required | The unique ID of the custom entity definition.             You can get this value from the Sprinklr UI:                  Open Entity Studio.     Go to the Custom tab and locate the entity.     Hover over the entity and click View.     Refer to the API Reference ID column for the desired entity. | String |

## Query Parameter












``

[example](https://dev.sprinklr.com/create-custom-entity-bulk#detailed-response-example)



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| responseMode | Optional | Indicates whether you want a detailed response. Supported Value: detailed     By default, a concise response is returned. Use this query parameter if you want a detailed response.      See . | String |

## Request Parameters












-
- ****
- ****
-



















`

`

-
- ****
- ****
- ****



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| type | Required | The unique ID of the custom entity definition. This is the same as the entity type path parameter.             You can get this value from the Sprinklr UI:                              Open Entity Studio.                 Go to the Custom tab and locate the entity.                 Hover over the entity and click View.                 Refer to the API Reference ID column for the desired entity. | String |
| entityId | Required | Custom ID for this entity record. It can be any unique value you assign. | String |
| name | Required | Display name for the entity record. It can be any value you choose. | String |
| values | Optional | Object containing entity fields and their corresponding values in key-value pairs.             Example:                           "values": {             "detail": "123",             "entityId": "CUST001",             "name": "Alice Johnson"             }             To get field IDs:                              Open Entity Studio.                 Go to the Custom tab and locate the entity.                 Hover over the entity and click View.                 In the Field and Relationship tab, refer to the API Reference ID column. | Object |

**Dev Notes: **This API supports only the **upsert operation**, and partial updates are not allowed. If any fields in the `values` object are omitted from the request, those fields will be unset in the record.

## Examples

### Example 1 - Default Concise Response




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/custom-entity/entity/bulk-upsert/_c_call_center_customer' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API KEY}' \
--header 'Content-Type: application/json' \
--data '[
    {
        "type": "_c_call_center_customer",
        "entityId": "_c_call_center_customer_1",
        "name": "Testing1",
        "values": {
            "detail": "123",
            "entityId": "CUST001",
            "name": "Alice Johnson"
        }
    },
    {
        "type": "_c_call_center_customer",
        "entityId": "_c_call_center_customer_2",
        "name": "Testing2",
        "values": {
            "detail": "456",
            "entityId": "CUST002",
            "name": "Bob Smith"
        }
    },
    {
        "type": "_c_call_center_customer",
        "entityId": "_c_call_center_customer_3",
        "name": "Testing3",
        "values": {
            "detail": "789",
            "entityId": "CUST003",
            "name": "Charlie Davis"
        }
    },
    {
        "type": "_c_call_center_customer",
        "entityId": "_c_call_center_customer_4",
        "name": "Testing4",
        "values": {
            "detail": "101112",
            "entityId": "CUST004",
            "name": "Diana Roberts"
        }
    },
    {
        "type": "_c_call_center_customer",
        "entityId": "_c_call_center_customer_5",
        "name": "Testing5",
        "values": {
            "detail": "131415",
            "entityId": "CUST005",
            "name": "Edward Lee"
        }
    }
]'



### Example - Response



{
    "data": [],
    "errors": [],
    "metadata": {
        "status": "success",
        "successCount": 5,
        "failedCount": 0
    }
}



### Example 2 - Detailed Response




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/custom-entity/entity/bulk-upsert/_c_call_center_customer?responseMode=detailed' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API KEY}' \
--header 'Content-Type: application/json' \
--header 'Cookie: JSESSIONID=2992C575E308EE6760EF67AE396E342B' \
--data '[
    {
        "type": "_c_call_center_customer",
        "entityId": "_c_call_center_customer_1",
        "name": "Testing1",
        "values": {
            "detail": "123",
            "entityId": "CUST001",
            "name": "Alice Johnson"
        }
    },
    {
        "type": "_c_call_center_customer",
        "entityId": "_c_call_center_customer_2",
        "name": "Testing2",
        "values": {
            "detail": "456",
            "entityId": "CUST002",
            "name": "Bob Smith"
        }
    },
    {
        "type": "_c_call_center_customer",
        "entityId": "_c_call_center_customer_3",
        "name": "Testing3",
        "values": {
            "detail": "789",
            "entityId": "CUST003",
            "name": "Charlie Davis"
        }
    },
    {
        "type": "_c_call_center_customer",
        "entityId": "_c_call_center_customer_4",
        "name": "Testing4",
        "values": {
            "detail": "101112",
            "entityId": "CUST004",
            "name": "Diana Roberts"
        }
    },
    {
        "type": "_c_call_center_customer",
        "entityId": "_c_call_center_customer_5",
        "name": "Testing5",
        "values": {
            "detail": "131415",
            "entityId": "CUST005",
            "name": "Edward Lee"
        }
    }
]'



### Example - Response



{
    "data": [
        {
            "id": "6904c9ebeb368a36324b0c3d",
            "entityId": "_c_call_center_customer_1",
            "name": "Testing1",
            "type": "_c_call_center_customer",
            "values": {
                "detail": "123",
                "entityId": "CUST001",
                "name": "Alice Johnson"
            },
            "createdTime": "Fri Oct 31 14:38:35 UTC 2025",
            "createdTimeInMillis": 1761921515882,
            "modifiedTime": "Fri Nov 07 06:24:42 UTC 2025",
            "modifiedTimeInMillis": 1762496682681
        },
        {
            "id": "6904c9ebeb368a36324b0c40",
            "entityId": "_c_call_center_customer_2",
            "name": "Testing2",
            "type": "_c_call_center_customer",
            "values": {
                "detail": "456",
                "entityId": "CUST002",
                "name": "Bob Smith"
            },
            "createdTime": "Fri Oct 31 14:38:35 UTC 2025",
            "createdTimeInMillis": 1761921515882,
            "modifiedTime": "Fri Nov 07 06:24:42 UTC 2025",
            "modifiedTimeInMillis": 1762496682681
        },
        {
            "id": "6904c9ebeb368a36324b0c41",
            "entityId": "_c_call_center_customer_3",
            "name": "Testing3",
            "type": "_c_call_center_customer",
            "values": {
                "detail": "789",
                "entityId": "CUST003",
                "name": "Charlie Davis"
            },
            "createdTime": "Fri Oct 31 14:38:35 UTC 2025",
            "createdTimeInMillis": 1761921515882,
            "modifiedTime": "Fri Nov 07 06:24:42 UTC 2025",
            "modifiedTimeInMillis": 1762496682681
        },
        {
            "id": "6904c9ebeb368a36324b0c42",
            "entityId": "_c_call_center_customer_4",
            "name": "Testing4",
            "type": "_c_call_center_customer",
            "values": {
                "detail": "101112",
                "entityId": "CUST004",
                "name": "Diana Roberts"
            },
            "createdTime": "Fri Oct 31 14:38:35 UTC 2025",
            "createdTimeInMillis": 1761921515882,
            "modifiedTime": "Fri Nov 07 06:24:42 UTC 2025",
            "modifiedTimeInMillis": 1762496682681
        },
        {
            "id": "6904c9ebeb368a36324b0c43",
            "entityId": "_c_call_center_customer_5",
            "name": "Testing5",
            "type": "_c_call_center_customer",
            "values": {
                "detail": "131415",
                "entityId": "CUST005",
                "name": "Edward Lee"
            },
            "createdTime": "Fri Oct 31 14:38:35 UTC 2025",
            "createdTimeInMillis": 1761921515882,
            "modifiedTime": "Fri Nov 07 06:24:42 UTC 2025",
            "modifiedTimeInMillis": 1762496682681
        }
    ],
    "errors": [],
    "metadata": {
        "status": "success",
        "successCount": 5,
        "failedCount": 0
    }
}



## Response Parameters

### Response Parameters - Default












































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Empty array. This array is reserved for custom entity records that are successfully upserted, but in the default response, it remains empty. | Array |
| errors |  | Array of any errors encountered during the API request. If there are no errors, this will be an empty array. | Array |
| metadata |  | Contains metadata related to the request, including status and counts for success and failure. | Object |
|  | status | Indicates the overall status of the request (for example, "success" or "failure"). | String |
|  | successCount | Number of records successfully upserted. | Integer |
|  | failedCount | Number of records that failed to be upserted. | Integer |

### Response Parameters - Detailed




















































































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Array of custom entity records that were successfully upserted. Each record contains details about the entity, such as its ID, entityId, name, values, and timestamps. | Array |
|  | id | The unique identifier of the custom entity record. | String |
|  | entityId | The entity identifier, which corresponds to the entityId provided in the upsert request. | String |
|  | name | The name of the custom entity. | String |
|  | type | The type of the custom entity, as specified in the request (for example, `_c_call_center_customer`). | String |
|  | values | An object containing the values of the custom entity, such as its detail, entityId, and name. | Object |
|  | detail | The specific detail of the entity (for example, "123", "456"). | String |
|  | entityId | The entity identifier within the `values` object, corresponding to the customer ID (for example, "CUST001", "CUST002"). | String |
|  | name | The name of the entity within the `values` object (for example, "Alice Johnson", "Bob Smith"). | String |
|  | createdTime | The timestamp of when the entity was created, in human-readable format (for example, "Fri Oct 31 14:38:35 UTC 2025"). | String |
|  | createdTimeInMillis | The timestamp of when the entity was created. | Epoch |
|  | modifiedTime | The timestamp of when the entity was last modified. | String |
|  | modifiedTimeInMillis | The timestamp of when the entity was last modified. | Epoch |
| errors |  | Array of any errors encountered during the API request. If there are no errors, this will be an empty array. | Array |
| metadata |  | Contains metadata related to the request, including status and counts for success and failure. | Object |
|  | status | Indicates the overall status of the request (for example, "success" or "failure"). | String |
|  | successCount | Number of records successfully upserted. | Integer |
|  | failedCount | Number of records that failed to be upserted. | Integer |

[](https://dev.sprinklr.com/create-custom-entity-bulk) 

 

 
[Back to top](https://dev.sprinklr.com/create-custom-entity-bulk)
