# GetAccountPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Displays the plan type of the user | 
**credits_type** | **str** | This is the type of the credit, \&quot;Send Limit\&quot; is one of the possible types of credit of a user. \&quot;Send Limit\&quot; implies the total number of emails you can send to the subscribers in your account. | 
**credits** | **float** | Remaining credits of the user | 
**start_date** | **date** | Date of the period from which the plan will start (only available for \&quot;subscription\&quot; and \&quot;reseller\&quot; plan type) | [optional] 
**end_date** | **date** | Date of the period from which the plan will end (only available for \&quot;subscription\&quot; and \&quot;reseller\&quot; plan type) | [optional] 
**user_limit** | **int** | Only in case of reseller account. It implies the total number of child accounts you can add to your account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


