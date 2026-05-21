---
title: "Remove Filter"
slug: remove-filter
url: https://dev.sprinklr.com/remove-filter
---

# Remove Filter

# Remove Filter


This method is used to remove the filter you added using the [addFilterToEvaluate](https://dev.sprinklr.com/add-filter-to-evaluate-live-chat-state) method. To remove the filter, pass the unique ID of the filter defined in the addFilterToEvaluate method.

## Method

`sprChat(‘removeFilterToEvaluate’);`

## Parameters







| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| filter | {      id: string   } | Required | An object containing the unique ID associated with the filter that is being evaluated. |

## Examples

The following are a few examples of unsubscribing the filter evaluation. The filter IDs are of the filters shown in the Add Filter topic:

**Example 1**: The following example removes the UserCountry filter:




  Copy Code



window.sprChat('removeFilterToEvaluate', {id: 'USER_COUNTRY_FILTER_ID'} );





**Example 2**: The following example removes the BusinessHours filter:




  Copy Code



window.sprChat('removeFilterToEvaluate', {id: 'BUSINESS_HOURS_FILTER_ID'} );





**Example 3**: The following example removes the AgentAvailability filter:




  Copy Code



window.sprChat('addFilterToEvaluate', {id:  'AVAILABLE_AGENTS_FILTER_ID'});





**Example 4**: The following example removes the IsConversationOpen filter:




  Copy Code



window.sprChat('addFilterToEvaluate', {id: 'IS_CONVERSATION_OPEN_FILTER_ID' } );





**Example 5**: The following example removes the NumberOfConversations filter:




  Copy Code



window.sprChat('removeFilterToEvaluate', {id: 'DOES_CONVERSATION_EXIST_FILTER'} );





[](https://dev.sprinklr.com/remove-filter)

[Back to top](https://dev.sprinklr.com/remove-filter)
