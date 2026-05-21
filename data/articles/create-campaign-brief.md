---
title: "Create Campaign Brief"
slug: create-campaign-brief
url: https://dev.sprinklr.com/create-campaign-brief
---

# Create Campaign Brief

#
  POST - Create Campaign Brief


You can use this API call to create Campaign Brief for a campaign.

## API Endpoint

https://api3.sprinklr.com/{env}/api/v2/campaign/{campaignId}/brief

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

## Path Parameters


















| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| campaignId | Required | The id of the campaign in which you want to create the new brief | String |

## Request Form Data Parameters























| Parameter | Required / Optional | Description | Type |
| --- | --- | --- | --- |
| briefName | Required | Name of the campaign brief. | String |
| htmlFile | Required | The .html file in your local that have campaign brief content. | .html File |

**Dev Notes: ** All html tags are supported except the `link` tag.

## Example - Request

 
 
       
 
 
 
 
 
 
 
 
 
 
 
Copy Code 
   
     

curl --location --request POST 'https://prod0-api3.sprinklr.com/api/campaign/{campaignId}/brief \
--header 'Accept: application/json' \
--header 'Key: {Enter your API KEY}' \
--header 'Authorization: Bearer {Enter your Access Token}' \
--form 'htmlFile=@"/Users/userName/test campaign.html"' \
--form 'briefName="\"Test_File1\""'
 

     
     
   

## Example - Response





 {
    "data": "Successfully added the requested brief: \"\"Test_File1\"\" to the campaign \"{campaignId}\".",
    "errors": []
}






 [](https://dev.sprinklr.com/create-campaign-brief)






[Back to top](https://dev.sprinklr.com/create-campaign-brief)
