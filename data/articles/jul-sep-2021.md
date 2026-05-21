---
title: "Jul - Sep, 2021"
slug: jul-sep-2021
url: https://dev.sprinklr.com/jul-sep-2021
---

# Jul - Sep, 2021

# Jul - Sep, 2021

**Developer Note:**
We have migrated our Developer Portal to a new platform. As part of this migration, all historical changelogs have been preserved.
Please note that the API base endpoint has changed from `api2` to `api3`.
For changelogs dated **before January 2025**, references to `api2` endpoints should be interpreted accordingly. If you're reviewing past updates, ensure you account for this change when mapping endpoint behavior or request structures.

## **Publishing Message API Endpoint Enhancement** - September 29th, 2021

You can use this API to publish quick replies on supported social and messaging channels.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/publishing/message

## **TLS v1.1 Deprecation Notice** - October 31, 2021

Sprinklr will be disabling support for TLS v1.1 across our public facing APIs. We are providing advance notice here so our Customers and Partners can prepare accordingly.

**Upcoming Breaking Change**
 Note that this includes a breaking changes to the API and may require a code change of your side. See below for more details.
















| Service | URL | Deprecation Date |
| --- | --- | --- |
| All public facing APIs. | https://api2.sprinklr.com | October 31, 2021 |

After the above said date, connection to the Sprinklr API using TLS v1.1 or below will be rejected, and an error will be returned (TLS negotiation will fail). You can continue to make API connections to Sprinklr using TLS v1.2 or above.

### Why are we disabling TLS v1.1?

The Internet Engineering Task Force (IETF) has formally deprecated Transport Layer Security (TLS) versions 1.0 (RFC 2246) and 1.1 (RFC 4346) as of March 2021 (RFC 8996).
These older versions lack support for current and recommended cryptographic algorithms and mechanisms; in light of that, Sprinklr is enforcing a higher standard of security by only allowing connections using TLS v1.2 or above.

## **Partial User Update API Endpoint** - July 17, 2021

You can partially update a User via this API call as it only updates the values passed in the API call payload.

**API Endpoint**

POST https://api2.sprinklr.com/{env}/api/v2/scim/update/{userId}

## **Draft Webhook Payload Enhancement** - July 17, 2021

To enhance the business use cases and to Draft Webhook Payload more useful in integrations, three new fields are added to Draft Webhook Payload.

**Added Fields**


```

"contentTemplateIds": [
  "5be9248ae4b05njbhdy78dt0"
],
 "accountTypes": [
  "ABC"
],
"sourceLocale": "en_US"

```

## **Webhook Callback Url Authentication Enhancement** - July 17, 2021

Now the Webhook Callback Url verification in Sprinklr UI will show verified for the following response code `200, 201, 201, 203, 204`.



## ** Publishing API Supported Channel Enhancement** - July 17, 2021.

Now you can send reply to fan messages via Sprinklr Publishing API on Apple Business Chat. This enhancement will help in external bot integration over Apple Business Chat, where the bot can use SPrinklr Publishig API to reply back to customer.

## **Sprinklr API User Additional Governance** - July 17, 2021

Now you can set governance over the data a user can fetch using Sprinklr API apart from the permission that are given to user in Sprinklr UI.

**Note: ** Please reach out to your Success Manager or Sprinklr support to get Additional Governance enabled for your environment.

[](https://dev.sprinklr.com/jul-sep-2021)

[Back to top](https://dev.sprinklr.com/jul-sep-2021)
