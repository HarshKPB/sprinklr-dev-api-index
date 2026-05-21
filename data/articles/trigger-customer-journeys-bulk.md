---
title: "Trigger Customer Journeys - Bulk"
slug: trigger-customer-journeys-bulk
url: https://dev.sprinklr.com/trigger-customer-journeys-bulk
---

# Trigger Customer Journeys - Bulk

#
  POST  Trigger Customer Journeys - Bulk



Sprinklr allows running automated customer journeys that are based on external events, such as a customer filling up a form, completing an online purchase, abandoning cart, etc. This API helps create new profiles and triggers customer journeys based on given information. If the profiles already exist, the API will associate the journeys with it.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/marketing-journey/bulk-trigger

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











| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| journeyId | Required | The unique identifier for the journey that needs to be triggered. | String |
| globalContextParams | Optional | Refers to the object containing the context parameters that will be universally applicable to all the profiles mentioned in the payload | Object |
| IGNORE_DEDUP | Optional | If true, the customer journeys can be triggered multiple times as the logic will ignore the trigger duplications | Boolean |
| journeyProfiles | Required | Refers to the array containing the profile details along with the context parameters for triggering the customer journeys | Array |
| unifiedProfile | Required | Refers to the object containing the profile detailsRefer to the table below for unifiedProfile object parameters' details | Object |
| contextParameters | Optional | Refers to the object containing the key and value pair for any additional properties and values that should be associated with the profile | Object |

**Dev Notes: **

The default limit for the number of profiles that can be added in the unifiedProfile object is up to 20 profiles.

To know more about the recommended profile limit and other capabilities, reach out to your Success Manager.

### unifiedProfile Object Description Table
















































































































