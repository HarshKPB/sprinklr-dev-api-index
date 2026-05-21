---
title: "Add Filter to Evaluate Live Chat State"
slug: add-filter-to-evaluate-live-chat-state
url: https://dev.sprinklr.com/add-filter-to-evaluate-live-chat-state
---

# Add Filter to Evaluate Live Chat State

#  Add Filter to Evaluate Live Chat State


This method is used to evaluate the state of Live Chat using filters. The results of the filter are passed to a subscriber function, which is in turn passed as a third argument. The subscriber function gets invoked each time the Live Chat state changes during a session.

## Method

`sprChat(‘addFilterToEvaluate’);`

## Parameters







****

****

****

- ****
-
****

-
****

-
********

-
****

-
****

-
****

| Parameter | Type | Required/Optional | Description |
| --- | --- | --- | --- |
| filter | type FilterType = {     filterType: ‘OR’ \| ‘AND’;     filters: Array<{         field: string;         values: Array;         filterType: string;         filters?: FilterType;         id?: string; }>; } type Filter = {     id: string;     filters: FilterType \| FilterType[] } | Required | Defines the filter you want to evaluate with. filterType: For the definition and values, see the Field, filter type, and values section below. id: A unique ID for this request. It is also needed to unsubscribe to the filter updates.   filters: An array of multiple filters or a singular filter object. The filters array includes the following parameters:   field: Name of the field that you want to evaluate.       values: Expected values of the field.        filterType: A comparator operator that is used to evaluate the expected values of the field with its current value in the Live Chat state.        id: Unique filter ID.        filters: Child filter of this filter (recursive). |
| callback | type Result = {     passed: boolean;     values: any; }; type Data = {     id: string;     filters: Filter,     results: Result \|      Result[]  } type Error = string; type Callback = ({data: Data, error: Error}) => void; | Required | The evaluated results of the filter are passed as an argument to the callback function. If any error occurs, the error is passed to the function instead of the results.    If an array of filters is passed to the callback function, an array of the results object is returned. Otherwise, a simple object is returned.    The results object consists of the following:      passed: Returns true if the values for all the given fields are as expected.        values: The current value of each field in the Live Chat state. |

### Filter fields, type, and values

The filter type, that is, the comparator, depends on the type of the field. For example, `timeSpentOnSite` is a numeric value. Therefore, you can use comparators like greater than or equal to.

The following is a list of the filter types that you can use:

GT: Greater than, GTE: Greater than or Equals to, LT: Less than, LTE: Less than or Equals to, EQUALS: Equals to, NOT_EQUALS: Not Equals to, IN: Containing In, NIN: Not Containing in, REGEX: matches regex pattern

The following table lists all the fields that can be queried, filter type, and values:







| fields | filterType | values (with sample/enums) |
| --- | --- | --- |
| 'browsingSession.timeSpentOnSite' | GT, GTE,  LT, LTE,  EQUALS,  NOT_EQUALS | [number]  For example: [3000] time in milliseconds |
| 'userIPDetails.countryLong' | IN, NIN,  REGEX | [string]  For example: [‘India’] |
| 'userIPDetails.city' | IN, NIN,  REGEX | [string]   For example: [‘Mumbai’] |
| 'BUSINESS_HOURS' | IN | [boolean]  For example: [true] or [false] |
| 'AVAILABLE_AGENTS' | GT, GTE,  LT, LTE,  EQUALS,  NOT_EQUALS | [boolean]  For example: [true] or [false] |
| 'AVAILABLE_AGENTS' | GT, GTE,  LT, LTE,  EQUALS,  NOT_EQUALS | [boolean]  For example: [true] or [false] |
| 'IS_CONVERSATION_OPEN' | IN | [boolean]  For example: [true] or [false] |
| 'DOES_CONVERSATION_EXIST' | GT, GTE,  LT, LTE,  EQUALS,  NOT_EQUALS | [number]  For example: [0] |

## Examples

**Example 1**: The following example evaluates whether the total time spent on the page is greater than or equal to 60 seconds:




  Copy Code



const TIME_SPENT_ON_PAGE_FILTER = {
   id: 'TIME_SPENT_ON_WEBSITE_FILTER_ID',
   filters: {
      filterType: 'OR',
      filters: [
         {
            field: 'browsingSession.timeSpentOnSite',
            filterType: 'GTE',
            values: [60000],
            id: 'TIME_SPENT_ON_WEBSITE_GTE_6000_ID'
         },
      ],
   },
};
const handleFilterResults = ({ data, error }) => {
   const { id, filters, results: { passed, values } } = data;
   // code
};
window.sprChat('addFilterToEvaluate', TIME_SPENT_ON_PAGE_FILTER, handleFilterResults);





**Example 2**: The following example evaluates whether the user is from India or Australia:




  Copy Code



