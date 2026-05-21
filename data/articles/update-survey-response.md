---
title: "Update Survey Response"
slug: update-survey-response
url: https://dev.sprinklr.com/update-survey-response
---

# Update Survey Response

#
  PUT Update Survey Response

This API enables you to update a survey response.

**Dev Notes: **To use this API, you will need values for the parameters mentioned below. To obtain these values, reach out to Sprinklr Support at [tickets@sprinklr.com](mailto:tickets@sprinklr.com).

## API Endpoint

	https://api3.sprinklr.com/`{env}`/api/v2/survey-response/`{survey-response-id}`

### Headers

API headers include the mandatory information you send along with the request URL and body. This information helps provide insights into request context and authorization credentials that, in turn, allows access to protected resources.











			``


[Authorize](https://dev.sprinklr.com/authorize)



			``


[Getting Started](https://dev.sprinklr.com/api-key-and-secret-generation)



			``



``

| Key | Value | Description |
| --- | --- | --- |
| Authorization | Bearer {token} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Path Parameters



















| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| {survey-response-id} | Required | String | Unique identifier of the survey response. |



**Steps to Retrieve Survey Response Id from Sprinklr UI**


- Open Customer Feedback Management (CFM) persona app in Sprinklr.

- In the **Programs** tab, locate the survey of which you want to fetch the responses.

- Hover over the survey. A **View** button is displayed.

- Click **View**.

- On the top bar, click **Responses**.

The **Response Id** column values correspond to `survey-response-id`.


### Request Parameters















****






****









| Parameter | Required/Optional | Type | Description |
| --- | --- | --- | --- |
| responseCustomFields | Optional | Object | Custom fields specific to the response. See Steps to Retrieve Survey and Transaction Custom Field Name given below. |
| transactionCustomFields | Optional | Object | Transactional custom fields related to the response. See Steps to Retrieve Survey and Transaction Custom Field Name given below. |
| profileCustomFields | Optional | Object | Custom profile fields related to the responder |

**Steps to Retrieve Survey and Transaction Custom Field Name from the Sprinklr UI**


- Open the **Customer Feedback Management (CFM)** persona app in Sprinklr.

- Navigate to the **Programs** tab and locate the survey for which you want to access custom fields.

- Hover over the survey to reveal the **View** button.

- Click **View** to open the survey details.

- From the top navigation bar, click **Settings**.

- Scroll to the **Survey Custom Fields** section. This section includes two options:


  - **Transaction Fields**

  - **Response Custom Fields**



- Click the **View Fields** button next to **Transaction Fields** if you're looking for transaction-related custom fields, or next to **Response Custom Fields** if you're looking for response-related custom fields.

- This opens a list of all the custom fields under the selected category.

- Find the specific field you're interested in. Click the three-dot menu (**⋮**) next to it.

- Select **Copy Field Name** to copy the internal field ID, which is used in API requests.


## Example - Request




 Copy Code


curl --location --request PUT 'https://api3.sprinklr.com/{env}/api/v2/survey-response/68c9247b3e6065068e7083d5' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {Enter Your Access Token}' \
--data '{
    "responseCustomFields": {
        "_c_672c9f4729193453ec0ac1ae": [
            "xyz"
        ]
    },
    "transactionCustomFields": {
        "_c_685bbcea402bb16a007c47ed": [
            "abc"
        ]
    },
    "profileCustomFields": {
        "_c_64cbf526fd8b0e259d72470a": [
            "20"
        ]
    }
}'



## Example - Response




{
    "data": "Survey response updated successfully.",
    "errors": []
}





  [](https://dev.sprinklr.com/update-survey-response)




[Back to top](https://dev.sprinklr.com/import-survey-response)
