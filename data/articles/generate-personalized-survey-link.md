---
title: "Generate Personalized Survey Link"
slug: generate-personalized-survey-link
url: https://dev.sprinklr.com/generate-personalized-survey-link
---

# Generate Personalized Survey Link

#
  POST Generate Personalized Survey Link

This API allows you to generate a personalized survey link for an existing survey, tailored to a specific user or transaction in Sprinklr CFM.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/survey-distribution/transactions/link

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

## Request Parameters














[Steps to Retrieve distributionId](https://dev.sprinklr.com/generate-personalized-survey-link#get-distributionId)






[Profile Parameters](https://dev.sprinklr.com/generate-personalized-survey-link#profile-object)










| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| distributionId | Required | ID of the survey distribution.See  given below. | String |
| profile | Optional | Object containing user details such as contact, demographics, channel profile, and workflow data. Refer to  table below. | Object |
| transactionProperties | Optional | Object containing custom fields associated with the transaction in key-value format. | Object |

### Retrieve distributionId from Sprinklr CFM UI

To retrieve the Distribution ID, ensure the following in the CFM UI:










      ********


      ****
      ************
********


      ********
      ************
****************
********



| Description | Quick Navigation |
| --- | --- |
| Create and publish a survey. | Programs > Create Survey |
| Create a Transaction Group of type API for the survey. | Audience Management > Transactions > Create Transaction Group         For the transaction group, select Type > API |
| Create a Distribution of type Personalized Links using the Transaction of type API. | Programs > Survey > Distribution         Create Distribution > Personalized Links > Create Now > Transactions         In Distribution Details, under Add Transactions, select the Transaction Group you created. |


After completing the prerequisites above, follow these steps to retrieve the Distribution ID from the Sprinklr CFM UI:



- Open the CFM Persona App.

- In the side navigation, click **Programs**.

- Locate the survey.

- Hover over the survey, and click **View**.

- Go to the **Distribution** tab.

- Locate the distribution that has the **Transaction (API)** type.

- Click the **three-dot icon** alongside the distribution name.

- Click **Copy Distribution ID**.


### Profile Object















































































































































































































| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| contact |  | Required | Contains user contact information. | Object |
|  | firstName | Optional | First name of the user. | String |
|  | lastName | Optional | Last name of the user. | String |
|  | fullName | Optional | Full name of the user. | String |
|  | email | Optional | Email address of the user. | String |
|  | phoneNo | Optional | Contact phone number. | String |
|  | website | Optional | List of associated websites. | Array[String] |
| demographics |  | Optional | User demographic data. | Object |
|  | gender | Optional | Gender of the user. | String |
|  | location | Optional | User’s location. | String |
| accounts[] |  | Optional | List of social or channel accounts. | Array[Object] |
|  | name | Optional | Display name for the account. | String |
|  | channelType | Required | Communication channel (for example, EMAIL). | String |
|  | channelId | Required | Identifier for the channel. | String |
|  | permalink | Optional | Unique identifier/handle for the account. | String |
|  | followers | Optional | Number of followers. | Integer |
|  | bio | Optional | Bio or description. | String |
|  | avatarUrl | Optional | Profile picture URL. | String |
|  | following | Optional | Number of followed accounts. | Integer |
|  | unSubscribed | Optional | Whether the user unsubscribed. | Boolean |
|  | deleted | Optional | Whether the account is deleted. | Boolean |
|  | statusCount | Optional | Number of messages/statuses. | Integer |
|  | accountSpecificInfos | Optional | Custom channel-specific details. | Object |
|  | additional | Optional | Any additional data. | Object |
|  | verified | Optional | Whether the account is verified. | Boolean |
| listMemberships |  | Optional | IDs of lists the user belongs to. | Array[Int] |
| customProperties |  | Optional | Key-value pairs for custom user attributes. | Object |
| spaceAssignments[] |  | Optional | List of space-level user data mappings. | Array[Object] |
|  | spaceId | Required | ID of the assigned space or context. | String |
|  | listMemberships | Optional | List IDs specific to this space. | Array[Int] |
|  | tags | Optional | Tags for segmentation or categorization. | Array[String] |

## Example - Request




 Copy Code


curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/survey-distribution/transactions/link' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--data-raw '{
    "distributionId": "68c8ea1f49fb99572152e44d",
    "profile": {
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
        }
    },
    "transactionProperties": {
        "_c_68b67514d2aad55878d8ffbf": [
            "Test API 3 1 2"
        ]
    }
}'



## Example - Response




{
    "data": {
        "profile": {
            "restricted": false,
            "id": "67482a8a2dda2643b2df4b9b",
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
                    "name": "John Doe",
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
                    "snModifiedTime": 1758532408823,
                    "statusCount": 0,
                    "accountSpecificInfos": [
                        {
                            "accountId": 0
                        }
                    ],
                    "additional": {},
                    "url": "john.doe@sprinklr.com"
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
                        "50"
                    ],
                    "_c_64cbf88bfd8b0e259d72577b": [
                        "8"
                    ],
                    "_c_651ed978c84c6928d762f976": [
                        "N/A"
                    ],
                    "_c_67494ad8c4e9ca33a853268a": [],
                    "_c_64c38bc50e8ea978f3f1228a": [
                        "3"
                    ]
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
            "createdTime": 1732782730455,
            "modifiedTime": 1758532464743
        },
        "transaction": {
            "id": "68d113704d439f1f1ec31d24",
            "transactionGroupId": "68c8e9a449fb99572152e0ef",
            "profileName": "John Doe",
            "channelProfileId": "TestingUser",
            "distributionChannel": "EMAIL",
            "transactionGroupType": "API",
            "customProperties": {},
            "isArchived": false
        },
        "surveyName": "Documentation Feedback",
        "surveyLink": "https://feedback-qa6.sprinklr.com/form?id=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJBY2Nlc3MgVG9rZW4gR2VuZXJhdGVkIEJ5IFNwcmlua2xyIiwidHJpZ2dlclNvdXJjZUlkIjoiNjc0ODJhOGEyZGRhMjY0M2IyZGY0YjliIiwic3VydmV5SWQiOiI2OGI4NGU0ZWNlNTE0NTQ3NjA5M2NlN2QiLCJjbGllbnRJZCI6NjYwMDAwMDIsImlzcyI6IlNQUklOS0xSIiwicmV1c2FibGVTdXJ2ZXlMaW5rIjoidHJ1ZSIsInR5cCI6IkpXVCIsInN1cnZleVJlc3BvbmRpbmdDaGFubmVsIjoiRU1BSUwiLCJzdXJ2ZXlSZXNwb25zZUlkIjoiNjhkMTEzNzA0ZDQzOWYxZjFlYzMxZDJiIiwic3VydmV5TW9kZSI6IlNUQU5EQVJEIiwidXNlcklkIjo2NjAxNDY1OCwidHJpZ2dlclNvdXJjZVR5cGUiOiJQUk9GSUxFIiwic3VydmV5QXV0aGVudGljYXRpb25TdGF0ZSI6Ik5PVF9SRVFVSVJFRCIsImRpc3RyaWJ1dGlvbkVudGl0eUlkIjoiNjhjOGVhMWY0OWZiOTk1NzIxNTJlNDRkIiwiYXVkIjoiU1BSSU5LTFIiLCJuYmYiOjE3NTg1MzEyNjcsInNjb3BlIjpbIlJFQUQiLCJXUklURSJdLCJzdXJ2ZXlSZXNwb25kZXJTblR5cGUiOiJFTUFJTCIsInN1cnZleUxhbmd1YWdlIjoiZW4iLCJwYXJ0bmVySWQiOjY2MDAwMDAwLCJ0b2tlblR5cGUiOiJBQ0NFU1MiLCJhdXRoVHlwZSI6IlNVUlZFWV9SRVNQT05TRSIsImlhdCI6MTc1ODUzMjQ2NywianRpIjoic3ByaW5rbHIifQ.HuQXlfT-j7cGOM8sldp4cJRolSP-sqzgUMhzI5ezu249tqD2PWWaBUJsY6ywOMIU1luAJOGaDrMKNnw_8yJHW48SyeZ8zmE-rvk4FGamXXLo2ejERNgWv7zPJvBVGxhrJp80PrEeHoT0uaPxPCgrs-ebAtKaqJgezoXgnChln8UDRs1G3VOXZWHzkltRhuw6ya7OS6vXmGH1dkDqz8UlhB61lX2Hum81DHQGOV1IsgXv0ZZlXeYkb8nx2HRGS3wWrl73weldElgbq3g4P_GuEPyopKDHKaPdF4Ij3onYRm269QKNX0G9VE_0oyne_QHWveKWJ0wXQcZTuxl_A3IU6w&clickTimeEpoch=%25click_time_epoch%25",
        "optOutUrl": "https://feedback-qa6.sprinklr.com/form?id=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJBY2Nlc3MgVG9rZW4gR2VuZXJhdGVkIEJ5IFNwcmlua2xyIiwidHJpZ2dlclNvdXJjZUlkIjoiNjc0ODJhOGEyZGRhMjY0M2IyZGY0YjliIiwic3VydmV5SWQiOiI2OGI4NGU0ZWNlNTE0NTQ3NjA5M2NlN2QiLCJjbGllbnRJZCI6NjYwMDAwMDIsImlzcyI6IlNQUklOS0xSIiwicmV1c2FibGVTdXJ2ZXlMaW5rIjoidHJ1ZSIsInR5cCI6IkpXVCIsInN1cnZleVJlc3BvbmRpbmdDaGFubmVsIjoiRU1BSUwiLCJzdXJ2ZXlSZXNwb25zZUlkIjoiNjhkMTEzNzA0ZDQzOWYxZjFlYzMxZDJiIiwic3VydmV5TW9kZSI6IlNUQU5EQVJEIiwidXNlcklkIjo2NjAxNDY1OCwidHJpZ2dlclNvdXJjZVR5cGUiOiJQUk9GSUxFIiwic3VydmV5QXV0aGVudGljYXRpb25TdGF0ZSI6Ik5PVF9SRVFVSVJFRCIsImRpc3RyaWJ1dGlvbkVudGl0eUlkIjoiNjhjOGVhMWY0OWZiOTk1NzIxNTJlNDRkIiwiYXVkIjoiU1BSSU5LTFIiLCJuYmYiOjE3NTg1MzEyNjcsInNjb3BlIjpbIlJFQUQiLCJXUklURSJdLCJzdXJ2ZXlSZXNwb25kZXJTblR5cGUiOiJFTUFJTCIsInN1cnZleUxhbmd1YWdlIjoiZW4iLCJwYXJ0bmVySWQiOjY2MDAwMDAwLCJ0b2tlblR5cGUiOiJBQ0NFU1MiLCJhdXRoVHlwZSI6IlNVUlZFWV9SRVNQT05TRSIsImlhdCI6MTc1ODUzMjQ2NywianRpIjoic3ByaW5rbHIifQ.HuQXlfT-j7cGOM8sldp4cJRolSP-sqzgUMhzI5ezu249tqD2PWWaBUJsY6ywOMIU1luAJOGaDrMKNnw_8yJHW48SyeZ8zmE-rvk4FGamXXLo2ejERNgWv7zPJvBVGxhrJp80PrEeHoT0uaPxPCgrs-ebAtKaqJgezoXgnChln8UDRs1G3VOXZWHzkltRhuw6ya7OS6vXmGH1dkDqz8UlhB61lX2Hum81DHQGOV1IsgXv0ZZlXeYkb8nx2HRGS3wWrl73weldElgbq3g4P_GuEPyopKDHKaPdF4Ij3onYRm269QKNX0G9VE_0oyne_QHWveKWJ0wXQcZTuxl_A3IU6w&clickTimeEpoch=%25click_time_epoch%25&optOut=true",
        "linkCreatedAt": "Sep 22, 2025, 09:14:24 AM",
        "surveyType": "STANDARD",
        "distributionId": "68c8ea1f49fb99572152e44d",
        "distributionName": "Distribute BR",
        "programId": "68b84e4ece5145476093ce85",
        "programName": "Documentation Feedback"
    },
    "errors": []
}




