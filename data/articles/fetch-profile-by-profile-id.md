---
title: "Fetch Profile by Profile Id"
slug: fetch-profile-by-profile-id
url: https://dev.sprinklr.com/fetch-profile-by-profile-id
---

# Fetch Profile by Profile Id

#
  GET Fetch Profile by Profile Id


	Using this API, you can fetch the data and metadata (stored in Sprinklr) associated with a profile for the given profile Id.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/profile/{profileId}


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










| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| profileId | Requied | Profile Id of the profile, you want to fetch.This is the profile id you receive in the create universal profile API response. | String |

## Example - Request















Copy Code



curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/profile/630087a8b8ef87db98bac318' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






## Example - Response





{
    "data": {
        "id": "630087a8b8ef87db98bac318",
        "contact": {
            "firstName": "John",
            "lastName": "Doe",
            "fullName": "John Doe",
            "phoneNo": "08884979555",
            "website": [
                "www.johndoe.com/",
                "123456789",
                "nicetest.com"
            ],
            "phoneDetails": [],
            "emailDetails": []
        },
        "demographics": {
            "location": "ca"
        },
        "works": [
            {
                "name": "Sprinklr india",
                "description": "Senior Project Development Manager 1",
                "title": "Senior Project Development Manager 4",
                "startDate": "3/2015",
                "endDate": "5/2022",
                "location": "California"
            },
            {
                "name": "sprinklr",
                "title": "senior developer",
                "startDate": "1/2021",
                "endDate": "2/2022"
            },
            {
                "name": "Sprinklr Japan",
                "description": "Senior Project Development Manager 12454",
                "title": "Senior Project Development Manager 134",
                "startDate": "3/2016",
                "endDate": "5/2021",
                "location": "India"
            },
            {
                "name": "Sprinklr",
                "description": "Senior Project Development Manager 2",
                "title": "Senior Project Development Manager 3",
                "startDate": "3/2015",
                "location": "Maharashtra, India"
            },
            {
                "name": "Sprinklr pvt ltd",
                "description": "Senior Project Development Manager 2",
                "title": "Senior Project Development Manager 2",
                "startDate": "3/2015",
                "endDate": "5/2022",
                "location": "India"
            }
        ],
        "profiles": [
            {
                "name": "John Doe",
                "channelType": "LINKEDIN",
                "channelId": "A_VZ01N30G",
                "permalink": "https://www.linkedin.com/in/john-doe-1855b120a/",
                "avatarUrl": "https://media.licdn.com/dms/image/D4D03AQGqA28WLrtltA/profile-displayphoto-shrink_800_800/0/1680075563811?e=1686182400&v=beta&t=CU8pwiWWM7RNCjNEblvF_1SQevfW8zgVKdp8-o76X8U&profileImageKey=urn%3Ali%3AdigitalmediaAsset%3AD4D03AQGqA28WLrtltA",
                "bio": "QA lead  2 at sprinklr, banglore, India",
                "followers": 25,
                "following": 0,
                "username": "John Doe",
                "unSubscribed": false,
                "deleted": false,
                "snCreatedTime": 0,
                "snModifiedTime": 1680587723251,
                "statusCount": 0,
                "accountSpecificInfos": [
                    {
                        "accountId": 1000136633
                    }
                ],
                "additional": {
                    "LOCATIONS": [
                        "{\"countryCode\":\"ca\",\"postalCode\":null,\"standardizedLocationUrn\":null,\"userSelectedGeoPlaceCode\":null,\"regionCode\":null}"
                    ],
                    "ADDRESS": [
                        "Ontario , Canada"
                    ],
                    "appId": [
                        "78ag8ulrglox5v"
                    ],
                    "pType": [
                        "PERSON"
                    ],
                    "headline": [
                        "Senior Associate Director"
                    ]
                }
            }
        ],
        "profileWorkflow": {
            "profileLists": [
                2,
                17518,
                3
            ],
            "customProperties": {
                "5b584ba4e4b085291d4c2e75": [
                    "profile"
                ],
                "_c_637df02b946df13455a7b9f5": [
                    "Show"
                ]
            },
            "profileSpaceWorkflows": [
                {
                    "profileLists": [
                        2691,
                        3
                    ],
                    "spaceId": "1000004509"
                }
            ]
        },
        "createdTime": 1660979112596,
        "modifiedTime": 1680587723279,
        "certificates": [
            {
                "authority": "Microsoft",
                "endMonthYear": "",
                "name": "Certified Data Scientist 2",
                "startMonthYear": "8/2020"
            },
            {
                "authority": "PMP Strategy",
                "endMonthYear": "3/2025",
                "licenseNumber": "PMP001",
                "name": "Project Management Professional (PMP)",
                "startMonthYear": "2/2019",
                "url": "www.pmp.com"
            },
            {
                "authority": "Microsoft",
                "endMonthYear": "4/2024",
                "licenseNumber": "CLA001",
                "name": "Certified Logistics Associate (CLA)",
                "startMonthYear": "2/2018"
            },
            {
                "authority": "ALTRAD",
                "endMonthYear": "",
                "licenseNumber": "34527678",
                "name": "Go lang",
                "startMonthYear": "6/2018"
            },
            {
                "authority": "Microsoft",
                "endMonthYear": "",
                "name": "Certified Data Scientist",
                "startMonthYear": "8/2020"
            }
        ],
        "educations": [
            {
                "name": "Northern Institute of Engineering Technical Campus (NIET)",
                "year": "2012",
                "startMonthYear": "2008",
                "grade": "A",
                "fieldsOfStudy": "Computer Science"
            },
            {
                "name": "Barkatullah University, Bhopal",
                "year": "2006",
                "startMonthYear": "2002",
                "grade": "A",
                "notes": "completed graguation",
                "activities": "vollyball",
                "fieldsOfStudy": "Computer Science"
            },
            {
                "name": "St Vincent2",
                "year": "2002",
                "startMonthYear": "2000",
                "grade": "A+",
                "fieldsOfStudy": "Science"
            },
            {
                "name": "Barkatullah University, Bhopal",
                "type": "B.Tech",
                "year": "2006",
                "startMonthYear": "2002",
                "grade": "A",
                "notes": "completed graguation",
                "activities": "vollyball",
                "fieldsOfStudy": "Computer Science"
            },
            {
                "name": "Northern Institute of Engineering Technical Campus (NIET)",
                "type": "Bachelor's degree",
                "year": "3/2012",
                "startMonthYear": "2/2008",
                "grade": "A++",
                "fieldsOfStudy": "Business/Managerial Economics"
            },
            {
                "name": "St. Vincent's High School",
                "type": "Intermediate",
                "year": "2003",
                "startMonthYear": "2001",
                "grade": "B",
                "fieldsOfStudy": "Computer Science"
            },
            {
                "name": "St Vincent",
                "year": "2002",
                "startMonthYear": "2000",
                "grade": "A1",
                "fieldsOfStudy": "Science"
            }
        ],
        "languages": [
            {
                "name": "English",
                "proficiency": "FULL_PROFESSIONAL"
            },
            {
                "name": "Japanese",
                "proficiency": "ELEMENTARY"
            },
            {
                "name": "Hindi",
                "proficiency": "LIMITED_WORKING"
            },
            {
                "name": "Korean",
                "proficiency": "ELEMENTARY"
            },
            {
                "name": "French",
                "proficiency": "LIMITED_WORKING"
            },
            {
                "name": "German",
                "proficiency": "ELEMENTARY"
            },
            {
                "name": "Hindi",
                "proficiency": "FULL_PROFESSIONAL"
            }
        ],
        "skills": [
            {
                "label": "Project Management"
            },
            {
                "label": "Scrum"
            },
            {
                "label": "Java"
            },
            {
                "label": "ASP.NET Web API"
            },
            {
                "label": "Customer Experience"
            },
            {
                "label": "Test Planning"
            },
            {
                "label": "Scrum Master"
            },
            {
                "label": "Team Managment - V1"
            },
            {
                "label": "Communication"
            },
            {
                "label": "Agile Testing"
            }
        ],
        "courses": [
            {
                "name": "SCRUM MASTER",
                "number": "SCR003"
            },
            {
                "name": "Java Script",
                "number": "JAVA104"
            },
            {
                "name": "AGILE Methodology 2",
                "number": "AG0042"
            },
            {
                "name": "Java Script",
                "number": "JAVA104"
            },
            {
                "name": "SCRUM MASTER",
                "number": "SCR003"
            },
            {
                "name": "SCRUM MASTER",
                "number": "SCM999"
            }
        ],
        "honors": [
            {
                "description": "Best performer of the Year 2022",
                "issueDate": "9/2022",
                "issuer": "Sprinklr",
                "title": "Best employee of the Year 2022"
            },
            {
                "issueDate": "5/2010",
                "issuer": "BPUT",
                "title": "Best Student of the year"
            },
            {
                "description": "Best performer of the Year 2023",
                "issueDate": "",
                "issuer": "St Mary's School",
                "title": "Best Student of the Year 2023"
            }
        ],
        "projects": [
            {
                "description": "Distributed project",
                "endMonthYear": "",
                "startMonthYear": "",
                "title": "Project Dst"
            },
            {
                "description": "NEw project",
                "endMonthYear": "8/2020",
                "startMonthYear": "8/2020",
                "title": "MI 6"
            },
            {
                "endMonthYear": "6/2021",
                "startMonthYear": "6/2021",
                "title": "MI 5",
                "url": "https://www.miproject.com/"
            }
        ],
        "publications": [
            {
                "date": "5/9/2022",
                "name": "Agile Methodology",
                "publisher": "ABC",
                "url": "https://www.abc.com/"
            },
            {
                "date": "8/12/2022",
                "name": "Qa Testing",
                "publisher": "test"
            }
        ],
        "testScores": [
            {
                "date": "",
                "name": "Python",
                "score": "89"
            },
            {
                "date": "11/2022",
                "name": "API Test",
                "score": "90"
            },
            {
                "date": "",
                "description": "Good test score",
                "name": "JAVA",
                "score": "100"
            },
            {
                "date": "5/2020",
                "description": "Go lang developement",
                "name": "Go lang New",
                "score": "88"
            }
        ]
    },
    "errors": []
}







