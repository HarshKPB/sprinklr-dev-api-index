---
title: "Create Topic Group 2.0"
slug: create-topic-group-2-0
url: https://dev.sprinklr.com/create-topic-group-2-0
---

# Create Topic Group 2.0

#
  POST - Create Topic Group


You can create a Listening Topic Group via this API call and you will get the topic group Id and other related objects as response after making the request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/listening-topic-group

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



























































































| Parameters | Sub-Params | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| name |  | Required | Topic Group name. | String |
| description |  | Optional | Topic Group description | String |
| shareConfig |  | Optional | The object containing share configurations which authorise users to view Listening Topics in this Topic Group. |  |
|  | userIds | Optional | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | Optional | List of User Group IDs, which is unique identifier for each User Group. | List<String> |
|  | clientIds | Optional | List of Client IDs, which is unique identifier for Client. | List<Long> |
|  | clientGroupIds | Optional | List of Client Group IDs, which is unique identifier for Client Group. | List<String> |
|  | shareWithEveryOne | Optional | Set it to true, if you want to share it with all users. | Boolean |
| permissionEntity |  | Optional | The object containing permission configuration to authorise users to edit or update Topics in this Topic Group. |  |
|  | userIds | Optional | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | Optional | List of User Group IDs, which is unique identifier for each User Group. | List<String> |

## Example - Request




 Copy Code



curl -X POST \
   https://api3.sprinklr.com/{env}/api/v2/listening-topic-group \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "GroupCreatedViaListeningAPI",
        "shareConfig": {
            "shareWithEveryOne": true
        },
        "permissionEntity": {
            "userIds": [
                600000000
            ],
            "userGroupIds": []
        }
    }'





## Example - Response




{
    "data": {
        "id": "603f952b9edad172a0ce0d97",
        "name": "GroupCreatedViaListeningAPI",
        "permissionEntity": {
            "userIds": [
                600000000
            ]
        }
    },
    "errors": []
}





### Response Parameters



















































































| Parameters | Sub-Params | Description | Type |  |
| --- | --- | --- | --- | --- |
| id |  | Listening Topic Group Id, the unique identifier of the Topic Group. | String |  |
| name |  | Topic Group name. | String |  |
| description |  | Topic Group description |  | String |
| shareConfig |  | The object containing share configurations which authorise users to view Listening Topics in this Topic Group. |  |  |
|  | userIds | List of User IDs, which is unique identifier for each User. | List<Long> |  |
|  | userGroupIds | List of User Group IDs, which is unique identifier for each User Group. | List<String> |  |
|  | clientIds | List of Client IDs, which is unique identifier for Client. | List<Long> |  |
|  | clientGroupIds | List of Client Group IDs, which is unique identifier for Client Group. | List<String> |  |
|  | shareWithEveryOne | Set it to true, if you want to share it with all users. | Boolean |  |
| permissionEntity |  | The object containing permission configuration to authorise users to edit or update Topics in this Topic Group. |  |  |
|  | userIds | List of User IDs, which is unique identifier for each User. | List<Long> |  |
|  | userGroupIds | List of User Group IDs, which is unique identifier for each User Group. | List<String> |  |

[](https://dev.sprinklr.com/create-topic-group-2-0)




[Back to top](https://dev.sprinklr.com/create-topic-group-2-0)
