# GetAllExternalFeedsFeeds

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the feed | 
**name** | **str** | Name of the feed | 
**url** | **str** | URL of the feed | 
**auth_type** | **str** | Auth type of the feed: * &#x60;basic&#x60; * &#x60;token&#x60; * &#x60;noAuth&#x60;  | 
**username** | **str** | Username for authType &#x60;basic&#x60; | [optional] 
**password** | **str** | Password for authType &#x60;basic&#x60; | [optional] 
**token** | **str** | Token for authType &#x60;token&#x60; | [optional] 
**headers** | [**list[GetExternalFeedByUUIDHeaders]**](GetExternalFeedByUUIDHeaders.md) | Custom headers for the feed | 
**max_retries** | **int** | Maximum number of retries on the feed url | 
**cache** | **bool** | Toggle caching of feed url response | 
**created_at** | **datetime** | Datetime on which the feed was created | 
**modified_at** | **datetime** | Datetime on which the feed was modified | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


