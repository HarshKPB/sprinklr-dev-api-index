---
title: "Digital Asset Management - Blueprint"
slug: digital-asset-management-blueprint
url: https://dev.sprinklr.com/digital-asset-management-blueprint
---

# Digital Asset Management - Blueprint

#
		 Digital Asset Management - Blueprint


Sprinklr’s Digital Asset Manager provides an organized and unified repository for storing, managing, and measuring your content assets' impact. [Sprinklr's governance](https://www.sprinklr.com/help/articles/manage-assets/permission-control-on-assets/64258122c7dea832a77cea85) allows setting content permissions and expiry dates to maintain the assets consistently.

Using Sprinklr Asset Manager APIs, you can upload, import, create, read, update, and delete assets to and from Sprinklr.

## Asset Synchronization - Use Cases

- Maintain a unified repository of digital assets within Sprinklr

- Reporting on assets for tracking asset engagement levels

- Publish DAM assets directly to social and messaging channels

## Things to Know in Advance

- Register on the [Sprinklr Developer Portal](https://dev.sprinklr.com/developer-portal-registration) to create a developer portal account

- Create a New App for [generating the API key](https://dev.sprinklr.com/getting-started)

- Refer to [authorize](https://dev.sprinklr.com/authorize) section for steps for generating the authorization token

- Once the key and authorization token are generated, make an API call using the “ME” endpoint. This helps validate that the key and token work as expected

- Make Asset API calls based on your use case. You can find the workflow and API documentation links below

## Sprinklr Asset Manager APIs: Workflow

1. Import Asset

1.1 Asset Import API

1.2 Asset Import Async API

1.2.1 Check Status API

2. Upload Asset

2.1 Media Upload API

2.2 Media Upload in Bulk API

3. Create Asset

3.1 Create Asset API

4. Asset Read/Search

4.1 Read Asset API

4.2 Search Asset API

5. Update Asset

5.1 Asset Update API

6. Delete Asset

6.1 Delete Asset API

7. Media Asset Security

7.1 Media Asset Security API

## 1. Import Asset

Asset import APIs help import an asset to Sprinklr from an external link.

### 1.1 Asset Import API

Using this API, you can import an asset to Sprinklr through an external link.

**Dev Notes: **Importing an asset does not mean that it is added to the Digital Asset Management store. Once the asset is uploaded successfully, you’ll have to call the asset create API to add it to DAM (Digital Asset Management) store.

**Developer Portal Documentation**: Asset Import API

### 1.2 Asset Import Async API

Using this API, you can import an asset to Sprinklr through an external link. The add-on advantage of asset import async API is that there are no size limitations when importing assets.

**Dev Notes: **

- There is no size limitation when using asset import async API

- The processing time for importing the asset depends on its size

- It is recommended to check the status of the import periodically

- The asset import API will continue running until the import is successful
**Developer Portal Documentation**: Asset Import Async

### 1.2.1 Check Status API

Using this API, you can check the upload status of asset import using the task Id received in the asset import async API response.
**Developer Portal Documentation**: Check Import Status

## 2. Upload Asset

Asset upload APIs help upload an asset to Sprinklr and generate a publicly accessible URL.

### 2.1 Media Upload API

You can upload an asset to Sprinklr from your local environment using this API.

**Dev Notes: **You can upload the following asset types: `FILE`, `IMAGE`, `VIDEO`

**Dev Portal Documentation**: Media Upload API

### 2.2 Media Upload in Bulk API

You can upload media assets in bulk using a single API call using this API.

**Dev Notes: **Supported asset types include: `FILE`, `IMAGE`, `VIDEO`

**Dev Portal Documentation**: Media Upload in Bulk

## 3. Create Asset

Using this API, you can create an asset in the Digital Asset Management store within Sprinklr.

### 3.1 Create Asset API

Using this API, you can create assets in DAM.

**Dev Notes: **

- Before creating a Digital Asset, you must upload or import the asset into the content store.

- Before creating a Link Asset, you must import the asset into the content store.

- You do not need to upload or import a Text Asset before creating it.

**Supported Asset Types: **
**Asset Create v1**: PHOTO, VIDEO, AUDIO, PRESENTATION, HTML, PDF, DOC, DOCX, EXCEL, ZIP, PSD, SKETCH, FONT, BENEFIT, SWOOSH_BENEFIT, LINK, TEXT, RTFD, RICH_TEXT, POST, CARD_ASSET, FEEDBACK, POLL, FORM, SURVEY, TEMPLATE_ASSET, REVIEW, CANVAS, DYNAMIC_IMAGE_TEMPLATE

**Asset Create v2**: PRESENTATION, PHOTO, VIDEO, AUDIO, FLASH, HTML, PDF, DOC, DOCX, EXCEL, ZIP, PSD, SKETCH, FONT

**Dev Portal Documentations**:

Create Asset API - v1

Create Asset API - v2

## 4. Asset Read/Search

Using these APIs, you can fetch details for the existing asset within Sprinklr.

### 4.1 Read Asset API

Using this API, you can fetch the details of an existing asset for the given asset Id. You can fetch the asset Id from the create asset API response or directly from the UI.

**How to Find Asset Id from the UI?**

- Navigate to “Assets” within the Digital Asset Management module

- Search for the asset you want the asset details for

- Hover over the three dots on the asset icon

- Click on details, and the asset Id should be visible in the overview section (see attached image)

**Dev Portal Documentation**: Read Asset API

### 4.2 Search Asset API

Using this API, you can search for an asset using sorting and filter conditions. You can also search assets based on keywords passed in the search API request.
**Dev Portal Documentation**: Search Asset API

## 5. Update Asset

Using the update API, an existing asset can be updated.

### 5.1 Asset Update API

Using this API, you can update the details of an existing asset within Sprinklr’s Digital Asset Management (DAM) store.
**Dev Portal Documentation**: Asset Update API

## 6. Delete Asset

Using the delete API, you can permanently delete an existing asset from Sprinklr.

### 6.1 Delete Asset API

Using this API, you can delete an asset from Sprinklr using the unique asset Id.

**Dev Notes: **204 No Content in the response implies that the asset is deleted successfully.

**Dev Portal Documentation**: Delete Asset API

## 7. Media Asset Security

Media asset security ensures that the uploaded media content is not publicly accessible. To enable this feature within Sprinklr, you can contact your success manager.
If you want to access restricted media content, media asset security API comes in handy.

### 7.1 Media Asset Security API

Using this API, you can download the restricted media content from Sprinklr. You receive a publicly accessible URL in response, accessible for a pre-configured time.

**Dev Notes: **The default expiry time for the publicly accessible URL is 90 minutes. However, the expiry time can be configured based on one's requirements.

**Dev Portal Documentation**: Media Asset Security API

## Sprinklr Asset Manager: FAQs

### 1. Is Reporting Available on Digital Assets?

Yes, reporting is available on DAM. You can select the data source as “DAM” in the reporting.

Once the widget is configured, you can use [reporting API](https://dev.sprinklr.com/reporting-blueprints) to export the asset details from within Sprinklr.
[](https://dev.sprinklr.com/digital-asset-management-blueprint)

[Back to top](https://dev.sprinklr.com/digital-asset-management-blueprint)
