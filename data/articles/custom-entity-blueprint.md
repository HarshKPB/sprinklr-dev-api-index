---
title: "Custom Entity - Blueprint"
slug: custom-entity-blueprint
url: https://dev.sprinklr.com/custom-entity-blueprint
---

# Custom Entity - Blueprint

#
		 Custom Entity - Blueprint


Custom entities are introduced to store external system data as objects within Sprinklr that contain user-defined objects specific to their use case or business requirements.
Once the entities are defined and stored within Sprinklr, you can read, search, update, and delete data using custom entity APIs. This data can also be visualized on the dashboards and used in reporting.

**Dev Notes: **Custom Entities do not support nested objects or relationships, like parent/child references.

## What are Custom Entities?

Custom entities are custom-made objects that help you store data outside Sprinklr, i.e., in some external system. You can create definitions and fields using custom entities and store data for the user-generated definition.
**`Custom Object (User-defined)`** -> **`Fields (User-defined)`** -> **`Entities (User-defined)`**

## Custom Entities - Key Terminologies

The following are the key terms that you need to be familiar with when working with custom entities,

### 1. Definitions

**Definitions refer to the type of data that you want to store.**
A suitable analogy for custom entity definition is the name of a spreadsheet that defines what type of data it will store.

### 2. Fields

**Fields store the type of information you want to store within the objects.**
A suitable analogy for custom entity fields could be the spreadsheet's column names defining the data type stored in each row.

### 3. Entities

**Entities store the values within the fields.**
A suitable analogy for a custom entity could be the values stored in each row within a spreadsheet.

**Dev Notes: **Contact your success manager for enabling custom entity support in your Sprinklr's instance.

### 1. Custom Entity Definition

The following APIs help create, fetch, and update a custom entity definition.

#### 1.1 Create Custom Entity Definition

You can create a custom entity definition using this API call, i.e., _c_inventory. This would be the table's name defining the data type it will hold.

## Create Custom Entity Definition - Sample Request




  Copy Code



curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/custom-entity/entity \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
  "id" : "_c_inventory",
  "name" : "Inventory Data",
  "pluralName" : "Inventories",
  "description" : "Describes Inventory Data"
}'



**Dev Portal Documentation**: Create Entity Definition

#### 1.2 Fetch Entity Definition

You can fetch the custom entity definition for the given entity Id using this API call.
**Dev Portal Documentation**: Fetch Entity Definition

#### 1.3 Update Entity Definition

Using this API call, you can update an existing custom entity definition.
**Dev Portal Documentation**: Update Entity Definition

### 2. Custom Entity Fields

The following APIs help create, fetch, and delete custom entity fields.

#### 2.1 Create Entity Field

You can create a field for a predefined custom entity definition using this API call. In the example above, we created a custom entity definition for _c_Inventory. Here, we will define the following different fields (table column names):

- UPC

- Product Type

- Supplier Id

**Dev Notes: **

- Currently, we can only define one field per API call.

- Defining data type is essential as it helps configure the field names while configuring reporting dashboards.

## Field 1 - Sample Request




  Copy Code



curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/custom-entity/field \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "_c_inventory__c_UPC",
    "apiName": "_c_upc",
    "name": "Universal Product Code",
    "entityDefinitionId": "_c_inventory",
    "type" : "NUMBER"
}'



## Field 2 - Sample Request




  Copy Code



curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/custom-entity/field \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "_c_inventory__c_productType",
    "apiName": "_c_productType",
    "name": "Product_Type",
    "entityDefinitionId": "_c_inventory",
    "type" : "TEXT"
}'



## Field 3 - Sample Request




  Copy Code



curl -X POST \
  https://api3.sprinklr.com/{env}/api/v2/custom-entity/field \
  -H 'Authorization: {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "_c_inventory__c_supplierId",
    "apiName": "_c_supplierId",
    "name": "Supplier_Id",
    "entityDefinitionId": "_c_inventory",
    "type" : "NUMBER"
}'



**Dev Portal Documentation**:  Create Custom Entity Field

#### 2.2 Fetch All Entity Fields

You can fetch all the fields for the given custom entity definition Id using this API call.
**Dev Portal Documentation**: Fetch Entity Fields

#### 2.3 Delete Custom Entity Field

You can delete a custom entity field using the definition Id and API name using this API call.
**Dev Portal Documentation**: Delete Custom Entity Field

### 3. Custom Entity

The following APis help create, fetch, search, update, delete, and initiate custom entity triggers.

#### 3.1 Create Custom Entity

