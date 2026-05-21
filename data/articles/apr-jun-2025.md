---
title: "Apr-Jun, 2025"
slug: apr-jun-2025
url: https://dev.sprinklr.com/apr-jun-2025
---

# Apr-Jun, 2025

# Apr - Jun, 2025

## Create/Update Universal Profile API Enhancement

A new optional query parameter `syncPartnerProfileListIfNotSet` has been added to the [Create/Update Universal Profile API](https://dev.sprinklr.com/create-update-universal-profile). This parameter accepts a Boolean value and defaults to `false`. It controls how the system handles the `profileList` field during  a profile update when the `profileList` is not included in the payload. When set to `false`, the system does not attempt to synchronize or overwrite the existing `profileList`. This prevents unintended changes to the `profileList` when it is not explicitly provided in the request.

## Introducing Import Survey Response API

	This API enables API-based response ingestion, allowing clients to push survey responses from any external source into Sprinklr CFM.

### Endpoint Details:



- [Import Survey Response API](https://dev.sprinklr.com/import-survey-response)

[](https://dev.sprinklr.com/apr-jun-2025)

[Back to top](https://dev.sprinklr.com/apr-jun-2025)
