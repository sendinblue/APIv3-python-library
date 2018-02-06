# CreateContact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the user. Mandatory if &#x60;attributes.sms&#x60; is not passed | [optional] 
**attributes** | **object** | Values of the attributes to fill. The attributes must exist in you contact database | [optional] 
**email_blacklisted** | **bool** | Blacklist the contact for emails (emailBlacklisted &#x3D; true) | [optional] 
**sms_blacklisted** | **bool** | Blacklist the contact for SMS (smsBlacklisted &#x3D; true) | [optional] 
**list_ids** | **list[int]** | Ids of the lists to add the contact to | [optional] 
**update_enabled** | **bool** | Facilitate to update existing contact in same request (updateEnabled &#x3D; true) | [optional] [default to False]
**smtp_blacklist_sender** | **list[str]** | SMTP forbidden sender for contact. Use only for email Contact ( only available if updateEnabled &#x3D; true ) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


