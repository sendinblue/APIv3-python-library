# GetExtendedContactDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the contact for which you requested the details | 
**id** | **int** | ID of the contact for which you requested the details | 
**email_blacklisted** | **bool** | Blacklist status for email campaigns (true&#x3D;blacklisted, false&#x3D;not blacklisted) | 
**sms_blacklisted** | **bool** | Blacklist status for SMS campaigns (true&#x3D;blacklisted, false&#x3D;not blacklisted) | 
**modified_at** | **str** | Last modification date of the contact (YYYY-MM-DD HH:mm:ss) | 
**list_ids** | **list[int]** |  | 
**list_unsubscribed** | **list[int]** |  | [optional] 
**attributes** | **dict(str, str)** |  | 
**statistics** | [**GetExtendedContactDetailsStatistics**](GetExtendedContactDetailsStatistics.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


