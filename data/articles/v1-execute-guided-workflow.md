---
title: "Execute Guided Workflow"
slug: v1-execute-guided-workflow
url: https://dev.sprinklr.com/v1-execute-guided-workflow
---

# Execute Guided Workflow

#
  POST Execute Gudied Workflow


Using this API, you can execute the guided workflow from the backend.

## API Endpoint

https://api3.sprinklr.com`/{env}/`api/v1/process-engine/queryProcess

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
| Authorization | Bearer {{token}} | Credential used by the API to authenticate a user with the serverFor generating authorization token, refer to  section on the developer portal |
| Key | api-key | API key helps authenticate the application with the serverFor generating API key, refer to  guide |
| Content-Type | application/json | Content-Type is a representation header that determines the type of data (media/resource) present in the request body |
| Accept | application/json | Determines the acceptable response type from the server |

### Request Parameters

****

| Parameter | Sub-Parameter | Required/Optional | Description | Type |
| --- | --- | --- | --- | --- |
| processVariables |  | Optional | Refers to the object containing the details of the asset on which the guided workflow needs to be executed | Object |
|  | processDefinitionId | Optional | Refers to the unique identifier for the guided workflow | String |
|  | merchantId | Optional | Refers to the unique identifier for tthe merchant used for payment | String |
|  | userId | Optional | Refers to the Sprinklr user Id associated with the agent | String |
|  | ivrType | Optional | Refers to the IVR type | String |
| processDefinitionId |  | Required | Refers to the unique identifier for the guided workflow | String |
| command |  | Required | Refers to the command you want to execute on the guided workflowSupported Value: START |  |

### Example - Request














Copy Code




curl -X POST \
  https://api3.sprinklr.com/{env}/api/v1/process-engine/queryProcess' \
  -H 'Authorization: Bearer {Enter your Access Token}' \
  -H 'Key: {Enter your API KEY}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "processVariables": {
        "processDefinitionId": "299048",
        "merchantId": "Test Merchant",
        "userId": "9812",
        "ivrType": "Payment"
    },
    "processDefinitionId": "299048",
    "command": "START"
}'





## Example - Response





{
    "processInstanceId": "6630dfc0e42a2d74cea01eaa",
    "outputVariables": {
        "merchantId": "Test Merchant",
        "ivrType": "Payment",
        "userId": "9812"
    }
}





[](https://dev.sprinklr.com/v1-guided-workflow)




[Back to top](https://dev.sprinklr.com/v1-guided-workflow)
