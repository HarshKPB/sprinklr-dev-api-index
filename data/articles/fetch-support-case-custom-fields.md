---
title: "Fetch Support Case Custom Fields"
slug: fetch-support-case-custom-fields
url: https://dev.sprinklr.com/fetch-support-case-custom-fields
---

# Fetch Support Case Custom Fields

#
  GET Fetch Support Case Custom Fields




You can enhance the support case by defining custom fields to elaborate on the issue or your businesses’ use case. Using this API, you can fetch all the available case-related custom fields that can be applied to the support ticket.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/support-ticket/case-custom-fields

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com//api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

## Example - Request















Copy Code



	curl -X GET \
 'https://api3.sprinklr.com/{env}/api/v2/support-ticket/case-custom-fields' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json'






## Example - Response





{
   "entities": [
       {
           "id": "5847e35be4b010d7cf24f303",
           "globalAsset": true,
           "assetClassList": [
               "UNIVERSAL_CASE"
           ],
           "fieldType": "PICKLIST_MULTISELECT",
           "fieldName": "5847e35be4b010d7cf24f302",
           "label": {
               "en": "Waiting for Brand response"
           },
           "options": [
               "yes",
               "No"
           ],
           "optionsOrder": "USER_DEFINED",
           "options2": [
               {
                   "label": "yes",
                   "value": "yes"
               },
               {
                   "label": "No",
                   "value": "No"
               }
           ],
           "dateµcreatedTime": "Dec 7, 2016 10:24:27 AM",
           "dateµmodifiedTime": "Apr 8, 2022 12:04:54 PM",
           "visibilityCriteria": {},
           "assetLevelConfig": [
               {
                   "assetClasses": [
                       "UNIVERSAL_CASE"
                   ],
                   "facetEnabled": false,
                   "required": false,
                   "contentReplacementEnabled": false,
                   "adhocSearchEnabled": false,
                   "autofillControllingFields": false
               }
           ],
           "assetTypeVsOrder": {
               "UNIVERSAL_CASE": 54.0
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
                               "4706"
                           ]
                       }
                   ],
                   "globallyVisible": false
               },
               "spacePermissions": [
                   {
                       "spaceType": "CLIENT",
                       "spaceId": "4706",
                       "permission": {
                           "shareConfigs": [
                               {
                                   "shareLevel": "USER_GROUP",
                                   "sharedWithIds": [
                                       "596f651ae4b0ee0938e8c162"
                                   ],
                                   "permissions": [
                                       "ALL"
                                   ]
                               }
                           ]
                       }
                   }
               ]
           },
           "ownerUserId": 66541,
           "scopeType": "DEFAULT",
           "optionType": "GENERAL",
           "nested": false,
           "minimumInput": 0,
           "mandatoryForClosingTicket": false,
           "report": "CUSTOM_FIELD"
 }
   ],
   "count": 154,
   "hasMore": true
}







[](https://dev.sprinklr.com/fetch-support-case-custom-fields)




[Back to top](https://dev.sprinklr.com/fetch-support-case-custom-fields)
