---
title: "Update Theme 2.0"
slug: update-theme-2-0
url: https://dev.sprinklr.com/update-theme-2-0
---

# Update Theme 2.0

#
  PUT - Update Theme

You can use this API endpoint to update Listening Theme and as response you will get the updated Listening Theme object after making the request.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v2/listening-theme/{Id}

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/getting-started)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameters



















| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| Id | Required | The unique Id of the Listening Theme. | String |

### Request Parameters











































































































































| Parameters | Sub-Params | Reuired/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| id |  | Required | The unique identifier of the Listening Theme. | String |
| name |  | Required | The Listening Theme name. | String |
| displayName |  | Optional | The Listening Theme display name. | String |
| iconUrl |  | Optional | The Listening Theme icon url. | String |
| imageUrl |  | Optional | The Listening Theme image url. | String |
| color |  | Optional | The Listening Theme identification colour. | String |
| description |  | Optional | The Listening Theme description. | String |
| filters |  | Required | The Filter list to filter out required data. | List<String> |
| tags |  | Optional | The Tags to group Listening Theme based on use case. | List<String> |
| shareConfig |  | Optional | The object containing share configurations which authorise users to view Listening Theme. |  |
|  | userIds | Optional | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | Optional | List of User Group IDs, which is unique identifier for each User Group. | List<String> |
|  | clientIds | Optional | List of Client IDs, which is unique identifier for Client. | List<Long> |
|  | clientGroupIds | Optional | List of Client Group IDs, which is unique identifier for Client Group. | List<String> |
|  | shareWithEveryOne | Optional | Set it to true, if you want to share it with all users. | Boolean |
| permissionEntity |  | Optional | The object containing permission configuration to authorise users to edit and Listening Themes. |  |
|  | userIds | Optional | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | Optional | List of User Group IDs, which is unique identifier for each User Group. | List<String> |

## Example - Request




Copy Code


curl -X PUT \
   'https://api3.sprinklr.com/{env}/api/v2/listening-theme/60486cef06ebe67ed55c4140' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "60486cef06ebe67ed55c4140",
    "name": "ListeningThemeAPITest",
    "displayName": "sampleCreateThemeDisplayName1",
    "color": "#FFFFF",
    "filters": [
    {
      "filterType": "IN",
      "field": "QUERY",
      "values": [
        {
          "advanceQuery": "keyword_list_or(\"5f601c2728cf4e53142af770\")",
          "textQuery": "keyword_list_or(\"5f601c2728cf4e53142af770\")"
        }
      ]
      }
  ],
    "description": "sampleCreateThemeUpdate",
    "tags": [],
    "shareConfig": {
            "shareWithEveryOne": true
    },
    "permissionEntity": {
        "userIds": [
            600000000
        ]
    }
}'





## Example - Response




{
    "data": {
        "id": "60486cef06ebe67ed55c4140",
        "name": "ListeningThemeAPITest",
        "displayName": "sampleCreateThemeDisplayName1",
        "color": "#FFFFF",
        "filters": [
            {
                "filterType": "IN",
                "field": "QUERY",
                "values": [
                    {
                        "advanceQuery": "keyword_list_or(\"5f601c2728cf4e53142af770\")",
                        "textQuery": "keyword_list_or(\"5f601c2728cf4e53142af770\")"
                    }
                ],
                "userFilter": false,
                "allValuesAllowed": true,
                "favourite": false,
                "mandatory": false,
                "locked": false,
                "details": {}
            }
        ],
        "description": "sampleCreateThemeUpdate",
        "permissionEntity": {
            "userIds": [
                600000000
            ]
        }
    },
    "errors": []
}





### Response Parameters























































































































| Parameters | Sub-Params | Description | Type |
| --- | --- | --- | --- |
| id |  | The unique identifier of the Listening Theme. | String |
| name |  | The Listening Theme name. | String |
| displayName |  | The Listening Theme display name. | String |
| iconUrl |  | The Listening Theme icon url. | String |
| imageUrl |  | The Listening Theme image url. | String |
| color |  | The Listening Theme identification colour. | String |
| description |  | The Listening Theme description. | String |
| filters |  | The Filter list to filter out required data. | List<String> |
| tags |  | The Tags to group Listening Theme based on use case. | List<String> |
| shareConfig |  | The object containing share configurations which authorise users to view Listening Theme. |  |
|  | userIds | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | List of User Group IDs, which is unique identifier for each User Group. | List<String> |
|  | clientIds | List of Client IDs, which is unique identifier for Client. | List<Long> |
|  | clientGroupIds | List of Client Group IDs, which is unique identifier for Client Group. | List<String> |
|  | shareWithEveryOne | Set it to true, if you want to share it with all users. | Boolean |
| permissionEntity |  | The object containing permission configuration to authorise users to edit and Listening Themes. |  |
|  | userIds | List of User IDs, which is unique identifier for each User. | List<Long> |
|  | userGroupIds | List of User Group IDs, which is unique identifier for each User Group. | List<String> |

[](https://dev.sprinklr.com/update-theme-2-0)




[Back to top](https://dev.sprinklr.com/update-theme-2-0)
