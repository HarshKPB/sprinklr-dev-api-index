---
title: "API Overview"
slug: api-overview
url: https://dev.sprinklr.com/api-overview
---

# API Overview

#
 API Overview


Sprinklr offers a variety of robust, convenient, and simple RESTful Web service APIs to integrate data from Sprinklr to any external system. Through Sprinklr’s API portal, your developers can create Web applications to interact directly with data that resides in Sprinklr.

Among the available features include RESTful APIs using JSON format, authentication via OAuth 2.0 invoking the existing user-level governance and security model built into Sprinklr as well as a developer portal to manage access to API documentation and API keys. We have APIs to deliver messages to dashboard streams, push or pull profile data, handle digital asset management, and work with reporting and listening insights.

## Sprinklr API Authentication (OAuth 2) and Governance

The OAuth 2.0 authorization framework enables a third-party application to obtain limited access to an HTTP service. Sprinklr currently supports OAuth 2.0 with Code Grant, Client Credentials Grant Type, and JWT Certificate Based Token Generation Process.

## How OAuth works

Let’s assume a user has already signed into one website or service (OAuth only works using HTTPS). The user then initiates a feature/transaction that needs to access another unrelated site or service. The following happens:

- The first website connects to the second website on behalf of the user, using OAuth, providing the user’s verified identity.

- The second site generates a one-time token and a one-time secret unique to the transaction and parties involved.

- The first site gives this token and secret to the initiating user’s client software.

- The client’s software presents the request token and secret to their authorization provider (which may or may not be the second site).

- If not already authenticated to the authorization provider, the client may be asked to authenticate. After authentication, the client is asked to approve the authorization transaction to the second website.

- The user approves (or their software silently approves) a particular transaction type at the first website.

- The user is given an approved access token (notice it’s no longer a request token).

- The user gives the approved access token to the first website.

- The first website gives the access token to the second website as proof of authentication on behalf of the user.

- The second website lets the first website access their site on behalf of the user.

- The user sees a successfully completed transaction occurring.

## How to Get Authentication and Generate Access Token for Sprinklr APIs

Authentication is a 2-step process. URL #1 is used to authenticate a key via a browser. URL #2 is used to generate an OAuth token via a POST request. [Click here to view the docs.](https://dev.sprinklr.com/authorize)

## Use Case

Use cases for a Partner Admin

- PA1 (access provided) API behavior?

- PA2 (access not provided) API behavior?

### PA1 (access provided) API behavior?

Let's see the API behavior when PA1 makes an API request.
**Example:** **Custom Field Create** You can create a Custom Field in the UI via this API call and you will get the Custom field {Id} as Response after making the Request.  Make a POST request and in the Body, enter a raw request with the JSON format, as the endpoint expects a JSON body which contains the details of the keys and values required in Create Custom Field. Click here to view the doc.

### PA2 (access not provided) API behavior?

Let's see the API behavior when PA2 makes an API request.
**Example:** **Custom Field Read** You can read a Custom Field via this API call. After making the GET Request, you will get the Custom Field Objects in JSON format as Response.

