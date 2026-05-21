---
title: "User (SCIM)"
slug: v1-user-apis
url: https://dev.sprinklr.com/v1-user-apis
---

# User (SCIM)

#
User (SCIM)

User management allows providing access to users within Sprinklr. The roles and permissions defined for the users decide the level of access provided to the provisioned users.

Using these APIs, you can create, fetch user details, define roles and permissions, update, and even delete a user.

### Supported User Types













| User-Type | Description |
| --- | --- |
| Partner Admin | Highest level of access; has visibility across the entire brand, can manage users, accounts, workflow structures, and client (local division) accesses, and structures. |
| Partner User | Second highest level of access; has visibility across the entire brand but cannot manage client (local division) accesses. |
| Client Admin | Highest level of access within a Client  environment, can manage users, accounts, and workflow structures within their local Client. |
| Client User | Lowest level of access/permissions; cannot manage users or accounts, cannot manage workflow structures within any local Client environment. |

**Related Article:** **[User Provisioning Blueprint](https://dev.sprinklr.com/user-provisioning-blueprint)**
