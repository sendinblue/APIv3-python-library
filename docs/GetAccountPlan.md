# GetAccountPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Displays the plan type of the user | 
**credits_type** | **str** | This is the type of the credit, \&quot;User Limit\&quot; or \&quot;Send Limit\&quot; are two possible types of credit of a user. \&quot;User Limit\&quot; implies the total number of subscribers you can add to your account, and \&quot;Send Limit\&quot; implies the total number of emails you can send to the subscribers in your account. | 
**credits** | **float** | Remaining credits of the user. This can either be \&quot;User Limit\&quot; or \&quot;Send Limit\&quot; depending on the plan. | 
**start_date** | **date** | Date of the period from which the plan will start (only available for \&quot;subscription\&quot;, \&quot;unlimited\&quot; and \&quot;reseller\&quot; plan type) | [optional] 
**end_date** | **date** | Date of the period from which the plan will end (only available for \&quot;subscription\&quot;, \&quot;unlimited\&quot; and \&quot;reseller\&quot; plan type) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


