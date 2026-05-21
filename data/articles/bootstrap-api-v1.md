---
title: "Bootstrap API V1"
slug: bootstrap-api-v1
url: https://dev.sprinklr.com/bootstrap-api-v1
---

# Bootstrap API V1

#
 GET  Bootstrap API V1


Use the following endpoints to retrieve lists & metadata of objects configured in the environment.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/bootstrap/resources

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |

## Supported Query Parameters

[PARTNER_ACCOUNTS](https://dev.sprinklr.com/bootstrap-api-v1#PARTNER_ACCOUNTS)

[USER_ACCESSIBLE_ACCOUNTS](https://dev.sprinklr.com/bootstrap-api-v1#USER_ACCESSIBLE_ACCOUNTS)

[PARTNER_CAMPAIGNS](https://dev.sprinklr.com/bootstrap-api-v1#PARTNER_CAMPAIGNS)

[PARTNER_ACCOUNT_GROUPS](https://dev.sprinklr.com/bootstrap-api-v1#PARTNER_ACCOUNT_GROUPS)

[PARTNER_USERS](https://dev.sprinklr.com/bootstrap-api-v1#PARTNER_USERS)

[PARTNER_USERS&clientId={workspace_id}](https://dev.sprinklr.com/bootstrap-api-v1#PARTNER_USERS_WORKSPACE)

[CLIENTS](https://dev.sprinklr.com/bootstrap-api-v1#CLIENTS)

[CLIENT_URL_SHORTNERS](https://dev.sprinklr.com/bootstrap-api-v1#CLIENT_URL_SHORTNERS)

[INBOUND_CUSTOM_FIELDS](https://dev.sprinklr.com/bootstrap-api-v1#INBOUND_CUSTOM_FIELDS)

[OUTBOUND_CUSTOM_FIELDS](https://dev.sprinklr.com/bootstrap-api-v1#OUTBOUND_CUSTOM_FIELDS)

[PROFILE_CUSTOM_FIELDS](https://dev.sprinklr.com/bootstrap-api-v1#PROFILE_CUSTOM_FIELDS)

[USER_CUSTOM_FIELDS](https://dev.sprinklr.com/bootstrap-api-v1#USER_CUSTOM_FIELDS)

[MEDIA_ASSET_CUSTOM_FIELDS](https://dev.sprinklr.com/bootstrap-api-v1#MEDIA_ASSET_CUSTOM_FIELDS)

[ACCOUNT_CUSTOM_FIELDS](https://dev.sprinklr.com/bootstrap-api-v1#ACCOUNT_CUSTOM_FIELDS)

[LISTENING_TOPIC_CUSTOM_FIELDS](https://dev.sprinklr.com/bootstrap-api-v1#LISTENING_TOPIC_CUSTOM_FIELDS)

[LISTENING_THEME_CUSTOM_FIELDS](https://dev.sprinklr.com/bootstrap-api-v1#LISTENING_THEME_CUSTOM_FIELDS)

[UM_STATUSES](https://dev.sprinklr.com/bootstrap-api-v1#UM_STATUSES)

[UM_PRIORITIES](https://dev.sprinklr.com/bootstrap-api-v1#UM_PRIORITIES)

[ACCESSIBLE_USERS](https://dev.sprinklr.com/bootstrap-api-v1#ACCESSIBLE_USERS)

[APPROVAL_PATHS](https://dev.sprinklr.com/bootstrap-api-v1#APPROVAL_PATHS)

[PARTNER_QUEUES/CLIENT_QUEUES](https://dev.sprinklr.com/bootstrap-api-v1#PARTNER_QUEUES_CLIENT_QUEUES)

[UNIVERSAL_CASE_QUEUES](https://dev.sprinklr.com/bootstrap-api-v1#UNIVERSAL_CASE_QUEUES)

[PARTNER_PROFILE_LISTS/CLIENT_PROFILE_LISTS](https://dev.sprinklr.com/bootstrap-api-v1#PARTNER_PROFILE_LISTS_CLIENT_PROFILE_LISTS)

[MACROS](https://dev.sprinklr.com/bootstrap-api-v1#MACROS)

[PERMISSIONS](https://dev.sprinklr.com/bootstrap-api-v1#PERMISSIONS)

[USER_GROUPS](https://dev.sprinklr.com/bootstrap-api-v1#USER_GROUPS)

| Type | Description |
| --- | --- |
|  | Extract all the social accounts available in the customer's environment |
|  | Extract all the workspaces' information accessible to the user associated with the token |
|  | Extract all the campaigns available in the customer's environment |
|  | Extract all the account groups available in the customer's environment |
|  | Fetch all the users available in the customer's environment |
|  | Extract list of all the users available in the customer's environment within the specific workspace |
|  | Extract all the workspaces configured with the customer's environment |
|  | Extract all the URL shorteners present within the environment |
|  | Extract all the inbound level custom fields |
|  | Extract all the outbound level custom fields |
|  | Extract all the profile level custom fields |
|  | Extract all the user level custom fields |
|  | Extract all the media asset level custom fields |
|  | Extract all the account asset level custom fields |
|  | Extract all the listening topic asset level custom fields |
|  | Extract all the listening theme asset level custom fields |
|  | Extracts the list of statuses with respect to universal messages |
|  | Extracts the list of priorities with respect to universal messages |
|  | Extracts list of users who have access to the workspace associated with the authorization token |
|  | Extracts list of all the approval paths present within the customer environment |
|  | Extracts all the details related to inbound message queues |
|  | Extracts all the details related to case queues |
|  | Extracts the details related to workspace/global profile lists |
|  | Extracts the list of all macros configured within the partner enviornment |
|  | Extracts the list of all permissions associated with the user linked to the authorization token |
|  | Extracts the list of all the user groups available in the partner environment |

**Dev Notes: **For fetching the data from a particular workspace, you can specify the clientId in the query parameters.

 For example, https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=MEDIA_ASSET_CUSTOM_FIELDS&clientId=100

### Partner Accounts

Returns the list of all active accounts in the partner environment.















Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=PARTNER_ACCOUNTS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
 "accountId": 22,
    "accountType": "TWITTER",
    "accountUserId": "1652452622",
    "isActive": true,
    "screenName": "jhon_goes",
    "profileImgUrl": "http://abs.twimg.com/sticky/default_profile_images/default_profile_2_normal.png",
    "ownerUserId": 26,
    "snType": "TWITTER",
    "userPermissions": ["ALL"],
    "report": "ACCOUNT"
}







### User Accessible Accounts

Returns the list of all accounts the user associated with the authorization token has access to.















Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=USER_ACCESSIBLE_ACCOUNTS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "USER_ACCESSIBLE_ACCOUNTS": [
        {
            "accountId": 999700,
            "accountType": "WHATSAPP_BUSINESS",
            "accountUserId": "87234565234",
            "screenName": "API Testing",
            "displayName": "API Testing",
            "snType": "WHATSAPP_BUSINESS",
            "createdTime": "2023-05-30 18:27:28",
            "modifiedTime": "2023-05-30 18:27:28",
            "ownerUserId": 600000001,
            "userPermissions": [
                "ALL"
            ],
            "followerCount": 0,
            "followingCount": 0,
            "statusCount": 0,
            "accountProps": {
                "accountId": "999700"
            },
            "report": "ACCOUNT"
        }
   ]
}







### Partner Campaigns

Returns the list of global campaigns in the partner environment














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=PARTNER_CAMPAIGNS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









 {
    "campaignId": 8,
    "campaignName": "Campaign 3",
    "external": false,
    "startDate": 1470181680000,
    "endDate": 1498866480000,
    "status": "APPROVED",
    "clientId": 4,
    "deleted": false
}







### Partner Account Groups

Returns the list of account groups.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=PARTNER_ACCOUNT_GROUPS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "id": "5515eacce4b0459cff2ae769",
    "groupName": "Test Accounts",
    "description": "",
    "assetGroupType": "DEFINED",
    "containedIds": ["22", "23", "36", "33", "24", "26", "37"],
    "assetType": "ACCOUNT",
    "clientId": 4,
    "deleted": false,
    "ownerUserId": 39
}







### Partner Users

Returns the list of all users in the partner environment.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=PARTNER_USERS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "userId": 25,
    "firstName": "First",
    "lastName": "Last",
    "emailAddress": "email@sprinklr.com",
    "profileImageUrl": "http://www.gravatar.com/avatar/e75a2w90fc9789f68f6166d2a8ac365e8?d=http://s3.amazonaws.com/spr-uploads/7/1/1362258601872/default-user.png",
    "passwordLoginDisabled": false,
    "visibleId": "First Last"
}







### PARTNER_USERS for Given Client Id

Returns the list of all local users in the client environment














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=PARTNER_USERS&clientId=4' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






### Clients

Returns all the workspaces within Sprinklr Partner environment.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=CLIENTS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "CLIENTS": [
        {
            "clientId": 7647,
            "partnerId": 1090,
            "clientName": "Good Knight Financial"
        },
        {
            "clientId": 7648,
            "partnerId": 1090,
            "clientName": "Good Knight Suites"
        },
        {
            "clientId": 7649,
            "partnerId": 1090,
            "clientName": "Good Knight Wellness"
        }
    ]
}







### Client URL Shorteners

Returns the list of URL shorteners present within the workspace.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=CLIENT_URL_SHORTNERS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "CLIENT_URL_SHORTNERS": {
        "urlShortners": [
            {
                "id": "5547_spr.ly",
                "urlShortner": "spr.ly",
                "clientId": 5547,
                "tinyUrlProvider": "SPRINKLR",
                "name": "Sprinklr"
            }
        ],
        "defaultShortner": {
            "id": "5547_spr.ly",
            "urlShortner": "spr.ly",
            "clientId": 5547,
            "tinyUrlProvider": "SPRINKLR",
            "name": "Sprinklr"
        },
        "clientDNS": "spr.ly"
    }
}







### Inbound Custom Fields

Returns the list of inbound custom properties.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=INBOUND_CUSTOM_FIELDS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "id": "5515edcbe4b0459cff2ae772",
    "clientId": 4,
    "globalAsset": false,
    "assetClassList": ["MESSAGE"],
    "fieldType": "PICKLIST",
    "fieldName": "5515ed936687eb2d72000000",
    "label": {
        "en": "InboundCategory"
    },
    "description": "Test custom property for the Sandbox",
    "helpText": {
        "en": ""
    },
    "options": ["Category1", "Category2", "Category3", ""],
    "defaultValue": "",
    "dateµcreatedTime": 1427500491800,
    "dateµmodifiedTime": 1460438094878,
    "facetEnabled": false,
    "adhocSearchEnabled": false,
    "enabled": true,
    "contentReplacementEnabled": false,
    "preferred": false,
    "required": false,
    "isHidden": false,
    "order": 1,
    "scopeType": "DEFAULT",
    "optionType": "GENERAL",
    "controllingFieldConfig": {},
    "controllingFieldId": "",
    "assetClass": "MESSAGE",
    "report": "CUSTOM_FIELD"
}







### Outbound Custom Fields

Returns the list of outbound custom properties.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=OUTBOUND_CUSTOM_FIELDS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "id": "5515ed61e4b0459cff2ae770",
    "clientId": 4,
    "globalAsset": false,
    "assetClassList": ["OUTBOUND_MESSAGE"],
    "fieldType": "PICKLIST",
    "fieldName": "5515ed1e6687eb5b04000000",
    "label": {
        "en": "Sub-type"
    },
    "description": "A custom property values for Sandbox testing",
    "helpText": {
        "en": ""
    },
    "options": ["Subtype1", "Subtype2", "Subtype3", ""],
    "defaultValue": "",
    "dateµcreatedTime": 1427500385430,
    "dateµmodifiedTime": 1460438094864,
    "facetEnabled": false,
    "adhocSearchEnabled": false,
    "enabled": true,
    "contentReplacementEnabled": false,
    "preferred": false,
    "required": false,
    "isHidden": false,
    "order": 1,
    "scopeType": "DEFAULT",
    "optionType": "GENERAL",
    "controllingFieldConfig": {},
    "controllingFieldId": "",
    "assetClass": "OUTBOUND_MESSAGE",
    "report": "CUSTOM_FIELD"
}







### PROFILE_CUSTOM_FIELDS

Returns the list of profile custom properties.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=PROFILE_CUSTOM_FIELDS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "id": "56fbccbde4b0629c138363e3",
    "globalAsset": true,
    "assetClassList": ["PROFILE"],
    "fieldType": "TEXT_MULTI",
    "fieldName": "Listening_Brand_Preference",
    "label": {
        "en": "Listening Brand Preference"
    },
    "description": "",
    "helpText": {
        "en": ""
    },
    "defaultValue": "",
    "dateµcreatedTime": 1459342525881,
    "dateµmodifiedTime": 1460438095034,
    "category": "",
    "facetEnabled": false,
    "adhocSearchEnabled": false,
    "enabled": true,
    "contentReplacementEnabled": false,
    "preferred": false,
    "required": false,
    "isHidden": false,
    "order": 0,
    "scopeType": "DEFAULT",
    "optionType": "GENERAL",
    "assetClass": "PROFILE",
    "report": "CUSTOM_FIELD"
}







### USER_CUSTOM_FIELDS

Returns the list of user custom properties.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=USER_CUSTOM_FIELDS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "USER_CUSTOM_FIELDS": [
        {
            "id": "655f4b267041592a5eccca96",
            "globalAsset": true,
            "assetClassList": [
                "USER"
            ],
            "fieldType": "PICKLIST",
            "fieldName": "_c_655f4b267041592a5eccca94",
            "label": {
                "en": "influencer test"
            },
            "description": "test description for influencer ",
            "options": [
                "100"
            ],
            "optionsOrder": "DESCENDING",
            "options2": [
                {
                    "label": "100",
                    "value": "100"
                }
            ],
            "dateµcreatedTime": 1700743974935,
            "dateµmodifiedTime": 1700746740752,
            "assetVsCategory": {},
            "additional": {},
            "visibilityCriteria": {
                "restricted": false
            },
            "assetLevelConfig": [
                {
                    "assetClasses": [],
                    "facetEnabled": false,
                    "required": false,
                    "contentReplacementEnabled": false,
                    "adhocSearchEnabled": false,
                    "autofillControllingFields": false,
                    "favoriteByAdmin": false
                }
            ],
            "assetTypeVsOrder": {
                "ACCOUNT": 1.700743974935E12
            },
            "facetEnabled": false,
            "adhocSearchEnabled": false,
            "enabled": true,
            "contentReplacementEnabled": false,
            "preferred": false,
            "required": false,
            "isHidden": false,
            "isHiddenFromMonitoring": false,
            "isHiddenFromCFMSurvey": false,
            "order": 0,
            "governance": {
                "visibility": {
                    "shareConfigs": [],
                    "globallyVisible": true
                }
            },
            "ownerUserId": 1000270470,
            "validationCriteria": [],
            "customFieldControllerById": {},
            "scopeType": "DEFAULT",
            "hasEntityScopedOptions": false,
            "optionType": "GENERAL",
            "optionsVisibilityList": [],
            "nested": false,
            "minimumInput": 0,
            "mandatoryForClosingTicket": false,
            "report": "CUSTOM_FIELD"
        }
    ]
}







### MEDIA_ASSET_CUSTOM_FIELDS

Returns the list of asset custom properties.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=MEDIA_ASSET_CUSTOM_FIELDS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "id": "5515ee1ae4b0459cff2ae774",
    "clientId": 4,
    "globalAsset": false,
    "assetClassList": ["MEDIA_ASSET"],
    "fieldType": "PICKLIST",
    "fieldName": "5515eddf6687eb2d72000001",
    "label": {
        "en": "RightsManagement"
    },
    "description": "Test custom property",
    "helpText": {
        "en": ""
    },
    "options": ["Allowed to use", "Copyright Restricted", "To Be Deleted", ""],
    "defaultValue": "",
    "dateµcreatedTime": 1427500570373,
    "dateµmodifiedTime": 1460438094890,
    "facetEnabled": false,
    "adhocSearchEnabled": false,
    "enabled": true,
    "contentReplacementEnabled": false,
    "preferred": false,
    "required": false,
    "isHidden": false,
    "order": 1,
    "scopeType": "DEFAULT",
    "optionType": "GENERAL",
    "controllingFieldConfig": {},
    "controllingFieldId": "",
    "assetClass": "MEDIA_ASSET",
    "report": "CUSTOM_FIELD"
}







### ACCOUNT_CUSTOM_FIELDS

Returns the list of account custom properties.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=ACCOUNT_CUSTOM_FIELDS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "id": "573ee0c8e4b0c529ab867e2d",
    "clientId": 4,
    "globalAsset": false,
    "assetClassList": ["ACCOUNT"],
    "fieldType": "PICKLIST",
    "fieldName": "573ee0c8e4b0c529ab867e2c",
    "label": {
        "en": "Account Country"
    },
    "description": "Country",
    "helpText": {
        "en": ""
    },
    "options": ["United States of America", "Afghanistan", "Albania"],
    "defaultValue": "United States of America",
    "dateµcreatedTime": 1463738568880,
    "dateµmodifiedTime": 1463738568880,
    "facetEnabled": true,
    "adhocSearchEnabled": false,
    "enabled": true,
    "contentReplacementEnabled": false,
    "preferred": false,
    "required": false,
    "isHidden": false,
    "order": 0,
    "customFieldControllerById": {},
    "scopeType": "DEFAULT",
    "optionType": "GENERAL",
    "report": "CUSTOM_FIELD"
}






### Listening Topic Custom Fields

Returns the list of custom properties associated with Listening Topics.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=LISTENING_TOPIC_CUSTOM_FIELDS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "LISTENING_TOPIC_CUSTOM_FIELDS": [
        {
            "id": "5b1f85bfe4b0279054c993be",
            "globalAsset": true,
            "assetClassList": [
                "LISTENING_TOPIC"
            ],
            "fieldType": "PICKLIST",
            "fieldName": "5b1f85bfe4b0279054c993bb",
            "label": {
                "en": "Brand type"
            },
            "helpText": {},
            "options": [
                "brand A",
                "brand B"
            ],
            "optionsOrder": "USER_DEFINED",
            "options2": [
                {
                    "label": "brand A",
                    "value": "brand A"
                },
                {
                    "label": "brand B",
                    "value": "brand B"
                }
            ],
            "dateµcreatedTime": 1528792511119,
            "dateµmodifiedTime": 1528792511119,
            "category": "",
            "visibilityCriteria": {},
            "assetLevelConfig": [
                {
                    "assetClasses": [],
                    "facetEnabled": false,
                    "required": false,
                    "contentReplacementEnabled": false,
                    "adhocSearchEnabled": false,
                    "autofillControllingFields": false
                }
            ],
            "assetTypeVsOrder": {
                "LISTENING_TOPIC": 1.528792511119E12
            },
            "facetEnabled": false,
            "adhocSearchEnabled": false,
            "enabled": true,
            "contentReplacementEnabled": false,
            "preferred": false,
            "required": false,
            "isHidden": false,
            "isHiddenFromMonitoring": false,
            "order": 0,
            "governance": {
                "visibility": {
                    "shareConfigs": [],
                    "globallyVisible": true
                }
            },
            "ownerUserId": 1000053168,
            "customFieldControllerById": {},
            "scopeType": "DEFAULT",
            "optionType": "GENERAL",
            "nested": false,
            "minimumInput": 0,
            "mandatoryForClosingTicket": false,
            "report": "CUSTOM_FIELD"
        },
        {
            "id": "5ce3c4a5e4b01c6eb6029b27",
            "globalAsset": true,
            "assetClassList": [
                "LISTENING_TOPIC"
            ],
            "fieldType": "PICKLIST",
            "fieldName": "5ce3c4a5e4b01c6eb6029b24",
            "label": {
                "en": "NewCF"
            },
            "helpText": {},
            "options": [
                "1",
                "2",
                ""
            ],
            "optionsOrder": "USER_DEFINED",
            "options2": [
                {
                    "label": "1",
                    "value": "1"
                },
                {
                    "label": "2",
                    "value": "2"
                },
                {
                    "label": "",
                    "value": ""
                }
            ],
            "dateµcreatedTime": 1558430885813,
            "dateµmodifiedTime": 1558430885813,
            "category": "",
            "visibilityCriteria": {
                "assetVsFilters": {}
            },
            "assetLevelConfig": [
                {
                    "assetClasses": [],
                    "facetEnabled": false,
                    "required": false,
                    "contentReplacementEnabled": false,
                    "adhocSearchEnabled": false,
                    "autofillControllingFields": false
                }
            ],
            "assetTypeVsOrder": {
                "LISTENING_TOPIC": 1.558430885813E12
            },
            "facetEnabled": false,
            "adhocSearchEnabled": false,
            "enabled": true,
            "contentReplacementEnabled": false,
            "preferred": false,
            "required": false,
            "isHidden": false,
            "isHiddenFromMonitoring": false,
            "order": 0,
            "governance": {
                "visibility": {
                    "shareConfigs": [],
                    "globallyVisible": true
                }
            },
            "ownerUserId": 1000063369,
            "validationCriteria": [],
            "customFieldControllerById": {},
            "scopeType": "DEFAULT",
            "optionType": "GENERAL",
            "optionsVisibilityList": [],
            "assetVsFilters": {},
            "nested": false,
            "minimumInput": 0,
            "mandatoryForClosingTicket": false,
            "report": "CUSTOM_FIELD"
       }
    ]
}







### Listening Theme Custom Fields

Returns the list of custom properties associated with Listening Themes.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=LISTENING_THEME_CUSTOM_FIELDS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "LISTENING_THEME_CUSTOM_FIELDS": [
        {
            "id": "5bab707de4b0947df29a419a",
            "clientId": 1000004509,
            "globalAsset": false,
            "assetClassList": [
                "PROFILE",
                "LISTENING_TOPIC",
                "LISTENING_THEME"
            ],
            "fieldType": "DATE",
            "fieldName": "5bab707de4b0947df29a4197",
            "label": {
                "en": "Date created"
            },
            "helpText": {},
            "optionsOrder": "USER_DEFINED",
            "dateµcreatedTime": 1537962109875,
            "dateµmodifiedTime": 1590735324812,
            "visibilityCriteria": {
                "assetVsFilters": {}
            },
            "assetLevelConfig": [
                {
                    "assetClasses": [],
                    "facetEnabled": false,
                    "required": false,
                    "contentReplacementEnabled": false,
                    "adhocSearchEnabled": false,
                    "autofillControllingFields": false
                }
            ],
            "assetTypeVsOrder": {
                "LISTENING_TOPIC": 1.590735324812E12,
                "LISTENING_THEME": 1.590735324812E12,
                "PROFILE": 1.537962109875E12
            },
            "facetEnabled": false,
            "adhocSearchEnabled": false,
            "enabled": true,
            "contentReplacementEnabled": false,
            "preferred": false,
            "required": false,
            "isHidden": false,
            "isHiddenFromMonitoring": false,
            "order": 0,
            "governance": {
                "visibility": {
                    "shareConfigs": [
                        {
                            "shareLevel": "CLIENT",
                            "sharedWithIds": [
                                "1000004509"
                            ]
                        }
                    ],
                    "globallyVisible": false
                }
            },
            "ownerUserId": 1000070666,
            "validationCriteria": [],
            "customFieldControllerById": {},
            "scopeType": "DEFAULT",
            "optionType": "GENERAL",
            "optionsVisibilityList": [],
            "assetVsFilters": {},
            "nested": false,
            "minimumInput": 0,
            "mandatoryForClosingTicket": false,
            "report": "CUSTOM_FIELD"
        },
        {
            "id": "5f9865af8cc6d16ed3b5cf5c",
            "globalAsset": true,
            "assetClassList": [
                "MESSAGE",
                "OUTBOUND_MESSAGE",
                "ACCOUNT",
                "AD_SET",
                "AD_VARIANT",
                "BRAND",
                "CAMPAIGN",
                "MEDIA_ASSET",
                "PAID_INITIATIVE",
                "PROFILE",
                "UNIVERSAL_CASE",
                "SUB_CAMPAIGN",
                "SPR_TASK",
                "UNIVERSAL_TASK",
                "LISTENING_THEME"
            ],
            "fieldType": "PICKLIST_MULTISELECT",
            "fieldName": "_c_5f9865af8cc6d16ed3b5cf59",
            "label": {
                "en": "Mobile CF1"
            },
            "helpText": {},
            "options": [
                "bbb",
                "cccc",
                "ddd"
            ],
            "optionsOrder": "USER_DEFINED",
            "defaultValue": "bbb",
            "options2": [
                {
                    "label": "111",
                    "value": "bbb"
                },
                {
                    "label": "222",
                    "value": "cccc"
                },
                {
                    "label": "ddd``",
                    "value": "ddd"
                }
            ],
            "dateµcreatedTime": 1603823023148,
            "dateµmodifiedTime": 1667650585526,
            "assetVsCategory": {},
            "additional": {
                "delimiter": [
                    null
                ],
                "timeZone": [
                    null
                ]
            },
            "visibilityCriteria": {
                "assetVsFilters": {}
            },
            "assetLevelConfig": [
                {
                    "assetClasses": [
                        "SUB_CAMPAIGN",
                        "MESSAGE",
                        "OUTBOUND_MESSAGE",
                        "CAMPAIGN"
                    ],
                    "facetEnabled": false,
                    "required": false,
                    "contentReplacementEnabled": false,
                    "adhocSearchEnabled": false,
                    "autofillControllingFields": false
                }
            ],
            "assetTypeVsOrder": {
                "UNIVERSAL_CASE": 1.603829197032E12,
                "AD_VARIANT": 1.603829197032E12,
                "SUB_CAMPAIGN": 1.603829197032E12,
                "LISTENING_THEME": 1.603955423269E12,
                "SPR_TASK": 1.603829197032E12,
                "BRAND": 1.603829197032E12,
                "MESSAGE": 1.603823023148E12,
                "MEDIA_ASSET": 1.603829197032E12,
                "ACCOUNT": 1.603829197032E12,
                "UNIVERSAL_TASK": 1.603955423269E12,
                "PROFILE": 1.603829197032E12,
                "AD_SET": 1.603829197032E12,
                "OUTBOUND_MESSAGE": 1.603823023148E12,
                "PAID_INITIATIVE": 1.603829197032E12,
                "CAMPAIGN": 1.603829197032E12
            },
            "facetEnabled": false,
            "adhocSearchEnabled": false,
            "enabled": true,
            "contentReplacementEnabled": false,
            "preferred": false,
            "required": false,
            "isHidden": false,
            "isHiddenFromMonitoring": false,
            "order": 0,
            "governance": {
                "visibility": {
                    "shareConfigs": [],
                    "globallyVisible": true
                }
            },
            "ownerUserId": 1000090470,
            "validationCriteria": [],
            "customFieldControllerById": {},
            "scopeType": "DEFAULT",
            "optionType": "GENERAL",
            "optionsVisibilityList": [],
            "protectedField": false,
            "assetVsFilters": {},
            "nested": false,
            "minimumInput": 0,
            "mandatoryForClosingTicket": false,
            "report": "CUSTOM_FIELD"
         }
    ]
}







### UM_STATUSES

Returns the list of statues for the universal messages.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=UM_STATUSES' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "UM_STATUSES": [
        {
            "status": "New",
            "displayName": "New - GKC"
        },
        {
            "status": "Closed",
            "displayName": "Closed - GKC"
        },
        {
            "status": "Under Review",
            "displayName": "Under Review - GKC"
        },
        {
            "status": "In Progress",
            "displayName": "In Progress - GKC"
        },
        {
            "status": "Awaiting Customer Response",
            "displayName": "Awaiting Customer Response - GKC"
        },
        {
            "status": "Hidden - GKC",
            "displayName": "Hidden - GKC"
        }
    ]
}







### UM_PRIORITIES

Returns the list of priorities for the universal messages.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=UM_PRIORITIES' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "UM_PRIORITIES": [
        {
            "priority": "MEDIUM",
            "displayName": "Medium"
        },
        {
            "priority": "LOW",
            "displayName": "Low"
        },
        {
            "priority": "HIGHEST",
            "displayName": "Highest"
        },
        {
            "priority": "LOWEST",
            "displayName": "Lowest"
        },
        {
            "priority": "HIGH",
            "displayName": "High"
        }
    ]
}







### ACCESSIBLE_USERS

Returns the user profile information for users who have access to the workspace.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=ACCESSIBLE_USERS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "userId": 25,
    "userType": "PRTADMN",
    "clientId": 4,
    "partnerId": 3,
    "createdTime": "2015-01-21 20:03:30.0",
    "modifiedTime": "2015-01-27 14:34:53.0",
    "firstName": "First",
    "lastName": "Last",
    "emailAddress": "email@sprinklr.com",
    "phoneNumber": "",
    "designation": "",
    "department": "",
    "properties": "{\"approverUserId\":\"\",\"isApprovalMandatory\":false,\"clientCustomProperties\":{},\"partnerCustomProperties\":{}}",
    "isDeleted": false,
    "currentPartnerId": 3,
    "passwordSetTime": "2015-01-27 14:34:53.0",
    "loginRestrictedIPs": [],
    "profileImageUrl": "http://www.gravatar.com/avatar/e75a290fcs9789f68f6166d2a8ac365e8?d=http://s3.amazonaws.com/spr-uploads/7/1/1362258601872/default-user.png",
    "passwordLoginDisabled": false,
    "locale": "en_US",
    "partnerCustomProperties": {},
    "visibleId": "First Last"
}







### APPROVAL_PATHS

Returns the approval paths configured within in the environment.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=APPROVAL_PATHS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "id": "56bb154be4b09f63885b4aff",
    "approvalPathName": "approval 2",
    "approvalPathDescription": "",
    "approvalStepList": [{
        "stepNumber": 0,
        "assigneeType": "USER",
        "assigneeId": 151
    }, {
        "stepNumber": 1,
        "assigneeType": "USER",
        "assigneeId": 122
    }],
    "assetClass": "OUTBOUND_MESSAGE",
    "entryConditions": [{
        "key": "USER_ID",
        "condition": "IN",
        "values": ["122", "151"]
    }],
    "priority": 1,
    "enabled": true,
    "versionId": 1,
    "clientId": 4,
    "ownerUserId": 151,
    "createdTime": 1455101259315,
    "modifiedTime": 1455101274612,
    "lastModifiedUserId": 151,
    "deleted": false,
    "canEdit": false
}







### PARTNER_QUEUES/CLIENT_QUEUES

Returns the queues in the partner or client environment.

**Dev Notes: **You can only fetch "Inbound Messages" queue type with this bootstrap call.















Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=CLIENT_QUEUES' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "CLIENT_QUEUES": [
        {
            "mongoId": "58ac68c9e4b041e0413269e1",
            "clientId": 5547,
            "id": 245,
            "name": "Universal Queue",
            "description": "",
            "delFlag": false,
            "modifiedTime": "2017-02-21 16:20:25",
            "createdTime": "2017-02-21 16:20:25",
            "ownerUserId": 108466,
            "queueType": "INBOUND_MESSAGES",
            "subscribers": {
                "id": "58ac68cbde9b91e5396a9420",
                "assetClass": "CLIENT_QUEUE",
                "assetId": "5547_245",
                "shareConfigs": [
                    {
                        "shareLevel": "USER",
                        "sharedWithIds": []
                    },
                    {
                        "shareLevel": "USER_GROUP",
                        "sharedWithIds": []
                    }
                ],
                "globallyVisible": false,
                "versionId": 1
            }
        }
    ]
}







### CASE LEVEL QUEUES

Returns the case level queues configured in the partner environment.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=UNIVERSAL_CASE_QUEUES' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "UNIVERSAL_CASE_QUEUES": [
        {
            "mongoId": "60a3aabfcc063d76c33a1151",
            "partnerId": 1,
            "anomalyEnabled": false,
            "id": 104596,
            "name": "Assignment Engine Processing",
            "description": "Contains all cases awaiting assignment via Assignment Engine. Upon reaching this queue, cases are routed to the specific Work Queue by the Work Queue Assignment rule.",
            "delFlag": false,
            "modifiedTime": "2022-12-22 09:42:37",
            "createdTime": "2019-09-09 18:32:58",
            "ownerUserId": 1000116941,
            "queueType": "UNIVERSAL_CASE"
        },
        {
            "mongoId": "60a3aabfcc063d76c33a114e",
            "partnerId": 1,
            "anomalyEnabled": false,
            "id": 104595,
            "name": "Survey",
            "description": "Contains all cases ready to have a survey sent.",
            "delFlag": false,
            "modifiedTime": "2019-09-09 17:01:21",
            "createdTime": "2019-05-01 16:30:20",
            "ownerUserId": 1000116941,
            "queueType": "UNIVERSAL_CASE"
        }
    ]
}






### PARTNER_PROFILE_LISTS/CLIENT_PROFILE_LISTS

Partner: Returns the profile lists in the partner environment

Client: Returns the profile lists in the client environment















Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=CLIENT_PROFILE_LISTS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "CLIENT_PROFILE_LISTS": [
        {
            "mongoId": "594f9f5be4b0c94528ff2356",
            "id": 1,
            "clientId": 5547,
            "ownerId": 91646,
            "lastModifiedUserId": 91646,
            "name": "Current Customer",
            "description": "Do Not Edit or Delete",
            "isDeleted": false,
            "createdTime": "2016-09-21 21:45:34.0",
            "modifiedTime": "2016-09-21 21:45:34.0",
            "properties": "{}",
            "createdTimeMillis": 1474494334000,
            "modifiedTimeMillis": 1474494334000
        }
    ]
}







### MACROS

In the UI, macros can be used to execute multiple actions on a message, asset, or profile with a single click, creating workflow efficiencies. This API returns a list of available macros .














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=MACROS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "MACROS": {
        "USER": [
            {
                "id": "59d66f43e4b0e20dad78d8e4",
                "name": "Add to queue",
                "description": "",
                "order": 0,
                "visibleWithinClient": false,
                "assetClass": "MESSAGE",
                "actions": {
                    "CASE_ADD_QUEUE": [
                        "1245"
                    ]
                },
                "idVsCustomPropertyDetails": {},
                "macrosForRelation": {},
                "manualActionData": {
                    "actions": {},
                    "idVsCustomPropertyDetails": {},
                    "mandatoryKeys": []
                },
                "partnerCustomProperties": {},
                "clientCustomProperties": {},
                "profilePartnerCustomProperties": {},
                "profileClientCustomProperties": {},
                "caseCustomProperties": {},
                "clientId": 5547,
                "ownerUserId": 108466,
                "createdTime": 1507225411338,
                "modifiedTime": 1507225411338,
                "lastModifiedUserId": 108466,
                "deleted": false,
                "canEdit": false
            }
        ],
        "SHARED": [
            {
                "id": "59e49c76e4b0c2eeef6f36a7",
                "name": "Close Case ",
                "description": "",
                "order": 0,
                "visibleWithinClient": false,
                "assetClass": "UNIVERSAL_CASE",
                "actions": {
                    "CASE_ADD_QUEUE": [
                        "3",
                        "36",
                        "1625"
                    ],
                    "CASE_REMOVE_QUEUE": [
                        "1"
                    ],
                    "EXECUTE_RULE": [
                        "58a173d3e4b02eb64d7327d3"
                    ]
                },
                "idVsCustomPropertyDetails": {
                    "spr_uc_status": {
                        "actionType": "set",
                        "assetType": "case",
                        "isClientLevel": false,
                        "scopeType": "DEFAULT",
                        "values": [
                            "Closed"
                        ]
                    }
                },
                "macrosForRelation": {},
                "manualActionData": {
                    "actions": {},
                    "idVsCustomPropertyDetails": {},
                    "mandatoryKeys": []
                },
                "partnerCustomProperties": {},
                "clientCustomProperties": {},
                "profilePartnerCustomProperties": {},
                "profileClientCustomProperties": {},
                "caseCustomProperties": {},
                "actionsRequiringConfirmation": [],
                "shareConfigs": [
                    {
                        "shareLevel": "GLOBAL"
                    }
                ],
                "clientId": 5547,
                "ownerUserId": 132559,
                "createdTime": 1508154486037,
                "modifiedTime": 1544703361625,
                "lastModifiedUserId": 108531,
                "deleted": false,
                "canEdit": false
            }
        ]
    }
}







