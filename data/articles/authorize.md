---
title: "Authorize"
slug: authorize
url: https://dev.sprinklr.com/authorize
---

# Authorize

#
 Authorize

The Sprinklr OAuth 2.0 authorization framework enables a third-party application to obtain limited access to an HTTP service. Sprinklr currently supports OAuth 2.0 with Code Grant and client credentials.
 Code grant requires a 3-legged flow among the resource server, the resource owner and the client. This allows the resource server to authenticate the client and the resource owner to authorize the client so that the client will be able to act on behalf of the resource owner. On the other hand, client credentials require setting up a default user for generating access token.

**Dev Notes: **To generate authorization token, you need to be assigned the `Generate Token` permission from within the Sprinklr Platform. This ensures that only authorized users can generate token and access Sprinklr APIs.

### Related Documentations

- [OAuth 2.0 for Customers](https://dev.sprinklr.com/oauth-2-0-for-customers) - Code Grant

- [OAuth 2.0 SSO for Partners](https://dev.sprinklr.com/oauth-2-0-for-partners) - Code Grant

- [Client Credentials Grant Type](https://dev.sprinklr.com/client-credentials-get) - Default User

- [JWT Token Generation](https://dev.sprinklr.com/jwt-token-generation) - Certificate Based

**Dev Notes: **Only one token can exist per API key. If you have multiple stateless instances, you'll have to generate a new API key and token pair for each of them. Kindly note that generating a new token will also update the refresh token.

For example, you have two stateless applications called A and B. If application A is using a token and now application B generates the token using the same API key (client_id), application A's token and refresh token will get invalidated.
