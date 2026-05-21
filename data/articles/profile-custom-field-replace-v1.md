---
title: "Profile Custom Field Replace v1"
slug: profile-custom-field-replace-v1
url: https://dev.sprinklr.com/profile-custom-field-replace-v1
---

# Profile Custom Field Replace v1

#
  POST - Profile Custom Field Replace

You can replace the values of profile custom properties on profiles via this API call.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/profile/workflow/customProperties

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

### Request Payload



```

```

[app-scoped](https://developers.facebook.com/docs/apps/faq#faq_610616752452545)

```

```

[Bootstrap](https://dev.sprinklr.com/bootstrap-api-v1)

```

```

```

```

```

```

[Bootstrap](https://dev.sprinklr.com/bootstrap-api-v1)

```

```

```

```

```

```

| Field | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| universalProfileKeyList | Required | The JSON array of the Universal Profile Key Use the universalProfileKeyList when you know the social network profile id, but not the Sprinklr profile id Example:  "universalProfileKeyList": [{     "snType": "FACEBOOK",     "snUserId": 215244391952058 }] NOTE: Facebook's profile ids are , so match rates are low for integrated apps. | List |
| ids | Required | An array of profile ids derived from Sprinklr Use the id when you know the Sprinklr profile id Example: "ids": [     "5152879be4b0f59a42d8c7ea",      "5152879be4b0f59a42d8c7eb" ] | List < String > |
| clientCustomProperties | Optional | An array of client (workspace level) custom properties in a JSON structure 						You can find the existing client custom properties with the  endpoint using types=PROFILE_CUSTOM_FIELDS. Client custom properties are denoted as "globalAsset": false. 						Key: 						 "fieldName": "_c_660a79a8acbec103d7541075" 						  						Value: 						"options2": [                                                       {                                                         "label": "Test1",                                                        "value": "Test2"                                                       },                                                       {                                                        "label": "Test3",                                                        "value": "Test4"                                                       }, 						  						Example: 						"clientCustomProperties": { 	"_c_660a79a8acbec103d7541075": ["Test2"] } 						This would replace the label on that custom field, i.e, the custom field will reflect Test1 on the profile | Map < String, List < String > > |
| partnerCustomProperties | Optional | An array of partner custom properties (global/customer level) in a JSON structure 						You can find the existing partner custom properties with the  endpoint using types=PROFILE_CUSTOM_FIELDS. Client custom properties are denoted as "globalAsset": true. 						Key: 						 "fieldName": "_c_660a79a8acbec103d7541075" 						  						Value: 						"options2": [                                                       {                                                         "label": "Test1",                                                        "value": "Test2"                                                       },                                                       {                                                        "label": "Test3",                                                        "value": "Test4"                                                       }, 						  						Example: 						"partnerCustomProperties": { 	"_c_660a79a8acbec103d7541075": ["Test4"] } 						This would replace the label on that custom field, i.e, the custom field will reflect Test3 on the profile | Map < String, List < String > > |

**Dev Notes: **

- You must configure the profile custom properties in Sprinklr in order to use them in this API call.
- The system will ignore invalid names and values.
- Profile Properties Insert is only available for TEXT_MULTI and PICKLIST_MULTISELECT profile custom properties.
-  You can discover the type of the profile custom property through the [Bootstrap](https://dev.sprinklr.com/bootstrap-api-v1) endpoint, and searching for "fieldType": "TEXT_MULTI" or "fieldType": "PICKLIST_MULTISELECT"

### Example - Request




 Copy Code


curl -X POST \
 'https://api3.sprinklr.com/{env}/api/v1/profile/workflow/customProperties' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '
{
"partnerCustomProperties": {
	"_c_660a79a8acbec103d7541075": ["Test4"]
    },
    "ids": "56f76964e4b0561cc540ba0f"
}'



## Example - Response




true





[](https://dev.sprinklr.com/profile-custom-field-replace-v1)




[Back to top](https://dev.sprinklr.com/profile-custom-field-replace-v1)
