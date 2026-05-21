---
title: "Fetch Product Catalogs"
slug: fetch-product-catalogs
url: https://dev.sprinklr.com/fetch-product-catalogs
---

# Fetch Product Catalogs

#   GET Fetch Product Catalogs
 

This API allows you to retrieve product catalogs associated with a specific ad account. A catalog is a container that holds information about the items that you want to advertise or sell.


**Related Knowledge Base Article: **[Create and Manage Facebook Product Catalogs](https://www.sprinklr.com/help/articles/advanced-use-cases/create-and-manage-facebook-product-catalogs/685ac9b420753412ba3db8e9)


## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/paid/resource/productCatalogForAdAccount

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


### Query Parameters














[Steps to Retrieve Account User Id](https://dev.sprinklr.com/fetch-product-catalogs#account_userid)


















| Parameter | Required/Optional | Description |
| --- | --- | --- |
| accountUserId | Required | Id of the ad account userSee |
| start | Optional | Starting index for pagination |
| limit | Optional | Number of results to return per page |
| keyword | Optional | Filter catalogs by name containing this string |

### Steps to Retrieve Account User Id



- In Sprinklr, click the **New Page** (**+**) icon to open the Launchpad.

- Navigate to the **Sprinklr Social** tab, then go to **Listen > Owned Social Accounts**.

- On the **Accounts** page, use the **Channels** dropdown in the top-left corner to select the desired channel type.

- In the resulting list, locate the ad account for which you want the ID. The value in the **User ID** column corresponds to the `accountUserId` parameter.

## Example - Request




 Copy Code


curl --location --request GET 'https://api3.sprinklr.com/{env}/api/v2/paid/resource/productCatalogForAdAccount?accountUserId=394232028806869&start=0&limit=2&keyword=v' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--header 'Key: {Enter Your API Key}'



## Example - Response





{
    "data": {
        "responseEntities": [
            {
                "productCatalog": {
                    "channelId": "1009576837563505",
                    "businessId": 66000998,
                    "vertical": "COMMERCE",
                    "channelType": "FACEBOOK",
                    "feedCount": 1,
                    "productCount": 513,
                    "associatedEventIds": [],
                    "associatedEvents": [],
                    "associatedUsers": [
                        {
                            "name": "Avik Dutta",
                            "id": "122118459038425105",
                            "role": "ADMIN"
                        },
                        {
                            "name": "Aditya Tripathi",
                            "id": "122117404556449412",
                            "role": "ADMIN"
                        },
                        {
                            "name": "r t",
                            "id": "122096139728369526",
                            "role": "ADMIN"
                        },
                        {
                            "name": "Alok Kumar",
                            "id": "122104831088229444",
                            "role": "ADMIN"
                        }
                    ],
                    "imageSettings": {
                        "carouselSettings": {
                            "transformationType": "NONE"
                        },
                        "singleAdSettings": {
                            "transformationType": "NONE"
                        }
                    },
                    "name": "validation test",
                    "clientId": 66000002,
                    "userId": 66004912,
                    "ownerUserId": 66004912,
                    "assetClass": "PAID_PRODUCT_CATALOG",
                    "isDeleted": false,
                    "visibilityId": "66c4541b56b0755079bba503",
                    "assetPermissionId": "66c4541b56b0755079bba542",
                    "createdTime": 1754566416230,
                    "modifiedTime": 1754566416230,
                    "id": "FACEBOOK_2191390907694449_1009576837563505"
                }
            },
            {
                "productCatalog": {
                    "channelId": "1414773226064270",
                    "businessId": 66000998,
                    "vertical": "HOTELS",
                    "channelType": "FACEBOOK",
                    "feedCount": 1,
                    "productCount": 0,
                    "associatedEventIds": [],
                    "associatedEvents": [],
                    "associatedUsers": [
                        {
                            "name": "Aman ad",
                            "id": "122100780542180800",
                            "role": "ADMIN"
                        },
                        {
                            "name": "Sourabh rohilla",
                            "id": "122107800710003213",
                            "role": "ADMIN"
                        },
                        {
                            "name": "Alok Kumar",
                            "id": "122104831088229444",
                            "role": "ADMIN"
                        }
                    ],
                    "imageSettings": {
                        "carouselSettings": {
                            "transformationType": "NONE"
                        },
                        "singleAdSettings": {
                            "transformationType": "NONE"
                        }
                    },
                    "name": "Abhinav Test",
                    "clientId": 66000002,
                    "userId": 66000009,
                    "ownerUserId": 66000009,
                    "assetClass": "PAID_PRODUCT_CATALOG",
                    "isDeleted": false,
                    "visibilityId": "65c27f08600f86e55adfc9af",
                    "assetPermissionId": "65c27f08600f86e55adfc9ea",
                    "createdTime": 1754566416212,
                    "modifiedTime": 1754566416212,
                    "id": "FACEBOOK_2191390907694449_1414773226064270"
                }
            }
        ]
    },
    "errors": []
}




### Response Parameters































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| data |  | Object containing the response data. |  |
|  | responseEntities | Object containing product catalog objects.See the Product Catalog table below. | Object |
| errors |  | Array containing error details, if any. | Array |


### Product Catalog Object




















































































































































































| Parameter | Sub-Parameter | Description | Type |
| --- | --- | --- | --- |
| channelId |  | Id of the channel | String |
| businessId |  | Id of the business | Number |
| vertical |  | Business vertical (for example, COMMERCE, HOTELS) | String |
| channelType |  | Advertising channel type (for example, FACEBOOK) | String |
| feedCount |  | Number of feeds associated with the catalog | Number |
| productCount |  | Total number of products in the catalog | Number |
| associatedEventIds |  | List of associated event Ids | Array |
| associatedEvents |  | List of associated event objects | Array |
| associatedUsers |  | List of users linked to the catalog | Array |
|  | name | Name of the user | String |
|  | id | Id of the user | String |
|  | role | Role of the user (for example, ADMIN) | String |
| imageSettings |  | Image transformation settings | Object |
| carouselSettings |  | Settings for carousel ads | Object |
|  | transformationType | Transformation type (for example, NONE) | String |
| singleAdSettings |  | Settings for single-image ads | Object |
|  | transformationType | Transformation type (for example, NONE) | String |
| name |  | Name of the product catalog | String |
| clientId |  | Id of the client owning the catalog | Number |
| userId |  | User Id who created the catalog | Number |
| ownerUserId |  | Owner user Id of the catalog | Number |
| assetClass |  | Asset type (for example, PAID_PRODUCT_CATALOG) | String |
| isDeleted |  | Indicates whether the catalog is marked as deleted | Boolean |
| visibilityId |  | Id representing visibility permissions | String |
| assetPermissionId |  | Id representing asset-level permissions | String |
| createdTime |  | Timestamp when the catalog was created | Epoch |
| modifiedTime |  | Timestamp of the last modification | Epoch |
| id |  | Id of the catalog | String |

[](https://dev.sprinklr.com/fetch-product-catalogs) 

 

 
[Back to top](https://dev.sprinklr.com/fetch-product-catalogs)