## Response Parameters




















[Profile Object](https://dev.sprinklr.com/generate-personalized-survey-link#profile-response-table)






[Transaction Object](https://dev.sprinklr.com/generate-personalized-survey-link#transaction-response-table)
































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Main data object containing sub-objects and fields. | Object |
|  | profile | User profile information.See  table below. | Object |
|  | transaction | User transaction information.See  table below. | Object |
|  | surveyName | Name of the survey. | String |
|  | surveyLink | Link to the survey form. | String |
|  | optOutUrl | Link to opt out of the survey. | String |
|  | linkCreatedAt | Timestamp when the survey link was created. | String |
|  | surveyType | Type of the survey. | String |
|  | distributionId | Identifier for survey distribution. | String |
|  | distributionName | Name of the survey distribution. | String |
|  | programId | Identifier for the survey program. | String |
|  | programName | Name of the survey program. | String |
| errors |  | Any error details related to the response. | Array/Object |

### Profile Object





















| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| contact |  | Required | Contains user contact information. | Object |
|  | firstName | Optional | First name of the user. | String |
|  | lastName | Optional | Last name of the user. | String |
|  | fullName | Optional | Full name of the user. | String |
|  | email | Optional | Email address. | String |
|  | phoneNo | Optional | Contact phone number. | String |
|  | website | Optional | List of associated websites. | Array[String] |
| demographics |  | Optional | User demographic data. | Object |
|  | gender | Optional | Gender of the user. | String |
|  | location | Optional | User’s location. | String |
| profiles[] |  | Optional | List of social or channel accounts. | Array[Object] |
|  | name | Optional | Display name for the account. | String |
|  | channelType | Required | Communication channel (for example, EMAIL). | String |
|  | channelId | Required | Identifier for the channel. | String |
|  | permalink | Optional | Unique identifier/handle for the account. | String |
|  | followers | Optional | Number of followers. | Integer |
|  | bio | Optional | Bio or description. | String |
|  | avatarUrl | Optional | Profile picture URL. | String |
|  | following | Optional | Number of followed accounts. | Integer |
|  | unSubscribed | Optional | Whether the user unsubscribed. | Boolean |
|  | deleted | Optional | Whether the account is deleted. | Boolean |
|  | statusCount | Optional | Number of messages/statuses. | Integer |
|  | accountSpecificInfos | Optional | Custom channel-specific details. | Object |
|  | additional | Optional | Any additional data. | Object |
|  | verified | Optional | Whether the account is verified. | Boolean |
| listMemberships |  | Optional | IDs of lists the user belongs to. | Array[Int] |
| customProperties |  | Optional | Key-value pairs for custom user attributes. | Object |
| spaceAssignments[] |  | Optional | List of space-level user data mappings. | Array[Object] |
|  | spaceId | Required | ID of the assigned space or context. | String |
|  | listMemberships | Optional | List IDs specific to this space. | Array[Int] |
|  | tags | Optional | Tags for segmentation or categorization. | Array[String] |

### Transaction Object



















































| Parameter | Description | Type |
| --- | --- | --- |
| id | ID of the transaction. | String |
| transactionGroupId | ID for the transaction group. | String |
| profileName | Name of the user tied to the transaction. | String |
| channelProfileId | Identifier for the communication profile. | String |
| distributionChannel | Channel used for distribution. | String |
| transactionGroupType | Type of transaction group. | String |
| customProperties | Custom key-value metadata for the transaction. | Object |
| isArchived | Indicates if the transaction is archived. | Boolean |


  [](https://dev.sprinklr.com/generate-personalized-survey-link)




[Back to top](https://dev.sprinklr.com/generate-personalized-survey-link)
