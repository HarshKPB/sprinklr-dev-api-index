---
title: "Search Leads"
slug: search-leads
url: https://dev.sprinklr.com/search-leads
---

# Search Leads

#
  POST Search Leads




The Search Lead API enables customers to retrieve lead information from the system using any combination of lead attributes including lead ID, user details, or other attribute values—addressing the absence of search capabilities in existing Sprinklr APIs. By allowing flexible attribute‑based filtering and enforcing clear pagination limits, the API provides an efficient and user‑friendly way to locate leads stored in the system.

**Dev Notes: **No permissions are required to use this paginated API, and users can specify both page and page size (up to a maximum of 100, which can be reduced but not increased) to control result volume. If page and size are not provided, the API returns the first 100 matching leads along with an indicator showing whether additional results are available.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/dmp/lead-search

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
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  	 guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Parameters







| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| filterType | Required | Defines the filter operator or logical grouping. Examples include boolean operators (OR) and predicates (EQUALS). | String |
| filters | Required | Collection of filter expressions used to search for leads. Supports logical grouping and nested conditions.Refer to the table below for array definition. | Array |

**Dev Notes: **If the filters are defined for the user and the lead event, defining the array parameters such as `filterType`, `field`, and `values` becomes essential.

### filters Array Description Table







| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| filterType | Required | Defines the filter operator or logical grouping. Examples include boolean operators (OR) and predicates (EQUALS). | String |
| field | Optional | Name of the lead attribute on which the filter condition is applied. Required for predicate filter types such as EQUALS. | String |
| values | Optional | List of values to compare against the specified field. Required for predicate filter types such as EQUALS. | Array |

## Example - Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/dmp/lead-search' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
   "filters": [
        {
            "filterType": "OR",
            "filters": [
                {
                    "filterType": "EQUALS",
                    "field": "name_nov26_25_1_1",
                    "values": ["hassain_nov26_25_2_2_2"]
                },
                {
                    "filterType": "EQUALS",
                    "field": "phone number_nov26_25_1_1",
                    "values": ["+919492266220"]
                }
            ]
        }
    ]
  }'






## Example - Response





