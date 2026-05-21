---
title: "Partially Update Universal Profile"
slug: partially-update-universal-profile
url: https://dev.sprinklr.com/partially-update-universal-profile
---

# Partially Update Universal Profile

#
  POST Partially Update Universal Profile



Using this API, you can partially update Universal Profile fields. You can update standard fields of a user’s universal profile, such as name, email, phone number, and custom attributes like country, without modifying other profile details.

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/profile/partial-update

### Headers

HTTP headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``




			```




			``


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












    [Create Universal Profile API](https://dev.sprinklr.com/create-update-universal-profile)




****````











































































    **````**
-
```

```

-
```

```

























| Parameters | Sub-Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| id |  | Required | Id of the profile you want to update. This is the profile id you receive in the  response. | String |
| profileKey |  | Optional | Contains the channel type and channel ID of the profile you want to update. Note:You must either pass id or profileKey to the API. | Object |
|  | channelType | Required | Refers to the social channel associated with the customer's profile | String |
|  | channelId | Required | Unique identifier of the profile on channel. | String |
| profileUpdateRequestDTO |  | Optional | Object containing the contact details to be updated. | Object |
|  | contactInfo | Optional | Object containing the contact details to be updated. | Object |
|  | contactInfo.firstName | Optional | First name of the user. | String |
|  | contactInfo.maidenName | Optional | Maiden name of the user. | String |
|  | contactInfo.lastName | Optional | Last name of the user. | String |
|  | contactInfo.fullName | Optional | Full name of the user. | String |
|  | contactInfo.website | Optional | List of websites. | Array |
|  | contactInfo.phoneNo | Optional | Phone number of the user. | String |
|  | contactInfo.emailDetails | Optional | Email details of the user. | Array |
| profileWorkflowUpdateRequestDTO |  | Optional |  | Object |
|  | partnerCustomProperties | Optional | Refers to the profile custom properties. You can use this to set or unset custom properties when updating the user. Please note that using this property will remove all the preset custom fields. partnerCustomProperties can't be used with partnerCustomPropertiesAdded, partnerCustomPropertiesRemoved, selectivePartnerCustomProperties   			        Syntax for Setting Custom Property:     {   "_c_5f635d84ddef993f24577401": [     "Test"   ] }           Syntax for Unsetting Custom Property:     {   "_c_5f635d84ddef993f24577401": [     ""   ] } | Object |
|  | partnerCustomPropertiesAdded | Optional | Use this to add new values to existing properties. | Object |
|  | partnerCustomPropertiesRemoved | Optional | Use this to remove specific values from existing properties. | Object |
|  | selectivePartnerCustomProperties | Optional | Use this to update specific properties. | Object |

## Examples

### Example 1 - Request


The following example demonstrates how to use `partnerCustomProperties` to unset the value of a custom property:















Copy Code



curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/profile/partial-update' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "id": "67482a8a2dda2643b2df4b9b",
    "profileUpdateRequestDTO": {
        "contactInfo": {
            "phoneNo": "99909880891"
        }
    },
    "profileWorkflowUpdateRequestDTO": {
        "partnerCustomProperties": {
            "_c_64dcb892e32de6530b5a8dbf": [""]
        }
    }
}'






### Example 1 - Response





{
    "data": "67482a8a2dda2643b2df4b9b",
    "errors": []
}






### Example 2 - Request


The following example demonstrates how to use `partnerCustomPropertiesAdded`:















Copy Code



curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/profile/partial-update' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "id": "67482a8a2dda2643b2df4b9b",
    "profileUpdateRequestDTO": {
        "contactInfo": {
            "phoneNo": "99909880891"
        }
    },
    "profileWorkflowUpdateRequestDTO": {
        "partnerCustomPropertiesAdded": {
            "_c_64dcb892e32de6530b5a8dbf": ["US", "UK"]
        }
    }
}'






### Example 2 - Response





{
    "data": "67482a8a2dda2643b2df4b9b",
    "errors": []
}







### Example 3 - Request


The following example demonstrates how to use `partnerCustomPropertiesRemoved`:















Copy Code



curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/profile/partial-update' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "id": "67482a8a2dda2643b2df4b9b",
    "profileUpdateRequestDTO": {
        "contactInfo": {
            "phoneNo": "99909880891"
        }
    },
    "profileWorkflowUpdateRequestDTO": {
        "partnerCustomPropertiesRemoved": {
            "_c_64dcb892e32de6530b5a8dbf": ["UK"]
        }
    }
}'






### Example 3 - Response





{
    "data": "67482a8a2dda2643b2df4b9b",
    "errors": []
}







### Example 4 - Request


The following example demonstrates how to use `selectivePartnerCustomProperties`:















Copy Code



curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/profile/partial-update' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
  "id": "6527a3477e759fa63734c9fe",
    "profileUpdateRequestDTO": {
        "contactInfo": {
            "firstName": "Deepak",
            "fullName": "Deepak Dev v1",
            "lastName": "Dev v1",
            "emailDetails": "bdeepakdevtest@gmail.com",
            "phoneNo": "9990988023"
        }
    },
    "profileWorkflowUpdateRequestDTO": {
        "selectivePartnerCustomProperties": {
            "spr_community_user_country": [
                "US"
            ]
        }
    }
}'






### Example 4 - Response





{
    "data": "6527a3477e759fa63734c9fe",
    "errors": []
}







### Example 5 - Request


The following example demonstrates how to use `profileKey` instead of `id`:















Copy Code



curl --location --request POST 'https://api3.sprinklr.com/{env}/api/v2/profile/partial-update' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--header 'Key: {Enter your API KEY}' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "profileKey": {
        "channelType": "EMAIL",
        "channelId": "inquiry1592@gmail.com"
    },
    "profileUpdateRequestDTO": {
        "contactInfo": {
            "firstName": "Test",
            "fullName": "Test Gmail v1",
            "lastName": "Gmail v1",
            "emailDetails": "inquiry1592@gmail.com",
            "phoneNo": "9990988089"
        }
    },
    "profileWorkflowUpdateRequestDTO": {
        "partnerCustomPropertiesAdded": {
            "_c_646b3c15c4b6a04acbecb70e": [
                "Profile"
            ]
        }
    }
}'






### Example 5 - Response





{
    "data": "650c2acd53edd220318c76f5",
    "errors": []
}






### Response Parameters














[Read Profile API](https://dev.sprinklr.com/fetch-profile-by-profile-id)










| Parameter | Description | Type |
| --- | --- | --- |
| data | Refers to the unique identifier for the customer's profileYou can further use this Id in  to fetch the profile details | String |
| errors | List of errors (if any). | Array |


[](https://dev.sprinklr.com/partially-update-universal-profile)






[Back to top](https://dev.sprinklr.com/partially-update-universal-profile)