**Method:** HTTP    **Endpoint: ** [GET](https://dev.sprinklr.com/custom-field-read-v1): `api/v1/customfield/{Id}` **Format**: JSON

### Header

The following set of HTTP header fields provide required information about the request or response, or about the object sent in the message body. Both request headers and response headers can be controlled using these endpoints.







```

``

``

| Key | Value | Description |
| --- | --- | --- |
| Content-Type | application/json | Request format should be JSON as the endpoint expects a JSON body. |
| Authorization | Bearer {{token}} | Credential used by an application to access an API. |
| Key | api-key | The API key acts as both a unique identifier and a secret token for authentication to a set of access rights. |

Request Parameters



| Query String Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| {id} | Required | The id of the Custom Field on which you want to make a Read API call. | String |

**Request**: `https://api3.sprinklr.com/prod0/api/v1/customfield/{id}`

**Response: **

```
Developer Inactive.

```

## Governance in Sprinklr

Governance is what allows users to establish permission levels for other users. Appropriate permissions are important on every level because they establish what the user can and can’t do within the platform. Governance implements the hierarchical structure of your organization throughout the Sprinklr platform.

Governance is being used in the Sprinklr platform at all times through user roles and permissions. Benefits of governance use include optimizing security initiatives, managing PR, and reproducing internal job structures.  Throughout the Sprinklr Platform, there are several aspects that need permission for use. For example, if you create a queue and want someone to be able to access that queue, they must be given appropriate permission to do so.  **Types of Users** There are 4 types of users within Sprinklr. They are:

- Partner Admin (highest level of access)

- Partner User

- Client Admin

- Client User (lowest level of access)

Within a client environment, Client-level roles/permissions override Partner-level. Click here for more information on Different Level of Users in Sprinklr Platform.

### How Sprinklr API Governance Model Works

Sprinklr API Governance model is directly dependent on Sprinklr User's role/permissions governance model. Governance is what allows users to establish permission levels for other users. Appropriate permissions are important on every level because they establish what the user can and can’t do within the platform and through API calls.

An API key is created for a user for making the API calls. As a result, all permissions and roles tied to a user are equally applied to the associated user API key. You cannot access any feature and cannot make an API call, even after having Sprinklr login credentials, if you do not have the role or the permissions necessary. Partner Roles can be used to permit user access across multiple clients, however, if a user is associated with a Partner Role and a Client Role, the Client Role access will supersede the Partner Role Permissions. Client Roles are user roles that determine the level of user access and permissions within a specific client environment. [Click here](https://www.sprinklr.com/help/articles/roles-and-permissions/manage-roles/6467a80f30f12540268fb658) for more information on adding Roles and Permissions.  (NOTE: [Click here](https://www.sprinklr.com/help/categories/roles-and-permissions/64588f8c72241235fc62d831) to learn more Governance How-To Guidelines)  Note that while Role-based permissions provide basic access within an environment, some content or assets may require additional permissions. Account permission is required for users to view content from, engage with, or publish from specific accounts. Permissions can provide or restrict access to specific areas of the platform or enable users to perform specific actions. You can learn more about how to create roles and permissions [here](https://www.sprinklr.com/help/articles/roles-and-permissions/manage-roles/6467a80f30f12540268fb658).  **Example**: User PA1 has permissions to see a SAM asset A123, but has no permission to see asset A567. So, when user PA1's API key k123 is used to access SAM assets then API will only return asset A123 but not A567.

### To Make An API Call

To make an API call you need to have an understanding of the following terms.

- **Environments** - Prod0, 1, 2, 3 etc.

- **Partner Environment** - Customer Environment made up by at least 1 Client Environment.

- **Client Environment** - Customer’s Client Environment/s.

- **User** - [Partner Admin](https://www.sprinklr.com/help/articles/roles-and-permissions/manage-roles/6467a80f30f12540268fb658), [Partner User](https://www.sprinklr.com/help/articles/roles-and-permissions/manage-roles/6467a80f30f12540268fb658), [Client Admin](https://www.sprinklr.com/help/articles/roles-and-permissions/manage-roles/6467a80f30f12540268fb658), [Client User](https://www.sprinklr.com/help/articles/roles-and-permissions/manage-roles/6467a80f30f12540268fb658).

You can add users to Sprinklr by providing them with the access and permissions they need to get started in Sprinklr. To add a user, you must be an Admin of the Partner or Client environment in which you want to add Users. Based on the roles and permissions, a user can make API calls. The roles and permissions automatically tie-up with the Access Token generated by the user.     **Example**: Suppose, if a company X has two clients Y1, Y2. Company X has added a User1 with permission to access the SAM Assets of client Y1. The User1 can now generate the Access Token and Access Token will automatically have all the details related to User1 roles and permissions. If the User1 tries to fetch or read the data from the SAM of Client Y2 with the Access Token he generated, he will get the 401 Unauthorised message.

[](https://dev.sprinklr.com/api-overview)

[Back to top](https://dev.sprinklr.com/api-overview)
