---
title: "Fetch Ad User Accounts"
slug: fetch-ad-user-accounts
url: https://dev.sprinklr.com/fetch-ad-user-accounts
---

# Fetch Ad User Accounts

#  POST Fetch Ad User Accounts

This API retrieves a list of social ad accounts associated with a specific user. The endpoint supports filtering based on ad objective, destination type, and user permissions. It is primarily used in the context of paid media publishing to identify eligible accounts for campaign creation or management.


## API Endpoint

https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/user/accounts

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


## Request Body Parameters












































      ``





      ``









| Field | Type | Required | Description |
| --- | --- | --- | --- |
| accountUserId | string | Yes | User ID associated with the social ad account. |
| adObjective | String (Enum) | Yes | Specifies the advertising objective. |
| destinationType | String (Enum) | No | The type of destination associated with the ad objective. |
| start | Integer | No | The starting index for pagination. |
| limit | Integer | No | The maximum number of results to retrieve. |
| userAction | String | No | The action performed by the user. Supported enum value: PUBLISH. |
| keyword | String | No | The keyword used for filtering or searching. This parameter is used for PINTEREST as a channel. |
| permissions | String | No | The set of permissions associated with the user. |

### Enum Values for adObjective

















| Enum | Label |
| --- | --- |
| OUTCOME_AWARENESS | Facebook Awareness |
| OUTCOME_ENGAGEMENT | Facebook Engagement |
| OUTCOME_LEADS | Facebook Leads |
| OUTCOME_SALES | Facebook Sales |
| OUTCOME_TRAFFIC | Facebook Traffic |
| OUTCOME_APP_PROMOTION | Facebook App Promotion |
| MARKETING_MESSAGES | Marketing Messages |

## Objective to Destination Type Mapping

The following table lists the supported `destinationType` values for each `adObjective`. Use this reference to determine valid destination types for your selected objective when configuring an ad.

Objectives like `OUTCOME_APP_PROMOTION` and `MARKETING_MESSAGES` do not support any destination types.


















| Objective (adObjective) | Destination Type (destinationType) |
| --- | --- |
| OUTCOME_TRAFFIC | WEBSITE_MESSENGER |
| APP_STORE |  |
| WHATSAPP |  |
| MESSENGER |  |
| INSTAGRAM_DIRECT |  |
| PHONE_CALL |  |
| INSTAGRAM_PROFILE |  |
| OUTCOME_AWARENESS | STORE_VISIT |
| WEBSITE_MESSENGER |  |
| OUTCOME_ENGAGEMENT | ON_POST |
| ON_VIDEO |  |
| WEBSITE_MESSENGER |  |
| ON_PAGE |  |
| WHATSAPP |  |
| APP_STORE |  |
| PHONE_CALL |  |
| ON_EVENT |  |
| CLICK_TO_MESSENGER |  |
| ON_REMINDER |  |
| SPONSORED_MESSAGES |  |
| OUTCOME_SALES | WEBSITE_MESSENGER |
| CATALOG |  |
| APP_STORE |  |
| WEBSITE_APP |  |
| WHATSAPP |  |
| MESSENGER |  |
| PHONE_CALL |  |
| OUTCOME_LEADS | ON_AD |
| WEBSITE_MESSENGER |  |
| MESSENGER |  |
| LEAD_FORM_MESSENGER |  |
| APP_STORE |  |
| LEAD_FROM_IG_DIRECT |  |
| PHONE_CALL |  |
| OUTCOME_APP_PROMOTION | (No destination types) |
| MARKETING_MESSAGES | (No destination types) |

## Steps to Retrieve `accountUserId`


- In Sprinklr, click the **New Page (+)** icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the Accounts page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the **User ID** column. This value corresponds to the `accountUserId`.

## Example Request

Copy Code


curl --location 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/user/accounts' \
--header 'Authorization: Bearer {Token}’ \
--header 'Key: {Api_Key}’ \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "adObjective": "OUTCOME_TRAFFIC",
    "accountUserId": "394232028806869",
    "destinationType": "WEBSITE",
    "start": "1",
    "limit": "20"
}'

## Example - Response


{
  "data": {
    "userAccountDTOS": [
      {
        "account": {
          "id": "663c95d46b23847f26606cf1",
          "accountId": 66014675,
          "accountUserId": "243810015485012",
          "accountType": "FBPAGE",
          "displayName": "Alok Page",
          "snType": "FACEBOOK",
          "businessCategory": "CORPORATE",
          "profileImgUrl": "https://storage.googleapis.com/...png",
          "accountUrl": "https://www.facebook.com/243810015485012",
          "userPermissions": ["ALL"],
          "accountHealth": {
            "status": "ACTION_REQUIRED",
            "issueKeys": [
              "FBPAGE_PERMISSION_MISSING_pages_manage_metadata",
              "FBPAGE_PERMISSION_MISSING_publish_video"
            ],
            "impactedAreas": [
              "Engagement",
              "Publishing",
              "Reporting"
            ],
            "updatedTime": 1753449787297
          }
        },
        "type": "PAGE",
        "properties": {
          "user_roles": [
            "ADVERTISE",
            "ANALYZE",
            "CREATE_CONTENT",
            "MESSAGING",
            "MODERATE",
            "MANAGE"
          ]
        }
      }
    ]
  },
  "errors": []
}

## Response Schema

Returns a list of social accounts under the `data` object containing the `userAccountDTOS` array.






















































































| Field | Sub Parameter | Type | Description |
| --- | --- | --- | --- |
| account | id | string | Internal ID of the account in Sprinklr. |
| accountId | number | Account ID used for paid publishing. |  |
| accountUserId | string | Social network user ID. |  |
| accountType | string | Type of account (e.g., FBPAGE, TWITTERHANDLE). |  |
| displayName | string | Display name of the account. |  |
| snType | string | Social network type (e.g., FACEBOOK, INSTAGRAM). |  |
| businessCategory | string | Business category of the account (e.g., CORPORATE). |  |
| profileImgUrl | string | URL of the profile image associated with the account. |  |
| accountUrl | string | Public URL of the social media account. |  |
| userPermissions | array | List of granted user-level permissions. |  |
| accountHealth | - | object | Account health details, including any permission issues. |
| type | - | string | Type of entity (e.g., PAGE, ACCOUNT). |
| properties | - | object | Properties associated with the account. |
| user_roles | array | List of roles assigned to the user on this account. |  |

[](https://dev.sprinklr.com/fetch-ad-user-accounts)

[Back to top](https://dev.sprinklr.com/fetch-ad-user-accounts)
