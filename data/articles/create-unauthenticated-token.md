---
title: "Create Unauthenticated Token"
slug: create-unauthenticated-token
url: https://dev.sprinklr.com/create-unauthenticated-token
---

# Create Unauthenticated Token

#
Create Unauthenticated Token



UnAuthenticated token helps authorize API calls that return publicly accessible data present on the community forum. This token doesn’t require any login process and can be used for read API calls.

### API Endpoint

https://care-api-`{{env}}`.sprinklr.com/care/community/jwt/un-authenticated/token

## Query Parameters


























| Parameters | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| requestToken | Required | Refers to the preshared key.This will be shared over with you over secure mail upon request | String |
| projectId | Required | Refers to the project Id of the instance.This will be shared over with you over secure mail upon request | String |

### Sample API Request




  Copy Code



curl -X POST \
  'https://care-api-{{env}}.sprinklr.com/care/community/jwt/un-authenticated/token?requestToken=_pre_shared_key_&projectId=_projectId' \





## Example - Response

      

eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJBY2Nlc3MgVG9rZW4gR2VuZXJhdGVkIGZyb20gQ29tbXVuaXR5IiwiYXVkIjpbIlNQUklOS0xSIl0sIm5iZiI6MTY1OTk0NTE1OCwic2NvcGUiOlsiUkVBRCIsIldSSVRFIl0sImlzcyI6IlNQUklOS0xSIiwidHlwIjoiSldUIiwidG9rZW5UeXBlIjoiQUNDRVNTIiwiYXV0aFR5cGUiOiJTUFJfVU5BVVRIRU5USUNBVEVEIiwiZXhwIjoxNjYyNTM4MzU4LCJwcm9qZWN0SWQiOiI5NWRhMjdiMi04ZTM4LTQwZWEtYTJlMS00ZTA3NjljZDc0NzEiLCJpYXQiOjE2NTk5NDYzNTgsImp0aSI6InNwcmlua2xyIn0.By1llcIaoKAISbgIhBR87ehomklOrJAXfPptB8OUImUv6vfpFCN3VtJizZIEFxhZ1ftZk2EbrYPTOW34s75ep8_HdmeQ3511oVMBC76_sQmMRHOgXhlwGqLovcHeOXk2qhJyvSPnYnp6uCPM7kNfUSz-pQEvGxiTMTROrf3DN5BJEQvGojCrJfYSKUb46DJZMw4om-mKX01Tbgb9qDcKJgMk05IPad8NA00iIBVRRPks7l6tEk3HeBNgQUjHXA7FsM42aKSFjjq_g0eBJYQFMkpS-BP_S3FUPvoPHjOmIxSz1cDWUtfR_0-l6tq9z6shVrAmPvnCFVC4HBoWWfCgxu





**Dev Notes: **By default, the unauthenticated token is valid for 30 days

## Response Parameters
















| Parameters | Description | Type |
| --- | --- | --- |
| UnAuthenticated Token | Token for making API requests that returns publicly accessible data | String |

[](https://dev.sprinklr.com/reporting-blueprints)




[Back to top](https://dev.sprinklr.com/reporting-blueprints)
