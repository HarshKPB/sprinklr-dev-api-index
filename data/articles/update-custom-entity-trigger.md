---
title: "Update Custom Entity Trigger"
slug: update-custom-entity-trigger
url: https://dev.sprinklr.com/update-custom-entity-trigger
---

# Update Custom Entity Trigger

#   PUT Update Custom Entity Trigger
 

Triggers help perform intended actions on the custom entity based on the configured trigger conditions. Using this API, you can update the trigger configuration for a given trigger id.

**Dev Notes: **Kindly note that the feature needs to be enabled in the customer's instance before you can call the custom entity APIs. You can reach out to your success manager for the enablement.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/custom-entity/trigger/{id}

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

### Path Parameters













[create trigger API](https://dev.sprinklr.com/create-custom-entity-trigger)

****



| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Id | Required | The trigger id that was received in the  response Example: 63089557e0d9e1004e767162 | string |

### Request Parameters












****





````

****

****

| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| entityType | Required | Refers to custom entity type, i.e., the custom entity definition IdExample: _c_caller | String |
| type | Required | Refers to the type of trigger, i.e., whether it is script based or rule basedSupported types: SCRIPT, RULEFor SCRIPT: the action will include a scriptFor RULE: the action will include the rule id | String |
| when | Required | Refers to the condition for executing trigger on custom entityExample: CREATE | List[String] |
| action | Required | Refers to the action that is performed when the trigger gets executed | String |
| enabled | Optional | If true, it implies that the trigger is enabled | Boolean |

## Example - Request




 Copy Code



curl -X PUT \
  'https://api3.sprinklr.com/{env}/api/v2/custom-entity/trigger/6308be31e0d9e1004e7696c3' \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
  "entityType": "_c_caller",
   "type": "SCRIPT",
   "when": [
           "UPDATE"
       ],
   "action":"def test 123 consultant_ids = after._c_notification_consultant_id \n        if (consultant_ids == null || consultant_ids.size() == 0) { \n            after._c_notification_trigger_status = \"no users passed\" \n            DB.save(after) \n            return; \n        } \n        List> filters = COLLECTION_UTILS.newList(); \n        filters.add(['federationId': consultant_ids]); \n        def users = DB.find('USER', ['$and': filters], consultant_ids.size(), false, [['key': 'USER_ID', 'order': 'asc']]); \n        if (users == null || users.size() == 0) { \n            after._c_notification_trigger_status = \"no users found\" \n            DB.save(after) \n            return; \n        } \n        //collect user ids and add to custom entity \n        List userIds = COLLECTION_UTILS.newList(); \n        after._c_user_ids = COLLECTION_UTILS.newList(); \n        for (def user : users) { \n            userIds.add(user.id); \n            after._c_user_ids.add(String.valueOf(user.id)) \n        } \n            after._c_notification_trigger_status = \"SUCCESS\" \n        DB.save(after) \n        def notification = ['body': after._c_notification_body, 'title': after._c_notification_title, 'action': after._c_notification_action, 'actionData': after._c_notification_action_data]; \n        PLATFORM.sendMobileNotification(notification, userIds, MAP_UTILS.newMap(), MAP_UTILS.newMap());",
   "enabled": true
}



## Example - Response




  {
    "data": {
        "id": "6308be31e0d9e1004e7696c3",
        "entityType": "_c_caller",
        "type": "SCRIPT",
        "when": [
            "UPDATE"
        ],
        "action": "def  test 123 consultant_ids = after._c_notification_consultant_id \n        if (consultant_ids == null || consultant_ids.size() == 0) { \n            after._c_notification_trigger_status = \"no users passed\" \n            DB.save(after) \n            return; \n        } \n        List> filters = COLLECTION_UTILS.newList(); \n        filters.add(['federationId': consultant_ids]); \n        def users = DB.find('USER', ['$and': filters], consultant_ids.size(), false, [['key': 'USER_ID', 'order': 'asc']]); \n        if (users == null || users.size() == 0) { \n            after._c_notification_trigger_status = \"no users found\" \n            DB.save(after) \n            return; \n        } \n        //collect user ids and add to custom entity \n        List userIds = COLLECTION_UTILS.newList(); \n        after._c_user_ids = COLLECTION_UTILS.newList(); \n        for (def user : users) { \n            userIds.add(user.id); \n            after._c_user_ids.add(String.valueOf(user.id)) \n        } \n            after._c_notification_trigger_status = \"SUCCESS\" \n        DB.save(after) \n        def notification = ['body': after._c_notification_body, 'title': after._c_notification_title, 'action': after._c_notification_action, 'actionData': after._c_notification_action_data]; \n        PLATFORM.sendMobileNotification(notification, userIds, MAP_UTILS.newMap(), MAP_UTILS.newMap());",
        "enabled": true,
        "createdTime": 1661505430268,
        "modifiedTime": 1661505430268
    },
    "errors": []
}



### Response Parameters












****















| Parameters | Description | Type |
| --- | --- | --- |
| id | The reference id for trigger.This is the same id that you sent as a path parameter | String |
| entityType | Refers to custom entity type, i.e., the custom entity definition IdExample: _c_caller | String |
| type | Refers to the type of trigger, i.e., whether it is script based or rule based | String |
| when | Refers to the condition for updating trigger on the custom entityExample: CREATE, UPDATE, SEARCh | List[String] |
| action | Refers to the action that is executed when the trigger gets executed | String |
| enabled | If true, it implies that the trigger is enabled | Boolean |
| createdTime | The time at which the custom entity trigger was updated | Epoch |
| modifiedTime | The time at which the custom entity trigger was last modified | Epoch |


[](https://dev.sprinklr.com/update-custom-entity-trigger) 

 

 
[Back to top](https://dev.sprinklr.com/update-custom-entity-trigger)
