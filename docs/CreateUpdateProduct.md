# CreateUpdateProduct

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product ID for which you requested the details | 
**name** | **str** | Mandatory in case of creation**. Name of the product for which you requested the details | 
**url** | **str** | URL to the product | [optional] 
**image_url** | **str** | Absolute URL to the cover image of the product | [optional] 
**sku** | **str** | Product identifier from the shop | [optional] 
**price** | **float** | Price of the product | [optional] 
**categories** | **list[str]** | Category ID-s of the product | [optional] 
**parent_id** | **str** | Parent product id of the product | [optional] 
**meta_info** | **dict(str, str)** | Meta data of product such as description, vendor, producer, stock level. The size of cumulative metaInfo shall not exceed **1000 KB**. Maximum length of metaInfo object can be 10. | [optional] 
**update_enabled** | **bool** | Facilitate to update the existing category in the same request (updateEnabled &#x3D; true) | [optional] [default to False]
**deleted_at** | **str** | UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ) of the product deleted from the shop&#39;s database | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


