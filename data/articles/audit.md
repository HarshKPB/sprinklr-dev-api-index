---
title: "Audit"
slug: audit
url: https://dev.sprinklr.com/audit
---

# Audit

#
Audit

Audit API provides details regarding the modifications (audit changelog) made to a given [asset class](https://help.sprinklr.com/articles/governance/asset-classes/613766585f2e7c0c9ed36e4a) over time. This is a governance component that offers visibility into who made what changes and when. The same is available in the within the platform under Activity tab. For more information, please check [here](https://help.sprinklr.com/conversations/search?page=1&q=audit%20trail).

### What is an Asset Class?

Features present on Sprinklr's platform, such as — Account, Outbound Message, Case, or Profile, are referred to as Asset Classes.

Supported Asset Classes Include: `UNIVERSAL_CASE`, `MESSAGE_WORKFLOW`, `PROFILE_WORKFLOW`, `MEDIA_ASSET`, `OUTBOUND_MESSAGE`

The API accepts asset Ids associated with the corresponding asset class, and, in turn, provides information on old and new values for the underlying fields.
