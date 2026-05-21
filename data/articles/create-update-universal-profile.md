---
title: "Create(Update) Universal Profile"
slug: create-update-universal-profile
url: https://dev.sprinklr.com/create-update-universal-profile
---

# Create(Update) Universal Profile

#
  POST Create(Update) Universal Profile


A customer or a Universal Profile stores user/customer information associated with the respective social profile within Sprinklr. These details are stored in the form of standard and custom fields and are visible under [Audience Profiles](https://www.sprinklr.com/help/articles/getting-started/audience-profile-governance/645e2044e66f2e36b45195d8) module within the Sprinklr platform.

Using this API, you can create or update a Universal Profile within Sprinklr.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/profile

**Dev Notes: **You can also create and update profile custom fields using this API .

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

### Query Parameter















				``````



| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| syncPartnerProfileListIfNotSet=false | Optional | Boolean | The syncPartnerProfileListIfNotSet=false parameter is a control flag used to determine how the system should handle the profileList field during a profile update — specifically when the profileList is not included in the payload. |

### Behavior by Scenario

#### 1. No query parameter passed & `profileList` not in payload


- **Behavior:** Default behavior applies.

- **Outcome:** `profileList` is set to `null`.

- **Explanation:** This is the legacy behavior. If no query parameter is sent and `profileList` is missing from the request body, it will clear (nullify) any existing `profileList` values.

#### 2. `syncPartnerProfileListIfNotSet=false` is passed & `profileList` is NOT in payload


- **Behavior:** Preserve existing values.

- **Outcome:** The existing `profileList` is **not modified**; it remains unchanged.

- **Explanation:** The flag tells the system: “If I haven’t provided `profileList`, do not modify the current value.”

#### 3. `syncPartnerProfileListIfNotSet=false` is passed & `profileList` IS in payload


- **Behavior:** Update.

- **Outcome:** The existing `profileList` is updated with the new values provided in the payload.

- **Explanation:** Since the field is present in the request, it is updated accordingly.

### Summary Table





      ``








      ``





      ``****





      ``



| Scenario | Query Param | profileList in Payload | Result |
| --- | --- | --- | --- |
| 1 | Not passed | Not present | profileList = null (default behavior) |
| 2 | false | Not present | profileList is preserved |
| 3 | false | Present | profileList updated with payload values |

### Request Parameters
















































































































``````






































































				[profile list](https://www.sprinklr.com/help/articles/sprinklr-service-glossary/universal-profile/640905717517d84a3aaf398d)

[Bootstrap API](https://dev.sprinklr.com/bootstrap-api-v1)






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

[Bootstrap API](https://dev.sprinklr.com/bootstrap-api-v1)



[tags](https://www.sprinklr.com/help/articles/tags/create-and-use-profile-tags/6467a2388ea3c9635cf3745d)



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| spaceId | Required | Refers to the workspace Id where the customer needs to be added | String |
| profileLists | Optional | List containing the  Ids on the workspace levelYou can fetch the existing workspace profile list name and Id using | List [Integer] |
| tags | Optional | Refers to the  that act as profile identifier based on common attributes associated with profilesPlease note that the tags can be added from customer's end. | List [String] |

## 1. Example Request without Query Parameter















Copy Code


 curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/profile' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "contact": {
        "firstName": "John",
        "lastName": "Doe",
        "fullName": "John Doe",
        "email": "john.doe@sprinklr.com",
        "phoneNo": "+33612241964",
        "website": [
            "https://youtube.com"
        ]
    },
    "demographics": {
        "gender": "male",
        "location": "UAE"
    },
    "profiles": [
        {
            "name": "John Doe",
            "channelType": "EMAIL",
            "channelId": "TestingUser",
            "permalink": "john.doe@sprinklr.com",
            "followers": 100,
            "bio": "testing 1234",
            "avatarUrl": "https://sprcdn-assets.sprinklr.com/787/d5dab244-1307-4426-a923-b90052d7d231-289403188/https___prod-media-proxy.sprin.jpg",
            "following": 10,
            "unSubscribed": false,
            "deleted": false,
            "statusCount": 0,
            "accountSpecificInfos": {},
            "additional": {},
            "verified": true
    }
],
"profileWorkflow": {
    "profileLists": [
        50,
        51
    ],
    "customProperties": {
        "_c_64dcb892e32de6530b5a8dbf": [
            "US"
        ]
    },
    "profileSpaceWorkflows": [
        {
            "spaceId": "66000002",
            "profileLists": [
                3,
                2,
                7,
                8
            ],
            "tags": [
                "b2c",
                "Finance"
            ]
        }
    ]
}'





## 1. Example - Response





{
    "data": {
        "id": "64fed24d53edd22031e97322",
        "contact": {
            "firstName": "John",
            "lastName": "Doe",
            "fullName": "John Doe",
            "email": "john.doe@sprinklr.com",
            "phoneNo": "+33612241964",
            "website": [
                "https://youtube.com"
            ],
            "phoneDetails": [],
            "emailDetails": []
        },
        "demographics": {
            "location": "UAE",
            "gender": "male"
        },
        "profiles": [
            {
                "name": "John",
                "channelType": "EMAIL",
                "channelId": "TestingUser",
                "permalink": "john.doe@sprinklr.com",
                "avatarUrl": "https://sprcdn-assets.sprinklr.com/787/d5dab244-1307-4426-a923-b90052d7d231-289403188/https___prod-media-proxy.sprin.jpg",
                "profileImageUrl": "https://sprcdn-assets.sprinklr.com/787/d5dab244-1307-4426-a923-b90052d7d231-289403188/https___prod-media-proxy.sprin.jpg",
                "bio": "testing 1234",
                "followers": 100,
                "following": 10,
                "verified": true,
                "unSubscribed": false,
                "deleted": false,
                "snCreatedTime": 0,
                "snModifiedTime": 1694424063713,
                "statusCount": 0,
                "accountSpecificInfos": [
                    {
                        "accountId": 0
                    }
                ],
                "additional": {},
                "url": "twitter/1234"
            }
        ],
        "profileWorkflow": {
            "profileLists": [
                50,
                51
            ],
            "customProperties": {
                "_c_64dcb892e32de6530b5a8dbf": [
                    "US"
                ],
                "_c_64cbf526fd8b0e259d72470a": [
                    "10"
                ],
                "_c_64e8a89a9deb2c0c668e7a57": []
            },
            "profileSpaceWorkflows": [
                {
                    "profileLists": [
                        3,
                        2,
                        7,
                        8
                    ],
                    "spaceId": "66000002"
                }
            ]
        },
        "createdTime": 1694421581198,
        "modifiedTime": 1694424063737,
        "restricted": false
    },
    "errors": []
}






**Dev Notes: **If you modify the channel Id, a new profile will be created. Else, the existing profile will be updated.


## 2. Example Request with Query Parameter















Copy Code


curl -X POST \
  'https://api3.sprinklr.com/{env}/api/v2/profile?syncPartnerProfileListIfNotSet=false' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
	"id": "651e7c72e366c7ec4473608f",
    "contact": {
        "firstName": "Shivangi",
        "lastName": "Test",
        "fullName": "Shivangi Test",
        "email": "test@sprinklr.com",
        "phoneNo": "+33612241964",
        "website": [
            "https://youtube.com"
        ]
    },
    "demographics": {
        "gender": "female",
        "location": "UAE"
    },
    "profiles": [
        {
            "name": "Shivangi Test",
            "channelType": "EMAIL",
            "channelId": "TestingUser",
            "permalink": "test@sprinklr.com",
            "followers": 100,
            "bio": "testing 1234",
            "avatarUrl": "https://sprcdn-assets.sprinklr.com/787/d5dab244-1307-4426-a923-b90052d7d231-289403188/https___prod-media-proxy.sprin.jpg",
            "following": 10,
            "unSubscribed": false,
            "deleted": false,
            "statusCount": 0,
            "accountSpecificInfos": {},
            "additional": {},
            "verified": true
    }
],
"profileWorkflow": {
    "customProperties": {
        "_c_64dcb892e32de6530b5a8dbf": [
            "US"
        ]
}
}
}'





### 2. Example - Response




{
    "data": {
        "restricted": false,
        "id": "651e7c72e366c7ec4473608f",
        "contact": {
            "firstName": "Shivangi",
            "lastName": "Test",
            "fullName": "Shivangi Test",
            "email": "test@sprinklr.com",
            "phoneNo": "+33612241964",
            "website": [
                "https://youtube.com"
            ],
            "phoneDetails": [],
            "emailDetails": []
        },
        "demographics": {
            "location": "UAE",
            "gender": "female"
        },
        "profiles": [
            {
                "name": "Shivangi Test",
                "channelType": "EMAIL",
                "channelId": "TestingUser",
                "permalink": "test@sprinklr.com",
                "avatarUrl": "https://sprcdn-assets.sprinklr.com/787/d5dab244-1307-4426-a923-b90052d7d231-289403188/https___prod-media-proxy.sprin.jpg",
                "profileImageUrl": "https://sprcdn-assets.sprinklr.com/787/d5dab244-1307-4426-a923-b90052d7d231-289403188/https___prod-media-proxy.sprin.jpg",
                "bio": "testing 1234",
                "followers": 100,
                "following": 10,
                "verified": true,
                "unSubscribed": false,
                "deleted": false,
                "snCreatedTime": 0,
                "snModifiedTime": 1747142178005,
                "statusCount": 0,
                "accountSpecificInfos": [
                    {
                        "accountId": 0
                    }
                ],
                "additional": {},
                "url": "test@sprinklr.com"
            }
        ],
        "profileWorkflow": {
            "profileLists": [
                51,
                52,
                17827
            ],
            "customProperties": {
                "_c_64dcb892e32de6530b5a8dbf": [
                    "US"
                ],
                "_c_619dd7172e3d641c7e4a7880": [
                    "sasasa"
                ],
                "_c_63887b85ace93839a016c1bf": [
                    "sasasasas"
                ],
                "_c_64de39897b5775215a72b83b": []
            },
            "profileSpaceWorkflows": [
                {
                    "profileLists": [
                        3,
                        2,
                        7,
                        8
                    ],
                    "tags": [
                        "b2c",
                        "finance"
                    ],
                    "spaceId": "66000002"
                }
            ]
        },
        "createdTime": 1696496754231,
        "modifiedTime": 1747142178006
    },
    "errors": []
}






### Response Parameters

[Read Profile API](https://dev.sprinklr.com/fetch-profile-by-profile-id)

[profile list](https://www.sprinklr.com/help/articles/sprinklr-service-glossary/universal-profile/640905717517d84a3aaf398d)

[Bootstrap API](https://dev.sprinklr.com/bootstrap-api-v1)

[custom properties](https://www.sprinklr.com/help/articles/custom-fields/about-custom-fields/64521b380d27fc559bbe45f2)

| Parameter | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Refers to the unique identifier for the customer's profileYou can further use this Id in  to fetch the profile details | String |
| contact |  | Contact information of the profile. |  |
|  | firstName | First name of the profile. | String |
|  | lastName | Last Name of the profile. | String |
|  | fullName | Full name of the profile. | String |
|  | email | Email id of the profile. | String |
|  | phoneNo | Phone number of the profile. | String |
|  | website | List of websites for the profile. | String |
| demographics |  | Demographic Information of the client. | Object |
|  | location | Refers to the country the customer belongs to | String |
|  | gender | Refers to the gender of the customer | String |
| profiles |  | Refers to the array containing the customer's social profile level details | Array |
|  | name | Refers to the name of the customer on the social profile | String |
|  | channelType | Refers to the social channel associated with the customer's profile | String |
|  | channelId | Unique id of the profile on channel. | String |
|  | permalink | Refers to the link of the profile on the social channel | String |
|  | avatarUrl | Refers to the image link for the display picture of the customer on the social media profile | String |
|  | profileImageUrl | Refers to the image link for the display picture of the customer on the social media profile | String |
|  | bio | Refers to the bio of the customer on the associated social profile | String |
|  | followers | Refers to the followers' count of the customer on the social channel | Integer |
|  | following | Refers to the count of people that the customer is following on the social channel | Integer |
|  | verified | If true, the social account of the customer is verified | Boolean |
|  | unSubscribed | If true, the profile is unsubscribed from receiving email notifications | Boolean |
|  | deleted | If true, the social profile has been deleted on the native channel | Boolean |
|  | snCreatedTime | Refers to the time at which the profile was created | Epoch |
|  | snModifiedTime | Refers to the time at which the profile was last modified | Epoch |
|  | statusCount | Refers to the total count of statues posted by the customer | Integer |
|  | accountSpecificInfos | Account Specific Info like accountId, externalId, etc.Account Specific Info Table given below. |  |
| profileWorkflow |  | Refers to the object containing the profile workflow properties such as profile list details, custom properties, and workspace level details | Object |
|  | profileLists | List containing the  Ids on the global (partner) levelYou can fetch the existing profile list name and Id using | List [Integer] |
|  | customProperties | Refers to the global level  you want to associate with the profile | Object |
|  | profileSpaceWorkflows | Refers to the array containing the workspace level properties associated with the profile. Refer to the table below for profileSpaceWorkflow parameters' description | Array |
| createdTime |  | Refers to the time at which the profile was created in Sprinklr | Epoch |
| modifiedTime |  | Refers to the time at which the profile was last modified in Sprinklr | Epoch |
| restricted |  | If true, profile is confidential and its' corresponding information is restricted | Boolean |


### Account Specific Info Parameter Description Table
























































| Parameter | Description | Type |
| --- | --- | --- |
| accountId | Account id of the profile. | Integer |
| externalId | External id of the profile. | String |
| lastBrandEngagedTime | Last brand engagement time. | Integer |
| lastFanEngagedTime | Last fan engagement time. | Integer |
| optIn | If True, optin.default: false | Boolean |
| fanSubscriptionState | Subscription state of fan. | String |
| activeUser | If True, user id active.default: false | Boolean |
| invited | If True, invited.default: false | Boolean |


### Profile Space Workflow Parameter Description Table

















[profile list](https://www.sprinklr.com/help/articles/sprinklr-service-glossary/universal-profile/640905717517d84a3aaf398d)

[Bootstrap API](https://dev.sprinklr.com/bootstrap-api-v1)




| Parameter | Description | Type |
| --- | --- | --- |
| spaceId | Refers to the workspace Id where the customer needs to be added | String |
| profileLists | List containing the  Ids on the workspace levelYou can fetch the existing workspace profile list name and Id using | List [Integer] |

	 [](https://dev.sprinklr.com/create-update-universal-profile)




[Back to top](https://dev.sprinklr.com/create-update-universal-profile)