Using this API, you can store data within the defined custom entity fields (add corresponding data for each defined column).

**Dev Notes: **

- Date is submitted in [epoch millisecond date/time format](https://www.epochconverter.com/)

- Entity Id returned in the response can be used to update/delete custom entity

- You can use the “name” parameter for uniquely identifying a particular row. This adds the advantage of defining a row using a primary key and also searching for custom entities basis on their unique name.

## Sample Request




  Copy Code



curl -L -X POST 'https://api3.sprinklr.com/api/v2/custom-entity/entity' \
-H 'key: API_KEY_HERE' \
-H 'Authorization: Bearer ACCESS_TOKEN_HERE' \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
--data-raw '{
    "type": "_c_inventory",
    "name": “inventory",
    "values": {
        "_c_UPC": 12345,
        "_c_productType": "accessory",
        "_c_supplierId": "3456"
           }
}'





**Dev Portal Documentation**: Create Custom Entity

#### 3.2 Fetch Custom Entity

Using this API, you can fetch the custom entity details for the given entity type and Id.
**Dev Portal Documentation**: Fetch Custom Entity

#### 3.3 Search Custom Entity Using Filters

Using this API, you can fetch custom entity details for the given filter and sorting conditions.
**Dev Portal Documentation**: Search Custom Entity Using Filters

#### 3.4 Partial Update for Custom Entity

Using this API, you can partially update the entity field value for a given custom entity type. In the request payload, you only need to pass the fields that need to be updated.
**Dev Portal Documentation**: Partial Update for Custom Entity

#### 3.5 Update Custom Entity

Using this API, you can update the values for custom entity fields using the entity Id. To make this request work, you’ll have to pass all the fields defined for the custom entity definition.
**Dev Portal Documentation**: Update Custom Entity

#### 3.6 Create/Update Custom Entity

Using this API, you can create or update a custom entity. If the entity details passed in the request payload are not found, the API will create a new entity using the given details. Else, it will update the custom entity.
**Dev Portal Documentation**: Create/Update Custom Entity

#### 3.7 Delete Custom Entity

Using this API, you can delete a custom entity using the unique identifier for the entity type and entity id.
**Dev Portal Documentation**: Delete Custom Entity

### 4. Custom Entity Triggers

#### 4.1  Create Custom Entity Trigger

You can create a trigger configuration for a custom entity using this API. Triggers can be run on create/update/delete of an entity. You can run a custom Groovy script or run a custom entity rule.
**Dev Portal Documentation**: Create Custom Entity Trigger

#### 4.2 Fetch Custom Entity Trigger

Using this API, you can fetch the custom entity trigger details using the unique reference ID.
**Dev Portal Documentation**:Fetch Custom Entity Trigger

#### 4.3 Fetch All Custom Entity Triggers

Using this API, you can fetch all the configured custom entity triggers for the given entity definition and trigger type.
**Dev Portal Documentation**: Fetch All Custom Entity Triggers

#### 4.4 Update Custom Entity Trigger

You can use this API to update the configuration for an existing custom entity trigger.
**Dev Portal Documentation**: Update Custom Entity Trigger

#### 4.5 Enable/Disable Custom Entity Trigger

Using this API, you can enable or disable a custom entity trigger using the unique identifier for the trigger.
**Dev Portal Documentation**: Enable/Disable Custom Entity Trigger

#### 4.6 Delete Custom Entity Trigger

Using this API, you can delete the trigger configuration of a custom entity for the given trigger id.
**Dev Portal Documentation**: Delete Custom entity Trigger

## Custom Entity: FAQs

### What are Some Best Practices for Creating Custom Entity Definitions and Fields?

- When creating definitions and fields, it is recommended to use intuitive names that describe the objective of the definition/field

- Include descriptions that signify the purpose of creating fields and definitions

- Refer to existing standard entity fields before creating new fields to avoid redundancy

- Use prefix _c_  for custom entities when creating definitions and fields

### Is Reporting Available for Custom Entities?

Yes, reporting is available for custom entities. Once the custom entity reporting is enabled, you can choose “Custom Entity” as a data source when plotting a widget. In the dimensions and metrics section, you can choose the custom entity fields defined within the required definition.

Supported Metrics/Dimensions for Custom Entity Field Data Types:

- Dimensions

- Metrics

- TEXT

- NUMBER

- DATE

- DOUBLE

- BOOLEAN

- INTEGER
	[](https://dev.sprinklr.com/custom-entity-blueprint)

[Back to top](https://dev.sprinklr.com/custom-entity-blueprint)
