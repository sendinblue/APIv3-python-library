# UpdateExternalFeed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the feed | [optional] 
**url** | **str** | URL of the feed | [optional] 
**auth_type** | **str** | Auth type of the feed:   * &#x60;basic&#x60;   * &#x60;token&#x60;   * &#x60;noAuth&#x60;  | [optional] 
**username** | **str** | Username for authType &#x60;basic&#x60; | [optional] 
**password** | **str** | Password for authType &#x60;basic&#x60; | [optional] 
**token** | **str** | Token for authType &#x60;token&#x60; | [optional] 
**headers** | [**list[GetExternalFeedByUUIDHeaders]**](GetExternalFeedByUUIDHeaders.md) | Custom headers for the feed | [optional] 
**max_retries** | **int** | Maximum number of retries on the feed url | [optional] 
**cache** | **bool** | Toggle caching of feed url response | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


