# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the order. | 
**created_at** | **str** | Event occurrence UTC date-time (YYYY-MM-DDTHH:mm:ssZ), when order is actually created. | 
**updated_at** | **str** | Event updated UTC date-time (YYYY-MM-DDTHH:mm:ssZ), when the status of the order is actually changed/updated. | 
**status** | **str** | State of the order. | 
**amount** | **float** | Total amount of the order, including all shipping expenses, tax and the price of items. | 
**products** | [**list[OrderProducts]**](OrderProducts.md) |  | 
**email** | **str** | Email of the contact, Mandatory if \&quot;phone\&quot; field is not passed in \&quot;billing\&quot; parameter. | [optional] 
**billing** | [**OrderBilling**](OrderBilling.md) |  | [optional] 
**coupons** | **list[str]** | Coupons applied to the order. Stored case insensitive. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