### PERMISSIONS

Permissions regulate user authorization via the UI. This API returns the available permission combinations per platform area.














Copy Code



{
curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=PERMISSIONS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "PERMISSIONS": {
        "AGENT_CONSOLE": [
            "PROCESSING_CASE_CLOCK",
            "PROCESSING_CLOCK",
            "DELETE_COLUMN",
            "EDIT_COLUMN",
            "SHARE",
            "CREATE",
            "CLONE",
            "CREATE_COLUMN",
            "DELETE",
            "CLONE_COLUMN",
            "LOCK",
            "LOCK_COLUMN",
            "VIEW",
            "EXPORT_COLUMN",
            "EDIT"
        ],
        "CASE_MANAGEMENT": [
            "CREATE_CASE",
            "CREATE_OPPORTUNITY",
            "CREATE_LEAD",
            "CREATE_ACCOUNT",
            "CREATE_CONTACT",
            "CREATE_TASK"
        ],
        "OUTBOUND_MESSAGE": [
            "VIEW",
            "CREATE_DRAFT",
            "EDIT_SENT_POST",
            "CREATE_LOCALIZED_COPY",
            "PUBLISH"
        ],
        "MEDIA_ASSET": [
            "SAM_ASSET_RESTRICTION",
            "IMAGE_EDITING_ADJUST",
            "VIEW_DETAILED",
            "SHARE",
            "CREATE",
            "POST",
            "MANAGE_FEATURED_CURATION",
            "COMMENT",
            "MANAGE_NOTIFICATION_CONFIG",
            "DELETE",
            "EXPORT",
            "DOWNLOAD",
            "LOCK",
            "IMAGE_EDITING_OVERLAY_TEXT",
            "USER_SHARING",
            "IMAGE_EDITING_ADD_SHAPE",
            "CREATE_SAM_EXTENSION_REQUEST",
            "IMAGE_EDITING_COLLAGE",
            "VIEW",
            "IMPORT",
            "IMAGE_EDITING_CROP",
            "IMAGE_EDITING_OVERLAY_IMAGE",
            "EDIT",
            "SUGGEST"
        ],
        "CASE": [
            "VIEW",
            "CREATE",
            "EDIT",
            "DELETE"
        ],
        "MONITORING_DASHBOARDS": [
            "PROCESSING_CASE_CLOCK",
            "PROCESSING_CLOCK",
            "DELETE_COLUMN",
            "EDIT_COLUMN",
            "SHARE",
            "CREATE",
            "CLONE",
            "CREATE_COLUMN",
            "DELETE",
            "LOCK",
            "CLONE_COLUMN",
            "USER_SHARING",
            "LOCK_COLUMN",
            "VIEW",
            "EXPORT_COLUMN",
            "VIEW_CASE_RATING",
            "EDIT"
        ]
    }
}







###  USER_GROUPS

Returns the list of user groups.














Copy Code



curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v1/bootstrap/resources?types=USER_GROUPS' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'









{
    "id": "563b9c9ae4b00641a732df73",
    "groupName": "API Project",
    "description": "",
    "assetGroupType": "DEFINED",
    "containedIds": ["114", "115", "113"],
    "assetType": "USER",
    "clientId": 4,
    "deleted": false,
    "ownerUserId": 39
}







	[](https://dev.sprinklr.com/bootstrap-api-v1)




[Back to top](https://dev.sprinklr.com/bootstrap-api-v1)
