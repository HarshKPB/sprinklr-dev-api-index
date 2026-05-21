---
title: "Bulk Update User Profiles"
slug: bulk-update-user-profiles
url: https://dev.sprinklr.com/bulk-update-user-profiles
---

# Bulk Update User Profiles

#
  POST Bulk Update User Profile


Use this API to update multiple user profiles in Sprinklr with a single request, where profiles can be identified using either channel-based attributes or profile IDs. You can update contact information and custom properties for each user.

**Dev Notes: **It is recommended to update a maximum of **10 user profiles** per request.

## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/profile/bulk-update

### Headers

HTTP headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			```







[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



| Key | Value | Description |
| --- | --- | --- |
| accept | application/json | Determines the acceptable response type from the server |
| Content-Type | application/json | Content-Type is representation header determines the type of data (media/resource) present in the request body. |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the dev portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  article |

### Request Parameters














































****
- ****
- ****
- ****

****``



| Parameter | Sub-Parameters | Required/Optional | Type | Description |
| --- | --- | --- | --- | --- |
| bulkProfileUpdateRequest |  | Required | Array | Array of profile update objects. Each object can include profileKey or id, and update details. |
|  | profileKey | Optional | Object | Object containing channel type and channel ID of the user. |
|  | id | Optional | String | Unique profile ID. |
|  | profileUpdateRequestDTO | Optional | Object | Object containing profile details to update. |
|  | profileWorkflowUpdateDTO | Optional | Object | Object containing custom property update operations.         Supported Operations:           partnerCustomProperties: Sets or overwrites the values of custom properties. Use when you want the property’s value list to match exactly what you provide.   partnerCustomPropertiesAdded: Adds new values to existing custom property values without removing current ones.   partnerCustomPropertiesRemoved: Removes specific values from existing custom property values.  In these operations, pass custom properties and their values. Example: "partnerCustomProperties": {                     "_c_650413d1bc1a140dc7c001ce": [                         "eng 1"                     ]                 } |

### profileKey














				[Channels](https://dev.sprinklr.com/channels-v1)









| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| channelType | Required | String | The channel type of the user. For example, EMAIL. For supported values, see . |
| channelID | Optional | String | The user ID of the user (email ID). |

### contactInfo

Include the `contactInfo` object inside the `profileUpdateRequestDTO` object to update profile details such as name, email, and phone number.










































| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| firstName | Optional | String | The first name of the contact. |
| fullName | Optional | String | The full name of the contact (for example, first and last name combined). |
| lastName | Optional | String | The last name or surname of the contact. |
| emailDetails | Optional | String | The primary email address of the contact. |
| phoneNo | Optional | String | The primary phone number of the contact. |

## Example - Request















Copy Code


 curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/profile/bulk-update' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Authorization: Bearer {Enter your API KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "bulkProfileUpdateRequest": [
        {
            "profileKey": {
                "channelType": "EMAIL",
                "channelId": "vineetDemo0699@outlook.com"
            },
            "profileUpdateRequestDTO": {
                "contactInfo": {
                    "firstName": "Vineet",
                    "fullName": "Vineet Email v1",
                    "lastName": "Email V1",
                    "emailDetails": "vineetDemo0699@outlook.com",
                    "phoneNo": "9990988089"
                }
            },
            "profileWorkflowUpdateRequestDTO": {
                "partnerCustomPropertiesRemoved": {
                    "spr_community_user_country": [
                        "US"
                    ]
                }
            }
        },
        {
            "id": "6940fdf8d697ea8282f126cf",
            "profileUpdateRequestDTO": {
                "contactInfo": {
                    "phoneNo": "99909880891"
                }
            },
            "profileWorkflowUpdateRequestDTO": {
                "partnerCustomProperties": {
                    "_c_64dcb892e32de6530b5a8dbf": [
                        "IN"
                    ]
                }
            }
        },
        {
            "id": "64eece42e37744040f8ef500",
            "profileUpdateRequestDTO": {
                "contactInfo": {
                    "phoneNo": "99909880891"
                }
            },
            "profileWorkflowUpdateRequestDTO": {
                "partnerCustomPropertiesAdded": {
                    "_c_650413d1bc1a140dc7c001ce": [
                        "eng 2"
                    ]
                }
            }
        }
    ]
}'





## Example - Response





{"data":[{"profileId":"663df2365b4cc52ae6fd663f","success":true},{"profileId":"6940fdf8d697ea8282f126cf","success":true},{"profileId":"64eece42e37744040f8ef500","success":true}],"errors":[]}






### Response Parameters
































| Parameter | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Array containing objects with profile information and success status | Array |
|  | profileId | Unique identifier for the user profile | String |
|  | success | Indicates whether the action for the profile was successful | Boolean |
| errors |  | Contains error details if any occurred (empty if none) | Array |

	 [](https://dev.sprinklr.com/bulk-update-user-profiles)




[Back to top](https://dev.sprinklr.com/bulk-update-user-profiles)
