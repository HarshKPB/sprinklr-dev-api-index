---
title: "Oct - Dec, 2022"
slug: oct-dec-2022
url: https://dev.sprinklr.com/oct-dec-2022
---

# Oct - Dec, 2022

# Oct - Dec, 2022

**Developer Note:** We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.	Please note that the API base endpoint has changed from `api2` to `api3`.

For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## ****BETA! Fetch Schema -  Nov 16th, 2022

Using this API, you can fetch the list of all the case-related fields whose values and properties you can extract using bulk data interface (BDI) API endpoints.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/bdi/manage/apis/schema

## ****BETA! Create/Update Endpoint -  Nov 16th, 2022

Using this API, you can create/update a template for an endpoint that defines all the selected case-related fields you want to track.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/bdi/manage/apis/endpoints/{endpointName}

## ****BETA! Fetch Endpoints -  Nov 16th, 2022

Using this API, you can fetch the list of all the endpoints with their respective templates created by you using the create/update endpoint API request.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/bdi/manage/apis/endpoints

## ****BETA! Delete Endpoint -  Nov 16th, 2022

Using this API, you can delete an existing endpoint.

**API Endpoint**

DELETE https://api2.sprinklr.com/{env}/api/v2/bdi/manage/apis/endpoints/{endpointName}

## ****BETA! Search Case -  Nov 16th, 2022

Using this API, you can search for cases using filters. You will be able to fetch the fields that are present in the template for the given endpoint name.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/bdi/apis/{endpointName}

## ****BETA! Search Case by Cursor -  Nov 16th, 2022

Using this API, you can search the next set of results using the cursor id you received in the search case API response.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/bdi/apis/{endpointName}

## ****Media Asset Security -  Nov 10th, 2022

This API call helps generate a private-access URL for five minutes to facilitate asset download. This ensures that the asset can be downloaded from within Sprinklr without making it publically accessible.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v1/secure-assets/fetch/{url}

## ****Fetch Standard Entity Definition -  Nov  9th, 2022

With this API, you can fetch the pre-defined standard entity definition details using the unique definition Id.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/standard-entity/definition/{entityDefinitionId}

## ****Create Standard Entity Field -  Nov  9th, 2022

Using this API, you can create a standard entity field for the given entity definition Id.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/standard-entity/field/{entityDefinitionId}

## ****Fetch Standard Entity Fields -  Nov  9th, 2022

Using this API, you can fetch all the standard entity fields created for the given definition Id.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/standard-entity/fields/{entityDefinitionId}

## ****Fetch Standard Entity Field Using apiName -  Nov  9th, 2022

Using this API, you can fetch the configured details for the standard entity field using the unique apiName.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/standard-entity/field/{entityDefinitionId}/{apiName}

## ****Update Standard Entity Field -  Nov  9th, 2022

Using this API, you can update the details for the standard entity field.

**API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/standard-entity/field/{entitydefinitionId}/{apiName}

## ****Create Standard Entity -  Nov  9th, 2022

Using this API, you can create a standard entity field, i.e., you can store values within the defined standard entity fields.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/standard-entity/entity/{entityDefinitionId}

## ****Fetch Standard Entity Using Entity Id -  Nov  9th, 2022

Using this API, you can fetch the standard entity details using the entity Id.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/standard-entity/entity/{entityDefinitionId}/{entityId}

## ****Update Standard Entity Using Entity Id -  Nov  9th, 2022

Using this API, you can update the details for the standard entity field.

**API Endpoint**

PUT https://api2.sprinklr.com/{env}/api/v2/standard-entity/entity/{entitydefinitionId}/{entityId}

## ****Fetch Standard Entity Using Primary Key Prefix-  Nov  9th, 2022

Using this API, you can fetch the standard entity using at least one of the primary key parameters, i.e., identityType, identityId, and channel.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/standard-entity/entity/byPrimaryKeyPrefix/{entityDefinitionId}

## ****Fetch Standard Entity Using Primary Key -  Nov  9th, 2022

Using this API, you can fetch the standard entity using all of the primary key parameters, i.e., identityType, identityId, and channel.

**API Endpoint**

GET https://api2.sprinklr.com/{env}/api/v2/standard-entity/entity/byPrimaryKey/{entityDefinitionId}

## ****Delete Standard Entity -  Nov  9th, 2022

Using this API, you can fetch the standard entity using all of the primary key parameters, i.e., identityType, identityId, and channel.

**API Endpoint**

DELETE https://api2.sprinklr.com/{env}/api/v2/standard-entity/entity/{entityDefinitionId}/{entityId}

## ****Update Standard Entity (Partial) -  Nov  9th, 2022

Using this API call, you can partially update standard entity field value for a given entity definition Id and and entity Id. In the request payload, you only need to pass the fields that need to be updated.

**API Endpoint**

PATCH https://api2.sprinklr.com/{env}/api/v2/standard-entity/entity/{entitydefinitionId}/{entityId}

## ****Create/Update Standard Entity -  Nov  9th, 2022

This API helps create/update a standard entity using entity Id. If the entity details passed in the request payload are not found, the API will create a new standard entity using the given details. Else, it will update the standard entity.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/standard-entity/entity/upsert/{entityDefinitionId}/{entityId}

## ****Create/Update Standard Entity Using Primary Key -  Nov  9th, 2022

This API helps create/update a standard entity using primary key. If the entity details passed in the request payload are not found, the API will create a new standard entity using the given details. Else, it will update the standard entity.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/standard-entity/entity/upsertByPrimaryKey/{entityDefinitionId}

## ****Sprinklr Community -  Nov  9th, 2022

Using the community APIs, you can fetch data and perform various actions on the community forum. One important thing to note here is that these APIs do not follow the standard OAuth 2.0 process for authorization. To access Community APIs, contact your success manager to setup projectId and requestToken.

**Community API Details**

Refer to [Community APIs](https://dev.sprinklr.com/community-apis).


[](https://dev.sprinklr.com/oct-dec-2022)

[Back to top](https://dev.sprinklr.com/oct-dec-2022)
