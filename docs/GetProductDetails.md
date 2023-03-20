# GetProductDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product ID for which you requested the details | 
**name** | **str** | Name of the product for which you requested the details | 
**created_at** | **str** | Creation UTC date-time of the product (YYYY-MM-DDTHH:mm:ss.SSSZ) | 
**modified_at** | **str** | Last modification UTC date-time of the product (YYYY-MM-DDTHH:mm:ss.SSSZ) | 
**url** | **str** | URL to the product | [optional] 
**image_url** | **str** | Absolute URL to the cover image of the product | [optional] 
**sku** | **str** | Product identifier from the shop | [optional] 
**price** | **float** | Price of the product | [optional] 
**categories** | **list[str]** | Category ID-s of the product | [optional] 
**parent_id** | **str** | Parent product id of the product | [optional] 
**s3_original** | **str** | S3 url of original image | [optional] 
**s3_thumb_analytics** | **str** | S3 thumbnail url of original image in 120x120 dimension for analytics section | 
**meta_info** | **object** | Meta data of product such as description, vendor, producer, stock level, etc. | [optional] 
**s3_thumb_editor** | **str** | S3 thumbnail url of original image in 600x400 dimension for editor section | 
**is_deleted** | **bool** | product deleted from the shop&#39;s database | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


