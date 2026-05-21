---
title: "Create Authenticated Token"
slug: create-authenticated-token
url: https://dev.sprinklr.com/create-authenticated-token
---

# Create Authenticated Token

#
  Create Authenticated Token



UnAuthenticated token helps authorize API calls that return publicly accessible data present on the community forum. This token doesn’t require any login process and can be used for read API calls.

### API Endpoint

https://care-api-{{env}}.sprinklr.com/care/community/jwt/un-authenticated/token

## Query Parameters


























| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| requestToken | Required | Refers to the preshared key.This will be shared over with you over secure mail upon request | String |
| projectId | Required | Refers to the project Id of the instance.This will be shared over with you over secure mail upon request | String |

### Sample API Request




  Copy Code



curl -X GET \
 'https://care-api-{{env}}.sprinklr.com/care/community/login'\
  -H 'Accept: application/json' \
  -H 'X-Community-Authorization: Bearer {{un-authenticated-token}}' \
  -H 'username: autouser' \
  -H 'password: Auto@123' \
  -H 'Content-Type: application/json' \





## Example - Response




{
"communityUserId":"60ae445e4a5ae60c2e29aa03",
"accessToken":"eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJBY2Nlc3MgVG9rZW4gR2VuZXJhdGVkIGZyb20gQ29tbXVuaXR5IiwiaXNzIjoiU1BSSU5LTFIiLCJ0eXAiOiJKV1QiLCJjb21tdW5pdHlVc2VySWQiOiI2MGFlNDQ1ZTRhNWFlNjBjMmUyOWFhMDMiLCJleHBlcmllbmNlSWQiOiJjZDZhYWFhZC03ZDAyLTQ1OTktOWM2Mi1hZWU4MDY4Zjc4ZGEiLCJhdWQiOlsiU1BSSU5LTFIiXSwibmJmIjoxNjU5OTUxMTczLCJzY29wZSI6WyJSRUFEIiwiV1JJVEUiXSwiYXV0aFR5cGUiOiJTUFJfQVVUSEVOVElDQVRFRCIsInRva2VuVHlwZSI6IkFDQ0VTUyIsImV4cCI6MTY2MjU0NDM3MywicHJvamVjdElkIjoiOTVkYTI3YjItOGUzOC00MGVhLWEyZTEtNGUwNzY5Y2Q3NDcxIiwiaWF0IjoxNjU5OTUyMzczLCJqdGkiOiJzcHJpbmtsciJ9.jdvuqKqh3g2UzuVF3XZrjaNjvPHFSwCi0ekQIyq76Licp2XtaOSqnDS_wtKc3xHFEqdUNUHUxQVebdWkgsEyYapAC1phjx_UAsn464i2SidAaknHcmf_XUwXtMtMp7je-ZWDXTKrXagJ3EkoG1h8ilpRJEnqAJEMaWmOK41rtFYw6FrimhCGppIfvaLNfAu_YhSDtCsCQ9anMc_kx-nVMh_oRf1mJR-Pl2i0z_PMKRF3VZSt4zk2bfB84WzJdtMsaLCkmnSCakewrLLFi6XRTdC9j0VGIpaiQ5_nDW4KEgsxdZvet4JEXvBtLmuWMWe_DUCje3TpPNbyKnWWMLPrHw",
"responseCode":"SUCCESS",
"responseMessage":"Successfully logged in."
}





**Dev Notes: **By default, the unauthenticated token is valid for 30 days

## Response Parameters
















| Parameters | Description | Type |
| --- | --- | --- |
| UnAuthenticated Token | Token for making API requests that returns publicly accessible data | String |

[](https://dev.sprinklr.com/reporting-blueprints)

[Back to top](https://dev.sprinklr.com/reporting-blueprints)