### Response Parameters











| Parameter | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| id |  | Unique identifier of the unified profile. | String |
| contact |  | Contact information of the profile. | Object |
|  | firstName | First name of the profile. | String |
|  | maidenName | Maiden name of the profile. | String |
|  | lastName | Last Name of the profile. | String |
|  | fullName | Full name of the profile. | String |
|  | email | Email id of the profile. | String |
|  | phoneNo | Phone number of the profile. | String |
|  | address | Address of the profile.Schema for Address Table given below. | String |
|  | website | List of websites for the profile | List [String] |
|  | phoneDetails | Refers to the additional phone details if any | List [Integer, String] |
|  | emailDetails | Refers to the email details | List [String] |
| demographics |  | Demographic Information of the customer | Object |
|  | location | Refers to the country code of the customer's location | String |
|  | age | Age of the profile. | Integer |
|  | gender | Gender of the profile. | String |
|  | language | Language of the profile. | String |
| works |  | Array containing the customer's work experience details if listed on the social profile | Array |
|  | name | Refers to the name of the organization | String |
|  | description | Refers to the role description | String |
|  | title | Refers to the customer's designation | String |
|  | startDate | Refers to the start date of the role | String |
|  | endDate | Refers to the end date of the role | String |
|  | location | Refers to the job location | String |
| profiles |  | List of social identities linked to the profile. |  |
|  | name | Name of the person. | String |
|  | channelType | Channel type of the profile. e.g. facebook. | String |
|  | channelId | Unique id of the profile on channel. | String |
|  | permalink | Link of the profile on social channel. | String |
|  | avatarUrl | Profile image link. | String |
|  | bio | Detailed description about the user. | String |
|  | followers | Followers count of the user. | Integer |
|  | following | Refers to the number of people the customer is following | Integer |
|  | username | Unique identifier of the user. | String |
|  | verified | True if the user is verified by the channel. default: false | Boolean |
|  | unSubscribed | True if the user is subscribed for email and other activities.default: false | Boolean |
|  | deleted | True if profile is deleted natively.default: false | Boolean |
|  | snCreatedTime | Social Channel created time. | Epoch |
|  | snModifiedTime | Social Channel modified time. | Epoch |
|  | statusCount | Refers to the number of statuses posted by the customer on the channel | Integer |
|  | accountSpecificInfos | Array containing the account Specific Info like accountId, externalId, etc. | Array |
|  | additional | Object containing the additional profile details | Object |
| profileWorkflow |  | Object containing the profile workflow details | Object |
|  | profileLists | Refers to the profile lists if any | List [Integer] |
|  | customProperties | Key and value pair for custom property name and value | Object |
|  | profileSpaceWorkflows | Array containing the profile properties specific to a workspace | Array |
| createdTime |  | Created time of the profile in Sprinklr | Epoch |
| modifiedTime |  | Last modified time of the profile in Sprinklr | Epoch |
| certificates |  | Array containing the professional certificate details that the customer holds |  |
| education |  | Array containing the education details of the customer | Array |
| languages |  | Array containing the language details | Array |
| skills |  | Array containing the skills that the customer has | Array |
| courses |  | Array containing the course details the customer has taken | Array |
| honors |  | Array containing the customer achievements |  |
| project |  | Array containing the details for the projects the customer has worked on |  |
| publications |  | Array containing the publications related to the customer | Array |
| testScores |  | Array containing the test score details | Array |

### Address Parameter Description Table








| Parameter | Description | Type |
| --- | --- | --- |
| street1 | First line of the user's address. | String |
| street2 | Second line of the user's address. | String |
| city | The city of the user's address to help identify the location. | String |
| state | The state of the user's address. | String |
| country | The country of the user's address. | String |
| postalCode | ZIP Code of the address. | String |

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









| Parameter | Sub Parameter | Description | Type |
| --- | --- | --- | --- |
| spaceId |  | Client Id. | String |
| modifiedTime |  | Last modified time of the space workflow | Integer |
| customFields |  | Client custom properties on the asset, if any. | String |
| queues |  | Client queue details of the message, if any. | Integer |
|  | queueId | Queue identifier to add the message to queue. | Integer |
|  | assignmentTime | Assignment time of the queue to the message. | Integer |
| profileLists |  | Client profile lists on the profile, if any. | Integer |

[](https://dev.sprinklr.com/fetch-profile-by-profile-id)





[Back to top](https://dev.sprinklr.com/fetch-profile-by-profile-id)