const USER_COUNTRY_FILTER = {
   id: 'USER_COUNTRY_FILTER_ID',
   filters: {
      filterType: 'OR',
      filters: [
         {
            field: 'userIPDetails.countryLong',
            filterType: 'IN',
            values: ['India', 'Australia'],
            id: 'USER_COUNTRY_IN_IND_AUS_ID'
         },
      ],
   },
};
const handleFilterResults = ({ data, error }) => {
   const { id, filters, results: { passed, values } } = data;
   // code
};
window.sprChat('addFilterToEvaluate', USER_COUNTRY_FILTER, handleFilterResults);





**Example 3**: The following example evaluates whether the user is not from cities like Mumbai or Delhi:




  Copy Code



const USER_CITY_FILTER = {
   id: 'USER_CITY_FILTER_ID',
   filters: {
      filterType: 'OR',
      filters: [
         {
            field: 'userIPDetails.city',
            filterType: 'NIN',
            values: ['Mumbai', 'Delhi'],
            id: 'USER_CITY_NIN_MUM_DEL_ID'
         },
      ],
   },
};
const handleFilterResults = ({ data, error }) => {
   const { id, filters, results: { passed, values } } = data;
   // code
};
window.sprChat('addFilterToEvaluate', USER_CITY_FILTER, handleFilterResults);





**Example 4**: The following example evaluates whether the user is reaching out to Live Chat during business hours:




  Copy Code



const BUSINESS_HOURS_FILTER = {
   id: 'BUSINESS_HOURS_FILTER_ID',
   filters: {
      filterType: 'OR',
      filters: [
         {
            field: 'BUSINESS_HOURS',
            filterType: 'IN',
            values: [true],
            id: 'BUSINESS_HOURS_ID',
          },
      ],
   },
};
const handleFilterResults = ({ data, error }) => {
   const { id, filters, results: { passed, values } } = data;
   // code
};
window.sprChat('addFilterToEvaluate', BUSINESS_HOURS_FILTER, handleFilterResults);





**Example 5**: The following example evaluates whether the number of available agents is greater than 0:




  Copy Code



const AVAILABLE_AGENTS_FILTER = {
   id: 'AVAILABLE_AGENTS_FILTER_ID',
   filters: {
      filterType: 'OR',
      filters: [
         {
            field: 'AVAILABLE_AGENTS',
            filterType: 'GT',
            values: [0],
            id: 'AVAILABLE_AGENTS_GT_0_ID'
        },
      ],
   },
};
const handleFilterResults = ({ data, error }) => {
   const { id, filters, results: { passed, values } } = data;
   // code
};
window.sprChat('addFilterToEvaluate', AVAILABLE_AGENTS_FILTER, handleFilterResults);





**Example 6**: The following example evaluates whether there are any active conversation present:




  Copy Code



const IS_CONVERSATION_OPEN_FILTER = {
   id: 'IS_CONVERSATION_OPEN_FILTER_ID',
   filters: {
      filterType: 'OR',
      filters: [
         {
            field: 'IS_CONVERSATION_OPEN',
            filterType: 'IN',
            values: [true],
            id: 'IS_CONVERSATION_OPEN_ID',          },
      ],
   },
});
const handleFilterResults = ({ data, error }) => {
   const { id, filters, results: { passed, values } } = data;
   // code
};
window.sprChat('addFilterToEvaluate', IS_CONVERSATION_OPEN_FILTER, handleFilterResults);





**Example 7**: The following example evaluates whether the number of conversations is greater than 0:




  Copy Code



const IS_CONVERSATION_OPEN_FILTER = {
   id: 'IS_CONVERSATION_OPEN_FILTER_ID',
   filters: {
      filterType: 'OR',
      filters: [
         {
            field: 'IS_CONVERSATION_OPEN',
            filterType: 'IN',
            values: [true],
            id: 'IS_CONVERSATION_OPEN_ID',          },
      ],
   },
});
const handleFilterResults = ({ data, error }) => {
   const { id, filters, results: { passed, values } } = data;
   // code
};
window.sprChat('addFilterToEvaluate', IS_CONVERSATION_OPEN_FILTER, handleFilterResults);






**Example 8**: The following example evaluates whether the number of conversations is greater than 0:




  Copy Code



const DOES_CONVERSATION_EXIST_FILTER = { 
    id: 'DOES_CONVERSATION_EXIST', 
    filters: { 
      filterType: 'OR', 
      filters: [ 
        { 
          field: 'DOES_CONVERSATION_EXIST', 
          filterType: 'GT', 
          values: [0], 
          id: 'DOES_CONVERSATION_EXIST_ID', 
        }, 
      ], 
    }, 
  }; 
  const handleFilterResults = ({ data, error }) => { 
    const { 
      results: { passed }, 
    } = data; 
     //code 
  }; 
  window.sprChat('addFilterToEvaluate', DOES_CONVERSATION_EXIST_FILTER, handleFilterResults);





[](https://dev.sprinklr.com/add-filter-to-evaluate-live-chat-state)

[Back to top](https://dev.sprinklr.com/add-filter-to-evaluate-live-chat-state)
