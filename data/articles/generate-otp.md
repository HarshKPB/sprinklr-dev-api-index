---
title: "Generate OTP"
slug: generate-otp
url: https://dev.sprinklr.com/generate-otp
---

# Generate OTP

#
Generate OTP



Using this API, you can generate a one-time PIN (OTP) and send it to the user via email.

**Dev Notes: **The Community APIs are designed to support limited and specific use cases only. They are not intended for building or replicating a full-scale community platform. For more advanced or large-scale community features, please contact your Sprinklr representative to explore supported solutions.

### API Endpoint

https://care-api-{env}.sprinklr.com/care/community/rest/authenticated/user/send-otp-via-email

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``



``

| Key | Value | Description |
| --- | --- | --- |
| X-Community-Authorization | Bearer {authenticated token} | The Aauthenticated token for making API calls that require creating, updating, deleting tasks |
| Accept | application/json | Determines the acceptable response type from the server |

## Example - Request




  Copy Code



curl -X POST \
  'https://care-api-`{env}`.sprinklr.com/care/community/rest/authenticated/user/send-otp-via-email' \
 -H 'X-Community-Authorization: Bearer {Authenticated Token}' \
  -H 'accept: application/json'  \





## Example - Response



{
    "success": true
}





## Response Parameters
















| Parameters | Description | Type |
| --- | --- | --- |
| success | If true, the OTP has been successfully generated and shared over email | Boolean |

[](https://dev.sprinklr.com/generate-otp)

[Back to top](https://dev.sprinklr.com/generate-otp)