{
    "hasMore": false,
    "result": [
        {
            "id": "6926e683ec827b3f6d908401",
            "segmentId": "FILE_UPLOAD_672A13E72771E8DA49070D0DAE95A266_1764157058148",
            "customerId": "userid_hassain_nov26_25_1_1_9",
            "staticLead": false,
            "attributes": [
                {
                    "key": "name_nov26_25_1_1",
                    "st_value": "hassain_nov26_25_2_2_2",
                    "fieldType": "STRING"
                },
                {
                    "key": "phone number_nov26_25_1_1",
                    "st_value": "+919618240549",
                    "fieldType": "STRING",
                    "piiAttribute": true
                },
                {
                    "key": "product_nov26_25_1_1",
                    "st_value": "debit card",
                    "fieldType": "STRING"
                },
                {
                    "key": "user id_nov26_25_1_1",
                    "st_value": "userid_hassain_nov26_25_1_1_9",
                    "fieldType": "STRING"
                }
            ],
            "user": {
                "custId": "userid_hassain_nov26_25_1_1_9",
                "customerId": "userid_hassain_nov26_25_1_1_9",
                "socialNetworkType": "EXTERNAL_APPLICATION",
                "anonymousId": "userid_hassain_nov26_25_1_1_9",
                "phoneDetails": [
                    {
                        "phoneNo": "9618240549",
                        "countryCode": "+91",
                        "countryId": "IN",
                        "type": "phone number_nov26_25_1_1",
                        "connectivity": 100.0
                    }
                ],
                "emailDetails": [],
                "attributes": []
            },
            "demographics": {},
            "sourceInfos": [
                {
                    "id": "aea82b88-b276-4166-b354-3f24a6df2da1",
                    "sourceId": "FILE_UPLOAD_672A13E72771E8DA49070D0DAE95A266_1764157058148",
                    "sourceName": "nov26_final.xlsx",
                    "sourceUploadTime": 1764157058871,
                    "sourceType": "FILE_UPLOAD"
                }
            ],
            "sourceName": "nov26_final.xlsx",
            "createdTime": 1764157058876,
            "modifiedTime": 1764251217096,
            "lastUpdatedTime": 1764251217096,
            "deleted": false,
            "globalCallAttempts": 4,
            "lastCallTime": 1764246181643,
            "leadSource": "DIRECT_LEAD",
            "aggregatedByValue": "userid_hassain_nov26_25_1_1_9",
            "connectivity": 100.0
        },
        {
            "id": "6926e683ec827b3f6d9083fd",
            "segmentId": "FILE_UPLOAD_672A13E72771E8DA49070D0DAE95A266_1764157058148",
            "customerId": "userid_hassain_nov26_25_1_1_5",
            "staticLead": false,
            "attributes": [
                {
                    "key": "name_nov26_25_1_1",
                    "st_value": "hassain_nov26_25_2_2_2",
                    "fieldType": "STRING"
                },
                {
                    "key": "phone number_nov26_25_1_1",
                    "st_value": "+919492266220",
                    "fieldType": "STRING",
                    "piiAttribute": true
                },
                {
                    "key": "product_nov26_25_1_1",
                    "st_value": "credit card",
                    "fieldType": "STRING"
                },
                {
                    "key": "user id_nov26_25_1_1",
                    "st_value": "userid_hassain_nov26_25_1_1_5",
                    "fieldType": "STRING"
                }
            ],
            "user": {
                "custId": "userid_hassain_nov26_25_1_1_5",
                "customerId": "userid_hassain_nov26_25_1_1_5",
                "socialNetworkType": "EXTERNAL_APPLICATION",
                "anonymousId": "userid_hassain_nov26_25_1_1_5",
                "phoneDetails": [
                    {
                        "phoneNo": "9492266220",
                        "countryCode": "+91",
                        "countryId": "IN",
                        "type": "phone number_nov26_25_1_1",
                        "connectivity": 100.0
                    }
                ],
                "emailDetails": [],
                "attributes": []
            },
            "demographics": {},
            "sourceInfos": [
                {
                    "id": "aea82b88-b276-4166-b354-3f24a6df2da1",
                    "sourceId": "FILE_UPLOAD_672A13E72771E8DA49070D0DAE95A266_1764157058148",
                    "sourceName": "nov26_final.xlsx",
                    "sourceUploadTime": 1764157058871,
                    "sourceType": "FILE_UPLOAD"
                }
            ],
            "sourceName": "nov26_final.xlsx",
            "createdTime": 1764157058876,
            "modifiedTime": 1764763318821,
            "lastUpdatedTime": 1764763318821,
            "deleted": false,
            "globalCallAttempts": 22,
            "lastCallTime": 1764573101067,
            "leadSource": "DIRECT_LEAD",
            "aggregatedByValue": "userid_hassain_nov26_25_1_1_5",
            "connectivity": 100.0
        },
        {
            "id": "6926e683ec827b3f6d9083ff",
            "segmentId": "FILE_UPLOAD_672A13E72771E8DA49070D0DAE95A266_1764157058148",
            "customerId": "userid_hassain_nov26_25_1_1_7",
            "staticLead": false,
            "attributes": [
                {
                    "key": "name_nov26_25_1_1",
                    "st_value": "hassain_nov26_25_2_2_2",
                    "fieldType": "STRING"
                },
                {
                    "key": "phone number_nov26_25_1_1",
                    "st_value": "+919492266220",
                    "fieldType": "STRING",
                    "piiAttribute": true
                },
                {
                    "key": "product_nov26_25_1_1",
                    "st_value": "debit card",
                    "fieldType": "STRING"
                },
                {
                    "key": "user id_nov26_25_1_1",
                    "st_value": "userid_hassain_nov26_25_1_1_7",
                    "fieldType": "STRING"
                }
            ],
            "user": {
                "custId": "userid_hassain_nov26_25_1_1_7",
                "customerId": "userid_hassain_nov26_25_1_1_7",
                "socialNetworkType": "EXTERNAL_APPLICATION",
                "anonymousId": "userid_hassain_nov26_25_1_1_7",
                "phoneDetails": [
                    {
                        "phoneNo": "9492266220",
                        "countryCode": "+91",
                        "countryId": "IN",
                        "type": "phone number_nov26_25_1_1",
                        "connectivity": 100.0
                    }
                ],
                "emailDetails": [],
                "attributes": []
            },
            "demographics": {},
            "sourceInfos": [
                {
                    "id": "aea82b88-b276-4166-b354-3f24a6df2da1",
                    "sourceId": "FILE_UPLOAD_672A13E72771E8DA49070D0DAE95A266_1764157058148",
                    "sourceName": "nov26_final.xlsx",
                    "sourceUploadTime": 1764157058871,
                    "sourceType": "FILE_UPLOAD"
                }
            ],
            "sourceName": "nov26_final.xlsx",
            "createdTime": 1764157058876,
            "modifiedTime": 1764573978654,
            "lastUpdatedTime": 1764573978654,
            "deleted": false,
            "globalCallAttempts": 26,
            "lastCallTime": 1764328509168,
            "leadSource": "DIRECT_LEAD",
            "aggregatedByValue": "userid_hassain_nov26_25_1_1_7",
            "connectivity": 100.0
        },
        {
            "id": "6926e683ec827b3f6d9083fb",
            "segmentId": "FILE_UPLOAD_672A13E72771E8DA49070D0DAE95A266_1764157058148",
            "customerId": "userid_hassain_nov26_25_1_1_3",
            "staticLead": false,
            "attributes": [
                {
                    "key": "name_nov26_25_1_1",
                    "st_value": "hassain_nov26_25_1_1_1",
                    "fieldType": "STRING"
                },
                {
                    "key": "phone number_nov26_25_1_1",
                    "st_value": "+919492266220",
                    "fieldType": "STRING",
                    "piiAttribute": true
                },
                {
                    "key": "product_nov26_25_1_1",
                    "st_value": "credit card",
                    "fieldType": "STRING"
                },
                {
                    "key": "user id_nov26_25_1_1",
                    "st_value": "userid_hassain_nov26_25_1_1_3",
                    "fieldType": "STRING"
                }
            ],
            "user": {
                "custId": "userid_hassain_nov26_25_1_1_3",
                "customerId": "userid_hassain_nov26_25_1_1_3",
                "socialNetworkType": "EXTERNAL_APPLICATION",
                "anonymousId": "userid_hassain_nov26_25_1_1_3",
                "phoneDetails": [
                    {
                        "phoneNo": "9492266220",
                        "countryCode": "+91",
                        "countryId": "IN",
                        "type": "phone number_nov26_25_1_1",
                        "connectivity": 100.0
                    }
                ],
                "emailDetails": [],
                "attributes": []
            },
            "demographics": {},
            "sourceInfos": [
                {
                    "id": "aea82b88-b276-4166-b354-3f24a6df2da1",
                    "sourceId": "FILE_UPLOAD_672A13E72771E8DA49070D0DAE95A266_1764157058148",
                    "sourceName": "nov26_final.xlsx",
                    "sourceUploadTime": 1764157058871,
                    "sourceType": "FILE_UPLOAD"
                }
            ],
            "sourceName": "nov26_final.xlsx",
            "createdTime": 1764157058875,
            "modifiedTime": 1764573973095,
            "lastUpdatedTime": 1764573973095,
            "deleted": false,
            "globalCallAttempts": 18,
            "lastCallTime": 1764312760364,
            "leadSource": "DIRECT_LEAD",
            "aggregatedByValue": "userid_hassain_nov26_25_1_1_3",
            "connectivity": 100.0
        },
        {
            "id": "6926e683ec827b3f6d9083fc",
            "segmentId": "FILE_UPLOAD_672A13E72771E8DA49070D0DAE95A266_1764157058148",
            "customerId": "userid_hassain_nov26_25_1_1_4",
            "staticLead": false,
            "attributes": [
                {
                    "key": "name_nov26_25_1_1",
                    "st_value": "hassain_nov26_25_2_2_2",
                    "fieldType": "STRING"
                },
                {
                    "key": "phone number_nov26_25_1_1",
                    "st_value": "+919492266220",
                    "fieldType": "STRING",
                    "piiAttribute": true
                },
                {
                    "key": "product_nov26_25_1_1",
                    "st_value": "credit card",
                    "fieldType": "STRING"
                },
                {
                    "key": "user id_nov26_25_1_1",
                    "st_value": "userid_hassain_nov26_25_1_1_4",
                    "fieldType": "STRING"
                }
            ],
            "user": {
                "custId": "userid_hassain_nov26_25_1_1_4",
                "customerId": "userid_hassain_nov26_25_1_1_4",
                "socialNetworkType": "EXTERNAL_APPLICATION",
                "anonymousId": "userid_hassain_nov26_25_1_1_4",
                "phoneDetails": [
                    {
                        "phoneNo": "9492266220",
                        "countryCode": "+91",
                        "countryId": "IN",
                        "type": "phone number_nov26_25_1_1",
                        "connectivity": 100.0
                    }
                ],
                "emailDetails": [],
                "attributes": []
            },
            "demographics": {},
            "sourceInfos": [
                {
                    "id": "aea82b88-b276-4166-b354-3f24a6df2da1",
                    "sourceId": "FILE_UPLOAD_672A13E72771E8DA49070D0DAE95A266_1764157058148",
                    "sourceName": "nov26_final.xlsx",
                    "sourceUploadTime": 1764157058871,
                    "sourceType": "FILE_UPLOAD"
                }
            ],
            "sourceName": "nov26_final.xlsx",
            "createdTime": 1764157058875,
            "modifiedTime": 1764573786625,
            "lastUpdatedTime": 1764573786625,
            "deleted": false,
            "globalCallAttempts": 17,
            "lastCallTime": 1764573786623,
            "leadSource": "DIRECT_LEAD",
            "aggregatedByValue": "userid_hassain_nov26_25_1_1_4",
            "connectivity": 100.0
        }
    ],
    "totalHits": 5,
    "selectAllSupported": false
}







### Response Parameters







| Parameters | Description | Type |
| --- | --- | --- |
| hasMore | Indicates whether more records are available beyond the current response payload. | Boolean |
| result | List of lead records returned by the API. | Array |
| totalHits | Total number of lead records matching the query. | Number |
| selectAllSupported | Indicates whether the API supports selecting all matching records in a single operation. | Boolean |

**Dev Notes: **If the result is defined for the user and the lead event, defining the array parameters such as `id`, `segmentId`, `customerId`, `staticLead` and `attributes` becomes essential.

### result Array Description Table







| Parameters | Description | Type |
| --- | --- | --- |
| id | Unique identifier of the lead. | String |
| segmentId | Identifier of the segment or source batch to which the lead belongs. | String |
| customerId | Unique customer identifier associated with the lead. | String |
| staticLead | Indicates whether the lead is static (true) or dynamically created (false). | Boolean |
| attributes | List of custom attributes associated with the lead. | Array |

	[](https://dev.sprinklr.com/search-leads)




[Back to top](https://dev.sprinklr.com/search-leads)
