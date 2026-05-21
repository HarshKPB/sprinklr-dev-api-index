---
title: "CFM Transaction APIs"
slug: cfm-transaction-apis
url: https://dev.sprinklr.com/cfm-transaction-apis
---

# CFM Transaction APIs

#  CFM Transaction APIs

Transactions in Sprinklr CFM allow you to record interaction data for customer events. Transactions provide a structured foundation for triggering personalized surveys and understanding contextual feedback.


## Key Concepts


### Transactions


A transaction is a single record that represents a specific interaction or event with a customer (for example, a purchase, support ticket, or delivery).

Each transaction contains metadata, called Transaction Fields, which are key-value pairs describing details of the interaction. Transaction Fields follow the Sprinklr Custom Field framework and support multiple data types:


- Text / Multi-Text

- Number

- Date-Time

- Single Select / Multi Select



### Characteristics of Transactions



- Every transaction must be linked to a Sprinklr Profile, ensuring the interaction is tied to the right customer.

- Surveys can be triggered after a transaction to collect context-specific feedback.

- Transaction metadata can be used to personalize survey experiences, create reports, and filter on analytics.

- Transactions integrate with CFM Workflows, enabling automated survey distribution once a transaction is ingested through API or other methods.



### Transaction Groups


A transaction group is a collection of transactions with a defined schema. Before using the Transaction APIs, you must create a transaction group.


## Setup Instructions



- In your CFM persona app, go to **Audience Management** → **Transactions**.

- Create a Transaction Group of type “API”.

- Define your schema with the required custom fields.

- Ensure that the custom fields in your API requests match the defined schema.


Transaction groups allow you to enforce structure, making it easy to align ingestion, personalization, and reporting across multiple interaction types.


Sprinklr provides APIs to create, fetch, and delete transactions.

[](https://dev.sprinklr.com/cfm-transaction-apis)

[Back to top](https://dev.sprinklr.com/cfm-transaction-apis)
