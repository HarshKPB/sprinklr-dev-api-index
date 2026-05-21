---
title: "User Provisioning - Blueprint"
slug: user-provisioning-blueprint
url: https://dev.sprinklr.com/user-provisioning-blueprint
---

# User Provisioning - Blueprint

#
		 User Provisioning - Blueprint



User provisioning is the onboarding and managing of users within a Sprinklr environment. You can add, modify, search, delete, and manage roles and permissions for users at both global and workspace levels. Sprinklr supports SCIM (System for Cross-domain Identity Management) APIs that help automate the user provisioning process.

Gartner states, “`User provisioning or account provisioning technology creates, modifies, disables, and deletes user accounts and their profiles across IT infrastructure and business applications.`”

The platform UI or APIs can onboard users in the Sprinklr environment. In this article, we’ll explore the capabilities of SCIM APIs.

**Commonly Used Naming Conventions**

- **Client**: at Workspace level

- **Partner/Customer** - at Global level

## Things to Know in Advance

- Register on the [developer portal](https://dev.sprinklr.com/developer-portal-registration). Next, [register the application](https://dev.sprinklr.com/getting-started) (generate API key), and generate an [authorization token](https://dev.sprinklr.com/authorize) to access Sprinklr’s SCIM APIs

- When generating the token, ensure that access is given to all the workspaces, you want to add the user to

- Adding users and defining roles & permissions is an admin feature

- Once the user is added to Sprinklr, an email invite is sent to them, which remains active for 60 days. The users can accept the invite and reset passwords and modify personal details.

- To add a user, you must be a partner admin or a partner user in a customer environment or a client admin within a workspace environment

- You cannot create a user with higher-level access than yourself. For example, if you are a workspace admin, you cannot create a global admin user

- Use a unique email id for every user, as no two instances of users can exist with the same email address.

- If a user is associated with both the customer and workspace roles, then the workspace role access will supersede the customer role permission.

- Reach out to your success manager to enable SSO (Single Sign On) for your Sprinklr instance

- Access and permission to create, view, edit, and delete dashboards and queues should be separately shared

- If access to multiple clients (workspaces) is involved in the provisioning, you should always create roles at partner level

- You can't create users in sandboxes. However, you can modify your users. Going forward, we recommend you add a new user in production and then push the user into the sandbox.

## Supported User Types

Sprinklr supports different user types that decide the level of access they’ll have. Refer to the table below for an overview of supported user types.

``

-
-
-
-
-

``

-
-
-
-
-

``

-
-
-
-

``

-
-

| User Level | Access Level | Description |
| --- | --- | --- |
| PARTNER_ADMIN (Global Admin) | Highest - can add Users at all levels | View all the existing workspace environmentsVisibility into all social channelsPublish across social channelsAssign roles and permissionsModify global level settings in the Administration module |
| PARTNER_USER (Global User) | Second Highest | View all social channels in the Customer or the shared Workspace environmentPublish across social channels within the WorkspaceChange Customer and Workspace level settings in Administration, including Rules Engine and Roles/PermissionsAdd users of equal or lower permission levelsAccess to Posting, Monitoring, Reporting, and all modules enabled in the Workspace Environment |
| CLIENT_ADMIN (Workspace Admin) | Highest at the workspace level | Override Global-level user's Roles/PermissionsAdd users of equal or lower permission levelsAccess to Posting, Monitoring, Reporting, and other enabled modules within the Workspace EnvironmentChange Workspace-level settings in Administration, including Rules Engine and Roles/Permissions |
| CLIENT_USER (Workspace User) | Lowest | View all provisioned channels in the Workspace EnvironmentAccess within the Workspace Environment on permission basis |

**Related Knowledgebase Article**: [Global and Workspace Users](https://www.sprinklr.com/help/articles/advanced-capabilities/global-and-workspace-users/67fd0ba0de7b4670fb2399fb)

## User Provisioning: API References

Refer to the following APIs for user provisioning workflow:

### Create User

Adding a user to Sprinklr can be achieved using the following APIs:

### 1.1 Create User API

Using this API, you can add a user to Sprinklr’s environment. The user will be added to the environment with which the access token is associated. The API request can specify the corresponding workspace details and user type.

**Related Developer Portal Documentation**:  [Create User](https://dev.sprinklr.com/create-user)

**Dev Notes: **

- Modern Engagement product seat is assigned to the user by default

- Only partner admin, partner user, or workspace admin is permissible to add users

- You cannot create a user with a higher user level than yourself

### 1.2 Create Distributed User

Distributed is a Sprinklr Lite version where you can distribute user capabilities to one or multiple sub-users or a team that can use Sprinklr on behalf of the brand.

**Note**: Refer to the following associated parameters to create a distributed user using SCIM API.

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| businessCategory | Required for setting up distributed user | Set to “Distributed” for creating a distributed user | String |
| isSpaceUser | Required | If true, the user can access space UI onlySet to “false” for creating a distributed user | Boolean |
| productSeat | Optional | If the user needs to be added to the Distributed, productSeat will be set to "Distributed" | String |

### 2. Create Asset Group

The asset group refers to the entities in Sprinklr that can be grouped. For example, you can create a User Group, which comprises multiple users at the Workspace level.

### 2.1 Create Dynamic User Group

Using this API, you can create a dynamic user group and assign the necessary platform permissions.

**Related Developer Portal Documentation**: [Create Asset Group](https://dev.sprinklr.com/create-asset-group)

### 3. Fetch User Details

The following APIs help in fetching the details for existing Sprinklr user.

### 3.1  Read User Using userId API

Using this API, you can fetch the details of an existing user for the given user id.

**Related Developer Portal Documentation**: [Read User Using User Id](https://dev.sprinklr.com/read-user)

### 3.2 Read User Using email Id API

Using this API, you can fetch the details of an existing user for the given user email id.

**Related Developer Portal Documentation**: [Read User Using Email Id](https://dev.sprinklr.com/read-user-by-email-id)

**Dev Notes: **The email id should be URL-encoded in the API request.

### 3.3 Search User

Using this API, you can search user/s for the given filter types and sorting conditions.

	**Related Developer Portal Documentation**: [Search By Entity User](https://dev.sprinklr.com/search-by-entity)

### 4. Update User

The following APIs help in updating the details for existing Sprinklr user.

### 4.1 Update User Details

Using this API, you can update the details of existing user

	**Related Developer Portal Documentation**: [Update User](https://dev.sprinklr.com/user-update)

**Dev Notes: **

- If createMissingClient is true, the user is added to all the workspaces (clientIds) mentioned in the request payload

- If deleteMissingClient is true, the user is deleted from all the workspaces (clientId) missing in the request payload

### 4.2 Partial Update User

Using this API, you can partially update the user details passed in the API request.

	**Related Developer Portal Documentation**: [Partial Update User](https://dev.sprinklr.com/partial-user-update)

### 4.3 Create/Update User

Using this API, you can create or update a user using a single API call. The user email is the unique identifier, i.e., if you pass a new email in the request, a user gets created, or else the user gets updated.

**Related Developer Portal Documentation**: [Create/Update Update User](https://dev.sprinklr.com/create-update-user)

### 5. Delete/Disable User

You can either delete or disable user using the update user API.

### 5.1 Delete User

Using this API, you can permanently delete the user from Sprinklr’s environment.

	**Related Developer Portal Documentation**: [Delete User](https://dev.sprinklr.com/delete-user)

### 5.2 Disable User

User can be enabled or disabled using create or update user endpoint. You can configure the API request field “active” to true or false to enable or disable the user.

	**Related Developer Portal Documentation**: [Update User](https://dev.sprinklr.com/user-update)

### 6. Bulk Import Users to Sprinklr

You can use the following APIs to import users to Sprinklr in bulk.

### 6.1 Download Template API

Using this API, you can download an excel template for uploading the user details, which can then be used as a source for importing users to Sprinklr.

**Related Developer Portal Documentation**: [Download Template](https://dev.sprinklr.com/bulk-import-entity)

**Dev Notes: **Alternatively, you can download the template from the Sprinklr platform. Refer to this [knowledgebase article](https://www.sprinklr.com/help/articles/user-management/add-users-in-sprinklr/6467b13c30f12540268fb693#a665e6c6-4cc7-44b7-b8ee-c4cf820400ee) for detailed steps.

### 6.2 Media Upload API

Once the template is downloaded, fill in the users’ details under the respective column field names. Once done, use media upload API to generate a publicly accessible URL for the file.

	**Related Dev Portal Documentation**: [Media Upload API](https://dev.sprinklr.com/media-upload)

### 6.3 Import Entity

Once the file has been uploaded, use import entity API to facilitate the import to Sprinklr.

**Related Dev Portal Documentation**: [Bulk Import API](https://dev.sprinklr.com/bulk-import-entity)

**Dev Notes: **Once you receive 200 OK and a task Id in the response for the above request, you can validate the import success from the payload sent to the callback URL.

## FAQs: User Provisioning

### 1. What is a User Group?

A user group involves creating a single group for multiple users sharing common attributes. This is primarily done at the workspace level. Two types of user groups can be created in Sprinklr, i.e.,

- **Static Group**: for manually adding users. You can select the users from the “Select Users” section to add users to the group

- **Dynamic Group**: for adding users based on a defined custom property. Select user attributes (custom fields) and corresponding values from the drop-down list. Users that meet this condition will automatically be added to the dynamic user group.
**Related Knowledgebase Articles**:

- [Create Static User Group](https://www.sprinklr.com/help/articles/sprinklr-service-glossary/user-groups/64090b5a7517d84a3aaf3993)

- [Create and Assign Dynamic user Groups](https://www.sprinklr.com/help/articles/user-management/create-and-assign-dynamic-user-groups/6467b1248ea3c9635cf374ba)

**Dev Notes: **To add a user to an existing user group using SCIM APIs, configure the userGroupIds field in the request payload.

The description for the field is given below:

| Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- |
| userGroupIds | Optional | Refers to the list of existing user group ids where you want to add the new user | List [Integer] |

**Related Knowledgebase Article**: [Manage User Groups](https://www.sprinklr.com/help/articles/sprinklr-service-glossary/user-groups/64090b5a7517d84a3aaf3993)

### 2. What Do We Mean by Assigning Roles & Permissions in Sprinklr?

Roles and permissions provide access to features/functionality and the capability to perform actions when accessing Sprinklr’s UI. Two different types of [roles supported by Sprinklr](https://www.sprinklr.com/help/articles/roles-and-permissions/manage-roles/6467a80f30f12540268fb658) include:

- **Workspace Role (formerly client)**: Defines the level of access and permissions within a specific workspace environment

- **Global Role (formerly partner)**: Defines the level of access and permissions across workspaces
**Related Knowledgebase Article**: [Sprinklr Platform Permissions](https://www.sprinklr.com/help/articles/roles-and-permissions/manage-roles/6467a80f30f12540268fb658)

### 3. What are Product Seats?

Partner and client admins can manage product seats while creating a user, which defines what Sprinklr product can be accessed by the user. The number of product seats visible in your account depends on your contract. The supported product seats include:

- Modern Engagement

- Modern Marketing

- Modern Care

- Modern Marketing Lite

- Distributed

**Dev Notes: **

- The user create API adds the user to Modern Engagement product seat by default

- Modern Ads and Modern Research users occupy a Modern Engagement seat
**Related Knowledgebase Article**: [About Product Seats](https://www.sprinklr.com/help/articles/platform-modules/about-product-seat/633c5c2d59534970b26f96eb)
[](https://dev.sprinklr.com/user-provisioning-blueprint)

[Back to top](https://dev.sprinklr.com/user-provisioning-blueprint)