``````






































































				[profile list](https://www.sprinklr.com/help/articles/sprinklr-service-glossary/universal-profile/640905717517d84a3aaf398d)

[Bootstrap API](https://dev.sprinklr.com/bootstrap-resources-v1)






				[custom properties](https://www.sprinklr.com/help/articles/custom-fields/about-custom-fields/64521b380d27fc559bbe45f2)











| Parameter | Sub Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| contact |  | Required | Refers to the object containing the contact details of the customer | Object |
|  | firstName | OptionalRecommended to pass first name as it acts as an unique identifier for the customer profile | Refers to the first name of the customer | String |
|  | maidenName | Optional | Refers to the maiden name of the customer (if any) | String |
|  | lastName | OptionalRecommended to pass last name as it acts as an unique identifier for the customer profile | Refers to the last name of the customer | String |
|  | fullName | Optional | Refers to the full name of the customerRecommended to pass full name as it acts as an unique identifier for the customer profile | String |
|  | email | Optional | Refers to the email of the customer | String |
|  | phoneNo | Optional | Refers to the contact number of the customer | String |
|  | website | Optional | Refers to the websites where the customer has been identified | List [String] |
| demographics |  | Optional | Refers to the object containing the demographics' details of the customer | Object |
|  | location | Optional | Refers to the country the customer belongs to | String |
|  | gender | Optional | Refers to the gender of the customer | String |
| profiles |  | Required | Array containing the social profile level details of the customer | Array |
|  | name | Required | Refers to the full name of the customer | String |
|  | channelType | Required | Refers to the channel type you want to associate with the profileKindly note the channel type is case sensitive and should be passed in uppercase, i.e., SMS for SMS channel, EMAIL for email channel, WHATSAPP for WhatsApp social channel, and so on. | String |
|  | channelId | Required | Refers to the channel Id, i.e., native channel user Id of the customer | String |
|  | permalink | Optional | Refers to the link to the social profile the customer is associated with | String |
|  | avatarUrl | Optional | Refers to the image link for the display picture of the customer on the social media profile | String |
|  | bio | Optional | Refers to the bio of the customer on the associated social profile | String |
|  | followers | Optional | Refers to the reach of the customer on the associated social profile | Integer |
|  | following | Optional | Refers to the number of people following the customer on the associated social profile | Integer |
|  | unSubscribed | Optional | If true, the profile is unsubscribed from receiving email notifications | Boolean |
|  | accountSpecificInfos | Optional | Refers to the array containing account Specific Info like accountId, externalId, etc.Account Specific Info Table given below. | Array |
| profileWorkflow |  | Optional | Refers to the object containing the profile workflow properties such as profile list details, custom properties, and workspace level details | Object |
|  | profileLists | Optional | List containing the  Ids on the global (partner) levelYou can fetch the existing profile list name and Id using | List [Integer] |
|  | customProperties | Optional | Refers to the global level  you want to associate with the profile | Object |
|  | profileSpaceWorkflows | Optional | Refers to the array containing the workspace level properties associated with the profile. Refer to the table below for profileSpaceWorkflow parameters' description | Array |

### Account Specific Info Parameter Description Table































































| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| accountId | Optional | Refers to the social account id to which you want to associate the profile with | Integer |
| externalId | Optional | Refers to the external id of the profile if any | String |
| lastBrandEngagedTime | Optional | Last brand engagement time. | Integer |
| lastFanEngagedTime | Optional | Last fan engagement time. | Integer |
| optIn | Optional | If True, optin.default: false | Boolean |
| fanSubscriptionState | Optional | Subscription state of fan. | String |
| activeUser | Optional | If True, user id active.default: false | Boolean |
| invited | Optional | If True, invited.default: false | Boolean |

### Profile Space Workflow Parameter Description Table





















[profile list](https://www.sprinklr.com/help/articles/sprinklr-service-glossary/universal-profile/640905717517d84a3aaf398d)

[Bootstrap API](https://dev.sprinklr.com/bootstrap-resources-v1)



[tags](https://www.sprinklr.com/help/articles/tags/create-and-use-profile-tags/6467a2388ea3c9635cf3745d)



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| spaceId | Required | Refers to the workspace Id where the customer needs to be added | String |
| profileLists | Optional | List containing the  Ids on the workspace levelYou can fetch the existing workspace profile list name and Id using | List [Integer] |
| tags | Optional | Refers to the  that act as profile identifier based on common attributes associated with profilesPlease note that the tags can be added from customer's end. | List [String] |

### Example - API Request















Copy Code



curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v2/marketing-journey/bulk-trigger' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "journeyId": "668b7c293f9ab80bff099de6",
    "globalContextParams": {
        "var1": "668b86de7c1d953be21ed1de",
        "IGNORE_DEDUP": true
    },
    "journeyProfiles": [
        {
            "unifiedProfile": {
                "contact": {
                    "firstName": "Test User"
                },
                "profiles": [
                    {
                        "channelType": "WHATSAPP_BUSINESS",
                        "channelId": "91788090133"
                    }
                ]
            },
            "contextParams": {
                "var1": "Test User"
            }
        },
        {
            "unifiedProfile": {
                "contact": {
                    "firstName": "Test User 1"
                },
                "profiles": [
                    {
                        "channelType": "WHATSAPP_BUSINESS",
                        "channelId": "919990008887"
                    }
                ]
            },
            "contextParams": {
                "var1": "Test User 1"
            }
        },
        {
            "unifiedProfile": {
                "contact": {
                    "firstName": "Test User 2"
                },
                "profiles": [
                    {
                        "channelType": "WHATSAPP_BUSINESS",
                        "channelId": "912227776543"
                    }
                ]
            },
            "contextParams": {
                "var1": "Test User 2"
            }
        },
        {
            "unifiedProfile": {
                "contact": {
                    "firstName": "Test User 3"
                },
                "profiles": [
                    {
                        "channelType": "WHATSAPP_BUSINESS",
                        "channelId": "919878231234"
                    }
                ]
            },
            "contextParams": {
                "var1": "Test User 3"
            }
        },
        {
            "unifiedProfile": {
                "contact": {
                    "firstName": "sahil"
                },
                "profiles": [
                    {
                        "channelType": "WHATSAPP_BUSINESS",
                        "channelId": "919267534212"
                    }
                ]
            },
            "contextParams": {
                "var1": "Test User 4"
            }
        }
    ]
}'






### Example - Response





{
    "data": {
        "status": "SUCCESS",
        "message": "Triggered Successfully",
        "trackingId": ""
    },
    "errors": []
}






	[](https://dev.sprinklr.com/trigger-customer-journeys-bulk)






[Back to top](https://dev.sprinklr.com/trigger-customer-journeys-bulk)
